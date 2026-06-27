#!/usr/bin/env python3
"""Render a static PNG of the wiki graph for embedding in the README.

GitHub markdown can't run the interactive force-graph (no JS), so this draws a
faithful still — same dark palette and degree-sized nodes as tools/graph/index.html
— that the README links to the live, interactive GitHub Pages viewer.

Deterministic (seeded layout) so re-runs don't churn the image. Optional helper:
needs networkx + Pillow (the browser viewer itself stays dependency-free).

Usage:
    python3 tools/graph/render_static.py        # reads graph.json, writes graph.png
"""

import json
import math
import os

import networkx as nx
from PIL import Image, ImageColor, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

# Mirror the viewer palette (index.html PALETTE).
PALETTE = {
    "code:concepts": "#58a6ff", "code:catalog": "#7ee787",
    "code:doc-concepts": "#f778ba", "code:overview": "#ffa657",
    "code:index": "#a5d6ff",
    "sources": "#d2a8ff", "topics": "#e3b341", "notes": "#39c5cf",
    "meta": "#8b949e",
}
FALLBACK = ["#8ddb8c", "#f0883e", "#db61a2", "#6cb6ff", "#c297ff", "#ec775c"]
BG = "#0d1117"
LINK = (55, 62, 70)         # dim link color on the dark bg
LABEL = (230, 237, 243)
PANEL = (22, 27, 34)
PANEL_BORDER = (48, 54, 61)

W, H = 1600, 1000           # final size
S = 2                       # supersample factor for smooth edges/circles


def color_of(group, _cache={}):
    if group in PALETTE:
        return PALETTE[group]
    if group not in _cache:
        _cache[group] = FALLBACK[len(_cache) % len(FALLBACK)]
    return _cache[group]


def font(size):
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


def main():
    data = json.load(open(os.path.join(HERE, "graph.json")))
    nodes = {n["id"]: n for n in data["nodes"]}

    G = nx.Graph()
    for nid, n in nodes.items():
        G.add_node(nid)
    for l in data["links"]:
        if l["source"] in nodes and l["target"] in nodes:
            G.add_edge(l["source"], l["target"])

    cw, ch = W * S, H * S
    img = Image.new("RGB", (cw, ch), ImageColor.getrgb(BG))
    d = ImageDraw.Draw(img)

    # Lay out the *connected* component on its own so disconnected orphans don't
    # blow up the bounding box and crush the cluster. Orphans get parked in a tidy
    # column on the left, under the legend.
    comps = sorted(nx.connected_components(G), key=len, reverse=True)
    main_nodes = comps[0]
    orphans = [n for c in comps[1:] for n in c]
    Gm = G.subgraph(main_nodes)
    try:
        raw = nx.kamada_kawai_layout(Gm)        # spreads connected graphs nicely
    except Exception:
        raw = nx.spring_layout(Gm, k=2.2 / math.sqrt(len(Gm)), iterations=400, seed=7)

    # main component -> right ~65% of the canvas (keeps clear of the top-left legend)
    xs = [p[0] for p in raw.values()]; ys = [p[1] for p in raw.values()]
    minx, maxx = min(xs), max(xs); miny, maxy = min(ys), max(ys)
    RX0, RX1, RY0, RY1 = 0.33 * cw, 0.97 * cw, 0.08 * ch, 0.90 * ch
    pos = {}
    for nid, (x, y) in raw.items():
        pos[nid] = (RX0 + (x - minx) / (maxx - minx or 1) * (RX1 - RX0),
                    RY0 + (y - miny) / (maxy - miny or 1) * (RY1 - RY0))
    # orphans down the left side, below the legend
    for i, nid in enumerate(orphans):
        pos[nid] = (0.135 * cw, (0.46 + 0.10 * i) * ch)

    def XY(nid):
        return pos[nid]

    # edges first (under nodes)
    for a, b in G.edges():
        d.line([XY(a), XY(b)], fill=LINK, width=max(1, S))

    # nodes sized by degree (area ~ degree, like nodeVal = 1 + deg)
    label_font = font(18 * S)
    for nid, n in nodes.items():
        px, py = XY(nid)
        r = math.sqrt(1 + n["deg"]) * 4.4 * S
        col = ImageColor.getrgb(color_of(n["group"]))
        d.ellipse([px - r, py - r, px + r, py + r], fill=col,
                  outline=ImageColor.getrgb(BG), width=max(1, S))
        # label the big hubs only, with the short page stem (not the long title)
        if n["deg"] >= 8:
            stem = os.path.basename(nid)[:-3] if nid.endswith(".md") else nid
            d.text((px + r + 4 * S, py), stem, fill=LABEL,
                   font=label_font, anchor="lm")

    # legend panel (top-left), mirrors the viewer
    counts = {}
    for n in nodes.values():
        counts[n["group"]] = counts.get(n["group"], 0) + 1
    order = sorted(counts.items(), key=lambda kv: -kv[1])
    lf = font(20 * S); tf = font(24 * S)
    pad = 16 * S; row_h = 30 * S
    pw = 360 * S; ph = pad * 2 + 40 * S + row_h * len(order)
    d.rounded_rectangle([20 * S, 20 * S, 20 * S + pw, 20 * S + ph],
                        radius=10 * S, fill=PANEL, outline=PANEL_BORDER, width=S)
    d.text((20 * S + pad, 20 * S + pad), "Wiki Graph  ·  code + prose",
           fill=LABEL, font=tf, anchor="lm")
    y0 = 20 * S + pad + 40 * S
    for i, (g, c) in enumerate(order):
        cy = y0 + i * row_h + row_h // 2
        dot = 11 * S
        d.ellipse([20 * S + pad, cy - dot // 2, 20 * S + pad + dot, cy + dot // 2],
                  fill=ImageColor.getrgb(color_of(g)))
        d.text((20 * S + pad + dot + 10 * S, cy), g, fill=LABEL, font=lf, anchor="lm")
        d.text((20 * S + pw - pad, cy), str(c), fill=(139, 148, 158), font=lf, anchor="rm")

    out = os.path.join(HERE, "graph.png")
    img.resize((W, H), Image.LANCZOS).save(out)
    print(f"wrote {out}  ({len(nodes)} nodes, {G.number_of_edges()} edges)")


if __name__ == "__main__":
    main()
