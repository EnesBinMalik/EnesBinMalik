"""Enes Öztürk · üst düzey profil rozeti.

docs/badge-master.svg — 720x720, çok katmanlı:
  dış ışıma · çift halka · sekizgen kalkan gövdesi · iç metal · EÖ monogramı ·
  yörünge noktaları · kalite çentikleri · imza şeridi

Kullanım: python tools_master_badge.py
"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
DOCS = ROOT / "docs"
FONT = "'Segoe UI',Inter,system-ui,-apple-system,Arial,sans-serif"
MONO = "'JetBrains Mono','Cascadia Code',Consolas,monospace"

CYAN, VIOLET, AMBER, GREEN, PINK = "#22D3EE", "#A78BFA", "#FBBF24", "#4ADE80", "#F472B6"


def build() -> str:
    W = 720
    cx = cy = 360
    L: list[str] = []
    a = L.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W}" width="{W}" height="{W}" '
      'role="img" aria-label="Enes Öztürk — imzalı ustalık rozeti">')
    a("<title>Enes Öztürk · Ustalık Rozeti</title>")
    a("<defs>")
    # zemin
    a('<radialGradient id="bg" cx="50%" cy="38%" r="70%">'
      '<stop offset="0" stop-color="#0C1626"/><stop offset="60%" stop-color="#070D18"/>'
      '<stop offset="100%" stop-color="#04070D"/></radialGradient>')
    # altın-gümüş metal
    a('<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">'
      '<stop offset="0" stop-color="#FFF7D6"/><stop offset="22%" stop-color="#FCD34D"/>'
      '<stop offset="45%" stop-color="#F59E0B"/><stop offset="62%" stop-color="#FDE68A"/>'
      '<stop offset="82%" stop-color="#D97706"/><stop offset="100%" stop-color="#FBBF24"/></linearGradient>')
    a('<linearGradient id="silver" x1="0" y1="0" x2="1" y2="1">'
      '<stop offset="0" stop-color="#FFFFFF" stop-opacity="0.92"/>'
      '<stop offset="40%" stop-color="#CBD5E1" stop-opacity="0.55"/>'
      '<stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.28"/></linearGradient>')
    a(f'<linearGradient id="neon" x1="0" y1="0" x2="1" y2="1">'
      f'<stop offset="0" stop-color="{CYAN}"/><stop offset="45%" stop-color="{VIOLET}"/>'
      f'<stop offset="100%" stop-color="{PINK}"/></linearGradient>')
    a('<linearGradient id="inner" x1="0" y1="0" x2="0" y2="1">'
      '<stop offset="0" stop-color="#101E33"/><stop offset="55%" stop-color="#0A1421"/>'
      '<stop offset="100%" stop-color="#060C15"/></linearGradient>')
    a(f'<radialGradient id="halo" cx="50%" cy="50%" r="50%">'
      f'<stop offset="0" stop-color="{CYAN}" stop-opacity="0.34"/>'
      f'<stop offset="55%" stop-color="{VIOLET}" stop-opacity="0.12"/>'
      f'<stop offset="100%" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>')
    a('<radialGradient id="shine" cx="34%" cy="26%" r="52%">'
      '<stop offset="0" stop-color="#FFFFFF" stop-opacity="0.30"/>'
      '<stop offset="60%" stop-color="#FFFFFF" stop-opacity="0.05"/>'
      '<stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>')
    a('<filter id="glow" x="-40%" y="-40%" width="180%" height="180%">'
      '<feGaussianBlur stdDeviation="7" result="b"/><feMerge>'
      '<feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    a('<filter id="soft" x="-40%" y="-40%" width="180%" height="180%">'
      '<feGaussianBlur stdDeviation="26"/></filter>')
    a('<pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse">'
      '<circle cx="1.2" cy="1.2" r="1.2" fill="#FFFFFF" fill-opacity="0.045"/></pattern>')
    a(f'<style>.t{{font-family:{FONT}}}.m{{font-family:{MONO}}}'
      f'.name{{font-family:{FONT};font-weight:800;letter-spacing:-2px}}'
      f'.cap{{font-family:{FONT};font-weight:700;letter-spacing:3.4px}}'
      f'.mini{{font-family:{MONO};letter-spacing:1.6px}}</style>')
    a("</defs>")

    # zemin
    a(f'<rect width="{W}" height="{W}" rx="40" fill="url(#bg)"/>')
    a(f'<rect width="{W}" height="{W}" rx="40" fill="url(#dots)"/>')
    a(f'<circle cx="{cx}" cy="{cy}" r="330" fill="url(#halo)"/>')
    a(f'<circle cx="{cx}" cy="{cy}" r="300" fill="url(#halo)" filter="url(#soft)" opacity="0.8"/>')

    # dış halkalar (çift çizgi + kesik yaylar)
    a(f'<circle cx="{cx}" cy="{cy}" r="286" fill="none" stroke="url(#neon)" stroke-width="2" stroke-opacity="0.55"/>')
    a(f'<circle cx="{cx}" cy="{cy}" r="272" fill="none" stroke="#FFFFFF" stroke-opacity="0.10" stroke-width="1"/>')
    for i, col in enumerate([CYAN, VIOLET, AMBER]):
        rot = -90 + i * 120
        a(f'<circle cx="{cx}" cy="{cy}" r="286" fill="none" stroke="{col}" stroke-width="4" '
          f'stroke-opacity="0.82" stroke-linecap="round" stroke-dasharray="52 1400" '
          f'transform="rotate({rot} {cx} {cy})" filter="url(#glow)"/>')

    # yörünge noktaları
    for ang, col, r in [(28, CYAN, 5.5), (152, VIOLET, 4.5), (248, AMBER, 4), (312, GREEN, 4)]:
        import math
        rad = math.radians(ang)
        px, py = cx + 286 * math.cos(rad), cy + 286 * math.sin(rad)
        a(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" fill="{col}" filter="url(#glow)" stroke-opacity="0.8"/>')

    # sekizgen kalkan gövdesi
    body = "M360 92 L549 171 L628 360 L549 549 L360 628 L171 549 L92 360 L171 171 Z"
    inner = "M360 138 L522 205 L586 360 L522 515 L360 582 L198 515 L134 360 L198 205 Z"
    a(f'<path d="{body}" fill="url(#gold)" fill-opacity="0.95" filter="url(#glow)" stroke-opacity="0.8"/>')
    a(f'<path d="{body}" fill="none" stroke="#FFF7D6" stroke-opacity="0.65" stroke-width="2"/>')
    a(f'<path d="{inner}" fill="url(#inner)" stroke="url(#silver)" stroke-width="2.5"/>')
    a(f'<path d="{inner}" fill="url(#shine)" opacity="0.55"/>')

    # iç çerçeve ince çizgi
    a(f'<path d="M360 156 L508 218 L564 360 L508 502 L360 564 L212 502 L156 360 L212 218 Z" '
      'fill="none" stroke="url(#neon)" stroke-opacity="0.55" stroke-width="1.6"/>')

    # monogram halkası
    a(f'<circle cx="{cx}" cy="252" r="80" fill="none" stroke="url(#gold)" stroke-width="4"/>')
    a(f'<circle cx="{cx}" cy="252" r="68" fill="{CYAN}" fill-opacity="0.07"/>')
    a(f'<circle cx="{cx}" cy="252" r="68" fill="none" stroke="{CYAN}" stroke-opacity="0.55" stroke-width="1.6"/>')
    a(f'<text x="{cx}" y="286" text-anchor="middle" class="name" font-size="88" fill="#F8FAFC">EÖ</text>')

    # isim ve künye
    a(f'<text x="{cx}" y="368" text-anchor="middle" class="t" font-size="32" font-weight="700" '
      'fill="#F1F5F9" letter-spacing="-0.5">Enes Öztürk</text>')
    a(f'<text x="{cx}" y="396" text-anchor="middle" class="mini" font-size="12.5" fill="#9DB0C8">'
      'GITHUB · ENESBINMALIK</text>')

    # kalite çentikleri
    for i, col in enumerate([CYAN, VIOLET, PINK, AMBER, GREEN]):
        x = cx - 104 + i * 46
        a(f'<rect x="{x}" y="466" width="34" height="6" rx="3" fill="{col}" fill-opacity="0.9"/>')

    # ustalık şeridi
    a(f'<rect x="{cx-138}" y="418" width="276" height="42" rx="21" fill="url(#neon)" fill-opacity="0.14" '
      'stroke="url(#neon)" stroke-opacity="0.7" stroke-width="1.6"/>')
    a(f'<text x="{cx}" y="446" text-anchor="middle" class="cap" font-size="14.5" fill="#E6F7FF">USTALIK ROZETİ</text>')

    # alt imza
    a(f'<text x="{cx}" y="500" text-anchor="middle" class="mini" font-size="11" fill="#BCC8DA">'
      '88 depo · 85 kapak · 6 alan</text>')
    a(f'<text x="{cx}" y="524" text-anchor="middle" class="mini" font-size="10.5" fill="#94A3B8">'
      'imza · Enes Öztürk</text>')

    a("</svg>")
    return "\n".join(L) + "\n"


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    out = DOCS / "badge-master.svg"
    out.write_text(build(), encoding="utf-8")
    print("✓", out)


if __name__ == "__main__":
    main()
