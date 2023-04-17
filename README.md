# Auto-GPT：自主 GPT-4 实验

> 这里是Auto-GPT中文项目- 同步fork Auto-GPT   Auto-GPT修改了分支规则，Fork同步于Stable最新分支

![gzh](gzh.png)

### 公众号内回复"Auto-GPT"加入群聊，共同探讨更多玩法

### 中文版Demo :

![Demo video](https://raw.githubusercontent.com/kaqijiang/Auto-GPT-ZH/master/demo.gif)

Auto-GPT 是一个实验性开源应用程序，展示了 GPT-4 语言模型的功能。该程序由 GPT-4 驱动，将 LLM 的“思想”链接在一起，以自主实现您设定的任何目标。作为 GPT-4 完全自主运行的首批示例之一，Auto-GPT 突破了 AI 的可能性界限。

## 可以做什么？

> 这里引用量子位的介绍

**自主人工智能**：它所具备的能力主打的就是一个“自主”，**完全不用人类插手**的那种！

**例如：**一位网友就要求AutoGPT开发一个网站，结果不到3分钟，AI自己就用React和Tailwind CSS“唰唰唰”地搞定了。

AI自己上网、自己使用第三方工具、自己思考、自己操作你的电脑。

**例如：**给他下达一个任务，用100美元的资金创建一个新的创业公司。

AgentGPT在接到这项任务之后，便开始了他的展示：

- 思考中……
- 添加任务：研究需要最少资金的低成本商业模式。
- 添加任务：确定潜在的目标市场及其需求。
- 添加任务：开发一个精简的MVP（最小可行产品），并在目标市场进行测试以验证需求。
- 思考中……

然后AgentGPT先是输出执行“研究需要最少资金的低成本商业模式”的结果：

> 根据我的研究，一些需要最少资金的低成本商业模式包括：
>
> 1、Dropshipping：通过Dropshipping，你可以在网上销售产品而无需持有库存。您只需通过第三方供应商完成订单，第三方供应商将产品直接运送给您的客户。你可以从50美元开始支付网站托管和域名注册费。
>
> 2、 社交媒体营销：如果你有社交媒体营销的天赋，你可以通过帮助企业接触他们的目标受众来创办自己的代理公司。你所需要的只是一台电脑，互联网连接，以及一些社交媒体营销的经验和技能，而你的起价只有50美元或更少。
>
> 3、活动策划：如果你对组织活动有热情，你可以开始自己的活动策划业务。你可以从策划一些小活动开始，比如生日派对、婚礼等等。你可以从100美元开始，创建一个简单的网站，名片，并通过社交媒体营销自己。
>
> 4、自由写作：如果你有写作天赋，你可以开始自己的自由写作事业。你可以通过在线平台，如Upwork、Fiver和其他求职网站找到客户。只需50美元，你就可以创建一个投资组合网站，并通过社交媒体营销自己。
>
> 这些只是一些低成本的商业模式，你只需要100美元的资金就可以考虑。选择一个符合你的技能和兴趣的商业模式是很重要的。

到这还没有完，AgentGPT会继续开始它的工作：

- 思考中……
- 添加任务：针对每种已确定的低成本商业模式，对潜在的产品或服务想法进行头脑风暴。
- 添加任务：评估每个想法的潜在盈利能力和可扩展性。
- 添加任务：选择最有希望的想法，并开发精益MVP，用于目标市场的测试。

而后便是继续地再思考、执行。

## 📋 要求

- 环境(选择一个就行)
  - [vscode + devcontainer](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers): 已经配置在.devcontainer文件夹下，可以直接使用
  - [Python 3.8 或者更高](https://www.tutorialspoint.com/how-to-install-python-in-windows)
- [OpenAI API key](https://platform.openai.com/account/api-keys)

可选的:

- [PINECONE API key](https://www.pinecone.io/)（如果你想要 Pinecone 支持存储日志，默认本地就行）

- [ElevenLabs Key](https://elevenlabs.io/) (如果你想让人工智能说话)

## 💾 安装方法

要安装 Auto-GPT，请按照下列步骤操作：

1. 确保满足上述所有**要求**，如果没有，请安装/获取它们。

以下命令需要在终端执行

2. 克隆存储库：对于此步骤，您需要安装 Git，但您可以通过单击此页面顶部的按钮来下载 zip 文件☝️

```
git clone git@github.com:kaqijiang/Auto-GPT-ZH.git
```

3. 终端中 cd到项目目录

```
cd 'Auto-GPT-ZH'
```

4. 终端中安装所需的依赖项

```
pip install -r requirements.txt
```

5. 重命名`.env.template`为`.env`并填写您的`OPENAI_API_KEY`. 如果您打算使用语音模式，请`ELEVEN_LABS_API_KEY`也填写您的。

  - 从以下网址获取您的 OpenAI API 密钥： https: [//platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)。
  - 从[https://elevenlabs.io](https://elevenlabs.io/)获取您的 ElevenLabs API 密钥。您可以使用网站上的“个人资料”选项卡查看您的 xi-api-key。

## 终端代理方法

推荐工具：[【稳定，高速梯子推荐56一年，活动时5折，点击直达】](https://www.hjtnt.pro/auth/register?code=QRY5)

Mac 下载 [ClashX Pro](https://install.appcenter.ms/users/clashx/apps/clashx-pro/distribution_groups/public) 设置 系统代理 增强模式 然后复制终端代理命令 在终端中输入，重启即可

根据自己的工具修改对应的端口

```
export https_proxy=http://127.0.0.1:8484 http_proxy=http://127.0.0.1:8484 all_proxy=socks5://127.0.0.1:8484
```

Windows 下载 [Clash for Windows](https://wws.lanzoux.com/iCEgLj27fra)，设置 系统代理 ，在终端中输入，重启即可。

根据自己的工具修改对应的端口

```
# 使用 http 类型代理
set http_proxy=http://127.0.0.1:8484
set https_proxy=http://127.0.0.1:8484
# 使用 socks 类型代理
netsh winhttp set proxy proxy-server="socks=127.0.0.1:8484" bypass-list="localhost"
netsh winhttp show proxy
netsh winhttp reset proxy
# 使用 socks 类型代理
set http_proxy=socks5://127.0.0.1:8484
set https_proxy=socks5://127.0.0.1:8484
```

## 🔧 用法

1. 在终端中运行 `main.py` 

```
python -m autogpt
```

2. 在 AUTO-GPT 的每个操作之后，输入“y”来授权命令，“y -N”来运行 N 个连续命令，“n”来退出程序，或者为 AI 输入额外的反馈。

### 日志

您将在文件夹中找到活动和错误日志`./output/logs`

输出调试日志：

```
python -m autogpt --debug
```

### 命令行参数

以下是您在运行 Auto-GPT 时可以使用的一些常见参数：

> 将尖括号 (<>) 中的任何内容替换为您要指定的值

- `python scripts/main.py --help`查看所有可用命令行参数的列表。
- `python scripts/main.py --ai-settings <filename>`使用不同的 AI 设置文件运行 Auto-GPT。
- `python scripts/main.py --use-memory  <memory-backend>`指定 3 个内存后端之一：`local`、`redis`或`pinecone`'no_memory'。

> **注意**：其中一些标志有简写形式，`-m`例如`--use-memory`. 用于`python scripts/main.py --help`获取更多信息

## 🗣️ 语音模式

使用它来将 TTS 用于 Auto-GPT

```
python -m autogpt --speak
```

## 🔍 谷歌 API 密钥配置

此部分是可选的，如果您在运行谷歌搜索时遇到错误 429 问题，请使用官方谷歌 API。要使用该`google_official_search`命令，您需要在环境变量中设置 Google API 密钥。

1. 转到[谷歌云控制台](https://console.cloud.google.com/)。
2. 如果您还没有帐户，请创建一个并登录。
3. 通过单击页面顶部的“选择项目”下拉菜单并单击“新建项目”来创建一个新项目。给它起个名字，然后单击“创建”。
4. 转到[API 和服务仪表板](https://console.cloud.google.com/apis/dashboard)并单击“启用 API 和服务”。搜索“自定义搜索 API”并单击它，然后单击“启用”。
5. 转到[凭据](https://console.cloud.google.com/apis/credentials)页面并单击“创建凭据”。选择“API 密钥”。
6. 复制 API 密钥并将其设置为在您的计算机上命名的环境变量`GOOGLE_API_KEY`。请参阅下面的设置环境变量。
7. 转到[自定义搜索引擎](https://cse.google.com/cse/all)页面并单击“添加”。
8. 按照提示设置搜索引擎。您可以选择搜索整个网络或特定站点。
9. 创建搜索引擎后，单击“控制面板”，然后单击“基本”。复制“搜索引擎 ID”并将其设置为`CUSTOM_SEARCH_ENGINE_ID`在您的计算机上命名的环境变量。请参阅下面的设置环境变量。

*请记住，您的每日免费自定义搜索配额最多只允许 100 次搜索。要增加此限制，您需要为项目分配一个计费帐户，以从每天多达 10,000 次搜索中获利。*

### 设置环境变量

对于 Windows 用户：

```
setx GOOGLE_API_KEY "YOUR_GOOGLE_API_KEY"
setx CUSTOM_SEARCH_ENGINE_ID "YOUR_CUSTOM_SEARCH_ENGINE_ID"

```

对于 macOS 和 Linux 用户：

```
export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
export CUSTOM_SEARCH_ENGINE_ID="YOUR_CUSTOM_SEARCH_ENGINE_ID"
```

## 🌲 Pinecone API 密钥设置

Pinecone 支持存储大量基于向量的内存，允许在任何给定时间只为代理加载相关内存。

1. 如果您还没有帐户，请前往[pinecone并创建一个帐户。](https://app.pinecone.io/)
2. 选择`Starter`计划以避免被收费。
3. 在左侧边栏的默认项目下找到您的 API 密钥和区域。

### 设置环境变量

只需在文件中设置它们`.env`。

或者，您可以从命令行设置它们（高级）：

对于 Windows 用户：

```
setx PINECONE_API_KEY "YOUR_PINECONE_API_KEY"
setx PINECONE_ENV "Your pinecone region" # something like: us-east4-gcp
```

对于 macOS 和 Linux 用户：

```
export PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
export PINECONE_ENV="Your pinecone region" # something like: us-east4-gcp
```

## 设置缓存类型

默认情况下，Auto-GPT 将使用 LocalCache 而不是 Redis 或 Pinecone。

要切换到任何一个，请将`MEMORY_BACKEND`env 变量更改为您想要的值：

`local`（默认）使用本地 JSON 缓存文件 `pinecone`使用您在 ENV 设置中配置的 Pinecone.io 帐户 `redis`将使用您配置的 redis 缓存

## 查看内存使用情况

1. 使用`--debug`标志查看内存使用情况:)

## 🧠内存预填充

```
# python scripts/data_ingestion.py -h 
usage: data_ingestion.py [-h] (--file FILE | --dir DIR) [--init] [--overlap OVERLAP] [--max_length MAX_LENGTH]

Ingest a file or a directory with multiple files into memory. Make sure to set your .env before running this script.

options:
  -h, --help               show this help message and exit
  --file FILE              The file to ingest.
  --dir DIR                The directory containing the files to ingest.
  --init                   Init the memory and wipe its content (default: False)
  --overlap OVERLAP        The overlap size between chunks when ingesting files (default: 200)
  --max_length MAX_LENGTH  The max_length of each chunk when ingesting files (default: 4000

# python scripts/data_ingestion.py --dir seed_data --init --overlap 200 --max_length 1000
```

这个位于 scripts/data_ingestion.py 的脚本允许您将文件导入内存并在运行 Auto-GPT 之前进行预填充。

内存预填充是一种技术，它涉及将相关文档或数据输入到人工智能的内存中，以便它可以利用这些信息生成更具见解和准确性的响应。

为了预填充内存，每个文档的内容被分成指定最大长度和指定重叠之间的块，然后将每个块添加到在 .env 文件中设置的内存后端。当需要 AI 回忆信息时，它可以访问那些预填充的记忆来生成更具见解和准确性的响应。

当需要处理大量数据或需要快速访问特定信息时，这种技术特别有用。通过预填充内存，AI 可以更有效地检索和使用这些信息，节省时间和 API 调用，并提高其响应的准确性。

例如，您可以在运行 Auto-GPT 之前下载 API 文档、Github 存储库等，并将其导入内存。

⚠️如果您使用 Redis 作为内存，请确保在 .env 文件中将 WIPE_REDIS_ON_START 设置为 False 来运行 Auto-GPT。

⚠️对于其他内存后端，我们目前在启动 Auto-GPT 时强制擦除内存。要使用这些内存后端摄取数据，您可以在 Auto-GPT 运行期间随时调用 data_ingestion.py 脚本。

一旦文件被导入内存，这些记忆将立即对 AI 可用，即使在 Auto-GPT 运行时导入也是如此。

在上面的示例中，该脚本初始化内存，将 seed_data 目录中的所有文件导入内存，并将块之间的重叠设置为 200，每个块的最大长度为 4000。请注意，您也可以使用 --file 参数将单个文件导入内存，并且该脚本将只导入 auto_gpt_workspace 目录中的文件。

您可以调整 max_length 和 overlap 参数，以微调当 AI“回忆”该内存时向其展示文档的方式：

- 增加 overlap 值可以使 AI 从每个块中访问更多的上下文信息，但这会导致创建更多的块，因此会增加内存后端使用和 OpenAI API 请求的次数。 
- 减少 max_length 值会创建更多的块，这可以通过在上下文中允许更多的消息历史记录来节省提示令牌，但也会增加块的数量。 
- 增加 max_length 值将向 AI 提供更多的上下文信息，减少创建的块数，并在 OpenAI API 请求上节省。然而，这可能会使用更多的提示令牌，并减少 AI 可用的总上下文。

## 连续模式⚠️

**无需**用户授权即可 100% 自动化地运行 AI 。不推荐连续模式。它具有潜在危险，可能会导致您的 AI 永远运行或执行您通常不会授权的操作。使用风险自负。

1. `main.py`在终端中运行Python 脚本：

```
python -m autogpt --continuous
python -m autogpt --speak --continuous #带语音
```

2.要退出程序，请按 Ctrl + C

## GPT3.5 ONLY 模式 

如果您无权访问 GPT4 api，此模式将允许您使用 Auto-GPT！

```
python -m autogpt --gpt3only
python -m autogpt --speak --gpt3only #带语音
```

建议将虚拟机用于需要高度安全措施的任务，以防止对主计算机的系统和数据造成任何潜在危害。

## 🖼 图像生成

默认情况下，Auto-GPT 使用 DALL-e 进行图像生成。要使用 Stable Diffusion，需要一个[HuggingFace API 令牌。](https://huggingface.co/settings/tokens)

获得令牌后，将这些变量设置为`.env`：

```
IMAGE_PROVIDER=sd
HUGGINGFACE_API_TOKEN="YOUR_HUGGINGFACE_API_TOKEN"
```

## ⚠️ 限制

该实验旨在展示 GPT-4 的潜力，但存在一些局限性：

1. 不是完善的应用程序或产品，只是一个实验
2. 在复杂的真实业务场景中可能表现不佳。事实上，如果确实如此，请分享您的结果！
3. 运行成本非常高，因此请使用 OpenAI 设置和监控您的 API 密钥限制！

## 🛡 免责声明

免责声明 Auto-GPT 这个项目是一个实验性应用程序，按“原样”提供，没有任何明示或暗示的保证。使用本软件，即表示您同意承担与其使用相关的所有风险，包括但不限于数据丢失、系统故障或可能出现的任何其他问题。

本项目的开发者和贡献者对因使用本软件而可能发生的任何损失、损害或其他后果不承担任何责任或义务。您对基于 Auto-GPT 提供的信息做出的任何决定和行动承担全部责任。

**请注意，由于使用代币，使用 GPT-4 语言模型可能会很昂贵。**通过使用此项目，您承认您有责任监控和管理您自己的代币使用情况和相关费用。强烈建议定期检查您的 OpenAI API 使用情况并设置任何必要的限制或警报以防止意外收费。

作为一项自主实验，Auto-GPT 可能会生成不符合现实世界商业惯例或法律要求的内容或采取的行动。您有责任确保基于此软件的输出做出的任何行动或决定符合所有适用的法律、法规和道德标准。本项目的开发者和贡献者对因使用本软件而产生的任何后果不承担任何责任。

通过使用 Auto-GPT，您同意就任何和所有索赔、损害、损失、责任、成本和费用（包括合理的律师费）对开发人员、贡献者和任何关联方进行赔偿、辩护并使其免受损害因您使用本软件或您违反这些条款而引起的。