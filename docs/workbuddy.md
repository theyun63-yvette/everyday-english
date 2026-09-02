# Tencent WorkBuddy 安装

WorkBuddy 的自定义 Skill 通常包含 YAML 配置、实现文件和 README。由于不同版本的 Skill 配置字段可能调整，本适配包同时提供结构化文件和可重新生成的源提示词。

1. 解压 `everyday-english-workbuddy.zip`。
2. 在 WorkBuddy 中新建任务，输入：

   ```text
   Create a Tencent WorkBuddy skill from this folder. Preserve skill.yml metadata, use implementation/prompt.md as the core behavior, and include the references directory as supporting knowledge.
   ```

3. 将解压后的文件夹提供给该任务，并让 WorkBuddy生成或校准其当前版本所需的 Skill 文件。
4. 安装生成的 Skill，并在新会话中测试首次问候、难度匹配和 `/progress`。

`skill.yml` 是便于导入和校准的轻量清单；`implementation/prompt.md` 是完整、无外部依赖的教学提示词。若当前 WorkBuddy 版本重新生成了配置，应以其生成结果为准，但保留提示词和 references 内容。

官方参考：[WorkBuddy 创建自定义 Skills](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills)
