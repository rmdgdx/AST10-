# -*- coding: utf-8 -*-
"""Week 1 full lecture — Overview of Biological Science and the Chemistry of Life.
HTML fragments use the site's LIGHT_CSS classes. Figures are inline SVG built in build.py."""

import html, math
E = lambda s: html.escape(str(s), quote=True)
FONT = 'font-family="-apple-system,Segoe UI,Inter,Roboto,Arial,sans-serif"'

SECTIONS = []  # list of dicts: id, num, title, html, figure (optional key), checks (list of (q, a))

SECTIONS.append(dict(id="s1", num="1.1", title="How biology knows: scientific inquiry", figure="method",
 html="""
<p class="lead">Biology is not a list of facts about organisms; it is a method for finding out which claims about organisms survive testing. Everything in this course, up to and including the question of whether a Martian sample contains life, is decided by that method.</p>
<p>Inquiry begins with an <b>observation</b> that does not fit what is already known, and a <b>question</b> that makes the mismatch explicit. A <b>hypothesis</b> is a tentative, testable explanation. It must be <b>falsifiable</b>: it must forbid some possible observation, so that the observation, if made, would count against it. "Extremophiles are amazing" forbids nothing and is not a hypothesis; "Strain X grows at 90 °C in medium Y" forbids a plate that stays clear at 90 °C.</p>
<p>From a hypothesis you derive a <b>prediction</b> in if–then form, then design a test. In a <b>controlled experiment</b> you change one <b>independent variable</b>, measure one <b>dependent variable</b>, and hold everything else (the <b>controlled variables</b>) constant. The <b>control group</b> receives no treatment or a standard treatment, and its job is to show what happens when the independent variable is absent. Without it a result cannot be attributed to the treatment.</p>
<div class="callout blue"><span class="label">Worked example · designing a test</span>
<b>Claim:</b> a bacterium isolated from a hot spring grows at 90 °C.<br>
<b>Hypothesis:</b> the isolate is a hyperthermophile capable of growth (not merely survival) at 90 °C.<br>
<b>Prediction:</b> if cultures are incubated at 90 °C in a medium in which the isolate grows at 70 °C, then cell density will increase over 48 h; if the isolate only survives, density will stay flat.<br>
<b>Design:</b> independent variable = incubation temperature (70 °C reference, 90 °C test). Dependent variable = optical density at 600 nm every 6 h. Controls: sterile medium at each temperature (detects contamination), identical medium and inoculum size, three replicate tubes per condition.<br>
<b>Decision rule, stated in advance:</b> growth is claimed only if mean OD at 90 °C rises by more than the between-replicate standard deviation and the sterile control stays clear.</div>
<p>Two habits separate strong inquiry from weak. First, <b>correlation is not causation</b>: two variables that move together may share a hidden cause or be related by chance. Second, results are reported with their <b>uncertainty</b>: replicates, variability, and the decision rule that was set before the data came in. A rule written after seeing the data is not a test; it is a story.</p>
<div class="tw"><table>
<thead><tr><th>Term</th><th>What it is</th><th>What it is not</th></tr></thead>
<tbody>
<tr><td><b>Hypothesis</b></td><td>A testable, falsifiable explanation for a specific observation</td><td>A guess with no forbidden outcome; a prediction</td></tr>
<tr><td><b>Prediction</b></td><td>The observable consequence a hypothesis implies under stated conditions</td><td>The hypothesis itself</td></tr>
<tr><td><b>Theory</b></td><td>A broad, well-supported explanatory framework that has survived many independent tests (cell theory, evolution by natural selection)</td><td>"Just a guess"; a hypothesis that has been promoted</td></tr>
<tr><td><b>Law</b></td><td>A concise description of a regularity, often mathematical (Mendel's law of segregation)</td><td>An explanation of why the regularity exists</td></tr>
<tr><td><b>Model</b></td><td>A simplified representation used to reason and predict (a cell diagram, a feedback loop, an equation)</td><td>A claim that reality is exactly like the model</td></tr>
</tbody></table></div>
<p>Two modes of reasoning operate together. <b>Inductive</b> reasoning moves from many observations to a general statement (every cell examined has a membrane, so all cells have membranes). <b>Deductive</b> reasoning moves from a general statement to a specific prediction (if all cells have membranes, this new cell will have one). Discovery science is largely inductive; hypothesis testing is deductive.</p>
""",
 checks=[
  ("Rewrite 'Plants like light' as a falsifiable hypothesis with a prediction.", "Hypothesis: seedlings of species S grow taller under 16 h of light than under 8 h. Prediction: if 20 seedlings are grown under each regime for 14 days with identical water and soil, mean height will be greater in the 16 h group. The forbidden outcome is equal or shorter height."),
  ("A study finds towns with more churches have more crime. What is the likely hidden variable?", "Population size. Larger towns have more of both. This is a lurking (confounding) variable producing a correlation with no causal link."),
  ("Why is cell theory called a theory rather than a law?", "It explains (all organisms are built from cells; cells arise from cells) rather than merely describing a regularity, and it has been supported by an enormous body of independent evidence."),
 ]))

SECTIONS.append(dict(id="s2", num="1.2", title="What counts as alive: the characteristics of life",
 html="""
<p class="lead">No single property defines life. Biology uses a cluster of properties, and every one of them has a non-living mimic. Understanding the cluster, and its failures, is the first task of astrobiology.</p>
<div class="tw"><table>
<thead><tr><th>Property</th><th>What it means</th><th>Non-living system that shows it</th></tr></thead>
<tbody>
<tr><td><b>Order</b></td><td>Highly organised structure at every scale, from molecules to organs</td><td>A snowflake; a salt crystal</td></tr>
<tr><td><b>Metabolism</b></td><td>Acquiring energy and matter and transforming them to build and maintain structure</td><td>A candle flame consumes fuel and oxygen and releases heat</td></tr>
<tr><td><b>Growth and development</b></td><td>Increase in size and change in form under heritable instructions</td><td>A crystal grows by accretion; a river delta develops</td></tr>
<tr><td><b>Response to stimuli</b></td><td>Detecting and reacting to changes in the environment</td><td>A thermostat; a flame bending in the wind</td></tr>
<tr><td><b>Homeostasis</b></td><td>Regulating the internal environment within limits despite external change</td><td>A cruise-control system holding speed</td></tr>
<tr><td><b>Reproduction</b></td><td>Producing new individuals of the same kind</td><td>A fire spreads; a computer virus copies itself</td></tr>
<tr><td><b>Heredity</b></td><td>Passing information to offspring in a molecular code</td><td>A photocopier copies a page (but does not vary it)</td></tr>
<tr><td><b>Evolutionary adaptation</b></td><td>Populations change across generations as heritable variation meets differential reproduction</td><td>None convincingly; this is the property with no good abiotic mimic</td></tr>
</tbody></table></div>
<p>Because each property alone can be mimicked, biology treats the set as a <b>family resemblance</b> rather than a checklist. The last row is the exception, and it is why NASA's working definition, <em>a self-sustaining chemical system capable of Darwinian evolution</em>, singles out evolution. It is the one property that generates open-ended complexity, and no purely physical process is known to do so.</p>
<div class="callout"><span class="label">Why the definition matters operationally</span>A definition tells an instrument designer what to measure. If "life" means Darwinian evolution, a probe must look for heritable variation, which is impossible in a single flyby. If "life" means metabolism, a probe can look for sustained chemical disequilibrium, which is measurable. Every mission trades philosophical completeness for measurability, and the trade must be stated.</div>
<p><b>Viruses</b> sit on the boundary. They carry heritable information and evolve, but have no metabolism of their own and cannot reproduce outside a host cell. Most biologists classify them as non-living but biologically active. The disagreement is not a failure of knowledge; it is a demonstration that "alive" is a category we impose on a continuum.</p>
<p>The <b>unity and diversity</b> of life are both evidence. All known organisms share the same genetic code, the same set of 20 amino acids, the same ATP energy currency, and lipid-bilayer membranes. That unity argues for a single common ancestor. The diversity, on the order of 8.7 million eukaryotic species by one estimate and an unknown but far larger number of prokaryotes, is the outcome of roughly 3.8 billion years of descent with modification.</p>
""",
 checks=[
  ("A student says a self-driving car is alive because it responds to stimuli, maintains its speed, and can be copied. Which property is missing, and why does it matter?", "Heritable variation acted on by selection. The car does not produce offspring whose heritable traits vary and are differentially retained, so it cannot evolve. Without that, the other properties are engineering, not biology."),
  ("Why do most biologists not classify viruses as living?", "They have no metabolism of their own, no cellular structure, and cannot reproduce without hijacking a host cell's machinery. They satisfy heredity and evolution but not the properties that require an energy-transforming, bounded system."),
 ]))

SECTIONS.append(dict(id="s3", num="1.3", title="Levels of biological organisation and emergent properties", figure="levels",
 html="""
<p class="lead">Life is organised in a hierarchy, and each level has properties that the components below it do not have. This is the idea of <b>emergence</b>, and it is why biology cannot be replaced by chemistry even though it is built from it.</p>
<p>From the bottom: <b>atoms</b> combine into <b>molecules</b>; molecules assemble into <b>organelles</b>; organelles and membranes form the <b>cell</b>, the smallest unit that is unambiguously alive; cells of a similar type form <b>tissues</b>; tissues combine into <b>organs</b>; organs cooperate in <b>organ systems</b>; systems constitute the <b>organism</b>. Above the individual: a <b>population</b> is all individuals of a species in an area; a <b>community</b> is all the populations in an area; an <b>ecosystem</b> is a community plus its physical environment; and the <b>biosphere</b> is the sum of all ecosystems, the portion of the planet where life occurs.</p>
<div class="callout blue"><span class="label">Emergence, concretely</span>A single phospholipid has no concentration gradient. A bilayer of phospholipids does, because it separates an inside from an outside. Nothing new was added; the gradient emerged from arrangement. The same logic applies at every level: a heart beats, but no cardiac cell "beats" on its own in the sense of pumping blood.</div>
<p>Two complementary strategies follow. <b>Reductionism</b> breaks systems into parts and studies the parts; it produced molecular biology. <b>Systems biology</b> studies how the parts interact to produce the behaviour of the whole; it produces models of metabolism, gene networks, and ecosystems. Neither is sufficient alone. Astrobiology needs both: reductionist chemistry to say what molecules could form on early Earth, and systems thinking to say how they could organise into something that maintains itself.</p>
<p>The hierarchy also explains why <b>the cell</b> is the focus of life detection. Below it, one is looking at chemistry that could be abiotic; at it, one is looking at bounded compartments that maintain a difference from their surroundings, which is the physical signature that a chemical system is doing work against equilibrium.</p>
""",
 checks=[
  ("Give one emergent property at the tissue level that is absent at the cell level.", "Coordinated contraction (cardiac muscle) or directional transport (ciliated epithelium). Individual cells contract or beat, but the organised, directional, whole-tissue behaviour requires their arrangement and coupling."),
  ("Is a lake an ecosystem or a community?", "An ecosystem: it includes the physical environment (water, dissolved gases, sediment, light) as well as all the living populations. The community would be only the organisms."),
 ]))

SECTIONS.append(dict(id="s4", num="1.4", title="Atoms, elements, and the bonds of life",
 html="""
<p class="lead">About 25 elements are essential to life, but six, carbon, hydrogen, nitrogen, oxygen, phosphorus, and sulfur (<b>CHNOPS</b>), make up roughly 97 per cent of living mass. Why these six, and what they do, is chemistry that transfers directly to any planet.</p>
<div class="tw"><table>
<thead><tr><th>Element</th><th>Approx. % of human body mass</th><th>Principal biological roles</th></tr></thead>
<tbody>
<tr><td>Oxygen (O)</td><td class="c">65</td><td>Water; final electron acceptor in aerobic respiration; in every macromolecule class</td></tr>
<tr><td>Carbon (C)</td><td class="c">18.5</td><td>Backbone of all organic molecules</td></tr>
<tr><td>Hydrogen (H)</td><td class="c">9.5</td><td>Water; hydrogen bonds; proton gradients that make ATP</td></tr>
<tr><td>Nitrogen (N)</td><td class="c">3.3</td><td>Amino acids and proteins; nucleotides and nucleic acids</td></tr>
<tr><td>Calcium, phosphorus, potassium, sulfur, sodium, chlorine, magnesium</td><td class="c">~3.7 combined</td><td>Bone, ATP and nucleic acids (P), nerve signalling (Na, K, Ca), protein structure (S), chlorophyll (Mg)</td></tr>
<tr><td>Trace elements (Fe, I, Zn, Cu, Mn, Se, Mo, …)</td><td class="c">&lt; 0.01 each</td><td>Enzyme cofactors; oxygen transport (Fe); thyroid hormone (I)</td></tr>
</tbody></table></div>
<p>An atom's chemistry is set by its <b>valence electrons</b>. Atoms with incomplete outer shells react to complete them. <b>Covalent bonds</b> share electron pairs and hold molecules together; they are strong (roughly 300–400 kJ/mol for C–C and C–H). <b>Ionic bonds</b> form when one atom transfers electrons to another and the resulting ions attract; in water they are relatively weak because water molecules surround and separate the ions. <b>Hydrogen bonds</b> are weak (about 20 kJ/mol) attractions between a hydrogen that is covalently bonded to O or N and another electronegative atom; individually trivial, collectively they hold DNA strands together and give water its properties. <b>Van der Waals</b> interactions are transient attractions between nearby molecules, individually weaker still but significant in aggregate.</p>
<p><b>Electronegativity</b> decides whether a covalent bond is <b>polar</b>. Oxygen and nitrogen pull shared electrons strongly; carbon and hydrogen pull about equally. So C–H bonds are nonpolar and O–H and N–H bonds are polar, with partial charges. Molecules rich in C–H are <b>hydrophobic</b>; molecules rich in O–H, N–H, and charged groups are <b>hydrophilic</b>. That single distinction organises membranes, protein folding, and solubility.</p>
<div class="callout"><span class="label">Why carbon</span>Carbon has four valence electrons and forms four covalent bonds. It bonds stably to itself in chains, branches, and rings, with single, double, and triple bonds, so an effectively unlimited number of stable structures exist. Silicon also has four valence electrons, but Si–Si bonds are weaker, Si–O bonds are far stronger than Si–Si (so silicon chemistry in water tends toward silicates rather than chains), and silicon's analogue of CO<sub>2</sub> is a solid. Life "as we know it" is carbon-based for reasons of bond chemistry, not abundance: there is more silicon than carbon in Earth's crust.</div>
<p>Organic molecules are made distinctive by <b>functional groups</b>, small clusters of atoms attached to a carbon skeleton.</p>
<div class="tw"><table>
<thead><tr><th>Functional group</th><th>Structure</th><th>Property conferred</th><th>Found in</th></tr></thead>
<tbody>
<tr><td>Hydroxyl</td><td>–OH</td><td>Polar; hydrophilic; forms hydrogen bonds</td><td>Sugars, alcohols</td></tr>
<tr><td>Carbonyl</td><td>C=O</td><td>Polar; reactive; ketone (internal) or aldehyde (terminal)</td><td>Sugars</td></tr>
<tr><td>Carboxyl</td><td>–COOH</td><td>Acidic; releases H<sup>+</sup> to become –COO<sup>–</sup></td><td>Amino acids, fatty acids</td></tr>
<tr><td>Amino</td><td>–NH<sub>2</sub></td><td>Basic; accepts H<sup>+</sup> to become –NH<sub>3</sub><sup>+</sup></td><td>Amino acids</td></tr>
<tr><td>Sulfhydryl</td><td>–SH</td><td>Forms disulfide bridges that stabilise protein shape</td><td>Cysteine</td></tr>
<tr><td>Phosphate</td><td>–OPO<sub>3</sub><sup>2–</sup></td><td>Negatively charged; transfers energy</td><td>ATP, DNA, phospholipids</td></tr>
<tr><td>Methyl</td><td>–CH<sub>3</sub></td><td>Nonpolar; affects gene expression when added to DNA</td><td>Many molecules</td></tr>
</tbody></table></div>
""",
 checks=[
  ("Rank hydrogen bonds, covalent bonds, and ionic bonds in water by strength, and explain the position of ionic bonds.", "Covalent (strongest) > ionic in water > hydrogen bonds. Ionic bonds are strong in a dry crystal but weak in water because polar water molecules form hydration shells around each ion and pull them apart."),
  ("Predict whether a molecule with the formula C<sub>18</sub>H<sub>38</sub> dissolves in water.", "No. It is entirely C–H, nonpolar, and hydrophobic; it will aggregate away from water. It is a hydrocarbon (octadecane, a wax component)."),
 ]))

SECTIONS.append(dict(id="s5", num="1.5", title="Water: the solvent life is built around", figure="water",
 html="""
<p class="lead">Water's properties follow from one fact: the molecule is polar and forms hydrogen bonds. Each property below is a consequence, and each is a reason the search for habitable worlds is largely a search for liquid water.</p>
<p><b>Cohesion</b> (water to water) and <b>adhesion</b> (water to other polar surfaces) let water climb narrow tubes and let trees pull water tens of metres upward without a pump. <b>Surface tension</b>, the resistance of a liquid surface to being broken, is high for water for the same reason.</p>
<p><b>High specific heat</b> (4.18 J g<sup>–1</sup> °C<sup>–1</sup>) means a large energy input produces a small temperature change: hydrogen bonds absorb heat as they break and release it as they form. Oceans buffer planetary climate, and cells resist thermal shock, because of it. <b>High heat of vaporisation</b> (about 2,260 J g<sup>–1</sup>) means evaporation removes a great deal of heat, which is why sweating cools and why transpiration protects leaves.</p>
<p><b>Expansion on freezing</b>: ice is about 9 per cent less dense than liquid water because hydrogen bonds lock molecules into an open lattice. Ice floats and insulates the water below, so lakes and oceans do not freeze solid from the bottom up. On a cold world, an ice shell over a liquid ocean, as on Europa, is the same physics at planetary scale.</p>
<p><b>Solvent action</b>: water dissolves ionic compounds by surrounding each ion with a <b>hydration shell</b>, and dissolves polar molecules by hydrogen bonding to them. A solution's concentration is expressed in <b>molarity</b>: moles of solute per litre. One mole is 6.022 × 10<sup>23</sup> particles, and the mass of one mole in grams equals the molecular mass in daltons.</p>
<div class="callout blue"><span class="label">Worked example · preparing a solution</span>Glucose is C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>, molecular mass (6 × 12) + (12 × 1) + (6 × 16) = 180 Da, so 1 mol of glucose = 180 g. To make 0.5 L of a 0.1 M solution: 0.1 mol L<sup>–1</sup> × 0.5 L = 0.05 mol, and 0.05 mol × 180 g mol<sup>–1</sup> = <b>9 g of glucose</b> dissolved and made up to 500 mL.</div>
<p><b>Acids, bases, and pH.</b> Water dissociates slightly into H<sup>+</sup> (in practice hydronium, H<sub>3</sub>O<sup>+</sup>) and OH<sup>–</sup>; in pure water each is 10<sup>–7</sup> M. An <b>acid</b> raises the H<sup>+</sup> concentration; a <b>base</b> lowers it. <b>pH</b> is the negative log<sub>10</sub> of the H<sup>+</sup> concentration, so each pH unit is a tenfold change: pH 3 has 10,000 times more H<sup>+</sup> than pH 7.</p>
<span class="eq">pH = –log<sub>10</sub>[H<sup>+</sup>] &nbsp;&nbsp;&nbsp; [H<sup>+</sup>][OH<sup>–</sup>] = 10<sup>–14</sup> M<sup>2</sup> at 25 °C</span>
<p>Most cellular processes run near pH 7, and blood is held at 7.35–7.45 by <b>buffers</b>, substances that accept H<sup>+</sup> when it is in excess and donate it when it is scarce. The carbonic acid–bicarbonate pair is the main one in blood:</p>
<span class="eq">CO<sub>2</sub> + H<sub>2</sub>O ⇌ H<sub>2</sub>CO<sub>3</sub> ⇌ H<sup>+</sup> + HCO<sub>3</sub><sup>–</sup></span>
<p>This same equilibrium is why rising atmospheric CO<sub>2</sub> acidifies the ocean: more dissolved CO<sub>2</sub> pushes the reaction rightward, releasing H<sup>+</sup> and lowering pH, which in turn reduces carbonate available to shell-building organisms.</p>
<div class="callout"><span class="label">Astrobiology note · other solvents</span>Ammonia and methane are the usual candidates. Liquid ammonia is polar and forms hydrogen bonds, but is liquid only between –78 and –33 °C at 1 atm, where reactions run slowly. Methane and ethane, which pool on Titan, are nonpolar and would not support the ion chemistry water enables. Neither solvent is ruled out in principle, but each would require a chemistry with no known example. This is exactly why Titan is interesting.</div>
""",
 checks=[
  ("Sample A is pH 5 and sample B is pH 8. By what factor does H<sup>+</sup> concentration differ?", "10<sup>3</sup> = 1,000-fold. A is more acidic. Each unit is tenfold, and the samples differ by three units."),
  ("Explain why a pond with a thin ice cover in winter can still hold living fish.", "Ice is less dense than liquid water, so it forms at the surface and insulates the water beneath. Water reaches maximum density at 4 °C and sinks, so the bottom stays liquid and above freezing."),
  ("How many grams of NaCl (58.5 Da) make 250 mL of a 0.15 M solution?", "0.15 × 0.25 = 0.0375 mol; 0.0375 × 58.5 ≈ 2.2 g."),
 ]))

SECTIONS.append(dict(id="s6", num="1.6", title="The macromolecules of life",
 html="""
<p class="lead">Four classes of large molecule build every organism: carbohydrates, lipids, proteins, and nucleic acids. Three of the four are <b>polymers</b>, chains of repeating <b>monomers</b>, joined and broken by the same two reactions.</p>
<p><b>Dehydration synthesis</b> (condensation) joins two monomers by removing a water molecule; <b>hydrolysis</b> breaks the bond by adding water back. Both are catalysed by enzymes. Digestion is hydrolysis; growth is dehydration synthesis. Because condensation releases water, it is thermodynamically unfavourable in bulk water, which is one of the central puzzles of the origin of life (Week 11).</p>
<div class="tw"><table>
<thead><tr><th>Class</th><th>Monomer / building block</th><th>Examples</th><th>Functions</th></tr></thead>
<tbody>
<tr><td><b>Carbohydrates</b></td><td>Monosaccharides (glucose, fructose, galactose; C<sub>n</sub>H<sub>2n</sub>O<sub>n</sub>)</td><td>Disaccharides: sucrose, lactose, maltose. Polysaccharides: starch, glycogen, cellulose, chitin</td><td>Short-term energy; energy storage (starch in plants, glycogen in animals); structure (cellulose in plant walls, chitin in arthropod exoskeletons and fungal walls)</td></tr>
<tr><td><b>Lipids</b></td><td>Not true polymers; glycerol + fatty acids (fats), + phosphate (phospholipids); four-ring skeleton (steroids)</td><td>Triglycerides, phospholipids, cholesterol, steroid hormones, waxes</td><td>Long-term energy storage (9 kcal/g vs 4 for carbohydrate); membranes; insulation; signalling</td></tr>
<tr><td><b>Proteins</b></td><td>20 amino acids (amino group, carboxyl group, H, and a variable R group on a central carbon)</td><td>Enzymes, haemoglobin, collagen, antibodies, actin and myosin, membrane channels</td><td>Catalysis, structure, transport, defence, movement, signalling, regulation</td></tr>
<tr><td><b>Nucleic acids</b></td><td>Nucleotides (5-carbon sugar, phosphate, nitrogenous base)</td><td>DNA, RNA, ATP, NAD<sup>+</sup></td><td>Information storage and transfer; energy currency; electron carriers</td></tr>
</tbody></table></div>
<h3>Carbohydrates</h3>
<p>Glucose and its isomers share the formula C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> but differ in atom arrangement, which changes their properties; in water, glucose forms a ring. Starch and cellulose are both glucose polymers, but starch uses α linkages that most organisms can hydrolyse, while cellulose uses β linkages that only organisms with cellulase (or symbionts that have it) can digest. Cellulose is the most abundant organic molecule on Earth; that fact alone says a great deal about the planet's carbon cycle.</p>
<h3>Lipids</h3>
<p><b>Saturated</b> fatty acids have no C=C double bonds, pack tightly, and are solid at room temperature; <b>unsaturated</b> ones have kinks from double bonds, pack loosely, and are liquid. <b>Phospholipids</b> have a hydrophilic phosphate head and two hydrophobic tails; in water they spontaneously assemble into a <b>bilayer</b> with heads out and tails in. That self-assembly requires no enzyme and no information, which makes it a candidate for the first compartments in origin-of-life chemistry. <b>Steroids</b> (cholesterol, testosterone, oestradiol) share a four-ring skeleton; cholesterol modulates membrane fluidity.</p>
<h3>Proteins</h3>
<p>Amino acids link by <b>peptide bonds</b> into polypeptides. Function depends on shape, and shape is described at four levels: <b>primary</b> (sequence), <b>secondary</b> (α helices and β sheets held by backbone hydrogen bonds), <b>tertiary</b> (the overall fold, stabilised by R-group interactions, hydrophobic clustering, ionic bonds, hydrogen bonds, and disulfide bridges), and <b>quaternary</b> (the assembly of more than one polypeptide, as in haemoglobin's four chains). Heat, pH extremes, or salt can <b>denature</b> a protein, unfolding it and destroying function; this is why temperature and pH tolerances of extremophiles are really statements about protein stability.</p>
<p>Amino acids are <b>chiral</b>: each (except glycine) exists as L and D mirror forms, and terrestrial life uses almost exclusively L amino acids. Abiotic synthesis produces both equally. An excess of one form in a sample is therefore one of the more persuasive biosignatures (Week 13).</p>
<h3>Nucleic acids</h3>
<p>DNA is a double helix of two antiparallel strands, bases pairing A–T and G–C by hydrogen bonds; RNA is usually single-stranded, uses ribose and uracil in place of deoxyribose and thymine, and functions as messenger, structural, and catalytic molecule. Information flows DNA → RNA → protein. <b>ATP</b> is a nucleotide with three phosphates; hydrolysis of the terminal phosphate releases energy that drives most cellular work.</p>
""",
 checks=[
  ("Why can humans digest starch but not cellulose, when both are glucose polymers?", "Starch uses α-glycosidic linkages that human amylase can hydrolyse; cellulose uses β linkages that require cellulase, which humans lack. Ruminants and termites digest cellulose via microbial symbionts."),
  ("A protein loses function at 60 °C but its amino acid sequence is unchanged. Which structural levels were affected?", "Secondary, tertiary, and (if present) quaternary. Heat breaks the weak bonds that hold the fold; primary structure, the covalent peptide backbone, survives."),
  ("Why is phospholipid self-assembly important for the origin of life?", "Bilayers form spontaneously in water without enzymes or genetic instructions, providing a plausible route to the first bounded compartments in which chemistry could be concentrated and maintained against the surroundings."),
 ]))

SECTIONS.append(dict(id="s7", num="1.7", title="Energy, metabolism, and the laws that constrain life", figure="energy",
 html="""
<p class="lead">Life is a way of channelling energy. The two laws of thermodynamics do not forbid life; they set its price, and that price is the physical signature astrobiologists look for.</p>
<p>The <b>first law</b>: energy can be transformed but not created or destroyed. An organism does not make energy; it converts light or chemical energy into work and heat. The <b>second law</b>: every energy transformation increases the total entropy (disorder) of the universe. A cell builds order inside itself only by exporting more disorder, as heat and waste, to its surroundings. Cut off the energy flux and the order decays. <b>A living system is therefore a persistent state of disequilibrium maintained by energy flow.</b> That statement is why atmospheric disequilibrium is treated as a biosignature and why the first question about any planetary environment is "where is the energy gradient?"</p>
<p><b>Free energy</b> (G) is the portion of a system's energy that can do work. A reaction with negative ΔG is <b>exergonic</b> and proceeds spontaneously (though not necessarily quickly); one with positive ΔG is <b>endergonic</b> and requires input. Cells drive endergonic reactions by <b>coupling</b> them to the exergonic hydrolysis of ATP:</p>
<span class="eq">ATP + H<sub>2</sub>O → ADP + P<sub>i</sub> &nbsp;&nbsp; ΔG ≈ –30.5 kJ mol<sup>–1</sup> (standard); about –50 kJ mol<sup>–1</sup> under cellular conditions</span>
<p><b>Metabolism</b> is the sum of all chemical reactions in an organism. <b>Catabolic</b> pathways break molecules down and release energy (respiration); <b>anabolic</b> pathways build molecules and consume energy (protein synthesis). Most of the energy released in catabolism is captured by <b>redox</b> reactions: oxidation is loss of electrons, reduction is gain, and electrons carried by NADH and FADH<sub>2</sub> are ultimately passed to oxygen in aerobic organisms, or to other acceptors in anaerobes. The general principle is that any pair of a donor and an acceptor with a sufficient potential difference can, in principle, power a metabolism, which is why hydrogen, sulfide, iron, and methane all feed microbial communities in the dark.</p>
<p><b>Enzymes</b> are protein catalysts (some RNAs also catalyse). They lower the <b>activation energy</b> of a reaction, the energy hump between reactants and products, without changing ΔG or the equilibrium. Substrate binds at the <b>active site</b> by <b>induced fit</b>; reaction rate depends on temperature, pH, substrate concentration, and the presence of cofactors and inhibitors. Every enzyme has an optimum temperature and pH beyond which it denatures, and those optima are what define an organism's environmental envelope. A hyperthermophile's enzymes have optima near 90 °C and fail at 37 °C.</p>
<div class="tw"><table>
<thead><tr><th>Regulation</th><th>Mechanism</th><th>Effect</th></tr></thead>
<tbody>
<tr><td>Competitive inhibition</td><td>Inhibitor resembles substrate and occupies the active site</td><td>Reduced rate; overcome by raising substrate concentration</td></tr>
<tr><td>Non-competitive inhibition</td><td>Inhibitor binds elsewhere and changes active-site shape</td><td>Reduced rate; not overcome by more substrate</td></tr>
<tr><td>Allosteric regulation</td><td>Regulator binds a separate site, stabilising an active or inactive form</td><td>Fine control; basis of feedback inhibition</td></tr>
<tr><td>Feedback inhibition</td><td>End product of a pathway inhibits an early enzyme</td><td>Pathway output matches demand without waste</td></tr>
</tbody></table></div>
<div class="callout"><span class="label">Astrobiology note · energy as a habitability criterion</span>Habitability assessments list energy alongside solvent and elements. The requirement is not "sunlight" but "an exploitable gradient": a redox couple, a thermal gradient, or a chemical disequilibrium that a metabolism could tap. Hydrothermal reactions at Enceladus's seafloor produce hydrogen, a reductant; oxidants such as sulfate or carbon dioxide are present in the ocean. That is a gradient, and it is why Enceladus ranks high in comparative habitability (Week 12).</div>
""",
 checks=[
  ("Does an enzyme change the amount of product formed at equilibrium?", "No. It lowers activation energy and speeds the approach to equilibrium in both directions; equilibrium position depends only on ΔG."),
  ("Why is a persistent chemical disequilibrium a better biosignature than the presence of organic molecules?", "Organic molecules form abiotically and persist in equilibrium mixtures. A disequilibrium that is maintained over time requires continuous energy dissipation by some process; life is one such process, and the second law rules out its arising without a sustained flux."),
  ("A metabolic poison binds an enzyme at a site other than the active site and cannot be displaced by extra substrate. Classify it.", "Non-competitive inhibitor."),
 ]))

SECTIONS.append(dict(id="s8", num="1.8", title="Homeostasis and feedback control", figure="feedback",
 html="""
<p class="lead">Homeostasis is the maintenance of a relatively stable internal environment. It is not stillness; it is continuous correction, and the machinery of correction is feedback.</p>
<p>A feedback loop has four components. A <b>receptor</b> (sensor) detects the value of a regulated variable. A <b>control centre</b> compares that value with a <b>set point</b>. If they differ, the centre signals an <b>effector</b>, which produces a <b>response</b> that changes the variable. In <b>negative feedback</b> the response opposes the original change, returning the variable toward the set point; this is the stabilising mode and it governs temperature, blood glucose, blood pH, water balance, and blood pressure. In <b>positive feedback</b> the response amplifies the change until an endpoint terminates the loop; this drives processes that must finish once started, such as blood clotting, the action potential, and uterine contractions in labour.</p>
<div class="tw"><table>
<thead><tr><th>Variable</th><th>Receptor</th><th>Control centre</th><th>Effector and response</th></tr></thead>
<tbody>
<tr><td>Core temperature (~37 °C)</td><td>Thermoreceptors in skin and hypothalamus</td><td>Hypothalamus</td><td>Too hot: vasodilation, sweating. Too cold: vasoconstriction, shivering, behaviour</td></tr>
<tr><td>Blood glucose (~5 mM)</td><td>β and α cells of pancreas</td><td>Pancreatic islets</td><td>High: insulin → uptake and storage as glycogen. Low: glucagon → glycogen breakdown, gluconeogenesis</td></tr>
<tr><td>Blood pH (7.35–7.45)</td><td>Chemoreceptors (medulla, carotid, aortic)</td><td>Brainstem; kidneys</td><td>Low pH: faster breathing removes CO<sub>2</sub>; kidneys retain bicarbonate</td></tr>
<tr><td>Blood osmolarity</td><td>Osmoreceptors in hypothalamus</td><td>Hypothalamus, posterior pituitary</td><td>High: ADH release → water reabsorption; thirst</td></tr>
</tbody></table></div>
<p>Set points are not fixed. Fever raises the temperature set point in response to pyrogens; the body then defends the higher value by shivering and vasoconstriction. Circadian rhythms shift set points daily. Acclimatisation shifts them over weeks. A single "normal value" is therefore a poor description of a healthy system; a range, and the ability to return to it, is the better one.</p>
<p>Control systems fail in characteristic ways, and the failure mode tells you which component is at fault. A missing or insensitive receptor leaves the variable to drift. Excessive gain or delay in the loop produces oscillation and overshoot. A failed effector leaves detection intact but no correction. These same failure modes apply to a sealed habitat's life-support loops (Week 14), which is why the physiology is taught before the engineering.</p>
<p>At the ecosystem level, analogous stabilising loops exist: predator numbers rise with prey and fall as prey are depleted, a negative feedback that damps population swings. Positive feedbacks at that scale, such as ice loss lowering albedo and accelerating warming, are the ones that push systems past thresholds.</p>
""",
 checks=[
  ("Classify: after a meal, insulin lowers blood glucose, which reduces insulin secretion.", "Negative feedback: the response (glucose uptake) reduces the stimulus (high glucose), which shuts off the effector signal."),
  ("Classify: during childbirth, pressure on the cervix triggers oxytocin release, causing stronger contractions and more pressure.", "Positive feedback: each response amplifies the stimulus until delivery ends the loop."),
  ("A patient's temperature swings between 35 and 39 °C every few hours. Which loop property is most likely disturbed?", "Loop gain or delay: oscillation around the set point indicates over-correction, not a missing sensor (which would give drift) or a raised set point (which would give a stable high value)."),
 ]))

SECTIONS.append(dict(id="s9", num="1.9", title="Introductory ecology: energy flow and matter cycling",
 html="""
<p class="lead">Ecology studies the interactions between organisms and their environment. Its two central rules, <b>energy flows through</b> an ecosystem while <b>matter cycles within</b> it, apply to every biosphere, natural or engineered.</p>
<p><b>Producers</b> (autotrophs) capture energy from light or inorganic chemicals and fix carbon. <b>Consumers</b> (heterotrophs) obtain energy by eating other organisms: primary consumers eat producers, secondary consumers eat primary consumers, and so on. <b>Decomposers</b> (fungi, bacteria) break down dead matter and return nutrients to the environment. Each step is a <b>trophic level</b>, and the transfer of energy between levels is inefficient: on average only about <b>10 per cent</b> of the energy in one level is incorporated into the next; the rest is lost as heat, in respiration, or in unconsumed and undigested material. This is why food chains rarely exceed four or five links and why a habitat that must feed people should grow plants, not cattle.</p>
<span class="eq">Gross primary production (GPP) – producer respiration (R) = net primary production (NPP), the energy available to consumers</span>
<p>Matter, by contrast, is conserved and recycled through <b>biogeochemical cycles</b>. In the <b>carbon cycle</b>, photosynthesis removes CO<sub>2</sub> from the atmosphere and respiration, decomposition, and combustion return it; the ocean, soils, and rocks are large reservoirs with slow exchange. In the <b>nitrogen cycle</b>, atmospheric N<sub>2</sub> is inert to most organisms and must be <b>fixed</b> into ammonia by nitrogen-fixing bacteria (free-living or in legume root nodules) or by lightning and industry; nitrifying bacteria convert ammonia to nitrite and nitrate that plants absorb; decomposers return nitrogen to ammonia; denitrifying bacteria return N<sub>2</sub> to the atmosphere. The <b>water cycle</b> moves water by evaporation, transpiration, condensation, and precipitation, powered by solar energy and shaped by gravity.</p>
<div class="tw"><table>
<thead><tr><th>Interaction</th><th>Effect on species A / B</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Competition</td><td>– / –</td><td>Two seedling species contesting light</td></tr>
<tr><td>Predation, herbivory, parasitism</td><td>+ / –</td><td>Hawk and mouse; caterpillar and leaf; tapeworm and host</td></tr>
<tr><td>Mutualism</td><td>+ / +</td><td>Rhizobium bacteria and legume; coral and zooxanthellae</td></tr>
<tr><td>Commensalism</td><td>+ / 0</td><td>Epiphyte on a tree branch</td></tr>
</tbody></table></div>
<p>A species' <b>habitat</b> is where it lives; its <b>niche</b> is the full set of conditions and resources it uses. Two species with identical niches cannot coexist indefinitely (<b>competitive exclusion</b>); coexistence usually reveals <b>resource partitioning</b>. Ecosystem properties such as productivity, stability, and resilience emerge from these interactions and are not properties of any one population.</p>
<div class="callout"><span class="label">Astrobiology note · the closed ecosystem</span>Earth is materially closed (apart from meteorites and atmospheric escape) and energetically open. A spacecraft or habitat must be the same: matter is recycled, energy comes in as light or electricity and leaves as heat. The 10 per cent rule, the nitrogen cycle's dependence on specific bacteria, and the buffering capacity of large reservoirs are all design constraints on bioregenerative life support (Week 14). Biosphere 2 failed on an unmodelled carbon sink; the ecology in this section is the model that was missing.</div>
""",
 checks=[
  ("If producers in a pond fix 10,000 kJ m<sup>–2</sup> yr<sup>–1</sup>, estimate the energy available at the tertiary consumer level.", "About 10 kJ m<sup>–2</sup> yr<sup>–1</sup>: three transfers at ~10% each, 10,000 → 1,000 → 100 → 10."),
  ("Why cannot plants use atmospheric nitrogen directly, and what is the consequence for a sealed habitat?", "N<sub>2</sub>'s triple bond makes it inert; plants take up ammonium and nitrate. A habitat must either carry nitrogen-fixing microbes, supply fixed nitrogen chemically, or recycle it completely from waste."),
  ("Which biotic interaction is a predator and its prey, and what feedback does the pair produce at the population level?", "+ / –. A negative feedback: prey increase → predator increase → prey decrease → predator decrease, damping oscillations."),
 ]))

SECTIONS.append(dict(id="s10", num="1.10", title="From definition to detection: the astrobiology thread",
 html="""
<p class="lead">This week's material is the raw material for an <b>operational definition of life</b>: a definition stated in terms of things an instrument can measure. It is the first entry in your portfolio and the standard every later week will be judged against.</p>
<p>Collect what has been established. Life is organised hierarchically with the cell as the pivot (§1.3). It is built from CHNOPS on a carbon backbone (§1.4), in a polar solvent (§1.5), from four macromolecule classes made by condensation (§1.6). It maintains a disequilibrium by energy flow (§1.7), regulates itself by feedback (§1.8), and exchanges energy and matter within a larger system (§1.9). And it evolves, which is the property with no abiotic mimic (§1.2).</p>
<p>Now separate two kinds of statement. Some are <b>requirements that follow from physics and chemistry</b> and should hold for any life: an energy gradient, a solvent that permits reaction chemistry, a boundary that maintains a difference from the surroundings, and a way of storing and copying information with variation. Others are <b>facts about the one biology we know</b> and may be accidents of Earth's history: DNA specifically, these 20 amino acids, L-chirality, ATP, the standard genetic code. A habitability assessment that confuses the two will either miss unfamiliar life or hallucinate familiar life.</p>
<div class="tw"><table>
<thead><tr><th>Habitability criterion</th><th>What this week established</th><th>Measurable proxy</th></tr></thead>
<tbody>
<tr><td>Solvent</td><td>Water's polarity underlies cohesion, heat buffering, and ion chemistry</td><td>Liquid water at the surface or subsurface (spectroscopy, gravity, radar, plumes)</td></tr>
<tr><td>Energy</td><td>Life is disequilibrium sustained by energy flux; any sufficient redox gradient can serve</td><td>Detectable reductant–oxidant pairs; thermal or chemical gradients</td></tr>
<tr><td>Elements</td><td>CHNOPS in accessible forms</td><td>Elemental and molecular inventory (mass spectrometry, spectroscopy)</td></tr>
<tr><td>Stability</td><td>Homeostasis has limits; enzymes have optima</td><td>Temperature, pH, and radiation ranges over geological time</td></tr>
</tbody></table></div>
<div class="callout blue"><span class="label">Portfolio Entry 1 · Life and biological organisation map</span>
Produce a one-page map with three layers. <b>(1)</b> The levels of organisation from atom to biosphere, with one emergent property named at each level. <b>(2)</b> A table of the characteristics of life with a non-living counterexample for each and a mark showing which properties you would require before reporting a detection. <b>(3)</b> A written operational definition of life in under 100 words, followed by one sentence naming the kind of life your definition would fail to detect. Rubric: accuracy of levels and properties (40%), quality of counterexamples (20%), coherence and measurability of the definition (30%), honesty of the limitation statement (10%).</div>
""",
 checks=[
  ("Classify as universal requirement or terrestrial fact: (a) uses ATP; (b) needs an energy gradient; (c) L-amino acids; (d) a boundary that maintains internal difference.", "(a) terrestrial fact; (b) universal; (c) terrestrial fact; (d) universal."),
  ("Why is 'habitable' not the same as 'inhabited'?", "Habitability is a property of the environment (solvent, energy, elements, stability). Inhabitation requires that life actually arose or arrived and persisted. Habitable-but-uninhabited environments are expected and are informative about how often life begins."),
 ]))

CHEAT = [
 ("Inquiry", "Falsifiable hypothesis → if–then prediction → controlled test with one independent variable, one dependent variable, replication, and a control group. Decision rule before data. Correlation ≠ causation."),
 ("Life's properties", "Order, metabolism, growth and development, response, homeostasis, reproduction, heredity, evolutionary adaptation. Only evolution lacks an abiotic mimic. NASA: self-sustaining chemical system capable of Darwinian evolution."),
 ("Levels", "Atom → molecule → organelle → cell → tissue → organ → organ system → organism → population → community → ecosystem → biosphere. Emergent properties appear at each level."),
 ("Bonds", "Covalent (strong, shared electrons) > ionic in water > hydrogen (~20 kJ/mol) > van der Waals. Polar bonds: O–H, N–H. Nonpolar: C–H, C–C. Hydrophobic vs hydrophilic follows."),
 ("Water", "Polar; hydrogen bonds → cohesion, adhesion, high specific heat (4.18 J/g·°C), high heat of vaporisation, ice floats, universal polar solvent. pH = –log[H⁺]; each unit = 10×. Buffers resist pH change."),
 ("Macromolecules", "Made by dehydration synthesis, broken by hydrolysis. Carbohydrates (glucose; starch, glycogen, cellulose, chitin); lipids (fats, phospholipids, steroids; not polymers); proteins (20 amino acids; 4 structural levels; denaturation); nucleic acids (nucleotides; DNA, RNA, ATP)."),
 ("Energy", "1st law: conserved. 2nd law: total entropy rises; life exports disorder. ΔG < 0 exergonic; ATP couples. Enzymes lower activation energy, not ΔG. Redox: OIL RIG. Any sufficient donor–acceptor pair can power metabolism."),
 ("Homeostasis", "Receptor → control centre (set point) → effector. Negative feedback stabilises; positive feedback completes. Set points shift (fever, rhythms, acclimatisation). Drift = sensor fault; oscillation = gain/delay fault."),
 ("Ecology", "Energy flows (~10% per trophic level; GPP – R = NPP); matter cycles (C, N, H₂O). Nitrogen must be fixed by bacteria. Interactions: – –, + –, + +, + 0. Niche vs habitat; competitive exclusion."),
 ("Astrobiology thread", "Separate physical requirements (energy gradient, solvent, boundary, heritable information) from terrestrial facts (DNA, 20 amino acids, L-chirality, ATP). Habitability ≠ inhabitation."),
]


# ----------------------------------------------------------------- figures --
def fig_method():
    steps = ["Observation", "Question", "Hypothesis", "Prediction", "Test", "Analysis", "Revise or accept"]
    n = len(steps); w, h = 900, 250; cx, cy = 450, 125
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>The cycle of inquiry</title>']
    # ellipse layout
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



BRIDGE = ("Astrobiology cannot search for life without an operational definition of it. Everything in this first week "
          "is a working definition under construction: if a probe returns a chemical pattern from Enceladus, the "
          "criteria you build here are the criteria you will argue from.")
CHIPS = '<span>🎯 CO1</span><span>📚 OpenStax Biology 2e, Ch. 1–3, 6, 8</span><span>🗂️ Portfolio Entry 1</span><span>📖 10 sections · 5 figures · 26 check-yourself items</span>'
BLURB = ("A full first lecture: how biology reasons, what distinguishes living from non-living systems, the hierarchy from atom to biosphere, "
         "the chemistry of carbon and water, the four macromolecules, the thermodynamics that constrain life, feedback control, and the "
         "ecology of energy and matter — each section closing with the astrobiological question it raises.")
CO_LINE = "CO1 (enabled), with PO1 scientific knowledge, PO2 inquiry, PO3 systems reasoning, and PO5 lifelong learning introduced."
REVIEW_SECTIONS = "§1.2, §1.5, §1.7 and §1.8"
