# 参与贡献

感谢你愿意为 md2wechat 出一份力！项目还很小，任何帮助都欢迎。

## 可以做什么

- **提 Issue**：排版 bug、新主题需求、新功能想法，直接开 issue 描述即可，最好附上能复现的 Markdown 片段
- **加主题**：主题就是一组内联样式定义，见 `src/md2wechat/themes.py`，照着现有主题抄一份改一改就是贡献
- **修 bug / 加功能**：Fork → 分支 → PR，下面有流程

## 开发环境

```bash
git clone https://github.com/baozizhuang/md2wechat.git
cd md2wechat
python -m venv .venv && source .venv/bin/activate
pip install -e .
md2wechat examples/example.md   # 应该能正常生成 HTML
```

## 提交 PR 的约定

1. 一个 PR 只做一件事
2. 新主题请附上粘贴进公众号编辑器后的效果截图
3. 提交信息用中文或英文都行，说清楚"做了什么、为什么"
4. 代码尽量保持无类型魔法、无重依赖——本项目定位是"装完即用的小工具"

## 行为准则

就一条：对事不对人，好好说话。
