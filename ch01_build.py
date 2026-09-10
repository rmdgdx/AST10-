# -*- coding: utf-8 -*-
"""Renderers for the full-depth Week 1 lecture and 30-item exercise set."""
import html, random
import meta, plan, ch01_lecture as L, ch01_items as X

E = lambda s: html.escape(str(s), quote=True)
FONT = 'font-family="-apple-system,Segoe UI,Inter,Roboto,Arial,sans-serif"'

# ----------------------------------------------------------------- figures --
def fig_method():
    steps = ["Observation", "Question", "Hypothesis", "Prediction", "Test", "Analysis", "Revise or accept"]
    n = len(steps); w, h = 900, 250; cx, cy = 450, 125
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>The cycle of inquiry</title>']
    # ellipse layout
    import math
    pts = []
    for i in range(n):
        a = -math.pi/2 + 2*math.pi*i/n
        pts.append((cx + 380*math.cos(a), cy + 88*math.sin(a)))
    for i, (x, y) in enumerate(pts):
        nx, ny = pts[(i+1) % n]
        o.append(f'<path d="M{x:.0f} {y:.0f} L{nx:.0f} {ny:.0f}" stroke="#1F4FA8" stroke-width="1.6" stroke-dasharray="4 4"/>')
    for i, (x, y) in enumerate(pts):
        pw = 40 + 7.2*len(steps[i]); hw = pw/2
        o.append(f'<rect x="{x-hw:.0f}" y="{y-19:.0f}" width="{pw:.0f}" height="38" rx="19" fill="#fff" stroke="#1F4FA8" stroke-width="1.5"/>')
        o.append(f'<circle cx="{x-hw+16:.0f}" cy="{y:.0f}" r="9" fill="#39FF14"/><text x="{x-hw+16:.0f}" y="{y+4:.0f}" text-anchor="middle" {FONT} font-size="11" font-weight="800" fill="#06250A">{i+1}</text>')
        o.append(f'<text x="{x+12:.0f}" y="{y+4:.0f}" text-anchor="middle" {FONT} font-size="12" font-weight="700" fill="#0B1F47">{steps[i]}</text>')
    o.append(f'<text x="{cx}" y="{cy-6}" text-anchor="middle" {FONT} font-size="13" fill="#555b73">A refuted hypothesis returns to step 3;</text>')
    o.append(f'<text x="{cx}" y="{cy+12}" text-anchor="middle" {FONT} font-size="13" fill="#555b73">a supported one is tested again by others.</text>')
    o.append('</svg>'); return "".join(o)


def fig_levels():
    items = ["Biosphere","Ecosystem","Community","Population","Organism","Organ system","Organ","Tissue","Cell","Organelle","Molecule","Atom"]
    notes = ["All ecosystems on the planet","Community plus its physical environment","All populations in an area","All individuals of one species in an area","An individual living thing","Organs cooperating in a function","Tissues combined for a function","Cells of similar type","Smallest unit that is alive","Membrane-bound compartment","Atoms bonded together","Smallest unit of an element"]
    n = len(items); rowh, pad = 30, 20; w, h = 840, pad*2 + n*rowh
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>Levels of biological organisation</title>']
    for i, (it, nt) in enumerate(zip(items, notes)):
        y = pad + i*rowh; inset = 9*(n-1-i); bw = 190 + inset*2; x = 60 + (n-1-i)*0 + (200 - inset)
        cell = (it == "Cell")
        o.append(f'<rect x="{x:.0f}" y="{y}" width="{bw:.0f}" height="{rowh-6}" rx="6" fill="{"#39FF14" if cell else "#1F4FA8"}" fill-opacity="{1 if cell else 0.10+0.06*(n-1-i)/2:.2f}" stroke="#1F4FA8" stroke-width="0.9"/>')
        o.append(f'<text x="{x+10:.0f}" y="{y+16}" {FONT} font-size="13" font-weight="{800 if cell else 600}" fill="#0B1F47">{it}</text>')
        o.append(f'<text x="{x+bw+12:.0f}" y="{y+16}" {FONT} font-size="12" fill="#555b73">{nt}</text>')
    o.append(f'<path d="M34 {pad+8} L34 {h-pad-8}" stroke="#39FF14" stroke-width="3"/><path d="M34 {pad+2} l-6 10 h12 z" fill="#39FF14"/>')
    o.append(f'<text x="24" y="{h/2:.0f}" {FONT} font-size="11" fill="#555b73" transform="rotate(-90 24 {h/2:.0f})" text-anchor="middle">increasing complexity, new properties emerge</text>')
    o.append('</svg>'); return "".join(o)


def fig_water():
    w, h = 760, 330
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>Water polarity and hydrogen bonding</title>']
    def mol(x, y, flip=False, label=True):
        d = -1 if flip else 1
        s = f'<g transform="translate({x} {y})">'
        for sx in (-1, 1):
            s += f'<line x1="0" y1="0" x2="{sx*30}" y2="{d*24}" stroke="#0B1F47" stroke-width="3"/>'
        s += '<circle cx="0" cy="0" r="22" fill="#1F4FA8"/><text x="0" y="5" text-anchor="middle" font-size="15" font-weight="800" fill="#fff" %s>O</text>' % FONT
        for sx in (-1, 1):
            s += f'<circle cx="{sx*30}" cy="{d*24}" r="13" fill="#DCE6F6" stroke="#0B1F47" stroke-width="1.5"/><text x="{sx*30}" y="{d*24+4}" text-anchor="middle" font-size="11" font-weight="700" fill="#0B1F47" {FONT}>H</text>'
        if label:
            s += f'<text x="0" y="-32" text-anchor="middle" font-size="13" font-weight="800" fill="#1F4FA8" {FONT}>δ–</text>'
            s += f'<text x="-30" y="48" text-anchor="middle" font-size="12" font-weight="800" fill="#0E6B1F" {FONT}>δ+</text><text x="30" y="48" text-anchor="middle" font-size="12" font-weight="800" fill="#0E6B1F" {FONT}>δ+</text>'
        return s + '</g>'
    # hydrogen bonds first (behind molecules): from an H to a neighbouring O
    hb = [((430,134),(360,190)), ((490,134),(560,190)), ((530,84),(460,110)), ((430,226),(360,190)), ((490,226),(560,190))]
    for (a, b) in hb:
        o.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#39FF14" stroke-width="3" stroke-dasharray="5 4"/>')
    o.append(mol(130, 130))
    o.append(f'<text x="130" y="215" text-anchor="middle" font-size="13" fill="#0B1F47" {FONT}>Bent shape, 104.5°: charge is</text><text x="130" y="232" text-anchor="middle" font-size="13" fill="#0B1F47" {FONT}>unevenly distributed → polar molecule</text>')
    for (x, y, f) in [(460,110,False),(560,190,True),(360,190,True),(460,250,True),(560,60,False)]:
        o.append(mol(x, y, f, label=False))
    o.append(f'<text x="460" y="312" text-anchor="middle" font-size="13" fill="#0B1F47" {FONT}>Dashed: hydrogen bonds (≈20 kJ/mol each) between δ+ H and δ– O of neighbours</text>')
    o.append('</svg>'); return "".join(o)


def fig_energy():
    w, h = 760, 300
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>Activation energy with and without an enzyme</title>']
    o.append(f'<line x1="70" y1="250" x2="720" y2="250" stroke="#0B1F47" stroke-width="1.5"/><line x1="70" y1="250" x2="70" y2="30" stroke="#0B1F47" stroke-width="1.5"/>')
    o.append(f'<text x="395" y="278" text-anchor="middle" font-size="13" fill="#555b73" {FONT}>Progress of reaction</text>')
    o.append(f'<text x="24" y="140" text-anchor="middle" font-size="13" fill="#555b73" {FONT} transform="rotate(-90 24 140)">Free energy (G)</text>')
    # uncatalysed: start 120, peak 50, end 190
    o.append('<path d="M90 120 C 250 120, 300 50, 395 50 S 540 190, 700 190" fill="none" stroke="#1F4FA8" stroke-width="3"/>')
    # catalysed: peak lower at 100
    o.append('<path d="M90 120 C 250 120, 300 100, 395 100 S 540 190, 700 190" fill="none" stroke="#39FF14" stroke-width="3" stroke-dasharray="7 5"/>')
    o.append(f'<line x1="90" y1="120" x2="720" y2="120" stroke="#C5D3EE" stroke-dasharray="3 4"/><line x1="90" y1="190" x2="720" y2="190" stroke="#C5D3EE" stroke-dasharray="3 4"/>')
    o.append(f'<text x="92" y="112" font-size="12" fill="#0B1F47" {FONT}>Reactants</text><text x="640" y="208" font-size="12" fill="#0B1F47" {FONT}>Products</text>')
    o.append('<line x1="395" y1="50" x2="395" y2="120" stroke="#1F4FA8" stroke-width="1.5"/><path d="M395 50 l-4 8 h8 z" fill="#1F4FA8"/>')
    o.append(f'<text x="405" y="42" font-size="12" font-weight="700" fill="#1F4FA8" {FONT}>E<tspan font-size="9" baseline-shift="sub">A</tspan> without enzyme</text>')
    o.append('<line x1="330" y1="100" x2="330" y2="120" stroke="#0E6B1F" stroke-width="1.5"/>')
    o.append(f'<text x="200" y="96" font-size="12" font-weight="700" fill="#0E6B1F" {FONT}>E<tspan font-size="9" baseline-shift="sub">A</tspan> with enzyme</text>')
    o.append('<line x1="700" y1="120" x2="700" y2="190" stroke="#0B1F47" stroke-width="1.5"/>')
    o.append(f'<text x="708" y="160" font-size="12" font-weight="700" fill="#0B1F47" {FONT}>ΔG &lt; 0</text>')
    o.append(f'<text x="708" y="176" font-size="11" fill="#555b73" {FONT}>unchanged</text>')
    o.append('</svg>'); return "".join(o)


def fig_feedback():
    steps = ["Stimulus: variable deviates", "Receptor detects", "Control centre compares to set point", "Effector responds", "Variable returns toward set point"]
    n = len(steps); boxw, gap, pad = 170, 26, 24; w, h = pad*2 + n*boxw + (n-1)*gap, 210
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>Negative feedback loop</title>']
    for i, it in enumerate(steps):
        x = pad + i*(boxw+gap)
        o.append(f'<rect x="{x}" y="46" width="{boxw}" height="90" rx="10" fill="#fff" stroke="#1F4FA8" stroke-width="1.4"/><rect x="{x}" y="46" width="{boxw}" height="5" rx="2" fill="#39FF14"/>')
        words, lines, cur = it.split(), [], ""
        for wd in words:
            if len(cur)+len(wd)+1 <= 20: cur=(cur+" "+wd).strip()
            else: lines.append(cur); cur=wd
        lines.append(cur); y0 = 92-(len(lines)-1)*9
        for j, ln in enumerate(lines): o.append(f'<text x="{x+boxw/2}" y="{y0+j*18}" text-anchor="middle" {FONT} font-size="13" fill="#0B1F47">{E(ln)}</text>')
        if i < n-1:
            ax = x+boxw+5; o.append(f'<path d="M{ax} 91 L{ax+gap-10} 91" stroke="#1F4FA8" stroke-width="1.6"/><path d="M{ax+gap-10} 91 l-7 -4.5 v9 z" fill="#1F4FA8"/>')
    lx = pad + (n-1)*(boxw+gap) + boxw/2; rx = pad + boxw/2
    o.append(f'<path d="M{lx} 136 L{lx} 172 L{rx} 172 L{rx} 140" fill="none" stroke="#0E6B1F" stroke-width="1.8" stroke-dasharray="6 4"/><path d="M{rx} 138 l-5 8 h10 z" fill="#0E6B1F"/>')
    o.append(f'<text x="{(lx+rx)/2}" y="192" text-anchor="middle" {FONT} font-size="12.5" fill="#0E6B1F" font-weight="700">Negative feedback: the response opposes the stimulus, so the loop shuts itself off</text>')
    o.append('</svg>'); return "".join(o)


FIGS = {
 "method": ("The cycle of inquiry", "Inquiry is iterative. A hypothesis is never proven; it is retained while it survives tests and abandoned when a prediction fails.", fig_method),
 "levels": ("Levels of biological organisation", "Each level has properties absent from the one below. The cell (highlighted) is the transition from chemistry to biology and the target of most life-detection strategies.", fig_levels),
 "water": ("Water polarity and hydrogen bonding", "The bent geometry and oxygen's electronegativity give each molecule partial charges; neighbours attract through hydrogen bonds, which underlie every property in §1.5.", fig_water),
 "energy": ("Activation energy with and without an enzyme", "The enzyme lowers the barrier and speeds the reaction; the free-energy change between reactants and products is untouched.", fig_energy),
 "feedback": ("Negative feedback loop", "Every homeostatic mechanism in the course maps onto this chain. Where a system fails, one element is missing, delayed, or mistuned.", fig_feedback),
}


def figure(key):
    t, cap, fn = FIGS[key]
    return f'<figure>{fn()}<figcaption><b>Figure.</b> {E(t)}. {E(cap)}</figcaption></figure>'


# ------------------------------------------------------------- lecture page --
def build_lecture(ch, head, banner, hero_light, light_footer, page_js, css):
    nxt = plan.PLAN[1]
    nav = "".join(f'<a href="#{s["id"]}">§{s["num"]}</a>' for s in L.SECTIONS)
    secs = []
    for s in L.SECTIONS:
        checks = "".join(f'<details class="ans"><summary>Check yourself: {q}</summary><div class="a"><p>{a}</p></div></details>' for q, a in s["checks"])
        fig = figure(s["figure"]) if s.get("figure") else ""
        secs.append(f'<section class="ch" id="{s["id"]}">\n  <h2><span class="num">§{s["num"]}</span>{E(s["title"])}</h2>\n{s["html"]}{fig}\n<h3>Check yourself</h3>{checks}\n</section>')
    cheat = "".join(f'<tr><td><b>{E(k)}</b></td><td>{v}</td></tr>' for k, v in L.CHEAT)
    chips = ('<span>🎯 CO1</span><span>📚 OpenStax Biology 2e, Ch. 1–3, 6, 8</span><span>🗂️ Portfolio Entry 1</span>'
             '<span>📖 10 sections · 5 figures · 26 check-yourself items</span>')
    blurb = ("A full first lecture: how biology reasons, what distinguishes living from non-living systems, the hierarchy from atom to biosphere, "
             "the chemistry of carbon and water, the four macromolecules, the thermodynamics that constrain life, feedback control, and the "
             "ecology of energy and matter — each section closing with the astrobiological question it raises.")
    out = head("Week 1 Lecture · Overview of Biological Science and the Chemistry of Life · ASTBIO 201", css,
               "ASTBIO 201 Week 1 lecture: scientific inquiry, characteristics and levels of life, atoms and water, macromolecules, energy and enzymes, homeostasis, ecology, and the astrobiology thread.")
    out += banner() + '<div class="progress" id="progress"></div>\n'
    out += hero_light(ch, "lecture", "Lecture Notes", blurb, chips)
    out += f"""<nav class="top" aria-label="Lecture sections"><div class="in">
  <a href="../index.html" class="home">⌂ Home</a><a href="#why">Why it matters</a>{nav}<a href="#cheat">Cheat sheet</a><a href="#class">In class</a>
</div></nav>
<main>
<section class="ch accent" id="why">
  <h2><span class="num">§</span>Why this week matters for astrobiology</h2>
  <div class="callout"><span class="label">Course thread</span>Astrobiology cannot search for life without an operational definition of it. Everything in this first week is a working definition under construction: if a probe returns a chemical pattern from Enceladus, the criteria you build here are the criteria you will argue from.</div>
  <ul class="checks">
    <li><b>Learning outcome.</b> {E(ch['outcome'])}</li>
    <li><b>Course outcomes served.</b> CO1 (enabled), with PO1 scientific knowledge, PO2 inquiry, PO3 systems reasoning, and PO5 lifelong learning introduced.</li>
    <li><b>How to use these notes.</b> Read each section, then answer its <b>Check yourself</b> items before opening them. The cheat sheet at the end is for revision, not first reading.</li>
    <li><b>Required output.</b> {E(ch['output'])} — specification in §1.10.</li>
  </ul>
  <div class="btnrow"><button class="btn ghost" onclick="toggleAll(true)">Open all checks</button><button class="btn ghost" onclick="toggleAll(false)">Close all</button><a class="btn" href="../exercises/ch01-exercises.html">✍️ Go to the 30-item test</a></div>
</section>
{chr(10).join(secs)}
<section class="ch accent" id="cheat">
  <h2><span class="num">§</span>Week 1 cheat sheet</h2>
  <div class="tw"><table><thead><tr><th style="width:22%">Topic</th><th>Remember</th></tr></thead><tbody>{cheat}</tbody></table></div>
</section>
<section class="ch" id="class">
  <h2><span class="num">§</span>In class this week</h2>
  <dl class="plan">
    <dt>Topics</dt><dd>{E(ch['topics'])}</dd><dt>Activities</dt><dd>{E(ch['tla'])}</dd><dt>Resources</dt><dd>{E(ch['resources'])}</dd>
    <dt>Assessment</dt><dd>{E(ch['assessment'])}</dd><dt>Evaluation</dt><dd>{E(ch['evaluation'])}</dd><dt>Output</dt><dd>{E(ch['output'])}</dd>
  </dl>
  <div class="btnrow"><a class="btn" href="../exercises/ch01-exercises.html">✍️ Week 1 exercises · 30-item test</a><button class="btn ghost" onclick="window.print()">Print / PDF</button></div>
  <div class="chnav"><a href="../index.html">⌂ Course Home</a><a href="../syllabus.html">📄 Syllabus</a><a class="next" href="{nxt['slug']}.html">Next: Week {nxt['week']} · {E(nxt['short'])} →</a></div>
</section>
</main>
"""
    out += light_footer("Week 1 Lecture Notes: Overview of Biological Science and the Chemistry of Life") + page_js + "\n</body>\n</html>\n"
    return out


# ------------------------------------------------------------ exercise page --
def balanced(items, seed):
    rnd = random.Random(seed); k = len(items); off = seed % 4
    base = [(i+off) % 4 for i in range(k)]
    for _ in range(600):
        rnd.shuffle(base)
        if all(base[i] != base[i+1] for i in range(k-1)): break
    out = []
    for idx, (it, tgt) in enumerate(zip(items, base)):
        r = random.Random(seed*1000+idx); opts = list(it["opts"]); correct = opts[it["a"]]
        rest = [o for i, o in enumerate(opts) if i != it["a"]]; r.shuffle(rest)
        new = rest[:tgt] + [correct] + rest[tgt:]; assert new[tgt] == correct
        d = dict(it); d["opts"] = new; d["a"] = tgt; out.append(d)
    return out


def build_exercises(ch, head, banner, hero_light, light_footer, page_js, css):
    items = balanced(X.ITEMS, seed=1501); letters = "ABCD"; nxt = plan.PLAN[1]
    roman = {1: "I", 2: "II", 3: "III", 4: "IV"}
    blocks_html = []; n = 0; ranges = {}
    for bnum, btitle, bref in X.BLOCKS:
        qs = []; start = n+1
        for it in [i for i in items if i["block"] == bnum]:
            n += 1
            opts = "".join(f'<label data-v="{letters[j]}"><input type="radio" name="q{n}" value="{letters[j]}"><b>{letters[j]}.</b><span>{o}</span></label>' for j, o in enumerate(it["opts"]))
            qs.append(f"""  <div class="q" data-a="{letters[it['a']]}"><div class="head"><span class="n">{n}.</span><span class="topic">{E(it['topic'])}</span><span class="tag {it['tag']}">{it['tag'].capitalize()}</span></div>
    <div class="stem"><p>{it['q']}</p></div>
    <div class="opts">{opts}</div>
    <details class="ans"><summary>Reveal answer and explanation</summary><div class="a"><p><span class="final">Correct answer: {letters[it['a']]}</span></p><p>{it['why']}</p></div></details>
  </div>""")
        ranges[bnum] = (start, n)
        blocks_html.append(f'<section class="ch" id="t{bnum}">\n  <h2><span class="num">{roman[bnum]}</span>{E(btitle)} <span class="tag pts">Items {start}–{n}</span></h2>\n  <p class="lead">Lecture reference: {bref}.</p>\n{chr(10).join(qs)}\n</section>')
    tasks = "".join(f"""  <div class="prob"><div class="head"><span class="n">Task {j}</span><span class="t">{E(t)}</span><span class="tag create">Create</span></div>
    <div class="body"><p>{E(p)}</p></div>
    <details class="ans"><summary>Instructor note and grading focus</summary><div class="a"><p>{E(g)}</p></div></details>
  </div>""" for j, (t, p, g) in enumerate(X.PORTFOLIO, 1))
    nav = "".join(f'<a href="#t{b}">{roman[b]} · {E(t.split(",")[0])}</a>' for b, t, _ in X.BLOCKS)
    tmap = " ".join(f"Items {ranges[b][0]}–{ranges[b][1]} · {E(t.lower())} ({r}).</b>" if False else f"Items {ranges[b][0]}–{ranges[b][1]} · {E(t.lower())} ({r})." for b, t, r in X.BLOCKS)
    chips = '<span>🧠 Analyze · Evaluate · Create</span><span>✍️ 30 items · 4 topic blocks</span><span>🔽 Answer + explanation per item</span><span>📊 Optional self-score</span><span>🗂️ 3 portfolio tasks</span>'
    blurb = ("Thirty multiple-choice items on the week's core: scientific inquiry and the characteristics and levels of life; atoms, bonds, and water; "
             "macromolecules, energy, and enzymes; homeostasis, ecology, and the astrobiology thread. None of the items can be answered by recall alone — "
             "each asks you to apply, analyze, or evaluate. Choose an answer first, then open the dropdown to check the answer and read why.")
    out = head("Week 1 Exercises · 30-Item HOTS Test · ASTBIO 201", css, "ASTBIO 201 Week 1 exercises: 30 higher-order multiple-choice items on inquiry, life's characteristics, chemistry of life, macromolecules, energy, homeostasis and ecology, with answers and explanations, plus portfolio tasks.")
    out += banner() + '<div class="progress" id="progress"></div>\n'
    out += hero_light(ch, "exercises", "30-Item HOTS Test", blurb, chips)
    out += f"""<nav class="top" aria-label="Test sections"><div class="in">
  <a href="../index.html" class="home">⌂ Home</a><a href="#how">Directions</a>{nav}<a href="#t5">V · Portfolio</a><a href="#score-box">Score</a>
</div></nav>
<main>
<section class="ch accent" id="how">
  <h2><span class="num">§</span>Directions</h2>
  <ul class="checks">
    <li>Each item has exactly <b>one</b> best answer. Read all four options before choosing — several are designed to be "almost right".</li>
    <li>Decide and mark your answer <b>before</b> opening the dropdown. The explanation tells you why the correct option is right <em>and</em> why the popular wrong ones are wrong.</li>
    <li>A periodic table and light arithmetic are all you need. Items reference lecture sections by § number so you can go back to what you missed.</li>
    <li>Press <b>Check my answers</b> at the end for a score. This is for self-review; it is not recorded.</li>
  </ul>
  <div class="btnrow"><button class="btn ghost" onclick="toggleAll(true)">Open all explanations</button><button class="btn ghost" onclick="toggleAll(false)">Close all</button><button class="btn" onclick="window.print()">Print / PDF</button></div>
</section>
{chr(10).join(blocks_html)}
<section class="ch" id="t5">
  <h2><span class="num">V</span>Portfolio and applied tasks <span class="tag pts">Graded outputs</span></h2>
  <p class="lead">These produce the syllabus output for Week 1: <b>{E(ch['output'])}</b> Evaluation: {E(ch['evaluation'])}</p>
{tasks}
</section>
<section class="ch accent" id="score-box">
  <h2><span class="num">§</span>Check Your Score</h2>
  <p class="lead">Answer all thirty items, then press the button. Items are marked green (correct) or red (incorrect, with the correct option outlined) so you know which explanations to study.</p>
  <div class="btnrow"><button class="btn" onclick="gradeAll()">Check my answers</button><button class="btn ghost" onclick="resetAll()">Reset</button><span id="score"></span></div>
  <div class="tw"><table>
    <thead><tr><th>Score</th><th>Interpretation</th><th>Suggested next step</th></tr></thead>
    <tbody>
      <tr><td><b>27–30</b></td><td>Mastery of the Week 1 core</td><td>Complete Portfolio Entry 1 and move to Week 2, Cell Structure and Function</td></tr>
      <tr><td><b>21–26</b></td><td>Solid, with a few specific gaps</td><td>Re-read the lecture sections cited for the items you missed; redo those items after a day</td></tr>
      <tr><td><b>15–20</b></td><td>Concepts partly formed</td><td>Review §1.2, §1.5, §1.7 and §1.8 with the figures; bring questions to consultation (by appointment)</td></tr>
      <tr><td><b>&lt; 15</b></td><td>Foundations need rebuilding</td><td>Work through the lecture's Check-yourself items first, then retake this test</td></tr>
    </tbody>
  </table></div>
  <div class="callout blue"><span class="label">Topic map</span>{tmap}</div>
  <div class="chnav">
    <a href="../chapters/ch01.html">← Week 1 Lecture</a>
    <a href="../index.html">⌂ Course Home</a>
    <a class="next" href="{nxt['slug']}-exercises.html">Next: Week {nxt['week']} · {E(nxt['short'])} →</a>
  </div>
</section>
</main>
"""
    out += light_footer("Week 1 Exercises: 30-Item HOTS Test") + page_js
    out += """
<script>
  function gradeAll(){
    const qs=[...document.querySelectorAll('.q')]; let score=0, answered=0;
    qs.forEach(q=>{ q.classList.remove('right','wrong'); q.querySelectorAll('label').forEach(l=>l.classList.remove('correct','chosen'));
      const sel=q.querySelector('input:checked'); if(sel) answered++;
      if(sel && sel.value===q.dataset.a){ score++; q.classList.add('right'); }
      else { q.classList.add('wrong'); q.querySelector('label[data-v="'+q.dataset.a+'"]').classList.add('correct'); if(sel) sel.closest('label').classList.add('chosen'); } });
    const el=document.getElementById('score');
    el.textContent=`Score: ${score} / ${qs.length}` + (answered<qs.length?` (${qs.length-answered} unanswered)`:'') + (score>=27?' — mastery':score>=21?' — solid':score>=15?' — review needed':' — rebuild foundations');
  }
  function resetAll(){ document.querySelectorAll('.q input').forEach(i=>i.checked=false); document.querySelectorAll('.q').forEach(q=>{q.classList.remove('right','wrong'); q.querySelectorAll('label').forEach(l=>l.classList.remove('correct','chosen'));}); document.getElementById('score').textContent=''; }
</script>
</body>
</html>
"""
    return out
