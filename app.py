import streamlit as st
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from enum import Enum

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="Wilken Key Engine | Million-Word Omnibus v4.0",
    page_icon="🗝️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CUSTOM CSS THEMING - Medieval Manuscript Aesthetics
# =============================================================================
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800;900&family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap');

:root {
    --parchment: #0a0a0f;
    --parchment-light: #14141a;
    --gold: #d4af37;
    --gold-dim: #8b7355;
    --gold-bright: #f4d03f;
    --text-primary: #e8e6e1;
    --text-secondary: #b8b5a8;
    --accent-green: #4a7c59;
    --bg-card: #14141a;
}

.stApp {
    background: linear-gradient(135deg, #0a0a0f 0%, #14141a 50%, #0a0a0f 100%);
}

h1, h2, h3 {
    font-family: 'Cinzel', serif !important;
    color: var(--gold) !important;
}

.stTextInput > div > div > input,
.stSelectbox > div > div > div {
    background: #14141a !important;
    border: 2px solid var(--gold-dim) !important;
    border-radius: 8px !important;
    color: var(--gold) !important;
}

.stTextInput > label,
.stSelectbox > label {
    color: var(--gold) !important;
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
    """Botanical specimen with complete Latin nomenclature."""
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
    phase: str
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
    "ary": {"transliteration": "a-ry", "meaning": "Aromatic yield / Volatile oil", "category": "chemical"},
    "ory": {"transliteration": "o-ry", "meaning": "Oral remedy / Internal use", "category": "medical"},
    "ary": {"transliteration": "a-ry", "meaning": "Applied remedy / External use", "category": "medical"},
    "y": {"transliteration": "y", "meaning": "Yield marker / Output indicator", "category": "suffix"},
    "am": {"transliteration": "am", "meaning": "Morning preparation / AM dose", "category": "temporal"},
    "om": {"transliteration": "om", "meaning": "Evening preparation / PM dose", "category": "temporal"},
}

# =============================================================================
# LATIN BOTANICAL DATABASE
# =============================================================================

LATIN_BOTANICAL_DATABASE: Dict[str, Dict[str, Any]] = {
    # Phase 1: Opening Protocols (f1r-f4v)
    "f1r": {
        "latin_name": "Chelidonium majus L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Greater Celandine", "Swallowwort", "Tetterwort"],
        "family": "Papaveraceae",
        "parts_used": ["Radix (Root)", "Latex (Milky sap)", "Folia (Leaves)"],
        "constituents": ["Chelidonine", "Sanguinarine", "Berberine", "Coptisine"],
        "properties": ["Choleretic", "Antispasmodic", "Analgesic", "Antimicrobial"],
        "description": "The Lobed-Leaf Plant - primary source of milky latex for pharmaceutical preparations"
    },
    "f1v": {
        "latin_name": "Chelidonium majus L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Greater Celandine", "Swallowwort"],
        "family": "Papaveraceae",
        "parts_used": ["Radix (Root)", "Herba (Aerial parts)", "Flos (Flowers)"],
        "constituents": ["Chelidonine", "Allocryptopine", "Sparteine"],
        "properties": ["Choleretic", "Antimicrobial", "Spasmolytic"],
        "description": "Complete plant with flowering stems and root system"
    },
    "f2r": {
        "latin_name": "Bellis perennis L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Common Daisy", "English Daisy", "Woundwort"],
        "family": "Asteraceae",
        "parts_used": ["Herba (Aerial parts)", "Flos (Flowers)", "Folia (Leaves)"],
        "constituents": ["Saponins", "Tannins", "Mucilage", "Flavonoids"],
        "properties": ["Emollient", "Astringent", "Vulnerary", "Anti-inflammatory"],
        "description": "The Day's Eye - opening and closing with the sun"
    },
    "f3r": {
        "latin_name": "Salvia officinalis L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Common Sage", "Garden Sage", "Dalmatian Sage"],
        "family": "Lamiaceae",
        "parts_used": ["Folia (Leaves)", "Cacumen (Stem tips)", "Herba (Aerial parts)"],
        "constituents": ["Thujone", "Cineole", "Camphor", "Rosmarinic acid"],
        "properties": ["Carminative", "Antispasmodic", "Cerebral tonic", "Antimicrobial"],
        "description": "The Saving Plant - from Latin 'salvere' meaning to heal"
    },
    "f4r": {
        "latin_name": "Papaver somniferum L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Opium Poppy", "Sleep-Bearing Poppy", "Breadseed Poppy"],
        "family": "Papaveraceae",
        "parts_used": ["Latex (Raw opium)", "Semen (Seeds)", "Cortex capsulae (Capsule wall)"],
        "constituents": ["Morphine", "Codeine", "Thebaine", "Papaverine", "Noscapine"],
        "properties": ["Narcotic", "Analgesic", "Sedative", "Antitussive", "Hypnotic"],
        "description": "The Sleep-Bringer - latex yields morphine and codeine"
    },
    "f5r": {
        "latin_name": "Mandragora officinarum L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Mandrake", "Love Apple", "Devil's Testicles"],
        "family": "Solanaceae",
        "parts_used": ["Radix (Root)", "Folia (Leaves)", "Fructus (Fruit)"],
        "constituents": ["Hyoscyamine", "Scopolamine", "Mandragorine", "Atropine"],
        "properties": ["Narcotic", "Hallucinogenic", "Analgesic", "Anesthetic"],
        "description": "The Human Root - forked root resembles human form"
    },
    "f9r": {
        "latin_name": "Mandragora officinarum L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Mandrake", "Satan's Apple"],
        "family": "Solanaceae",
        "parts_used": ["Radix (Root)", "Folia (Leaves)", "Fructus (Fruit)"],
        "constituents": ["Hyoscyamine", "Scopolamine", "Atropine"],
        "properties": ["Narcotic", "Anesthetic", "Deliriant"],
        "description": "Flowering mandrake with characteristic purple flowers"
    },
    "f25r": {
        "latin_name": "Paeonia officinalis L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Common Peony", "European Peony"],
        "family": "Paeoniaceae",
        "parts_used": ["Radix (Root)", "Semen (Seeds)", "Flos (Flowers)"],
        "constituents": ["Paeoniflorin", "Tannins", "Triterpenoids"],
        "properties": ["Antispasmodic", "Tonic", "Astringent"],
        "description": "The Healing Peony - seeds traditionally used for nightmares"
    },
    "f67r": {
        "latin_name": "Veratrum album L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["White Hellebore", "False Hellebore", "European Hellebore"],
        "family": "Melanthiaceae",
        "parts_used": ["Rhizoma (Rhizome)", "Radix (Root)", "Herba (Aerial parts)"],
        "constituents": ["Veratridine", "Cevadine", "Protoveratrine", "Jervine"],
        "properties": ["Emetic", "Cathartic", "Hypotensive", "Insecticidal"],
        "description": "The White Hellebore - powerful purge for celestial preparation"
    },
    "f68v": {
        "latin_name": "Atropa belladonna L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Deadly Nightshade", "Belladonna", "Devil's Cherries"],
        "family": "Solanaceae",
        "parts_used": ["Folia (Leaves)", "Radix (Root)", "Semen (Seeds)"],
        "constituents": ["Atropine", "Hyoscyamine", "Scopolamine", "Belladonnine"],
        "properties": ["Anticholinergic", "Mydriatic", "Hallucinogenic", "Toxic"],
        "description": "The Beautiful Lady - dilates pupils, dangerously toxic"
    },
    "f75r": {
        "latin_name": "Arnica montana L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Mountain Arnica", "Leopard's Bane", "Wolf's Bane"],
        "family": "Asteraceae",
        "parts_used": ["Flos (Flowers)", "Rhizoma (Rhizome)", "Herba (Aerial parts)"],
        "constituents": ["Helenalin", "Dihydrohelenalin", "Thymol derivatives", "Flavonoids"],
        "properties": ["Anti-inflammatory", "Analgesic", "Circulatory stimulant", "Antimicrobial"],
        "description": "The Mountain Healer - alpine flower for trauma"
    },
    "f79v": {
        "latin_name": "Symphytum officinale L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Comfrey", "Knitbone", "Boneset"],
        "family": "Boraginaceae",
        "parts_used": ["Radix (Root)", "Folia (Leaves)", "Herba (Aerial parts)"],
        "constituents": ["Allantoin", "Rosmarinic acid", "Tannins", "Mucilage", "Pyrrolizidine alkaloids"],
        "properties": ["Vulnerary", "Anti-inflammatory", "Cell proliferant", "Demulcent"],
        "description": "The Bone Knitter - allantoin promotes cell division"
    },
    "f85r": {
        "latin_name": "Commiphora myrrha (Nees) Engl.",
        "authority": "Nees von Esenbeck, 1897",
        "common_names": ["Myrrh", "Gum Myrrh"],
        "family": "Burseraceae",
        "parts_used": ["Resina (Resin tears)"],
        "constituents": ["Commiphoric acid", "Commiphorinic acid", "Volatile oils", "Resins"],
        "properties": ["Antimicrobial", "Astringent", "Wound healing", "Anti-inflammatory"],
        "description": "The Bitter Resin - ancient wound remedy"
    },
    "f88r": {
        "latin_name": "Cinchona pubescens Vahl",
        "authority": "Vahl, 1790",
        "common_names": ["Quinine Tree", "Fever Tree", "Red Cinchona"],
        "family": "Rubiaceae",
        "parts_used": ["Cortex (Bark)", "Radix (Root)"],
        "constituents": ["Quinine", "Quinidine", "Cinchonine", "Cinchonidine"],
        "properties": ["Antimalarial", "Antipyretic", "Bitter tonic", "Antiarrhythmic"],
        "description": "The Fever Tree - bark yields quinine"
    },
    "f91r": {
        "latin_name": "Digitalis purpurea L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Foxglove", "Dead Men's Bells", "Fairy Fingers"],
        "family": "Plantaginaceae",
        "parts_used": ["Folia (Leaves)", "Herba (Aerial parts)"],
        "constituents": ["Digoxin", "Digitoxin", "Gitoxin", "Digitonin"],
        "properties": ["Cardiotonic", "Antiarrhythmic", "Diuretic", "Cardiac glycoside"],
        "description": "The Fairy Glove - cardiac glycoside source, narrow therapeutic window"
    },
    "f103r": {
        "latin_name": "Vitex agnus-castus L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Chaste Tree", "Monk's Pepper", "Abraham's Balm"],
        "family": "Lamiaceae",
        "parts_used": ["Fructus (Berries)"],
        "constituents": ["Agnuside", "Casticin", "Vitexin", "Essential oils"],
        "properties": ["Hormonal regulator", "Prolactin inhibitor", "Menstrual regulator"],
        "description": "The Chaste Berry - hormonal regulator for women's health"
    },
    "f106v": {
        "latin_name": "Gentiana lutea L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Great Yellow Gentian", "Bitter Root", "Yellow Gentian"],
        "family": "Gentianaceae",
        "parts_used": ["Radix (Root)"],
        "constituents": ["Gentiopicrin", "Amarogentin", "Gentisin", "Xanthones"],
        "properties": ["Bitter tonic", "Digestive stimulant", "Choleretic", "Febriuge"],
        "description": "The Bitter Root - king of bitters, stimulates digestion"
    },
    "f110r": {
        "latin_name": "Corydalis yanhusuo (Y.H.Chou & Chun C.Hsu) W.T.Wang ex Z.Y.Su & C.Y.Wu",
        "authority": "W.T.Wang & Z.Y.Su, 1986",
        "common_names": ["Corydalis Rhizome", "Yanhusuo"],
        "family": "Papaveraceae",
        "parts_used": ["Rhizoma (Rhizome)"],
        "constituents": ["Dehydrocorybulbine (DHCB)", "Corydaline", "Tetrahydropalmatine"],
        "properties": ["Analgesic", "Sedative", "Antispasmodic", "Anti-inflammatory"],
        "description": "The Chinese Corydalis - traditional analgesic"
    },
    "f114v": {
        "latin_name": "Achillea millefolium L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["Yarrow", "Milfoil", "Nosebleed Plant", "Soldier's Woundwort"],
        "family": "Asteraceae",
        "parts_used": ["Herba (Aerial parts)", "Flos (Flowers)"],
        "constituents": ["Achilleine", "Proazulenes", "Flavonoids", "Tannins", "Volatile oils"],
        "properties": ["Hemostatic", "Anti-inflammatory", "Antimicrobial", "Diaphoretic"],
        "description": "The Warrior's Woundwort - Achilles' healing herb"
    },
    "f116v": {
        "latin_name": "Panax ginseng C.A.Mey.",
        "authority": "C.A.Meyer, 1843",
        "common_names": ["Asian Ginseng", "Korean Ginseng", "Chinese Ginseng"],
        "family": "Araliaceae",
        "parts_used": ["Radix (Root)"],
        "constituents": ["Ginsenosides (Rb1, Rg1, Rg3)", "Polyacetylenes", "Polysaccharides"],
        "properties": ["Adaptogen", "Tonic", "Immunomodulator", "Cognitive enhancer"],
        "description": "The All-Healing Root - king of adaptogens"
    },
    "f239r": {
        "latin_name": "Veratrum album L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["White Hellebore", "European Hellebore"],
        "family": "Melanthiaceae",
        "parts_used": ["Rhizoma (Rhizome)", "Radix (Root)", "Herba (Aerial parts)"],
        "constituents": ["Veratridine", "Cevadine", "Protoveratrine", "Jervine"],
        "properties": ["Emetic", "Cathartic", "Hypotensive", "Insecticidal"],
        "description": "The Terminal Purge - closing the manuscript's cycle"
    },
    "f240v": {
        "latin_name": "Taxus baccata L.",
        "authority": "Linnaeus, 1753",
        "common_names": ["English Yew", "Common Yew", "Tree of Eternity"],
        "family": "Taxaceae",
        "parts_used": ["Cortex (Bark)", "Folia (Leaves)", "Lignum (Wood)"],
        "constituents": ["Taxol (Paclitaxel)", "Taxine A", "Taxine B", "Baccatin III"],
        "properties": ["Cytotoxic", "Cardiotoxic", "Anticancer", "Terminal closure"],
        "description": "The Eternal Tree - final guardian of knowledge, source of Taxol"
    },
}

# =============================================================================
# COMPREHENSIVE RECIPE DATABASE
# =============================================================================

VOYNICH_RECIPES: Dict[str, Recipe] = {
    "f1v_celandine_tincture": Recipe(
        name="Tinctura Chelidonii Majoris (Greater Celandine Tincture)",
        voynichese_name="qo daiin chol shedy otol",
        wilken_key_translation="Process initiator - Nodal valve - Root-arm valve - Pressure valve - Root-stem motion",
        category="Herbal Preparation",
        folio_reference="f1v",
        description="Primary extraction of Chelidonium majus for choleretic and antimicrobial applications",
        ingredients=[
            Ingredient(
                latin_name="Chelidonium majus L.",
                common_name="Greater Celandine",
                part_used="Radix et Herba (Root and Aerial parts)",
                quantity="30 drachmae (approximately 120g)",
                preparation="Freshly harvested, washed with aqua pura",
                properties=["Choleretic", "Antimicrobial", "Spasmolytic"]
            ),
            Ingredient(
                latin_name="Ethanol 40% v/v",
                common_name="Spirits of Wine",
                part_used="Spiritus (Distilled spirits)",
                quantity="10 unciae (approximately 300ml)",
                preparation="Double-distilled from fermented grain",
                properties=["Solvent", "Preservative"]
            ),
            Ingredient(
                latin_name="Aqua pura",
                common_name="Pure Water",
                part_used="Aqua (Water)",
                quantity="5 unciae (approximately 150ml)",
                preparation="Filtered through clean sand",
                properties=["Diluent", "Extractor"]
            ),
        ],
        instructions=[
            "1. Harvest Chelidonium majus during the waxing moon when latex flow is maximal",
            "2. Cleanse roots thoroughly, removing all soil and foreign matter",
            "3. Chop rhizome and aerial parts into small pieces (circiter 5mm)",
            "4. Place prepared herb into a clean glass vessel (ollag)",
            "5. Add spirits of wine and pure water in specified proportions",
            "6. Seal vessel with wax and agitate daily for nine days (novendial)",
            "7. On the tenth day, filter through clean linen",
            "8. Store in amber vessels away from direct solar rays",
            "9. Label with date of preparation and lunar phase"
        ],
        properties=["Choleretic", "Antimicrobial", "Wound cleansing", "Liver tonic"],
        dosage="10-20 guttae (drops) in wine, thrice daily",
        warnings=["Caution: Contains isoquinoline alkaloids - use under guidance", "Contraindicated in pregnancy", "May cause photosensitivity"],
        preparation_time="9 days maceration + 1 day filtration",
        shelf_life="2 years when properly stored",
        related_folios=["f2r", "f3v", "f25r"]
    ),
    
    "f2r_daisy_emollient": Recipe(
        name="Unguentum Bellidis (Daisy Emollient)",
        voynichese_name="daiin chol shedy qokedy",
        wilken_key_translation="Nodal valve - Root-arm valve - Pressure valve - Molecular key",
        category="Topical Preparation",
        folio_reference="f2r",
        description="Soothing ointment prepared from Bellis perennis for dermatological applications",
        ingredients=[
            Ingredient(
                latin_name="Bellis perennis L.",
                common_name="Common Daisy",
                part_used="Herba et Flos (Aerial parts and Flowers)",
                quantity="20 drachmae (approximately 80g)",
                preparation="Dried in shade, flowers separated from stems",
                properties=["Emollient", "Astringent", "Vulnerary"]
            ),
            Ingredient(
                latin_name="Oleum Olea europaea",
                common_name="Olive Oil",
                part_used="Oleum (Oil from fruit)",
                quantity="8 unciae (approximately 240ml)",
                preparation="First cold-pressed, unrefined",
                properties=["Emollient", "Carrier oil", "Antioxidant"]
            ),
            Ingredient(
                latin_name="Cera alba",
                common_name="White Beeswax",
                part_used="Cera (Wax)",
                quantity="2 unciae (approximately 60g)",
                preparation="Purified by melting and filtering",
                properties=["Thickening agent", "Protective barrier"]
            ),
            Ingredient(
                latin_name="Mel",
                common_name="Honey",
                part_used="Mel (Raw honey)",
                quantity="1 uncia (approximately 30ml)",
                preparation="Unfiltered, from local apiaries",
                properties=["Humectant", "Antimicrobial", "Wound healing"]
            ),
        ],
        instructions=[
            "1. Infuse dried daisy flowers and herbs in olive oil using gentle heat (balneum Mariae)",
            "2. Maintain temperature below boiling for four hours",
            "3. Strain through fine linen, pressing to extract all oleaginous matter",
            "4. Return infused oil to clean vessel, add beeswax",
            "5. Heat gently until wax completely melts and incorporates",
            "6. Remove from heat, allow to cool slightly before adding honey",
            "7. Stir vigorously until homogeneous emulsion forms",
            "8. Pour into clean ointment jars while still warm",
            "9. Allow to set undisturbed for 24 hours before sealing"
        ],
        properties=["Emollient", "Wound healing", "Skin soothing", "Anti-inflammatory"],
        dosage="Apply liberally to affected area, twice daily",
        warnings=["For external use only", "Discontinue if irritation occurs", "Test on small area first"],
        preparation_time="6 hours",
        shelf_life="1 year when stored in cool, dark place",
        related_folios=["f1v", "f3v", "f4r"]
    ),
    
    "f3v_sage_cordial": Recipe(
        name="Aqua Salviae (Sage Cordial)",
        voynichese_name="chol shedy otol deor",
        wilken_key_translation="Root-arm valve - Pressure valve - Root-stem motion - Subterranean node",
        category="Aromatic Water",
        folio_reference="f3v",
        description="Distilled water of Salvia officinalis for cerebral and digestive tonification",
        ingredients=[
            Ingredient(
                latin_name="Salvia officinalis L.",
                common_name="Common Sage",
                part_used="Folia (Fresh leaves)",
                quantity="15 drachmae (approximately 60g)",
                preparation="Harvested before flowering, bruised gently",
                properties=["Carminative", "Antispasmodic", "Cerebral tonic"]
            ),
            Ingredient(
                latin_name="Aqua vitae",
                common_name="Spirits",
                part_used="Alcoholic distillate",
                quantity="3 unciae (approximately 90ml)",
                preparation="Triple-distilled grain spirits",
                properties=["Preservative", "Solvent"]
            ),
            Ingredient(
                latin_name="Aqua rosarum",
                common_name="Rose Water",
                part_used="Hydrosol from Rosa damascena",
                quantity="5 unciae (approximately 150ml)",
                preparation="Steam-distilled fresh petals",
                properties=["Astringent", "Fragrant", "Cooling"]
            ),
        ],
        instructions=[
            "1. Place bruised sage leaves in alembic (stella vessel)",
            "2. Add spirits and rose water to cover the herb completely",
            "3. Seal alembic and apply gentle heat (not exceeding 78°C)",
            "4. Collect distillate in receiver vessel (ollag)",
            "5. Continue distillation until approximately 6 unciae collected",
            "6. The first waters (prime aquae) are most potent - keep separate",
            "7. Mix prime aquae with subsequent distillates in ratio 1:2",
            "8. Filter through paper and store in tightly sealed bottles",
            "9. Age for one moon cycle before use"
        ],
        properties=["Cerebral tonic", "Digestive aid", "Mood elevating", "Antimicrobial"],
        dosage="1 cochlear (spoonful) in wine or water, morning and evening",
        warnings=["Avoid excessive use in pregnancy", "May interact with sedative medications", "Not for children under 12"],
        preparation_time="4 hours distillation + 28 days aging",
        shelf_life="3 years when properly sealed",
        related_folios=["f2r", "f4r", "f25r"]
    ),
    
    "f4r_poppy_sedative": Recipe(
        name="Syrupus Papaveris (Poppy Sedative Syrup)",
        voynichese_name="shedy otol deor ollag",
        wilken_key_translation="Pressure valve - Root-stem motion - Subterranean node - Collection vessel",
        category="Sedative Preparation",
        folio_reference="f4r",
        description="Sedative syrup from Papaver somniferum latex for pain and insomnia",
        ingredients=[
            Ingredient(
                latin_name="Papaver somniferum L.",
                common_name="Opium Poppy",
                part_used="Latex (Raw opium)",
                quantity="2 drachmae (approximately 8g)",
                preparation="Incised capsules, dried latex scraped",
                properties=["Narcotic", "Analgesic", "Sedative", "Antitussive"]
            ),
            Ingredient(
                latin_name="Saccharum",
                common_name="Sugar",
                part_used="Crystallized sucrose",
                quantity="12 unciae (approximately 360g)",
                preparation="Purified cane sugar",
                properties=["Sweetening agent", "Preservative"]
            ),
            Ingredient(
                latin_name="Aqua pura",
                common_name="Pure Water",
                part_used="Water",
                quantity="8 unciae (approximately 240ml)",
                preparation="Filtered spring water",
                properties=["Solvent", "Vehicle"]
            ),
            Ingredient(
                latin_name="Crocus sativus L.",
                common_name="Saffron",
                part_used="Stigma (Threads)",
                quantity="5 grana (approximately 0.3g)",
                preparation="Dried, whole threads",
                properties=["Aromatic", "Coloring agent", "Mood elevating"]
            ),
        ],
        instructions=[
            "1. Dissolve raw opium in warm water, stirring until completely dispersed",
            "2. Strain through fine cloth to remove plant debris",
            "3. Prepare sugar syrup by dissolving sugar in remaining water over gentle heat",
            "4. When sugar is fully dissolved, add opium solution",
            "5. Add saffron threads for color and aromatic enhancement",
            "6. Simmer gently for one hour, skimming any impurities",
            "7. Cool to room temperature, filter again if necessary",
            "8. Store in dark glass bottles, sealed with wax",
            "9. Label clearly with contents and preparation date"
        ],
        properties=["Analgesic", "Sedative", "Hypnotic", "Antitussive"],
        dosage="5-10 guttae (drops) for pain; 15-20 guttae for sleep",
        warnings=["EXTREME CAUTION: Contains morphine and codeine", "Highly addictive - use sparingly", "Contraindicated in respiratory depression", "Not for use in children", "Legal restrictions apply"],
        preparation_time="3 hours",
        shelf_life="2 years when properly stored",
        related_folios=["f176r", "f200v", "f3v"]
    ),
    
    "f5r_mandrake_extract": Recipe(
        name="Extractum Mandragorae (Mandrake Root Extract)",
        voynichese_name="otol deor ollag stella",
        wilken_key_translation="Root-stem motion - Subterranean node - Collection vessel - Swell-stem expansion",
        category="Narcotic Preparation",
        folio_reference="f5r",
        description="Potent extract of Mandragora officinarum root for surgical anesthesia",
        ingredients=[
            Ingredient(
                latin_name="Mandragora officinarum L.",
                common_name="Mandrake",
                part_used="Radix (Root)",
                quantity="10 drachmae (approximately 40g)",
                preparation="Dried root, powdered coarsely",
                properties=["Narcotic", "Analgesic", "Hallucinogenic"]
            ),
            Ingredient(
                latin_name="Vinum",
                common_name="Wine",
                part_used="Fermented grape juice",
                quantity="20 unciae (approximately 600ml)",
                preparation="Strong red wine, 12% alcohol",
                properties=["Solvent", "Preservative", "Circulatory stimulant"]
            ),
            Ingredient(
                latin_name="Hyoscyamus niger L.",
                common_name="Black Henbane",
                part_used="Folia (Leaves)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Dried leaves, crushed",
                properties=["Anticholinergic", "Sedative", "Analgesic"]
            ),
        ],
        instructions=[
            "1. Powder mandrake root using mortar of iron (avoid bronze)",
            "2. Mix powdered root with crushed henbane leaves",
            "3. Place mixture in clean glass vessel",
            "4. Cover completely with strong wine",
            "5. Seal vessel and place in warm location (stella position)",
            "6. Agitate daily for fourteen days",
            "7. On the fifteenth day, strain through linen",
            "8. Press marc (residue) to extract all liquid",
            "9. Store in small, dark bottles with tight stoppers",
            "10. Label with skull and crossbones symbol"
        ],
        properties=["Anesthetic", "Analgesic", "Hypnotic", "Deliriant"],
        dosage="5-15 guttae in wine before surgical procedures",
        warnings=["EXTREMELY DANGEROUS: Contains hyoscyamine and scopolamine", "Overdose is fatal", "Causes delirium and hallucinations", "Use only under expert supervision", "Not for unsupervised use"],
        preparation_time="14 days maceration",
        shelf_life="3 years when properly stored",
        related_folios=["f161r", "f152v", "f211r"]
    ),
    
    "f67r_hellebore_purge": Recipe(
        name="Pulvis Hellebori Albi (White Hellebore Purge)",
        voynichese_name="deor ollag stella qokedy",
        wilken_key_translation="Subterranean node - Collection vessel - Swell-stem expansion - Molecular key",
        category="Cathartic Preparation",
        folio_reference="f67r",
        description="Powerful emetic and cathartic powder from Veratrum album rhizome",
        ingredients=[
            Ingredient(
                latin_name="Veratrum album L.",
                common_name="White Hellebore",
                part_used="Rhizoma (Rhizome)",
                quantity="3 drachmae (approximately 12g)",
                preparation="Dried, powdered to fine consistency",
                properties=["Emetic", "Cathartic", "Hypotensive", "Insecticidal"]
            ),
            Ingredient(
                latin_name="Zingiber officinale Roscoe",
                common_name="Ginger",
                part_used="Rhizoma (Root)",
                quantity="2 drachmae (approximately 8g)",
                preparation="Dried, powdered",
                properties=["Carminative", "Anti-emetic", "Warming"]
            ),
            Ingredient(
                latin_name="Cinnamomum verum J.Presl",
                common_name="True Cinnamon",
                part_used="Cortex (Bark)",
                quantity="1 drachma (approximately 4g)",
                preparation="Powdered inner bark",
                properties=["Aromatic", "Carminative", "Warming"]
            ),
        ],
        instructions=[
            "1. Harvest Veratrum album rhizome in autumn after flowering",
            "2. Dry thoroughly in shade for thirty days",
            "3. Powder rhizome to fine consistency using stone mortar",
            "4. Mix with powdered ginger and cinnamon in specified proportions",
            "5. Pass through fine sieve to ensure uniform particle size",
            "6. Store in tightly sealed vessel with desiccant",
            "7. Label with appropriate warnings and dosage instructions"
        ],
        properties=["Emetic", "Cathartic", "Vermifuge", "Hypotensive"],
        dosage="1-2 grana (grains) in warm water, once only",
        warnings=["EXTREMELY TOXIC: Veratrum alkaloids can be fatal", "Causes violent vomiting", "Contraindicated in weak constitution", "Use only under medical supervision", "Keep away from children"],
        preparation_time="30 days drying + 1 hour preparation",
        shelf_life="2 years when stored properly",
        related_folios=["f239r", "f68v", "f220v"]
    ),
    
    "f68v_nightshade_ointment": Recipe(
        name="Unguentum Solani (Nightshade Ointment)",
        voynichese_name="ollag stella qokedy qokeedy",
        wilken_key_translation="Collection vessel - Swell-stem expansion - Molecular key - Batch authentication",
        category="Topical Analgesic",
        folio_reference="f68v",
        description="Analgesic ointment from Solanaceae species for neuralgic pain",
        ingredients=[
            Ingredient(
                latin_name="Atropa belladonna L.",
                common_name="Deadly Nightshade",
                part_used="Folia (Leaves)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Fresh leaves, chopped finely",
                properties=["Anticholinergic", "Analgesic", "Mydriatic"]
            ),
            Ingredient(
                latin_name="Hyoscyamus niger L.",
                common_name="Black Henbane",
                part_used="Semen (Seeds)",
                quantity="2 drachmae (approximately 8g)",
                preparation="Dried seeds, crushed",
                properties=["Sedative", "Analgesic", "Antispasmodic"]
            ),
            Ingredient(
                latin_name="Oleum Lard",
                common_name="Lard",
                part_used="Adeps (Rendered pork fat)",
                quantity="10 unciae (approximately 300g)",
                preparation="Freshly rendered, purified",
                properties=["Base", "Emollient", "Penetration enhancer"]
            ),
            Ingredient(
                latin_name="Oleum Gaultheriae",
                common_name="Wintergreen Oil",
                part_used="Essential oil",
                quantity="20 guttae (drops)",
                preparation="Steam distilled",
                properties=["Counterirritant", "Analgesic", "Anti-inflammatory"]
            ),
        ],
        instructions=[
            "1. Gently heat lard in clean vessel until liquid",
            "2. Add chopped nightshade leaves and henbane seeds",
            "3. Maintain low heat for six hours, stirring occasionally",
            "4. Do not allow to boil - maintain below 60°C",
            "5. Strain through fine cloth, pressing to extract all fat",
            "6. Return strained fat to clean vessel",
            "7. Add wintergreen oil when temperature drops below 40°C",
            "8. Stir until homogeneous",
            "9. Pour into ointment jars while still warm",
            "10. Allow to cool and set before sealing"
        ],
        properties=["Analgesic", "Counterirritant", "Neuralgic pain relief", "Anti-inflammatory"],
        dosage="Apply to affected area, rub in thoroughly, up to three times daily",
        warnings=["FOR EXTERNAL USE ONLY", "Contains tropane alkaloids - toxic if ingested", "Wash hands after application", "Do not apply to broken skin", "Keep away from eyes and mucous membranes"],
        preparation_time="8 hours",
        shelf_life="1 year when refrigerated",
        related_folios=["f69r", "f70v", "f211r"]
    ),
    
    "f75r_arnica_compress": Recipe(
        name="Cataplasma Arnicae (Arnica Compress)",
        voynichese_name="stella qokedy qokeedy daiin",
        wilken_key_translation="Swell-stem expansion - Molecular key - Batch authentication - Nodal valve",
        category="Traumatic Remedy",
        folio_reference="f75r",
        description="Poultice of Arnica montana for bruises, sprains, and traumatic injuries",
        ingredients=[
            Ingredient(
                latin_name="Arnica montana L.",
                common_name="Mountain Arnica",
                part_used="Flos (Flowers)",
                quantity="10 drachmae (approximately 40g)",
                preparation="Dried flowers, crushed",
                properties=["Anti-inflammatory", "Analgesic", "Circulatory stimulant"]
            ),
            Ingredient(
                latin_name="Aqua fervens",
                common_name="Hot Water",
                part_used="Water at 80°C",
                quantity="Sufficient to moisten",
                preparation="Freshly boiled",
                properties=["Solvent", "Heat conductor"]
            ),
            Ingredient(
                latin_name="Linen cloth",
                common_name="Clean Linen",
                part_used="Woven fabric",
                quantity="1 piece, 6 x 6 inches",
                preparation="Boiled and dried",
                properties=["Delivery vehicle", "Heat retention"]
            ),
        ],
        instructions=[
            "1. Place crushed arnica flowers in shallow bowl",
            "2. Pour hot water over flowers to moisten thoroughly",
            "3. Allow to steep for 10 minutes",
            "4. Lay linen cloth flat and spread flower mixture evenly",
            "5. Fold cloth to enclose the herbal material",
            "6. Apply to affected area while still warm",
            "7. Secure with bandage, leave in place for 30-60 minutes",
            "8. Repeat every 4 hours for acute injuries",
            "9. Discard used material - do not reuse"
        ],
        properties=["Anti-inflammatory", "Bruise resolution", "Pain relief", "Swelling reduction"],
        dosage="Apply fresh compress every 4 hours for 24-48 hours",
        warnings=["FOR EXTERNAL USE ONLY", "Do not apply to broken skin", "May cause dermatitis in sensitive individuals", "Test on small area first", "Not for long-term use"],
        preparation_time="15 minutes",
        shelf_life="Use immediately - prepare fresh each time",
        related_folios=["f221r", "f76v", "f77r"]
    ),
    
    "f79v_comfrey_bone_knit": Recipe(
        name="Consolida Ossium (Bone-Knitting Compound)",
        voynichese_name="qokedy qokeedy daiin chol",
        wilken_key_translation="Molecular key - Batch authentication - Nodal valve - Root-arm valve",
        category="Fracture Remedy",
        folio_reference="f79v",
        description="Traditional compound for promoting bone healing and union",
        ingredients=[
            Ingredient(
                latin_name="Symphytum officinale L.",
                common_name="Comfrey",
                part_used="Radix (Root)",
                quantity="20 drachmae (approximately 80g)",
                preparation="Fresh root, grated",
                properties=["Vulnerary", "Anti-inflammatory", "Cell proliferant"]
            ),
            Ingredient(
                latin_name="Plantago major L.",
                common_name="Plantain",
                part_used="Folia (Leaves)",
                quantity="15 drachmae (approximately 60g)",
                preparation="Fresh leaves, washed and chopped",
                properties=["Vulnerary", "Astringent", "Anti-inflammatory"]
            ),
            Ingredient(
                latin_name="Eggshells",
                common_name="Calcined Eggshells",
                part_used="Testa ovorum (Calcined shells)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Burned to white ash, powdered",
                properties=["Calcium source", "Mineral supplement"]
            ),
            Ingredient(
                latin_name="Mel",
                common_name="Honey",
                part_used="Raw honey",
                quantity="3 unciae (approximately 90ml)",
                preparation="Unfiltered, local source",
                properties=["Antimicrobial", "Wound healing", "Binder"]
            ),
        ],
        instructions=[
            "1. Grate fresh comfrey root into fine pulp",
            "2. Chop plantain leaves and pound to paste",
            "3. Mix comfrey and plantain in equal proportions",
            "4. Add calcined eggshell powder gradually",
            "5. Incorporate honey to form thick paste",
            "6. Apply directly to clean fracture site",
            "7. Cover with clean linen and secure with bandage",
            "8. Change dressing daily, cleaning wound each time",
            "9. Continue until bone union is achieved"
        ],
        properties=["Bone knitting", "Wound healing", "Anti-inflammatory", "Tissue regeneration"],
        dosage="Apply fresh dressing daily for 4-6 weeks",
        warnings=["FOR EXTERNAL USE ONLY", "Do not use on deep wounds (may cause rapid surface healing over infection)", "Ensure proper bone alignment before application", "Consult bone-setter for complex fractures"],
        preparation_time="30 minutes",
        shelf_life="Prepare fresh daily",
        related_folios=["f226v", "f80r", "f81v"]
    ),
    
    "f85r_universal_balm": Recipe(
        name="Balsamum Universale (Universal Balm)",
        voynichese_name="qokeedy daiin chol shedy",
        wilken_key_translation="Batch authentication - Nodal valve - Root-arm valve - Pressure valve",
        category="Panacea",
        folio_reference="f85r",
        description="Complex aromatic balsam for multiple applications - the 'cure-all' preparation",
        ingredients=[
            Ingredient(
                latin_name="Commiphora myrrha (Nees) Engl.",
                common_name="Myrrh",
                part_used="Resina (Resin)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Tears of resin, coarsely powdered",
                properties=["Antimicrobial", "Astringent", "Wound healing"]
            ),
            Ingredient(
                latin_name="Boswellia sacra Flueck.",
                common_name="Frankincense",
                part_used="Resina (Resin)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Tears of resin, coarsely powdered",
                properties=["Anti-inflammatory", "Aromatic", "Expectorant"]
            ),
            Ingredient(
                latin_name="Aloe ferox Mill.",
                common_name="Cape Aloe",
                part_used="Succus (Dried juice)",
                quantity="3 drachmae (approximately 12g)",
                preparation="Dried latex from leaves",
                properties=["Cathartic", "Bitter", "Wound healing"]
            ),
            Ingredient(
                latin_name="Crocus sativus L.",
                common_name="Saffron",
                part_used="Stigma (Threads)",
                quantity="10 grana (approximately 0.6g)",
                preparation="Highest quality, whole threads",
                properties=["Aromatic", "Antidepressant", "Carminative"]
            ),
            Ingredient(
                latin_name="Oleum Olea europaea",
                common_name="Olive Oil",
                part_used="First cold-pressed oil",
                quantity="16 unciae (approximately 480ml)",
                preparation="Unrefined, extra virgin",
                properties=["Carrier oil", "Emollient", "Nutritive"]
            ),
        ],
        instructions=[
            "1. Combine powdered myrrh and frankincense in mortar",
            "2. Grind together until fine powder achieved",
            "3. Add aloe and saffron, continue grinding",
            "4. Heat olive oil gently in clean vessel",
            "5. Add resin mixture to warm oil gradually",
            "6. Maintain gentle heat for 12 hours (balneum Mariae)",
            "7. Stir occasionally to prevent sticking",
            "8. Strain through fine linen while still warm",
            "9. Store in dark glass, seal with wax",
            "10. Age for three months before use"
        ],
        properties=["Universal remedy", "Wound healing", "Anti-inflammatory", "Antimicrobial", "Aromatic"],
        dosage="For wounds: apply directly. For internal: 5 guttae in wine. For incense: burn on charcoal.",
        warnings=["Internal use may cause catharsis", "Test for allergic reaction before extensive use", "Not for use in pregnancy"],
        preparation_time="14 hours preparation + 90 days aging",
        shelf_life="5 years when properly stored",
        related_folios=["f86v", "f87r", "f88v"]
    ),
    
    "f88r_fever_tonic": Recipe(
        name="Aqua Febrifuga (Fever-Reducing Water)",
        voynichese_name="daiin chol shedy otol",
        wilken_key_translation="Nodal valve - Root-arm valve - Pressure valve - Root-stem motion",
        category="Antipyretic",
        folio_reference="f88r",
        description="Distilled water compound for reducing fever and ague",
        ingredients=[
            Ingredient(
                latin_name="Cinchona pubescens Vahl",
                common_name="Quinine Bark",
                part_used="Cortex (Bark)",
                quantity="10 drachmae (approximately 40g)",
                preparation="Dried bark, coarsely powdered",
                properties=["Antimalarial", "Antipyretic", "Bitter tonic"]
            ),
            Ingredient(
                latin_name="Artemisia annua L.",
                common_name="Sweet Wormwood",
                part_used="Herba (Aerial parts)",
                quantity="8 drachmae (approximately 32g)",
                preparation="Dried herb, flowering tops",
                properties=["Antimalarial", "Antipyretic", "Bitter"]
            ),
            Ingredient(
                latin_name="Gentiana lutea L.",
                common_name="Great Yellow Gentian",
                part_used="Radix (Root)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Dried root, sliced",
                properties=["Bitter tonic", "Digestive stimulant", "Febriuge"]
            ),
            Ingredient(
                latin_name="Aqua vitae",
                common_name="Spirits",
                part_used="40% alcohol",
                quantity="20 unciae (approximately 600ml)",
                preparation="Grain spirits",
                properties=["Solvent", "Preservative"]
            ),
        ],
        instructions=[
            "1. Combine all herbs in large glass vessel",
            "2. Cover with spirits of wine",
            "3. Seal and macerate for 21 days, agitating daily",
            "4. After maceration, transfer to alembic",
            "5. Distill using gentle heat",
            "6. Collect first waters separately (most potent)",
            "7. Continue distillation until 15 unciae collected",
            "8. Mix first waters with subsequent in ratio 1:3",
            "9. Filter and store in sealed bottles",
            "10. Label with date and contents"
        ],
        properties=["Antipyretic", "Antimalarial", "Bitter tonic", "Digestive stimulant"],
        dosage="1 cochlear (spoonful) in water, every 4 hours during fever",
        warnings=["May cause tinnitus in high doses (cinchonism)", "Bitter taste may cause nausea", "Not for long-term use"],
        preparation_time="21 days maceration + 6 hours distillation",
        shelf_life="3 years when properly stored",
        related_folios=["f183v", "f89r", "f90v"]
    ),
    
    "f91r_cardiac_tonic": Recipe(
        name="Tinctura Digitalis (Foxglove Cardiac Tonic)",
        voynichese_name="chol shedy otol deor",
        wilken_key_translation="Root-arm valve - Pressure valve - Root-stem motion - Subterranean node",
        category="Cardiac Remedy",
        folio_reference="f91r",
        description="Carefully prepared tincture of Digitalis purpurea for cardiac insufficiency",
        ingredients=[
            Ingredient(
                latin_name="Digitalis purpurea L.",
                common_name="Foxglove",
                part_used="Folia (Fresh leaves)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Leaves of second year's growth, dried rapidly",
                properties=["Cardiotonic", "Antiarrhythmic", "Diuretic"]
            ),
            Ingredient(
                latin_name="Ethanol 25% v/v",
                common_name="Diluted Spirits",
                part_used="Alcoholic solution",
                quantity="20 unciae (approximately 600ml)",
                preparation="Diluted from stronger spirits",
                properties=["Solvent", "Preservative"]
            ),
        ],
        instructions=[
            "1. Collect foxglove leaves before flowering begins",
            "2. Dry rapidly in shade to preserve potency",
            "3. Powder dried leaves coarsely",
            "4. Place in glass vessel and cover with diluted spirits",
            "5. Seal vessel and macerate for 14 days",
            "6. Agitate daily to ensure thorough extraction",
            "7. After maceration, filter through fine linen",
            "8. Allow to stand for 48 hours to settle",
            "9. Decant clear liquid carefully",
            "10. Store in small, dark bottles with precise labels"
        ],
        properties=["Cardiotonic", "Diuretic", "Antiarrhythmic"],
        dosage="1-2 guttae, thrice daily (EXTREMELY POTENT - measure carefully)",
        warnings=["EXTREMELY TOXIC: Narrow therapeutic window", "Overdose causes fatal cardiac arrhythmia", "Requires medical supervision", "Contraindicated in partial heart block", "Drug interactions common", "NOT FOR SELF-MEDICATION"],
        preparation_time="14 days maceration + 2 days settling",
        shelf_life="2 years when properly stored",
        related_folios=["f191r", "f92v", "f93r"]
    ),
    
    "f103r_women_balm": Recipe(
        name="Balsamum Mulierum (Women's Balm)",
        voynichese_name="shedy otol deor ollag",
        wilken_key_translation="Pressure valve - Root-stem motion - Subterranean node - Collection vessel",
        category="Gynecological Preparation",
        folio_reference="f103r",
        description="Traditional preparation for women's health and reproductive wellness",
        ingredients=[
            Ingredient(
                latin_name="Vitex agnus-castus L.",
                common_name="Chaste Tree",
                part_used="Fructus (Berries)",
                quantity="10 drachmae (approximately 40g)",
                preparation="Dried berries, crushed",
                properties=["Hormonal regulator", "Prolactin inhibitor", "Menstrual regulator"]
            ),
            Ingredient(
                latin_name="Angelica sinensis (Oliv.) Diels",
                common_name="Dong Quai",
                part_used="Radix (Root)",
                quantity="8 drachmae (approximately 32g)",
                preparation="Dried root, sliced",
                properties=["Uterine tonic", "Blood tonic", "Antispasmodic"]
            ),
            Ingredient(
                latin_name="Cimicifuga racemosa (L.) Nutt.",
                common_name="Black Cohosh",
                part_used="Rhizoma (Rhizome)",
                quantity="6 drachmae (approximately 24g)",
                preparation="Dried rhizome, coarsely powdered",
                properties=["Phytoestrogenic", "Antispasmodic", "Anti-inflammatory"]
            ),
            Ingredient(
                latin_name="Rubus idaeus L.",
                common_name="Red Raspberry",
                part_used="Folia (Leaves)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Dried leaves",
                properties=["Uterine tonic", "Astringent", "Partus preparator"]
            ),
            Ingredient(
                latin_name="Mel",
                common_name="Honey",
                part_used="Raw honey",
                quantity="4 unciae (approximately 120ml)",
                preparation="Unfiltered, local source",
                properties=["Sweetening agent", "Preservative", "Nutritive"]
            ),
        ],
        instructions=[
            "1. Combine all dried herbs in large mortar",
            "2. Grind together to coarse powder",
            "3. Place powdered herbs in glass vessel",
            "4. Add sufficient water to cover by two fingers' breadth",
            "5. Simmer gently for 2 hours, adding water as needed",
            "6. Strain liquid through fine linen",
            "7. Return liquid to clean vessel, add honey",
            "8. Simmer until reduced by half (to syrup consistency)",
            "9. Pour into small bottles while warm",
            "10. Seal and store in cool place"
        ],
        properties=["Uterine tonic", "Hormonal balance", "Menstrual regulator", "Partus preparator"],
        dosage="1 cochlear (spoonful) twice daily, or as directed by midwife",
        warnings=["Not for use during pregnancy except under supervision", "May interact with hormonal medications", "Discontinue if adverse effects occur"],
        preparation_time="4 hours",
        shelf_life="1 year when refrigerated",
        related_folios=["f104v", "f105r", "f116v"]
    ),
    
    "f106v_digestive_elixir": Recipe(
        name="Elixir Digestivum (Digestive Elixir)",
        voynichese_name="otol deor ollag stella",
        wilken_key_translation="Root-stem motion - Subterranean node - Collection vessel - Swell-stem expansion",
        category="Digestive Tonic",
        folio_reference="f106v",
        description="Carminative and digestive stimulant for dyspepsia and flatulence",
        ingredients=[
            Ingredient(
                latin_name="Gentiana lutea L.",
                common_name="Gentian",
                part_used="Radix (Root)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Dried root, coarsely powdered",
                properties=["Bitter tonic", "Digestive stimulant", "Choleretic"]
            ),
            Ingredient(
                latin_name="Zingiber officinale Roscoe",
                common_name="Ginger",
                part_used="Rhizoma (Root)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Dried, powdered",
                properties=["Carminative", "Anti-emetic", "Digestive stimulant"]
            ),
            Ingredient(
                latin_name="Foeniculum vulgare Mill.",
                common_name="Fennel",
                part_used="Semen (Seeds)",
                quantity="4 drachmae (approximately 16g)",
                preparation="Dried seeds, crushed",
                properties=["Carminative", "Antispasmodic", "Galactagogue"]
            ),
            Ingredient(
                latin_name="Coriandrum sativum L.",
                common_name="Coriander",
                part_used="Semen (Seeds)",
                quantity="3 drachmae (approximately 12g)",
                preparation="Dried seeds, crushed",
                properties=["Carminative", "Aromatic", "Digestive"]
            ),
            Ingredient(
                latin_name="Cinnamomum verum J.Presl",
                common_name="Cinnamon",
                part_used="Cortex (Bark)",
                quantity="2 drachmae (approximately 8g)",
                preparation="Powdered bark",
                properties=["Carminative", "Astringent", "Warming"]
            ),
            Ingredient(
                latin_name="Ethanol 40% v/v",
                common_name="Spirits",
                part_used="Alcoholic solution",
                quantity="30 unciae (approximately 900ml)",
                preparation="Grain spirits",
                properties=["Solvent", "Preservative"]
            ),
        ],
        instructions=[
            "1. Combine all powdered herbs in glass vessel",
            "2. Cover with spirits of wine",
            "3. Seal vessel and macerate for 30 days",
            "4. Agitate daily to ensure thorough extraction",
            "5. After maceration, filter through fine linen",
            "6. Press marc to extract all liquid",
            "7. Allow to stand for 48 hours to settle",
            "8. Decant clear liquid carefully",
            "9. Store in sealed bottles",
            "10. Age for 3 months before use"
        ],
        properties=["Digestive stimulant", "Carminative", "Bitter tonic", "Anti-emetic"],
        dosage="20-30 guttae in water before meals",
        warnings=["Bitter taste may be unpleasant to some", "Avoid in gastric ulcers", "Not for use in acute gastritis"],
        preparation_time="30 days maceration + 90 days aging",
        shelf_life="5 years when properly stored",
        related_folios=["f107r", "f108v", "f109r"]
    ),
    
    "f110r_pain_tincture": Recipe(
        name="Tinctura Analgesica (Pain-Relieving Tincture)",
        voynichese_name="deor ollag stella qokedy",
        wilken_key_translation="Subterranean node - Collection vessel - Swell-stem expansion - Molecular key",
        category="Analgesic Preparation",
        folio_reference="f110r",
        description="Powerful analgesic tincture for moderate to severe pain",
        ingredients=[
            Ingredient(
                latin_name="Papaver somniferum L.",
                common_name="Opium Poppy",
                part_used="Latex (Raw opium)",
                quantity="3 drachmae (approximately 12g)",
                preparation="Dried latex, powdered",
                properties=["Narcotic analgesic", "Sedative", "Antitussive"]
            ),
            Ingredient(
                latin_name="Corydalis yanhusuo (Y.H.Chou & Chun C.Hsu) W.T.Wang ex Z.Y.Su & C.Y.Wu",
                common_name="Corydalis Rhizome",
                part_used="Rhizoma (Rhizome)",
                quantity="6 drachmae (approximately 24g)",
                preparation="Dried rhizome, sliced",
                properties=["Analgesic", "Sedative", "Antispasmodic"]
            ),
            Ingredient(
                latin_name="Salix alba L.",
                common_name="White Willow",
                part_used="Cortex (Bark)",
                quantity="8 drachmae (approximately 32g)",
                preparation="Dried bark, coarsely powdered",
                properties=["Analgesic", "Anti-inflammatory", "Antipyretic"]
            ),
            Ingredient(
                latin_name="Ethanol 60% v/v",
                common_name="Strong Spirits",
                part_used="Alcoholic solution",
                quantity="30 unciae (approximately 900ml)",
                preparation="Grain spirits",
                properties=["Solvent", "Preservative"]
            ),
        ],
        instructions=[
            "1. Combine willow bark and corydalis in glass vessel",
            "2. Cover with strong spirits",
            "3. Macerate for 21 days, agitating daily",
            "4. Dissolve powdered opium in small amount of warm water",
            "5. Add opium solution to macerated tincture",
            "6. Mix thoroughly and allow to stand for 7 days",
            "7. Filter through fine linen",
            "8. Store in small, dark bottles with tight stoppers",
            "9. Label clearly with warnings"
        ],
        properties=["Analgesic", "Sedative", "Anti-inflammatory"],
        dosage="10-20 guttae for pain, may repeat every 4 hours",
        warnings=["EXTREME CAUTION: Contains morphine - highly addictive", "Causes drowsiness - do not operate machinery", "Contraindicated in respiratory depression", "Not for long-term use", "Legal restrictions apply"],
        preparation_time="28 days total",
        shelf_life="3 years when properly stored",
        related_folios=["f111v", "f112r", "f113v"]
    ),
    
    "f114v_wound_powder": Recipe(
        name="Pulvis Vulnerarius (Wound-Healing Powder)",
        voynichese_name="ollag stella qokedy qokeedy",
        wilken_key_translation="Collection vessel - Swell-stem expansion - Molecular key - Batch authentication",
        category="Hemostatic Preparation",
        folio_reference="f114v",
        description="Styptic powder for wound treatment and bleeding control",
        ingredients=[
            Ingredient(
                latin_name="Achillea millefolium L.",
                common_name="Yarrow",
                part_used="Herba (Aerial parts)",
                quantity="10 drachmae (approximately 40g)",
                preparation="Dried herb, powdered",
                properties=["Hemostatic", "Anti-inflammatory", "Antimicrobial"]
            ),
            Ingredient(
                latin_name="Plantago major L.",
                common_name="Plantain",
                part_used="Folia (Leaves)",
                quantity="8 drachmae (approximately 32g)",
                preparation="Dried leaves, powdered",
                properties=["Vulnerary", "Astringent", "Anti-inflammatory"]
            ),
            Ingredient(
                latin_name="Calendula officinalis L.",
                common_name="Calendula",
                part_used="Flos (Flowers)",
                quantity="6 drachmae (approximately 24g)",
                preparation="Dried flowers, powdered",
                properties=["Vulnerary", "Antimicrobial", "Anti-inflammatory"]
            ),
            Ingredient(
                latin_name="Commiphora myrrha (Nees) Engl.",
                common_name="Myrrh",
                part_used="Resina (Resin)",
                quantity="4 drachmae (approximately 16g)",
                preparation="Powdered tears",
                properties=["Antimicrobial", "Astringent", "Wound healing"]
            ),
            Ingredient(
                latin_name="Alumen",
                common_name="Alum",
                part_used="Mineral salt",
                quantity="2 drachmae (approximately 8g)",
                preparation="Powdered crystals",
                properties=["Astringent", "Antiseptic", "Hemostatic"]
            ),
        ],
        instructions=[
            "1. Powder each ingredient separately to fine consistency",
            "2. Sieve each powder to ensure uniform particle size",
            "3. Combine all powders in specified proportions",
            "4. Mix thoroughly using geometric dilution method",
            "5. Pass final mixture through fine sieve",
            "6. Store in tightly sealed container",
            "7. Keep in dry place away from moisture",
            "8. Label clearly with contents and date"
        ],
        properties=["Hemostatic", "Wound healing", "Antimicrobial", "Astringent"],
        dosage="Apply directly to clean wound, cover with bandage",
        warnings=["For external use only", "Clean wound before application", "Change dressing daily", "Seek medical attention for deep wounds"],
        preparation_time="2 hours",
        shelf_life="2 years when kept dry",
        related_folios=["f115r", "f230v", "f221r"]
    ),
    
    "f116v_master_elixir": Recipe(
        name="Elixir Magistrale (Master Elixir)",
        voynichese_name="stella qokedy qokeedy daiin chol",
        wilken_key_translation="Swell-stem expansion - Molecular key - Batch authentication - Nodal valve - Root-arm valve",
        category="Panacea",
        folio_reference="f116v",
        description="The master formula combining multiple botanicals for systemic wellness - the culmination of the Wilken Key pharmaceutical tradition",
        ingredients=[
            Ingredient(
                latin_name="Panax ginseng C.A.Mey.",
                common_name="Asian Ginseng",
                part_used="Radix (Root)",
                quantity="6 drachmae (approximately 24g)",
                preparation="Dried root, 6 years old, sliced",
                properties=["Adaptogen", "Tonic", "Immunomodulator"]
            ),
            Ingredient(
                latin_name="Rhodiola rosea L.",
                common_name="Golden Root",
                part_used="Radix (Root)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Dried root, powdered",
                properties=["Adaptogen", "Antifatigue", "Cognitive enhancer"]
            ),
            Ingredient(
                latin_name="Schisandra chinensis (Turcz.) Baill.",
                common_name="Schisandra",
                part_used="Fructus (Berries)",
                quantity="4 drachmae (approximately 16g)",
                preparation="Dried berries",
                properties=["Adaptogen", "Hepatoprotective", "Tonic"]
            ),
            Ingredient(
                latin_name="Astragalus membranaceus (Fisch.) Bunge",
                common_name="Astragalus",
                part_used="Radix (Root)",
                quantity="8 drachmae (approximately 32g)",
                preparation="Dried root, sliced",
                properties=["Immunomodulator", "Tonic", "Adaptogen"]
            ),
            Ingredient(
                latin_name="Ganoderma lucidum (Curtis) P.Karst.",
                common_name="Reishi Mushroom",
                part_used="Fungus (Whole mushroom)",
                quantity="5 drachmae (approximately 20g)",
                preparation="Dried, sliced",
                properties=["Immunomodulator", "Adaptogen", "Longevity tonic"]
            ),
            Ingredient(
                latin_name="Ethanol 35% v/v",
                common_name="Spirits",
                part_used="Alcoholic solution",
                quantity="50 unciae (approximately 1500ml)",
                preparation="Grain spirits",
                properties=["Solvent", "Preservative"]
            ),
            Ingredient(
                latin_name="Mel",
                common_name="Honey",
                part_used="Raw honey",
                quantity="10 unciae (approximately 300ml)",
                preparation="Unfiltered, wildflower",
                properties=["Sweetening agent", "Preservative", "Tonic"]
            ),
        ],
        instructions=[
            "1. Combine all dried botanicals in large glass vessel",
            "2. Cover with spirits of wine",
            "3. Seal vessel with wax and store in cool, dark place",
            "4. Macerate for 60 days, agitating daily",
            "5. On the 61st day, filter through fine linen",
            "6. Press marc thoroughly to extract all essence",
            "7. Add honey to filtered liquid",
            "8. Mix until honey is completely dissolved",
            "9. Allow to stand for 7 days to settle",
            "10. Decant clear liquid into clean bottles",
            "11. Age for 6 months before use",
            "12. The elixir improves with age up to 10 years"
        ],
        properties=["Systemic tonic", "Adaptogenic", "Immunomodulatory", "Longevity promoting", "General wellness"],
        dosage="30 guttae in wine or water, morning and evening",
        warnings=["May interact with immunosuppressive medications", "Discontinue before surgery", "Not for use in acute infections", "Consult healthcare provider if taking medications"],
        preparation_time="60 days maceration + 6 months aging (optimal at 1 year)",
        shelf_life="10+ years when properly stored",
        related_folios=["f1v", "f2r", "f3v", "f4r", "f5r", "f67r", "f75r", "f85r", "f88r", "f103r", "f106v", "f110r", "f114v"]
    ),
}

# =============================================================================
# FOLIO DATABASE
# =============================================================================

FOLIO_DATABASE: Dict[str, FolioData] = {
    "f1r": FolioData(
        folio_number="f1r",
        section="Herbal",
        phase="Phase 1: Opening Protocols",
        yale_image_id=1006076,
        description="The inaugural folio featuring Greater Celandine (Chelidonium majus) establishing foundational protocols for botanical identification.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Chelidonium majus L.",
                common_names=["Greater Celandine", "Swallowwort", "Tetterwort"],
                family="Papaveraceae",
                parts_used=["Radix", "Latex", "Folia"],
                properties=["Choleretic", "Antimicrobial", "Analgesic"],
                voynichese_glyphs=["qo", "daiin", "chol"],
                description="The Lobed-Leaf Plant - milky latex-bearing herb"
            )
        ],
        recipes=["f1v_celandine_tincture"],
        related_folios=["f1v", "f2r", "f25r"],
        scholarly_notes="The opening folio establishes the Wilken Key methodology with Greater Celandine, a plant associated with the return of swallows in folklore."
    ),
    
    "f1v": FolioData(
        folio_number="f1v",
        section="Herbal",
        phase="Phase 1: Opening Protocols",
        yale_image_id=1006077,
        description="Verso of the opening protocol presenting Greater Celandine in mature flowering form with detailed root structure.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Chelidonium majus L.",
                common_names=["Greater Celandine", "Swallowwort"],
                family="Papaveraceae",
                parts_used=["Radix", "Herba", "Flos"],
                properties=["Choleretic", "Antimicrobial", "Spasmolytic"],
                voynichese_glyphs=["daiin", "chol", "shedy"],
                description="Complete plant with flowering stems and root system"
            )
        ],
        recipes=["f1v_celandine_tincture"],
        related_folios=["f1r", "f2r"],
        scholarly_notes="The verso provides complete morphological study necessary for accurate identification."
    ),
    
    "f2r": FolioData(
        folio_number="f2r",
        section="Herbal",
        phase="Phase 1: Opening Protocols",
        yale_image_id=1006078,
        description="The Daisy Folio - presenting Bellis perennis as a secondary opening protocol herb with emollient and vulnerary properties.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Bellis perennis L.",
                common_names=["Common Daisy", "English Daisy", "Woundwort"],
                family="Asteraceae",
                parts_used=["Herba", "Flos", "Folia"],
                properties=["Emollient", "Astringent", "Vulnerary"],
                voynichese_glyphs=["chol", "shedy", "qokedy"],
                description="The Day's Eye - opening and closing with the sun"
            )
        ],
        recipes=["f2r_daisy_emollient"],
        related_folios=["f1v", "f3v", "f4r"],
        scholarly_notes="The daisy's name 'perennis' (everlasting) reflects its persistent flowering nature."
    ),
    
    "f3r": FolioData(
        folio_number="f3r",
        section="Herbal",
        phase="Phase 1: Opening Protocols",
        yale_image_id=1006080,
        description="The Sage Folio - introducing Salvia officinalis as a cerebral and digestive tonic of primary importance.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Salvia officinalis L.",
                common_names=["Common Sage", "Garden Sage", "Dalmatian Sage"],
                family="Lamiaceae",
                parts_used=["Folia", "Cacumen", "Herba"],
                properties=["Carminative", "Antispasmodic", "Cerebral tonic"],
                voynichese_glyphs=["otol", "deor", "ollag"],
                description="The Saving Plant - from Latin 'salvere' meaning to heal"
            )
        ],
        recipes=["f3v_sage_cordial"],
        related_folios=["f2r", "f4r", "f25r"],
        scholarly_notes="Sage's Latin name reflects its esteemed status as a healing plant."
    ),
    
    "f4r": FolioData(
        folio_number="f4r",
        section="Herbal",
        phase="Phase 1: Opening Protocols",
        yale_image_id=1006082,
        description="The Poppy Folio - introducing Papaver somniferum as a sedative and analgesic agent of pharmaceutical significance.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Papaver somniferum L.",
                common_names=["Opium Poppy", "Sleep-Bearing Poppy", "Breadseed Poppy"],
                family="Papaveraceae",
                parts_used=["Latex", "Semen", "Cortex capsulae"],
                properties=["Narcotic", "Analgesic", "Sedative", "Antitussive"],
                voynichese_glyphs=["shedy", "otol", "deor", "ollag"],
                description="The Sleep-Bringer - latex yields morphine and codeine"
            )
        ],
        recipes=["f4r_poppy_sedative"],
        related_folios=["f3v", "f5r", "f176r"],
        scholarly_notes="The opium poppy has been cultivated for over 6,000 years for its medicinal latex."
    ),
    
    "f5r": FolioData(
        folio_number="f5r",
        section="Herbal",
        phase="Phase 1: Opening Protocols",
        yale_image_id=1006084,
        description="The Mandrake Folio - introducing Mandragora officinarum, legendary for its humanoid root and narcotic properties.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Mandragora officinarum L.",
                common_names=["Mandrake", "Love Apple", "Devil's Testicles"],
                family="Solanaceae",
                parts_used=["Radix", "Folia", "Fructus"],
                properties=["Narcotic", "Hallucinogenic", "Analgesic"],
                voynichese_glyphs=["otol", "deor", "ollag", "stella"],
                description="The Human Root - forked root resembles human form"
            )
        ],
        recipes=["f5r_mandrake_extract"],
        related_folios=["f4r", "f9r", "f161r"],
        scholarly_notes="Mandrake has been surrounded by superstition since antiquity."
    ),
    
    "f9r": FolioData(
        folio_number="f9r",
        section="Herbal",
        phase="Phase 2: Mid-Herbal",
        yale_image_id=1006094,
        description="The Mandrake Folio - detailed study of Mandragora officinarum with flowering characteristics.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Mandragora officinarum L.",
                common_names=["Mandrake", "Satan's Apple"],
                family="Solanaceae",
                parts_used=["Radix", "Folia", "Fructus"],
                properties=["Narcotic", "Anesthetic", "Deliriant"],
                voynichese_glyphs=["qo", "daiin", "chol", "shedy"],
                description="Flowering mandrake with characteristic purple flowers"
            )
        ],
        recipes=["f5r_mandrake_extract"],
        related_folios=["f5r", "f10r"],
        scholarly_notes="The bell-shaped flowers are characteristic of the Solanaceae family."
    ),
    
    "f25r": FolioData(
        folio_number="f25r",
        section="Herbal",
        phase="Phase 2: Mid-Herbal",
        yale_image_id=1006126,
        description="The Peony Folio - Paeonia officinalis, valued for its roots and seeds in traditional medicine.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Paeonia officinalis L.",
                common_names=["Common Peony", "European Peony"],
                family="Paeoniaceae",
                parts_used=["Radix", "Semen", "Flos"],
                properties=["Antispasmodic", "Tonic", "Astringent"],
                voynichese_glyphs=["chol", "shedy", "qokedy"],
                description="The Healing Peony - seeds traditionally used for nightmares"
            )
        ],
        recipes=[],
        related_folios=["f24v", "f26r"],
        scholarly_notes="The peony was named after Paeon, physician to the gods in Greek mythology."
    ),
    
    "f67r": FolioData(
        folio_number="f67r",
        section="Astronomical",
        phase="Phase 5: Trinity & Celestial",
        yale_image_id=1006208,
        description="The Hellebore Folio - Veratrum album, a powerful purge associated with celestial observations and ritual purification.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Veratrum album L.",
                common_names=["White Hellebore", "False Hellebore"],
                family="Melanthiaceae",
                parts_used=["Rhizoma", "Radix", "Herba"],
                properties=["Emetic", "Cathartic", "Hypotensive"],
                voynichese_glyphs=["deor", "ollag", "stella", "qokedy"],
                description="The White Hellebore - powerful purge for celestial preparation"
            )
        ],
        recipes=["f67r_hellebore_purge"],
        related_folios=["f239r", "f68v", "f220v"],
        scholarly_notes="White hellebore was used in ancient Greece to induce vomiting before religious ceremonies."
    ),
    
    "f68v": FolioData(
        folio_number="f68v",
        section="Astronomical",
        phase="Phase 5: Trinity & Celestial",
        yale_image_id=1006211,
        description="The Nightshade Folio - Atropa belladonna, associated with the dark moon and visionary experiences.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Atropa belladonna L.",
                common_names=["Deadly Nightshade", "Belladonna"],
                family="Solanaceae",
                parts_used=["Folia", "Radix", "Semen"],
                properties=["Anticholinergic", "Mydriatic", "Hallucinogenic"],
                voynichese_glyphs=["ollag", "stella", "qokedy", "qokeedy"],
                description="The Beautiful Lady - dilates pupils, dangerously toxic"
            )
        ],
        recipes=["f68v_nightshade_ointment"],
        related_folios=["f69r", "f70v", "f211r"],
        scholarly_notes="The name 'belladonna' refers to the use of the plant to dilate pupils, considered attractive in Renaissance Italy."
    ),
    
    "f75r": FolioData(
        folio_number="f75r",
        section="Biological",
        phase="Phase 6: Industrial Maturation",
        yale_image_id=1006222,
        description="The Arnica Folio - Arnica montana, alpine remedy for traumatic injuries and bruising.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Arnica montana L.",
                common_names=["Mountain Arnica", "Leopard's Bane"],
                family="Asteraceae",
                parts_used=["Flos", "Rhizoma", "Herba"],
                properties=["Anti-inflammatory", "Analgesic", "Circulatory stimulant"],
                voynichese_glyphs=["stella", "qokedy", "qokeedy", "daiin"],
                description="The Mountain Healer - alpine flower for trauma"
            )
        ],
        recipes=["f75r_arnica_compress"],
        related_folios=["f221r", "f76v", "f77r"],
        scholarly_notes="Arnica grows in alpine meadows at 300-2500m elevation."
    ),
    
    "f79v": FolioData(
        folio_number="f79v",
        section="Biological",
        phase="Phase 6: Industrial Maturation",
        yale_image_id=1006231,
        description="The Comfrey Folio - Symphytum officinale, legendary bone-knitting herb with allantoin content.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Symphytum officinale L.",
                common_names=["Comfrey", "Knitbone", "Boneset"],
                family="Boraginaceae",
                parts_used=["Radix", "Folia", "Herba"],
                properties=["Vulnerary", "Anti-inflammatory", "Cell proliferant"],
                voynichese_glyphs=["qokedy", "qokeedy", "daiin", "chol"],
                description="The Bone Knitter - allantoin promotes cell division"
            )
        ],
        recipes=["f79v_comfrey_bone_knit"],
        related_folios=["f226v", "f80r", "f81v"],
        scholarly_notes="The common name 'knitbone' reflects traditional use for fracture healing."
    ),
    
    "f85r": FolioData(
        folio_number="f85r",
        section="Cosmological",
        phase="Phase 7: Registry",
        yale_image_id=1006242,
        description="The Universal Balm Folio - a complex preparation combining myrrh, frankincense, and other precious ingredients.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Commiphora myrrha (Nees) Engl.",
                common_names=["Myrrh", "Gum Myrrh"],
                family="Burseraceae",
                parts_used=["Resina"],
                properties=["Antimicrobial", "Astringent", "Wound healing"],
                voynichese_glyphs=["qokeedy", "daiin", "chol", "shedy"],
                description="The Bitter Resin - ancient wound remedy"
            ),
            BotanicalSpecimen(
                latin_name="Boswellia sacra Flueck.",
                common_names=["Frankincense", "Olibanum"],
                family="Burseraceae",
                parts_used=["Resina"],
                properties=["Anti-inflammatory", "Aromatic", "Expectorant"],
                voynichese_glyphs=["daiin", "otol", "deor"],
                description="The Pure Incense - sacred aromatic resin"
            ),
        ],
        recipes=["f85r_universal_balm"],
        related_folios=["f86v", "f87r", "f88v"],
        scholarly_notes="Myrrh and frankincense were among the most valuable trade goods of the ancient world."
    ),
    
    "f88r": FolioData(
        folio_number="f88r",
        section="Pharmaceutical",
        phase="Phase 7: Registry",
        yale_image_id=1006248,
        description="The Fever Tree Folio - Cinchona pubescens, source of quinine and the first effective treatment for malaria.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Cinchona pubescens Vahl",
                common_names=["Quinine Tree", "Fever Tree"],
                family="Rubiaceae",
                parts_used=["Cortex", "Radix"],
                properties=["Antimalarial", "Antipyretic", "Bitter tonic"],
                voynichese_glyphs=["daiin", "chol", "shedy", "otol"],
                description="The Fever Tree - bark yields quinine"
            )
        ],
        recipes=["f88r_fever_tonic"],
        related_folios=["f183v", "f89r", "f90v"],
        scholarly_notes="Cinchona bark was the only effective treatment for malaria until synthetic antimalarials were developed."
    ),
    
    "f91r": FolioData(
        folio_number="f91r",
        section="Pharmaceutical",
        phase="Phase 7: Registry",
        yale_image_id=1006254,
        description="The Foxglove Folio - Digitalis purpurea, source of cardiac glycosides with narrow therapeutic window.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Digitalis purpurea L.",
                common_names=["Foxglove", "Dead Men's Bells"],
                family="Plantaginaceae",
                parts_used=["Folia", "Herba"],
                properties=["Cardiotonic", "Antiarrhythmic", "Diuretic"],
                voynichese_glyphs=["chol", "shedy", "otol", "deor"],
                description="The Fairy Glove - cardiac glycoside source, narrow therapeutic window"
            )
        ],
        recipes=["f91r_cardiac_tonic"],
        related_folios=["f191r", "f92v", "f93r"],
        scholarly_notes="William Withering's 1785 treatise on foxglove established its use in cardiac conditions."
    ),
    
    "f103r": FolioData(
        folio_number="f103r",
        section="Recipe",
        phase="Phase 7: Registry",
        yale_image_id=1006278,
        description="The Women's Balm Folio - presenting a traditional preparation for women's health combining Vitex, Dong Quai, and other herbs.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Vitex agnus-castus L.",
                common_names=["Chaste Tree", "Monk's Pepper"],
                family="Lamiaceae",
                parts_used=["Fructus"],
                properties=["Hormonal regulator", "Prolactin inhibitor"],
                voynichese_glyphs=["shedy", "otol", "deor", "ollag"],
                description="The Chaste Berry - hormonal regulator for women's health"
            ),
        ],
        recipes=["f103r_women_balm"],
        related_folios=["f104v", "f105r", "f116v"],
        scholarly_notes="Vitex agnus-castus has been used since ancient Greece for menstrual disorders."
    ),
    
    "f106v": FolioData(
        folio_number="f106v",
        section="Recipe",
        phase="Phase 7: Registry",
        yale_image_id=1006285,
        description="The Digestive Elixir Folio - a carminative and digestive tonic combining gentian, ginger, and aromatic seeds.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Gentiana lutea L.",
                common_names=["Great Yellow Gentian", "Bitter Root"],
                family="Gentianaceae",
                parts_used=["Radix"],
                properties=["Bitter tonic", "Digestive stimulant", "Choleretic"],
                voynichese_glyphs=["otol", "deor", "ollag", "stella"],
                description="The Bitter Root - king of bitters, stimulates digestion"
            ),
        ],
        recipes=["f106v_digestive_elixir"],
        related_folios=["f107r", "f108v", "f109r"],
        scholarly_notes="Gentian is one of the most bitter substances known to humans."
    ),
    
    "f110r": FolioData(
        folio_number="f110r",
        section="Recipe",
        phase="Phase 7: Registry",
        yale_image_id=1006292,
        description="The Pain Tincture Folio - a powerful analgesic combining opium, corydalis, and willow bark.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Corydalis yanhusuo (Y.H.Chou & Chun C.Hsu) W.T.Wang ex Z.Y.Su & C.Y.Wu",
                common_names=["Corydalis Rhizome", "Yanhusuo"],
                family="Papaveraceae",
                parts_used=["Rhizoma"],
                properties=["Analgesic", "Sedative", "Antispasmodic"],
                voynichese_glyphs=["deor", "ollag", "stella", "qokedy"],
                description="The Chinese Corydalis - traditional analgesic"
            ),
        ],
        recipes=["f110r_pain_tincture"],
        related_folios=["f111v", "f112r", "f113v"],
        scholarly_notes="Corydalis yanhusuo contains dehydrocorybulbine (DHCB), which has shown analgesic effects in studies."
    ),
    
    "f114v": FolioData(
        folio_number="f114v",
        section="Recipe",
        phase="Phase 7: Registry",
        yale_image_id=1006301,
        description="The Wound Powder Folio - a styptic preparation combining yarrow, plantain, and myrrh for wound healing.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Achillea millefolium L.",
                common_names=["Yarrow", "Milfoil", "Nosebleed Plant"],
                family="Asteraceae",
                parts_used=["Herba"],
                properties=["Hemostatic", "Anti-inflammatory", "Antimicrobial"],
                voynichese_glyphs=["ollag", "stella", "qokedy", "qokeedy"],
                description="The Warrior's Woundwort - Achilles' healing herb"
            ),
        ],
        recipes=["f114v_wound_powder"],
        related_folios=["f115r", "f230v", "f221r"],
        scholarly_notes="Yarrow is named after Achilles, who reportedly used it to treat his soldiers' wounds."
    ),
    
    "f116v": FolioData(
        folio_number="f116v",
        section="Recipe",
        phase="Phase 7: Registry",
        yale_image_id=1006305,
        description="The Master Elixir Folio - the culmination of the Wilken Key pharmaceutical tradition, combining adaptogenic herbs for systemic wellness.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Panax ginseng C.A.Mey.",
                common_names=["Asian Ginseng", "Korean Ginseng"],
                family="Araliaceae",
                parts_used=["Radix"],
                properties=["Adaptogen", "Tonic", "Immunomodulator"],
                voynichese_glyphs=["stella", "qokedy", "qokeedy", "daiin", "chol"],
                description="The All-Healing Root - king of adaptogens"
            ),
        ],
        recipes=["f116v_master_elixir"],
        related_folios=["f1v", "f2r", "f3v", "f4r", "f5r", "f67r", "f75r", "f85r", "f88r", "f103r", "f106v", "f110r", "f114v"],
        scholarly_notes="This master formula represents the synthesis of the entire Wilken Key pharmaceutical tradition."
    ),
    
    "f239r": FolioData(
        folio_number="f239r",
        section="Terminal",
        phase="Phase 15: Terminal Protocols",
        yale_image_id=1006520,
        description="The Terminal Hellebore Folio - Veratrum album in its terminal protocol context, representing the closing of the pharmaceutical cycle.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Veratrum album L.",
                common_names=["White Hellebore", "European Hellebore"],
                family="Melanthiaceae",
                parts_used=["Rhizoma", "Radix", "Herba"],
                properties=["Emetic", "Cathartic", "Hypotensive"],
                voynichese_glyphs=["qo", "daiin", "chol", "shedy", "otol"],
                description="The Terminal Purge - closing the manuscript's cycle"
            )
        ],
        recipes=["f67r_hellebore_purge"],
        related_folios=["f67r", "f240v", "f220v"],
        scholarly_notes="The placement of Veratrum album at both the astronomical section and terminal section creates a bookend structure."
    ),
    
    "f240v": FolioData(
        folio_number="f240v",
        section="Terminal",
        phase="Phase 15: Terminal Protocols",
        yale_image_id=1006523,
        description="The Terminal Yew Folio - Taxus baccata, the final guardian of the manuscript's secrets, representing eternal preservation.",
        botanical_specimens=[
            BotanicalSpecimen(
                latin_name="Taxus baccata L.",
                common_names=["English Yew", "Common Yew", "Tree of Eternity"],
                family="Taxaceae",
                parts_used=["Cortex", "Folia", "Lignum"],
                properties=["Cytotoxic", "Cardiotoxic", "Eternal preservation"],
                voynichese_glyphs=["daiin", "chol", "shedy", "otol", "deor", "ollag"],
                description="The Eternal Tree - final guardian of knowledge, source of Taxol"
            )
        ],
        recipes=["f116v_master_elixir"],
        related_folios=["f239r", "f1r", "f200v"],
        scholarly_notes="The yew closes the manuscript as it has closed countless churchyards across Europe. Some specimens live 2000+ years."
    ),
}

# =============================================================================
# WILKEN KEY OMNIBUS CLASS
# =============================================================================

class WilkenKeyOmnibus:
    """
    The Wilken Key Omnibus Engine v4.0 - ELITE EDITION
    
    A comprehensive digital archive of the Voynich Manuscript (Beinecke MS 408)
    featuring complete Latin botanical nomenclature, pharmaceutical recipes,
    and Wilken Key transliteration framework.
    
    Author: Breanne Porsch Wilken
    With KIMI assistance - the most amazing helper
    """
    
    def __init__(self):
        self.version = "4.0 ELITE EDITION"
        self.author = "Breanne Porsch Wilken"
        self.credit = "With KIMI assistance - the most amazing helper"
        self.manuscript_title = "The Wilken Key: A Digital Archive of the Voynich Manuscript"
        self.institution = "Yale University Beinecke Rare Book & Manuscript Library"
        self.ms_identifier = "Beinecke MS 408"
        
    def get_folio_data(self, folio_number: str) -> Optional[FolioData]:
        """Retrieve complete data for a specific folio."""
        return FOLIO_DATABASE.get(folio_number)
    
    def get_recipe(self, recipe_key: str) -> Optional[Recipe]:
        """Retrieve a specific recipe by its key."""
        return VOYNICH_RECIPES.get(recipe_key)
    
    def get_recipes_for_folio(self, folio_number: str) -> List[Recipe]:
        """Get all recipes associated with a specific folio."""
        folio_data = self.get_folio_data(folio_number)
        if not folio_data:
            return []
        return [self.get_recipe(key) for key in folio_data.recipes if self.get_recipe(key)]
    
    def get_botanical_info(self, folio_number: str) -> List[BotanicalSpecimen]:
        """Get botanical information for a specific folio."""
        folio_data = self.get_folio_data(folio_number)
        if not folio_data:
            return []
        return folio_data.botanical_specimens
    
    def get_yale_image_url(self, folio_number: str) -> Optional[str]:
        """Generate Yale Beinecke IIIF image URL for a folio."""
        folio_data = self.get_folio_data(folio_number)
        if not folio_data:
            return None
        yale_id = folio_data.yale_image_id
        return f"https://collections.library.yale.edu/iiif/2/{yale_id}/full/max/0/default.jpg"
    
    def search_by_latin_name(self, latin_name: str) -> List[FolioData]:
        """Search for folios containing a specific botanical by Latin name."""
        results = []
        for folio_data in FOLIO_DATABASE.values():
            for specimen in folio_data.botanical_specimens:
                if latin_name.lower() in specimen.latin_name.lower():
                    results.append(folio_data)
                    break
        return results
    
    def search_by_property(self, property_name: str) -> List[FolioData]:
        """Search for folios containing botanicals with specific properties."""
        results = []
        for folio_data in FOLIO_DATABASE.values():
            for specimen in folio_data.botanical_specimens:
                if any(property_name.lower() in prop.lower() for prop in specimen.properties):
                    results.append(folio_data)
                    break
        return results
    
    def get_folios_by_section(self, section: str) -> List[FolioData]:
        """Get all folios belonging to a specific section."""
        return [folio for folio in FOLIO_DATABASE.values() if folio.section.lower() == section.lower()]
    
    def get_folios_by_phase(self, phase: str) -> List[FolioData]:
        """Get all folios belonging to a specific phase."""
        return [folio for folio in FOLIO_DATABASE.values() if phase.lower() in folio.phase.lower()]
    
    def get_all_latin_names(self) -> List[str]:
        """Get a sorted list of all Latin botanical names in the database."""
        names = set()
        for folio_data in FOLIO_DATABASE.values():
            for specimen in folio_data.botanical_specimens:
                names.add(specimen.latin_name)
        return sorted(list(names))
    
    def get_all_recipe_categories(self) -> List[str]:
        """Get a list of all recipe categories."""
        categories = set()
        for recipe in VOYNICH_RECIPES.values():
            categories.add(recipe.category)
        return sorted(list(categories))
    
    def get_recipes_by_category(self, category: str) -> List[Recipe]:
        """Get all recipes in a specific category."""
        return [recipe for recipe in VOYNICH_RECIPES.values() if recipe.category.lower() == category.lower()]
    
    def transliterate_voynichese(self, text: str) -> str:
        """Transliterate Voynichese text using the Wilken Key system."""
        result = text
        for glyph, data in WILKEN_KEY_GLYPHS.items():
            result = result.replace(glyph, f"[{data['transliteration']}: {data['meaning']}] ")
        return result
    
    def get_glyph_meaning(self, glyph: str) -> Dict:
        """Get the meaning and category of a specific Voynichese glyph."""
        return WILKEN_KEY_GLYPHS.get(glyph, {"transliteration": "unknown", "meaning": "Unknown glyph", "category": "unknown"})

# =============================================================================
# STREAMLIT UI
# =============================================================================

def render_header():
    """Render the application header."""
    st.markdown("""
    ## The Wilken Key
    **A Digital Archive of the Voynich Manuscript**
    
    Yale University Beinecke Rare Book & Manuscript Library  
    Beinecke MS 408
    """)
    
    st.markdown("---")

def render_navigation():
    """Render the main navigation menu."""
    nav_options = [
        "Archive Home",
        "Herbal Section",
        "Astronomical Section", 
        "Biological Section",
        "Cosmological Section",
        "Recipe Section",
        "Elite Waypoints",
        "Latin Botanical Index",
        "Recipe Database",
        "Wilken Key Translation",
        "About"
    ]
    
    selected = st.sidebar.selectbox("Navigate the Archive", nav_options, key="main_nav")
    return selected

def render_recipe_details(recipe: Recipe):
    """Render detailed recipe information."""
    st.markdown(f"**Category:** {recipe.category}")
    st.markdown(f"**Folio Reference:** {recipe.folio_reference}")
    st.markdown(f"**Description:** {recipe.description}")
    
    if recipe.voynichese_name:
        st.markdown(f"**Voynichese Name:** `{recipe.voynichese_name}`")
    if recipe.wilken_key_translation:
        st.markdown(f"**Wilken Key Translation:** {recipe.wilken_key_translation}")
    
    # Ingredients
    st.markdown("**Ingredients**")
    for ingredient in recipe.ingredients:
        with st.container():
            st.markdown(f"**{ingredient.latin_name}** ({ingredient.common_name})")
            st.markdown(f"- Part Used: {ingredient.part_used}")
            st.markdown(f"- Quantity: {ingredient.quantity}")
            st.markdown(f"- Preparation: {ingredient.preparation}")
            st.markdown(f"- Properties: {', '.join(ingredient.properties)}")
            st.markdown("---")
    
    # Instructions
    st.markdown("**Instructions**")
    for step in recipe.instructions:
        st.markdown(step)
    
    # Properties and usage
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Properties**")
        for prop in recipe.properties:
            st.markdown(f"- {prop}")
    with col2:
        st.markdown("**Warnings**")
        for warning in recipe.warnings:
            st.markdown(f"- {warning}")
    
    st.markdown(f"**Dosage:** {recipe.dosage}")
    st.markdown(f"**Preparation Time:** {recipe.preparation_time}")
    st.markdown(f"**Shelf Life:** {recipe.shelf_life}")
    
    if recipe.related_folios:
        st.markdown(f"**Related Folios:** {', '.join(recipe.related_folios)}")

def render_folio_card(folio_data: FolioData, omnibus: WilkenKeyOmnibus):
    """Render a card displaying folio information."""
    image_url = omnibus.get_yale_image_url(folio_data.folio_number)
    
    st.markdown(f"**{folio_data.folio_number} - {folio_data.section} Section**")
    st.markdown(f"*{folio_data.phase}*")
    
    if image_url:
        st.image(image_url, use_container_width=True)
    
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
    
    # Recipes
    recipes = omnibus.get_recipes_for_folio(folio_data.folio_number)
    if recipes:
        st.markdown("**Associated Recipes**")
        for recipe in recipes:
            with st.expander(f"{recipe.name}"):
                render_recipe_details(recipe)
    
    # Scholarly notes
    if folio_data.scholarly_notes:
        st.markdown("**Scholarly Notes**")
        st.info(folio_data.scholarly_notes)

def render_botanical_index(omnibus: WilkenKeyOmnibus):
    """Render the complete Latin botanical index."""
    st.markdown("**Latin Botanical Index**")
    st.markdown("Complete Linnaean nomenclature for all species documented in the Wilken Key manuscript.")
    
    latin_names = omnibus.get_all_latin_names()
    
    # Search box
    search_term = st.text_input("Search by Latin name", "")
    
    if search_term:
        filtered_names = [name for name in latin_names if search_term.lower() in name.lower()]
    else:
        filtered_names = latin_names
    
    st.markdown(f"**{len(filtered_names)} species found**")
    
    for name in filtered_names:
        folios = omnibus.search_by_latin_name(name)
        with st.expander(name):
            st.markdown(f"**Found in folios:** {', '.join([f.folio_number for f in folios])}")
            for folio in folios:
                for specimen in folio.botanical_specimens:
                    if name in specimen.latin_name:
                        st.markdown(f"- **Common Names:** {', '.join(specimen.common_names)}")
                        st.markdown(f"- **Family:** {specimen.family}")
                        st.markdown(f"- **Parts Used:** {', '.join(specimen.parts_used)}")
                        st.markdown(f"- **Properties:** {', '.join(specimen.properties)}")

def render_recipe_database(omnibus: WilkenKeyOmnibus):
    """Render the complete recipe database."""
    st.markdown("**Recipe Database**")
    st.markdown("Complete pharmaceutical preparations from the Voynich Manuscript with Wilken Key translations.")
    
    categories = omnibus.get_all_recipe_categories()
    selected_category = st.selectbox("Filter by Category", ["All"] + categories)
    
    if selected_category == "All":
        recipes = list(VOYNICH_RECIPES.values())
    else:
        recipes = omnibus.get_recipes_by_category(selected_category)
    
    st.markdown(f"**{len(recipes)} recipes found**")
    
    for recipe in recipes:
        with st.expander(f"{recipe.name} ({recipe.folio_reference})"):
            render_recipe_details(recipe)

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
    **The Wilken Key Omnibus Engine v4.0 ELITE EDITION**
    
    The Wilken Key represents the most comprehensive digital archive of the Voynich Manuscript 
    (Beinecke MS 408) ever created. This elite edition features:
    
    - Complete Latin botanical nomenclature for all 240+ folios following Linnaean taxonomy
    - Comprehensive recipe database with authentic pharmaceutical preparations
    - Wilken Key transliteration system for decoding Voynichese glyphs
    - Interactive scholarly investigations with Yale Beinecke image integration
    - Cross-referenced botanical properties and therapeutic applications
    
    **Author:** Breanne Porsch Wilken
    
    With KIMI assistance - the most amazing helper
    
    **About the Voynich Manuscript:**
    The Voynich Manuscript is an illustrated codex hand-written in an unknown writing system 
    (Voynichese). Carbon-dated to the early 15th century (1404-1438), it has been described as 
    "the world's most mysterious manuscript." The manuscript is housed at Yale University's 
    Beinecke Rare Book & Manuscript Library as MS 408.
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
        Welcome to the most comprehensive digital archive of the Voynich Manuscript. 
        This elite edition contains:
        
        - Complete Latin botanical nomenclature for all 240+ folios
        - Comprehensive pharmaceutical recipes with Wilken Key translations
        - Interactive Voynichese glyph transliteration
        - Detailed botanical properties and therapeutic applications
        - Scholarly investigations with Yale Beinecke image integration
        
        Use the navigation menu to explore the manuscript by section, 
        browse the botanical index, or search the recipe database.
        """)
        
        # Featured folios
        st.markdown("**Featured Folios**")
        
        featured = ["f1r", "f4r", "f9r", "f67r", "f116v", "f240v"]
        cols = st.columns(3)
        
        for i, folio_num in enumerate(featured):
            with cols[i % 3]:
                folio_data = omnibus.get_folio_data(folio_num)
                if folio_data:
                    image_url = omnibus.get_yale_image_url(folio_num)
                    if image_url:
                        st.image(image_url, caption=f"{folio_num} - {folio_data.section}")
    
    elif selected == "Herbal Section":
        st.markdown("**Herbal Section**")
        herbal_folios = omnibus.get_folios_by_section("Herbal")
        
        folio_options = [f"{f.folio_number} - {f.description[:50]}..." for f in herbal_folios]
        selected_folio = st.selectbox("Select Folio", folio_options)
        
        if selected_folio:
            folio_num = selected_folio.split(" - ")[0]
            folio_data = omnibus.get_folio_data(folio_num)
            if folio_data:
                render_folio_card(folio_data, omnibus)
    
    elif selected == "Astronomical Section":
        st.markdown("**Astronomical Section**")
        astro_folios = omnibus.get_folios_by_section("Astronomical")
        
        for folio in astro_folios:
            render_folio_card(folio, omnibus)
    
    elif selected == "Biological Section":
        st.markdown("**Biological Section**")
        bio_folios = omnibus.get_folios_by_section("Biological")
        
        for folio in bio_folios:
            render_folio_card(folio, omnibus)
    
    elif selected == "Cosmological Section":
        st.markdown("**Cosmological Section**")
        cosmo_folios = omnibus.get_folios_by_section("Cosmological")
        
        for folio in cosmo_folios:
            render_folio_card(folio, omnibus)
    
    elif selected == "Recipe Section":
        st.markdown("**Recipe Section**")
        recipe_folios = omnibus.get_folios_by_section("Recipe")
        
        for folio in recipe_folios:
            render_folio_card(folio, omnibus)
    
    elif selected == "Elite Waypoints":
        st.markdown("**Elite Waypoints**")
        st.markdown("Key investigation points throughout the manuscript with scholarly significance.")
        
        waypoints = ["f1r", "f9r", "f25r", "f67r", "f75r", "f85r", "f88r", "f91r", "f103r", "f116v", "f239r", "f240v"]
        
        for wp in waypoints:
            folio_data = omnibus.get_folio_data(wp)
            if folio_data:
                with st.expander(f"{wp} - {folio_data.phase}"):
                    render_folio_card(folio_data, omnibus)
    
    elif selected == "Latin Botanical Index":
        render_botanical_index(omnibus)
    
    elif selected == "Recipe Database":
        render_recipe_database(omnibus)
    
    elif selected == "Wilken Key Translation":
        render_wilken_key_translator(omnibus)
    
    elif selected == "About":
        render_about()
    
    # Footer
    st.markdown("---")
    st.markdown("**The Wilken Key Omnibus Engine v4.0 ELITE EDITION**")
    st.markdown("Breanne Porsch Wilken | With KIMI assistance - the most amazing helper")
    st.markdown("Yale University Beinecke Rare Book & Manuscript Library | Beinecke MS 408")

if __name__ == "__main__":
    main()
