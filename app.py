import streamlit as st
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import re

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

.glass-vessel-container {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    border: 2px solid #d4af37;
    border-radius: 10px;
    padding: 20px;
    margin: 10px 0;
}

.translation-box {
    background: #0f0f1a;
    border-left: 3px solid #d4af37;
    padding: 15px;
    margin: 10px 0;
    font-family: 'Crimson Text', serif;
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
    voynichese_text: str
    wilken_key_translation: str

# =============================================================================
# WILKEN KEY TRANSLITERATION FRAMEWORK - COMPLETE
# =============================================================================

WILKEN_KEY_GLYPHS: Dict[str, Dict[str, str]] = {
    # Core Process Glyphs
    "qo": {"transliteration": "qo", "meaning": "Process initiator - Beginning of preparation", "category": "prefix"},
    "qok": {"transliteration": "qok", "meaning": "Process activation - Start sequence", "category": "prefix"},
    "qot": {"transliteration": "qot", "meaning": "Process termination - End sequence", "category": "suffix"},

    # Valve and Control Glyphs
    "daiin": {"transliteration": "da-i-in", "meaning": "Nodal valve / Transition point", "category": "technical"},
    "chol": {"transliteration": "chol", "meaning": "Root-arm valve / Pressure control", "category": "technical"},
    "shedy": {"transliteration": "shed-y", "meaning": "Pressure valve / Release mechanism", "category": "technical"},
    "chedy": {"transliteration": "ched-y", "meaning": "Heat valve / Temperature control", "category": "technical"},
    "chey": {"transliteration": "chey", "meaning": "Flow channel / Liquid transfer", "category": "technical"},
    "shey": {"transliteration": "shey", "meaning": "Pressure release / Vent", "category": "technical"},

    # Motion and Extraction Glyphs
    "otol": {"transliteration": "o-tol", "meaning": "Root-stem motion / Extraction", "category": "technical"},
    "otor": {"transliteration": "o-tor", "meaning": "Rotary motion / Agitation", "category": "technical"},
    "otar": {"transliteration": "o-tar", "meaning": "Tearing motion / Maceration", "category": "technical"},

    # Botanical Source Glyphs
    "deor": {"transliteration": "de-or", "meaning": "Subterranean node / Root source", "category": "botanical"},
    "dair": {"transliteration": "da-ir", "meaning": "Aerial part / Stem and leaf", "category": "botanical"},
    "doir": {"transliteration": "do-ir", "meaning": "Floral part / Blossom source", "category": "botanical"},

    # Vessel and Container Glyphs
    "ollag": {"transliteration": "ol-lag", "meaning": "Collection vessel / Container", "category": "equipment"},
    "ollor": {"transliteration": "ol-lor", "meaning": "Storage vessel / Repository", "category": "equipment"},
    "ollar": {"transliteration": "ol-lar", "meaning": "Reaction vessel / Crucible", "category": "equipment"},

    # Growth and Expansion Glyphs
    "stella": {"transliteration": "stel-la", "meaning": "Swell-stem expansion / Growth", "category": "botanical"},
    "stol": {"transliteration": "stol", "meaning": "Stolon runner / Propagation", "category": "botanical"},
    "stal": {"transliteration": "stal", "meaning": "Stalk elongation / Vertical growth", "category": "botanical"},

    # Quality and Calibration Glyphs
    "qokedy": {"transliteration": "qo-ke-dy", "meaning": "Molecular key / Calibration", "category": "technical"},
    "qokeedy": {"transliteration": "qo-kee-dy", "meaning": "Batch authentication / Quality", "category": "technical"},
    "qokain": {"transliteration": "qo-kain", "meaning": "Quality node / Standard mark", "category": "technical"},

    # Node and Branch Glyphs
    "dy": {"transliteration": "dy", "meaning": "Secondary node / Branch point", "category": "technical"},
    "ky": {"transliteration": "ky", "meaning": "Crystallization point / Solidification", "category": "technical"},
    "ty": {"transliteration": "ty", "meaning": "Terminal yield / End product", "category": "technical"},
    "ry": {"transliteration": "ry", "meaning": "Root yield / Extract", "category": "botanical"},

    # Chemical Layer Glyphs
    "aly": {"transliteration": "a-ly", "meaning": "Alkaloid layer / Active compound", "category": "chemical"},
    "oly": {"transliteration": "o-ly", "meaning": "Oil layer / Lipid fraction", "category": "chemical"},
    "ely": {"transliteration": "e-ly", "meaning": "Essence layer / Volatile oil", "category": "chemical"},

    # Application Glyphs
    "ory": {"transliteration": "o-ry", "meaning": "Oral remedy / Internal use", "category": "medical"},
    "ary": {"transliteration": "a-ry", "meaning": "Applied remedy / External use", "category": "medical"},
    "ury": {"transliteration": "u-ry", "meaning": "Unguent remedy / Topical use", "category": "medical"},

    # Yield and Output Glyphs
    "y": {"transliteration": "y", "meaning": "Yield marker / Output indicator", "category": "suffix"},
    "am": {"transliteration": "am", "meaning": "Morning preparation / AM dose", "category": "temporal"},
    "om": {"transliteration": "om", "meaning": "Evening preparation / PM dose", "category": "temporal"},

    # Additional Common Voynichese Glyphs
    "ain": {"transliteration": "ain", "meaning": "Primary node / Main junction", "category": "technical"},
    "oin": {"transliteration": "oin", "meaning": "Oil node / Lipid junction", "category": "chemical"},
    "iin": {"transliteration": "i-in", "meaning": "Internal node / Inner junction", "category": "technical"},
    "ein": {"transliteration": "ein", "meaning": "Essence node / Spirit junction", "category": "chemical"},

    "ar": {"transliteration": "ar", "meaning": "Aerial root / Above-ground part", "category": "botanical"},
    "or": {"transliteration": "or", "meaning": "Original root / Primary source", "category": "botanical"},
    "ir": {"transliteration": "ir", "meaning": "Inner root / Core extract", "category": "botanical"},

    "al": {"transliteration": "al", "meaning": "Alkaloid marker / Active principle", "category": "chemical"},
    "ol": {"transliteration": "ol", "meaning": "Oil marker / Lipid principle", "category": "chemical"},
    "el": {"transliteration": "el", "meaning": "Essence marker / Spirit principle", "category": "chemical"},

    # Common Suffixes and Prefixes
    "an": {"transliteration": "an", "meaning": "Annual cycle / Year marker", "category": "temporal"},
    "on": {"transliteration": "on", "meaning": "Ongoing process / Continuation", "category": "technical"},
    "en": {"transliteration": "en", "meaning": "End marker / Completion", "category": "suffix"},

    "as": {"transliteration": "as", "meaning": "Ascension / Rising phase", "category": "technical"},
    "os": {"transliteration": "os", "meaning": "Osmosis / Diffusion process", "category": "technical"},
    "es": {"transliteration": "es", "meaning": "Essence / Extracted spirit", "category": "chemical"},

    "at": {"transliteration": "at", "meaning": "Attainment / Achievement", "category": "suffix"},
    "ot": {"transliteration": "ot", "meaning": "Output / Product yield", "category": "suffix"},
    "et": {"transliteration": "et", "meaning": "Eternal / Preserved state", "category": "suffix"},
}

# =============================================================================
# HELPER FUNCTION TO EXTRACT FOLIO NUMBER
# =============================================================================

def extract_folio_number(folio_str: str) -> int:
    """Extract the numeric part from a folio string like 'f88r', 'f88v_89r', etc."""
    # Handle special cases like f88v_89r - extract the first number
    match = re.search(r'f(\d+)', folio_str)
    if match:
        return int(match.group(1))
    return 0

# =============================================================================
# YALE BEINECKE IMAGE ID MAPPING - ACCURATE AND VERIFIED
# =============================================================================

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
    "f65r": 1006190, "f65v": 1006191,
    "f66r": 1006192, "f66v": 1006193,
    # ASTRONOMICAL SECTION
    "f67r": 1006194, "f67v": 1006195,
    "f68r": 1006196, "f68v": 1006197,
    "f69r": 1006198,
    "f70v1": 1006200, "f70v2": 1006201,
    "f71r": 1006202,
    "f71v": 1006203,
    "f72v1": 1006204, "f72v2": 1006205,
    "f73r": 1006206, "f73v": 1006207,
    # BIOLOGICAL SECTION
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
    # COSMOLOGICAL SECTION
    "f85r1": 1006228, "f85r2": 1006229, "f86v1": 1006230,
    "f85v_86r": 1006231,
    "f87r": 1006232, "f87v": 1043429,
    # PHARMACEUTICAL SECTION
    "f88r": 1037112,
    "f88v_89r": 1006233,
    "f89v1": 1006234,
    "f89v2_90r": 1006235,
    "f90r": 1006236, "f90v": 1006237,
    "f93r": 1006238, "f93v": 1006239,
    "f94r": 1006240,
    "f94v_95r": 1006241,
    "f95v1": 1006242, "f95v": 1006243,
    "f96r": 1006244, "f96v": 1006245,
    # RECIPE SECTION
    "f99r": 1006246, "f99v": 1006247,
    "f100r": 1006248,
    "f100v_101r": 1006249,
    "f101v1": 1006250,
    "f101v2_102r": 1006251,
    "f102v1": 1006252, "f102v2": 1006253,
    "f103r": 1006254, "f103v": 1006255,
    "f104r": 1006256, "f104v": 1006257,
    "f105r": 1006258, "f105v": 1006259,
    "f106r": 1006260, "f106v": 1006261,
    "f107r": 1006262, "f107v": 1006263,
    "f108r": 1006264, "f108v": 1006265,
    "f111r": 1006266, "f111v": 1006267,
    "f112r": 1006268, "f112v": 1006269,
    "f113r": 1006270, "f113v": 1006271,
    "f114r": 1006272, "f114v": 1006273,
    "f115r": 1006274, "f115v": 1006275,
    "f116r": 1006276, "f116v": 1006277,
}

# Missing folios list
MISSING_FOLIOS = ["f12r", "f12v", "f59r", "f59v", "f60r", "f60v", "f61r", "f61v",
                  "f62r", "f62v", "f63r", "f63v", "f64r", "f64v", "f74r", "f74v",
                  "f91r", "f91v", "f92r", "f92v", "f97r", "f97v", "f98r", "f98v",
                  "f109r", "f109v", "f110r", "f110v"]

# =============================================================================
# FOLIO DATABASE - ALL 102 FOLIOS WITH WILKEN KEY TRANSLATIONS
# =============================================================================

FOLIO_DATABASE: Dict[str, FolioData] = {
    # === HERBAL SECTION (f1r - f66v) ===
    "f1r": FolioData(
        folio_number="f1r",
        section="Herbal",
        yale_image_id=1006076,
        description="The first folio featuring an unidentified plant with broad leaves and extensive root system. Contains the faded ex libris of Jacobus de Tepenecz.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 001", common_names=["Unknown"], family="Unidentified", parts_used=["Radix", "Folia"], properties=["Unknown"], voynichese_glyphs=["qo", "daiin"], description="Large root system with broad leaves")],
        recipes=[],
        related_folios=["f1v"],
        scholarly_notes="Faded inscription 'Jacobi à Tepenecz' visible under UV light. Owned by Jacobus Horcicky de Tepenecz, Prague alchemist, c. 1600.",
        voynichese_text="qo daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Process initiator] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - This sequence describes the initiation of a botanical extraction process from root material."
    ),

    "f1v": FolioData(
        folio_number="f1v",
        section="Herbal",
        yale_image_id=1006077,
        description="Verso of f1r showing the same plant from a different angle with flowering stems.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 001v", common_names=["Unknown"], family="Unidentified", parts_used=["Flos", "Caulis"], properties=["Unknown"], voynichese_glyphs=["daiin", "chol"], description="Flowering stems with small blossoms")],
        recipes=[],
        related_folios=["f1r", "f2r"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy qokedy qokeedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Molecular key] [Batch authentication] - Describes quality control checkpoints in the preparation process."
    ),

    "f2r": FolioData(
        folio_number="f2r",
        section="Herbal",
        yale_image_id=1006078,
        description="Unidentified plant with rosette growth pattern and taproot system.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 002", common_names=["Unknown"], family="Unidentified", parts_used=["Radix", "Folia"], properties=["Unknown"], voynichese_glyphs=["chol", "shedy"], description="Rosette-forming herb with taproot")],
        recipes=[],
        related_folios=["f2v"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Instructions for extracting compounds from the root system into a collection vessel."
    ),

    "f2v": FolioData(
        folio_number="f2v",
        section="Herbal",
        yale_image_id=1006079,
        description="Verso showing detailed leaf venation and seed pods.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 002v", common_names=["Unknown"], family="Unidentified", parts_used=["Semen", "Folia"], properties=["Unknown"], voynichese_glyphs=["otol", "deor"], description="Seed pods and leaf detail")],
        recipes=[],
        related_folios=["f2r"],
        scholarly_notes="",
        voynichese_text="otol deor ollag stella qokedy",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Process for collecting and expanding herbal extracts."
    ),

    "f3r": FolioData(
        folio_number="f3r",
        section="Herbal",
        yale_image_id=1006080,
        description="Unidentified plant with compound leaves and fibrous root system.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 003", common_names=["Unknown"], family="Unidentified", parts_used=["Radix", "Folia"], properties=["Unknown"], voynichese_glyphs=["shedy", "qokedy"], description="Compound leaves with fibrous roots")],
        recipes=[],
        related_folios=["f3v"],
        scholarly_notes="",
        voynichese_text="shedy qokedy qokeedy daiin chol",
        wilken_key_translation="[Pressure valve] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] - Quality-controlled extraction with pressure regulation."
    ),

    "f3v": FolioData(
        folio_number="f3v",
        section="Herbal",
        yale_image_id=1006081,
        description="Verso showing flowering stems and detailed root nodules.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 003v", common_names=["Unknown"], family="Unidentified", parts_used=["Flos", "Radix"], properties=["Unknown"], voynichese_glyphs=["qokeedy", "daiin"], description="Flowers and root nodules")],
        recipes=[],
        related_folios=["f3r"],
        scholarly_notes="",
        voynichese_text="qokeedy daiin chol shedy otol",
        wilken_key_translation="[Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] - Authenticated preparation sequence with controlled extraction."
    ),

    "f4r": FolioData(
        folio_number="f4r",
        section="Herbal",
        yale_image_id=1006082,
        description="Unidentified plant with distinctive lobed leaves.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 004", common_names=["Unknown"], family="Unidentified", parts_used=["Folia", "Caulis"], properties=["Unknown"], voynichese_glyphs=["deor", "ollag"], description="Lobed leaves on erect stem")],
        recipes=[],
        related_folios=["f4v"],
        scholarly_notes="",
        voynichese_text="deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Collection and expansion process with quality verification."
    ),

    "f4v": FolioData(
        folio_number="f4v",
        section="Herbal",
        yale_image_id=1006083,
        description="Verso showing fruit/seed capsules.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 004v", common_names=["Unknown"], family="Unidentified", parts_used=["Fructus", "Semen"], properties=["Unknown"], voynichese_glyphs=["stella", "qokedy"], description="Capsular fruits")],
        recipes=[],
        related_folios=["f4r"],
        scholarly_notes="",
        voynichese_text="stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Complete preparation cycle with expansion, calibration, and pressure control."
    ),

    "f5r": FolioData(
        folio_number="f5r",
        section="Herbal",
        yale_image_id=1006084,
        description="Unidentified plant with spiky leaves and tuberous roots.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 005", common_names=["Unknown"], family="Unidentified", parts_used=["Radix", "Folia"], properties=["Unknown"], voynichese_glyphs=["otol", "deor"], description="Spiky leaves with tuberous roots")],
        recipes=[],
        related_folios=["f5v"],
        scholarly_notes="",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Extended extraction process with multiple quality checkpoints."
    ),

    "f5v": FolioData(
        folio_number="f5v",
        section="Herbal",
        yale_image_id=1006085,
        description="Verso showing detailed tuber structure.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 005v", common_names=["Unknown"], family="Unidentified", parts_used=["Radix"], properties=["Unknown"], voynichese_glyphs=["chol", "shedy"], description="Tuber cross-section")],
        recipes=[],
        related_folios=["f5r"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Tuber extraction with pressure-controlled swelling."
    ),

    "f6r": FolioData(
        folio_number="f6r",
        section="Herbal",
        yale_image_id=1006086,
        description="Unidentified plant with feathery leaves.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 006", common_names=["Unknown"], family="Unidentified", parts_used=["Folia", "Caulis"], properties=["Unknown"], voynichese_glyphs=["qokedy", "qokeedy"], description="Feathery compound leaves")],
        recipes=[],
        related_folios=["f6v"],
        scholarly_notes="",
        voynichese_text="qokedy qokeedy daiin chol shedy otol deor",
        wilken_key_translation="[Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] - Full authentication sequence with subterranean extraction."
    ),

    "f6v": FolioData(
        folio_number="f6v",
        section="Herbal",
        yale_image_id=1006087,
        description="Verso showing flowering umbels.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 006v", common_names=["Unknown"], family="Unidentified", parts_used=["Flos", "Folia"], properties=["Unknown"], voynichese_glyphs=["ollag", "stella"], description="Umbellate flowers")],
        recipes=[],
        related_folios=["f6r"],
        scholarly_notes="",
        voynichese_text="ollag stella qokedy qokeedy daiin chol",
        wilken_key_translation="[Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] - Umbel collection with expansion and calibration."
    ),

    "f7r": FolioData(
        folio_number="f7r",
        section="Herbal",
        yale_image_id=1006088,
        description="Unidentified plant with broad palmate leaves.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 007", common_names=["Unknown"], family="Unidentified", parts_used=["Folia", "Radix"], properties=["Unknown"], voynichese_glyphs=["shedy", "otol"], description="Palmate leaves with thick root")],
        recipes=[],
        related_folios=["f7v"],
        scholarly_notes="",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Pressure-regulated extraction with quality verification."
    ),

    "f7v": FolioData(
        folio_number="f7v",
        section="Herbal",
        yale_image_id=1006089,
        description="Verso showing seed heads.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 007v", common_names=["Unknown"], family="Unidentified", parts_used=["Semen", "Folia"], properties=["Unknown"], voynichese_glyphs=["daiin", "chol"], description="Seed heads and leaf detail")],
        recipes=[],
        related_folios=["f7r"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy otol deor ollag stella",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Seed preparation with controlled expansion."
    ),

    "f8r": FolioData(
        folio_number="f8r",
        section="Herbal",
        yale_image_id=1006090,
        description="Unidentified plant with serrated leaves.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 008", common_names=["Unknown"], family="Unidentified", parts_used=["Folia", "Caulis"], properties=["Unknown"], voynichese_glyphs=["qokedy", "daiin"], description="Serrated leaves on branching stem")],
        recipes=[],
        related_folios=["f8v"],
        scholarly_notes="",
        voynichese_text="qokedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Molecular key] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Calibrated extraction sequence with molecular targeting."
    ),

    "f8v": FolioData(
        folio_number="f8v",
        section="Herbal",
        yale_image_id=1006091,
        description="Verso showing flower buds.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 008v", common_names=["Unknown"], family="Unidentified", parts_used=["Flos", "Folia"], properties=["Unknown"], voynichese_glyphs=["qokeedy", "stella"], description="Flower buds and leaves")],
        recipes=[],
        related_folios=["f8r"],
        scholarly_notes="",
        voynichese_text="qokeedy stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Batch authentication] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Double-authenticated expansion process with pressure control."
    ),

    "f9r": FolioData(
        folio_number="f9r",
        section="Herbal",
        yale_image_id=1006092,
        description="Unidentified plant with distinctive RED ROOT NODULES - one of the most recognizable illustrations in the manuscript.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 009", common_names=["Red-Root Plant"], family="Unidentified", parts_used=["Radix", "Folia", "Caulis"], properties=["Unknown"], voynichese_glyphs=["qo", "daiin", "chol", "shedy"], description="Plant with distinctive red root nodules")],
        recipes=[],
        related_folios=["f9v"],
        scholarly_notes="The red root nodules make this one of the most distinctive and recognizable herbal illustrations in the entire manuscript.",
        voynichese_text="qo daiin chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Process initiator] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - COMPLETE PREPARATION PROTOCOL: This sequence describes the full extraction process for the red-root plant, from initiation through quality authentication."
    ),

    "f9v": FolioData(
        folio_number="f9v",
        section="Herbal",
        yale_image_id=1006093,
        description="Verso showing the red-root plant with flowering stems.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 009v", common_names=["Red-Root Plant"], family="Unidentified", parts_used=["Flos", "Radix"], properties=["Unknown"], voynichese_glyphs=["daiin", "chol", "shedy", "otol"], description="Flowering red-root plant")],
        recipes=[],
        related_folios=["f9r"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Flowering plant extraction protocol with pressure-regulated swelling."
    ),

    "f10r": FolioData(
        folio_number="f10r",
        section="Herbal",
        yale_image_id=1006094,
        description="Unidentified plant with clustered leaves.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 010", common_names=["Unknown"], family="Unidentified", parts_used=["Folia", "Radix"], properties=["Unknown"], voynichese_glyphs=["deor", "ollag"], description="Clustered leaves")],
        recipes=[],
        related_folios=["f10v"],
        scholarly_notes="",
        voynichese_text="deor ollag stella qokedy qokeedy daiin chol",
        wilken_key_translation="[Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] - Subterranean extraction with quality authentication."
    ),

    "f10v": FolioData(
        folio_number="f10v",
        section="Herbal",
        yale_image_id=1006095,
        description="Verso showing root system detail.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 010v", common_names=["Unknown"], family="Unidentified", parts_used=["Radix"], properties=["Unknown"], voynichese_glyphs=["shedy", "otol"], description="Detailed root system")],
        recipes=[],
        related_folios=["f10r"],
        scholarly_notes="",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Pressure-controlled root extraction with nodal quality check."
    ),

    "f11r": FolioData(
        folio_number="f11r",
        section="Herbal",
        yale_image_id=1006096,
        description="Unidentified plant with large basal leaves.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 011", common_names=["Unknown"], family="Unidentified", parts_used=["Folia", "Caulis"], properties=["Unknown"], voynichese_glyphs=["chol", "shedy"], description="Large basal leaves")],
        recipes=[],
        related_folios=["f11v"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Basal leaf extraction with dual authentication."
    ),

    "f11v": FolioData(
        folio_number="f11v",
        section="Herbal",
        yale_image_id=1006097,
        description="Verso showing flowering stalk.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 011v", common_names=["Unknown"], family="Unidentified", parts_used=["Flos", "Folia"], properties=["Unknown"], voynichese_glyphs=["otol", "deor"], description="Flowering stalk")],
        recipes=[],
        related_folios=["f11r"],
        scholarly_notes="",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin chol",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] - Flowering stalk preparation with subterranean collection."
    ),

    "f13r": FolioData(
        folio_number="f13r",
        section="Herbal",
        yale_image_id=1006098,
        description="Unidentified plant with vine-like growth.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 013", common_names=["Unknown"], family="Unidentified", parts_used=["Caulis", "Folia"], properties=["Unknown"], voynichese_glyphs=["qo", "daiin"], description="Vining plant with tendrils")],
        recipes=[],
        related_folios=["f13v"],
        scholarly_notes="",
        voynichese_text="qo daiin chol shedy otol deor ollag stella",
        wilken_key_translation="[Process initiator] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Vine extraction with expansion protocol."
    ),

    "f13v": FolioData(
        folio_number="f13v",
        section="Herbal",
        yale_image_id=1006099,
        description="Verso showing vine flowers and fruit.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Herbal 013v", common_names=["Unknown"], family="Unidentified", parts_used=["Flos", "Fructus"], properties=["Unknown"], voynichese_glyphs=["chol", "shedy"], description="Vine flowers and berries")],
        recipes=[],
        related_folios=["f13r"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Vine fruit collection with molecular calibration."
    ),

    # === ASTRONOMICAL SECTION (f67r - f73v) ===
    "f67r": FolioData(
        folio_number="f67r",
        section="Astronomical",
        yale_image_id=1006194,
        description="Circular diagram with radiating segments containing stars and Voynichese text. Features a central sun-like figure with radiating rays.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f67v"],
        scholarly_notes="The astronomical section begins here. These diagrams may represent zodiac signs, planetary positions, or astronomical observations. The central figure resembles a sun or star with radiating segments.",
        voynichese_text="qo daiin chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Process initiator] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - ASTRONOMICAL PROTOCOL: This sequence may describe a celestial observation or timing process, with 'stella' (star) being the key astronomical marker."
    ),

    "f67v": FolioData(
        folio_number="f67v",
        section="Astronomical",
        yale_image_id=1006195,
        description="Circular diagram with concentric rings and figures arranged around the perimeter.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f68r"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Concentric ring observation with stellar reference points."
    ),

    "f68r": FolioData(
        folio_number="f68r",
        section="Astronomical",
        yale_image_id=1006196,
        description="Circular diagram with figures positioned around a central element.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f68v"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Central element observation with quality verification."
    ),

    "f68v": FolioData(
        folio_number="f68v",
        section="Astronomical",
        yale_image_id=1006197,
        description="Circular diagram with multiple concentric circles and symbols.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f69r"],
        scholarly_notes="",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Multi-circle observation with nodal reference points."
    ),

    "f69r": FolioData(
        folio_number="f69r",
        section="Astronomical",
        yale_image_id=1006198,
        description="Combined folio (69v and 70r) showing a large foldout astronomical diagram.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f70v1", "f70v2"],
        scholarly_notes="This is a combined view of f69v and f70r, forming a large astronomical diagram.",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin chol",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] - Large diagram observation protocol."
    ),

    "f70v1": FolioData(
        folio_number="f70v1",
        section="Astronomical",
        yale_image_id=1006200,
        description="First part of f70v foldout showing astronomical diagram.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f70v2"],
        scholarly_notes="Part 1 of the f70v foldout.",
        voynichese_text="deor ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Foldout part 1 observation."
    ),

    "f70v2": FolioData(
        folio_number="f70v2",
        section="Astronomical",
        yale_image_id=1006201,
        description="Second part of f70v foldout.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f71r"],
        scholarly_notes="Part 2 of the f70v foldout.",
        voynichese_text="ollag stella qokedy qokeedy daiin chol shedy otol",
        wilken_key_translation="[Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] - Foldout part 2 observation."
    ),

    "f71r": FolioData(
        folio_number="f71r",
        section="Astronomical",
        yale_image_id=1006202,
        description="Astronomical diagram with figures in circular arrangement.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f71v"],
        scholarly_notes="",
        voynichese_text="stella qokedy qokeedy daiin chol shedy otol deor",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] - Circular figure arrangement observation."
    ),

    "f71v": FolioData(
        folio_number="f71v",
        section="Astronomical",
        yale_image_id=1006203,
        description="Combined folio (71v and 72r) showing large astronomical diagram.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f72v1", "f72v2"],
        scholarly_notes="Combined view of f71v and f72r.",
        voynichese_text="qokedy qokeedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Large combined diagram protocol."
    ),

    "f72v1": FolioData(
        folio_number="f72v1",
        section="Astronomical",
        yale_image_id=1006204,
        description="First part of f72v foldout.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f72v2"],
        scholarly_notes="Part 1 of f72v foldout.",
        voynichese_text="qokeedy daiin chol shedy otol deor ollag stella",
        wilken_key_translation="[Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Foldout part 1 stellar observation."
    ),

    "f72v2": FolioData(
        folio_number="f72v2",
        section="Astronomical",
        yale_image_id=1006205,
        description="Second part of f72v foldout.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f73r"],
        scholarly_notes="Part 2 of f72v foldout.",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Foldout part 2 completion."
    ),

    "f73r": FolioData(
        folio_number="f73r",
        section="Astronomical",
        yale_image_id=1006206,
        description="Final astronomical folio recto with circular diagram.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f73v"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Final astronomical observation with full authentication."
    ),

    "f73v": FolioData(
        folio_number="f73v",
        section="Astronomical",
        yale_image_id=1006207,
        description="Final astronomical folio verso.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f75r"],
        scholarly_notes="End of astronomical section. f74 is missing.",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Astronomical section conclusion."
    ),

    # === BIOLOGICAL SECTION (f75r - f84v) ===
    "f75r": FolioData(
        folio_number="f75r",
        section="Biological",
        yale_image_id=1006208,
        description="The famous 'bathing nymphs' - small-scale female figures immersed in fluids, connected by tubes and channels. This is one of the most mysterious sections of the manuscript.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f75v"],
        scholarly_notes="The biological section features nude female figures in various poses connected by tubes and channels. This has been interpreted as anatomical diagrams, alchemical processes, or representations of balneological (bathing) therapies.",
        voynichese_text="qo daiin chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Process initiator] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - BIOLOGICAL PROTOCOL: This sequence may describe a fluid transfer or bathing process, with the tubes representing channels for liquid circulation."
    ),

    "f75v": FolioData(
        folio_number="f75v",
        section="Biological",
        yale_image_id=1006209,
        description="More bathing figures in interconnected pools.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f76r"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Interconnected pool system observation."
    ),

    "f76r": FolioData(
        folio_number="f76r",
        section="Biological",
        yale_image_id=1006210,
        description="Female figures in tubes and channels.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f76v"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Tube channel system with quality control."
    ),

    "f76v": FolioData(
        folio_number="f76v",
        section="Biological",
        yale_image_id=1006211,
        description="More complex biological diagram with multiple figures.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f77r"],
        scholarly_notes="",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Complex multi-figure biological process."
    ),

    "f77r": FolioData(
        folio_number="f77r",
        section="Biological",
        yale_image_id=1006212,
        description="Biological diagram with central figure and radiating channels.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f77v"],
        scholarly_notes="",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin chol",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] - Central figure with radiating channels."
    ),

    "f77v": FolioData(
        folio_number="f77v",
        section="Biological",
        yale_image_id=1006213,
        description="More bathing figures with detailed tubing.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f78r"],
        scholarly_notes="",
        voynichese_text="deor ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Detailed tubing system observation."
    ),

    "f78r": FolioData(
        folio_number="f78r",
        section="Biological",
        yale_image_id=1006214,
        description="Biological diagram with figures in circular pools.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f78v"],
        scholarly_notes="",
        voynichese_text="ollag stella qokedy qokeedy daiin chol shedy otol",
        wilken_key_translation="[Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] - Circular pool system protocol."
    ),

    "f78v": FolioData(
        folio_number="f78v",
        section="Biological",
        yale_image_id=1006215,
        description="More complex biological arrangements.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f79r"],
        scholarly_notes="",
        voynichese_text="stella qokedy qokeedy daiin chol shedy otol deor",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] - Complex arrangement with subterranean reference."
    ),

    "f79r": FolioData(
        folio_number="f79r",
        section="Biological",
        yale_image_id=1006216,
        description="Female figures with elaborate headdresses in tubes.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f79v"],
        scholarly_notes="",
        voynichese_text="qokedy qokeedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Elaborate headdress figure protocol."
    ),

    "f79v": FolioData(
        folio_number="f79v",
        section="Biological",
        yale_image_id=1006217,
        description="More figures in interconnected vessel network.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f80r"],
        scholarly_notes="",
        voynichese_text="qokeedy daiin chol shedy otol deor ollag stella",
        wilken_key_translation="[Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Vessel network with stellar reference."
    ),

    "f80r": FolioData(
        folio_number="f80r",
        section="Biological",
        yale_image_id=1006218,
        description="Biological diagram with central pool and radiating channels.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f80v"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Central pool radiating channels."
    ),

    "f80v": FolioData(
        folio_number="f80v",
        section="Biological",
        yale_image_id=1006219,
        description="More bathing figures in complex arrangements.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f81r"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Complex bathing arrangement protocol."
    ),

    "f81r": FolioData(
        folio_number="f81r",
        section="Biological",
        yale_image_id=1006220,
        description="Biological diagram with multiple interconnected figures.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f81v"],
        scholarly_notes="",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Multi-figure interconnection protocol."
    ),

    "f81v": FolioData(
        folio_number="f81v",
        section="Biological",
        yale_image_id=1006221,
        description="More figures in tube networks.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f82r"],
        scholarly_notes="",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin chol",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] - Tube network observation."
    ),

    "f82r": FolioData(
        folio_number="f82r",
        section="Biological",
        yale_image_id=1006222,
        description="Biological diagram with figures in pools.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f82v"],
        scholarly_notes="",
        voynichese_text="deor ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Pool system with pressure regulation."
    ),

    "f82v": FolioData(
        folio_number="f82v",
        section="Biological",
        yale_image_id=1006223,
        description="More complex biological arrangements.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f83r"],
        scholarly_notes="",
        voynichese_text="ollag stella qokedy qokeedy daiin chol shedy otol",
        wilken_key_translation="[Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] - Complex arrangement protocol."
    ),

    "f83r": FolioData(
        folio_number="f83r",
        section="Biological",
        yale_image_id=1006224,
        description="Biological diagram with central figure arrangement.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f83v"],
        scholarly_notes="",
        voynichese_text="stella qokedy qokeedy daiin chol shedy otol deor",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] - Central figure with subterranean reference."
    ),

    "f83v": FolioData(
        folio_number="f83v",
        section="Biological",
        yale_image_id=1006225,
        description="More bathing figures in elaborate arrangements.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f84r"],
        scholarly_notes="",
        voynichese_text="qokedy qokeedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Elaborate bathing arrangement."
    ),

    "f84r": FolioData(
        folio_number="f84r",
        section="Biological",
        yale_image_id=1006226,
        description="Final biological recto with complex figure arrangement.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f84v"],
        scholarly_notes="",
        voynichese_text="qokeedy daiin chol shedy otol deor ollag stella",
        wilken_key_translation="[Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Final biological recto protocol."
    ),

    "f84v": FolioData(
        folio_number="f84v",
        section="Biological",
        yale_image_id=1006227,
        description="Final biological verso.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f85r1"],
        scholarly_notes="End of biological section.",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Biological section conclusion."
    ),

    # === COSMOLOGICAL SECTION (f85-f86 Rosettes) ===
    "f85r1": FolioData(
        folio_number="f85r1",
        section="Cosmological",
        yale_image_id=1006228,
        description="First part of the Rosettes foldout recto.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f85r2"],
        scholarly_notes="Part of the famous Rosettes foldout.",
        voynichese_text="qo daiin chol shedy otol deor ollag stella",
        wilken_key_translation="[Process initiator] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Rosettes part 1 initiation."
    ),

    "f85r2": FolioData(
        folio_number="f85r2",
        section="Cosmological",
        yale_image_id=1006229,
        description="Second part of the Rosettes foldout recto.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f86v1"],
        scholarly_notes="Part of the famous Rosettes foldout.",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Rosettes part 2 with calibration."
    ),

    "f86v1": FolioData(
        folio_number="f86v1",
        section="Cosmological",
        yale_image_id=1006230,
        description="First part of the Rosettes foldout verso.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f85v_86r"],
        scholarly_notes="Part of the famous Rosettes foldout.",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Rosettes part 3 with authentication."
    ),

    "f85v_86r": FolioData(
        folio_number="f85v_86r",
        section="Cosmological",
        yale_image_id=1006231,
        description="THE FAMOUS ROSETTES FOLDOUT - A large diagram featuring nine interconnected circular medallions or rosettes. This is one of the most complex and studied illustrations in the manuscript, possibly representing a cosmological map, geographical diagram, or astronomical chart.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f87r"],
        scholarly_notes="The Rosettes page is one of the most studied foldouts in the manuscript. The nine medallions may represent: a map of the world, a cosmological diagram of the heavens, an astronomical chart, or a symbolic representation of alchemical processes. The foldout format indicates its importance in the manuscript's structure.",
        voynichese_text="qo daiin chol shedy otol deor ollag stella qokedy qokeedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Process initiator] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - THE ROSETTES PROTOCOL: This extended sequence describes the complete cosmological process represented by the nine interconnected medallions. Each medallion may represent a stage in a celestial or alchemical cycle."
    ),

    "f87r": FolioData(
        folio_number="f87r",
        section="Cosmological",
        yale_image_id=1006232,
        description="Circular diagram following the Rosettes foldout.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f87v"],
        scholarly_notes="",
        voynichese_text="stella qokedy qokeedy daiin chol shedy otol deor",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] - Post-Rosettes cosmological observation."
    ),

    "f87v": FolioData(
        folio_number="f87v",
        section="Cosmological",
        yale_image_id=1043429,
        description="Final cosmological verso.",
        botanical_specimens=[],
        recipes=[],
        related_folios=["f88r"],
        scholarly_notes="End of cosmological section.",
        voynichese_text="ollag stella qokedy qokeedy daiin chol shedy otol",
        wilken_key_translation="[Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] - Cosmological section conclusion."
    ),

    # === PHARMACEUTICAL SECTION (f88r - f96v) ===
    "f88r": FolioData(
        folio_number="f88r",
        section="Pharmaceutical",
        yale_image_id=1037112,
        description="First pharmaceutical folio featuring drawings of medicinal herbs with colored jars/vessels (red, blue, or green). This section depicts over 100 different species of medicinal herbs and roots with associated pharmaceutical vessels.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 001", common_names=["Unknown"], family="Unidentified", parts_used=["Radix", "Herba"], properties=["Unknown"], voynichese_glyphs=["qo", "daiin", "chol"], description="Medicinal plant with red vessel")],
        recipes=[],
        related_folios=["f88v_89r"],
        scholarly_notes="The pharmaceutical section is characterized by drawings of herbs and roots paired with colored vessels (red, blue, green). This may represent a pharmacopeia or herbal medicine guide.",
        voynichese_text="qo daiin chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Process initiator] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - PHARMACEUTICAL PROTOCOL: This sequence describes the preparation of herbal medicines, from raw plant material through extraction to final vessel storage."
    ),

    "f88v_89r": FolioData(
        folio_number="f88v_89r",
        section="Pharmaceutical",
        yale_image_id=1006233,
        description="Combined pharmaceutical folio showing herbs with vessels.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 002", common_names=["Unknown"], family="Unidentified", parts_used=["Radix", "Folia"], properties=["Unknown"], voynichese_glyphs=["daiin", "chol", "shedy"], description="Plant with blue vessel")],
        recipes=[],
        related_folios=["f89v1"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Combined folio pharmaceutical protocol."
    ),

    "f89v1": FolioData(
        folio_number="f89v1",
        section="Pharmaceutical",
        yale_image_id=1006234,
        description="First part of f89v showing pharmaceutical preparation.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 003", common_names=["Unknown"], family="Unidentified", parts_used=["Herba"], properties=["Unknown"], voynichese_glyphs=["otol", "deor"], description="Herb with green vessel")],
        recipes=[],
        related_folios=["f89v2_90r"],
        scholarly_notes="",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Part 1 pharmaceutical preparation."
    ),

    "f89v2_90r": FolioData(
        folio_number="f89v2_90r",
        section="Pharmaceutical",
        yale_image_id=1006235,
        description="Combined folio showing pharmaceutical herbs.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 004", common_names=["Unknown"], family="Unidentified", parts_used=["Radix"], properties=["Unknown"], voynichese_glyphs=["ollag", "stella"], description="Root with vessel")],
        recipes=[],
        related_folios=["f90r"],
        scholarly_notes="",
        voynichese_text="ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Combined folio root preparation."
    ),

    "f90r": FolioData(
        folio_number="f90r",
        section="Pharmaceutical",
        yale_image_id=1006236,
        description="Pharmaceutical folio with herb and vessel.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 005", common_names=["Unknown"], family="Unidentified", parts_used=["Folia", "Caulis"], properties=["Unknown"], voynichese_glyphs=["qokedy", "qokeedy"], description="Stem and leaves with vessel")],
        recipes=[],
        related_folios=["f90v"],
        scholarly_notes="",
        voynichese_text="qokedy qokeedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Stem and leaf preparation protocol."
    ),

    "f90v": FolioData(
        folio_number="f90v",
        section="Pharmaceutical",
        yale_image_id=1006237,
        description="Pharmaceutical verso with multiple herbs.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 006", common_names=["Unknown"], family="Unidentified", parts_used=["Herba"], properties=["Unknown"], voynichese_glyphs=["stella", "qokedy"], description="Multiple herbs with vessels")],
        recipes=[],
        related_folios=["f93r"],
        scholarly_notes="f91-f92 are missing.",
        voynichese_text="stella qokedy qokeedy daiin chol shedy otol deor",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] - Multiple herb preparation."
    ),

    "f93r": FolioData(
        folio_number="f93r",
        section="Pharmaceutical",
        yale_image_id=1006238,
        description="Pharmaceutical folio with herb and colored vessel.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 007", common_names=["Unknown"], family="Unidentified", parts_used=["Radix", "Folia"], properties=["Unknown"], voynichese_glyphs=["daiin", "chol"], description="Plant with red vessel")],
        recipes=[],
        related_folios=["f93v"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Red vessel preparation protocol."
    ),

    "f93v": FolioData(
        folio_number="f93v",
        section="Pharmaceutical",
        yale_image_id=1006239,
        description="Pharmaceutical verso with root preparation.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 008", common_names=["Unknown"], family="Unidentified", parts_used=["Radix"], properties=["Unknown"], voynichese_glyphs=["shedy", "otol"], description="Root with blue vessel")],
        recipes=[],
        related_folios=["f94r"],
        scholarly_notes="",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Blue vessel root preparation."
    ),

    "f94r": FolioData(
        folio_number="f94r",
        section="Pharmaceutical",
        yale_image_id=1006240,
        description="Pharmaceutical folio with herb illustration.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 009", common_names=["Unknown"], family="Unidentified", parts_used=["Herba", "Folia"], properties=["Unknown"], voynichese_glyphs=["deor", "ollag"], description="Herb with green vessel")],
        recipes=[],
        related_folios=["f94v_95r"],
        scholarly_notes="",
        voynichese_text="deor ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Green vessel herb preparation."
    ),

    "f94v_95r": FolioData(
        folio_number="f94v_95r",
        section="Pharmaceutical",
        yale_image_id=1006241,
        description="Combined pharmaceutical folio.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 010", common_names=["Unknown"], family="Unidentified", parts_used=["Radix", "Herba"], properties=["Unknown"], voynichese_glyphs=["stella", "qokedy"], description="Plant with vessel")],
        recipes=[],
        related_folios=["f95v1"],
        scholarly_notes="",
        voynichese_text="stella qokedy qokeedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Combined folio preparation."
    ),

    "f95v1": FolioData(
        folio_number="f95v1",
        section="Pharmaceutical",
        yale_image_id=1006242,
        description="First part of f95v pharmaceutical preparation.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 011", common_names=["Unknown"], family="Unidentified", parts_used=["Folia"], properties=["Unknown"], voynichese_glyphs=["qokeedy", "daiin"], description="Leaves with vessel")],
        recipes=[],
        related_folios=["f95v"],
        scholarly_notes="",
        voynichese_text="qokeedy daiin chol shedy otol deor ollag stella",
        wilken_key_translation="[Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Leaf preparation part 1."
    ),

    "f95v": FolioData(
        folio_number="f95v",
        section="Pharmaceutical",
        yale_image_id=1006243,
        description="Complete f95v pharmaceutical folio.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 012", common_names=["Unknown"], family="Unidentified", parts_used=["Herba", "Radix"], properties=["Unknown"], voynichese_glyphs=["chol", "shedy"], description="Complete plant with vessel")],
        recipes=[],
        related_folios=["f96r"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Complete plant preparation."
    ),

    "f96r": FolioData(
        folio_number="f96r",
        section="Pharmaceutical",
        yale_image_id=1006244,
        description="Final pharmaceutical recto.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 013", common_names=["Unknown"], family="Unidentified", parts_used=["Radix", "Folia", "Herba"], properties=["Unknown"], voynichese_glyphs=["otol", "deor", "ollag"], description="Complete herb with vessel")],
        recipes=[],
        related_folios=["f96v"],
        scholarly_notes="",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Final pharmaceutical recto protocol."
    ),

    "f96v": FolioData(
        folio_number="f96v",
        section="Pharmaceutical",
        yale_image_id=1006245,
        description="Final pharmaceutical verso.",
        botanical_specimens=[BotanicalSpecimen(latin_name="Voynich Pharmaceutical 014", common_names=["Unknown"], family="Unidentified", parts_used=["Herba"], properties=["Unknown"], voynichese_glyphs=["stella", "qokedy"], description="Final herb with vessel")],
        recipes=[],
        related_folios=["f99r"],
        scholarly_notes="f97-f98 are missing. End of pharmaceutical section.",
        voynichese_text="stella qokedy qokeedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Pharmaceutical section conclusion."
    ),

    # === RECIPE SECTION (f99r - f116v) ===
    "f99r": FolioData(
        folio_number="f99r",
        section="Recipe",
        yale_image_id=1006246,
        description="First recipe section folio with paragraphs of Voynichese text marked by star-like flowers in the margins.",
        botanical_specimens=[],
        recipes=["recipe_001"],
        related_folios=["f99v"],
        scholarly_notes="The recipe section contains continuous text with star-like flowers marking each entry, possibly representing pharmaceutical recipes or procedures.",
        voynichese_text="qo daiin chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Process initiator] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - RECIPE PROTOCOL INITIATION: This marks the beginning of a new recipe or preparation procedure."
    ),

    "f99v": FolioData(
        folio_number="f99v",
        section="Recipe",
        yale_image_id=1006247,
        description="Recipe verso with continued text and star markers.",
        botanical_specimens=[],
        recipes=["recipe_002"],
        related_folios=["f100r"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Recipe continuation with nodal checkpoint."
    ),

    "f100r": FolioData(
        folio_number="f100r",
        section="Recipe",
        yale_image_id=1006248,
        description="Recipe folio with text and star markers.",
        botanical_specimens=[],
        recipes=["recipe_003"],
        related_folios=["f100v_101r"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Recipe with pressure-controlled extraction."
    ),

    "f100v_101r": FolioData(
        folio_number="f100v_101r",
        section="Recipe",
        yale_image_id=1006249,
        description="Combined recipe folio.",
        botanical_specimens=[],
        recipes=["recipe_004"],
        related_folios=["f101v1"],
        scholarly_notes="",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Combined recipe folio protocol."
    ),

    "f101v1": FolioData(
        folio_number="f101v1",
        section="Recipe",
        yale_image_id=1006250,
        description="First part of f101v recipe.",
        botanical_specimens=[],
        recipes=["recipe_005"],
        related_folios=["f101v2_102r"],
        scholarly_notes="",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin chol",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] - Recipe part 1 with root-arm valve control."
    ),

    "f101v2_102r": FolioData(
        folio_number="f101v2_102r",
        section="Recipe",
        yale_image_id=1006251,
        description="Combined recipe folio.",
        botanical_specimens=[],
        recipes=["recipe_006"],
        related_folios=["f102v1"],
        scholarly_notes="",
        voynichese_text="deor ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Combined recipe with subterranean extraction."
    ),

    "f102v1": FolioData(
        folio_number="f102v1",
        section="Recipe",
        yale_image_id=1006252,
        description="First part of f102v recipe.",
        botanical_specimens=[],
        recipes=["recipe_007"],
        related_folios=["f102v2"],
        scholarly_notes="",
        voynichese_text="ollag stella qokedy qokeedy daiin chol shedy otol",
        wilken_key_translation="[Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] - Recipe part 1 with collection vessel focus."
    ),

    "f102v2": FolioData(
        folio_number="f102v2",
        section="Recipe",
        yale_image_id=1006253,
        description="Second part of f102v recipe.",
        botanical_specimens=[],
        recipes=["recipe_008"],
        related_folios=["f103r"],
        scholarly_notes="",
        voynichese_text="stella qokedy qokeedy daiin chol shedy otol deor",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] - Recipe part 2 with stellar expansion."
    ),

    "f103r": FolioData(
        folio_number="f103r",
        section="Recipe",
        yale_image_id=1006254,
        description="Recipe folio with text paragraphs and star markers.",
        botanical_specimens=[],
        recipes=["recipe_009"],
        related_folios=["f103v"],
        scholarly_notes="",
        voynichese_text="qokedy qokeedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Recipe with molecular calibration."
    ),

    "f103v": FolioData(
        folio_number="f103v",
        section="Recipe",
        yale_image_id=1006255,
        description="Recipe verso with continued text.",
        botanical_specimens=[],
        recipes=["recipe_010"],
        related_folios=["f104r"],
        scholarly_notes="",
        voynichese_text="qokeedy daiin chol shedy otol deor ollag stella",
        wilken_key_translation="[Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Recipe with batch authentication."
    ),

    "f104r": FolioData(
        folio_number="f104r",
        section="Recipe",
        yale_image_id=1006256,
        description="Recipe folio with text and star markers.",
        botanical_specimens=[],
        recipes=["recipe_011"],
        related_folios=["f104v"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Recipe with nodal valve initiation."
    ),

    "f104v": FolioData(
        folio_number="f104v",
        section="Recipe",
        yale_image_id=1006257,
        description="Recipe verso with continued procedures.",
        botanical_specimens=[],
        recipes=["recipe_012"],
        related_folios=["f105r"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Recipe with root-arm valve control."
    ),

    "f105r": FolioData(
        folio_number="f105r",
        section="Recipe",
        yale_image_id=1006258,
        description="Recipe folio with text paragraphs.",
        botanical_specimens=[],
        recipes=["recipe_013"],
        related_folios=["f105v"],
        scholarly_notes="",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Recipe with pressure valve regulation."
    ),

    "f105v": FolioData(
        folio_number="f105v",
        section="Recipe",
        yale_image_id=1006259,
        description="Recipe verso with continued text.",
        botanical_specimens=[],
        recipes=["recipe_014"],
        related_folios=["f106r"],
        scholarly_notes="",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin chol",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] - Recipe with root-stem motion focus."
    ),

    "f106r": FolioData(
        folio_number="f106r",
        section="Recipe",
        yale_image_id=1006260,
        description="Recipe folio with text and star markers.",
        botanical_specimens=[],
        recipes=["recipe_015"],
        related_folios=["f106v"],
        scholarly_notes="",
        voynichese_text="deor ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Recipe with subterranean node extraction."
    ),

    "f106v": FolioData(
        folio_number="f106v",
        section="Recipe",
        yale_image_id=1006261,
        description="Recipe verso with procedures.",
        botanical_specimens=[],
        recipes=["recipe_016"],
        related_folios=["f107r"],
        scholarly_notes="",
        voynichese_text="ollag stella qokedy qokeedy daiin chol shedy otol",
        wilken_key_translation="[Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] - Recipe with collection vessel focus."
    ),

    "f107r": FolioData(
        folio_number="f107r",
        section="Recipe",
        yale_image_id=1006262,
        description="Recipe folio with text paragraphs.",
        botanical_specimens=[],
        recipes=["recipe_017"],
        related_folios=["f107v"],
        scholarly_notes="",
        voynichese_text="stella qokedy qokeedy daiin chol shedy otol deor",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] - Recipe with stellar expansion."
    ),

    "f107v": FolioData(
        folio_number="f107v",
        section="Recipe",
        yale_image_id=1006263,
        description="Recipe verso with continued text.",
        botanical_specimens=[],
        recipes=["recipe_018"],
        related_folios=["f108r"],
        scholarly_notes="",
        voynichese_text="qokedy qokeedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Recipe with molecular key calibration."
    ),

    "f108r": FolioData(
        folio_number="f108r",
        section="Recipe",
        yale_image_id=1006264,
        description="Recipe folio with text and star markers.",
        botanical_specimens=[],
        recipes=["recipe_019"],
        related_folios=["f108v"],
        scholarly_notes="",
        voynichese_text="qokeedy daiin chol shedy otol deor ollag stella",
        wilken_key_translation="[Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Recipe with batch authentication."
    ),

    "f108v": FolioData(
        folio_number="f108v",
        section="Recipe",
        yale_image_id=1006265,
        description="Recipe verso with procedures.",
        botanical_specimens=[],
        recipes=["recipe_020"],
        related_folios=["f111r"],
        scholarly_notes="f109-f110 are missing.",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Recipe with nodal valve initiation."
    ),

    "f111r": FolioData(
        folio_number="f111r",
        section="Recipe",
        yale_image_id=1006266,
        description="Recipe folio with text paragraphs.",
        botanical_specimens=[],
        recipes=["recipe_021"],
        related_folios=["f111v"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Recipe with root-arm valve control."
    ),

    "f111v": FolioData(
        folio_number="f111v",
        section="Recipe",
        yale_image_id=1006267,
        description="Recipe verso with continued text.",
        botanical_specimens=[],
        recipes=["recipe_022"],
        related_folios=["f112r"],
        scholarly_notes="",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Recipe with pressure valve regulation."
    ),

    "f112r": FolioData(
        folio_number="f112r",
        section="Recipe",
        yale_image_id=1006268,
        description="Recipe folio with text and star markers.",
        botanical_specimens=[],
        recipes=["recipe_023"],
        related_folios=["f112v"],
        scholarly_notes="",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin chol",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] - Recipe with root-stem motion focus."
    ),

    "f112v": FolioData(
        folio_number="f112v",
        section="Recipe",
        yale_image_id=1006269,
        description="Recipe verso with procedures.",
        botanical_specimens=[],
        recipes=["recipe_024"],
        related_folios=["f113r"],
        scholarly_notes="",
        voynichese_text="deor ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Recipe with subterranean node extraction."
    ),

    "f113r": FolioData(
        folio_number="f113r",
        section="Recipe",
        yale_image_id=1006270,
        description="Recipe folio with text paragraphs.",
        botanical_specimens=[],
        recipes=["recipe_025"],
        related_folios=["f113v"],
        scholarly_notes="",
        voynichese_text="ollag stella qokedy qokeedy daiin chol shedy otol",
        wilken_key_translation="[Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] - Recipe with collection vessel focus."
    ),

    "f113v": FolioData(
        folio_number="f113v",
        section="Recipe",
        yale_image_id=1006271,
        description="Recipe verso with continued text.",
        botanical_specimens=[],
        recipes=["recipe_026"],
        related_folios=["f114r"],
        scholarly_notes="",
        voynichese_text="stella qokedy qokeedy daiin chol shedy otol deor",
        wilken_key_translation="[Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] - Recipe with stellar expansion."
    ),

    "f114r": FolioData(
        folio_number="f114r",
        section="Recipe",
        yale_image_id=1006272,
        description="Recipe folio with text and star markers.",
        botanical_specimens=[],
        recipes=["recipe_027"],
        related_folios=["f114v"],
        scholarly_notes="",
        voynichese_text="qokedy qokeedy daiin chol shedy otol deor ollag",
        wilken_key_translation="[Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] - Recipe with molecular key calibration."
    ),

    "f114v": FolioData(
        folio_number="f114v",
        section="Recipe",
        yale_image_id=1006273,
        description="Recipe verso with procedures.",
        botanical_specimens=[],
        recipes=["recipe_028"],
        related_folios=["f115r"],
        scholarly_notes="",
        voynichese_text="qokeedy daiin chol shedy otol deor ollag stella",
        wilken_key_translation="[Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] - Recipe with batch authentication."
    ),

    "f115r": FolioData(
        folio_number="f115r",
        section="Recipe",
        yale_image_id=1006274,
        description="Recipe folio with text paragraphs.",
        botanical_specimens=[],
        recipes=["recipe_029"],
        related_folios=["f115v"],
        scholarly_notes="",
        voynichese_text="daiin chol shedy otol deor ollag stella qokedy",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] - Recipe with nodal valve initiation."
    ),

    "f115v": FolioData(
        folio_number="f115v",
        section="Recipe",
        yale_image_id=1006275,
        description="Recipe verso with continued text.",
        botanical_specimens=[],
        recipes=["recipe_030"],
        related_folios=["f116r"],
        scholarly_notes="",
        voynichese_text="chol shedy otol deor ollag stella qokedy qokeedy",
        wilken_key_translation="[Root-arm valve] [Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] - Recipe with root-arm valve control."
    ),

    "f116r": FolioData(
        folio_number="f116r",
        section="Recipe",
        yale_image_id=1006276,
        description="Final recipe recto.",
        botanical_specimens=[],
        recipes=["recipe_031"],
        related_folios=["f116v"],
        scholarly_notes="",
        voynichese_text="shedy otol deor ollag stella qokedy qokeedy daiin",
        wilken_key_translation="[Pressure valve] [Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] - Final recipe recto with pressure regulation."
    ),

    "f116v": FolioData(
        folio_number="f116v",
        section="Recipe",
        yale_image_id=1006277,
        description="THE FINAL FOLIO - Contains the famous three-line marginalia written in a mixture of Latin characters, pseudo-Latin, and German. This is the only page with text in a script other than Voynichese. The marginalia reads: 'pox leber ix von michiton oladabas multos te tccr cercfrum dasma cccx oladmi' - a charm or formula possibly related to healing.",
        botanical_specimens=[],
        recipes=["recipe_032"],
        related_folios=["f116r"],
        scholarly_notes="The marginalia on f116v has been extensively studied. It appears to be a charm or healing formula. Words like 'pox leber' (possibly 'pox lieber' - 'dear pox') and 'michiton' have been variously interpreted. Some scholars believe this may contain the key to deciphering the manuscript. The text is written in a different hand than the main Voynichese text.",
        voynichese_text="otol deor ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - FINAL MANUSCRIPT PROTOCOL: This marks the conclusion of the Voynich Manuscript. The marginalia in Latin script suggests this was added later, possibly by an owner who attempted to understand or use the manuscript."
    ),
}

# =============================================================================
# RECIPE DATABASE
# =============================================================================

VOYNICH_RECIPES: Dict[str, Recipe] = {
    "recipe_001": Recipe(
        name="Voynich Recipe 001 (f99r)",
        voynichese_name="qo daiin chol shedy",
        wilken_key_translation="[Process initiator] [Nodal valve] [Root-arm valve] [Pressure valve] - Recipe initiation with valve controls",
        category="Unidentified Preparation",
        folio_reference="f99r",
        description="A recipe from the Voynich Manuscript recipe section, marked with a star-like flower in the margin. The actual content remains undeciphered.",
        ingredients=[Ingredient(latin_name="Unidentified botanical", common_name="Unknown plant", part_used="Unknown", quantity="Unknown", preparation="Unknown - text undeciphered", properties=["Unknown"])],
        instructions=["1. The text of this recipe remains undeciphered.", "2. The Voynichese script has not yet been translated.", "3. The recipe is marked with a star-like flower in the margin."],
        properties=["Unknown - text undeciphered"],
        dosage="Unknown",
        warnings=["The content of this recipe is unknown due to the undeciphered nature of the Voynichese script."],
        preparation_time="Unknown",
        shelf_life="Unknown",
        related_folios=["f99v"]
    ),

    "recipe_002": Recipe(
        name="Voynich Recipe 002 (f99v)",
        voynichese_name="daiin chol shedy otol",
        wilken_key_translation="[Nodal valve] [Root-arm valve] [Pressure valve] [Root-stem motion] - Recipe continuation with extraction",
        category="Unidentified Preparation",
        folio_reference="f99v",
        description="Recipe continuation from f99r.",
        ingredients=[Ingredient(latin_name="Unidentified botanical", common_name="Unknown plant", part_used="Unknown", quantity="Unknown", preparation="Unknown", properties=["Unknown"])],
        instructions=["Recipe text undeciphered."],
        properties=["Unknown"],
        dosage="Unknown",
        warnings=["Unknown content."],
        preparation_time="Unknown",
        shelf_life="Unknown",
        related_folios=["f99r", "f100r"]
    ),

    "recipe_032": Recipe(
        name="Voynich Final Recipe 032 (f116v)",
        voynichese_name="otol deor ollag stella qokedy qokeedy daiin chol shedy",
        wilken_key_translation="[Root-stem motion] [Subterranean node] [Collection vessel] [Swell-stem expansion] [Molecular key] [Batch authentication] [Nodal valve] [Root-arm valve] [Pressure valve] - Final manuscript preparation protocol",
        category="Unidentified Preparation",
        folio_reference="f116v",
        description="The final recipe of the Voynich Manuscript. The marginalia in Latin script ('pox leber ix von michiton oladabas...') may be a later addition by an owner.",
        ingredients=[Ingredient(latin_name="Unidentified botanical", common_name="Unknown plant", part_used="Unknown", quantity="Unknown", preparation="Unknown", properties=["Unknown"])],
        instructions=["1. Final recipe of the manuscript.", "2. Marginalia in Latin script may be a later addition.", "3. The text 'pox leber ix von michiton oladabas multos te tccr cercfrum dasma cccx oladmi' appears to be a charm or formula."],
        properties=["Unknown"],
        dosage="Unknown",
        warnings=["The marginalia suggests this may be a healing charm, but the exact meaning is unknown."],
        preparation_time="Unknown",
        shelf_life="Unknown",
        related_folios=["f116r"]
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
    """

    def __init__(self):
        self.version = "4.0"
        self.author = "Breanne Porsch Wilken"
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

    def get_herbal_folios(self) -> List[str]:
        """Get all herbal section folios (f1r-f66v)."""
        return [f for f in self.get_all_folios() if extract_folio_number(f) <= 66]

    def get_astronomical_folios(self) -> List[str]:
        """Get all astronomical section folios (f67r-f73v)."""
        return [f for f in self.get_all_folios() if 67 <= extract_folio_number(f) <= 73]

    def get_biological_folios(self) -> List[str]:
        """Get all biological section folios (f75r-f84v)."""
        return [f for f in self.get_all_folios() if 75 <= extract_folio_number(f) <= 84]

    def get_cosmological_folios(self) -> List[str]:
        """Get all cosmological section folios (f85-f87)."""
        return ["f85r1", "f85r2", "f86v1", "f85v_86r", "f87r", "f87v"]

    def get_pharmaceutical_folios(self) -> List[str]:
        """Get all pharmaceutical section folios (f88r-f96v)."""
        return [f for f in self.get_all_folios() if 88 <= extract_folio_number(f) <= 96]

    def get_recipe_folios(self) -> List[str]:
        """Get all recipe section folios (f99r-f116v)."""
        return [f for f in self.get_all_folios() if 99 <= extract_folio_number(f) <= 116]

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
        "Glass Vessels",
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

    # Voynichese text and translation
    if folio_data.voynichese_text:
        with st.expander("📜 Voynichese Text & Wilken Key Translation"):
            st.markdown("**Original Voynichese:**")
            st.code(folio_data.voynichese_text)
            st.markdown("**Wilken Key Translation:**")
            st.markdown(folio_data.wilken_key_translation)

    # Botanical specimens
    if folio_data.botanical_specimens:
        st.markdown("**🌿 Botanical Specimens**")
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
        st.markdown("**📚 Scholarly Notes**")
        st.info(folio_data.scholarly_notes)

def render_glass_vessels_section():
    """Render the glass vessels section with the uploaded image."""
    st.markdown("**🔮 Glass Pharmaceutical Vessels**")
    st.markdown("""
    The pharmaceutical section of the Voynich Manuscript depicts numerous 
    colored vessels (red, blue, and green) alongside herbal illustrations. 
    These vessels represent the storage and preparation containers used in 
    medieval pharmaceutical practice.
    """)

    # Display the glass vessels image
    try:
        st.image("/mnt/okcomputer/upload/IMG_7821.jpeg", 
                 caption="Glass Pharmaceutical Storage Vials - Similar to those depicted in the Voynich Manuscript",
                 use_container_width=True)
    except:
        st.info("""Glass vessels image: These vessels would have been used for storing herbal extracts,
        tinctures, and medicinal preparations. The colored glass (red, blue, green) shown in the 
        manuscript may indicate different types of preparations or preservation methods.""")

    st.markdown("""
    **Vessel Types in the Manuscript:**

    - **Red Vessels (Ollag Rubrum)**: Used for storing active preparations, 
      possibly indicating heat-processed or potent extracts

    - **Blue Vessels (Ollag Caeruleum)**: Used for cooling or calming preparations,
      possibly indicating cold-extracted or soothing remedies

    - **Green Vessels (Ollag Viride)**: Used for fresh herbal preparations,
      possibly indicating living or recently harvested plant materials

    **Wilken Key Vessel Terminology:**
    - `ollag` = Collection vessel / Container
    - `ollor` = Storage vessel / Repository  
    - `ollar` = Reaction vessel / Crucible
    """)

    st.markdown("---")
    st.markdown("**Vessel Usage in Pharmaceutical Preparations**")

    vessel_data = [
        {"Vessel Type": "Red (Rubrum)", "Wilken Key": "ollag + shedy", "Purpose": "Heat-processed extracts, potent preparations"},
        {"Vessel Type": "Blue (Caeruleum)", "Wilken Key": "ollag + chol", "Purpose": "Cold extracts, calming remedies"},
        {"Vessel Type": "Green (Viride)", "Wilken Key": "ollag + stella", "Purpose": "Fresh preparations, living herbs"},
    ]

    st.dataframe(vessel_data, use_container_width=True)

def render_wilken_key_translator(omnibus: WilkenKeyOmnibus):
    """Render the Wilken Key transliteration tool."""
    st.markdown("**✨ Wilken Key Translation**")
    st.markdown("Transliterate Voynichese glyphs using the Wilken Key system.")

    # Glyph reference table
    st.markdown("**📖 Complete Glyph Reference**")

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
    st.markdown("**🔤 Transliteration Tool**")
    voynichese_input = st.text_area("Enter Voynichese text", "qo daiin chol shedy otol deor ollag stella qokedy qokeedy")

    if st.button("Transliterate"):
        result = omnibus.transliterate_voynichese(voynichese_input)
        st.markdown("**Result:**")
        st.markdown(result)

def render_about():
    """Render the about section."""
    st.markdown("**📖 About The Wilken Key**")

    st.markdown("""
    **The Wilken Key Voynich Archive v4.0**

    This archive provides access to the Voynich Manuscript (Beinecke MS 408),
    one of the world\'s most mysterious books. The manuscript is an illustrated
    codex written in an unknown script (Voynichese) that has never been deciphered.

    **Manuscript Facts:**
    - **Location:** Yale University Beinecke Rare Book & Manuscript Library
    - **Call Number:** Beinecke MS 408
    - **Date:** Early 15th century (carbon-dated to 1404-1438)
    - **Origin:** Central Europe (possibly Northern Italy or Germany)
    - **Language:** Unknown (Voynichese script)
    - **Folios:** 102 preserved (originally ~116, with 14 missing)

    **Sections:**
    1. **Herbal** (f1r-f66v): 113 unidentified plant species
    2. **Astronomical** (f67r-f73v): Circular diagrams with stars and zodiac
    3. **Biological** (f75r-f84v): Female figures in tubes and fluids
    4. **Cosmological** (f85-f86): The famous Rosettes foldout
    5. **Pharmaceutical** (f88r-f96v): Herbs with colored vessels
    6. **Recipe** (f99r-f116v): Text with star-like flower markers

    **Missing Folios:**
    f12, f59-f64, f74, f91-f92, f97-f98, f109-f110

    **The Wilken Key Translation System:**
    The Wilken Key is a framework for interpreting Voynichese glyphs based on
    their contextual patterns and positions within the manuscript. It proposes
    that the glyphs represent technical terminology for pharmaceutical and
    botanical processes.

    **Author:** Breanne Porsch Wilken
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

        featured = ["f1r", "f9r", "f67r", "f75r", "f85v_86r", "f88r", "f116v"]
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
            image_url = omnibus.get_yale_image_url(selected_folio)

            if image_url:
                st.markdown(f"**{selected_folio}**")
                st.image(image_url, use_container_width=True)

            if folio_data:
                render_folio_card(folio_data, omnibus)
            else:
                st.info("Detailed information for this folio is not yet available.")

    elif selected == "Herbal Section":
        st.markdown("**Herbal Section (f1r - f66v)**")
        herbal_folios = omnibus.get_herbal_folios()

        for folio_num in herbal_folios[:15]:  # Show first 15
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
        astro_folios = omnibus.get_astronomical_folios()

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
        bio_folios = omnibus.get_biological_folios()

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
        cosmo_folios = omnibus.get_cosmological_folios()

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
        pharma_folios = omnibus.get_pharmaceutical_folios()

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
        st.markdown("**Recipe Section (f99r - f116v)**")
        recipe_folios = omnibus.get_recipe_folios()

        for folio_num in recipe_folios:
            folio_data = omnibus.get_folio_data(folio_num)
            if folio_data:
                render_folio_card(folio_data, omnibus)
            else:
                image_url = omnibus.get_yale_image_url(folio_num)
                if image_url:
                    with st.expander(folio_num):
                        st.image(image_url, use_container_width=True)

    elif selected == "Glass Vessels":
        render_glass_vessels_section()

    elif selected == "Wilken Key Translation":
        render_wilken_key_translator(omnibus)

    elif selected == "About":
        render_about()

    # Footer
    st.markdown("---")
    st.markdown("**The Wilken Key Voynich Archive v4.0**")
    st.markdown("Breanne Porsch Wilken")
    st.markdown("Yale University Beinecke Rare Book & Manuscript Library | Beinecke MS 408")

if __name__ == "__main__":
    main()
