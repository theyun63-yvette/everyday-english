# Codex 安装

## 使用 ZIP

1. 下载并解压 `everyday-english-codex.zip`。
2. 将其中的 `everyday-english` 文件夹放到：

   ```text
   ~/.codex/skills/everyday-english
   ```

3. 新建或刷新 Codex 任务。
4. 输入 `$everyday-english`，或直接提出英语陪练、语法纠错、角色扮演等需求。

## 使用 Git

```bash
git clone https://github.com/theyun63-yvette/everyday-english.git ~/.codex/skills/everyday-english
```

`agents/openai.yaml` 是 Codex 的界面元数据。核心教学逻辑位于 `SKILL.md` 和 `references/`。
