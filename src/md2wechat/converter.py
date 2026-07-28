"""核心转换逻辑：Markdown → 全内联样式的公众号 HTML。

思路：
1. 用 markdown-it-py 把 Markdown 渲染成标准 HTML；
2. 用 BeautifulSoup 遍历所有标签，按主题把样式写成内联 style；
3. 外层包一个 <section> 作为整体容器。

为什么要全内联？公众号编辑器会丢弃 <style> 标签和 class 属性，
只有写在 style 里的样式在"复制-粘贴"后还能活下来。
"""

from __future__ import annotations

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

from .themes import DEFAULT_THEME, THEMES

# 这几个标签没有独立键名时，沿用什么样式
_TAG_ALIAS = {"h5": "h4", "h6": "h4"}


def _make_md() -> MarkdownIt:
    md = MarkdownIt("commonmark", {"html": True, "breaks": True})
    md.enable(["table", "strikethrough"])
    return md


_MD = _make_md()


def _style_key(tag) -> str:
    """给一个 bs4 标签算出它在主题表里的键名。"""
    name = tag.name
    if name == "code":
        return "pre_code" if tag.parent and tag.parent.name == "pre" else "codespan"
    if name == "p":
        parent = tag.parent.name if tag.parent else ""
        return {"blockquote": "blockquote_p", "li": "li_p"}.get(parent, "p")
    return _TAG_ALIAS.get(name, name)


def apply_styles(fragment: str, styles: dict) -> str:
    """给一段 HTML 的所有标签套上内联样式，并包一层 <section>。"""
    soup = BeautifulSoup(fragment, "html.parser")
    for el in soup.find_all(True):
        style = styles.get(_style_key(el))
        if style:
            el["style"] = style
    inner = "".join(str(child) for child in soup.contents)
    return f'<section style="{styles["section"]}">{inner}</section>'


def convert(markdown_text: str, theme: str = DEFAULT_THEME) -> str:
    """把 Markdown 文本转成可粘贴进公众号编辑器的 HTML。

    :param markdown_text: Markdown 源文本
    :param theme: 主题名，见 md2wechat.themes.THEMES
    :return: 全内联样式的 HTML 片段（<section> 包裹）
    """
    if theme not in THEMES:
        raise ValueError(f"未知主题 {theme!r}，可用：{', '.join(THEMES)}")
    fragment = _MD.render(markdown_text)
    return apply_styles(fragment, THEMES[theme]["styles"])
