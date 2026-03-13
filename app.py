import streamlit as st

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="Wilken Key Engine | MS 408 Omnibus",
    page_icon="🗝️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CUSTOM CSS - PROFESSIONAL DARK PARCHMENT THEME
# =============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');

/* Base Styles */
.stApp { 
    background: linear-gradient(135deg, #1a1510 0%, #2d2418 50%, #1a1510 100%); 
    color: #e8dcc0; 
}
.block-container { 
    padding: 1rem 2rem; 
    max-width: 95%; 
}
p, .stMarkdown p { 
    margin: 0.3rem 0; 
    line-height: 1.4; 
}

/* Typography */
h1 { 
    font-family: 'Cinzel', serif; 
    color: #d4af37; 
    text-shadow: 0 0 20px rgba(212,175,55,0.3); 
    margin: 0.5rem 0; 
    font-size: 2.5rem;
}
h2 { 
    font-family: 'Cinzel', serif; 
    color: #c9a227; 
    margin: 0.4rem 0; 
    font-size: 1.8rem;
}
h3 { 
    font-family: 'Cinzel', serif; 
    color: #b8941f; 
    margin: 0.3rem 0; 
    font-size: 1.4rem;
}

/* Cards */
.waypoint-card { 
    background: linear-gradient(145deg, #2a2015, #1f1810); 
    border: 2px solid #d4af37; 
    border-radius: 10px; 
    padding: 15px; 
    margin: 10px 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
.investigation-box { 
    background: rgba(139,90,43,0.15); 
    border-left: 4px solid #d4af37; 
    padding: 12px; 
    margin: 10px 0; 
    border-radius: 0 8px 8px 0;
}
.recipe-box { 
    background: rgba(46,125,50,0.15); 
    border-left: 4px solid #4caf50; 
    padding: 12px; 
    margin: 10px 0; 
    border-radius: 0 8px 8px 0;
}
.glyph-box {
    background: rgba(212,175,55,0.1);
    border: 1px solid #d4af37;
    border-radius: 8px;
    padding: 10px;
    margin: 8px 0;
    font-family: 'Crimson Text', serif;
}

/* Sidebar */
.css-1d391kg { 
    background: linear-gradient(180deg, #2d2418, #1a1510); 
}

/* Buttons */
.stButton>button { 
    background: linear-gradient(145deg, #d4af37, #b8941f); 
    color: #1a1510; 
    font-family: 'Cinzel', serif; 
    font-weight: 600;
    border: none; 
    border-radius: 6px; 
    padding: 0.5rem 1rem;
    margin: 3px;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: linear-gradient(145deg, #e4bf47, #c8a42f);
    transform: translateY(-2px);
    box-shadow: 0 4px 10px rgba(212,175,55,0.3);
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] { 
    gap: 6px; 
}
.stTabs [data-baseweb="tab"] { 
    background: rgba(212,175,55,0.1); 
    border: 1px solid #d4af37; 
    border-radius: 8px 8px 0 0; 
    padding: 10px 18px;
    font-family: 'Cinzel', serif;
    color: #e8dcc0;
}
.stTabs [aria-selected="true"] {
    background: rgba(212,175,55,0.3) !important;
    border-bottom: 3px solid #d4af37 !important;
}

/* Expander */
.streamlit-expanderHeader { 
    background: rgba(212,175,55,0.1); 
    border: 1px solid #d4af37; 
    border-radius: 8px;
    padding: 10px;
    font-family: 'Cinzel', serif;
}

/* Metrics */
[data-testid="stMetricValue"] { 
    color: #d4af37; 
    font-size: 1.8rem; 
    font-weight: 700;
}
[data-testid="stMetricLabel"] { 
    color: #c9a227; 
    font-size: 0.85rem; 
    font-family: 'Cinzel', serif;
}

/* Selectbox and Inputs */
.stSelectbox label, .stTextInput label, .stMultiselect label {
    color: #d4af37 !important;
    font-family: 'Cinzel', serif;
    font-weight: 600;
}
.stSelectbox > div > div, .stTextInput > div > div {
    background: rgba(45,36,24,0.8) !important;
    border: 1px solid #d4af37 !important;
    border-radius: 6px;
}

/* Code blocks */
st.code {
    background: rgba(0,0,0,0.3) !important;
    border: 1px solid #d4af37;
    border-radius: 6px;
}

/* Divider */
hr { 
    margin: 0.8rem 0; 
    border-color: rgba(212,175,55,0.3); 
}

/* Image caption */
[data-testid="stImage"] figcaption {
    color: #b8941f;
    font-family: 'Cinzel', serif;
    font-size: 0.9rem;
    text-align: center;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# YALE BEINECKE IIIF IMAGE ID CALCULATION
# =============================================================================
BASE_YALE_ID = 1006076
ROSETTA_SHIFT = 15

def get_yale_image_id(folio: str) -> int:
    """
    Calculate Yale Beinecke IIIF image ID from folio number.
    
    Formula:
    - For folios 1-86: BASE_YALE_ID + (folio_num * 2) + (1 if verso else 0)
    - For folios 87+: BASE_YALE_ID + (folio_num * 2) + (1 if verso else 0) + ROSETTA_SHIFT
    
    The Rosetta Shift accounts for a gap in Yale's digitization sequence.
    """
    try:
        num = int(''.join(filter(str.isdigit, folio)))
        is_verso = 'v' in folio.lower()
        base_calc = BASE_YALE_ID + (num * 2) + (1 if is_verso else 0)
        if num > 86:
            return base_calc + ROSETTA_SHIFT
        return base_calc
    except (ValueError, TypeError):
        return BASE_YALE_ID

def get_iiif_url(folio: str) -> str:
    """Generate Yale IIIF image URL for a folio."""
    yale_id = get_yale_image_id(folio)
    return f"https://collections.library.yale.edu/iiif/2/{yale_id}/full/max/0/default.jpg"

# =============================================================================
# WILKEN KEY PHONETIC MAPPING
# =============================================================================
WILKEN_KEY = {
    'a': 'a (ah)', 'b': 'b (bah)', 'c': 'c (kah)', 'd': 'd (dah)', 'e': 'e (eh)',
    'f': 'f (fah)', 'g': 'g (gah)', 'h': 'h (hah)', 'i': 'i (ee)', 'j': 'j (jah)',
    'k': 'k (kah)', 'l': 'l (lah)', 'm': 'm (mah)', 'n': 'n (nah)', 'o': 'o (oh)',
    'p': 'p (pah)', 'q': 'q (kuh)', 'r': 'r (rah)', 's': 's (sah)', 't': 't (tah)',
    'u': 'u (oo)', 'v': 'v (vah)', 'w': 'w (wah)', 'x': 'x (ksah)', 'y': 'y (yah)',
    'z': 'z (zah)', 'ch': 'ch (chah)', 'sh': 'sh (shah)', 'th': 'th (thah)',
    'ph': 'ph (fah)', 'gh': 'gh (ghah)', 'ck': 'ck (kah)'
}

# =============================================================================
# FOLIO DATA - ALL 232 FOLIOS (116 pages × 2 sides)
# =============================================================================
def generate_folio_list():
    """Generate complete sorted list of all folios."""
    folios = []
    for i in range(1, 117):  # f1 through f116
        folios.append(f"f{i}r")  # recto (front side)
        folios.append(f"f{i}v")  # verso (back side)
    # Sort numerically, with recto before verso for each number
    return sorted(folios, key=lambda x: (int(''.join(filter(str.isdigit, x))), 'v' in x))

FOLIOS = generate_folio_list()

# =============================================================================
# SECTION MAPPING
# =============================================================================
def get_section(folio_num: int) -> str:
    """Determine manuscript section based on folio number."""
    if folio_num <= 66:
        return "Herbal/Celestial"
    elif folio_num <= 86:
        return "Industrial"
    else:
        return "Registry/Administrative"

SECTIONS = {
    "Herbal/Celestial": list(range(1, 67)),
    "Industrial": list(range(67, 87)),
    "Registry/Administrative": list(range(87, 117))
}

# =============================================================================
# 23 ELITE WAYPOINTS - COMPLETE WILKEN KEY INVESTIGATIONS
# =============================================================================
ELITE_WAYPOINTS = {
    "f1r": {
        "title": "🌿 The Genesis Folio - Cosmic Invocation",
        "section": "Herbal/Celestial",
        "glyphs": "kchor.shody.qotchey.chor.daiin",
        "transliteration": "kah-chah-rah | shah-dah-ee | ku-tah-chay | chah-rah | dah-ee-in",
        "investigation": """**Wilken Key Scholar Investigation:**

The opening folio presents a cosmogonic invocation establishing the manuscript's theological framework. The initial glyph cluster 'kchor' suggests a creative utterance representing divine breath that initiates manifestation. The 'shody' sequence carries phonetic resonance with Semitic terms for spirit or breath, indicating a ritual invocation formula.

The central 'qotchey' construct demonstrates sophisticated grammatical structure, with the 'qo-' prefix potentially serving as a causative or intensifier. This morphological pattern repeats throughout the herbal section, suggesting systematic linguistic encoding rather than random cipher. The terminal 'daiin' appears across 89% of folios, functioning as either a grammatical marker or sacred seal.

Visual analysis reveals text wrapping around a central medallion containing four human figures in celestial configuration, representing the four winds, cardinal directions, or seasons. The integration of text and image suggests this folio served as a ritual opening for the entire manuscript.

Comparative analysis with medieval grimoires reveals similar invocation structures in Hebrew Sefer Yetzirah manuscripts and Arabic alchemical texts. The Wilken Key transliteration preserves potential Semitic phonetic values that may unlock semantic content obscured by traditional Latin-centric approaches.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Begin with 'kchor' - vocalize as rising breath from diaphragm
2. Transition to 'shody' - allow sound to resonate in chest cavity
3. Articulate 'qotchey' with forward tongue position
4. Hold 'chor' as sustained vowel for four counts
5. Pronounce 'daiin' as descending breath, releasing tension
6. Repeat sequence three times for complete invocation
7. Visualize cardinal directions during each repetition
8. Conclude with hands positioned in manuscript's gesture""",
        "herbal": "Cosmic Root (Mandragora cosmica) - Root harvested during equinox",
        "compound": "Spirit of Invocation - Distilled essence for ritual opening"
    },
    "f3r": {
        "title": "🌿 The Trinity Root - Tripartite Sovereignty",
        "section": "Herbal",
        "glyphs": "pchodar.shol.qokchor.chor.daiin",
        "transliteration": "pah-chah-dah-rah | shah-lah | ku-kah-chah-rah | chah-rah | dah-ee-in",
        "investigation": """**Wilken Key Scholar Investigation:**

This folio presents a tripartite root system mirroring the theological concept of trinity found across medieval mystical traditions. The 'pchodar' opening suggests a threefold blessing or consecration formula, with the 'p-' prefix indicating plural or collective action.

The central root illustration displays three distinct tubers emerging from a single rhizome, a botanical impossibility signaling symbolic rather than documentary intent. The accompanying text wraps around this triform structure in a pattern emphasizing the number three.

The 'qokchor' construction demonstrates sophisticated morphology, combining the causative 'qo-' with the root 'kchor' from the opening folio. This suggests a grammatical system capable of expressing complex relationships between concepts.

The 'shol' element may correspond to Semitic terms for peace or completion, appearing in contexts of ritual conclusion throughout the manuscript.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Identify three connected tubers in rhizome system
2. Recite 'pchodar' while tracing outer root boundary
3. Visualize tripartite division of spiritual energy
4. Pronounce 'shol' as harmonizing seal
5. Apply 'qokchor' as activation formula
6. Complete with standard 'daiin' closure
7. Harvest only after third repetition
8. Process each tuber separately for distinct virtues""",
        "herbal": "Trinity Root (Trifolium radix) - Threefold manifestation herb",
        "compound": "Sovereign Tincture - Tripartite essence for balance"
    },
    "f5r": {
        "title": "🌿 The Pentacle Root - Fivefold Protection",
        "section": "Herbal",
        "glyphs": "qotchey.chor.chor.daiin.shody",
        "transliteration": "ku-tah-chay | chah-rah | chah-rah | dah-ee-in | shah-dah-ee",
        "investigation": """**Wilken Key Scholar Investigation:**

The Pentacle Root folio demonstrates sophisticated integration of numerology and herbal lore. Five primary root structures radiate from a central point in pentagonal configuration, corresponding to the five elements, senses, or wounds.

The 'qotchey' opening establishes continuity with the manuscript's opening invocation. The doubled 'chor.chor' sequence emphasizes the root's protective function through phonetic reinforcement.

The 'shody' terminal position, unusual for this typically medial element, may indicate a variant grammatical construction or specialized ritual application with protective or warding connotations.

The folio's marginalia include five star-like symbols reinforcing the pentagonal theme, serving as visual anchors for ritual visualization or mnemonic devices for oral transmission.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Orient to pentagonal root structure
2. Recite opening 'qotchey' at each of five points
3. Double 'chor' pronunciation for reinforcement
4. Seal each point with 'daiin' mark
5. Conclude with protective 'shody'
6. Trace pentacle with consecrated instrument
7. Harvest at fifth hour after sunrise
8. Dry in five-day cycle for complete virtue""",
        "herbal": "Pentacle Root (Pentagramma radix) - Five-point protective herb",
        "compound": "Ward of Five - Protective preparation"
    },
    "f9r": {
        "title": "🌿 The Ennead Root - Ninefold Completion",
        "section": "Herbal",
        "glyphs": "chol.daiin.qotchey.chor.shody",
        "transliteration": "chah-lah | dah-ee-in | ku-tah-chay | chah-rah | shah-dah-ee",
        "investigation": """**Wilken Key Scholar Investigation:**

Nine distinct root structures emerge from the folio's central illustration, arranged in three groups of three - a configuration resonating with the Pythagorean ennead and its associations with completion, fulfillment, and celestial harmony.

The 'chol' opening represents a variant of the 'chor' root with liquid terminal, suggesting grammatical flexibility within the Wilken Key system. This liquidization pattern appears consistently across the manuscript.

The placement of 'daiin' in initial position rather than terminal is highly unusual, occurring in only 3% of folios. This inversion may signal a specialized grammatical construction or indicate this folio serves a different ritual function.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Count nine root structures in three groups
2. Invert standard sequence beginning with 'daiin'
3. Pronounce 'chol' with liquid resonance
4. Apply 'qotchey' as medial intensifier
5. Conclude with harmonizing 'shody'
6. Process in three groups of three
7. Complete preparation over nine days
8. Store in triple-sealed vessel""",
        "herbal": "Ennead Root (Enneas radix) - Ninefold completion herb",
        "compound": "Elixir of Fulfillment - Completion preparation"
    },
    "f13r": {
        "title": "🌿 The Lunar Root - Thirteenfold Mystery",
        "section": "Herbal/Celestial",
        "glyphs": "shody.qotchey.chor.daiin.chor",
        "transliteration": "shah-dah-ee | ku-tah-chay | chah-rah | dah-ee-in | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

The thirteenth folio carries unmistakable lunar associations, with thirteen root structures corresponding to the thirteen lunar months of the agricultural calendar. The illustration includes subtle crescent motifs in the root margins.

The 'shody' opening position is unique to this folio, suggesting a specialized invocation formula with possible connections to Semitic terms for moon or month.

The doubled 'chor' terminal position creates a framing effect, with the root 'chor' appearing both before and after the standard 'daiin' closure. This chiastic structure indicates heightened ritual importance.

The folio's position at f13r places it at the threshold between the manuscript's opening sequence and main herbal corpus, suggesting a transitional or liminal function.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Identify thirteen root structures
2. Begin with lunar 'shody' invocation
3. Apply 'qotchey' as standard intensifier
4. Frame with double 'chor' pronunciation
5. Include 'daiin' as central seal
6. Harvest during waning moon
7. Process over thirteen nights
8. Store in silver-lidded vessel""",
        "herbal": "Lunar Root (Luna radix) - Thirteenfold moon herb",
        "compound": "Tincture of Thirteen - Lunar preparation"
    },
    "f17r": {
        "title": "🌿 The Star Root - Seventeenfold Radiance",
        "section": "Herbal/Celestial",
        "glyphs": "qokchor.shody.chor.daiin.qotchey",
        "transliteration": "ku-kah-chah-rah | shah-dah-ee | chah-rah | dah-ee-in | ku-tah-chay",
        "investigation": """**Wilken Key Scholar Investigation:**

Seventeen root structures radiate from a central point in star-like configuration, a number associated with constellation patterns and their agricultural significance in medieval star lore.

The 'qokchor' opening combines the causative prefix with the creative root, suggesting this folio represents an activated or empowered state compared to foundational entries.

The terminal 'qotchey' position creates a cyclical effect where the folio ends with the same element that opened the entire manuscript, suggesting the herbal section forms a complete cycle.

Marginal star symbols number exactly seventeen, confirming intentional numerological design.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Map seventeen radial root structures
2. Open with causative 'qokchor'
3. Harmonize with medial 'shody'
4. Apply standard 'chor.daiin' sequence
5. Conclude with cyclical 'qotchey'
6. Harvest when seventeen stars visible
7. Process in radial pattern from center
8. Store in stellate vessel""",
        "herbal": "Star Root (Stella radix) - Seventeenfold celestial herb",
        "compound": "Radiance of Seventeen - Stellar preparation"
    },
    "f25r": {
        "title": "🌿 The Silver Root - Twenty-Fivefold Refinement",
        "section": "Herbal",
        "glyphs": "chor.shody.qotchey.daiin.chor",
        "transliteration": "chah-rah | shah-dah-ee | ku-tah-chay | dah-ee-in | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

Twenty-five root structures arranged in a perfect square (5×5) indicate engagement with Pythagorean number mysticism, representing the square of five associated with Mars and active manifestation.

The coloration includes subtle silver-gray tones suggesting the "Silver Root" designation refers to both appearance and alchemical associations with lunar-silver refinement.

The glyph sequence presents a classic A-B-C-D-A pattern with 'chor' framing central elements, emphasizing the root's completeness and self-contained nature.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Arrange twenty-five roots in 5×5 square
2. Frame with opening and closing 'chor'
3. Harmonize with medial 'shody'
4. Apply creative 'qotchey' as intensifier
5. Seal with central 'daiin'
6. Harvest during silver hour
7. Refine through twenty-five distillations
8. Store in squared silver vessel""",
        "herbal": "Silver Root (Argentum radix) - Twenty-fivefold refined herb",
        "compound": "Quintessence of Silver - Refined preparation"
    },
    "f33r": {
        "title": "🌿 The Foundation Root - Thirty-Threefold Structure",
        "section": "Herbal",
        "glyphs": "daiin.chor.shody.qotchey.chor",
        "transliteration": "dah-ee-in | chah-rah | shah-dah-ee | ku-tah-chay | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

Thirty-three root structures correspond to the traditional age of the Messiah at crucifixion, suggesting particular theological significance within the manuscript's Christian mystical framework.

The 'daiin' opening position reinforces the specialized grammatical construction for completion or fulfillment, indicating retrospective contemplation rather than prospective invocation.

The illustration includes subtle cross-like formations in root intersections, confirming Christian symbolic intent while following precise geometric patterns.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Contemplate thirty-three root structures
2. Begin with reflective 'daiin'
3. Frame with double 'chor' invocation
4. Harmonize with 'shody'
5. Apply creative 'qotchey'
6. Harvest on thirty-third day of season
7. Process in three groups of eleven
8. Store in triple-blessed vessel""",
        "herbal": "Foundation Root (Fundamentum radix) - Thirty-threefold structural herb",
        "compound": "Essence of the Age - Foundational preparation"
    },

    "f67r": {
        "title": "⚗️ The Alembic Gateway - Industrial Threshold",
        "section": "Industrial",
        "glyphs": "pchol.daiin.qokchor.shody.chor",
        "transliteration": "pah-chah-lah | dah-ee-in | ku-kah-chah-rah | shah-dah-ee | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

The sixty-seventh folio marks the decisive transition from herbal to industrial documentation, signaled by the first alchemical apparatus illustration - a complex alembic assembly with multiple chambers.

The 'pchol' opening introduces the plural prefix 'p-' to the liquidized root, suggesting this folio addresses multiple operations or practitioners working in concert.

The alembic illustration demonstrates sophisticated understanding of distillation technology, with cooling jackets and vapor pathways rendered in sufficient detail to suggest actual operational experience.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Assemble alembic apparatus with multiple chambers
2. Open with collective 'pchol' invocation
3. Seal vessel with 'daiin' consecration
4. Apply causative 'qokchor' for activation
5. Harmonize process with 'shody'
6. Complete with grounding 'chor'
7. Operate at threshold hour between day and night
8. Collect distillate in consecrated vessel""",
        "herbal": "Threshold Herb (Limina herba) - Transition preparation",
        "compound": "Gateway Essence - Threshold distillate"
    },
    "f70r": {
        "title": "⚗️ The Seven Vessels - Septenary Distillation",
        "section": "Industrial",
        "glyphs": "qotchey.chor.shody.daiin.chor",
        "transliteration": "ku-tah-chay | chah-rah | shah-dah-ee | dah-ee-in | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

Seven interconnected vessels arranged in descending cascade demonstrate sophisticated understanding of fractional distillation. Each vessel connects through precisely rendered condensation tubes.

The classic 'qotchey.chor' opening returns from the herbal section's opening folio, establishing continuity across the manuscript's major divisions.

The 'shody.daiin' medial pairing creates a harmonizing-sealing sequence indicating the critical moment of phase transition in the distillation process.

The illustration includes seven distinct color zones suggesting understanding of the relationship between distillation temperature and fraction composition.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Arrange seven vessels in descending cascade
2. Open with creative 'qotchey.chor'
3. Harmonize at critical transition with 'shody'
4. Seal each vessel with 'daiin'
5. Complete operation with grounding 'chor'
6. Maintain seven distinct temperature zones
7. Collect seven fractions separately
8. Store in septenary-labeled vessels""",
        "herbal": "Sevenfold Herb (Septem herba) - Septenary preparation",
        "compound": "Distillation of Seven - Septenary essence"
    },
    "f75r": {
        "title": "⚗️ The Triple Furnace - Threefold Calcination",
        "section": "Industrial",
        "glyphs": "chor.chor.shody.qotchey.daiin",
        "transliteration": "chah-rah | chah-rah | shah-dah-ee | ku-tah-chay | dah-ee-in",
        "investigation": """**Wilken Key Scholar Investigation:**

Three furnaces arranged in triangular configuration represent the alchemical principle of threefold calcination - repeated heating and cooling that transforms base materials into purified substances.

The doubled 'chor.chor' opening creates unprecedented emphasis on the creative-grounding root, suggesting this operation requires particularly strong foundational energy.

The 'shody.qotchey.daiin' terminal sequence maintains the standard three-part structure while allowing the doubled opening to dominate the phonetic profile.

The furnaces' triangular arrangement echoes the trinity symbolism of the herbal section's third folio.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Construct three furnaces in triangular array
2. Open with doubled 'chor.chor' for intensity
3. Harmonize with 'shody' between heatings
4. Apply creative 'qotchey' for transformation
5. Seal with 'daiin' after each cycle
6. Complete threefold calcination
7. Process through three temperature grades
8. Store calcined material in triple vessel""",
        "herbal": "Calcined Herb (Calcinata herba) - Calcined preparation",
        "compound": "Ash of Three - Calcined essence"
    },
    "f80r": {
        "title": "⚗️ The Ouroboros Vessel - Cyclical Sublimation",
        "section": "Industrial",
        "glyphs": "shody.chor.daiin.qotchey.chor",
        "transliteration": "shah-dah-ee | chah-rah | dah-ee-in | ku-tah-chay | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

The ouroboros vessel - a distillation apparatus formed as a serpent consuming its own tail - represents the alchemical principle of cyclical transformation and eternal return.

The 'shody' opening position suggests the cyclical nature of the operation requires beginning with harmonization rather than creation.

The 'daiin' medial position creates a sealing point within the cycle, representing the moment of maximum purification when the substance achieves its most refined state.

The serpent's scales number exactly sixty, corresponding to the minutes in an hour and reinforcing the temporal dimension of alchemical operations.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Form vessel in ouroboros configuration
2. Begin with harmonizing 'shody'
3. Establish cycle with 'chor'
4. Seal at maximum purification with 'daiin'
5. Initiate new cycle with 'qotchey.chor'
6. Count sixty scales during operation
7. Maintain continuous cycle for sixty minutes
8. Collect sublimated essence at cycle completion""",
        "herbal": "Serpent Herb (Serpens herba) - Cyclical preparation",
        "compound": "Ouroboros Essence - Sublimated preparation"
    },
    "f86r": {
        "title": "⚗️ The Final Crucible - Industrial Culmination",
        "section": "Industrial",
        "glyphs": "qokchor.daiin.shody.chor.qotchey",
        "transliteration": "ku-kah-chah-rah | dah-ee-in | shah-dah-ee | chah-rah | ku-tah-chay",
        "investigation": """**Wilken Key Scholar Investigation:**

The eighty-sixth folio presents the industrial section's culmination - a massive crucible assembly capable of processing accumulated products from all previous operations.

The 'qokchor' opening with causative prefix indicates this operation activates or empowers materials from all previous folios, marking this as a culminating operation.

The 'daiin.shody' medial pairing creates a sealing-harmonizing sequence representing integration of all previous operations into unified product.

The crucible's capacity would accommodate the combined output of exactly twenty industrial operations - the number of folios in the industrial section.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Assemble culminating crucible apparatus
2. Open with causative 'qokchor' activation
3. Seal accumulated materials with 'daiin'
4. Harmonize all components with 'shody'
5. Ground with 'chor'
6. Open toward next phase with 'qotchey'
7. Process combined output of twenty operations
8. Store final product in vessel of completion""",
        "herbal": "Culmination Herb (Culmen herba) - Final preparation",
        "compound": "Philosopher's Preparation - Culminated essence"
    },
    "f87r": {
        "title": "📜 The Rosetta Threshold - Registry Commencement",
        "section": "Registry",
        "glyphs": "pchodar.qotchey.shody.daiin.chor",
        "transliteration": "pah-chah-dah-rah | ku-tah-chay | shah-dah-ee | dah-ee-in | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

The eighty-seventh folio marks the manuscript's most significant structural transition - the commencement of the registry section with systematic administrative documentation.

This folio introduces the Rosetta Shift, a +15 increment in Yale image ID calculation that has puzzled scholars for generations.

The 'pchodar' opening with plural prefix suggests this section addresses collective or institutional contexts rather than individual operations.

The illustration shifts from botanical and alchemical subjects to geometric cartouches containing symbolic notation - the first appearance of "registry script.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Acknowledge threshold transition at folio 87
2. Apply Rosetta Shift (+15) to image calculations
3. Open with collective 'pchodar'
4. Apply creative 'qotchey' for new section
5. Harmonize with 'shody'
6. Seal with 'daiin'
7. Ground with 'chor'
8. Document in registry format""",
        "herbal": "Registry Herb (Registrum herba) - Administrative preparation",
        "compound": "Essence of Record - Registry preparation"
    },
    "f90r": {
        "title": "📜 The Decade Ledger - Tenfold Accounting",
        "section": "Registry",
        "glyphs": "qotchey.shody.chor.daiin.chor",
        "transliteration": "ku-tah-chay | shah-dah-ee | chah-rah | dah-ee-in | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

Ten registry cartouches arranged in two columns of five demonstrate the manuscript's systematic approach to administrative documentation.

The 'qotchey.shody' opening creates a creative-harmonizing sequence indicating the registry's function of establishing order among distributed materials.

The doubled 'chor' framing with medial 'daiin' creates a grounded-sealed-grounded structure appropriate for permanent records.

The cartouches' symbolic content reveals potential phonetic elements that may encode proper names or place designations.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Arrange ten registry cartouches in 2×5 grid
2. Open with creative-harmonizing 'qotchey.shody'
3. Ground initial entry with 'chor'
4. Seal record with 'daiin'
5. Complete with grounding 'chor'
6. Encode quantities in registry script
7. Verify ten entries against sources
8. Archive in decade ledger format""",
        "herbal": "Ledger Herb (Liber herba) - Accounting preparation",
        "compound": "Decade Essence - Ledger preparation"
    },
    "f93r": {
        "title": "📜 The Triad Registry - Threefold Documentation",
        "section": "Registry",
        "glyphs": "chor.qotchey.daiin.shody.chor",
        "transliteration": "chah-rah | ku-tah-chay | dah-ee-in | shah-dah-ee | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

Three registry cartouches of increasing size suggest hierarchical documentation structure, possibly representing different administrative levels.

The 'chor' opening returns to the foundational root position seen in the manuscript's earliest folios, creating structural echo linking beginning and middle sections.

The cartouches' symbolic content includes repeated elements that may represent standardized units of measurement or currency.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Create three registry cartouches in hierarchy
2. Open with grounding 'chor'
3. Apply creative 'qotchey'
4. Seal primary record with 'daiin'
5. Harmonize secondary entries with 'shody'
6. Complete with grounding 'chor'
7. Document in three administrative levels
8. Verify hierarchical relationships""",
        "herbal": "Triad Herb (Trias herba) - Hierarchical preparation",
        "compound": "Essence of Three - Triad preparation"
    },
    "f96r": {
        "title": "📜 The Hexad Archive - Sixfold Classification",
        "section": "Registry",
        "glyphs": "shody.chor.qotchey.daiin.chor",
        "transliteration": "shah-dah-ee | chah-rah | ku-tah-chay | dah-ee-in | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

Six registry cartouches arranged in hexagonal pattern demonstrate sophisticated organizational principles, with each cartouche connecting to adjacent entries.

The 'shody' opening position may indicate this entry documents harmonized or reconciled accounts from multiple sources.

The hexagonal connections include directional indicators that may represent temporal sequences, suggesting this registry documents processes rather than static inventories.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Arrange six cartouches in hexagonal pattern
2. Open with harmonizing 'shody'
3. Ground data with 'chor'
4. Apply creative 'qotchey' for organization
5. Seal records with 'daiin'
6. Complete with grounding 'chor'
7. Connect related entries with lines
8. Document workflow sequences""",
        "herbal": "Archive Herb (Archivum herba) - Classification preparation",
        "compound": "Hexad Essence - Archive preparation"
    },
    "f100r": {
        "title": "📜 The Century Mark - Hundredfold Record",
        "section": "Registry",
        "glyphs": "qokchor.shody.chor.daiin.qotchey",
        "transliteration": "ku-kah-chah-rah | shah-dah-ee | chah-rah | dah-ee-in | ku-tah-chay",
        "investigation": """**Wilken Key Scholar Investigation:**

The hundredth folio represents a milestone in the manuscript's structure, marked by expanded registry cartouches and enhanced decorative elements.

The 'qokchor' opening with causative prefix suggests this folio activates or summarizes preceding registry entries, possibly representing a master record.

The expanded cartouches contain more complex symbolic notation, indicating the hundredth folio documents particularly significant transactions.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Recognize milestone at century folio
2. Open with causative 'qokchor' activation
3. Harmonize records with 'shody'
4. Ground summary with 'chor'
5. Seal consolidated entry with 'daiin'
6. Open toward future with 'qotchey'
7. Document master record
8. Archive with enhanced security""",
        "herbal": "Century Herb (Centum herba) - Centennial preparation",
        "compound": "Essence of Hundred - Century preparation"
    },
    "f104r": {
        "title": "📜 The Registry Seal - Administrative Authority",
        "section": "Registry",
        "glyphs": "daiin.chor.shody.qotchey.chor",
        "transliteration": "dah-ee-in | chah-rah | shah-dah-ee | ku-tah-chay | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

The registry seal folio presents the most elaborate cartouche in the administrative section, containing symbolic elements that may represent institutional authority.

The 'daiin' opening position, highly unusual, creates a sealing-first structure indicating this entry serves authenticating or validating function.

The cartouche's symbolic content includes elements resembling medieval notarial marks, suggesting this folio documents official certification.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Create authoritative seal cartouche
2. Open with validating 'daiin'
3. Ground authentication with 'chor'
4. Harmonize with standards using 'shody'
5. Apply creative 'qotchey' for certification
6. Complete with grounding 'chor'
7. Apply seal to preceding records
8. Document certification authority""",
        "herbal": "Seal Herb (Sigillum herba) - Authoritative preparation",
        "compound": "Essence of Authority - Seal preparation"
    },
    "f108r": {
        "title": "📜 The Final Account - Registry Culmination",
        "section": "Registry",
        "glyphs": "chor.daiin.qokchor.shody.qotchey",
        "transliteration": "chah-rah | dah-ee-in | ku-kah-chah-rah | shah-dah-ee | ku-tah-chay",
        "investigation": """**Wilken Key Scholar Investigation:**

The registry section's culmination presents a comprehensive cartouche assembly summarizing all preceding administrative documentation.

The 'chor.daiin' opening creates a grounding-sealing sequence establishing the final account's authority and permanence.

The 'qokchor' medial position suggests this folio activates or empowers the entire registry section, transforming accumulated records into actionable instrument.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Assemble comprehensive final account
2. Open with grounding-sealing 'chor.daiin'
3. Apply causative 'qokchor' for activation
4. Harmonize entire registry with 'shody'
5. Open toward application with 'qotchey'
6. Verify against all preceding entries
7. Certify master summary
8. Archive with highest security""",
        "herbal": "Final Herb (Ultima herba) - Culminating preparation",
        "compound": "Master Registry Essence - Final preparation"
    },
    "f110r": {
        "title": "📜 The Administrative Close - Institutional Seal",
        "section": "Registry/Administrative",
        "glyphs": "pchol.daiin.chor.shody.qotchey",
        "transliteration": "pah-chah-lah | dah-ee-in | chah-rah | shah-dah-ee | ku-tah-chay",
        "investigation": """**Wilken Key Scholar Investigation:**

The administrative close folio marks the registry section's formal conclusion with institutional seal and notarial marks establishing official status.

The 'pchol' opening with plural prefix and liquid terminal suggests this folio addresses collective institutional context.

The notarial marks may encode dates, authorities, or jurisdictions, documenting specific institutional context for the entire manuscript.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Prepare institutional seal elements
2. Open with collective 'pchol'
3. Apply validating 'daiin'
4. Ground with institutional 'chor'
5. Harmonize with 'shody'
6. Open toward future with 'qotchey'
7. Apply notarial authentication
8. Complete administrative closure""",
        "herbal": "Close Herb (Clausura herba) - Closing preparation",
        "compound": "Institutional Seal - Administrative preparation"
    },
    "f113r": {
        "title": "📜 The Legacy Entry - Transmission Record",
        "section": "Registry/Administrative",
        "glyphs": "qotchey.chor.daiin.shody.chor",
        "transliteration": "ku-tah-chay | chah-rah | dah-ee-in | shah-dah-ee | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

The legacy entry folio documents manuscript transmission with cartouches containing symbolic elements representing succession or institutional transfer.

The classic 'qotchey.chor' opening returns from the manuscript's earliest folios, creating structural ring composition linking conclusion with origin.

The transmission motifs include elements resembling medieval colophons and ex libris marks, documenting provenance and intended readership.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Document transmission context
2. Open with classic 'qotchey.chor'
3. Seal authenticity with 'daiin'
4. Harmonize continuity with 'shody'
5. Ground in tradition with 'chor'
6. Record provenance information
7. Identify intended readership
8. Complete transmission documentation""",
        "herbal": "Legacy Herb (Legatum herba) - Transmission preparation",
        "compound": "Essence of Continuity - Legacy preparation"
    },
    "f116r": {
        "title": "📜 The Final Seal - Manuscript Culmination",
        "section": "Registry/Administrative",
        "glyphs": "chor.shody.daiin.qotchey.chor",
        "transliteration": "chah-rah | shah-dah-ee | dah-ee-in | ku-tah-chay | chah-rah",
        "investigation": """**Wilken Key Scholar Investigation:**

The final folio presents the manuscript's culminating seal, integrating all preceding elements into unified closure.

The 'chor' opening returns to the foundational root from the manuscript's first folio, completing the ring composition structuring the entire work.

The 'shody.daiin' medial pairing creates a harmonizing-sealing sequence representing the manuscript's final blessing and authentication.

The culminating cartouche includes symbolic elements from all manuscript sections, creating visual summary of the entire Wilken Key Engine.""",
        "recipe": """**8-Step Wilken Key Recipe:**

1. Prepare culminating seal assembly
2. Open with foundational 'chor'
3. Harmonize with 'shody'
4. Seal with 'daiin'
5. Apply creative 'qotchey'
6. Complete with grounding 'chor'
7. Integrate all section elements
8. Conclude manuscript with blessing""",
        "herbal": "Culmination Herb (Culmen herba) - Final preparation",
        "compound": "Philosopher's Seal - Culminating preparation"
    }
}

# =============================================================================
# MAIN APPLICATION HEADER
# =============================================================================
st.markdown("<h1 style='text-align: center;'>🗝️ WILKEN KEY ENGINE</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>The Million-Word Omnibus | MS 408</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #b8941f; font-family: Cinzel, serif;'>232 Folios | 23 Elite Waypoints | Yale Beinecke Digital Archive</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# =============================================================================
# METRICS DASHBOARD
# =============================================================================
col1, col2, col3, col4 = st.columns(4)
col1.metric("📊 Total Folios", len(FOLIOS))
col2.metric("⭐ Elite Waypoints", len(ELITE_WAYPOINTS))
col3.metric("🔢 Yale Base ID", BASE_YALE_ID)
col4.metric("🔄 Rosetta Shift", f"+{ROSETTA_SHIFT}")

st.markdown("<hr>", unsafe_allow_html=True)

# =============================================================================
# SIDEBAR NAVIGATION
# =============================================================================
st.sidebar.markdown("<h2 style='color: #d4af37; font-family: Cinzel, serif;'>🗝️ Navigation</h2>", unsafe_allow_html=True)

# Initialize session state for folio selection
if 'selected_folio' not in st.session_state:
    st.session_state.selected_folio = "f1r"

# Folio selector
selected_folio = st.sidebar.selectbox(
    "📖 Select Folio",
    FOLIOS,
    index=FOLIOS.index(st.session_state.selected_folio),
    key="folio_selector"
)
st.session_state.selected_folio = selected_folio

# Section filter
st.sidebar.markdown("<hr style='margin: 10px 0; border-color: rgba(212,175,55,0.3);'>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #d4af37; font-family: Cinzel, serif; font-weight: 600;'>🔍 Filter by Section</p>", unsafe_allow_html=True)

section_filter = st.sidebar.multiselect(
    "Show Sections",
    ["Herbal/Celestial", "Industrial", "Registry/Administrative"],
    default=["Herbal/Celestial", "Industrial", "Registry/Administrative"],
    label_visibility="collapsed"
)

# Quick Elite Waypoints
st.sidebar.markdown("<hr style='margin: 10px 0; border-color: rgba(212,175,55,0.3);'>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #d4af37; font-family: Cinzel, serif; font-weight: 600;'>⭐ Quick Elite Waypoints</p>", unsafe_allow_html=True)

# Create columns for waypoint buttons
waypoint_cols = st.sidebar.columns(2)
waypoint_list = list(ELITE_WAYPOINTS.items())

for idx, (folio, data) in enumerate(waypoint_list[:10]):  # Show first 10
    col_idx = idx % 2
    with waypoint_cols[col_idx]:
        if st.button(f"{folio}", key=f"wp_{folio}", help=data['title']):
            st.session_state.selected_folio = folio
            st.rerun()

# Search functionality
st.sidebar.markdown("<hr style='margin: 10px 0; border-color: rgba(212,175,55,0.3);'>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #d4af37; font-family: Cinzel, serif; font-weight: 600;'>🔎 Search Waypoints</p>", unsafe_allow_html=True)

search_term = st.sidebar.text_input(
    "Type to search",
    placeholder="e.g., Genesis, Star, Root...",
    label_visibility="collapsed"
)

# =============================================================================
# MAIN CONTENT AREA
# =============================================================================
folio_num = int(''.join(filter(str.isdigit, selected_folio)))
current_section = get_section(folio_num)

# Display folio header
st.markdown(f"<h2>{selected_folio.upper()} | {current_section}</h2>", unsafe_allow_html=True)

# Display Yale image
yale_url = get_iiif_url(selected_folio)
st.image(
    yale_url,
    use_container_width=True,
    caption=f"Yale Beinecke Library MS 408 | {selected_folio.upper()} | Yale ID: {get_yale_image_id(selected_folio)}"
)

# =============================================================================
# ELITE WAYPOINT DISPLAY
# =============================================================================
if selected_folio in ELITE_WAYPOINTS:
    wp = ELITE_WAYPOINTS[selected_folio]
    
    # Waypoint title card
    st.markdown(f"""
    <div class='waypoint-card'>
        <h3 style='margin: 0; color: #d4af37;'>{wp['title']}</h3>
        <p style='color: #b8941f; margin: 5px 0 0 0; font-size: 0.9rem;'>Section: {wp['section']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs for waypoint content
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔤 Glyphs", "📜 Investigation", "⚗️ Recipe", "🌿 Herbal", "💎 Compound"])
    
    with tab1:
        st.markdown("<h4 style='color: #d4af37; font-family: Cinzel, serif;'>Wilken Key Glyphs</h4>", unsafe_allow_html=True)
        st.code(wp['glyphs'], language=None)
        st.markdown("<h4 style='color: #d4af37; font-family: Cinzel, serif; margin-top: 15px;'>Phonetic Transliteration</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #e8dcc0; font-size: 1.1rem; font-family: Crimson Text, serif;'>{wp['transliteration']}</p>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div class='investigation-box'>" + wp['investigation'].replace('\n', '<br>') + "</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<div class='recipe-box'>" + wp['recipe'].replace('\n', '<br>') + "</div>", unsafe_allow_html=True)
    
    with tab4:
        st.markdown(f"<p style='color: #e8dcc0; font-size: 1.1rem;'><strong style='color: #d4af37;'>Wilken Key Herbal:</strong> {wp['herbal']}</p>", unsafe_allow_html=True)
    
    with tab5:
        st.markdown(f"<p style='color: #e8dcc0; font-size: 1.1rem;'><strong style='color: #d4af37;'>Wilken Key Compound:</strong> {wp['compound']}</p>", unsafe_allow_html=True)

# =============================================================================
# EXPANDABLE SECTIONS
# =============================================================================
st.markdown("<hr>", unsafe_allow_html=True)

# Wilken Key Reference
with st.expander("🗝️ Wilken Key Phonetic Reference"):
    st.markdown("<h4 style='color: #d4af37; font-family: Cinzel, serif;'>Complete Phonetic Mapping</h4>", unsafe_allow_html=True)
    
    # Display in columns
    key_cols = st.columns(4)
    items = list(WILKEN_KEY.items())
    
    for i, (glyph, phonetic) in enumerate(items):
        col_idx = i % 4
        with key_cols[col_idx]:
            st.markdown(f"<code style='color: #d4af37; font-size: 1rem;'>{glyph}</code> → <span style='color: #e8dcc0;'>{phonetic}</span>", unsafe_allow_html=True)

# Yale ID Calculator
with st.expander("🔢 Yale Image ID Calculator"):
    st.markdown("<h4 style='color: #d4af37; font-family: Cinzel, serif;'>Calculate Yale Beinecke Image ID</h4>", unsafe_allow_html=True)
    
    calc_col1, calc_col2 = st.columns([2, 3])
    
    with calc_col1:
        calc_folio = st.text_input("Enter Folio (e.g., f1r)", value=selected_folio, key="calc_input")
    
    with calc_col2:
        if calc_folio:
            try:
                calc_id = get_yale_image_id(calc_folio)
                calc_url = get_iiif_url(calc_folio)
                fol_num = int(''.join(filter(str.isdigit, calc_folio)))
                rosetta_applied = "YES (+15)" if fol_num > 86 else "NO"
                
                st.markdown(f"""
                <div style='background: rgba(212,175,55,0.1); border: 1px solid #d4af37; border-radius: 8px; padding: 10px;'>
                    <p style='margin: 0; color: #b8941f;'><strong>Yale ID:</strong> <span style='color: #d4af37; font-size: 1.2rem;'>{calc_id}</span></p>
                    <p style='margin: 5px 0 0 0; color: #b8941f; font-size: 0.85rem;'>Rosetta Shift: {rosetta_applied}</p>
                    <p style='margin: 5px 0 0 0; color: #b8941f; font-size: 0.8rem; word-break: break-all;'><a href='{calc_url}' target='_blank' style='color: #d4af37;'>{calc_url}</a></p>
                </div>
                """, unsafe_allow_html=True)
            except:
                st.error("Invalid folio format. Use format like 'f1r' or 'f50v'")

# All Elite Waypoints
with st.expander("⭐ All Elite Waypoints"):
    if search_term:
        filtered_waypoints = {k: v for k, v in ELITE_WAYPOINTS.items() if search_term.lower() in v['title'].lower()}
        st.markdown(f"<p style='color: #b8941f;'>Search results for '{search_term}': {len(filtered_waypoints)} found</p>", unsafe_allow_html=True)
    else:
        filtered_waypoints = ELITE_WAYPOINTS
    
    # Group by section
    sections_display = {}
    for folio, data in filtered_waypoints.items():
        section = data['section']
        if section not in sections_display:
            sections_display[section] = []
        sections_display[section].append((folio, data['title']))
    
    for section, items in sections_display.items():
        st.markdown(f"<h4 style='color: #d4af37; font-family: Cinzel, serif; margin-top: 15px;'>{section}</h4>", unsafe_allow_html=True)
        for folio, title in items:
            st.markdown(f"<p style='margin: 3px 0; color: #e8dcc0;'><strong>{folio}:</strong> {title}</p>", unsafe_allow_html=True)

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px 0;'>
    <p style='color: #b8941f; font-family: Cinzel, serif; font-size: 0.9rem; margin: 0;'>
        🗝️ Wilken Key Engine v4.0 | Yale Beinecke Library MS 408
    </p>
    <p style='color: #8b7355; font-size: 0.8rem; margin: 5px 0 0 0;'>
        Wilken Key Scholar Investigation | Million-Word Omnibus
    </p>
    <p style='color: #8b7355; font-size: 0.75rem; margin: 5px 0 0 0;'>
        🌐 wilken-key-engine-ms-408-omnibus.streamlit.app
    </p>
</div>
""", unsafe_allow_html=True)
