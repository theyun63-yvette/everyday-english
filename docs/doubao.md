# 豆包 / 火山方舟安装

## 火山方舟 Managed Agents

`everyday-english-doubao.zip` 已按包含 `SKILL.md` 和 `references/` 的 Skill 包生成：

1. 在火山方舟创建或打开一个智能体。
2. 选择豆包模型。
3. 在 Skills 配置中上传 `everyday-english-doubao.zip`。
4. 启用 Skill 后，用首次开场语测试新会话。

## 不支持 Skill ZIP 的豆包入口

安装包还包含：

- `system-prompt.md`：可复制到智能体的人设或系统提示词；
- `opening-message.md`：固定首次开场语。

如果使用扣子或其他豆包智能体平台，把 `system-prompt.md` 作为核心提示词，并将 `references/` 中的文档加入知识库或上下文。不要将平台原生记忆当作必需条件；跨会话进度仍可使用 `/progress` 摘要。

官方参考：[火山方舟 Skills 管理](https://www.volcengine.com/docs/82379/2161690) · [AgentKit Skills](https://www.volcengine.com/docs/84458/2335446)
