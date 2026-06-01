# Project Quickstart Skill 中文说明

这是一个 Codex Skill，目标是帮助学生、求职者和新贡献者快速理解陌生的软件项目。

它会引导 Agent 先阅读仓库结构、依赖、入口文件、核心流程和测试信息，再生成适合学习、面试和简历表达的项目速查资料。同时，它会要求 Agent 标注证据来源和验证状态，避免把没有确认过的内容说得过满。

## 它能产出什么

- 项目一句话总结
- 架构和核心流程说明
- Mermaid 架构图或流程图
- 建议优先阅读的关键文件
- 关键结论的证据表
- 项目优点、风险和改进方向
- 面试或简历表达要点
- 已验证内容、未验证内容和不确定点

## 安装

先克隆这个仓库，然后把 Skill 文件夹复制到 Codex 的 skills 目录。

Windows PowerShell:

```powershell
git clone https://github.com/ZYZ666-RGB/project-quickstart-skill.git
$skillsDir = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills" } else { Join-Path $HOME ".codex\skills" }
New-Item -ItemType Directory -Force $skillsDir
Copy-Item -Recurse .\project-quickstart-skill\project-quickstart $skillsDir
```

macOS/Linux:

```bash
git clone https://github.com/ZYZ666-RGB/project-quickstart-skill.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R project-quickstart-skill/project-quickstart "${CODEX_HOME:-$HOME/.codex}/skills/"
```

如果安装后 Codex 没有立刻识别这个 Skill，可以重启 Codex。

## 使用方式

显式调用：

```text
Use $project-quickstart to help me understand this repository and prepare an interview-ready project brief.
```

自然语言触发示例：

```text
帮我快速理解这个项目，我面试要讲。
```

```text
我刚 clone 了这个仓库，应该先看哪些文件？
```

```text
帮我把这个项目整理成简历项目经历，并列出技术亮点。
```

## 仓库结构

```text
project-quickstart/
+-- SKILL.md
+-- agents/openai.yaml
+-- assets/project-brief-template.md
+-- evals/routing-cases.yaml
+-- references/output-rubric.md
+-- scripts/repo_snapshot.py
```

## 关键文件说明

- `project-quickstart/SKILL.md`：Skill 的触发描述和核心工作流。
- `project-quickstart/references/output-rubric.md`：项目分析报告的质量标准。
- `project-quickstart/assets/project-brief-template.md`：可复用的项目速查文档模板。
- `project-quickstart/evals/routing-cases.yaml`：正例、负例和边界路由测试用例。
- `project-quickstart/scripts/repo_snapshot.py`：快速扫描仓库结构的辅助脚本。

## Evals

路由和行为测试用例在：

```text
project-quickstart/evals/routing-cases.yaml
```

建议用同一组用例在不同模型或平台上测试：

- 正例：应该加载这个 Skill。
- 负例：不应该加载这个 Skill。
- 边界例：观察路由是否稳定。

如果正例不触发，可以收窄或补充 `SKILL.md` 的 description。  
如果负例误触发，优先修改 description，避免 Skill 变得太宽。

## 适合谁

- 想快速读懂开源项目的大学生
- 准备面试或简历项目的求职者
- 刚加入项目的新贡献者
- 想把“项目理解流程”沉淀成可复用方法的人

## License

MIT
