from pathlib import Path
import sys

import webview


APP_TITLE = "ATEN PDU Web Panel"
HTML_FILE = "aten_pdu_web_helper_v2.html"


def resolve_html_path() -> Path:
    if hasattr(sys, "_MEIPASS"):
        base_path = Path(getattr(sys, "_MEIPASS"))
    else:
        base_path = Path(__file__).resolve().parent
    return base_path / HTML_FILE


def main() -> None:
    html_path = resolve_html_path()
    if not html_path.exists():
        raise FileNotFoundError(f"HTML dosyası bulunamadı: {html_path}")

    webview.create_window(
        APP_TITLE,
        url=html_path.as_uri(),
        width=1400,
        height=900,
        min_size=(1000, 700),
    )
    webview.start()


if __name__ == "__main__":
    main()
