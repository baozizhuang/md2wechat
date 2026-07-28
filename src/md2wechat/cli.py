"""md2wechat 命令行入口。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .converter import convert
from .themes import DEFAULT_THEME, THEMES


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="md2wechat",
        description="把 Markdown 转成可直接粘贴进微信公众号编辑器的排版 HTML（全内联样式，不丢格式）。",
    )
    parser.add_argument("input", nargs="?", help="Markdown 文件路径；省略则从标准输入读取")
    parser.add_argument("-o", "--output", help="输出 HTML 路径，默认 <输入文件名>.wechat.html；从标准输入读取时默认打印到屏幕")
    parser.add_argument("-t", "--theme", default=DEFAULT_THEME, help=f"主题，可选：{', '.join(THEMES)}（默认 {DEFAULT_THEME}）")
    parser.add_argument("--list-themes", action="store_true", help="列出全部主题后退出")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)

    if args.list_themes:
        for name, theme in THEMES.items():
            mark = "（默认）" if name == DEFAULT_THEME else ""
            print(f"{name}{mark} — {theme['description']}")
        return 0

    if args.theme not in THEMES:
        print(f"未知主题：{args.theme}（可用：{', '.join(THEMES)}）", file=sys.stderr)
        return 2

    out: Path | None = None
    if args.input:
        src = Path(args.input)
        text = src.read_text(encoding="utf-8")
        out = Path(args.output) if args.output else src.with_suffix(".wechat.html")
    else:
        text = sys.stdin.read()
        if args.output:
            out = Path(args.output)

    html = convert(text, args.theme)

    if out is None:
        print(html)
        return 0

    out.write_text(html, encoding="utf-8")
    print(f"已生成：{out}（主题：{args.theme}）")
    print("下一步：用浏览器打开这个文件，全选复制，粘贴进公众号编辑器即可。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
