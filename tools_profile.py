"""Enes Öztürk · GitHub profil görselleri.

Üretir:
  docs/profile-banner.svg   1200x400  — profil README üstü
  docs/badge-shield.svg      600x600  — kalkan formunda rozet vitrini
  docs/badge-hex.svg         600x600  — altıgen formunda rozet vitrini

Kullanım: python tools_profile.py
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ROOT / "docs"
FONT = "'Segoe UI',Inter,system-ui,-apple-system,Arial,sans-serif"
MONO = "'JetBrains Mono','Cascadia Code',Consolas,monospace"

INK = "#E9F0FB"
DIM = "#8FA0BD"
FAINT = "#5A6B88"
CYAN = "#22D3EE"
VIOLET = "#A78BFA"
AMBER = "#FBBF24"
GREEN = "#4ADE80"
PINK = "#F472B6"
ORANGE = "#FB923C"


def defs() -> str:
    return (
        "<defs>"
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#05090F"/><stop offset="50%" stop-color="#0A1220"/>'
        '<stop offset="100%" stop-color="#121E33"/></linearGradient>'
        '<linearGradient id="acc" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{CYAN}"/><stop offset="55%" stop-color="{VIOLET}"/>'
        f'<stop offset="100%" stop-color="{VIOLET}" stop-opacity="0.08"/></linearGradient>'
        '<radialGradient id="g1" cx="50%" cy="50%" r="50%">'
        f'<stop offset="0" stop-color="{CYAN}" stop-opacity="0.26"/>'
        f'<stop offset="100%" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="g2" cx="50%" cy="50%" r="50%">'
        f'<stop offset="0" stop-color="{VIOLET}" stop-opacity="0.24"/>'
        f'<stop offset="100%" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>'
        '<linearGradient id="metal" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#FFFFFF" stop-opacity="0.22"/>'
        '<stop offset="45%" stop-color="#FFFFFF" stop-opacity="0.04"/>'
        '<stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.10"/></linearGradient>'
        '<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#FFFFFF" stop-opacity="0.18"/>'
        '<stop offset="60%" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
        '<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">'
        '<path d="M40 0H0V40" fill="none" stroke="#FFFFFF" stroke-opacity="0.035"/></pattern>'
        '<filter id="soft" x="-30%" y="-30%" width="160%" height="160%">'
        '<feGaussianBlur stdDeviation="22"/></filter>'
        f'<style>.t{{font-family:{FONT}}}.m{{font-family:{MONO}}}'
        f'.ttl{{font-family:{FONT};font-weight:700;letter-spacing:-1.6px}}'
        f'.cap{{font-family:{FONT};font-weight:600;letter-spacing:3px}}</style>'
        "</defs>"
    )


def banner() -> str:
    W, H = 1200, 400
    a: list[str] = []
    L = a.append
    L(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      'role="img" aria-label="Enes Öztürk — GitHub profil vitrini">')
    L("<title>Enes Öztürk · GitHub Profil Vitrini</title>")
    L(defs())
    L(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')
    L(f'<rect width="{W}" height="{H}" fill="url(#grid)"/>')
    L(f'<ellipse cx="200" cy="60" rx="420" ry="240" fill="url(#g1)"/>')
    L(f'<ellipse cx="1080" cy="380" rx="420" ry="260" fill="url(#g2)"/>')
    L(f'<rect x="0" y="0" width="6" height="{H}" fill="url(#acc)"/>')

    # üst şerit
    L(f'<g class="m" font-size="11.5" fill="{FAINT}" letter-spacing="1.8">'
      f'<text x="48" y="42">GITHUB</text><text x="112" y="42" fill="#1E3050">/</text>'
      f'<text x="128" y="42">ENESBINMALIK</text>'
      f'<text x="1152" y="42" text-anchor="end" fill="{CYAN}" fill-opacity="0.85">PROFİL VİTRİNİ</text></g>')
    L(f'<line x1="48" y1="58" x2="1152" y2="58" stroke="#FFFFFF" stroke-opacity="0.07"/>')

    # isim + ünvan
    L(f'<text x="48" y="132" class="ttl" font-size="54" fill="{INK}">Enes Öztürk</text>')
    L(f'<text x="48" y="166" class="t" font-size="17" fill="{DIM}">'
      'Bilgisayar Programcılığı Öğrencisi · IoT &amp; Yazılım Geliştirici · AI &amp; Cloud</text>')
    L(f'<rect x="48" y="186" width="56" height="3" rx="1.5" fill="{CYAN}"/>')

    # istatistik kartları
    stats = [("126", "public repo", CYAN), ("85", "imzalı kapak", VIOLET),
             ("47", "takipçi", GREEN), ("8", "teknoloji hattı", AMBER)]
    for i, (n, lab, col) in enumerate(stats):
        x = 48 + i * 150
        L(f'<rect x="{x}" y="214" width="138" height="84" rx="14" fill="#0B1420" fill-opacity="0.9" stroke="#1E3050"/>')
        L(f'<rect x="{x}" y="214" width="4" height="84" rx="2" fill="{col}"/>')
        L(f'<text x="{x+20}" y="256" class="t" font-size="28" font-weight="700" fill="{col}">{n}</text>')
        L(f'<text x="{x+20}" y="278" class="m" font-size="11" fill="{DIM}">{lab}</text>')

    # sağ: rozet vitrini (kalkan)
    cx, cy = 900, 200
    L(f'<g transform="translate({cx},{cy}) scale(0.66) translate(-300,-300)">')
    L('<path d="M300 60 L520 140 V320 C520 440 420 520 300 560 C180 520 80 440 80 320 V140 Z" '
      'fill="#0B1420" fill-opacity="0.92" stroke="url(#acc)" stroke-width="3"/>')
    L('<path d="M300 92 L492 162 V318 C492 424 404 492 300 528 C196 492 108 424 108 318 V162 Z" '
      'fill="url(#metal)" stroke="#FFFFFF" stroke-opacity="0.10"/>')
    L(f'<text x="300" y="250" text-anchor="middle" class="ttl" font-size="112" fill="{CYAN}">EÖ</text>')
    L(f'<text x="300" y="300" text-anchor="middle" class="m" font-size="26" fill="{INK}" letter-spacing="2.5">ENES ÖZTÜRK</text>')
    L(f'<text x="300" y="332" text-anchor="middle" class="m" font-size="16" fill="{DIM}" fill-opacity="1" letter-spacing="1.4">GITHUB · ENESBINMALIK</text>')
    L(f'<rect x="196" y="374" width="208" height="34" rx="17" fill="{CYAN}" fill-opacity="0.12" stroke="{CYAN}" stroke-opacity="0.45"/>')
    L(f'<text x="300" y="397" text-anchor="middle" class="cap" font-size="12" fill="{CYAN}">İMZALI VİTRİN</text>')
    L("</g>")

    # alt şerit
    L(f'<line x1="48" y1="336" x2="1152" y2="336" stroke="#FFFFFF" stroke-opacity="0.07"/>')
    L(f'<text x="48" y="368" class="m" font-size="12.5" fill="{DIM}">'
      'Node.js · GraphQL · Java · Rust · Solana · React · .NET</text>')
    L(f'<text x="1152" y="368" class="m" font-size="12" fill="{CYAN}" text-anchor="end" fill-opacity="0.85">'
      'github.com/EnesBinMalik</text>')
    L("</svg>")
    return "\n".join(a) + "\n"


def badge(shape: str = "shield") -> str:
    """Rozet vitrini: kalkan veya altıgen formunda, imzalı."""
    W, H = 600, 600
    a: list[str] = []
    L = a.append
    L(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'role="img" aria-label="Enes Öztürk — imzalı GitHub rozeti ({shape})">')
    L(f"<title>Enes Öztürk · GitHub Rozeti ({shape})</title>")
    L(defs())
    # arka plan: koyu disk + ışıma
    L(f'<circle cx="300" cy="300" r="290" fill="#0A1220"/>')
    L(f'<circle cx="300" cy="300" r="290" fill="url(#grid)" fill-opacity="0.9"/>')
    L(f'<ellipse cx="220" cy="180" rx="260" ry="200" fill="url(#g1)"/>')
    L(f'<ellipse cx="400" cy="450" rx="260" ry="220" fill="url(#g2)"/>')

    if shape == "hex":
        outer = "M300 46 L520 174 V426 L300 554 L80 426 V174 Z"
        inner = "M300 82 L490 194 V406 L300 518 L110 406 V194 Z"
    else:
        outer = "M300 52 L522 132 V318 C522 444 414 524 300 560 C186 524 78 444 78 318 V132 Z"
        inner = "M300 88 L492 158 V316 C492 424 402 490 300 524 C198 490 108 424 108 316 V158 Z"

    L(f'<path d="{outer}" fill="#0B1420" fill-opacity="0.95" stroke="url(#acc)" stroke-width="3.5"/>')
    L(f'<path d="{inner}" fill="url(#metal)" stroke="#FFFFFF" stroke-opacity="0.12"/>')
    L(f'<path d="{outer}" fill="url(#sheen)" fill-opacity="0.5"/>')

    # merkez: EÖ monogramı (tek halka, okunur kontrast)
    L(f'<circle cx="300" cy="228" r="70" fill="{CYAN}" fill-opacity="0.06"/>')
    L(f'<circle cx="300" cy="228" r="70" fill="none" stroke="{CYAN}" stroke-opacity="0.75" stroke-width="2.5"/>')
    L(f'<text x="300" y="256" text-anchor="middle" class="ttl" font-size="70" fill="{CYAN}">EÖ</text>')
    L(f'<text x="300" y="330" text-anchor="middle" class="m" font-size="18" fill="{INK}" letter-spacing="3.5">ENES ÖZTÜRK</text>')
    L(f'<text x="300" y="356" text-anchor="middle" class="m" font-size="12" fill="{DIM}" letter-spacing="1.6">GITHUB · ENESBINMALIK</text>')

    # 4 çentik (kalite işareti)
    for i, col in enumerate([CYAN, VIOLET, AMBER, GREEN]):
        x = 238 + i * 42
        L(f'<rect x="{x}" y="374" width="30" height="4" rx="2" fill="{col}" fill-opacity="0.85"/>')

    L(f'<rect x="198" y="394" width="204" height="32" rx="16" fill="{CYAN}" fill-opacity="0.12" '
      f'stroke="{CYAN}" stroke-opacity="0.45"/>')
    L(f'<text x="300" y="416" text-anchor="middle" class="cap" font-size="10.5" fill="{CYAN}">İMZALI ROZET</text>')
    L(f'<text x="300" y="450" text-anchor="middle" class="m" font-size="10.5" fill="{DIM}">'
      'tasarım &amp; geliştirme · Enes Öztürk</text>')
    L("</svg>")
    return "\n".join(a) + "\n"


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    (DOCS / "profile-banner.svg").write_text(banner(), encoding="utf-8")
    (DOCS / "badge-shield.svg").write_text(badge("shield"), encoding="utf-8")
    (DOCS / "badge-hex.svg").write_text(badge("hex"), encoding="utf-8")
    print("✓ docs/profile-banner.svg · docs/badge-shield.svg · docs/badge-hex.svg")


if __name__ == "__main__":
    main()
