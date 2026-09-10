# -*- coding: utf-8 -*-
"""Course metadata extracted from RTU_Astrobiology_Three_Term_Syllabus.docx"""

COURSE = {
    "code": "ASTBIO 201 (Proposed)",
    "title": "Astrobiology",
    "units": "3 units",
    "contact": "3 hours/week (45 hours)",
    "prereq": "None; senior high school biology and physics are recommended",
    "coreq": "None",
    "semester": "1st Semester",
    "ay": "2026-2027",
    "faculty": "Dr. Ryan Manuel D. Guido",
    "college": "College of Arts and Sciences",
    "department": "Department of Earth and Space Sciences",
    "program": "Bachelor of Science in Astronomy",
    "revision": "Revision No. 1",
    "created": "21 August 2026",
    "effectivity": "1st Semester, AY 2026-2027",
    "description": (
        "This course develops the biological knowledge needed to study life in the universe. "
        "Term 1 introduces general biology, cell structure and function, genetics, evolution, taxonomy, "
        "microorganisms, botany, zoology, and ecology. Term 2 examines human anatomy and physiology, "
        "homeostasis, biophysics, and the physics of the human body. Term 3 focuses on space life science "
        "and astrobiology, including origins of life, planetary habitability, extremophiles, biosignatures, "
        "life-detection strategies, biological responses to space environments, closed ecosystems, and "
        "planetary protection."
    ),
}

VMV = {
    "vision": "A smart and transnational university.",
    "vision_fil": "Isang smart at transnasyonal na unibersidad.",
    "mission": ("To produce competent and socially responsible professionals through innovative instructions, "
                "high-impact research, and sustainable extension services responsive to the diverse needs of "
                "glocal communities."),
    "philosophy": ("The Rizal Technological University believes in nurturing the creative potentials of Filipinos "
                   "to excel in a dynamic world order and advocates commitment to global peace and sustainable "
                   "development along with sense of moral responsibility and cultural patronage."),
    "values": "Integrity, Nationalism, Inclusivity, Excellence, Innovation",
    "goal": ("Advance scientific literacy, inquiry, and innovation through interdisciplinary education and research "
             "responsive to national and global needs."),
    "objectives": ("Develop strong foundations in the natural and quantitative sciences; strengthen research and "
                   "data-analysis competencies; and promote ethical, inclusive, and sustainable scientific practice."),
    "peo": ("Within three to five years after graduation, graduates are expected to apply astronomy and space-science "
            "knowledge in professional or research settings, communicate evidence responsibly, collaborate across "
            "disciplines, and pursue continuing professional development."),
}

PROGRAM_OUTCOMES = [
    ("PO1", "Scientific knowledge", "Integrates relevant concepts from astronomy, physics, biology, Earth science, and space science when explaining natural phenomena."),
    ("PO2", "Scientific inquiry and data analysis", "Formulates investigable questions, selects appropriate methods, analyzes evidence, and evaluates uncertainty."),
    ("PO3", "Quantitative and systems reasoning", "Uses mathematical, computational, and systems models to interpret interacting processes and solve scientific problems."),
    ("PO4", "Communication and collaboration", "Communicates scientific findings clearly and contributes responsibly to individual and team-based work."),
    ("PO5", "Ethics, sustainability, and lifelong learning", "Applies ethical, inclusive, sustainable, and planetary-protection principles while pursuing continuing learning."),
]

COURSE_OUTCOMES = [
    ("CO1", "Explain the chemical, cellular, genetic, metabolic, evolutionary, and ecological foundations of life.", ["E","I","I","","I"]),
    ("CO2", "Apply taxonomy, systematics, and phylogeny to classify organisms and interpret biological diversity.", ["E","E","I","","I"]),
    ("CO3", "Compare the organization, reproduction, physiology, and adaptations of representative plants, animals, and microorganisms.", ["E","E","I","I","E"]),
    ("CO4", "Describe the organization and coordinated functions of the major human organ systems using appropriate anatomical and physiological terminology.", ["E","I","E","","E"]),
    ("CO5", "Apply biophysical principles and quantitative reasoning to human movement, circulation, respiration, neural signaling, sensory function, thermoregulation, and radiation exposure.", ["E","E","E","","E"]),
    ("CO6", "Explain major astrobiological concepts involving the origin and evolution of life, habitability, extremophiles, biosignatures, and planetary environments.", ["E","E","E","I","E"]),
    ("CO7", "Evaluate evidence and methods used in life detection, space biology, closed ecosystems, and planetary protection while recognizing uncertainty and false positives.", ["E","D","E","E","D"]),
    ("CO8", "Design and communicate an evidence-based astrobiological investigation or habitability assessment for a selected extraterrestrial environment.", ["D","D","D","D","D"]),
]

TERMS = {
    1: {"name": "Term 1", "label": "Foundations of life", "weeks": "Weeks 1-5",
        "blurb": "The chemistry, cells, genetics, and diversity that define what life is and how it is organised on one planet.",
        "accent": "--t1"},
    2: {"name": "Term 2", "label": "The body as a physical system", "weeks": "Weeks 6-10",
        "blurb": "Human anatomy and physiology read through physics: levers, pressure, flow, potentials, optics, and radiation.",
        "accent": "--t2"},
    3: {"name": "Term 3", "label": "Life beyond Earth", "weeks": "Weeks 11-15",
        "blurb": "Origins, habitability, biosignatures, organisms in space environments, and the ethics of contact and contamination.",
        "accent": "--t3"},
}

GRADING = [("Coursework", 20), ("Attendance", 10), ("Participation", 20), ("Major examinations", 35), ("Project/s", 15)]
GRADING_NOTE = "Major examinations: Term 1 - 10%; Term 2 - 10%; Term 3/Final - 15%."

MAJOR_OUTPUTS = [
    ("Term 1 portfolio", "Biological foundations, cell biology, taxonomy, botany, and zoology outputs."),
    ("Term 2 portfolio", "Human anatomy and physiology system maps, practical tasks, and biophysics problem sets."),
    ("Term 3 case study", "Habitability, biosignature, or life-detection evidence analysis."),
    ("Astrobiology capstone", "A 6-8 page investigation or habitability assessment, matrix, diagram, presentation, and individual reflection."),
    ("Major examinations", "Individual Term 1, Term 2, and Term 3 integrative assessments."),
]

REFERENCES = [
    ("OpenStax Biology 2e", "Cells, genetics, evolution, biodiversity, botany, zoology, and ecology."),
    ("OpenStax Anatomy and Physiology 2e", "Human anatomy, physiology, and homeostasis."),
    ("OpenStax Microbiology", "Microbial diversity, metabolism, genetics, and extremophiles."),
    ("OpenStax College Physics 2e", "Mechanics, fluids, gases, electricity, sound, optics, and radiation."),
]
READINGS = [
    ("NASA Astrobiology Program", "Astrobiology's core questions and current scientific context."),
    ("NASA: The Human Body in Space", "Body-system responses to spaceflight."),
    ("NASA: Five Hazards of Human Spaceflight", "Spaceflight risk framework."),
    ("NASA Space Crops", "Plant biology and bioregenerative support beyond Earth."),
]

POLICIES = [
    ("Preparation and attendance", "Students are expected to complete assigned readings and participate in scheduled learning activities. Attendance and make-up work follow University policy."),
    ("Scientific evidence and integrity", "Claims must be supported by credible sources. Students must distinguish data, models, hypotheses, and speculation and must not fabricate references or evidence."),
    ("Generative AI", "AI tools may be used only as permitted by the instructor and must be disclosed. Students remain responsible for accuracy, originality, and source verification."),
    ("Safety and privacy", "Activities are educational and non-diagnostic. Self-measurement is optional; equivalent simulated data will be available. Personal health information must not be required or disclosed."),
    ("Collaboration and accessibility", "Group work must identify individual contributions. Reasonable alternatives will be provided for activities involving vision, hearing, mobility, physiological measurement, or public presentation."),
]

CQI = [
    ("RTU-OVPASA-UCIO-F018", "Syllabus Development and Revision Request Form"),
    ("RTU-OVPASA-UCIO-F019", "Course Syllabus Acknowledgement Form"),
    ("RTU-OVPASA-UCIO-F035", "Program Outcomes Assessment and Evaluation Matrix"),
    ("RTU-OVPASA-UCIO-F036", "Stakeholder Consultation Survey Form"),
]
