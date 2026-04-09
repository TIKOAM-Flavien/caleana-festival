import json
import os
from pathlib import Path
from html import escape


ROOT = Path(__file__).resolve().parents[1]
CONTENT_PATH = ROOT / "content" / "subpages.fr.json"


def _join_url(base: str, path: str) -> str:
    base = (base or "").rstrip("/")
    path = (path or "").strip("/")
    return f"{base}/{path}/"


def _render_nav_items(items):
    return "\n".join(
        f'                <li><a href="{escape(item["href"])}">{escape(item["label"])}</a></li>'
        for item in items
    )


def _render_footer_items(items):
    out = []
    for idx, item in enumerate(items):
        if idx:
            out.append('            <span class="sep">●</span>')
        out.append(f'            <a href="{escape(item["href"])}">{escape(item["label"])}</a>')
    return "\n".join(out)


def _render_list(items):
    if not items:
        return ""
    lis = "\n".join(f"                            <li>{item}</li>" for item in items)
    return f"""
                        <ul class="about-list" style="margin-top: 0.75rem;">
{lis}
                        </ul>"""


def _render_paragraphs(paragraphs):
    if not paragraphs:
        return ""
    rendered = []
    for i, p in enumerate(paragraphs):
        cls = "" if i == 0 else ' class="info-note"'
        style = "" if i == 0 else ' style="margin-top: 0.75rem;"'
        rendered.append(f"                        <p{cls}{style}>\n                            {p}\n                        </p>")
    return "\n".join(rendered)


def _render_block(block):
    block_type = block.get("type")
    title = block.get("title", "")
    paragraphs = block.get("paragraphs", [])
    items = block.get("list", [])
    cta = block.get("cta")

    card_class = "about-card"
    if block_type == "card_main":
        card_class = "about-card about-card--main"

    title_html = f"                        <h2>{escape(title)}</h2>\n" if title else ""
    paras_html = _render_paragraphs(paragraphs)
    list_html = _render_list(items)

    cta_html = ""
    if isinstance(cta, dict) and cta.get("label") and cta.get("href"):
        cta_html = f"""
                        <p style="margin-top: 1rem;">
                            <a class="cta-button" href="{escape(cta["href"])}">{escape(cta["label"])}</a>
                        </p>"""

    return f"""
                    <div class="{card_class}">
{title_html}{paras_html}{list_html}{cta_html}
                    </div>"""


def render_page(site, common, page):
    slug = page["slug"].strip("/")
    canonical = _join_url(site["canonical_base"], slug)
    title = page["title"]
    meta_description = page["meta_description"]
    h1 = page["h1"]

    nav_items = common.get("nav_items", [])
    footer_items = common.get("footer_items", [])
    cta_label = common.get("cta_label", "Découvrir le festival")
    cta_href = common.get("cta_href", "/")

    blocks_html = "\n".join(_render_block(b) for b in page.get("blocks", []))

    return f"""<!DOCTYPE html>
<html lang="{escape(site.get("lang", "fr"))}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="format-detection" content="telephone=no">
    <meta name="referrer" content="strict-origin-when-cross-origin">
    <title>{escape(title)}</title>
    <meta name="description" content="{escape(meta_description)}">
    <meta name="robots" content="index, follow">
    <meta name="theme-color" content="{escape(site.get("theme_color", "#3D1B6E"))}">

    <script async src="https://www.googletagmanager.com/gtag/js?id={escape(site["ga4_id"])}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{escape(site["ga4_id"])}');
    </script>

    <link rel="canonical" href="{escape(canonical)}">

    <meta property="og:type" content="website">
    <meta property="og:title" content="{escape(title)}">
    <meta property="og:description" content="{escape(meta_description)}">
    <meta property="og:url" content="{escape(canonical)}">
    <meta property="og:locale" content="fr_FR">
    <meta property="og:site_name" content="Caleana Festival">

    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" href="/favicon-32x32.png" type="image/png" sizes="32x32">
    <link rel="icon" href="/favicon-192x192.png" type="image/png" sizes="192x192">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180">
    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Lato:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <a class="skip-link" href="#mainContent">Aller au contenu</a>

    <nav class="nav nav-scrolled" aria-label="Navigation principale">
        <div class="container">
            <a href="/" class="nav-logo">Caleana festival</a>
            <ul class="nav-links" style="gap: 1rem; justify-content: flex-end;">
{_render_nav_items(nav_items)}
                <li><a class="nav-cta" href="/" aria-label="Retour à la page principale">Page principale</a></li>
            </ul>
        </div>
    </nav>

    <main id="mainContent">
        <section class="about" aria-label="Découvrir le festival" style="padding-top: 7.5rem; padding-bottom: 0;">
            <div class="container" style="text-align: center;">
                <a class="cta-button" href="{escape(cta_href)}" aria-label="Découvrir le festival (page principale)">
                    {escape(cta_label)}
                </a>
            </div>
        </section>

        <section class="about" style="padding-top: 7.5rem;">
            <div class="container">
                <h1 class="section-title" style="margin-bottom: 1.25rem;">{escape(h1)}</h1>

                <div class="about-grid" style="grid-template-columns: 1fr; gap: 1.25rem;">
{blocks_html}
                </div>
            </div>
        </section>

        <section class="about" aria-label="Découvrir le festival" style="padding-top: 0; padding-bottom: 5rem;">
            <div class="container" style="text-align: center;">
                <a class="cta-button" href="{escape(cta_href)}" aria-label="Découvrir le festival (page principale)">
                    {escape(cta_label)}
                </a>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="footer-logo">Caleana Festival</div>
        <p class="footer-credit">
{_render_footer_items(footer_items)}
        </p>
    </footer>
</body>
</html>
"""


def main():
    if not CONTENT_PATH.exists():
        raise SystemExit(f"Missing content file: {CONTENT_PATH}")

    data = json.loads(CONTENT_PATH.read_text(encoding="utf-8"))
    site = data["site"]
    common = data.get("common", {})
    pages = data.get("pages", [])

    written = 0
    for page in pages:
        slug = page["slug"].strip("/")
        out_dir = ROOT / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "index.html"
        out_path.write_text(render_page(site, common, page), encoding="utf-8")
        written += 1

    print(f"OK: generated {written} pages from {CONTENT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

