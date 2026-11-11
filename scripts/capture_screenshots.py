"""! @file capture_screenshots.py
@brief Takes one screenshot per lecture step, headless, inside the Playwright Docker image.

Never run this on the host desktop (framework/process/gui-testing.md). Use
scripts/capture_screenshots.sh, which starts the container.

Environment:
  BLOG_URL      base URL of the running blog (default http://host.docker.internal:8081)
  TERMINAL_DIR  folder with step texts (NN-name.txt) that are rendered as a terminal window
  OUT_DIR       folder for the PNG files (default /out)
  GIT_URL       optional URL of the repository page on the git host
"""
import html
import logging
import os
import secrets
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

logger = logging.getLogger("capture")

BLOG_URL = os.environ.get("BLOG_URL", "http://host.docker.internal:8081")
TERMINAL_DIR = Path(os.environ.get("TERMINAL_DIR", "/terminal"))
OUT_DIR = Path(os.environ.get("OUT_DIR", "/out"))
GIT_URL = os.environ.get("GIT_URL", "")
VIEWPORT = {"width": 1200, "height": 760}

TERMINAL_PAGE = """<html><body style="margin:0;background:#1e1e2e;color:#cdd6f4;
font:15px/1.5 Consolas,'DejaVu Sans Mono',monospace;padding:28px">
<div style="color:#89b4fa;margin-bottom:12px">{title}</div><pre style="margin:0;white-space:pre-wrap">{body}</pre>
</body></html>"""


def shoot(page: Page, name: str, full_page: bool = False) -> None:
    """! @brief Saves a screenshot of the current page as <name>.png."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(OUT_DIR / f"{name}.png"), full_page=full_page)
    logger.info("saved %s", name)


def render_terminals(page: Page) -> None:
    """! @brief Renders every NN-name.txt of TERMINAL_DIR as a terminal screenshot."""
    for text_file in sorted(TERMINAL_DIR.glob("*.txt")):
        body = html.escape(text_file.read_text(encoding="utf-8"))
        page.set_content(TERMINAL_PAGE.format(title=html.escape(text_file.stem), body=body))
        shoot(page, text_file.stem, full_page=True)


def set_editor(page: Page, field: str, text: str) -> None:
    """! @brief Fills a CKEditor field through the editor API, or the textarea when it is not loaded."""
    page.evaluate(
        "([name, value]) => { if (window.CKEDITOR && CKEDITOR.instances[name]) {"
        " CKEDITOR.instances[name].setData(value); } else {"
        " document.querySelector('textarea[name=' + name + ']').value = value; } }",
        [field, text],
    )


def blog_pages(page: Page) -> None:
    """! @brief Registers the admin, writes a post, comments and takes the blog screenshots."""
    password = secrets.token_urlsafe(12)
    page.goto(f"{BLOG_URL}/register")
    shoot(page, "10-register-form")
    page.fill("input[name=name]", "Admin")
    page.fill("input[name=email]", "admin@example.test")
    page.fill("input[name=password]", password)
    page.click("input[type=submit], button[type=submit]")
    page.goto(f"{BLOG_URL}/login")
    shoot(page, "11-login-form")
    page.fill("input[name=email]", "admin@example.test")
    page.fill("input[name=password]", password)
    page.click("input[type=submit], button[type=submit]")
    page.goto(f"{BLOG_URL}/new-post")
    page.fill("input[name=title]", "Deploying my first Flask blog")
    page.fill("input[name=subtitle]", "Environment variables, gunicorn and PostgreSQL")
    set_editor(page, "body", "<p>The blog now runs from a container with a PostgreSQL database.</p>")
    shoot(page, "12-new-post-form")
    page.click("input[type=submit], button[type=submit]")
    page.goto(BLOG_URL)
    shoot(page, "01-blog-home", full_page=True)
    page.goto(f"{BLOG_URL}/post/1")
    set_editor(page, "comment_text", "<p>Nice and live!</p>")
    page.click("input[value='Submit Comment']")
    shoot(page, "13-blog-post", full_page=True)
    page.goto(f"{BLOG_URL}/about")
    shoot(page, "14-about")


def git_host(page: Page) -> None:
    """! @brief Screenshots the repository page on the git host, when reachable."""
    if not GIT_URL:
        return
    try:
        page.goto(GIT_URL, timeout=20000)
        shoot(page, "05-repository-on-git-host")
        page.goto(GIT_URL + "/commits/branch/main", timeout=20000)
        shoot(page, "02-commit-history")
    except Exception:  # network or host problem: the terminal fallbacks stay in place
        logger.exception("git host page not reachable")


def main() -> None:
    """! @brief Entry point."""
    logging.basicConfig(level=logging.INFO)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        render_terminals(page)
        blog_pages(page)
        git_host(page)
        browser.close()


if __name__ == "__main__":
    main()
