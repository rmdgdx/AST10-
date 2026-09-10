# -*- coding: utf-8 -*-
"""Week 2 full lecture — Cell Structure and Function."""
import html, math
E = lambda s: html.escape(str(s), quote=True)
FONT = 'font-family="-apple-system,Segoe UI,Inter,Roboto,Arial,sans-serif"'

BRIDGE = ("Every proposed biosignature instrument is really a bet about cells: that life compartmentalises, that it runs "
          "redox chemistry across a membrane, and that it leaves lipids behind. Cell biology is where those bets are justified or abandoned.")
CHIPS = '<span>🎯 CO1</span><span>📚 OpenStax Biology 2e, Ch. 4–11</span><span>🗂️ Portfolio Entry 2</span><span>📖 10 sections · 6 figures · 30 check-yourself items</span>'
BLURB = ("The cell from the outside in: why cells are small, how prokaryotes and eukaryotes differ and why they share so much, the organelles and "
         "what each does, the membrane and every way molecules cross it, how respiration and photosynthesis both run on proton gradients, and how "
         "cells copy themselves with and without variation — each section closing with the question it raises for life beyond Earth.")
CO_LINE = "CO1 (enabled), with PO1 scientific knowledge, PO2 inquiry, and PO3 systems reasoning introduced."
REVIEW_SECTIONS = "§2.2, §2.5, §2.7 and §2.9"

SECTIONS = []

SECTIONS.append(dict(id="s1", num="2.1", title="Cell theory, microscopy, and why cells are small", figure="sav",
 html="""
<p class="lead">Cell theory has three claims: all organisms are made of one or more cells; the cell is the basic unit of structure and function; and all cells arise from pre-existing cells. The third claim, established by Virchow and Pasteur in the 1850s–60s, closed the door on spontaneous generation and opened the one that origin-of-life research still walks through: if cells only come from cells, where did the first one come from?</p>
<p>Cells are seen, not deduced. <b>Light microscopy</b> magnifies up to about 1,000× and resolves objects roughly 0.2 μm apart, limited by the wavelength of visible light; it can image living cells, especially with fluorescence labelling. <b>Electron microscopy</b> uses an electron beam with a far shorter wavelength, resolving to about 0.2 nm: transmission EM (TEM) sections the specimen for internal detail, scanning EM (SEM) images surfaces in three dimensions. Both require fixed, dead specimens. <b>Magnification</b> enlarges; <b>resolution</b> is the ability to separate two points, and it is resolution, not magnification, that sets what can be seen.</p>
<div class="tw"><table>
<thead><tr><th>Scale</th><th>Object</th><th>Instrument that resolves it</th></tr></thead>
<tbody>
<tr><td>0.1–1 nm</td><td>Atoms, small molecules</td><td>X-ray crystallography, cryo-EM</td></tr>
<tr><td>2–20 nm</td><td>Proteins, ribosomes, membrane thickness (~8 nm)</td><td>Electron microscopy</td></tr>
<tr><td>0.2–2 μm</td><td>Bacteria, mitochondria, viruses at the small end</td><td>Light (limit) and electron microscopy</td></tr>
<tr><td>10–100 μm</td><td>Most eukaryotic cells; human egg ~100 μm</td><td>Light microscopy</td></tr>
<tr><td>&gt; 1 mm</td><td>Frog egg, some algal cells, neurons up to a metre long</td><td>Unaided eye</td></tr>
</tbody></table></div>
<p>Why are most cells microscopic? Because a cell exchanges material through its surface but consumes it throughout its volume. As a cell grows, surface area rises with the <b>square</b> of its linear size while volume rises with the <b>cube</b>, so the <b>surface-area-to-volume ratio</b> falls. Beyond a certain size, diffusion across the surface cannot supply the interior. Cells that are large cheat: they are flat, long, or highly folded, or they have internal membranes to add surface, which is one of the evolutionary rationales for organelles.</p>
<div class="callout blue"><span class="label">Worked example · surface-area-to-volume</span>Treat a cell as a cube of side <i>s</i>. Surface area = 6<i>s</i><sup>2</sup>; volume = <i>s</i><sup>3</sup>; ratio = 6/<i>s</i>.<br>
<i>s</i> = 1 μm: ratio 6 μm<sup>–1</sup>. &nbsp; <i>s</i> = 10 μm: ratio 0.6. &nbsp; <i>s</i> = 100 μm: ratio 0.06.<br>
A tenfold increase in size cuts the exchange capacity per unit of cytoplasm tenfold. A bacterium 1 μm across has 100 times more membrane per unit volume than a 100 μm cell, which is part of why bacterial metabolism per gram runs so much faster.</div>
<p>There is a lower limit too. A cell must hold a genome, ribosomes, and enough enzymes to run a metabolism; the smallest free-living cells, some mycoplasmas, are about 0.2–0.3 μm. This bounds the size of any bounded, self-maintaining chemical system built from molecules like ours, and it is the reason the "nanofossils" of ALH 84001, at 20–100 nm, drew immediate scepticism (Week 13).</p>
""",
 checks=[
  ("Two microscopes both magnify 1,000×, but one resolves 0.2 μm and the other 0.5 μm. Which shows more detail, and why?", "The 0.2 μm instrument. Magnification enlarges the image; resolution determines whether two nearby points are distinguishable. Higher magnification with poor resolution produces a larger blur."),
  ("A spherical cell doubles its radius. By what factor do its surface area and volume change?", "Surface area ×4 (r²); volume ×8 (r³). The surface-to-volume ratio halves."),
  ("Why do neurons a metre long not violate the surface-to-volume constraint?", "They are extremely thin. A long, narrow cylinder keeps a high surface-to-volume ratio because no point in the cytoplasm is far from a membrane."),
 ]))

SECTIONS.append(dict(id="s2", num="2.2", title="Prokaryotic and eukaryotic cells", figure="cells",
 html="""
<p class="lead">All cells share four features: a plasma membrane, cytoplasm, ribosomes, and DNA. Everything else divides the living world into two architectures.</p>
<p><b>Prokaryotic cells</b> (domains Bacteria and Archaea) have no membrane-bound nucleus: the chromosome, usually a single circular DNA molecule, lies in a region called the <b>nucleoid</b>. They lack membrane-bound organelles, are typically 0.5–5 μm, and are enclosed by a cell wall (peptidoglycan in bacteria; various polymers in archaea, never peptidoglycan). Many carry small extra DNA circles called <b>plasmids</b>, external <b>flagella</b> for motility, <b>pili</b> for attachment and DNA exchange, and a <b>capsule</b> for protection. Their small size and high surface-to-volume ratio let them grow and divide fast, some in under 20 minutes.</p>
<p><b>Eukaryotic cells</b> (domain Eukarya: protists, fungi, plants, animals) enclose linear chromosomes, wrapped around histone proteins, in a <b>nucleus</b> bounded by a double membrane. They are typically 10–100 μm and partition their functions among membrane-bound organelles. Compartmentalisation lets incompatible reactions run side by side, concentrates reactants, and adds internal membrane surface for the reactions that need it.</p>
<div class="tw"><table>
<thead><tr><th>Feature</th><th>Prokaryote</th><th>Eukaryote</th></tr></thead>
<tbody>
<tr><td>Nucleus</td><td>Absent; nucleoid region</td><td>Present, double membrane with pores</td></tr>
<tr><td>DNA</td><td>Usually one circular chromosome; plasmids</td><td>Multiple linear chromosomes with histones</td></tr>
<tr><td>Membrane-bound organelles</td><td>Absent (some have internal membrane folds)</td><td>Present: ER, Golgi, mitochondria, lysosomes, etc.</td></tr>
<tr><td>Ribosomes</td><td>70S (smaller)</td><td>80S in cytoplasm; 70S in mitochondria and chloroplasts</td></tr>
<tr><td>Size</td><td>0.5–5 μm</td><td>10–100 μm</td></tr>
<tr><td>Cell wall</td><td>Bacteria: peptidoglycan. Archaea: pseudopeptidoglycan, protein, or polysaccharide</td><td>Plants: cellulose. Fungi: chitin. Animals: none</td></tr>
<tr><td>Division</td><td>Binary fission</td><td>Mitosis or meiosis</td></tr>
<tr><td>Cytoskeleton</td><td>Simple homologues (FtsZ, MreB)</td><td>Microtubules, microfilaments, intermediate filaments</td></tr>
</tbody></table></div>
<p><b>Archaea</b> deserve separate mention. They are prokaryotic in structure but share their transcription and translation machinery with eukaryotes, and their membrane lipids are unique: <b>ether-linked</b> branched isoprenoid chains rather than the <b>ester-linked</b> straight fatty acids of bacteria and eukaryotes, sometimes spanning the whole membrane as a monolayer. Ether bonds resist hydrolysis and the monolayer resists melting, which is why archaea dominate many hot, acidic, and hypersaline habitats. Their lipids also survive in rock, making them useful biomarkers.</p>
<div class="callout"><span class="label">Endosymbiosis · where mitochondria and chloroplasts came from</span>Mitochondria and chloroplasts have double membranes, their own small circular genomes, 70S ribosomes sensitive to antibacterial antibiotics, and they divide by fission independently of the cell cycle. The endosymbiotic theory holds that they descend from free-living bacteria engulfed by an ancestral host cell roughly 2 billion years ago: an α-proteobacterium became the mitochondrion, and later a cyanobacterium became the chloroplast. Gene sequences confirm both origins. The eukaryotic cell is therefore itself a merger, and complexity in life's history arrived at least once by partnership rather than by gradual elaboration.</div>
""",
 checks=[
  ("A newly isolated cell is 1 μm, lacks a nucleus, and has ether-linked branched membrane lipids without peptidoglycan. Classify it.", "An archaeon. Bacteria have ester-linked lipids and (usually) peptidoglycan; eukaryotes have nuclei."),
  ("List three pieces of evidence for the bacterial origin of mitochondria.", "Double membrane; own circular DNA; 70S ribosomes inhibited by antibacterial antibiotics; division by fission; gene sequences closest to α-proteobacteria. Any three."),
  ("Why can prokaryotes generally outgrow eukaryotes in a nutrient-rich flask?", "Higher surface-to-volume ratio, simpler division (binary fission with no spindle), smaller genomes to copy, and less structural investment per cell."),
 ]))

SECTIONS.append(dict(id="s3", num="2.3", title="A tour of the eukaryotic cell",
 html="""
<p class="lead">Organelles are compartments with jobs. The table is the reference; the paragraphs below it are the logic of how the compartments cooperate.</p>
<div class="tw"><table>
<thead><tr><th>Structure</th><th>Description</th><th>Function</th><th>Present in</th></tr></thead>
<tbody>
<tr><td><b>Nucleus</b></td><td>Double-membrane envelope with pores; contains chromatin and the nucleolus</td><td>Stores and expresses the genome; nucleolus assembles ribosomal subunits</td><td>All eukaryotes</td></tr>
<tr><td><b>Ribosome</b></td><td>rRNA + protein; free in cytosol or bound to ER; not membrane-bound</td><td>Protein synthesis</td><td>All cells</td></tr>
<tr><td><b>Rough ER</b></td><td>Membrane network studded with ribosomes, continuous with the nuclear envelope</td><td>Synthesis and folding of secreted and membrane proteins</td><td>All eukaryotes</td></tr>
<tr><td><b>Smooth ER</b></td><td>Ribosome-free tubules</td><td>Lipid and steroid synthesis; detoxification; calcium storage</td><td>All eukaryotes</td></tr>
<tr><td><b>Golgi apparatus</b></td><td>Stacked flattened sacs (cisternae)</td><td>Modifies, sorts, and packages proteins and lipids; makes lysosomes</td><td>All eukaryotes</td></tr>
<tr><td><b>Lysosome</b></td><td>Vesicle of acid hydrolases, pH ~5</td><td>Digests macromolecules, worn organelles, engulfed material</td><td>Animals mainly</td></tr>
<tr><td><b>Peroxisome</b></td><td>Vesicle of oxidative enzymes</td><td>Breaks down fatty acids; detoxifies H<sub>2</sub>O<sub>2</sub> with catalase</td><td>All eukaryotes</td></tr>
<tr><td><b>Mitochondrion</b></td><td>Double membrane; inner membrane folded into cristae; matrix with DNA and ribosomes</td><td>Aerobic respiration; most ATP synthesis</td><td>Nearly all eukaryotes</td></tr>
<tr><td><b>Chloroplast</b></td><td>Double membrane; internal thylakoids stacked as grana within the stroma</td><td>Photosynthesis</td><td>Plants, algae</td></tr>
<tr><td><b>Central vacuole</b></td><td>Large membrane-bound sac (tonoplast)</td><td>Storage, waste, turgor pressure, growth by water uptake</td><td>Plants</td></tr>
<tr><td><b>Cytoskeleton</b></td><td>Microtubules (tubulin), microfilaments (actin), intermediate filaments</td><td>Shape, transport tracks, movement, division</td><td>All eukaryotes</td></tr>
<tr><td><b>Centrosome, cilia, flagella</b></td><td>Microtubule organising centre; 9+2 microtubule arrays</td><td>Spindle organisation; motility and fluid movement</td><td>Animals; some protists and plant gametes</td></tr>
<tr><td><b>Cell wall</b></td><td>Cellulose (plants), chitin (fungi)</td><td>Support, protection, resists turgor</td><td>Plants, fungi, many protists</td></tr>
<tr><td><b>Extracellular matrix</b></td><td>Collagen, proteoglycans, fibronectin</td><td>Support, adhesion, signalling</td><td>Animals</td></tr>
</tbody></table></div>
<h3>The endomembrane system</h3>
<p>The nuclear envelope, ER, Golgi, lysosomes, vesicles, and plasma membrane form one continuous or vesicle-connected system. A secreted protein is made on the rough ER, folded and tagged, carried in a transport vesicle to the Golgi, modified (often by adding sugars), sorted into a secretory vesicle, and released by <b>exocytosis</b> at the plasma membrane. A lysosomal enzyme follows the same path but is diverted into a lysosome. The system is a conveyor with addresses, and disorders of it (Tay-Sachs, cystic fibrosis in part) are disorders of sorting and folding.</p>
<h3>Energy organelles</h3>
<p>Mitochondria's inner membrane is folded into cristae to increase the surface on which the electron transport chain sits, the same surface-to-volume logic as §2.1 applied inside the cell. Chloroplasts do the same with thylakoid membranes. Both organelles are semi-autonomous, with their own genomes and ribosomes, and both are the sites of the proton-gradient chemistry in §2.7–§2.8.</p>
<h3>Plant versus animal cells</h3>
<p>Plant cells add a cellulose wall, chloroplasts, and a central vacuole, and lack centrosomes with centrioles and lysosomes (their vacuole takes over digestive functions). Animal cells have lysosomes, centrioles, and an extracellular matrix, and lack walls, which is why they can change shape, crawl, and engulf.</p>
<div class="callout"><span class="label">Astrobiology note · what survives</span>Of everything in the table, only a few things persist in rock for billions of years: membrane lipids and their breakdown products (hopanes from bacteria, steranes from eukaryotes, archaeal isoprenoids), mineralised walls, and the isotopic signature of carbon that passed through enzymes. Organelle organisation does not fossilise. A search for ancient or extraterrestrial cells is therefore a search for chemical residues and morphology, not for compartments.</div>
""",
 checks=[
  ("Trace the path of a digestive enzyme destined for a lysosome from gene to organelle.", "Gene transcribed in the nucleus → mRNA exported through nuclear pores → translated on a ribosome bound to rough ER → folded and glycosylated in the ER lumen → vesicle to the Golgi → modified and sorted (mannose-6-phosphate tag) → vesicle buds off as a lysosome or fuses with one."),
  ("A cell has abundant smooth ER and few ribosomes. Predict its specialisation.", "Lipid or steroid synthesis (e.g. adrenal cortex, testis) or detoxification (liver). Smooth ER is where those reactions occur."),
  ("Why do mitochondria have cristae?", "Folding increases inner-membrane surface area, allowing more electron transport chains and ATP synthase per organelle, the same reason cells are small and leaves are thin."),
 ]))

SECTIONS.append(dict(id="s4", num="2.4", title="The plasma membrane", figure="membrane",
 html="""
<p class="lead">The membrane is the cell's definition of self: a boundary about 8 nm thick that decides what enters, what leaves, and what the inside can differ from the outside in. The <b>fluid mosaic model</b> describes it as a two-dimensional fluid of lipids in which proteins float.</p>
<p><b>Phospholipids</b> are amphipathic: a hydrophilic phosphate head and two hydrophobic fatty-acid tails. In water they spontaneously form a <b>bilayer</b>, tails inward, heads facing the aqueous inside and outside. The bilayer is a barrier to ions and polar molecules and a poor barrier to small nonpolar ones (O<sub>2</sub>, CO<sub>2</sub>, steroid hormones). It is fluid: lipids drift laterally about 2 μm per second, but rarely flip between leaflets.</p>
<p><b>Fluidity</b> is tuned. Unsaturated tails (kinked) keep the membrane fluid at low temperature; saturated tails pack tightly and stiffen it. <b>Cholesterol</b> (in animals) buffers: it reduces fluidity at high temperature by restraining movement and increases it at low temperature by preventing tight packing. Organisms adjust lipid composition to their environment, which is why cold-adapted fish and psychrophilic bacteria have more unsaturated lipids, and why archaea in boiling springs use ether-linked, branched, sometimes monolayer-forming lipids.</p>
<div class="tw"><table>
<thead><tr><th>Membrane protein class</th><th>Function</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Channel</td><td>Hydrophilic pore for specific ions or water; passive</td><td>Aquaporin; K<sup>+</sup> leak channel</td></tr>
<tr><td>Carrier (transporter)</td><td>Binds solute and changes shape to move it; passive or active</td><td>GLUT glucose transporter; Na<sup>+</sup>/K<sup>+</sup> pump</td></tr>
<tr><td>Receptor</td><td>Binds a signal molecule and triggers a cellular response</td><td>Insulin receptor</td></tr>
<tr><td>Enzyme</td><td>Catalyses reactions at the membrane surface</td><td>ATP synthase; digestive enzymes on intestinal cells</td></tr>
<tr><td>Recognition (glycoprotein)</td><td>Cell identity; immune recognition</td><td>ABO blood group antigens; MHC proteins</td></tr>
<tr><td>Adhesion / junction</td><td>Binds cells to each other or to the matrix</td><td>Cadherins; integrins</td></tr>
</tbody></table></div>
<p>Carbohydrates attached to lipids (<b>glycolipids</b>) and proteins (<b>glycoproteins</b>) coat the outer surface as the <b>glycocalyx</b>, the cell's molecular face. The membrane is therefore <b>asymmetric</b>: the two leaflets differ in lipid and protein composition, and that asymmetry is maintained actively.</p>
<div class="callout blue"><span class="label">Selective permeability, summarised</span>Crosses freely: small nonpolar molecules (O<sub>2</sub>, CO<sub>2</sub>, N<sub>2</sub>), lipids. Crosses slowly: small uncharged polar molecules (water, ethanol, urea). Needs a protein: ions (Na<sup>+</sup>, K<sup>+</sup>, Cl<sup>–</sup>, H<sup>+</sup>), large polar molecules (glucose, amino acids), macromolecules. The rule is the polarity rule from §1.4: the hydrophobic core rejects charge.</div>
<div class="callout"><span class="label">Astrobiology note · membranes as the first structure and the last trace</span>Fatty acids and simple amphiphiles found in carbonaceous meteorites form vesicles in water without any enzyme. Compartmentalisation is therefore the origin-of-life problem with the most convincing abiotic solution (Week 11). At the other end of time, lipid skeletons are the most durable molecular fossils: hopanes and steranes are recovered from rocks over 1.6 billion years old, and ether lipids would flag archaeal-type life in a returned sample.</div>
""",
 checks=[
  ("A bacterium is moved from 37 °C to 10 °C. Predict the change in its membrane lipid composition over subsequent generations, and why.", "More unsaturated (kinked) fatty acids, and shorter chains. Both keep the bilayer fluid at low temperature; without the change the membrane would stiffen and transport would fail."),
  ("Rank for rate of unaided crossing of a bilayer: Na⁺, O₂, glucose, ethanol.", "O₂ > ethanol > glucose ≈ very slow > Na⁺ (essentially none). Small and nonpolar crosses fastest; charged crosses not at all."),
  ("Why is membrane asymmetry evidence that a membrane is being actively maintained?", "Lipids do not spontaneously flip between leaflets, so a stable difference between the two faces requires enzymes (flippases) spending energy. Asymmetry is a signature of ongoing work."),
 ]))

SECTIONS.append(dict(id="s5", num="2.5", title="Passive transport: diffusion, facilitated diffusion, and osmosis", figure="tonicity",
 html="""
<p class="lead">Passive transport moves substances <b>down</b> their concentration gradient at no energy cost to the cell. The energy is already stored in the gradient; the cell only decides whether to open a path.</p>
<p><b>Simple diffusion</b> is the net movement of a substance from where it is more concentrated to where it is less, driven by random molecular motion. Rate increases with the concentration difference, temperature, and surface area, and decreases with distance and molecular size (Fick's law, met again in Week 9). Only substances that cross the bilayer unaided diffuse this way. Each substance diffuses down its <b>own</b> gradient, independently of others.</p>
<p><b>Facilitated diffusion</b> is passive transport through a channel or carrier protein. It is specific, saturable (rate plateaus when carriers are all busy), and still requires no ATP. Aquaporins pass about three billion water molecules per second; the GLUT carriers move glucose into most cells; ion channels are often gated by voltage, ligand, or mechanical stress.</p>
<p><b>Osmosis</b> is the diffusion of water across a selectively permeable membrane, toward the side with more solute (less free water). <b>Tonicity</b> describes a solution's effect on cell volume: in a <b>hypotonic</b> solution water enters and the cell swells; in a <b>hypertonic</b> solution water leaves and the cell shrinks; in an <b>isotonic</b> solution there is no net movement. A cell without a wall lyses in a hypotonic medium (red cells in distilled water) and crenates in a hypertonic one. A walled cell becomes <b>turgid</b> in hypotonic medium, which is what holds a plant upright, and <b>plasmolyses</b>, the membrane pulling away from the wall, in hypertonic medium.</p>
<div class="tw"><table>
<thead><tr><th>Solution</th><th>Net water movement</th><th>Animal cell</th><th>Plant cell</th></tr></thead>
<tbody>
<tr><td>Hypotonic (lower solute outside)</td><td>Into the cell</td><td>Swells; may lyse</td><td>Turgid (normal, desirable)</td></tr>
<tr><td>Isotonic</td><td>None net</td><td>Normal</td><td>Flaccid (wilting begins)</td></tr>
<tr><td>Hypertonic (higher solute outside)</td><td>Out of the cell</td><td>Shrivels (crenation)</td><td>Plasmolysed</td></tr>
</tbody></table></div>
<div class="callout blue"><span class="label">Worked example · predicting cell volume</span>Red blood cells (internal osmolarity ≈ 300 mOsm) are placed in three solutions: (a) 0.9% NaCl (≈ 300 mOsm), (b) distilled water, (c) 3% NaCl (≈ 1,000 mOsm).<br>
(a) Isotonic: no net water flow; cells keep their biconcave shape. (b) Hypotonic: water enters; cells swell and burst (haemolysis), releasing haemoglobin. (c) Hypertonic: water leaves; cells shrink and crenate.<br>
Note that <b>osmolarity</b> counts particles: 0.9% NaCl is ≈ 154 mM NaCl but ≈ 300 mOsm because each NaCl yields two ions. A 300 mM glucose solution is also ≈ 300 mOsm, and isotonic, because glucose does not dissociate.</div>
<p>Organisms that live in water that is not isotonic to them must <b>osmoregulate</b>. Freshwater protists pump water out with contractile vacuoles; marine bony fish drink and excrete salt; halophilic archaea accumulate potassium to several molar to match a saturated brine. Every one of these is a continuous energy cost, and it sets the salinity range an organism can occupy.</p>
""",
 checks=[
  ("A cell is placed in a solution and neither swells nor shrinks, yet the solution contains a solute the cell lacks. Explain.", "The solution is isotonic in total particle concentration even though its composition differs. Tonicity depends on the concentration of non-penetrating solutes, not on which solutes they are."),
  ("Is 200 mM CaCl₂ hypertonic, hypotonic, or isotonic to a 300 mOsm cell?", "Hypertonic: CaCl₂ gives three particles, so 200 mM ≈ 600 mOsm. Water leaves the cell."),
  ("Why is facilitated diffusion saturable while simple diffusion is not?", "Facilitated diffusion depends on a finite number of carrier proteins that each handle one solute at a time; when all are occupied, rate cannot rise further. Simple diffusion has no such limiting component."),
 ]))

SECTIONS.append(dict(id="s6", num="2.6", title="Active and bulk transport",
 html="""
<p class="lead">Active transport moves substances <b>against</b> their gradient, which costs energy and is how cells build the gradients that everything else runs on.</p>
<p><b>Primary active transport</b> uses ATP directly. The <b>sodium–potassium pump</b> (Na<sup>+</sup>/K<sup>+</sup>-ATPase) exports three Na<sup>+</sup> and imports two K<sup>+</sup> per ATP hydrolysed, in a cycle of binding, phosphorylation, and conformational change. It consumes about a third of a resting animal cell's ATP (two-thirds in neurons), and it does three things at once: maintains the Na<sup>+</sup> and K<sup>+</sup> gradients, generates a net outward positive charge that contributes to the <b>membrane potential</b> (about –70 mV in neurons), and keeps cell volume stable by holding intracellular solute down. The <b>proton pump</b> (H<sup>+</sup>-ATPase) plays the same role in plants, fungi, and bacteria.</p>
<span class="eq">3 Na<sup>+</sup><sub>in</sub> + 2 K<sup>+</sup><sub>out</sub> + ATP → 3 Na<sup>+</sup><sub>out</sub> + 2 K<sup>+</sup><sub>in</sub> + ADP + P<sub>i</sub></span>
<p><b>Secondary active transport</b> (cotransport) uses the energy stored in one gradient to move another solute uphill. In the intestine, the sodium–glucose cotransporter lets Na<sup>+</sup> flow down its gradient and drags glucose in against its own; the Na<sup>+</sup> gradient was paid for earlier by the pump. <b>Symport</b> moves both solutes the same direction; <b>antiport</b> moves them in opposite directions (Na<sup>+</sup>/Ca<sup>2+</sup> exchanger, Na<sup>+</sup>/H<sup>+</sup> exchanger). Plants run sucrose–H<sup>+</sup> symport into the phloem on a proton gradient.</p>
<p>An <b>electrochemical gradient</b> combines two forces on an ion: the chemical gradient (concentration) and the electrical gradient (membrane potential). K<sup>+</sup> is more concentrated inside, so its chemical gradient pushes it out, but the negative interior pulls it in; the balance point is the ion's equilibrium potential (Week 8).</p>
<h3>Bulk transport</h3>
<p>Macromolecules and particles move in vesicles. <b>Exocytosis</b> fuses a secretory vesicle with the membrane, releasing its contents and adding its membrane to the surface. <b>Endocytosis</b> pinches membrane inward: <b>phagocytosis</b> engulfs particles and cells ("eating"), <b>pinocytosis</b> takes in fluid non-specifically ("drinking"), and <b>receptor-mediated endocytosis</b> concentrates specific ligands in coated pits before internalising them (LDL cholesterol uptake; the entry route of many viruses). All three cost ATP.</p>
<div class="tw"><table>
<thead><tr><th>Mechanism</th><th>Direction relative to gradient</th><th>Protein required</th><th>ATP used</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Simple diffusion</td><td>Down</td><td>No</td><td>No</td><td>O<sub>2</sub> into a cell</td></tr>
<tr><td>Facilitated diffusion</td><td>Down</td><td>Channel or carrier</td><td>No</td><td>Glucose via GLUT; water via aquaporin</td></tr>
<tr><td>Osmosis</td><td>Water down its own gradient</td><td>Optional (aquaporin)</td><td>No</td><td>Red cell in hypotonic solution</td></tr>
<tr><td>Primary active</td><td>Up</td><td>Pump (ATPase)</td><td>Directly</td><td>Na<sup>+</sup>/K<sup>+</sup> pump</td></tr>
<tr><td>Secondary active</td><td>Up (driven by another solute going down)</td><td>Cotransporter</td><td>Indirectly</td><td>Na<sup>+</sup>–glucose symport</td></tr>
<tr><td>Endocytosis / exocytosis</td><td>Either</td><td>Membrane machinery</td><td>Yes</td><td>Phagocytosis; hormone secretion</td></tr>
</tbody></table></div>
<div class="callout"><span class="label">Astrobiology note · gradients are the signature of work</span>A dead cell equilibrates: within hours its ion gradients collapse and its membrane potential is zero. A living cell holds gradients against leakage continuously. This is the cellular version of the disequilibrium argument from §1.7, and it is measurable in the laboratory (membrane-potential dyes) and, at planetary scale, as atmospheric or geochemical disequilibrium.</div>
""",
 checks=[
  ("A drug blocks Na⁺/K⁺-ATPase. Predict three consequences for an animal cell over the next hour.", "Na⁺ accumulates inside and K⁺ leaks out, so the membrane potential decays; secondary active transport that depends on the Na⁺ gradient (glucose, amino acid uptake) slows; intracellular solute rises, water enters, and the cell swells."),
  ("Is sodium–glucose cotransport active or passive? Justify.", "Active (secondary). Glucose moves against its gradient. No ATP is hydrolysed at the transporter, but the Na⁺ gradient it exploits was built by ATP-driven pumping."),
  ("Why does receptor-mediated endocytosis allow a cell to take up a substance that is scarce in the extracellular fluid?", "Receptors concentrate the ligand at the membrane before the vesicle forms, so each vesicle carries far more of the target than pinocytosis of the same volume would."),
 ]))

SECTIONS.append(dict(id="s7", num="2.7", title="Cellular respiration: harvesting chemical energy", figure="chemiosmosis",
 html="""
<p class="lead">Respiration oxidises fuel in controlled steps and captures the released energy as ATP. The chemistry is redox; the engineering is a proton gradient across a membrane.</p>
<span class="eq">C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6 O<sub>2</sub> → 6 CO<sub>2</sub> + 6 H<sub>2</sub>O &nbsp;&nbsp; ΔG° ≈ –2,870 kJ mol<sup>–1</sup></span>
<p>Glucose is oxidised (loses electrons, as hydrogen) and oxygen is reduced. Electrons are not passed to oxygen directly; they are collected by <b>NAD<sup>+</sup></b> (→ NADH) and <b>FAD</b> (→ FADH<sub>2</sub>) and handed to an electron transport chain, so the energy is released in small, capturable amounts rather than as one burst of heat.</p>
<div class="tw"><table>
<thead><tr><th>Stage</th><th>Location (eukaryote)</th><th>Inputs → outputs (per glucose)</th><th>ATP</th><th>Needs O<sub>2</sub>?</th></tr></thead>
<tbody>
<tr><td><b>Glycolysis</b></td><td>Cytosol</td><td>Glucose → 2 pyruvate; 2 NAD<sup>+</sup> → 2 NADH</td><td>2 net (substrate-level)</td><td>No</td></tr>
<tr><td><b>Pyruvate oxidation</b></td><td>Mitochondrial matrix</td><td>2 pyruvate → 2 acetyl-CoA + 2 CO<sub>2</sub>; 2 NADH</td><td>0</td><td>Indirectly</td></tr>
<tr><td><b>Citric acid (Krebs) cycle</b></td><td>Matrix</td><td>2 acetyl-CoA → 4 CO<sub>2</sub>; 6 NADH, 2 FADH<sub>2</sub></td><td>2 (as GTP)</td><td>Indirectly</td></tr>
<tr><td><b>Oxidative phosphorylation</b></td><td>Inner membrane</td><td>10 NADH + 2 FADH<sub>2</sub> + 6 O<sub>2</sub> → H<sub>2</sub>O; proton gradient → ATP</td><td>~26–28</td><td>Yes</td></tr>
<tr><td><b>Total</b></td><td></td><td></td><td><b>~30–32</b></td><td></td></tr>
</tbody></table></div>
<p><b>Glycolysis</b> is ten cytosolic reactions that split glucose into two pyruvate, investing 2 ATP and recovering 4, for a net 2, plus 2 NADH. It needs no oxygen and no organelle, is found in essentially every organism, and is therefore thought to be among the most ancient metabolic pathways. <b>Pyruvate oxidation</b> and the <b>citric acid cycle</b> complete the oxidation of carbon to CO<sub>2</sub> inside the mitochondrion, generating most of the NADH.</p>
<p><b>Oxidative phosphorylation</b> is where the ATP is made. The electron transport chain, four protein complexes in the inner membrane, passes electrons from NADH and FADH<sub>2</sub> down a series of redox carriers to oxygen, which is reduced to water. The energy released pumps H<sup>+</sup> from the matrix into the intermembrane space, creating a <b>proton-motive force</b>: a concentration gradient plus a charge difference. Protons flow back through <b>ATP synthase</b>, a rotary motor that couples the flow to phosphorylation of ADP. This coupling of a redox reaction to ATP synthesis through a proton gradient is <b>chemiosmosis</b> (Mitchell, 1961), and it is near-universal: mitochondria, chloroplasts, and bacterial membranes all use it. Oxygen's role is simply to be the final electron acceptor; without it the chain backs up, NADH is not regenerated, and everything upstream stops.</p>
<h3>Without oxygen</h3>
<p><b>Fermentation</b> regenerates NAD<sup>+</sup> so that glycolysis can continue when there is no acceptor for the chain. Lactic acid fermentation (muscle under load, lactobacilli) reduces pyruvate to lactate; alcoholic fermentation (yeast) reduces it to ethanol and CO<sub>2</sub>. Either way the yield is only the 2 ATP of glycolysis, which is why fermenting cells consume sugar so fast. <b>Anaerobic respiration</b> is different: a full electron transport chain with a final acceptor other than O<sub>2</sub>, such as nitrate, sulfate, iron(III), or CO<sub>2</sub> (methanogens). Yields are lower than with oxygen but far above fermentation, and these metabolisms sustain the deep subsurface, sediments, and hydrothermal systems.</p>
<div class="callout"><span class="label">Astrobiology note · metabolism without sunlight or oxygen</span>The general form of respiration is: electron donor → chain → electron acceptor, with the energy captured via a proton gradient. On Earth the donor can be organic carbon, H<sub>2</sub>, H<sub>2</sub>S, Fe<sup>2+</sup>, NH<sub>4</sub><sup>+</sup>, or CH<sub>4</sub>, and the acceptor O<sub>2</sub>, NO<sub>3</sub><sup>–</sup>, SO<sub>4</sub><sup>2–</sup>, Fe<sup>3+</sup>, or CO<sub>2</sub>. Habitability assessment asks which donor–acceptor pairs an environment offers and how much free energy each yields. Enceladus's plume, with H<sub>2</sub> and CO<sub>2</sub>, offers the methanogen couple; Europa's ocean may offer oxidants delivered by radiolysis of its ice.</div>
""",
 checks=[
  ("Cyanide blocks the final complex of the electron transport chain. Explain why ATP production collapses even though glycolysis and the citric acid cycle enzymes are intact.", "Electrons cannot reach oxygen, so the chain backs up, NADH cannot be reoxidised to NAD⁺, the proton gradient dissipates, ATP synthase stops, and the NAD⁺ shortage then stalls the cycle and pyruvate oxidation. Only glycolysis with fermentation continues, yielding 2 ATP."),
  ("A yeast culture switches from aerobic to anaerobic conditions. Predict the change in glucose consumption per unit of growth and explain.", "Consumption rises sharply (about 15-fold in principle) because fermentation yields ~2 ATP per glucose versus ~30 aerobically. This is the Pasteur effect."),
  ("Why is the ATP yield quoted as 'about 30–32' rather than an exact number?", "Proton stoichiometry per ATP is not an integer, some of the gradient is spent on transport into the mitochondrion, and cytosolic NADH enters via shuttles of differing efficiency."),
 ]))

SECTIONS.append(dict(id="s8", num="2.8", title="Photosynthesis: capturing light",
 html="""
<p class="lead">Photosynthesis is respiration in reverse in outcome, and its close relative in mechanism: light drives electrons uphill, a proton gradient makes ATP, and the ATP fixes carbon.</p>
<span class="eq">6 CO<sub>2</sub> + 6 H<sub>2</sub>O + light → C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> + 6 O<sub>2</sub></span>
<p>In plants and algae it happens in the chloroplast; in cyanobacteria, on internal membranes. It has two stages.</p>
<h3>Light reactions (thylakoid membranes)</h3>
<p><b>Chlorophyll a</b> and accessory pigments (chlorophyll b, carotenoids) absorb mostly blue and red light, reflecting green. Absorbed photons excite electrons in <b>photosystem II</b>; the electrons are replaced by splitting water (<b>photolysis</b>), which releases O<sub>2</sub> as a by-product. Excited electrons pass down an electron transport chain, pumping H<sup>+</sup> into the thylakoid space, then are re-excited in <b>photosystem I</b> and used to reduce NADP<sup>+</sup> to <b>NADPH</b>. The proton gradient drives <b>ATP synthase</b>, exactly as in mitochondria but with the gradient oriented the other way (into the thylakoid). Products: ATP, NADPH, O<sub>2</sub>.</p>
<h3>Calvin cycle (stroma)</h3>
<p>The enzyme <b>rubisco</b> attaches CO<sub>2</sub> to a five-carbon acceptor (RuBP), producing two three-carbon molecules; ATP and NADPH from the light reactions reduce these to G3P, a sugar; most G3P regenerates RuBP, and the surplus builds glucose, sucrose, starch, and cellulose. Fixing one CO<sub>2</sub> costs 3 ATP and 2 NADPH; one glucose costs 18 ATP and 12 NADPH. Rubisco is slow and also reacts with O<sub>2</sub> (photorespiration), a flaw plants have worked around with C<sub>4</sub> and CAM pathways (Week 4).</p>
<div class="tw"><table>
<thead><tr><th></th><th>Photosynthesis</th><th>Cellular respiration</th></tr></thead>
<tbody>
<tr><td>Organelle and membrane</td><td>Chloroplast thylakoid</td><td>Mitochondrial inner membrane</td></tr>
<tr><td>Electron source and sink</td><td>Water → NADP<sup>+</sup></td><td>NADH → oxygen</td></tr>
<tr><td>Energy source</td><td>Light</td><td>Chemical (reduced carbon)</td></tr>
<tr><td>Proton gradient built into</td><td>Thylakoid lumen</td><td>Intermembrane space</td></tr>
<tr><td>Gas exchange</td><td>CO<sub>2</sub> in, O<sub>2</sub> out</td><td>O<sub>2</sub> in, CO<sub>2</sub> out</td></tr>
<tr><td>Shared machinery</td><td colspan="2">Electron transport chain, chemiosmosis, ATP synthase, NAD(P) carriers</td></tr>
</tbody></table></div>
<p>The two processes together make the biosphere a closed carbon loop and an open energy flow (§1.9). Oxygenic photosynthesis, evolved by cyanobacteria at least 2.4 billion years ago, oxygenated the atmosphere in the <b>Great Oxidation Event</b>, remade the planet's surface chemistry, poisoned most of the anaerobic biosphere, and made aerobic respiration, with its 15-fold energy advantage, possible.</p>
<div class="callout"><span class="label">Astrobiology note · pigments, oxygen, and other stars</span>Oxygen in an atmosphere is a candidate biosignature precisely because oxygenic photosynthesis is its main source on Earth. But abiotic oxygen from water photolysis is possible, and photosynthesis need not produce oxygen at all: anoxygenic photosynthesis using H<sub>2</sub>S or Fe<sup>2+</sup> as electron donors is older and still widespread. Pigment absorption also depends on the star: around a red M dwarf, photosynthesis tuned to infrared has been proposed, and the vegetation "red edge" that makes Earth's plants detectable from orbit might sit at a different wavelength. Week 13 returns to all of this.</div>
""",
 checks=[
  ("Where does the oxygen released by photosynthesis come from: CO₂ or H₂O? How was this established?", "From water, split at photosystem II. Isotope-labelling experiments with ¹⁸O-water produced ¹⁸O₂; ¹⁸O-CO₂ did not."),
  ("List three components shared by chloroplast and mitochondrial energy conversion, and the one thing that differs in direction.", "Electron transport chain, proton pumping, ATP synthase (and NAD(P) carriers). The proton gradient points into the thylakoid lumen but out of the mitochondrial matrix; ATP is made on the stroma/matrix side in both."),
  ("Why would a planet with only anoxygenic photosynthesis be hard to detect by an oxygen biosignature?", "No oxygen is released; electrons come from sulfide or iron instead of water. The biosphere could be extensive and the atmosphere still anoxic."),
 ]))

SECTIONS.append(dict(id="s9", num="2.9", title="The cell cycle and mitosis", figure="cycle",
 html="""
<p class="lead">Cells reproduce by copying their genome and dividing. In eukaryotes the process is sequenced by a cycle with checkpoints, and its failures are the biology of cancer.</p>
<p>The <b>cell cycle</b> has two main phases. <b>Interphase</b> (about 90 per cent of the cycle) is subdivided into <b>G<sub>1</sub></b> (growth, normal function), <b>S</b> (DNA synthesis: each chromosome is replicated into two identical <b>sister chromatids</b> joined at the centromere), and <b>G<sub>2</sub></b> (further growth, preparation for division). <b>M phase</b> is mitosis plus cytokinesis. Cells that stop dividing exit to <b>G<sub>0</sub></b>, where most adult neurons and muscle cells remain.</p>
<div class="tw"><table>
<thead><tr><th>Mitotic stage</th><th>What happens</th><th>What you see</th></tr></thead>
<tbody>
<tr><td><b>Prophase</b></td><td>Chromatin condenses into visible chromosomes; spindle begins to form from centrosomes; nucleolus disappears</td><td>Distinct X-shaped chromosomes appear</td></tr>
<tr><td><b>Prometaphase</b></td><td>Nuclear envelope fragments; spindle microtubules attach to kinetochores at each centromere</td><td>Chromosomes begin to move</td></tr>
<tr><td><b>Metaphase</b></td><td>Chromosomes align at the cell's equator (metaphase plate); each sister chromatid attached to the opposite pole</td><td>A single line of chromosomes</td></tr>
<tr><td><b>Anaphase</b></td><td>Cohesin cleaved; sister chromatids separate and are pulled to opposite poles; cell elongates</td><td>Two V-shaped groups moving apart</td></tr>
<tr><td><b>Telophase</b></td><td>Nuclear envelopes re-form around each set; chromosomes decondense; spindle disassembles</td><td>Two nuclei</td></tr>
<tr><td><b>Cytokinesis</b></td><td>Animals: actin–myosin ring pinches a cleavage furrow. Plants: vesicles build a cell plate that becomes the new wall</td><td>Two daughter cells</td></tr>
</tbody></table></div>
<p>The result is two genetically identical diploid cells, used for growth, repair, and asexual reproduction. The outcome depends on the fidelity of S phase (DNA replication with proofreading, error rate about one per 10<sup>9</sup> bases) and of anaphase (correct attachment, so each daughter receives exactly one copy of each chromosome).</p>
<h3>Checkpoints</h3>
<p>Progress is gated by <b>cyclin</b>–<b>cyclin-dependent kinase</b> (CDK) complexes whose activity rises and falls through the cycle. At the <b>G<sub>1</sub> checkpoint</b> the cell asks whether it is large enough, has nutrients, has received growth signals, and has undamaged DNA; the tumour suppressor <b>p53</b> halts the cycle if DNA is damaged and triggers repair or apoptosis. At the <b>G<sub>2</sub> checkpoint</b> it verifies replication is complete. At the <b>M (spindle) checkpoint</b> anaphase waits until every kinetochore is attached. <b>Cancer</b> is, at the cellular level, the loss of this control: mutations activate proto-oncogenes into oncogenes (accelerators stuck on) or inactivate tumour suppressors (brakes cut), and cells divide without the normal signals, ignore damage, and, in metastasis, lose adhesion and invade.</p>
<h3>Binary fission</h3>
<p>Prokaryotes divide more simply. The circular chromosome replicates from its origin; the two copies move apart as the cell elongates; the protein FtsZ (a tubulin relative) forms a ring at mid-cell and directs the inward growth of membrane and wall. No spindle and no nuclear envelope are needed, which is one reason it is fast.</p>
<div class="callout"><span class="label">Astrobiology note · division under radiation</span>The DNA-damage checkpoints exist because replication errors and radiation damage are constant. Beyond Earth's magnetosphere the ionising radiation flux is far higher and its damage more clustered (Week 14). Organisms that thrive there, Deinococcus radiodurans is the standard example, do not avoid damage; they have exceptional repair and multiple genome copies. Any assessment of life's viability in a high-radiation environment is really an assessment of repair capacity versus damage rate.</div>
""",
 checks=[
  ("A cell has 46 chromosomes in G₁. How many chromosomes and how many chromatids does it have at metaphase, and in each daughter cell after mitosis?", "Metaphase: 46 chromosomes, 92 chromatids (each chromosome has two sister chromatids). Each daughter: 46 chromosomes, 46 chromatids (one per chromosome)."),
  ("A drug prevents spindle microtubules from forming. At which stage does the cell arrest and why?", "Metaphase/spindle checkpoint. Without kinetochore attachment the checkpoint is not satisfied, so anaphase cannot begin. This is how vinca alkaloids and taxanes act in chemotherapy."),
  ("Why is p53 called 'the guardian of the genome'?", "It arrests the cycle at G₁ when DNA is damaged, promotes repair, and triggers apoptosis if repair fails, preventing propagation of mutations. It is mutated in about half of human cancers."),
 ]))

SECTIONS.append(dict(id="s10", num="2.10", title="Meiosis, variation, and the cellular basis of a biosignature",
 html="""
<p class="lead">Mitosis copies. Meiosis reshuffles, and in doing so supplies the heritable variation that the definition of life in Week 1 made central.</p>
<p><b>Meiosis</b> is one round of DNA replication followed by <b>two</b> divisions, producing four <b>haploid</b> cells from one <b>diploid</b> cell. In animals these are gametes; in plants, spores. Humans are diploid (2<i>n</i> = 46, in 23 homologous pairs, one of each pair from each parent); gametes are haploid (<i>n</i> = 23); fertilisation restores 2<i>n</i>.</p>
<div class="tw"><table>
<thead><tr><th>Stage</th><th>Key event</th></tr></thead>
<tbody>
<tr><td><b>Prophase I</b></td><td>Homologous chromosomes pair (synapsis) and exchange segments by <b>crossing over</b> at chiasmata: recombinant chromatids result</td></tr>
<tr><td><b>Metaphase I</b></td><td>Homologous <b>pairs</b> align at the plate; the orientation of each pair is random (<b>independent assortment</b>)</td></tr>
<tr><td><b>Anaphase I</b></td><td>Homologues separate; sister chromatids stay together. The reductional division: each daughter is haploid but with duplicated chromosomes</td></tr>
<tr><td><b>Meiosis II</b></td><td>Like mitosis: sister chromatids separate. Four haploid cells, each genetically unique</td></tr>
</tbody></table></div>
<div class="tw"><table>
<thead><tr><th></th><th>Mitosis</th><th>Meiosis</th></tr></thead>
<tbody>
<tr><td>DNA replications / divisions</td><td>1 / 1</td><td>1 / 2</td></tr>
<tr><td>Daughter cells</td><td>2, diploid, identical to parent</td><td>4, haploid, all different</td></tr>
<tr><td>Homologues pair and cross over</td><td>No</td><td>Yes (prophase I)</td></tr>
<tr><td>Purpose</td><td>Growth, repair, asexual reproduction</td><td>Gamete or spore formation; sexual reproduction</td></tr>
</tbody></table></div>
<p>Three sources of variation arise. <b>Crossing over</b> creates chromosomes with new allele combinations. <b>Independent assortment</b> of 23 pairs gives 2<sup>23</sup> (about 8.4 million) possible chromosome combinations per gamete. <b>Random fertilisation</b> multiplies that by the same number from the other parent. Add mutation, the ultimate source of new alleles, and every sexually produced individual is genetically unique. <b>Nondisjunction</b>, failure of chromosomes to separate, produces gametes with an extra or missing chromosome; trisomy 21 is the most familiar viable outcome.</p>
<p>Why sex, when asexual reproduction is faster and passes on all of a parent's genes? The prevailing answers are that recombination lets populations track changing environments and parasites, purges harmful mutations more efficiently, and brings beneficial mutations together. Whatever the balance of reasons, sexual recombination has been retained across almost all eukaryotic lineages, and prokaryotes achieve a similar end by horizontal gene transfer (Week 3).</p>
<h3>Collecting the thread</h3>
<p>A cell, as this week has described it, is a bounded compartment (§2.4) that maintains gradients against leakage by continuous work (§2.5–§2.6), harvests energy from a redox couple through a proton gradient (§2.7–§2.8), and copies itself with correction and, in eukaryotes, with recombination (§2.9–§2.10). Each clause maps to a measurable property. A boundary leaves lipids and morphology. Maintained gradients are chemical disequilibrium. Redox metabolism leaves isotopically fractionated carbon and sulfur, and, in an atmosphere, gas mixtures that should not coexist. Replication with variation is the hardest to detect remotely and the one that would settle the question.</p>
<div class="callout blue"><span class="label">Portfolio Entry 2 · Annotated cell and transport model</span>
Produce a labelled diagram of one cell type of your choice (bacterial, archaeal, plant, or animal) with: <b>(1)</b> every structure named and its function stated in one line; <b>(2)</b> five transport events drawn across the membrane, one each of simple diffusion, facilitated diffusion, osmosis, primary active transport, and either secondary active or bulk transport, each annotated with direction relative to gradient and energy source; <b>(3)</b> a 150-word note stating which features of your cell would leave a detectable trace after one billion years in sediment and which would not. Rubric: structural accuracy (35%), transport annotations (35%), preservation note (20%), clarity (10%).</div>
""",
 checks=[
  ("Distinguish the products of meiosis I from those of mitosis in a 2n = 4 cell.", "Meiosis I gives two cells each with 2 chromosomes (n), each chromosome still with two chromatids, and homologues separated. Mitosis gives two cells each with 4 chromosomes (2n), each with one chromatid, genetically identical."),
  ("At which meiotic stage does nondisjunction of homologous chromosomes occur, and what gametes result?", "Anaphase I. Two gametes with n + 1 and two with n – 1 for that chromosome."),
  ("Which of the four cellular properties collected in the final paragraph would a single flyby mass spectrometer be able to test?", "Boundary (lipids), and metabolism (isotopic fractionation or disequilibrium mixtures). Gradient maintenance would need a sample with live cells; replication with variation cannot be assessed remotely."),
 ]))

CHEAT = [
 ("Cell theory", "All organisms are cells; the cell is the unit of life; cells come from cells. Light microscopy resolves ~0.2 μm; EM ~0.2 nm. Resolution, not magnification, sets what is seen."),
 ("Size limits", "SA/V = 6/s for a cube: falls as cells grow. Lower limit ~0.2 μm (genome + ribosomes). Large cells are flat, long, or folded."),
 ("Prokaryote vs eukaryote", "No nucleus vs nucleus; circular vs linear DNA with histones; 70S vs 80S ribosomes; 0.5–5 vs 10–100 μm. Archaea: ether-linked branched lipids, no peptidoglycan, eukaryote-like transcription."),
 ("Organelles", "Nucleus (genome); ribosome (protein); rough ER (secreted proteins); smooth ER (lipids, detox); Golgi (sort, package); lysosome (digest); peroxisome (oxidise); mitochondrion (ATP); chloroplast (photosynthesis); vacuole (turgor); cytoskeleton (shape, transport)."),
 ("Membrane", "Fluid mosaic: phospholipid bilayer + proteins; ~8 nm; asymmetric. Unsaturation and cholesterol tune fluidity. Free crossing: small nonpolar. Needs protein: ions, large polar."),
 ("Passive transport", "Down gradient, no ATP: simple diffusion, facilitated diffusion (channel/carrier, saturable), osmosis (water toward solute). Hypotonic → swell/turgid; hypertonic → shrink/plasmolyse. Osmolarity counts particles."),
 ("Active transport", "Up gradient. Primary: ATP directly (Na⁺/K⁺ pump 3 out, 2 in). Secondary: rides another gradient (Na⁺–glucose symport). Bulk: endocytosis (phago-, pino-, receptor-mediated), exocytosis."),
 ("Respiration", "Glycolysis (cytosol, 2 ATP, no O₂) → pyruvate oxidation → citric acid cycle (matrix) → ETC + chemiosmosis (inner membrane, ~26–28 ATP). Total ~30–32. O₂ = final acceptor. Fermentation: 2 ATP, regenerates NAD⁺. Anaerobic respiration: other acceptors."),
 ("Photosynthesis", "Light reactions (thylakoid): water split, O₂ released, ATP + NADPH via proton gradient. Calvin cycle (stroma): rubisco fixes CO₂, 3 ATP + 2 NADPH per CO₂. Same chemiosmosis as respiration."),
 ("Cell cycle", "G₁ → S (replication) → G₂ → M (PMAT + cytokinesis). Checkpoints G₁ (p53), G₂, spindle. Cancer = lost control. Binary fission in prokaryotes."),
 ("Meiosis", "1 replication, 2 divisions → 4 haploid unique cells. Crossing over (prophase I), independent assortment (metaphase I), random fertilisation. Nondisjunction → aneuploidy."),
 ("Astrobiology thread", "Cell = boundary + maintained gradients + redox metabolism via proton gradient + replication with variation. Traces: lipids, morphology, disequilibrium, isotopes. Only variation is undetectable remotely."),
]

# ---------------------------------------------------------------- figures --
def fig_sav():
    w, h = 760, 300
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>Surface-area-to-volume ratio falls as size rises</title>']
    cubes = [(1, 30, "1 μm"), (2, 60, "2 μm"), (4, 120, "4 μm")]
    x = 40
    for s, px, lab in cubes:
        d = px*0.35
        o.append(f'<rect x="{x}" y="{200-px}" width="{px}" height="{px}" fill="#DCE6F6" stroke="#1F4FA8" stroke-width="1.5"/>')
        o.append(f'<path d="M{x} {200-px} l{d} -{d} h{px} v{px} l-{d} {d}" fill="#C5D3EE" stroke="#1F4FA8" stroke-width="1.5"/>')
        o.append(f'<path d="M{x+px} {200-px} l{d} -{d}" stroke="#1F4FA8" stroke-width="1.5"/>')
        sa, vol = 6*s*s, s**3
        o.append(f'<text x="{x+px/2+d/2:.0f}" y="228" text-anchor="middle" font-size="13" font-weight="800" fill="#0B1F47" {FONT}>side {lab}</text>')
        o.append(f'<text x="{x+px/2+d/2:.0f}" y="246" text-anchor="middle" font-size="12" fill="#555b73" {FONT}>SA {sa} μm² · V {vol} μm³</text>')
        o.append(f'<text x="{x+px/2+d/2:.0f}" y="266" text-anchor="middle" font-size="13" font-weight="800" fill="#0E6B1F" {FONT}>SA/V = {sa/vol:g}</text>')
        x += px + d + 60
    o.append(f'<text x="540" y="70" font-size="13" fill="#0B1F47" {FONT}>As side length doubles:</text>')
    o.append(f'<text x="540" y="92" font-size="13" fill="#0B1F47" {FONT}>surface ×4, volume ×8,</text>')
    o.append(f'<text x="540" y="114" font-size="13" font-weight="800" fill="#1F4FA8" {FONT}>ratio halves.</text>')
    o.append(f'<text x="540" y="146" font-size="12" fill="#555b73" {FONT}>Exchange happens at the surface;</text><text x="540" y="164" font-size="12" fill="#555b73" {FONT}>demand scales with volume.</text>')
    o.append('</svg>'); return "".join(o)


def fig_cells():
    w, h = 800, 330
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>Prokaryotic and eukaryotic cells compared</title>']
    # prokaryote (rod)
    o.append(f'<text x="170" y="30" text-anchor="middle" font-size="15" font-weight="800" fill="#1F4FA8" {FONT}>Prokaryote (~2 μm)</text>')
    o.append('<rect x="60" y="120" width="220" height="90" rx="45" fill="#fff" stroke="#1F4FA8" stroke-width="3"/>')
    o.append('<rect x="66" y="126" width="208" height="78" rx="39" fill="#F1F5FC" stroke="#1F4FA8" stroke-width="1.2" stroke-dasharray="3 3"/>')
    o.append('<path d="M120 165 q20 -25 40 0 t40 0 t40 0" fill="none" stroke="#0B1F47" stroke-width="2"/>')
    o.append('<circle cx="100" cy="150" r="7" fill="none" stroke="#0B1F47" stroke-width="1.5"/>')
    for (cx, cy) in [(90,185),(130,190),(200,185),(240,150),(255,180)]:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="#39FF14" stroke="#0E6B1F"/>')
    o.append('<path d="M280 165 q20 -14 40 0 q20 14 40 0" fill="none" stroke="#0B1F47" stroke-width="2"/>')
    for (x, y, t) in [(170,235,"nucleoid (circular DNA)"),(100,120,"plasmid"),(170,255,"ribosomes · wall · capsule"),(330,150,"flagellum")]:
        o.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="11.5" fill="#555b73" {FONT}>{t}</text>')
    # eukaryote
    o.append(f'<text x="580" y="30" text-anchor="middle" font-size="15" font-weight="800" fill="#1F4FA8" {FONT}>Eukaryote (~20 μm)</text>')
    o.append('<ellipse cx="580" cy="170" rx="180" ry="120" fill="#fff" stroke="#1F4FA8" stroke-width="3"/>')
    o.append('<circle cx="560" cy="160" r="45" fill="#DCE6F6" stroke="#1F4FA8" stroke-width="2"/><circle cx="560" cy="160" r="41" fill="none" stroke="#1F4FA8" stroke-width="1" stroke-dasharray="3 3"/><circle cx="552" cy="152" r="10" fill="#1F4FA8" fill-opacity=".5"/>')
    o.append('<path d="M610 130 q30 5 30 30 q0 25 -30 30" fill="none" stroke="#1F4FA8" stroke-width="1.5"/><path d="M618 138 q22 5 22 22 q0 20 -22 25" fill="none" stroke="#1F4FA8" stroke-width="1.5"/>')
    for (cx, cy) in [(470,120),(490,215),(680,200),(660,110)]:
        o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="22" ry="11" fill="#E8FFE0" stroke="#0E6B1F" stroke-width="1.5"/><path d="M{cx-14} {cy} q7 -8 14 0 t14 0" fill="none" stroke="#0E6B1F" stroke-width="1"/>')
    o.append('<path d="M640 240 h40 M640 250 h44 M640 260 h40" stroke="#1F4FA8" stroke-width="3" stroke-linecap="round"/>')
    for (cx, cy) in [(520,110),(510,230),(620,215),(700,160)]:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="3" fill="#39FF14" stroke="#0E6B1F"/>')
    for (x, y, t) in [(560,222,"nucleus + nucleolus"),(650,178,"ER"),(470,145,"mitochondria"),(662,278,"Golgi"),(760,250,"ribosomes")]:
        o.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="11.5" fill="#555b73" {FONT}>{t}</text>')
    o.append(f'<text x="400" y="318" text-anchor="middle" font-size="12" fill="#0B1F47" {FONT}>Shared by both: plasma membrane · cytoplasm · ribosomes · DNA. Not to scale: the eukaryote is ~10× longer, ~1000× the volume.</text>')
    o.append('</svg>'); return "".join(o)


def fig_membrane():
    w, h = 800, 300
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>Fluid mosaic membrane</title>']
    o.append(f'<text x="400" y="30" text-anchor="middle" font-size="13" fill="#555b73" {FONT}>Outside (extracellular fluid) — glycocalyx</text>')
    for i in range(0, 28):
        x = 40 + i*26
        if 9 <= i <= 11 or 18 <= i <= 20: continue
        for (hy, ty) in [(110, 1), (190, -1)]:
            o.append(f'<circle cx="{x}" cy="{hy}" r="9" fill="#1F4FA8"/>')
            o.append(f'<path d="M{x-4} {hy+ty*9} q-3 {ty*18} 0 {ty*36} M{x+4} {hy+ty*9} q3 {ty*18} 0 {ty*36}" fill="none" stroke="#0B1F47" stroke-width="2"/>')
    # channel protein
    o.append('<rect x="266" y="96" width="70" height="108" rx="18" fill="#E8FFE0" stroke="#0E6B1F" stroke-width="2"/><rect x="292" y="96" width="18" height="108" fill="#fff" stroke="#0E6B1F" stroke-width="1" stroke-dasharray="3 2"/>')
    o.append('<circle cx="301" cy="80" r="4" fill="#39FF14" stroke="#0E6B1F"/><path d="M301 86 v100" stroke="#0E6B1F" stroke-width="1.5" stroke-dasharray="4 3"/><path d="M301 214 l-4 -8 h8 z" fill="#0E6B1F"/>')
    # carrier protein
    o.append('<path d="M500 96 h70 v108 h-70 z" fill="#E8FFE0" stroke="#0E6B1F" stroke-width="2"/><path d="M518 96 q17 40 0 54 q-17 14 0 54" fill="none" stroke="#0E6B1F" stroke-width="1.5"/><circle cx="527" cy="150" r="6" fill="#39FF14" stroke="#0E6B1F"/>')
    # cholesterol
    for x in (150, 700):
        o.append(f'<rect x="{x-5}" y="118" width="10" height="34" rx="3" fill="#FFD166" stroke="#9A6A10"/>')
    # glycoprotein sugars
    for (x, y) in [(300,66),(288,58),(312,60)]:
        o.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#fff" stroke="#1F4FA8"/>')
    o.append(f'<text x="400" y="278" text-anchor="middle" font-size="13" fill="#555b73" {FONT}>Inside (cytosol) — cytoskeleton attaches here</text>')
    for (x, y, t) in [(301,236,"channel: ion passes down gradient"),(535,236,"carrier: binds, changes shape"),(150,172,"cholesterol"),(700,172,"cholesterol"),(60,150,"~8 nm")]:
        o.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="11.5" fill="#0B1F47" {FONT}>{t}</text>')
    o.append('</svg>'); return "".join(o)


def fig_tonicity():
    w, h = 760, 260
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>Cells in hypotonic, isotonic, and hypertonic solutions</title>']
    panels = [("Hypotonic", "water in → swells, may lyse", 44, 0.75, 6, 22), ("Isotonic", "no net movement → normal", 34, 1.0, 14, 14), ("Hypertonic", "water out → shrinks", 26, 1.0, 26, 8)]
    for i, (name, note, r, ry, dots_out, dots_in) in enumerate(panels):
        cx = 130 + i*250; cy = 125
        o.append(f'<rect x="{cx-105}" y="40" width="210" height="170" rx="12" fill="#F1F5FC" stroke="#C5D3EE"/>')
        o.append(f'<text x="{cx}" y="30" text-anchor="middle" font-size="14" font-weight="800" fill="#1F4FA8" {FONT}>{name}</text>')
        import random as _r; rnd = _r.Random(i+7)
        for _ in range(dots_out):
            x = rnd.uniform(cx-98, cx+98); y = rnd.uniform(48, 202)
            if (x-cx)**2 + ((y-cy)/ry)**2 > (r+8)**2: o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="2.5" fill="#1F4FA8"/>')
        o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*ry}" fill="#fff" stroke="#0E6B1F" stroke-width="2.5"/>')
        for _ in range(dots_in):
            x = rnd.uniform(cx-r+6, cx+r-6); y = rnd.uniform(cy-r*ry+6, cy+r*ry-6); o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="2.5" fill="#0E6B1F"/>')
        arrows = {"Hypotonic": [(cx-r-30, cy, cx-r-8, cy), (cx+r+30, cy, cx+r+8, cy)], "Hypertonic": [(cx-r-8, cy, cx-r-30, cy), (cx+r+8, cy, cx+r+30, cy)], "Isotonic": []}[name]
        for (x1, y1, x2, y2) in arrows:
            d = 1 if x2 > x1 else -1
            o.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#39FF14" stroke-width="4"/><path d="M{x2} {y2} l{-d*8} -5 v10 z" fill="#39FF14"/>')
        o.append(f'<text x="{cx}" y="236" text-anchor="middle" font-size="12" fill="#0B1F47" {FONT}>{note}</text>')
    o.append(f'<text x="380" y="256" text-anchor="middle" font-size="11.5" fill="#555b73" {FONT}>Dots = solute particles. Green arrows = net water movement (osmosis), toward higher solute concentration.</text>')
    o.append('</svg>'); return "".join(o)


def fig_chemiosmosis():
    w, h = 800, 300
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>Chemiosmosis in the mitochondrial inner membrane</title>']
    o.append('<rect x="40" y="120" width="720" height="60" fill="#DCE6F6" stroke="#1F4FA8"/>')
    o.append(f'<text x="60" y="60" font-size="13" font-weight="800" fill="#1F4FA8" {FONT}>Intermembrane space — high [H⁺]</text>')
    o.append(f'<text x="60" y="262" font-size="13" font-weight="800" fill="#1F4FA8" {FONT}>Matrix — low [H⁺]</text>')
    for i, (x, lab) in enumerate([(120, "I"), (260, "III"), (400, "IV")]):
        o.append(f'<rect x="{x-35}" y="100" width="70" height="100" rx="14" fill="#E8FFE0" stroke="#0E6B1F" stroke-width="2"/><text x="{x}" y="156" text-anchor="middle" font-size="16" font-weight="800" fill="#0E6B1F" {FONT}>{lab}</text>')
        o.append(f'<path d="M{x+26} 196 L{x+26} 82" stroke="#1F4FA8" stroke-width="3"/><path d="M{x+26} 78 l-6 10 h12 z" fill="#1F4FA8"/><text x="{x+36}" y="92" font-size="12" font-weight="700" fill="#1F4FA8" {FONT}>H⁺</text>')
    o.append('<path d="M155 150 h70 M295 150 h70" stroke="#0B1F47" stroke-width="2" stroke-dasharray="5 3"/><text x="190" y="142" text-anchor="middle" font-size="11" fill="#0B1F47" %s>e⁻</text><text x="330" y="142" text-anchor="middle" font-size="11" fill="#0B1F47" %s>e⁻</text>' % (FONT, FONT))
    o.append(f'<text x="120" y="228" text-anchor="middle" font-size="12" fill="#0B1F47" {FONT}>NADH → NAD⁺ + e⁻</text>')
    o.append(f'<text x="420" y="228" text-anchor="middle" font-size="12" fill="#0B1F47" {FONT}>½ O₂ + 2 H⁺ + 2 e⁻ → H₂O</text>')
    # ATP synthase
    o.append('<rect x="590" y="95" width="60" height="60" rx="30" fill="#39FF14" stroke="#0E6B1F" stroke-width="2"/><rect x="605" y="150" width="30" height="55" fill="#39FF14" stroke="#0E6B1F" stroke-width="2"/><rect x="580" y="195" width="80" height="40" rx="14" fill="#39FF14" stroke="#0E6B1F" stroke-width="2"/>')
    o.append('<path d="M620 78 L620 200" stroke="#1F4FA8" stroke-width="3" stroke-dasharray="6 3"/><path d="M620 206 l-6 -10 h12 z" fill="#1F4FA8"/><text x="636" y="80" font-size="12" font-weight="700" fill="#1F4FA8" %s>H⁺ flows back</text>' % FONT)
    o.append(f'<text x="620" y="262" text-anchor="middle" font-size="13" font-weight="800" fill="#0E6B1F" {FONT}>ATP synthase: ADP + Pᵢ → ATP</text>')
    o.append(f'<text x="700" y="150" text-anchor="middle" font-size="11.5" fill="#555b73" {FONT}>inner</text><text x="700" y="165" text-anchor="middle" font-size="11.5" fill="#555b73" {FONT}>membrane</text>')
    o.append('</svg>'); return "".join(o)


def fig_cycle():
    w, h = 760, 320; cx, cy, R = 250, 160, 110
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img"><title>The eukaryotic cell cycle</title>']
    segs = [("G₁", 0, 0.40, "#DCE6F6"), ("S", 0.40, 0.70, "#C5D3EE"), ("G₂", 0.70, 0.88, "#DCE6F6"), ("M", 0.88, 1.0, "#39FF14")]
    for name, a0, a1, col in segs:
        t0, t1 = -math.pi/2 + 2*math.pi*a0, -math.pi/2 + 2*math.pi*a1
        x0, y0 = cx + R*math.cos(t0), cy + R*math.sin(t0); x1, y1 = cx + R*math.cos(t1), cy + R*math.sin(t1)
        large = 1 if (a1-a0) > 0.5 else 0
        o.append(f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{R} {R} 0 {large} 1 {x1:.1f} {y1:.1f} Z" fill="{col}" stroke="#fff" stroke-width="3"/>')
        tm = (t0+t1)/2; o.append(f'<text x="{cx+0.68*R*math.cos(tm):.0f}" y="{cy+0.68*R*math.sin(tm)+5:.0f}" text-anchor="middle" font-size="16" font-weight="800" fill="#0B1F47" {FONT}>{name}</text>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="46" fill="#fff" stroke="#1F4FA8"/><text x="{cx}" y="{cy-4}" text-anchor="middle" font-size="12" fill="#1F4FA8" font-weight="800" {FONT}>Interphase</text><text x="{cx}" y="{cy+12}" text-anchor="middle" font-size="11" fill="#555b73" {FONT}>≈ 90% of cycle</text>')
    # checkpoints
    for a, lab in [(0.40, "G₁ checkpoint: size, nutrients, DNA intact (p53)"), (0.88, "G₂ checkpoint: replication complete"), (0.96, "Spindle checkpoint: all kinetochores attached")]:
        t = -math.pi/2 + 2*math.pi*a; x, y = cx + R*math.cos(t), cy + R*math.sin(t)
        o.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#fff" stroke="#0E6B1F" stroke-width="3"/>')
    for i, t in enumerate(["G₁: growth; exit to G₀ possible", "S: DNA replication → sister chromatids", "G₂: growth, checks", "M: mitosis (PMAT) + cytokinesis", "Circles = checkpoints (G₁ / G₂ / spindle)"]):
        o.append(f'<text x="420" y="{70+i*32}" font-size="13" fill="#0B1F47" {FONT}>{t}</text>')
    o.append(f'<text x="420" y="250" font-size="12" fill="#555b73" {FONT}>Cyclin–CDK activity rises and falls to drive each transition.</text>')
    o.append('</svg>'); return "".join(o)


FIGS = {
 "sav": ("Surface-area-to-volume ratio falls as size rises", "Exchange capacity scales with surface, demand with volume, so a cell that doubles in size halves its supply per unit of cytoplasm.", fig_sav),
 "cells": ("Prokaryotic and eukaryotic cells compared", "Both share a membrane, cytoplasm, ribosomes, and DNA. The eukaryote adds a nucleus and compartments; the prokaryote wins on speed and surface-to-volume.", fig_cells),
 "membrane": ("The fluid mosaic membrane", "A phospholipid bilayer with embedded channel and carrier proteins, cholesterol buffering fluidity, and carbohydrate chains facing outward.", fig_membrane),
 "tonicity": ("Cells in hypotonic, isotonic, and hypertonic solutions", "Water moves toward the higher solute concentration. Animal cells swell or shrink; walled cells become turgid or plasmolysed.", fig_tonicity),
 "chemiosmosis": ("Chemiosmosis in the mitochondrial inner membrane", "Electron transport pumps protons out of the matrix; their return through ATP synthase makes ATP. Chloroplasts and bacteria use the same design.", fig_chemiosmosis),
 "cycle": ("The eukaryotic cell cycle", "Interphase occupies most of the cycle; checkpoints gate the transitions. Cancer is the loss of these controls.", fig_cycle),
}
