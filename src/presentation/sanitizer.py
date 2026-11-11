"""! @file sanitizer.py
@brief Allow-list HTML sanitiser for rich text written in CKEditor (stdlib only).
"""
import html
from html.parser import HTMLParser
from urllib.parse import urlparse

from constants import (
    ALLOWED_ATTRIBUTES,
    ALLOWED_TAGS,
    ALLOWED_URL_SCHEMES,
    DROPPED_CONTENT_TAGS,
    VOID_TAGS,
)

_URL_ATTRIBUTES = frozenset({"href", "src"})


def _is_safe_url(value: str) -> bool:
    """! @brief Tells whether a URL is relative or uses an allowed scheme."""
    cleaned = "".join(ch for ch in value if ch.isprintable() and not ch.isspace())
    return urlparse(cleaned).scheme.lower() in ALLOWED_URL_SCHEMES | {""}


class _Sanitizer(HTMLParser):
    """! @brief Rebuilds HTML keeping only allowed tags and attributes."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._out: list[str] = []
        self._dropping: list[str] = []

    @property
    def result(self) -> str:
        """! @brief The sanitised HTML collected so far."""
        return "".join(self._out)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in DROPPED_CONTENT_TAGS:
            self._dropping.append(tag)
            return
        if self._dropping or tag not in ALLOWED_TAGS:
            return
        self._out.append(f"<{tag}{self._render_attributes(attrs)}>")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in DROPPED_CONTENT_TAGS or self._dropping or tag not in ALLOWED_TAGS:
            return
        self._out.append(f"<{tag}{self._render_attributes(attrs)}>")

    def handle_endtag(self, tag: str) -> None:
        if self._dropping:
            if tag == self._dropping[-1]:
                self._dropping.pop()
            return
        if tag in ALLOWED_TAGS and tag not in VOID_TAGS:
            self._out.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if not self._dropping:
            self._out.append(html.escape(data))

    @staticmethod
    def _render_attributes(attrs: list[tuple[str, str | None]]) -> str:
        """! @brief Renders the allowed attributes with escaped values."""
        parts = []
        for name, value in attrs:
            if name not in ALLOWED_ATTRIBUTES or value is None:
                continue
            if name in _URL_ATTRIBUTES and not _is_safe_url(value):
                continue
            parts.append(f' {name}="{html.escape(value, quote=True)}"')
        return "".join(parts)


def sanitize_html(raw: str) -> str:
    """! @brief Returns the HTML with scripts, event handlers and unsafe URLs removed."""
    parser = _Sanitizer()
    parser.feed(raw)
    parser.close()
    return parser.result
