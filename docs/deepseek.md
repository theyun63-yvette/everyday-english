# DeepSeek 安装与使用

## DeepSeek Harness

解压 `everyday-english-deepseek.zip`，把：

```text
harness/.agents/skills/everyday-english
```

复制到项目的：

```text
.agents/skills/everyday-english
```

DeepSeek Harness 可以从 `.agents/skills/` 发现符合 Agent Skills 结构的技能。完成后在新会话中调用 `everyday-english`。

## DeepSeek API

安装包的 `api/` 中包含：

- `system-prompt.md`：由核心 Skill 和四份参考资料合并生成；
- `api-example.py`：仅使用 Python 标准库的最小调用示例。

设置 API Key 后运行：

```bash
export DEEPSEEK_API_KEY="your-key"
python3 api/api-example.py
```

API 示例不会永久保存学习记录。需要跨会话继续时，请将 `/progress` 生成的摘要存入自己的应用，并在下一次请求中作为上下文提供。

官方参考：[DeepSeek Harness](https://www.deepseek.com/harness/en/) · [DeepSeek API 示例](https://api-docs.deepseek.com/api_samples/chat_curl/)
