# Claude / Claude Code 安装

本项目的 `SKILL.md` 和 `references/` 遵循 Agent Skills 的渐进式加载结构。

## Claude Code 个人安装

将 Claude 安装包中的 `everyday-english` 文件夹复制到：

```text
~/.claude/skills/everyday-english
```

## Claude Code 项目安装

将同一个文件夹复制到项目内：

```text
<project>/.claude/skills/everyday-english
```

个人安装适合所有项目；项目安装适合随仓库共享。重新开始会话后，可显式调用 `$everyday-english`，也可以直接提出匹配的英语学习请求。

`agents/openai.yaml` 不包含在 Claude 安装包中，因为它只服务于 Codex 界面。

官方参考：[Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) · [Claude Code Skills](https://code.claude.com/docs/en/skills)
