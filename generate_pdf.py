from fpdf import FPDF

def clean_text(text):
    replacements = {
        "’": "'",
        "–": "-",
        "€": "euros",
        "é": "e",
        "è": "e",
        "à": "a",
        "ê": "e",
        "â": "a",
        "î": "i",
        "ô": "o",
        "û": "u",
        "ç": "c"
    }
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    return text

class ProjectPDF(FPDF):
    def header(self):
        if hasattr(self, 'current_title'):
            self.set_font("Helvetica", "B", 14)
            self.set_text_color(30, 30, 30)
            self.cell(0, 10, self.current_title, ln=True, align="C")
            self.ln(5)

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(0, 51, 102)
        self.cell(0, 8, title, ln=True)
        self.ln(1)

    def chapter_body(self, body):
        self.set_font("Helvetica", "", 11)
        self.set_text_color(0)
        self.multi_cell(0, 8, body)
        self.ln(4)

    def add_project(self, title, sections):
        self.add_page()
        self.current_title = title
        self.header()
        for section_title, section_body in sections.items():
            self.chapter_title(section_title)
            self.chapter_body(section_body)

# Contenus des projets
project_1 = {
    "Titre du Projet": "SAV Batiment+ : Service Apres-Vente pour Carrelage, Electricite et Peinture",
    "Resume Executif": "Service SAV specialise dans les materiaux de construction, offrant une assistance apres achat.",
    "Problematique": "Manque de support technique fiable apres achat des materiaux.",
    "Objectifs": "- Court terme : equipe pilote\n- Moyen terme : extension\n- Long terme : leader national",
    "Cible": "Particuliers, boutiques, promoteurs, artisans.",
    "Solution Proposee": "Service mobile, packs SAV, partenariat boutiques.",
    "Business Model": "Paiement intervention, abonnement boutiques.",
    "Besoin de Financement": "15 000 euros pour equipement, equipe et pub.",
    "Avantages Investisseurs": "Rentabilite rapide, secteur en croissance."
}

project_2 = {
    "Titre du Projet": "MotoLink Express : Livraison Urbaine Rapide a Moto",
    "Resume Executif": "Service de livraison rapide et simple, avec appli, WhatsApp ou appel.",
    "Problematique": "Services de livraison lents, inaccessibles aux particuliers.",
    "Objectifs": "- Court terme : lancement pilote\n- Moyen terme : developpement plateforme\n- Long terme : extension nationale",
    "Cible": "Commercants, entreprises, e-commerce, particuliers.",
    "Solution Proposee": "Livreurs formes, appli simple, paiement mobile.",
    "Business Model": "Paiement course, abonnements, pub locale.",
    "Besoin de Financement": "10 000 a 12 000 euros pour motos, appli, pub.",
    "Avantages Investisseurs": "Marche en croissance, modele duplicable."
}

# Nettoyage
project_1_clean = {k: clean_text(v) for k, v in project_1.items()}
project_2_clean = {k: clean_text(v) for k, v in project_2.items()}

# Creer et generer le PDF
pdf = ProjectPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_project("PROJET 1 : SAV Batiment+", project_1_clean)
pdf.add_project("PROJET 2 : MotoLink Express", project_2_clean)

pdf.output("Projets_Mr_Hie_G_Michel.pdf")
print("PDF genere avec succes.")
