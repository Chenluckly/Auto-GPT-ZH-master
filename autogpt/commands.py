import json
import datetime
import autogpt.agent_manager as agents
from autogpt.config import Config
from autogpt.json_parser import fix_and_parse_json
from autogpt.image_gen import generate_image
from duckduckgo_search import ddg
from autogpt.ai_functions import evaluate_code, improve_code, write_tests
from autogpt.browse import scrape_links, scrape_text, summarize_text
from autogpt.execute_code import execute_python_file, execute_shell
from autogpt.file_operations import (
    append_to_file,
    delete_file,
    read_file,
    search_files,
    write_to_file,
)
from autogpt.memory import get_memory
from autogpt.speak import say_text
from autogpt.web import browse_website


cfg = Config()


def is_valid_int(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_command(response):
    """Parse the response and return the command name and arguments"""
    try:
        response_json = fix_and_parse_json(response)

        if "command" not in response_json:
            return "Error:","JSON 中缺少'command'对象"

        if not isinstance(response_json, dict):
            return "Error:", f"'response_json' 对象不是字典 {response_json}"

        command = response_json["command"]
        if not isinstance(command, dict):
            return "Error:", "'command' 对象不是字典"

        if "name" not in command:
            return "Error:", "'command'对象中缺少'name'字段 "

        command_name = command["name"]

        # Use an empty dictionary if 'args' field is not present in 'command' object
        arguments = command.get("args", {})

        return command_name, arguments
    except json.decoder.JSONDecodeError:
        return "Error:", "无效的 JSON"
    # All other errors, return "Error: + error message"
    except Exception as e:
        return "Error:", str(e)


def execute_command(command_name, arguments):
    """Execute the command and return the result"""
    memory = get_memory(cfg)

    try:
        if command_name == "google":
            # Check if the Google API key is set and use the official search method
            # If the API key is not set or has only whitespaces, use the unofficial
            # search method
            key = cfg.google_api_key
            if key and key.strip() and key != "your-google-api-key":
                return google_official_search(arguments["input"])
            else:
                return google_search(arguments["input"])
        elif command_name == "memory_add":
            return memory.add(arguments["string"])
        elif command_name == "start_agent":
            return start_agent(
                arguments["name"], arguments["task"], arguments["prompt"]
            )
        elif command_name == "message_agent":
            return message_agent(arguments["key"], arguments["message"])
        elif command_name == "list_agents":
            return list_agents()
        elif command_name == "delete_agent":
            return delete_agent(arguments["key"])
        elif command_name == "get_text_summary":
            return get_text_summary(arguments["url"], arguments["question"])
        elif command_name == "get_hyperlinks":
            return get_hyperlinks(arguments["url"])
        elif command_name == "read_file":
            return read_file(arguments["file"])
        elif command_name == "write_to_file":
            return write_to_file(arguments["file"], arguments["text"])
        elif command_name == "append_to_file":
            return append_to_file(arguments["file"], arguments["text"])
        elif command_name == "delete_file":
            return delete_file(arguments["file"])
        elif command_name == "search_files":
            return search_files(arguments["directory"])
        elif command_name == "browse_website":
            return browse_website(arguments["url"], arguments["question"])
        # TODO: Change these to take in a file rather than pasted code, if
        # non-file is given, return instructions "Input should be a python
        # filepath, write your code to file and try again"
        elif command_name == "evaluate_code":
            return evaluate_code(arguments["code"])
        elif command_name == "improve_code":
            return improve_code(arguments["suggestions"], arguments["code"])
        elif command_name == "write_tests":
            return write_tests(arguments["code"], arguments.get("focus"))
        elif command_name == "execute_python_file":  # Add this command
            return execute_python_file(arguments["file"])
        elif command_name == "execute_shell":
            if cfg.execute_local_commands:
                return execute_shell(arguments["command_line"])
            else:
                return (
                    "你不允许运行本地 shell 命令。要执行 shell 命令，必须在配置文件中将 EXECUTE_LOCAL_COMMANDS 设置为 'True'。不要尝试绕过此限制。"
                )
        elif command_name == "generate_image":
            return generate_image(arguments["prompt"])
        elif command_name == "do_nothing":
            return "No action performed."
        elif command_name == "task_complete":
            shutdown()
        else:
            return f"未知的命令 '{command_name}'. 请参阅“COMMANDS”列表以获取可用命令,并仅以指定的 JSON 格式响应。"
    # All errors, return "Error: + error message"
    except Exception as e:
        return "Error: " + str(e)


def get_datetime():
    """Return the current date and time"""
    return "当前日期和时间: " + datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def google_search(query, num_results=8):
    """Return the results of a google search"""
    search_results = []
    if not query:
        return json.dumps(search_results)

    for j in ddg(query, max_results=num_results):
        search_results.append(j)

    return json.dumps(search_results, ensure_ascii=False, indent=4)


def google_official_search(query, num_results=8):
    """Return the results of a google search using the official Google API"""
    import json

    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError

    try:
        # Get the Google API key and Custom Search Engine ID from the config file
        api_key = cfg.google_api_key
        custom_search_engine_id = cfg.custom_search_engine_id

        # Initialize the Custom Search API service
        service = build("customsearch", "v1", developerKey=api_key)

        # Send the search query and retrieve the results
        result = (
            service.cse()
            .list(q=query, cx=custom_search_engine_id, num=num_results)
            .execute()
        )

        # Extract the search result items from the response
        search_results = result.get("items", [])

        # Create a list of only the URLs from the search results
        search_results_links = [item["link"] for item in search_results]

    except HttpError as e:
        # Handle errors in the API call
        error_details = json.loads(e.content.decode())

        # Check if the error is related to an invalid or missing API key
        if error_details.get("error", {}).get(
            "code"
        ) == 403 and "invalid API key" in error_details.get("error", {}).get(
            "message", ""
        ):
            return "Error: 提供的 Google API Key无效."
        else:
            return f"Error: {e}"

    # Return the list of search result URLs
    return search_results_links


def get_text_summary(url, question):
    """Return the results of a google search"""
    text = scrape_text(url)
    summary = summarize_text(url, text, question)
    return """ "结果" : """ + summary


def get_hyperlinks(url):
    """Return the results of a google search"""
    return scrape_links(url)


def shutdown():
    """Shut down the program"""
    print("关机中...")
    quit()


def start_agent(name, task, prompt, model=cfg.fast_llm_model):
    """Start an agent with a given name, task, and prompt"""
    # Remove underscores from name
    voice_name = name.replace("_", " ")
    first_message = f"""你是 {name}.  回应: "Acknowledged". 中文版来自自阿杰，公众号内获取最新代码《阿杰的人生路》"""
    agent_intro = f"{voice_name} 在这里，向您报到！"

    # Create agent
    if cfg.speak_mode:
        say_text(agent_intro, 1)
    key, ack = agents.create_agent(task, first_message, model)

    if cfg.speak_mode:
        say_text(f"Hello {voice_name}.你的任务如下. {task}.")

    # Assign task (prompt), get response
    agent_response = agents.message_agent(key, prompt)

    return f"Agent {name} created with key {key}. First response: {agent_response}"


def message_agent(key, message):
    """Message an agent with a given key and message"""
    # Check if the key is a valid integer
    if is_valid_int(key):
        agent_response = agents.message_agent(int(key), message)
    # Check if the key is a valid string
    elif isinstance(key, str):
        agent_response = agents.message_agent(key, message)
    else:
        return "无效的Key, 必须是整数或字符串."

    # Speak response
    if cfg.speak_mode:
        say_text(agent_response, 1)
    return agent_response


def list_agents():
    """List all agents"""
    return list_agents()


def delete_agent(key):
    """Delete an agent with a given key"""
    result = agents.delete_agent(key)
    return f"Agent {key} deleted." if result else f"Agent {key} does not exist."
