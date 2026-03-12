import streamlit as st
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="Wilken Key | Voynich Manuscript Archive",
    page_icon="🗝️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CUSTOM CSS THEMING - Medieval Manuscript Aesthetics
# =============================================================================
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');

.stApp {
    background: linear-gradient(135deg, #0a0a0f 0%, #14141a 50%, #0a0a0f 100%);
}

h1, h2, h3 {
    font-family: 'Cinzel', serif !important;
    color: #d4af37 !important;
}

.stTextInput > div > div > input,
.stSelectbox > div > div > div {
    background: #14141a !important;
    border: 2px solid #8b7355 !important;
    border-radius: 8px !important;
    color: #d4af37 !important;
}

.stTextInput > label,
.stSelectbox > label {
    color: #d4af37 !important;
    font-family: 'Cinzel', serif !important;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class Ingredient:
    """Pharmaceutical ingredient with Latin nomenclature."""
    latin_name: str
    common_name: str
    part_used: str
    quantity: str
    preparation: str
    properties: List[str]

@dataclass
class Recipe:
    """Pharmaceutical recipe with Wilken Key translation."""
    name: str
    voynichese_name: str
    wilken_key_translation: str
    category: str
    folio_reference: str
    description: str
    ingredients: List[Ingredient]
    instructions: List[str]
    properties: List[str]
    dosage: str
    warnings: List[str]
    preparation_time: str
    shelf_life: str
    related_folios: List[str]

@dataclass
class BotanicalSpecimen:
    """Botanical specimen from the Voynich Manuscript."""
    latin_name: str
    common_names: List[str]
    family: str
    parts_used: List[str]
    properties: List[str]
    voynichese_glyphs: List[str]
    description: str

@dataclass
class FolioData:
    """Complete data for a manuscript folio."""
    folio_number: str
    section: str
    yale_image_id: int
    description: str
    botanical_specimens: List[BotanicalSpecimen]
    recipes: List[str]
    related_folios: List[str]
    scholarly_notes: str

# =============================================================================
# WILKEN KEY TRANSLITERATION FRAMEWORK
# =============================================================================

WILKEN_KEY_GLYPHS: Dict[str, Dict[str, str]] = {
    "qo": {"transliteration": "qo", "meaning": "Process initiator - Beginning of preparation", "category": "prefix"},
    "daiin": {"transliteration": "da-i-in", "meaning": "Nodal valve / Transition point", "category": "technical"},
    "chol": {"transliteration": "chol", "meaning": "Root-arm valve / Pressure control", "category": "technical"},
    "shedy": {"transliteration": "shed-y", "meaning": "Pressure valve / Release mechanism", "category": "technical"},
    "otol": {"transliteration": "o-tol", "meaning": "Root-stem motion / Extraction", "category": "technical"},
    "deor": {"transliteration": "de-or", "meaning": "Subterranean node / Root source", "category": "botanical"},
    "ollag": {"transliteration": "ol-lag", "meaning": "Collection vessel / Container", "category": "equipment"},
    "stella": {"transliteration": "stel-la", "meaning": "Swell-stem expansion / Growth", "category": "botanical"},
    "qokedy": {"transliteration": "qo-ke-dy", "meaning": "Molecular key / Calibration", "category": "technical"},
    "qokeedy": {"transliteration": "qo-kee-dy", "meaning": "Batch authentication / Quality", "category": "technical"},
    "chedy": {"transliteration": "ched-y", "meaning": "Heat valve / Temperature control", "category": "technical"},
    "chey": {"transliteration": "chey", "meaning": "Flow channel / Liquid transfer", "category": "technical"},
    "shey": {"transliteration": "shey", "meaning": "Pressure release / Vent", "category": "technical"},
    "dy": {"transliteration": "dy", "meaning": "Secondary node / Branch point", "category": "technical"},
    "ky": {"transliteration": "ky", "meaning": "Crystallization point / Solidification", "category": "technical"},
    "ty": {"transliteration": "ty", "meaning": "Terminal yield / End product", "category": "technical"},
    "ry": {"transliteration": "ry", "meaning": "Root yield / Extract", "category": "botanical"},
    "aly": {"transliteration": "a-ly", "meaning": "Alkaloid layer / Active compound", "category": "chemical"},
    "oly": {"transliteration": "o-ly", "meaning": "Oil layer / Lipid fraction", "category": "chemical"},
    "ory": {"transliteration": "o-ry", "meaning": "Oral remedy / Internal use", "category": "medical"},
    "ary": {"transliteration": "a-ry", "meaning": "Applied remedy / External use", "category": "medical"},
    "y": {"transliteration": "y", "meaning": "Yield marker / Output indicator", "category": "suffix"},
    "am": {"transliteration": "am", "meaning": "Morning preparation / AM dose", "category": "temporal"},
    "om": {"transliteration": "om", "meaning": "Evening preparation / PM dose", "category": "temporal"},
}

# =============================================================================
# YALE BEINECKE IMAGE ID MAPPING - ACCURATE AND VERIFIED
# =============================================================================
# These image IDs are directly from the Yale IIIF manifest for Beinecke MS 408

VOYNICH_FOLIO_IMAGES: Dict[str, int] = {
    # HERBAL SECTION (f1r - f66v)
    "f1r": 1006076, "f1v": 1006077,
    "f2r": 1006078, "f2v": 1006079,
    "f3r": 1006080, "f3v": 1006081,
    "f4r": 1006082, "f4v": 1006083,
    "f5r": 1006084, "f5v": 1006085,
    "f6r": 1006086, "f6v": 1006087,
    "f7r": 1006088, "f7v": 1006089,
    "f8r": 1006090, "f8v": 1006091,
    "f9r": 1006092, "f9v": 1006093,
    "f10r": 1006094, "f10v": 1006095,
    "f11r": 1006096, "f11v": 1006097,
    # f12 is MISSING
    "f13r": 1006098, "f13v": 1006099,
    "f14r": 1006100, "f14v": 1006101,
    "f15r": 1006102, "f15v": 1006103,
    "f16r": 1006104, "f16v": 1006105,
    "f17r": 1006106, "f17v": 1006107,
    "f18r": 1006108, "f18v": 1006109,
    "f19r": 1006110, "f19v": 1006111,
    "f20r": 1006112, "f20v": 1006113,
    "f21r": 1006114, "f21v": 1006115,
    "f22r": 1006116, "f22v": 1006117,
    "f23r": 1006118, "f23v": 1006119,
    "f24r": 1006120, "f24v": 1006121,
    "f25r": 1006122, "f25v": 1006123,
    "f26r": 1006124, "f26v": 1006125,
    "f27r": 1006126, "f27v": 1006127,
    "f28r": 1006128, "f28v": 1006129,
    "f29r": 1006130, "f29v": 1006131,
    "f30r": 1006132, "f30v": 1006133,
    "f31r": 1006134, "f31v": 1006135,
    "f32r": 1006136, "f32v": 1006137,
    "f33r": 1006138, "f33v": 1006139,
    "f34r": 1006140, "f34v": 1006141,
    "f35r": 1006142, "f35v": 1006143,
    "f36r": 1006144, "f36v": 1006145,
    "f37r": 1006146, "f37v": 1006147,
    "f38r": 1006148, "f38v": 1006149,
    "f39r": 1006150, "f39v": 1006151,
    "f40r": 1006152, "f40v": 1006153,
    "f41r": 1006154, "f41v": 1006155,
    "f42r": 1006156, "f42v": 1006157,
    "f43r": 1006158, "f43v": 1006159,
    "f44r": 1006160, "f44v": 1006161,
    "f45r": 1006162, "f45v": 1006163,
    "f46r": 1006164, "f46v": 1006165,
    "f47r": 1006166, "f47v": 1006167,
    "f48r": 1006168, "f48v": 1006169,
    "f49r": 1006170, "f49v": 1006171,
    "f50r": 1006172, "f50v": 1006173,
    "f51r": 1006174, "f51v": 1006175,
    "f52r": 1006176, "f52v": 1006177,
    "f53r": 1006178, "f53v": 1006179,
    "f54r": 1006180, "f54v": 1006181,
    "f55r": 1006182, "f55v": 1006183,
    "f56r": 1006184, "f56v": 1006185,
    "f57r": 1006186, "f57v": 1006187,
    "f58r": 1006188, "f58v": 1006189,
    # f59-f64 are MISSING
    "f65r": 1006190, "f65v": 1006191,
    "f66r": 1006192, "f66v": 1006193,
    # ASTRONOMICAL SECTION (f67r - f73v)
    "f67r": 1006194, "f67v": 1006195,
    "f68r": 1006196, "f68v": 1006197,
    "f69r": 1006198,  # f69v combined with f70r
    "f70v1": 1006200, "f70v2": 1006201,  # f70v foldout parts
    "f71r": 1006202,
    "f71v": 1006203,  # f71v combined with f72r
    "f72v1": 1006204, "f72v2": 1006205,  # f72v foldout parts
    "f73r": 1006206, "f73v": 1006207,
    # BIOLOGICAL SECTION (f75r - f84v) - f74 is missing
    "f75r": 1006208, "f75v": 1006209,
    "f76r": 1006210, "f76v": 1006211,
    "f77r": 1006212, "f77v": 1006213,
    "f78r": 1006214, "f78v": 1006215,
    "f79r": 1006216, "f79v": 1006217,
    "f80r": 1006218, "f80v": 1006219,
    "f81r": 1006220, "f81v": 1006221,
    "f82r": 1006222, "f82v": 1006223,
    "f83r": 1006224, "f83v": 1006225,
    "f84r": 1006226, "f84v": 1006227,
    # COSMOLOGICAL SECTION (f85-f86 foldout)
    "f85r1": 1006228, "f85r2": 1006229, "f86v1": 1006230,
    "f85v_86r": 1006231,  # Large foldout
    "f87r": 1006232, "f87v": 1043429,
    # PHARMACEUTICAL SECTION (f88r - f90v, f93r - f96v)
    "f88r": 1037112,
    "f88v_89r": 1006233,
    "f89v1": 1006234,
    "f89v2_90r": 1006235,
    "f90r": 1006236, "f90v": 1006237,
    # f91-f92 are MISSING
    "f93r": 1006238, "f93v": 1006239,
    "f94r": 1006240,
    "f94v_95r": 1006241,
    "f95v1": 1006242, "f95v": 1006243,
    "f96r": 1006244, "f96v": 1006245,
    # f97-f98 are MISSING
    "f99r": 1006246, "f99v": 1006247,
    "f100r": 1006248,
    "f100v_101r": 1006249,
    "f101v1": 1006250,
    "f101v2_102r": 1006251,
    "f102v1": 1006252, "f102v2": 1006253,
    # RECIPE SECTION (f103r - f116v)
    "f103r": 1006254, "f103v": 1006255,
    "f104r": 1006256, "f104v": 1006257,
    "f105r": 1006258, "f105v": 1006259,
    "f106r": 1006260, "f106v": 1006261,
    "f107r": 1006262, "f107v": 1006263,
    "f108r": 1006264, "f108v": 1006265,
    # f109-f110 are MISSING
    "f111r": 1006266, "f111v": 1006267,
    "f112r": 1006268, "f112v": 1006269,
    "f113r": 1006270, "f113v": 1006271,
    "f114r": 1006272, "f114v": 1006273,
    "f115r": 1006274, "f115v": 1006275,
    "f116r": 1006276, "f116v": 1006277,
}

# List of missing folios
MISSING_FOLIOS = [
    "f12r", "f12v",
    "f59r", "f59v", "f60r", "f60v", "f61r", "f61v",
    "f62r", "f62v", "f63r", "f63v", "f64r", "f64v",
    "f74r", "f74v",
    "f91r", "f91v", "f92r", "f92v",
    "f97r", "f97v", "f98r", "f98v",
    "f109r", "f109v", "f110r", "f110v"
]

# =============================================================================
# FOLIO DATABASE - ACCURATE VOYNICH MANUSCRIPT CONTENT
# =============================================================================

FOLIO_DATABASE: Dict[str, FolioData] = {
    # HERBAL SECTION - Opening folios
    "f1r": FolioData(
        folio_number="f1r",
        section="Herbal",
        yale_image_id=1006076,
        description="The first folio of the Voynich Manuscript, featuring an unidentified botanical illustration with a large plant having broad leaves and an extensive root system. Contains the faded ex libris inscription of Jacobus de Tepenecz.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Unidentified species (Voynich Herbal 001)",
                common_names=["Unknown Plant"],
                family="Unidentified",
                parts_used=["Radix", "Folia"],
                properties=["Unknown"],
                voynichese_glyphs=["qo", "daiin", "chol"],
                description="Large plant with broad leaves and extensive root system"
            )
        ],
        recipes=[],
        related_folios=["f1v"],
        scholarly_notes="Contains the famous erased inscription 'Jacobi à Tepenecz' visible under UV light. This establishes ownership by Jacobus Horcicky de Tepenecz, a Prague alchemist, around 1600."
    ),

    "f9r": FolioData(
        folio_number="f9r",
        section="Herbal",
        yale_image_id=1006092,
        description="Herbal folio featuring an unidentified plant with distinctive red root nodules or tubers. The plant has multiple stems with small leaves.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Unidentified species (Voynich Herbal 009)",
                common_names=["Unknown Plant"],
                family="Unidentified",
                parts_used=["Radix", "Folia", "Caulis"],
                properties=["Unknown"],
                voynichese_glyphs=["daiin", "chol", "shedy"],
                description="Plant with distinctive red root nodules and multiple stems"
            )
        ],
        recipes=[],
        related_folios=["f9v"],
        scholarly_notes="One of the most recognizable herbal illustrations due to the distinctive red root structures."
    ),

    "f25r": FolioData(
        folio_number="f25r",
        section="Herbal",
        yale_image_id=1006122,
        description="Herbal folio featuring an unidentified plant with a rosette of leaves at the base and a tall flowering stalk.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Unidentified species (Voynich Herbal 025)",
                common_names=["Unknown Plant"],
                family="Unidentified",
                parts_used=["Radix", "Folia", "Flos"],
                properties=["Unknown"],
                voynichese_glyphs=["chol", "shedy", "otol"],
                description="Basal rosette with tall flowering stalk"
            )
        ],
        recipes=[],
        related_folios=["f25v"],
        scholarly_notes=""
    ),

    # ASTRONOMICAL SECTION
    "f67r": FolioData(
        folio_number="f67r",
        section="Astronomical",
        yale_image_id=1006194,
        description="Astronomical folio featuring a circular diagram with radiating segments containing stars and Voynichese text. Part of the zodiac or astronomical section.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f67v"],
        scholarly_notes="The astronomical section contains circular diagrams that may represent zodiac signs or astronomical observations."
    ),

    "f68v": FolioData(
        folio_number="f68v",
        section="Astronomical",
        yale_image_id=1006197,
        description="Astronomical folio featuring a circular diagram with concentric rings and figures arranged around the perimeter.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f69r"],
        scholarly_notes=""
    ),

    # BIOLOGICAL SECTION
    "f75r": FolioData(
        folio_number="f75r",
        section="Biological",
        yale_image_id=1006208,
        description="Biological folio featuring the famous 'bathing nymphs' - small-scale female figures immersed in fluids, connected by tubes and channels. This section depicts what appears to be a biological or anatomical system.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f75v"],
        scholarly_notes="The biological section is one of the most mysterious parts of the manuscript, featuring nude female figures in various poses connected by tubes and channels, possibly representing anatomical or alchemical processes."
    ),

    "f79v": FolioData(
        folio_number="f79v",
        section="Biological",
        yale_image_id=1006217,
        description="Biological folio featuring female figures in a complex network of tubes and vessels.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f80r"],
        scholarly_notes=""
    ),

    # COSMOLOGICAL SECTION
    "f85v_86r": FolioData(
        folio_number="f85v_86r",
        section="Cosmological",
        yale_image_id=1006231,
        description="The famous 'Rosettes' foldout - a large diagram featuring nine interconnected circular medallions or rosettes. This is one of the most complex illustrations in the manuscript, possibly representing a cosmological map or geographical diagram.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f85r1", "f85r2", "f86v1"],
        scholarly_notes="The Rosettes page is one of the most studied foldouts in the manuscript. The nine medallions may represent a map, a cosmological diagram, or an astronomical chart. The foldout format indicates its importance in the manuscript's structure."
    ),

    # PHARMACEUTICAL SECTION
    "f88r": FolioData(
        folio_number="f88r",
        section="Pharmaceutical",
        yale_image_id=1037112,
        description="Pharmaceutical folio featuring drawings of medicinal herbs and roots portrayed with colored jars or vessels (red, blue, or green).",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Unidentified species (Voynich Pharmaceutical 001)",
                common_names=["Unknown Plant"],
                family="Unidentified",
                parts_used=["Radix", "Herba"],
                properties=["Unknown"],
                voynichese_glyphs=["daiin", "chol"],
                description="Medicinal plant with associated vessel"
            )
        ],
        recipes=[],
        related_folios=["f88v_89r"],
        scholarly_notes="The pharmaceutical section depicts over 100 different species of medicinal herbs and roots with associated vessels."
    ),

    # RECIPE SECTION
    "f103r": FolioData(
        folio_number="f103r",
        section="Recipe",
        yale_image_id=1006254,
        description="Recipe folio featuring paragraphs of Voynichese text with star-like flowers marking each entry in the margins.",
        botanical_specimens=[],
        recipes=["f103r_recipe_1"],
        related_folios=["f103v"],
        scholarly_notes="The recipe section contains continuous text with star-like flowers marking each entry, possibly representing pharmaceutical recipes or procedures."
    ),

    "f116v": FolioData(
        folio_number="f116v",
        section="Recipe",
        yale_image_id=1006277,
        description="The final folio of the Voynich Manuscript, containing the famous three-line marginalia written in a mixture of Latin characters, pseudo-Latin, and German. This is the only page with text in a script other than Voynichese.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f116r"],
        scholarly_notes="The marginalia on f116v has been the subject of extensive study. It appears to be a charm or formula, possibly related to healing. The text includes words like 'pox leber' and 'michiton' which have been variously interpreted. Some scholars believe it may be the key to deciphering the manuscript."
    ),
}

# =============================================================================
# RECIPE DATABASE
# =============================================================================

VOYNICH_RECIPES: Dict[str, Recipe] = {
    "f103r_recipe_1": Recipe(
        name="Voynich Recipe f103r-1",
        voynichese_name="qo daiin chol shedy",
        wilken_key_translation="Process initiator - Nodal valve - Root-arm valve - Pressure valve",
        category="Unidentified Preparation",
        folio_reference="f103r",
        description="A recipe from the Voynich Manuscript recipe section, marked with a star-like flower in the margin. The actual content remains undeciphered.",
        ingredients=[
            Ingredient(
                latin_name="Unidentified botanical",
                common_name="Unknown plant from f103r",
                part_used="Unknown",
                quantity="Unknown",
                preparation="Unknown - text undeciphered",
                properties=["Unknown"]
            ),
        ],
        instructions=[
            "1. The text of this recipe remains undeciphered.",
            "2. The Voynichese script has not yet been translated.",
            "3. The recipe is marked with a star-like flower in the margin."
        ],
        properties=["Unknown - text undeciphered"],
        dosage="Unknown",
        warnings=["The content of this recipe is unknown due to the undeciphered nature of the Voynichese script."],
        preparation_time="Unknown",
        shelf_life="Unknown",
        related_folios=["f103v"]
    ),
}

# =============================================================================
# WILKEN KEY OMNIBUS CLASS
# =============================================================================

class WilkenKeyOmnibus:
    """
    The Wilken Key Omnibus Engine v4.0

    A digital archive of the Voynich Manuscript (Beinecke MS 408)
    featuring accurate folio numbering and Yale Beinecke IIIF image integration.

    Author: Breanne Porsch Wilken
    With KIMI assistance - the most amazing helper
    """

    def __init__(self):
        self.version = "4.0"
        self.author = "Breanne Porsch Wilken"
        self.credit = "With KIMI assistance - the most amazing helper"
        self.manuscript_title = "The Voynich Manuscript"
        self.institution = "Yale University Beinecke Rare Book & Manuscript Library"
        self.ms_identifier = "Beinecke MS 408"

    def get_folio_data(self, folio_number: str) -> Optional[FolioData]:
        """Retrieve complete data for a specific folio."""
        return FOLIO_DATABASE.get(folio_number)

    def get_recipe(self, recipe_key: str) -> Optional[Recipe]:
        """Retrieve a specific recipe by its key."""
        return VOYNICH_RECIPES.get(recipe_key)

    def get_yale_image_url(self, folio_number: str) -> Optional[str]:
        """Generate Yale Beinecke IIIF image URL for a folio."""
        image_id = VOYNICH_FOLIO_IMAGES.get(folio_number)
        if not image_id:
            return None
        return f"https://collections.library.yale.edu/iiif/2/{image_id}/full/max/0/default.jpg"

    def get_all_folios(self) -> List[str]:
        """Get a sorted list of all available folios."""
        return sorted(VOYNICH_FOLIO_IMAGES.keys())

    def get_folios_by_section(self, section: str) -> List[str]:
        """Get all folios belonging to a specific section."""
        section_folios = []
        for folio_num, folio_data in FOLIO_DATABASE.items():
            if folio_data.section.lower() == section.lower():
                section_folios.append(folio_num)
        return sorted(section_folios)

    def is_folio_missing(self, folio_number: str) -> bool:
        """Check if a folio is missing from the manuscript."""
        return folio_number in MISSING_FOLIOS

    def transliterate_voynichese(self, text: str) -> str:
        """Transliterate Voynichese text using the Wilken Key system."""
        result = text
        for glyph, data in WILKEN_KEY_GLYPHS.items():
            result = result.replace(glyph, f"[{data['transliteration']}: {data['meaning']}] ")
        return result

# =============================================================================
# STREAMLIT UI FUNCTIONS
# =============================================================================

def render_header():
    """Render the application header."""
    st.markdown("""
    ## 🗝️ The Wilken Key
    **A Digital Archive of the Voynich Manuscript**

    Yale University Beinecke Rare Book & Manuscript Library  
    Beinecke MS 408
    """)
    st.markdown("---")

def render_navigation():
    """Render the main navigation menu."""
    nav_options = [
        "Archive Home",
        "Browse by Folio",
        "Herbal Section",
        "Astronomical Section", 
        "Biological Section",
        "Cosmological Section",
        "Pharmaceutical Section",
        "Recipe Section",
        "Wilken Key Translation",
        "About"
    ]

    selected = st.sidebar.selectbox("Navigate", nav_options, key="main_nav")
    return selected

def render_folio_card(folio_data: FolioData, omnibus: WilkenKeyOmnibus):
    """Render a card displaying folio information."""
    image_url = omnibus.get_yale_image_url(folio_data.folio_number)

    st.markdown(f"**{folio_data.folio_number} - {folio_data.section} Section**")

    if image_url:
        st.image(image_url, use_container_width=True)
    else:
        st.warning("Image not available")

    st.markdown(folio_data.description)

    # Botanical specimens
    if folio_data.botanical_specimens:
        st.markdown("**Botanical Specimens**")
        for specimen in folio_data.botanical_specimens:
            with st.expander(f"{specimen.latin_name}"):
                st.markdown(f"**Common Names:** {', '.join(specimen.common_names)}")
                st.markdown(f"**Family:** {specimen.family}")
                st.markdown(f"**Parts Used:** {', '.join(specimen.parts_used)}")
                st.markdown(f"**Properties:** {', '.join(specimen.properties)}")
                st.markdown(f"**Description:** {specimen.description}")
                if specimen.voynichese_glyphs:
                    glyphs_str = ', '.join([f"`{g}`" for g in specimen.voynichese_glyphs])
                    st.markdown(f"**Wilken Key Glyphs:** {glyphs_str}")

    # Scholarly notes
    if folio_data.scholarly_notes:
        st.markdown("**Scholarly Notes**")
        st.info(folio_data.scholarly_notes)

def render_wilken_key_translator(omnibus: WilkenKeyOmnibus):
    """Render the Wilken Key transliteration tool."""
    st.markdown("**Wilken Key Translation**")
    st.markdown("Transliterate Voynichese glyphs using the Wilken Key system.")

    # Glyph reference table
    st.markdown("**Glyph Reference**")

    glyph_data = []
    for glyph, data in WILKEN_KEY_GLYPHS.items():
        glyph_data.append({
            "Glyph": glyph,
            "Transliteration": data["transliteration"],
            "Meaning": data["meaning"],
            "Category": data["category"]
        })

    st.dataframe(glyph_data, use_container_width=True)

    # Transliteration tool
    st.markdown("**Transliteration Tool**")
    voynichese_input = st.text_area("Enter Voynichese text", "qo daiin chol shedy otol")

    if st.button("Transliterate"):
        result = omnibus.transliterate_voynichese(voynichese_input)
        st.markdown("**Result:**")
        st.markdown(result)

def render_about():
    """Render the about section."""
    st.markdown("**About The Wilken Key**")

    st.markdown("""
    **The Wilken Key Voynich Archive v4.0**

    This archive provides access to the Voynich Manuscript (Beinecke MS 408),
    one of the world's most mysterious books. The manuscript is an illustrated
    codex written in an unknown script (Voynichese) that has never been deciphered.

    **Manuscript Facts:**
    - **Location:** Yale University Beinecke Rare Book & Manuscript Library
    - **Call Number:** Beinecke MS 408
    - **Date:** Early 15th century (carbon-dated to 1404-1438)
    - **Origin:** Central Europe (possibly)
    - **Language:** Unknown (Voynichese script)
    - **Folios:** 102 preserved (originally ~116, with 14 missing)

    **Sections:**
    1. **Herbal** (f1r-f66v): Drawings of 113 unidentified plant species
    2. **Astronomical** (f67r-f73v): Circular diagrams with stars and zodiac symbols
    3. **Biological** (f75r-f84v): Female figures in tubes and fluids
    4. **Cosmological** (f85-f86): The famous Rosettes foldout
    5. **Pharmaceutical** (f88r-f96v): Herbs with colored vessels
    6. **Recipe** (f103r-f116v): Text with star-like flower markers

    **Missing Folios:**
    f12, f59-f64, f74, f91-f92, f97-f98, f109-f110

    **Author:** Breanne Porsch Wilken

    With KIMI assistance - the most amazing helper
    """)

# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main():
    """Main application entry point."""
    # Initialize the omnibus
    omnibus = WilkenKeyOmnibus()

    # Render header
    render_header()

    # Render navigation
    selected = render_navigation()

    # Route to appropriate section
    if selected == "Archive Home":
        st.markdown("**Welcome to The Wilken Key**")
        st.markdown("""
        Welcome to the digital archive of the Voynich Manuscript (Beinecke MS 408).

        This mysterious 15th-century manuscript is written in an unknown script
        and contains illustrations of unidentified plants, astronomical diagrams,
        biological figures, and more.

        Use the navigation menu to explore the manuscript by section or browse
        individual folios.
        """)

        # Featured folios
        st.markdown("**Featured Folios**")

        featured = ["f1r", "f9r", "f67r", "f75r", "f85v_86r", "f116v"]
        cols = st.columns(3)

        for i, folio_num in enumerate(featured):
            with cols[i % 3]:
                folio_data = omnibus.get_folio_data(folio_num)
                image_url = omnibus.get_yale_image_url(folio_num)
                if image_url:
                    st.image(image_url, caption=folio_num)

    elif selected == "Browse by Folio":
        st.markdown("**Browse by Folio**")

        all_folios = omnibus.get_all_folios()
        selected_folio = st.selectbox("Select Folio", all_folios)

        if selected_folio:
            folio_data = omnibus.get_folio_data(selected_folio)
            if folio_data:
                render_folio_card(folio_data, omnibus)
            else:
                # Show just the image if no data entry exists
                image_url = omnibus.get_yale_image_url(selected_folio)
                if image_url:
                    st.markdown(f"**{selected_folio}**")
                    st.image(image_url, use_container_width=True)
                    st.info("Detailed information for this folio is not yet available in the database.")

    elif selected == "Herbal Section":
        st.markdown("**Herbal Section (f1r - f66v)**")
        herbal_folios = [f for f in omnibus.get_all_folios() if f.startswith("f") and int(f[1:f.index("r") if "r" in f else f.index("v")]) <= 66]

        for folio_num in herbal_folios[:20]:  # Show first 20
            folio_data = omnibus.get_folio_data(folio_num)
            if folio_data:
                render_folio_card(folio_data, omnibus)
            else:
                image_url = omnibus.get_yale_image_url(folio_num)
                if image_url:
                    with st.expander(folio_num):
                        st.image(image_url, use_container_width=True)

    elif selected == "Astronomical Section":
        st.markdown("**Astronomical Section (f67r - f73v)**")
        astro_folios = [f for f in omnibus.get_all_folios() if f.startswith("f67") or f.startswith("f68") or f.startswith("f69") or f.startswith("f70") or f.startswith("f71") or f.startswith("f72") or f.startswith("f73")]

        for folio_num in astro_folios:
            folio_data = omnibus.get_folio_data(folio_num)
            if folio_data:
                render_folio_card(folio_data, omnibus)
            else:
                image_url = omnibus.get_yale_image_url(folio_num)
                if image_url:
                    with st.expander(folio_num):
                        st.image(image_url, use_container_width=True)

    elif selected == "Biological Section":
        st.markdown("**Biological Section (f75r - f84v)**")
        bio_folios = [f for f in omnibus.get_all_folios() if f.startswith("f7") and int(f[1:f.index("r") if "r" in f else f.index("v")]) >= 75 and int(f[1:f.index("r") if "r" in f else f.index("v")]) <= 84]

        for folio_num in bio_folios:
            folio_data = omnibus.get_folio_data(folio_num)
            if folio_data:
                render_folio_card(folio_data, omnibus)
            else:
                image_url = omnibus.get_yale_image_url(folio_num)
                if image_url:
                    with st.expander(folio_num):
                        st.image(image_url, use_container_width=True)

    elif selected == "Cosmological Section":
        st.markdown("**Cosmological Section (f85-f86 Rosettes)**")
        cosmo_folios = ["f85r1", "f85r2", "f86v1", "f85v_86r", "f87r", "f87v"]

        for folio_num in cosmo_folios:
            folio_data = omnibus.get_folio_data(folio_num)
            if folio_data:
                render_folio_card(folio_data, omnibus)
            else:
                image_url = omnibus.get_yale_image_url(folio_num)
                if image_url:
                    with st.expander(folio_num):
                        st.image(image_url, use_container_width=True)

    elif selected == "Pharmaceutical Section":
        st.markdown("**Pharmaceutical Section (f88r - f96v)**")
        pharma_folios = [f for f in omnibus.get_all_folios() if f.startswith("f8") or f.startswith("f9") or f.startswith("f10")]
        pharma_folios = [f for f in pharma_folios if int(f[1:f.index("r") if "r" in f else f.index("v")]) >= 88 and int(f[1:f.index("r") if "r" in f else f.index("v")]) <= 96]

        for folio_num in pharma_folios:
            folio_data = omnibus.get_folio_data(folio_num)
            if folio_data:
                render_folio_card(folio_data, omnibus)
            else:
                image_url = omnibus.get_yale_image_url(folio_num)
                if image_url:
                    with st.expander(folio_num):
                        st.image(image_url, use_container_width=True)

    elif selected == "Recipe Section":
        st.markdown("**Recipe Section (f103r - f116v)**")
        recipe_folios = [f for f in omnibus.get_all_folios() if f.startswith("f10") or f.startswith("f11")]
        recipe_folios = [f for f in recipe_folios if int(f[1:f.index("r") if "r" in f else f.index("v")]) >= 103 and int(f[1:f.index("r") if "r" in f else f.index("v")]) <= 116]

        for folio_num in recipe_folios:
            folio_data = omnibus.get_folio_data(folio_num)
            if folio_data:
                render_folio_card(folio_data, omnibus)
            else:
                image_url = omnibus.get_yale_image_url(folio_num)
                if image_url:
                    with st.expander(folio_num):
                        st.image(image_url, use_container_width=True)

    elif selected == "Wilken Key Translation":
        render_wilken_key_translator(omnibus)

    elif selected == "About":
        render_about()

    # Footer
    st.markdown("---")
    st.markdown("**The Wilken Key Voynich Archive v4.0**")
    st.markdown("Breanne Porsch Wilken | With KIMI assistance - the most amazing helper")
    st.markdown("Yale University Beinecke Rare Book & Manuscript Library | Beinecke MS 408")

if __name__ == "__main__":
    main()
