"""md2wechat —— 把 Markdown 转成可直接粘贴进微信公众号编辑器的排版 HTML。"""

from .converter import convert
from .themes import DEFAULT_THEME, THEMES

__version__ = "0.1.0"

__all__ = ["convert", "THEMES", "DEFAULT_THEME", "__version__"]
