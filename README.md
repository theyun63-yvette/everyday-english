# Everyday English 👋

一个轻松、耐心，但会认真指出问题的日常英语教练。

我做它的出发点很简单：**学英语不应该一直停留在“我懂”，而是要慢慢变成“我能说出来”。** 它会陪你聊天、模拟真实场景，在不打断表达的前提下纠正关键错误，并把值得复习的内容整理下来。

## 它能做什么

- 💬 日常聊天与口语陪练
- 🎭 旅行、购物、工作闲聊等情景角色扮演
- ✍️ 区分“语法错误”和“正确但不自然”
- 🧠 根据真实错误安排语法练习和主动复习
- 📈 按 beginner、intermediate、advanced 调整难度
- 📝 生成可复制到下一次对话的学习记录

## 支持的平台

| 平台 | 使用方式 |
|---|---|
| Codex | 原生 Skill，直接安装 |
| Claude / Claude Code | Agent Skills 格式，直接安装 |
| DeepSeek Harness | Agent Skills 格式，直接安装 |
| DeepSeek API | 使用合并后的 system prompt 和示例脚本 |
| 豆包 / 火山方舟 | 上传 Skill ZIP，或复制 system prompt 配置智能体 |
| Tencent WorkBuddy | 使用适配包创建自定义 Skill |

各平台安装说明：

- [Codex](docs/codex.md)
- [Claude / Claude Code](docs/claude.md)
- [DeepSeek](docs/deepseek.md)
- [豆包 / 火山方舟](docs/doubao.md)
- [Tencent WorkBuddy](docs/workbuddy.md)

Release 和 Actions 构建产物提供独立 ZIP 安装包。

## 最快开始

Codex：

```bash
git clone https://github.com/theyun63-yvette/everyday-english.git ~/.codex/skills/everyday-english
```

Claude Code：

```bash
git clone https://github.com/theyun63-yvette/everyday-english.git ~/.claude/skills/everyday-english
```

然后输入：

```text
$everyday-english
```

也可以自然地说：

```text
和我练习周末计划，聊天过程中先别频繁打断我。
```

## 安装包

运行下面的命令可在 `dist/` 生成六个版本：

```bash
python3 scripts/build_packages.py
```

- `everyday-english-agent-skill.zip`
- `everyday-english-codex.zip`
- `everyday-english-claude.zip`
- `everyday-english-deepseek.zip`
- `everyday-english-doubao.zip`
- `everyday-english-workbuddy.zip`

## 常用命令

`/chat` · `/roleplay` · `/grammar` · `/review` · `/correct` · `/summary` · `/progress`

默认从轻松对话开始。说错没关系，先把真正想说的话说出来。
