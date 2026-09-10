# -*- coding: utf-8 -*-
"""Generic renderers for full-depth chapter lectures and 30-item exercise sets.
Each chapter supplies a lecture module (SECTIONS, FIGS, CHEAT, BRIDGE, CHIPS, BLURB, CO_LINE, REVIEW_SECTIONS)
and an items module (BLOCKS, ITEMS, PORTFOLIO)."""
import html, random
import meta, plan

E = lambda s: html.escape(str(s), quote=True)
FONT = 'font-family="-apple-system,Segoe UI,Inter,Roboto,Arial,sans-serif"'

def figure(L, key):
    t, cap, fn = L.FIGS[key]
    return f'<figure>{fn()}<figcaption><b>Figure.</b> {E(t)}. {E(cap)}</figcaption></figure>'


# ------------------------------------------------------------- lecture page --
def build_lecture(ch, L, head, banner, hero_light, light_footer, page_js, css):
    idx = [c["slug"] for c in plan.PLAN].index(ch["slug"]); nxt = plan.PLAN[idx+1] if idx+1 < len(plan.PLAN) else None; prv = plan.PLAN[idx-1] if idx else None; wk = ch["week"]
    nav = "".join(f'<a href="#{s["id"]}">§{s["num"]}</a>' for s in L.SECTIONS)
    secs = []
    for s in L.SECTIONS:
        checks = "".join(f'<details class="ans"><summary>Check yourself: {q}</summary><div class="a"><p>{a}</p></div></details>' for q, a in s["checks"])
        fig = figure(L, s["figure"]) if s.get("figure") else ""
        secs.append(f'<section class="ch" id="{s["id"]}">\n  <h2><span class="num">§{s["num"]}</span>{E(s["title"])}</h2>\n{s["html"]}{fig}\n<h3>Check yourself</h3>{checks}\n</section>')
    cheat = "".join(f'<tr><td><b>{E(k)}</b></td><td>{v}</td></tr>' for k, v in L.CHEAT)
    chips, blurb = L.CHIPS, L.BLURB
    out = head(f"Week {wk} Lecture · {ch['title']} · ASTBIO 201", css, f"ASTBIO 201 Week {wk} lecture: {ch['title']}. {ch['outcome']}")
    out += banner() + '<div class="progress" id="progress"></div>\n'
    out += hero_light(ch, "lecture", "Lecture Notes", blurb, chips)
    out += f"""<nav class="top" aria-label="Lecture sections"><div class="in">
  <a href="../index.html" class="home">⌂ Home</a><a href="#why">Why it matters</a>{nav}<a href="#cheat">Cheat sheet</a><a href="#class">In class</a>
</div></nav>
<main>
<section class="ch accent" id="why">
  <h2><span class="num">§</span>Why this week matters for astrobiology</h2>
  <div class="callout"><span class="label">Course thread</span>{E(L.BRIDGE)}</div>
  <ul class="checks">
    <li><b>Learning outcome.</b> {E(ch['outcome'])}</li>
    <li><b>Course outcomes served.</b> {L.CO_LINE}</li>
    <li><b>How to use these notes.</b> Read each section, then answer its <b>Check yourself</b> items before opening them. The cheat sheet at the end is for revision, not first reading.</li>
    <li><b>Required output.</b> {E(ch['output'])} — specification in the final section.</li>
  </ul>
  <div class="btnrow"><button class="btn ghost" onclick="toggleAll(true)">Open all checks</button><button class="btn ghost" onclick="toggleAll(false)">Close all</button><a class="btn" href="../exercises/{ch['slug']}-exercises.html">✍️ Go to the 30-item test</a></div>
</section>
{chr(10).join(secs)}
<section class="ch accent" id="cheat">
  <h2><span class="num">§</span>Week {wk} cheat sheet</h2>
  <div class="tw"><table><thead><tr><th style="width:22%">Topic</th><th>Remember</th></tr></thead><tbody>{cheat}</tbody></table></div>
</section>
<section class="ch" id="class">
  <h2><span class="num">§</span>In class this week</h2>
  <dl class="plan">
    <dt>Topics</dt><dd>{E(ch['topics'])}</dd><dt>Activities</dt><dd>{E(ch['tla'])}</dd><dt>Resources</dt><dd>{E(ch['resources'])}</dd>
    <dt>Assessment</dt><dd>{E(ch['assessment'])}</dd><dt>Evaluation</dt><dd>{E(ch['evaluation'])}</dd><dt>Output</dt><dd>{E(ch['output'])}</dd>
  </dl>
  <div class="btnrow"><a class="btn" href="../exercises/{ch['slug']}-exercises.html">✍️ Week {wk} exercises · 30-item test</a><button class="btn ghost" onclick="window.print()">Print / PDF</button></div>
  <div class="chnav">{'<a href="'+prv['slug']+'.html">← Week '+str(prv['week'])+' · '+E(prv['short'])+'</a>' if prv else '<a href="../index.html">⌂ Course Home</a>'}<a href="../syllabus.html">📄 Syllabus</a>{'<a class="next" href="'+nxt['slug']+'.html">Next: Week '+str(nxt['week'])+' · '+E(nxt['short'])+' →</a>' if nxt else '<a class="next" href="../index.html">⌂ Course Home →</a>'}</div>
</section>
</main>
"""
    out += light_footer(f"Week {wk} Lecture Notes: {ch['title']}") + page_js + "\n</body>\n</html>\n"
    return out


# ------------------------------------------------------------ exercise page --
def balanced(items, seed):
    """Permute each item's options so keys are spread evenly across A-D with no two consecutive equal."""
    rnd = random.Random(seed); k = len(items); off = seed % 4
    base = [(i+off) % 4 for i in range(k)]
    rnd.shuffle(base)
    for _ in range(50):  # repair pass: swap a duplicate with a later position that breaks no adjacency
        fixed = True
        for i in range(k-1):
            if base[i] == base[i+1]:
                for j in range(i+2, k):
                    if base[j] != base[i] and (j == k-1 or base[j+1] != base[i]) and base[j-1] != base[i+1] and (j+1 >= k or base[j+1] != base[i+1]):
                        base[i+1], base[j] = base[j], base[i+1]; break
                fixed = False
        if fixed: break
    assert all(base[i] != base[i+1] for i in range(k-1)), "could not balance keys"
    out = []
    for idx, (it, tgt) in enumerate(zip(items, base)):
        r = random.Random(seed*1000+idx); opts = list(it["opts"]); correct = opts[it["a"]]
        rest = [o for i, o in enumerate(opts) if i != it["a"]]; r.shuffle(rest)
        new = rest[:tgt] + [correct] + rest[tgt:]; assert new[tgt] == correct
        d = dict(it); d["opts"] = new; d["a"] = tgt; out.append(d)
    return out


def build_exercises(ch, L, X, head, banner, hero_light, light_footer, page_js, css):
    idx = [c["slug"] for c in plan.PLAN].index(ch["slug"]); nxt = plan.PLAN[idx+1] if idx+1 < len(plan.PLAN) else None; wk = ch["week"]
    items = balanced(X.ITEMS, seed=1500+wk); letters = "ABCD"
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
    blurb = (f"Thirty multiple-choice items on the week's core: {X.SCOPE} None of the items can be answered by recall alone — "
             "each asks you to apply, analyze, or evaluate. Choose an answer first, then open the dropdown to check the answer and read why.")
    out = head(f"Week {wk} Exercises · 30-Item HOTS Test · ASTBIO 201", css, f"ASTBIO 201 Week {wk} exercises: 30 higher-order multiple-choice items on {ch['title']}, with answers and explanations, plus portfolio tasks.")
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
  <p class="lead">These produce the syllabus output for Week {wk}: <b>{E(ch['output'])}</b> Evaluation: {E(ch['evaluation'])}</p>
{tasks}
</section>
<section class="ch accent" id="score-box">
  <h2><span class="num">§</span>Check Your Score</h2>
  <p class="lead">Answer all thirty items, then press the button. Items are marked green (correct) or red (incorrect, with the correct option outlined) so you know which explanations to study.</p>
  <div class="btnrow"><button class="btn" onclick="gradeAll()">Check my answers</button><button class="btn ghost" onclick="resetAll()">Reset</button><span id="score"></span></div>
  <div class="tw"><table>
    <thead><tr><th>Score</th><th>Interpretation</th><th>Suggested next step</th></tr></thead>
    <tbody>
      <tr><td><b>27–30</b></td><td>Mastery of the Week {wk} core</td><td>Complete the portfolio tasks and move to {('Week '+str(nxt['week'])+', '+E(nxt['title'])) if nxt else 'the final examination'}</td></tr>
      <tr><td><b>21–26</b></td><td>Solid, with a few specific gaps</td><td>Re-read the lecture sections cited for the items you missed; redo those items after a day</td></tr>
      <tr><td><b>15–20</b></td><td>Concepts partly formed</td><td>Review {L.REVIEW_SECTIONS} with the figures; bring questions to consultation (by appointment)</td></tr>
      <tr><td><b>&lt; 15</b></td><td>Foundations need rebuilding</td><td>Work through the lecture's Check-yourself items first, then retake this test</td></tr>
    </tbody>
  </table></div>
  <div class="callout blue"><span class="label">Topic map</span>{tmap}</div>
  <div class="chnav">
    <a href="../chapters/{ch['slug']}.html">← Week {wk} Lecture</a>
    <a href="../index.html">⌂ Course Home</a>
    {'<a class="next" href="'+nxt['slug']+'-exercises.html">Next: Week '+str(nxt['week'])+' · '+E(nxt['short'])+' →</a>' if nxt else '<a class="next" href="../syllabus.html">Syllabus →</a>'}
  </div>
</section>
</main>
"""
    out += light_footer(f"Week {wk} Exercises: 30-Item HOTS Test") + page_js
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
