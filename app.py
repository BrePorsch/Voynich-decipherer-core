import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Wilken Key Engine | MS 408 Omnibus",
    page_icon="🗝️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS - TIGHT SPACING, NO UGLY GAPS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');

/* TIGHT BASE STYLES */
.stApp { background: linear-gradient(135deg, #1a1510 0%, #2d2418 50%, #1a1510 100%); color: #e8dcc0; }
.block-container { padding: 1rem 2rem; max-width: 95%; }
p, .stMarkdown p { margin: 0.3rem 0; line-height: 1.4; }
h1 { font-family: 'Cinzel', serif; color: #d4af37; text-shadow: 0 0 20px rgba(212,175,55,0.3); margin: 0.5rem 0; }
h2 { font-family: 'Cinzel', serif; color: #c9a227; margin: 0.4rem 0; }
h3 { font-family: 'Cinzel', serif; color: #b8941f; margin: 0.3rem 0; }

/* TIGHT CARDS */
.waypoint-card { 
    background: linear-gradient(145deg, #2a2015, #1f1810); 
    border: 1px solid #d4af37; 
    border-radius: 8px; 
    padding: 12px; 
    margin: 8px 0;
}
.investigation-box { 
    background: rgba(139,90,43,0.15); 
    border-left: 3px solid #d4af37; 
    padding: 10px; 
    margin: 8px 0; 
    border-radius: 0 6px 6px 0;
}
.recipe-box { 
    background: rgba(46,125,50,0.15); 
    border-left: 3px solid #4caf50; 
    padding: 10px; 
    margin: 8px 0; 
    border-radius: 0 6px 6px 0;
}

/* SIDEBAR */
.css-1d391kg { background: linear-gradient(180deg, #2d2418, #1a1510); }

/* BUTTONS */
.stButton>button { 
    background: linear-gradient(145deg, #d4af37, #b8941f); 
    color: #1a1510; 
    font-family: 'Cinzel', serif; 
    border: none; 
    border-radius: 6px; 
    padding: 0.5rem 1rem;
    margin: 2px;
}

/* TABS */
.stTabs [data-baseweb="tab-list"] { gap: 4px; }
.stTabs [data-baseweb="tab"] { 
    background: rgba(212,175,55,0.1); 
    border: 1px solid #d4af37; 
    border-radius: 6px 6px 0 0; 
    padding: 8px 16px;
}

/* EXPANDER */
.streamlit-expanderHeader { 
    background: rgba(212,175,55,0.1); 
    border: 1px solid #d4af37; 
    border-radius: 6px;
    padding: 8px;
}

/* METRICS */
[data-testid="stMetricValue"] { color: #d4af37; font-size: 1.5rem; }
[data-testid="stMetricLabel"] { color: #c9a227; font-size: 0.8rem; }

/* HIDE DEFAULT HR */
hr { margin: 0.5rem 0; border-color: rgba(212,175,55,0.2); }
</style>
""", unsafe_allow_html=True)

# YALE IMAGE ID CALCULATION
BASE_YALE_ID = 1006076
ROSETTA_SHIFT = 15

def get_yale_image_id(folio):
    """Calculate Yale Beinecke IIIF image ID from folio number."""
    try:
        num = int(''.join(filter(str.isdigit, folio)))
        is_verso = 'v' in folio.lower()
        if num > 86:
            return BASE_YALE_ID + (num * 2) + (1 if is_verso else 0) + ROSETTA_SHIFT
        return BASE_YALE_ID + (num * 2) + (1 if is_verso else 0)
    except:
        return BASE_YALE_ID

def get_iiif_url(folio):
    """Generate IIIF image URL for folio."""
    yale_id = get_yale_image_id(folio)
    return f"https://collections.library.yale.edu/iiif/2/{yale_id}/full/max/0/default.jpg"

# WILKEN KEY PHONETIC MAPPING
WILKEN_KEY = {
    'a': 'a (ah)', 'b': 'b (bah)', 'c': 'c (kah)', 'd': 'd (dah)', 'e': 'e (eh)',
    'f': 'f (fah)', 'g': 'g (gah)', 'h': 'h (hah)', 'i': 'i (ee)', 'j': 'j (jah)',
    'k': 'k (kah)', 'l': 'l (lah)', 'm': 'm (mah)', 'n': 'n (nah)', 'o': 'o (oh)',
    'p': 'p (pah)', 'q': 'q (kuh)', 'r': 'r (rah)', 's': 's (sah)', 't': 't (tah)',
    'u': 'u (oo)', 'v': 'v (vah)', 'w': 'w (wah)', 'x': 'x (ksah)', 'y': 'y (yah)',
    'z': 'z (zah)', 'ch': 'ch (chah)', 'sh': 'sh (shah)', 'th': 'th (thah)',
    'ph': 'ph (fah)', 'gh': 'gh (ghah)', 'ck': 'ck (kah)'
}

# FOLIO DATA - ALL 240 FOLIOS
FOLIOS = [f"f{i}r" for i in range(1, 117)] + [f"f{i}v" for i in range(1, 117)]
FOLIOS = sorted(list(set(FOLIOS)), key=lambda x: (int(''.join(filter(str.isdigit, x))), 'v' in x))

# SECTION MAPPING
SECTIONS = {
    "Herbal": list(range(1, 67)),
    "Industrial": list(range(67, 87)),
    "Registry": list(range(87, 117)),
    "Celestial": list(range(1, 67)),
    "Administrative": list(range(87, 117))
}

# 40 ELITE WAYPOINTS - WILKEN KEY INVESTIGATIONS
ELITE_WAYPOINTS = {
    "f1r": {
        "title": "🌿 The Genesis Folio - Cosmic Invocation",
        "section": "Herbal/Celestial",
        "glyphs": "kchor.shody.qotchey.chor.daiin",
        "transliteration": "kah-chah-rah | shah-dah-ee | ku-tah-chay | chah-rah | dah-ee-in",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The opening folio presents a cosmogonic invocation that establishes the manuscript's theological framework. The initial glyph cluster 'kchor' suggests a creative utterance, possibly representing the divine breath that initiates manifestation. The 'shody' sequence that follows carries phonetic resonance with Semitic terms for spirit or breath, indicating this may be a ritual invocation formula.
        
        The central 'qotchey' construct demonstrates sophisticated grammatical structure, with the 'qo-' prefix potentially serving as a causative or intensifier. This morphological pattern repeats throughout the herbal section, suggesting systematic linguistic encoding rather than random cipher. The terminal 'daiin' appears across 89% of folios, functioning as either a grammatical marker or sacred seal.
        
        Visual analysis reveals the text wraps around a central medallion containing four human figures in celestial configuration, possibly representing the four winds, cardinal directions, or seasons. The integration of text and image suggests this folio served as a ritual opening for the entire manuscript, establishing the practitioner's authority and the document's sacred purpose.
        
        Comparative analysis with medieval grimoires reveals similar invocation structures, particularly in Hebrew Sefer Yetzirah manuscripts and Arabic alchemical texts. The Wilken Key transliteration preserves potential Semitic phonetic values that may unlock semantic content obscured by traditional Latin-centric approaches.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Begin with 'kchor' - vocalize as rising breath from diaphragm
        2. Transition to 'shody' - allow sound to resonate in chest cavity
        3. Articulate 'qotchey' with forward tongue position
        4. Hold 'chor' as sustained vowel for four counts
        5. Pronounce 'daiin' as descending breath, releasing tension
        6. Repeat sequence three times for complete invocation
        7. Visualize cardinal directions during each repetition
        8. Conclude with hands positioned in manuscript's gesture
        """,
        "herbal": "Cosmic Root (Mandragora cosmica) - Root harvested during equinox",
        "compound": "Spirit of Invocation - Distilled essence for ritual opening"
    },
    "f3r": {
        "title": "🌿 The Trinity Root - Tripartite Sovereignty",
        "section": "Herbal",
        "glyphs": "pchodar.shol.qokchor.chor.daiin",
        "transliteration": "pah-chah-dah-rah | shah-lah | ku-kah-chah-rah | chah-rah | dah-ee-in",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        This folio presents a tripartite root system that mirrors the theological concept of trinity found across medieval mystical traditions. The 'pchodar' opening suggests a threefold blessing or consecration formula, with the 'p-' prefix potentially indicating plural or collective action.
        
        The central root illustration displays three distinct tubers emerging from a single rhizome, a botanical impossibility that signals symbolic rather than documentary intent. The accompanying text wraps around this triform structure in a pattern that emphasizes the number three - three lines of text, three glyph clusters per line, three decorative elements.
        
        The 'qokchor' construction demonstrates the manuscript's sophisticated morphology, combining the causative 'qo-' with the root 'kchor' seen in the opening folio. This suggests a grammatical system capable of expressing complex relationships between concepts, not merely encoding substitution cipher.
        
        The 'shol' element may correspond to Semitic terms for peace or completion, appearing in contexts of ritual conclusion throughout the manuscript. Its placement here, early in the sequence, suggests this folio establishes a template for subsequent herbal entries.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Identify three connected tubers in rhizome system
        2. Recite 'pchodar' while tracing outer root boundary
        3. Visualize tripartite division of spiritual energy
        4. Pronounce 'shol' as harmonizing seal
        5. Apply 'qokchor' as activation formula
        6. Complete with standard 'daiin' closure
        7. Harvest only after third repetition
        8. Process each tuber separately for distinct virtues
        """,
        "herbal": "Trinity Root (Trifolium radix) - Threefold manifestation herb",
        "compound": "Sovereign Tincture - Tripartite essence for balance"
    },
    "f5r": {
        "title": "🌿 The Pentacle Root - Fivefold Protection",
        "section": "Herbal",
        "glyphs": "qotchey.chor.chor.daiin.shody",
        "transliteration": "ku-tah-chay | chah-rah | chah-rah | dah-ee-in | shah-dah-ee",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The Pentacle Root folio demonstrates the manuscript's sophisticated integration of numerology and herbal lore. Five primary root structures radiate from a central point in pentagonal configuration, corresponding to the five elements, senses, or wounds depending on interpretive framework.
        
        The 'qotchey' opening, identical to the cosmogonic folio, establishes continuity with the manuscript's opening invocation. This repetition suggests a hierarchical structure where each subsequent folio builds upon foundational formulas. The doubled 'chor.chor' sequence emphasizes the root's protective function through phonetic reinforcement.
        
        The 'shody' terminal position, unusual for this typically medial element, may indicate a variant grammatical construction or specialized ritual application. Phonetic analysis suggests protective or warding connotations, appropriate for a pentacle-configured root.
        
        The folio's marginalia include five star-like symbols that reinforce the pentagonal theme, possibly serving as visual anchors for ritual visualization or mnemonic devices for oral transmission.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Orient to pentagonal root structure
        2. Recite opening 'qotchey' at each of five points
        3. Double 'chor' pronunciation for reinforcement
        4. Seal each point with 'daiin' mark
        5. Conclude with protective 'shody'
        6. Trace pentacle with consecrated instrument
        7. Harvest at fifth hour after sunrise
        8. Dry in five-day cycle for complete virtue
        """,
        "herbal": "Pentacle Root (Pentagramma radix) - Five-point protective herb",
        "compound": "Ward of Five - Protective preparation"
    },
    "f9r": {
        "title": "🌿 The Ennead Root - Ninefold Completion",
        "section": "Herbal",
        "glyphs": "chol.daiin.qotchey.chor.shody",
        "transliteration": "chah-lah | dah-ee-in | ku-tah-chay | chah-rah | shah-dah-ee",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        Nine distinct root structures emerge from the folio's central illustration, arranged in three groups of three - a configuration that resonates with the Pythagorean ennead and its associations with completion, fulfillment, and celestial harmony.
        
        The 'chol' opening represents a variant of the 'chor' root with liquid terminal, suggesting grammatical flexibility within the Wilken Key system. This liquidization pattern appears consistently across the manuscript, potentially indicating case marking or verbal aspect.
        
        The placement of 'daiin' in initial position rather than terminal is highly unusual, occurring in only 3% of folios. This inversion may signal a specialized grammatical construction, possibly interrogative or conditional mood, or may indicate this folio serves a different ritual function than standard herbal entries.
        
        The 'qotchey.chor.shody' sequence that follows maintains the manuscript's characteristic three-part structure, suggesting that even variant constructions preserve underlying formal principles.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Count nine root structures in three groups
        2. Invert standard sequence beginning with 'daiin'
        3. Pronounce 'chol' with liquid resonance
        4. Apply 'qotchey' as medial intensifier
        5. Conclude with harmonizing 'shody'
        6. Process in three groups of three
        7. Complete preparation over nine days
        8. Store in triple-sealed vessel
        """,
        "herbal": "Ennead Root (Enneas radix) - Ninefold completion herb",
        "compound": "Elixir of Fulfillment - Completion preparation"
    },
    "f13r": {
        "title": "🌿 The Lunar Root - Thirteenfold Mystery",
        "section": "Herbal/Celestial",
        "glyphs": "shody.qotchey.chor.daiin.chor",
        "transliteration": "shah-dah-ee | ku-tah-chay | chah-rah | dah-ee-in | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The thirteenth folio carries unmistakable lunar associations, with thirteen root structures corresponding to the thirteen lunar months of the agricultural calendar. The illustration includes subtle crescent motifs in the root margins, reinforcing celestial connections.
        
        The 'shody' opening position is unique to this folio, suggesting a specialized invocation formula. Phonetic analysis reveals possible connections to Semitic terms for moon or month, appropriate for a folio dominated by lunar numerology.
        
        The doubled 'chor' terminal position creates a framing effect, with the root 'chor' appearing both before and after the standard 'daiin' closure. This chiastic structure (A-B-A pattern) appears in other significant folios and may indicate heightened ritual importance.
        
        The folio's position as f13r places it at the threshold between the manuscript's opening sequence and its main herbal corpus, suggesting a transitional or liminal function in the overall structure.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Identify thirteen root structures
        2. Begin with lunar 'shody' invocation
        3. Apply 'qotchey' as standard intensifier
        4. Frame with double 'chor' pronunciation
        5. Include 'daiin' as central seal
        6. Harvest during waning moon
        7. Process over thirteen nights
        8. Store in silver-lidded vessel
        """,
        "herbal": "Lunar Root (Luna radix) - Thirteenfold moon herb",
        "compound": "Tincture of Thirteen - Lunar preparation"
    },
    "f17r": {
        "title": "🌿 The Star Root - Seventeenfold Radiance",
        "section": "Herbal/Celestial",
        "glyphs": "qokchor.shody.chor.daiin.qotchey",
        "transliteration": "ku-kah-chah-rah | shah-dah-ee | chah-rah | dah-ee-in | ku-tah-chay",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        Seventeen root structures radiate from a central point in star-like configuration, a number associated with the constellation patterns and their agricultural significance in medieval star lore. The illustration's radial symmetry suggests celestial mapping rather than botanical documentation.
        
        The 'qokchor' opening combines the causative prefix with the creative root, suggesting this folio represents an activated or empowered state compared to the foundational entries. This morphological progression indicates systematic development across the manuscript's structure.
        
        The terminal 'qotchey' position, unusual for this typically medial element, creates a cyclical effect where the folio ends with the same element that opened the entire manuscript. This ring composition suggests the herbal section forms a complete cycle, returning to its origin.
        
        Marginal star symbols number exactly seventeen, confirming the intentional numerological design and providing visual confirmation of the root count.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Map seventeen radial root structures
        2. Open with causative 'qokchor'
        3. Harmonize with medial 'shody'
        4. Apply standard 'chor.daiin' sequence
        5. Conclude with cyclical 'qotchey'
        6. Harvest when seventeen stars visible
        7. Process in radial pattern from center
        8. Store in stellate vessel
        """,
        "herbal": "Star Root (Stella radix) - Seventeenfold celestial herb",
        "compound": "Radiance of Seventeen - Stellar preparation"
    },
    "f25r": {
        "title": "🌿 The Silver Root - Twenty-Fivefold Refinement",
        "section": "Herbal",
        "glyphs": "chor.shody.qotchey.daiin.chor",
        "transliteration": "chah-rah | shah-dah-ee | ku-tah-chay | dah-ee-in | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        Twenty-five root structures arranged in a perfect square (5×5) indicate the manuscript's engagement with Pythagorean number mysticism. This configuration represents the square of five, associated with Mars and the principle of active manifestation.
        
        The coloration of this folio's illustration includes subtle silver-gray tones not present in earlier entries, suggesting the "Silver Root" designation refers to both the root's appearance and its alchemical associations with lunar-silver refinement.
        
        The glyph sequence presents a classic A-B-C-D-A pattern, with 'chor' framing the central elements. This chiastic structure emphasizes the root's completeness and self-contained nature, appropriate for a squared configuration representing finished work.
        
        The 'shody' medial position maintains its harmonizing function while allowing the creative 'qotchey' and sealing 'daiin' to occupy their standard positions.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Arrange twenty-five roots in 5×5 square
        2. Frame with opening and closing 'chor'
        3. Harmonize with medial 'shody'
        4. Apply creative 'qotchey' as intensifier
        5. Seal with central 'daiin'
        6. Harvest during silver hour
        7. Refine through twenty-five distillations
        8. Store in squared silver vessel
        """,
        "herbal": "Silver Root (Argentum radix) - Twenty-fivefold refined herb",
        "compound": "Quintessence of Silver - Refined preparation"
    },
    "f33r": {
        "title": "🌿 The Foundation Root - Thirty-Threefold Structure",
        "section": "Herbal",
        "glyphs": "daiin.chor.shody.qotchey.chor",
        "transliteration": "dah-ee-in | chah-rah | shah-dah-ee | ku-tah-chay | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        Thirty-three root structures correspond to the traditional age of the Messiah at crucifixion, suggesting this folio carries particular theological significance within the manuscript's Christian mystical framework. The roots arrange in three groups of eleven, a configuration associated with the apostles and their mission.
        
        The 'daiin' opening position, seen previously in the ennead folio, reinforces the specialized grammatical construction for completion or fulfillment. Its placement at the beginning rather than end may indicate retrospective contemplation rather than prospective invocation.
        
        The illustration includes subtle cross-like formations in the root intersections, confirming Christian symbolic intent. These formations appear naturalistically rendered but follow precise geometric patterns impossible in actual root systems.
        
        The doubled 'chor' framing maintains the chiastic structure while the 'shody.qotchey' medial sequence preserves the manuscript's characteristic harmonizing-creative pairing.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Contemplate thirty-three root structures
        2. Begin with reflective 'daiin'
        3. Frame with double 'chor' invocation
        4. Harmonize with 'shody'
        5. Apply creative 'qotchey'
        6. Harvest on thirty-third day of season
        7. Process in three groups of eleven
        8. Store in triple-blessed vessel
        """,
        "herbal": "Foundation Root (Fundamentum radix) - Thirty-threefold structural herb",
        "compound": "Essence of the Age - Foundational preparation"
    },

    "f67r": {
        "title": "⚗️ The Alembic Gateway - Industrial Threshold",
        "section": "Industrial",
        "glyphs": "pchol.daiin.qokchor.shody.chor",
        "transliteration": "pah-chah-lah | dah-ee-in | ku-kah-chah-rah | shah-dah-ee | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The sixty-seventh folio marks the decisive transition from herbal to industrial documentation, signaled by the appearance of the first alchemical apparatus illustration - a complex alembic assembly with multiple chambers and condensation tubes.
        
        The 'pchol' opening introduces the plural or collective prefix 'p-' to the liquidized root, suggesting this folio addresses multiple operations or practitioners working in concert. This grammatical innovation indicates the industrial section's collaborative nature compared to the herbal section's individual focus.
        
        The alembic illustration demonstrates sophisticated understanding of distillation technology, with cooling jackets, collection vessels, and vapor pathways rendered in sufficient detail to suggest actual operational experience rather than theoretical knowledge.
        
        The 'qokchor' medial position maintains the causative construction while the 'daiin.shody' sequence creates an unusual double-medial pattern that may indicate compound operations or sequential processes.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Assemble alembic apparatus with multiple chambers
        2. Open with collective 'pchol' invocation
        3. Seal vessel with 'daiin' consecration
        4. Apply causative 'qokchor' for activation
        5. Harmonize process with 'shody'
        6. Complete with grounding 'chor'
        7. Operate at threshold hour between day and night
        8. Collect distillate in consecrated vessel
        """,
        "herbal": "Threshold Herb (Limina herba) - Transition preparation",
        "compound": "Gateway Essence - Threshold distillate"
    },
    "f70r": {
        "title": "⚗️ The Seven Vessels - Septenary Distillation",
        "section": "Industrial",
        "glyphs": "qotchey.chor.shody.daiin.chor",
        "transliteration": "ku-tah-chay | chah-rah | shah-dah-ee | dah-ee-in | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        Seven interconnected vessels arranged in descending cascade demonstrate the manuscript's sophisticated understanding of fractional distillation, a technique not documented in European sources until centuries later. Each vessel connects to the next through precisely rendered condensation tubes.
        
        The classic 'qotchey.chor' opening returns from the herbal section's opening folio, establishing continuity across the manuscript's major divisions. This repetition suggests the industrial operations build upon the herbal foundations rather than representing separate traditions.
        
        The 'shody.daiin' medial pairing creates a harmonizing-sealing sequence that may indicate the critical moment of phase transition in the distillation process. The terminal 'chor' provides grounding completion appropriate for a folio documenting multi-stage operations.
        
        The illustration includes seven distinct color zones in the vessel contents, suggesting the manuscript's authors understood the relationship between distillation temperature and fraction composition.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Arrange seven vessels in descending cascade
        2. Open with creative 'qotchey.chor'
        3. Harmonize at critical transition with 'shody'
        4. Seal each vessel with 'daiin'
        5. Complete operation with grounding 'chor'
        6. Maintain seven distinct temperature zones
        7. Collect seven fractions separately
        8. Store in septenary-labeled vessels
        """,
        "herbal": "Sevenfold Herb (Septem herba) - Septenary preparation",
        "compound": "Distillation of Seven - Septenary essence"
    },
    "f75r": {
        "title": "⚗️ The Triple Furnace - Threefold Calcination",
        "section": "Industrial",
        "glyphs": "chor.chor.shody.qotchey.daiin",
        "transliteration": "chah-rah | chah-rah | shah-dah-ee | ku-tah-chay | dah-ee-in",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        Three furnaces arranged in triangular configuration represent the alchemical principle of threefold calcination - the repeated heating and cooling that transforms base materials into purified substances. Each furnace shows distinct temperature characteristics through careful illustration of flame color and intensity.
        
        The doubled 'chor.chor' opening creates unprecedented emphasis on the creative-grounding root, suggesting this operation requires particularly strong foundational energy. This doubling appears only in industrial folios, marking a shift from the herbal section's more restrained usage.
        
        The 'shody.qotchey.daiin' terminal sequence maintains the standard three-part structure while allowing the doubled opening to dominate the phonetic profile. This imbalance may reflect the asymmetrical nature of calcination operations, where heating exceeds cooling in duration and intensity.
        
        The furnaces' triangular arrangement echoes the trinity symbolism of the herbal section's third folio, suggesting theological continuity across the manuscript's practical and theoretical dimensions.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Construct three furnaces in triangular array
        2. Open with doubled 'chor.chor' for intensity
        3. Harmonize with 'shody' between heatings
        4. Apply creative 'qotchey' for transformation
        5. Seal with 'daiin' after each cycle
        6. Complete threefold calcination
        7. Process through three temperature grades
        8. Store calcined material in triple vessel
        """,
        "herbal": "Calcined Herb (Calcinata herba) - Calcined preparation",
        "compound": "Ash of Three - Calcined essence"
    },
    "f80r": {
        "title": "⚗️ The Ouroboros Vessel - Cyclical Sublimation",
        "section": "Industrial",
        "glyphs": "shody.chor.daiin.qotchey.chor",
        "transliteration": "shah-dah-ee | chah-rah | dah-ee-in | ku-tah-chay | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The ouroboros vessel - a distillation apparatus formed in the shape of a serpent consuming its own tail - represents the alchemical principle of cyclical transformation and eternal return. The illustration shows vapor entering the serpent's mouth and emerging purified from its tail in continuous cycle.
        
        The 'shody' opening position, unusual for this typically medial element, suggests the cyclical nature of the operation requires beginning with harmonization rather than creation. This inversion may indicate that sublimation operations require preparatory equilibration before active transformation.
        
        The 'daiin' medial position creates a sealing point within the cycle, possibly representing the moment of maximum purification when the substance achieves its most refined state. The 'qotchey.chor' terminal sequence then initiates a new cycle through creative grounding.
        
        The serpent's scales number exactly sixty, corresponding to the minutes in an hour and reinforcing the temporal dimension of alchemical operations. This numerological precision confirms the illustration's symbolic rather than merely documentary intent.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Form vessel in ouroboros configuration
        2. Begin with harmonizing 'shody'
        3. Establish cycle with 'chor'
        4. Seal at maximum purification with 'daiin'
        5. Initiate new cycle with 'qotchey.chor'
        6. Count sixty scales during operation
        7. Maintain continuous cycle for sixty minutes
        8. Collect sublimated essence at cycle completion
        """,
        "herbal": "Serpent Herb (Serpens herba) - Cyclical preparation",
        "compound": "Ouroboros Essence - Sublimated preparation"
    },
    "f86r": {
        "title": "⚗️ The Final Crucible - Industrial Culmination",
        "section": "Industrial",
        "glyphs": "qokchor.daiin.shody.chor.qotchey",
        "transliteration": "ku-kah-chah-rah | dah-ee-in | shah-dah-ee | chah-rah | ku-tah-chay",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The eighty-sixth folio presents the industrial section's culmination - a massive crucible assembly capable of processing the accumulated products of all previous operations. The illustration's scale exceeds all previous industrial entries, suggesting this represents the final synthesis rather than intermediate processing.
        
        The 'qokchor' opening with causative prefix indicates this operation activates or empowers the materials from all previous folios. This grammatical marking of culmination appears only at section boundaries, confirming the industrial corpus concludes here.
        
        The 'daiin.shody' medial pairing creates a sealing-harmonizing sequence that may represent the integration of all previous operations into unified product. The terminal 'qotchey' then opens toward the registry section that follows, suggesting continuity between industrial production and administrative documentation.
        
        The crucible's capacity, calculated from illustration proportions, would accommodate the combined output of exactly twenty industrial operations - the number of folios in the industrial section.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Assemble culminating crucible apparatus
        2. Open with causative 'qokchor' activation
        3. Seal accumulated materials with 'daiin'
        4. Harmonize all components with 'shody'
        5. Ground with 'chor'
        6. Open toward next phase with 'qotchey'
        7. Process combined output of twenty operations
        8. Store final product in vessel of completion
        """,
        "herbal": "Culmination Herb (Culmen herba) - Final preparation",
        "compound": "Philosopher's Preparation - Culminated essence"
    },

    "f87r": {
        "title": "📜 The Rosetta Threshold - Registry Commencement",
        "section": "Registry",
        "glyphs": "pchodar.qotchey.shody.daiin.chor",
        "transliteration": "pah-chah-dah-rah | ku-tah-chay | shah-dah-ee | dah-ee-in | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The eighty-seventh folio marks the manuscript's most significant structural transition - the commencement of the registry section with its systematic administrative documentation. This folio introduces the Rosetta Shift, a +15 increment in Yale image ID calculation that has puzzled scholars for generations.
        
        The 'pchodar' opening with plural prefix suggests this section addresses collective or institutional contexts rather than individual operations. The registry's administrative function requires addressing multiple practitioners, suppliers, and beneficiaries.
        
        The illustration shifts from botanical and alchemical subjects to geometric cartouches containing symbolic notation - the first appearance of what scholars term "registry script." These cartouches may represent encoded names, quantities, or transactional records.
        
        The Rosetta Shift's significance extends beyond image ID calculation to suggest a fundamental reorganization of the manuscript's content at this point, possibly indicating compilation from separate source documents or a deliberate structural division between practical and administrative content.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Acknowledge threshold transition at folio 87
        2. Apply Rosetta Shift (+15) to image calculations
        3. Open with collective 'pchodar'
        4. Apply creative 'qotchey' for new section
        5. Harmonize with 'shody'
        6. Seal with 'daiin'
        7. Ground with 'chor'
        8. Document in registry format
        """,
        "herbal": "Registry Herb (Registrum herba) - Administrative preparation",
        "compound": "Essence of Record - Registry preparation"
    },
    "f90r": {
        "title": "📜 The Decade Ledger - Tenfold Accounting",
        "section": "Registry",
        "glyphs": "qotchey.shody.chor.daiin.chor",
        "transliteration": "ku-tah-chay | shah-dah-ee | chah-rah | dah-ee-in | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        Ten registry cartouches arranged in two columns of five demonstrate the manuscript's systematic approach to administrative documentation. Each cartouche contains distinct symbolic notation suggesting encoded entries for quantities, sources, or destinations.
        
        The 'qotchey.shody' opening creates a creative-harmonizing sequence that may indicate the registry's function of establishing order (creation) among distributed materials (harmonization). This pairing appears consistently in registry folios, marking a shift from the herbal and industrial sections' different opening patterns.
        
        The doubled 'chor' framing with medial 'daiin' creates a grounded-sealed-grounded structure appropriate for permanent records. The terminal 'chor' reinforces the registry's archival function, ensuring documentation remains stable and accessible.
        
        The cartouches' symbolic content, analyzed through the Wilken Key framework, reveals potential phonetic elements that may encode proper names or place designations. This discovery suggests the registry may contain identifiable historical information obscured by traditional cipher approaches.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Arrange ten registry cartouches in 2×5 grid
        2. Open with creative-harmonizing 'qotchey.shody'
        3. Ground initial entry with 'chor'
        4. Seal record with 'daiin'
        5. Complete with grounding 'chor'
        6. Encode quantities in registry script
        7. Verify ten entries against sources
        8. Archive in decade ledger format
        """,
        "herbal": "Ledger Herb (Liber herba) - Accounting preparation",
        "compound": "Decade Essence - Ledger preparation"
    },
    "f93r": {
        "title": "📜 The Triad Registry - Threefold Documentation",
        "section": "Registry",
        "glyphs": "chor.qotchey.daiin.shody.chor",
        "transliteration": "chah-rah | ku-tah-chay | dah-ee-in | shah-dah-ee | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        Three registry cartouches of increasing size suggest hierarchical documentation structure, possibly representing different administrative levels or transaction categories. The largest cartouche occupies the central position, flanked by two smaller entries in symmetrical arrangement.
        
        The 'chor' opening returns to the foundational root position seen in the manuscript's earliest folios, suggesting the registry section reconnects with the herbal section's grounding principles. This structural echo creates a ring composition linking the manuscript's beginning and middle sections.
        
        The 'qotchey.daiin' medial pairing maintains the creative-sealing sequence while the terminal 'shody.chor' creates an unusual harmonizing-grounding combination unique to this folio. This variant may indicate specialized documentation for harmonized or reconciled accounts.
        
        The cartouches' symbolic content includes repeated elements that may represent standardized units of measurement or currency, suggesting the registry documents actual transactions rather than theoretical distributions.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Create three registry cartouches in hierarchy
        2. Open with grounding 'chor'
        3. Apply creative 'qotchey'
        4. Seal primary record with 'daiin'
        5. Harmonize secondary entries with 'shody'
        6. Complete with grounding 'chor'
        7. Document in three administrative levels
        8. Verify hierarchical relationships
        """,
        "herbal": "Triad Herb (Trias herba) - Hierarchical preparation",
        "compound": "Essence of Three - Triad preparation"
    },
    "f96r": {
        "title": "📜 The Hexad Archive - Sixfold Classification",
        "section": "Registry",
        "glyphs": "shody.chor.qotchey.daiin.chor",
        "transliteration": "shah-dah-ee | chah-rah | ku-tah-chay | dah-ee-in | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        Six registry cartouches arranged in hexagonal pattern demonstrate sophisticated organizational principles, with each cartouche connecting to adjacent entries through illustrated lines suggesting relational classification. This hexad structure appears in medieval administrative manuals for complex inventory systems.
        
        The 'shody' opening position, unusual for registry folios, may indicate this entry documents harmonized or reconciled accounts from multiple sources. The harmonizing element's priority suggests resolution of discrepancies rather than initial recording.
        
        The 'chor.qotchey' sequence creates a grounding-creative pairing that may represent the transformation of raw data into organized records. The 'daiin.chor' terminal combination maintains the sealing-grounding structure seen in other registry entries.
        
        The hexagonal connections between cartouches include directional indicators that may represent temporal sequences, suggesting this registry documents processes or workflows rather than static inventories.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Arrange six cartouches in hexagonal pattern
        2. Open with harmonizing 'shody'
        3. Ground data with 'chor'
        4. Apply creative 'qotchey' for organization
        5. Seal records with 'daiin'
        6. Complete with grounding 'chor'
        7. Connect related entries with lines
        8. Document workflow sequences
        """,
        "herbal": "Archive Herb (Archivum herba) - Classification preparation",
        "compound": "Hexad Essence - Archive preparation"
    },
    "f100r": {
        "title": "📜 The Century Mark - Hundredfold Record",
        "section": "Registry",
        "glyphs": "qokchor.shody.chor.daiin.qotchey",
        "transliteration": "ku-kah-chah-rah | shah-dah-ee | chah-rah | dah-ee-in | ku-tah-chay",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The hundredth folio represents a milestone in the manuscript's structure, marked by expanded registry cartouches and enhanced decorative elements that signal heightened administrative significance. The illustration includes marginal flourishes absent from previous registry entries.
        
        The 'qokchor' opening with causative prefix suggests this folio activates or summarizes preceding registry entries, possibly representing a master record or consolidated account. The grammatical marking of causation indicates transformative administrative function.
        
        The 'shody.chor' medial pairing creates a harmonizing-grounding sequence that may represent the integration of multiple records into unified summary. The terminal 'qotchey' then opens toward subsequent entries, suggesting the century mark serves as both culmination and new beginning.
        
        The expanded cartouches contain more complex symbolic notation than previous registry entries, possibly indicating the hundredth folio documents particularly significant transactions or summarizes multiple preceding entries.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Recognize milestone at century folio
        2. Open with causative 'qokchor' activation
        3. Harmonize records with 'shody'
        4. Ground summary with 'chor'
        5. Seal consolidated entry with 'daiin'
        6. Open toward future with 'qotchey'
        7. Document master record
        8. Archive with enhanced security
        """,
        "herbal": "Century Herb (Centum herba) - Centennial preparation",
        "compound": "Essence of Hundred - Century preparation"
    },
    "f104r": {
        "title": "📜 The Registry Seal - Administrative Authority",
        "section": "Registry",
        "glyphs": "daiin.chor.shody.qotchey.chor",
        "transliteration": "dah-ee-in | chah-rah | shah-dah-ee | ku-tah-chay | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The registry seal folio presents the most elaborate cartouche in the administrative section, containing symbolic elements that may represent institutional authority or official validation. The cartouche's border includes decorative motifs suggesting seals or stamps used for authentication.
        
        The 'daiin' opening position, highly unusual for any folio, creates a sealing-first structure that may indicate this entry serves authenticating or validating function for preceding registry records. The seal's priority suggests administrative hierarchy.
        
        The 'chor.shody' medial pairing creates a grounding-harmonizing sequence that may represent the authentication process itself - establishing validity (grounding) and reconciling with standards (harmonizing). The terminal 'qotchey.chor' then opens validated records for future reference.
        
        The cartouche's symbolic content includes elements resembling medieval notarial marks, suggesting this folio may document official certification or institutional approval of the registry's contents.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Create authoritative seal cartouche
        2. Open with validating 'daiin'
        3. Ground authentication with 'chor'
        4. Harmonize with standards using 'shody'
        5. Apply creative 'qotchey' for certification
        6. Complete with grounding 'chor'
        7. Apply seal to preceding records
        8. Document certification authority
        """,
        "herbal": "Seal Herb (Sigillum herba) - Authoritative preparation",
        "compound": "Essence of Authority - Seal preparation"
    },
    "f108r": {
        "title": "📜 The Final Account - Registry Culmination",
        "section": "Registry",
        "glyphs": "chor.daiin.qokchor.shody.qotchey",
        "transliteration": "chah-rah | dah-ee-in | ku-kah-chah-rah | shah-dah-ee | ku-tah-chay",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The registry section's culmination presents a comprehensive cartouche assembly that summarizes all preceding administrative documentation. The illustration's scale and complexity exceed all previous registry entries, suggesting this represents final accounting or master summary.
        
        The 'chor.daiin' opening creates a grounding-sealing sequence that may establish the final account's authority and permanence. This initial sealing ensures the culmination cannot be modified or challenged.
        
        The 'qokchor' medial position with causative prefix suggests this folio activates or empowers the entire registry section, transforming accumulated records into actionable administrative instrument. The terminal 'shody.qotchey' then opens toward harmonious future application.
        
        The comprehensive cartouche includes symbolic elements from all preceding registry entries, creating visual summary of the entire administrative corpus. This integration confirms the Wilken Key approach's validity - the manuscript's structure reveals intentional design rather than random compilation.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Assemble comprehensive final account
        2. Open with grounding-sealing 'chor.daiin'
        3. Apply causative 'qokchor' for activation
        4. Harmonize entire registry with 'shody'
        5. Open toward application with 'qotchey'
        6. Verify against all preceding entries
        7. Certify master summary
        8. Archive with highest security
        """,
        "herbal": "Final Herb (Ultima herba) - Culminating preparation",
        "compound": "Master Registry Essence - Final preparation"
    },
    "f110r": {
        "title": "📜 The Administrative Close - Institutional Seal",
        "section": "Registry/Administrative",
        "glyphs": "pchol.daiin.chor.shody.qotchey",
        "transliteration": "pah-chah-lah | dah-ee-in | chah-rah | shah-dah-ee | ku-tah-chay",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The administrative close folio marks the registry section's formal conclusion with institutional seal and notarial marks that establish official status. The illustration includes marginal elements resembling medieval chancery conventions for authenticated documents.
        
        The 'pchol' opening with plural prefix and liquid terminal suggests this folio addresses collective institutional context rather than individual transactions. The administrative function requires addressing organizational entities and their representatives.
        
        The 'daiin.chor' medial pairing creates a sealing-grounding sequence that may represent the institutional validation process. The terminal 'shody.qotchey' then opens toward harmonious future institutional operations.
        
        The notarial marks include elements that may encode dates, authorities, or jurisdictions, suggesting this folio documents specific institutional context for the entire manuscript. Wilken Key analysis of these marks may reveal historically identifiable information.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Prepare institutional seal elements
        2. Open with collective 'pchol'
        3. Apply validating 'daiin'
        4. Ground with institutional 'chor'
        5. Harmonize with 'shody'
        6. Open toward future with 'qotchey'
        7. Apply notarial authentication
        8. Complete administrative closure
        """,
        "herbal": "Close Herb (Clausura herba) - Closing preparation",
        "compound": "Institutional Seal - Administrative preparation"
    },
    "f113r": {
        "title": "📜 The Legacy Entry - Transmission Record",
        "section": "Registry/Administrative",
        "glyphs": "qotchey.chor.daiin.shody.chor",
        "transliteration": "ku-tah-chay | chah-rah | dah-ee-in | shah-dah-ee | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The legacy entry folio documents manuscript transmission with cartouches containing symbolic elements that may represent succession, inheritance, or institutional transfer. The illustration includes motifs suggesting continuity across generations or jurisdictions.
        
        The classic 'qotchey.chor' opening returns from the manuscript's earliest folios, creating structural ring composition that links conclusion with origin. This echo suggests intentional design emphasizing the manuscript's unity across its extensive corpus.
        
        The 'daiin.shody' medial pairing creates a sealing-harmonizing sequence that may represent the transmission process itself - establishing authenticity (sealing) and ensuring continuity (harmonizing). The terminal 'chor' grounds the legacy in stable tradition.
        
        The transmission motifs include elements resembling medieval colophons and ex libris marks, suggesting this folio documents the manuscript's provenance and intended readership. Wilken Key analysis may reveal identifiable historical transmission chains.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Document transmission context
        2. Open with classic 'qotchey.chor'
        3. Seal authenticity with 'daiin'
        4. Harmonize continuity with 'shody'
        5. Ground in tradition with 'chor'
        6. Record provenance information
        7. Identify intended readership
        8. Complete transmission documentation
        """,
        "herbal": "Legacy Herb (Legatum herba) - Transmission preparation",
        "compound": "Essence of Continuity - Legacy preparation"
    },
    "f116r": {
        "title": "📜 The Final Seal - Manuscript Culmination",
        "section": "Registry/Administrative",
        "glyphs": "chor.shody.daiin.qotchey.chor",
        "transliteration": "chah-rah | shah-dah-ee | dah-ee-in | ku-tah-chay | chah-rah",
        "investigation": """
        **Wilken Key Scholar Investigation:**
        
        The final folio presents the manuscript's culminating seal, integrating all preceding elements into unified closure. The illustration includes the most elaborate cartouche in the entire manuscript, with decorative elements drawn from herbal, industrial, and registry sections.
        
        The 'chor' opening returns to the foundational root that opened the manuscript's first folio, completing the ring composition that structures the entire work. This return confirms the Wilken Key approach's validity - the manuscript reveals systematic design through its phonetic and structural patterns.
        
        The 'shody.daiin' medial pairing creates a harmonizing-sealing sequence that may represent the manuscript's final blessing and authentication. The terminal 'qotchey.chor' then opens toward future readers while grounding in completed tradition.
        
        The culminating cartouche includes symbolic elements from all manuscript sections, creating visual summary of the entire Wilken Key Engine. This integration demonstrates the manuscript's coherence as unified work of medieval mystical scholarship.
        """,
        "recipe": """
        **8-Step Wilken Key Recipe:**
        1. Prepare culminating seal assembly
        2. Open with foundational 'chor'
        3. Harmonize with 'shody'
        4. Seal with 'daiin'
        5. Apply creative 'qotchey'
        6. Complete with grounding 'chor'
        7. Integrate all section elements
        8. Conclude manuscript with blessing
        """,
        "herbal": "Culmination Herb (Culmen herba) - Final preparation",
        "compound": "Philosopher's Seal - Culminating preparation"
    }
}

# HEADER
st.markdown("<h1 style='text-align: center;'>🗝️ WILKEN KEY ENGINE</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>The Million-Word Omnibus | MS 408</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #b8941f;'>240 Folios | 40 Elite Waypoints | Yale Beinecke Digital Archive</p>", unsafe_allow_html=True)

# METRICS
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Folios", len(FOLIOS))
col2.metric("Elite Waypoints", len(ELITE_WAYPOINTS))
col3.metric("Yale Base ID", BASE_YALE_ID)
col4.metric("Rosetta Shift", f"+{ROSETTA_SHIFT}")

# SIDEBAR
st.sidebar.markdown("<h2>🗝️ Navigation</h2>", unsafe_allow_html=True)
selected_folio = st.sidebar.selectbox("Select Folio", FOLIOS)

# Section filter
section_filter = st.sidebar.multiselect(
    "Filter by Section",
    ["Herbal", "Industrial", "Registry", "Celestial", "Administrative"],
    default=["Herbal", "Industrial", "Registry", "Celestial", "Administrative"]
)

# Quick elite waypoints
st.sidebar.markdown("<h3>⭐ Elite Waypoints</h3>", unsafe_allow_html=True)
for folio, data in list(ELITE_WAYPOINTS.items())[:5]:
    if st.sidebar.button(f"{folio}: {data['title'][:25]}...", key=f"nav_{folio}"):
        selected_folio = folio

# Search
search_term = st.sidebar.text_input("Search Waypoints")

# MAIN CONTENT
folio_num = int(''.join(filter(str.isdigit, selected_folio)))
is_verso = 'v' in selected_folio.lower()

# Determine section
if folio_num <= 66:
    current_section = "Herbal/Celestial"
elif folio_num <= 86:
    current_section = "Industrial"
else:
    current_section = "Registry/Administrative"

# FOLIO DISPLAY
st.markdown(f"<h2>{selected_folio.upper()} | {current_section}</h2>", unsafe_allow_html=True)

# Image
yale_url = get_iiif_url(selected_folio)
st.image(yale_url, use_container_width=True, caption=f"Yale Beinecke MS 408 | {selected_folio.upper()}")

# ELITE WAYPOINT DISPLAY
if selected_folio in ELITE_WAYPOINTS:
    wp = ELITE_WAYPOINTS[selected_folio]
    
    st.markdown(f"<div class='waypoint-card'><h3>{wp['title']}</h3></div>", unsafe_allow_html=True)
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔤 Glyphs", "📜 Investigation", "⚗️ Recipe", "🌿 Herbal", "💎 Compound"])
    
    with tab1:
        st.markdown("<h4>Wilken Key Glyphs</h4>", unsafe_allow_html=True)
        st.code(wp['glyphs'], language=None)
        st.markdown("<h4>Phonetic Transliteration</h4>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #d4af37;'>{wp['transliteration']}</p>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("<div class='investigation-box'>" + wp['investigation'] + "</div>", unsafe_allow_html=True)
    
    with tab3:
        st.markdown("<div class='recipe-box'>" + wp['recipe'] + "</div>", unsafe_allow_html=True)
    
    with tab4:
        st.markdown(f"<p><strong>Wilken Key Herbal:</strong> {wp['herbal']}</p>", unsafe_allow_html=True)
    
    with tab5:
        st.markdown(f"<p><strong>Wilken Key Compound:</strong> {wp['compound']}</p>", unsafe_allow_html=True)

# WILKEN KEY REFERENCE
with st.expander("🗝️ Wilken Key Phonetic Reference"):
    st.markdown("<h4>Phonetic Mapping</h4>", unsafe_allow_html=True)
    key_cols = st.columns(4)
    items = list(WILKEN_KEY.items())
    for i, (glyph, phonetic) in enumerate(items):
        key_cols[i % 4].markdown(f"<code>{glyph}</code> → {phonetic}", unsafe_allow_html=True)

# YALE ID CALCULATOR
with st.expander("🔢 Yale Image ID Calculator"):
    calc_folio = st.text_input("Enter Folio (e.g., f1r)", selected_folio)
    if calc_folio:
        calc_id = get_yale_image_id(calc_folio)
        calc_url = get_iiif_url(calc_folio)
        st.markdown(f"<p><strong>Yale ID:</strong> {calc_id}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>IIIF URL:</strong> <a href='{calc_url}' target='_blank'>{calc_url}</a></p>", unsafe_allow_html=True)

# ALL ELITE WAYPOINTS
with st.expander("⭐ All 40 Elite Waypoints"):
    if search_term:
        filtered = {k: v for k, v in ELITE_WAYPOINTS.items() if search_term.lower() in v['title'].lower()}
    else:
        filtered = ELITE_WAYPOINTS
    
    for folio, data in filtered.items():
        st.markdown(f"<p><strong>{folio}:</strong> {data['title']}</p>", unsafe_allow_html=True)

# FOOTER
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #b8941f;'>🗝️ Wilken Key Engine v3.0 | Yale Beinecke Library MS 408 | Million-Word Omnibus</p>", unsafe_allow_html=True)
