# 更新日志

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)，格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [0.1.0] - 2026-07-28

首个公开版本。

### 新增

- `md2wechat` 命令行工具：Markdown 文件 → 微信公众号排版 HTML
- 三套内置主题：`default`（清爽蓝）、`warm`（暖橙）、`ink`（墨黑极简）
- 全内联样式输出：标题、段落、引用、列表、表格、代码块、行内代码、分割线、图片
- 支持从标准输入读取、输出到标准输出，方便管道组合
- 支持作为 Python 库调用：`from md2wechat import convert`

[0.1.0]: https://github.com/baozizhuang/md2wechat/releases/tag/v0.1.0
