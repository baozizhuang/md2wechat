"""内置主题。

每个主题就是一张"元素 → 内联样式"的映射表。
公众号编辑器会过滤 <style> 标签和 class，所以所有样式都必须内联。

想加新主题？复制一份 DEFAULT_STYLES 改色即可，键名保持不变。
"""

# 键名说明：
#   section        最外层容器（基础字体/字号/行距）
#   h1 ~ h4        标题（h5/h6 自动沿用 h4）
#   p              正文段落
#   blockquote     引用块容器
#   blockquote_p   引用块内的段落
#   ul / ol / li   列表
#   li_p           列表项内的段落
#   strong / em / del / a
#   codespan       行内代码 `code`
#   pre / pre_code 代码块及其中的 code
#   table / th / td
#   img / hr

FONT_STACK = (
    "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'PingFang SC', "
    "'Hiragino Sans GB', 'Microsoft YaHei', Arial, sans-serif"
)
MONO_STACK = "Menlo, Consolas, 'Courier New', monospace"

DEFAULT_STYLES = {
    "section": (
        f"font-family: {FONT_STACK}; font-size: 16px; color: #3f3f3f; "
        "line-height: 1.75; letter-spacing: 0.03em; text-align: justify; padding: 0 8px;"
    ),
    "h1": "font-size: 20px; font-weight: 700; color: #1a1a1a; text-align: center; margin: 32px 0 20px;",
    "h2": "font-size: 18px; font-weight: 700; color: #1a1a1a; margin: 30px 0 14px; padding-left: 10px; border-left: 4px solid #1e6fff; line-height: 1.4;",
    "h3": "font-size: 17px; font-weight: 700; color: #1a1a1a; margin: 24px 0 12px;",
    "h4": "font-size: 16px; font-weight: 700; color: #1a1a1a; margin: 20px 0 10px;",
    "p": "margin: 12px 0; font-size: 16px; color: #3f3f3f;",
    "blockquote": "margin: 16px 0; padding: 10px 16px; background: #f7f9fc; border-left: 4px solid #c9d6e8; color: #6a737d;",
    "blockquote_p": "margin: 4px 0; font-size: 15px; color: #6a737d;",
    "ul": "margin: 12px 0; padding-left: 26px;",
    "ol": "margin: 12px 0; padding-left: 26px;",
    "li": "margin: 6px 0; line-height: 1.75;",
    "li_p": "margin: 0; font-size: 16px; color: #3f3f3f;",
    "strong": "font-weight: 700; color: #1a1a1a;",
    "em": "font-style: italic;",
    "del": "color: #999999;",
    "a": "color: #1e6fff; text-decoration: none;",
    "codespan": (
        f"font-family: {MONO_STACK}; font-size: 14px; background: #f0f2f5; "
        "color: #d6336c; padding: 2px 6px; border-radius: 4px; margin: 0 2px;"
    ),
    "pre": (
        "background: #f6f8fa; border: 1px solid #e8eaed; border-radius: 8px; "
        "padding: 14px 16px; overflow-x: auto; margin: 16px 0; font-size: 13px; line-height: 1.6;"
    ),
    "pre_code": f"font-family: {MONO_STACK}; font-size: 13px; color: #24292e; background: transparent; padding: 0;",
    "table": "width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px;",
    "th": "background: #f2f4f7; border: 1px solid #dfe2e6; padding: 8px 12px; font-weight: 700; color: #1a1a1a; text-align: left;",
    "td": "border: 1px solid #dfe2e6; padding: 8px 12px; color: #3f3f3f;",
    "img": "max-width: 100%; border-radius: 8px; display: block; margin: 16px auto;",
    "hr": "border: none; border-top: 1px solid #e5e7eb; margin: 32px 0;",
}

WARM_STYLES = {
    **DEFAULT_STYLES,
    "section": (
        f"font-family: {FONT_STACK}; font-size: 16px; color: #43332a; "
        "line-height: 1.8; letter-spacing: 0.03em; text-align: justify; padding: 0 8px;"
    ),
    "h2": "font-size: 18px; font-weight: 700; color: #2b1d12; margin: 30px 0 14px; padding-left: 10px; border-left: 4px solid #d9711e; line-height: 1.4;",
    "p": "margin: 12px 0; font-size: 16px; color: #43332a;",
    "li_p": "margin: 0; font-size: 16px; color: #43332a;",
    "blockquote": "margin: 16px 0; padding: 10px 16px; background: #fdf3ea; border-left: 4px solid #f0cba8; color: #8a6d52;",
    "blockquote_p": "margin: 4px 0; font-size: 15px; color: #8a6d52;",
    "a": "color: #c2410c; text-decoration: none;",
    "codespan": (
        f"font-family: {MONO_STACK}; font-size: 14px; background: #fdf0e5; "
        "color: #c2410c; padding: 2px 6px; border-radius: 4px; margin: 0 2px;"
    ),
    "strong": "font-weight: 700; color: #2b1d12;",
    "th": "background: #fbeede; border: 1px solid #e8d9c6; padding: 8px 12px; font-weight: 700; color: #2b1d12; text-align: left;",
    "td": "border: 1px solid #e8d9c6; padding: 8px 12px; color: #43332a;",
    "hr": "border: none; border-top: 1px solid #ecdfd0; margin: 32px 0;",
}

INK_STYLES = {
    **DEFAULT_STYLES,
    "h1": "font-size: 20px; font-weight: 700; color: #111111; text-align: center; margin: 32px 0 20px;",
    "h2": "font-size: 18px; font-weight: 700; color: #111111; margin: 30px 0 14px; padding-bottom: 6px; border-bottom: 2px solid #111111;",
    "h3": "font-size: 17px; font-weight: 700; color: #111111; margin: 24px 0 12px;",
    "h4": "font-size: 16px; font-weight: 700; color: #111111; margin: 20px 0 10px;",
    "blockquote": "margin: 16px 0; padding: 10px 16px; background: #fafafa; border-left: 4px solid #111111; color: #555555;",
    "blockquote_p": "margin: 4px 0; font-size: 15px; color: #555555;",
    "a": "color: #111111; text-decoration: underline;",
    "codespan": (
        f"font-family: {MONO_STACK}; font-size: 14px; background: #f0f0f0; "
        "color: #111111; padding: 2px 6px; border-radius: 4px; margin: 0 2px;"
    ),
    "strong": "font-weight: 700; color: #000000;",
    "th": "background: #f0f0f0; border: 1px solid #cccccc; padding: 8px 12px; font-weight: 700; color: #111111; text-align: left;",
    "td": "border: 1px solid #cccccc; padding: 8px 12px; color: #3f3f3f;",
    "img": "max-width: 100%; display: block; margin: 16px auto;",
    "hr": "border: none; border-top: 2px solid #111111; margin: 32px 0;",
}

THEMES = {
    "default": {
        "description": "清爽蓝：左侧蓝色竖条标题，适合大多数科普/技术号",
        "styles": DEFAULT_STYLES,
    },
    "warm": {
        "description": "暖橙：暖色调，适合生活、亲子、人文类账号",
        "styles": WARM_STYLES,
    },
    "ink": {
        "description": "墨黑：黑白极简，下划线式标题，适合深度长文",
        "styles": INK_STYLES,
    },
}

DEFAULT_THEME = "default"
