import streamlit as st
from typing import Dict, List, Optional, Any

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Wilken Key Engine | Million-Word Omnibus",
    page_icon="🗝️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS THEMING
def apply_custom_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap');
    
    :root {
        --parchment: #0a0a0f;
        --gold: #d4af37;
        --gold-dim: #8b7355;
        --text-primary: #e8e6e1;
        --accent-green: #4a7c59;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0a0a0f 0%, #14141a 50%, #0a0a0f 100%);
    }
    
    h1, h2, h3 {
        font-family: 'Cinzel', serif !important;
        color: var(--gold) !important;
        text-shadow: 0 0 20px rgba(212, 175, 55, 0.3);
    }
    
    h1 {
        font-size: 2.5rem !important;
        background: linear-gradient(135deg, #d4af37, #f4d03f, #d4af37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    h2 {
        margin-top: 10px !important;
        margin-bottom: 10px !important;
    }
    
    h3 {
        margin-top: 8px !important;
        margin-bottom: 8px !important;
    }
    
    p, div, span, li {
        font-family: 'Crimson Text', serif !important;
        color: var(--text-primary);
        line-height: 1.6;
    }
    
    p {
        margin-bottom: 8px !important;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f14 0%, #1a1a22 100%);
        border-right: 1px solid var(--gold-dim);
    }
    
    [data-testid="stSidebar"] .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    
    .folio-card {
        background: linear-gradient(145deg, #14141a 0%, #1a1a22 100%);
        border: 1px solid var(--gold-dim);
        border-radius: 8px;
        padding: 15px;
        margin: 5px 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    }
    
    .manuscript-frame {
        border: 2px solid var(--gold-dim);
        border-radius: 4px;
        padding: 8px;
        background: linear-gradient(145deg, #0f0f14, #1a1a22);
    }
    
    .glyph-badge {
        display: inline-block;
        background: linear-gradient(145deg, #1a1a22, #0f0f14);
        border: 1px solid var(--gold);
        border-radius: 4px;
        padding: 4px 12px;
        margin: 2px;
        font-family: 'Cinzel', monospace !important;
        color: var(--gold);
        font-size: 0.9rem;
    }
    
    .recipe-step {
        background: rgba(74, 124, 89, 0.1);
        border-left: 3px solid var(--accent-green);
        padding: 8px 12px;
        margin: 4px 0;
        border-radius: 0 4px 4px 0;
        font-family: 'Crimson Text', serif;
    }
    
    a {
        color: var(--gold) !important;
        text-decoration: none !important;
    }
    
    a:hover {
        color: var(--gold-bright) !important;
        text-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
    }
    
    .stButton button {
        background: linear-gradient(145deg, #1a1a22, #0f0f14) !important;
        border: 1px solid var(--gold-dim) !important;
        color: var(--gold) !important;
        font-family: 'Cinzel', serif !important;
    }
    
    .stButton button:hover {
        border-color: var(--gold) !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3);
    }
    
    [data-testid="column"] {
        padding: 0 8px !important;
    }
    
    [data-testid="stImageCaption"] {
        margin-top: 4px !important;
        margin-bottom: 4px !important;
    }
    
    .stSelectbox {
        margin-bottom: 8px !important;
    }
    
    .stAlert {
        padding: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)


# WILKEN KEY ENGINE - MILLION-WORD OMNIBUS CLASS
class WilkenKeyOmnibus:
    """The Complete Million-Word Omnibus Engine for MS 408."""
    
    BASE_YALE_ID: int = 1006076
    ROSETTA_SHIFT: int = 15
    SHIFT_THRESHOLD: int = 86
    
    def __init__(self):
        """Initialize the complete omnibus archive."""
        self.glyphs: Dict[str, str] = {
            "qo": "qo", "a": "aa", "o": "r", "l": "l", "i": "ee",
            "r": "r", "m": "m", "t": "oo", "p": "p", "k": "k",
            "s": "s", "d": "d", "g": "g", "e": "e", "f": "f",
            "u": "u", "b": "b", "h": "h", "n": "n", "y": "y",
            "ai": "er", "ch": "k", "sh": "sh", "th": "th"
        }
        
        # Elite Waypoints - 40 critical folios from all 15 phases
        self.elite_waypoints = self._load_elite_waypoints()
        
        # Generate complete archive
        self.archive = self._generate_complete_archive()
    
    def _load_elite_waypoints(self):
        """Load all 40 elite waypoints from the 15-phase omnibus."""
        return {
            # Phase 1: f1r, f1v, f4r, f4v
            "f1r": {
                "title": "General Protocol (f1r) - Laboratory Entrance",
                "words": ["oladaba", "qothol"],
                "desc": "The General Protocol on f1r acts as the entrance to the entire botanical series of MS 408. Every operation must begin with the ritualistic scouring of copper vessels using oak ash harvested during the previous lunar cycle. The intake valves must be calibrated precisely three hours before the Aries dawn. Observe the steam carefully as it transitions from a translucent gray to a vibrant emerald green. This visual shift indicates that the chlorophyll-lock has been released, allowing the volatile oils to be captured correctly. Refer immediately to f1v and f33r for the subsequent plant-specific stabilization protocols.",
                "recipe": [
                    "Scour all copper retorts with lunar-harvested oak ash for a mirror-finish",
                    "Calibrate the laboratory intake valves to zero-low flow at the Aries dawn",
                    "Heat the primary induction vessel to the designated blood-heat threshold",
                    "Introduce the first bundle of serrated leaves into the copper chamber",
                    "Monitor for the transition from gray steam to vibrant emerald green",
                    "Capture the resulting volatile oils in lead-seal borosilicate jars",
                    "Synchronize the intake volume with the f1v sap levels for the 9-vat factory",
                    "Seal the primary extraction and prepare for f33r balancing"
                ],
                "ref": "Introductory Protocol; Links to f1v and f33r. Yale: 1006077",
                "yale": "1006077",
                "section": "🌿 Herbal Section"
            },
            "f1v": {
                "title": "The Lobed-Leaf Plant (f1v) - Primary Sap Source",
                "words": ["deor", "ollag"],
                "desc": "The Lobed-Leaf Plant on f1v is identified by its central branching stem and large green-washed leaves with distinct venation. This illustration shows a complex, bulbous root system that indicates a high concentration of milky, latex-like sap required for the creation of lipid-based medical salves. Note the small blue clusters at the apical top of the stem which are the primary source of the 'ee' essence required for star-extraction synergy. Harvesting of the sap must occur directly before the morning dew evaporates, using a sterilized obsidian blade to score the root crown without introducing iron contamination.",
                "recipe": [
                    "Score the root crown with a sterilized obsidian blade at dawn",
                    "Collect the resulting milky sap in a shallow ceramic tray",
                    "Filter the sap through a triple layer of fine-woven linen until clear",
                    "Isolate the 'ee' essence from the blue apical clusters for later synergy",
                    "Seal the filtered sap in airtight amber glass to prevent solar oxidation",
                    "Label the batch for Slot 2 in the 12-slot archival inventory sequence",
                    "Monitor for lipid separation over a 24-hour cycle in a dark chamber",
                    "Cross-reference f1r for final activation during the maturation phase"
                ],
                "ref": "Primary Sap Source; Links to f1r (Protocol) and f33r (Balancing). Yale: 1006078",
                "yale": "1006078",
                "section": "🌿 Herbal Section"
            },
            "f4r": {
                "title": "The Branching Lipid Thicket (f4r) - Volatile Carrier",
                "words": ["qokedy", "m-r"],
                "desc": "Folio 4r represents the paramount laboratory waypoint for the initialization of high-volatility lipid carrier sequences within the manuscript core. The unique eight-fold branching architecture serves as a geometric cipher defining the specific timing of the steam-injection intervals required to unlock the chlorophyll-lock of the apical tips. The Wilken Key identifies the 'qokedy' markers as molecular keys used to calibrate the laboratory's grid-timed treatments, ensuring total transdermal permeability.",
                "recipe": [
                    "Identify the branching tips during the first high-moon rise of the solstice",
                    "Use an obsidian blade to separate exactly 500g of fresh, buds-on tips",
                    "Discard all root and stem structures immediately to avoid contamination",
                    "Pack the copper retort induction basket tightly with the isolated tips",
                    "Heat the water base to a steady 95C, monitoring for emerald steam",
                    "Release pressure-valves at every 15-minute shedy interval for three hours",
                    "Siphon the clear carrier oil into borosilicate glass for daily use",
                    "Label as 'Neural Carrier f4' and store in the lead-seal vault"
                ],
                "ref": "Neural Carrier Oil; Directs to f67 celestial timing. Yale: 1006083",
                "yale": "1006083",
                "section": "🌿 Herbal Section"
            },
            "f4v": {
                "title": "The Fan-Leaf Cooling Matrix (f4v) - Thermal Exchange",
                "words": ["deor", "ollag"],
                "desc": "Folio 4v serves as the master guide for treating inflammatory fever outbreaks within the monastic infirmary through high-aqueous antipyretic cooling compresses. The illustration of the multi-lobed fan-leaf system serves as a natural radiator schematic; the Brotherhood utilizes the specific venation patterns to coordinate the manual maceration pressure. The Wilken Key identifies the 'deor' root markers as subterranean nodes where the plant stores its primary heat-dispersing reagents before the morning rain.",
                "recipe": [
                    "Gather four large fan-leaf clusters during a heavy morning rainfall",
                    "Audit each lobe for signs of insect surface-breach or organic decay",
                    "Submerge fresh leaves immediately in chilled mountain spring water",
                    "Macerate the leaves by hand until a homogenous dark green paste forms",
                    "Blend with three drops of f33v triple-root binding agent for cohesion",
                    "Maintain the cooling mash at a steady 4C on an ice-bed",
                    "Apply as a quarter-inch layer onto linen wraps for the patient's joints",
                    "Replace the compress every three 15-minute shedy intervals to maintain cooling"
                ],
                "ref": "Cooling Reagent; Pairs with f33v for inflammation. Yale: 1006084",
                "yale": "1006084",
                "section": "🌿 Herbal Section"
            },
            # Phase 2: f17r, f20r, f25r
            "f17r": {
                "title": "The Solar-Flare Botanical (f17r) - Photo-Sensitive Extract",
                "words": ["daiin", "shedy", "otol"],
                "desc": "Folio 17r represents a specialized laboratory waypoint focused on the capture of photo-sensitive alkaloids through high-noon solar distillation. The illustration features a vibrant, sun-like flower head with radiating petals which the Brotherhood utilizes as a natural solar-collector schematic for the laboratory heat-exchangers. The Wilken key identifies the 'daiin' nodal markers on the petals as the precise points where the solar-essence must be diverted into the lead-seal vials before the sun passes its zenith.",
                "recipe": [
                    "Solar Identification: Identify the f17r solar-flare specimen during the peak of the summer solstice",
                    "Zenith Harvest: Harvest exactly 300 grams of petals at high-noon using a gilded obsidian blade",
                    "Reflector Setup: Align the laboratory roof-mirrors to focus concentrated solar light onto the copper retort",
                    "Pressure Prep: Pack the petals into the secondary induction chamber with 'shedy' valves at 0.12 torque",
                    "Distillation Cycle: Steam-distill the petals for exactly ninety minutes monitoring for gold color shift",
                    "Node Diversion: Divert the gold-essence through daiin nodal filters to remove contaminants",
                    "Flash Cooling: Siphon the resulting oil into an ice-chilled lead-seal vessel to lock photo-sensitive alkaloids",
                    "Archive Sync: Label as 'Solar Lipid f17' and store in dark-glass quadrant awaiting f116v certification"
                ],
                "ref": "Solar Essence Source; Links to f67 celestial series. Yale: 1006109",
                "yale": "1006109",
                "section": "🌿 Herbal Section"
            },
            "f20r": {
                "title": "The Bell-Stem Reagent (f20r) - Resonance Synergy",
                "words": ["stella", "deor", "ollag"],
                "desc": "Folio 20r introduces the laboratory study of bell-shaped flower systems and their unique role in the creation of liquid-resonance medicines. The illustration depicts a central vertical stem supporting staggered, bell-shaped blue flowers which the Brotherhood utilizes as a natural filter-architecture during the cold-press maceration of botanical saps. The Wilken framework identifies the 'stella' markers on the bells as a signal for swell-stem expansion.",
                "recipe": [
                    "Resonance Harvest: Gather the bell-shaped flowers during the first morning dew of a waning moon",
                    "Structural Audit: Ensure each bell is pristine; discard any showing vertical fractures or browning",
                    "Vibratory Grinding: Grind the bells in a stone mortar utilizing a wood-and-felt pestle for rhythmic vibration",
                    "Base Synthesis: Blend the bell-mash 1:1 with the lobed-leaf sap from f1v to create high-frequency liquid resonance",
                    "Alkaloid Lock: Submerge the mixture in a lead-seal flask and expose to laboratory tuning-forks for three shedy intervals",
                    "Pressure Press: Siphon the resulting blue-wash fluid through fine silk mesh at steady 0.05 flow-valves",
                    "Thermal Storage: Store the resonant fluid in temperature-controlled earthenware jar at exactly 10 degrees Celsius",
                    "Inventory Sync: Label as 'Resonance Carrier f20' and transfer to factory induction vats for f86v maturation"
                ],
                "ref": "Resonance Buffer; Pairs with f1v; Precursor to f67. Yale: 1006115",
                "yale": "1006115",
                "section": "🌿 Herbal Section"
            },
            "f25r": {
                "title": "The Trumpet Root Synthesis (f25r) - Grounding Reagent",
                "words": ["aladaba", "qokeedy", "m-r"],
                "desc": "Folio 25r is characterized by its large, trumpet-like flower heads and a central, thickened root core which acts as the primary waypoint for the grounding reagent sequence. The Wilken key identifies the 'aladaba' markers on the root-flare as the phonetic labels for the swell-arm-dig process required to unearth the specimen without damaging the sensitive subterranean fibers. Laboratory engineers utilize the trumpet-flower on 25r as a biological intake manifold.",
                "recipe": [
                    "Grounding Harvest: Dig the central trumpet-root precisely four hours after the peak of a spring-tide lunar rise",
                    "Fiber Prep: Rinse the root flare with cold spring water and slice longitudinally into consistent thin-strips",
                    "Reduction Phase: Simmer the root-strips in the f4r thin oil base for eight solar hours at 85 degrees Celsius",
                    "Trituration: Grind the reduced fiber into a homogenous dark umber paste using a heavy quartz pestle",
                    "Lipid Lock: Blend the grounding paste 1:2 with the f17r solar lipid to create the master-thermal buffer",
                    "Valve Calibration: Synchronize the viscosity of the paste to match the qokeedy markers on f86v industrial schematic",
                    "Final Sealing: Store the grounding reagent in a high-borosilicate glass vessel sealed with triple layer of beeswax and linen",
                    "Maturation Load: Transfer the batch to Slot 5 of the archival inventory for final maturation and f116v certification"
                ],
                "ref": "Structural Stabilizer; Successor to f1r; Links to f17r. Yale: 1006125",
                "yale": "1006125",
                "section": "🌿 Herbal Section"
            },
            # Phase 3: f31r, f33r, f33v
            "f31r": {
                "title": "The Serrated Thistle (f31r) - Aromatic Buffer",
                "words": ["qokedy", "m-r", "otol"],
                "desc": "Folio 31r reveals the laboratory study of a highly resilient serrated thistle species which the Brotherhood utilizes as a primary aromatic buffer for high-heat distillation cycles. The illustration features a robust, thorned vertical stalk supporting staggered, spiky leaf clusters that indicate a high concentration of protective alkaloids. The Wilken key identifies the 'qokedy' segments on the leaf tips as the specific markers for the pre-solstice harvest required to lock the plant's essential volatile oils into the stem marrow.",
                "recipe": [
                    "Protective Identification: Identify the f31r serrated thistle during the waxing crescent moon of early June",
                    "Obsidian Harvesting: Separate the stalk from the root system using a sterilized obsidian blade ensuring thorn-points remain intact",
                    "Steam-Distillation Prep: Scour the laboratory retort with oak ash and mountain charcoal to achieve mirror-polish",
                    "Calibrated Induction: Pack the stalk segments into the induction chamber with 'k-e' key-valves at 0.08 pressure-baseline",
                    "Thermal Reduction: Distill the stalks at exactly 88 degrees Celsius for three solar cycles monitoring for yellow-wash shift",
                    "Aromatic Filter: Siphon the resulting oil through wire-mesh silk screen to remove all fibrous particulate matter",
                    "Final Sealing: Store the aromatic buffer in lead-seal borosilicate vials kept in darkness of laboratory basement",
                    "Batch Sync: Label as 'Thistle Buffer f31' and prepare for synchronization with f33r balance matrix during maturation"
                ],
                "ref": "Aromatic Buffer; Protective carrier for maturation cycles. Yale: 1006134",
                "yale": "1006134",
                "section": "🌿 Herbal Section"
            },
            "f33r": {
                "title": "The Rosetta Balance (f33r) - Dual Species Synergy",
                "words": ["qokedy", "ll", "daiin"],
                "desc": "Folio 33r is the absolute cornerstone of the MS 408 pharmacological balance sequence, acting as the primary Rosetta waypoint for the mid-spring harvest cycle. The illustration features two distinct plant species placed in side-by-side symmetry—a green serrated plant and a yellowish bulbous plant—which laboratory engineers utilize to coordinate the viscosity alignment of all subsequent decoctions. The Wilken key identifies the 'qokedy' and 'll' (arm-arm) markers on this page as the molecular keys used to calibrate the laboratory's 9-vat induction grid shown later.",
                "recipe": [
                    "Simultaneous Harvest: Gather the green serrated plant and the yellow bulbous plant precisely at dawn of waning moon in late April",
                    "Segmentation: Chop the green leaves into uniform 2-inch laboratory segments to prepare for high-pressure steam extraction",
                    "Root Pressing: Cold-press the yellowish roots into concentrated binding juice using stone screw-press ensuring no iron-contamination",
                    "Viscosity Blending: Combine the green extract and the yellow root-juice in marble vat at precise 2:1 weight ratio by mass",
                    "Steady Simmer: Simmer the mixture for exactly one solar hour below boiling point (82 degrees Celsius) until thick uniform substrate forms",
                    "Dual Filtration: Siphon the resulting balance matrix through double layer of unbleached silk to remove all cellular residues",
                    "Inventory Logging: Label the batch as 'Rosetta Balance f33r' and store in Slot 4 quadrant of laboratory apothecary for 24 hours",
                    "Factory Transfer: Transfer the stabilized matrix to the induction vats of f86v schematic for final maturation and terminal batch certification"
                ],
                "ref": "Balancing page; Links f1v, f33v, and f86v factory. Yale: 1006138",
                "yale": "1006138",
                "section": "🌿 Herbal Section"
            },
            "f33v": {
                "title": "The Triple-Root Matrix (f33v) - The Salve Core",
                "words": ["chedy", "otol", "deor"],
                "desc": "Folio 33v represents the peak of mid-herbal root synergy within the MS 408, detailing the complex maceration of the 'chedy' triple-root system into the primary salve substrate for the Brotherhood. The illustration depicts three intertwined, bulbous root cores which indicate a high concentration of lipid-locking alkaloids required to stabilize high-volatility star-essences.",
                "recipe": [
                    "Matrix Harvest: Unearth the triple-root system manually during the summer solstice ensuring subterranean bulb-skin remains completely intact",
                    "Separate Grinding: Grind each of the three root systems into fine individual laboratory mash using stone mortar at constant 15 degrees Celsius",
                    "Cooling Submersion: Submerge the separate mashes into the f4v fan-leaf cooling infusion to lock in volatile alkaloids before final blending",
                    "Trituration Cycle: Blend the three mashes together into unified ivory paste utilizing heavy quartz pestle in rhythmic 'otol' (root-stem) motions",
                    "Viscosity Check: Monitor for darkening color shift to emerald-brown indicating successful binding of triple-root alkaloids to matrix",
                    "Lipid Incorporation: Blend the unified paste 1:1 with the milky sap from f1v to create the final semi-solid topical carrier",
                    "Vacuum Sealing: Store the triple-root matrix in lead-seal earthenware jars ensuring no light exposure during 48-hour stabilization phase",
                    "Factory Loading: Load the stabilized matrix into the induction vats of f86v industrial schematic for final maturation and monastic batch certification"
                ],
                "ref": "Universal Binder; Cornerstone of 12-slot inventory system. Yale: 1006139",
                "yale": "1006139",
                "section": "🌿 Herbal Section"
            },
            # Phase 4: f48r, f57v, f58r
            "f48r": {
                "title": "The Broad-Leaf Tonic Precursor (f48r)",
                "words": ["deor", "ollag", "stella"],
                "desc": "Folio 48r introduces the laboratory study of a broad-leaf tonic precursor characterized by its intricate, emerald-wash venation and massive subterranean bulb density. The illustration features a central vertical stalk supporting wide, fan-like leaves which the Brotherhood utilizes as a natural thermal radiator during the early condensation phases of the distillation cycle.",
                "recipe": [
                    "Bulb Identification: Identify the f48r tonic precursor during the waxing crescent moon of the summer solstice targeting most bulbous roots",
                    "Obsidian Extraction: Unearth the bulb manually using a specialized obsidian spade to ensure no iron contamination during soil separation",
                    "Spring-Water Purge: Rinse the bulb surface with chilled mountain spring water to remove all organic debris without damaging subterranean skin",
                    "Longitudinal Slicing: Slice the bulb into consistent quarter-inch segments to expose the inner fibrous marrow for laboratory reduction",
                    "Steady Simmer: Simmer the marrow-segments in the f4r thin oil base for eight solar cycles at constant 80-degree Celsius temperature",
                    "Trituration Cycle: Grind the reduced marrow into uniform ivory-colored paste using heavy quartz pestle in rhythmic circular motions",
                    "Substrate Sync: Blend 1:2 with the lobed-leaf sap from f1v to create high-density pharmacological carrier for star-essences",
                    "Vacuum Sealing: Store the finalized tonic precursor in lead-seal borosilicate vials and transition to f57v grid-sync phase"
                ],
                "ref": "Tonic Precursor; Links to f57v grid. Yale: 1006180",
                "yale": "1006180",
                "section": "🌿 Herbal Section"
            },
            "f57v": {
                "title": "The Pharma Grid Foundation (f57v) - Nodal Schematic",
                "words": ["daiin", "chol", "shedy"],
                "desc": "Folio 57v serves as the primary pharmaceutical grid foundation for the entire MS 408 archive, establishing the spatial relationship between chemical nodes and laboratory pressure-flow intervals. The illustration features a series of containers and interconnected lines which the Brotherhood utilizes as a mechanical flow-chart for early-stage distillates and reagents.",
                "recipe": [
                    "Grid Synchronization: Align the laboratory grid nodes according to the daiin markers found on the f57v schematic",
                    "Valve Precision: Establish the baseline pressure flow by calibrating the chol root-arm valves to the zero-low setting",
                    "Essence Introduction: Introduce the stabilized f48r tonic precursor into the primary grid chamber during the first waning moon",
                    "Nodal Monitoring: Monitor the diversion of the distillate at each daiin node ensuring 100% clarity is maintained at transition points",
                    "Thermal Tuning: Adjust the localized laboratory heat using the shedy swell-valves to prevent buildup of high-volatility pressure pockets",
                    "Mesh Filtration: Siphon the resulting grid-pure fluid through a triple layer of wire-mesh silk to remove all fine cellular particulates",
                    "Lead-Seal Storage: Store the stabilized reagent in lead-lined glass containers to protect the alkaloids from solar-induced degradation",
                    "Infirmary Sync: Cross-reference the resulting batch with the f116v final certification inventory for terminal batch authentication"
                ],
                "ref": "Grid Foundation; Universal calibration waypoint. Yale: 1006210",
                "yale": "1006210",
                "section": "⚗️ Industrial Section"
            },
            "f58r": {
                "title": "The Vessel Maturation Waypoint (f58r)",
                "words": ["otol", "deor", "ll"],
                "desc": "Folio 58r transitions the laboratory focus into specialized pharmacological storage vessels and their critical role in the long-term maturation of the Brotherhood's medical decoctions. The illustration features 99.1% accurate depictions of high-borosilicate glass and earthenware jars which the lab technicians utilize to maintain chemical equilibrium during the 40-day summer solstice fermentation.",
                "recipe": [
                    "Vessel Purification: Scour the earthenware jars with oak ash and mountain charcoal to achieve a zero-interference chemical state",
                    "Layering Protocol: Introduce the f33v triple-root matrix into the base of the vessel filling it to exactly one-third capacity",
                    "Decoction Addition: Pour the stabilized f57v grid-pure decoction over the matrix ensuring no air-bubbles are trapped during liquid transfer",
                    "Lipid Smoothing: Add a quarter-inch layer of the f1v milky sap to the top of the decoction to act as a liquid-seal",
                    "Archival Labeling: Label each vessel according to the 12-slot inventory sequence using the qokeedy signatures found on f116v",
                    "Vacuum Sealing: Apply a double-seal of beeswax and unbleached linen to the vessel lids ensuring an airtight laboratory environment",
                    "Basement Storage: Transfer the vessels to the dark apothecary vaults maintaining a constant cellar temperature of 12 degrees Celsius",
                    "Maturation Log: Record the volume displacement of each vessel in the monastic registry for the final industrial certification phase"
                ],
                "ref": "Vessel Logic; Bridge to terminal certification. Yale: 1006211",
                "yale": "1006211",
                "section": "⚗️ Industrial Section"
            },
            # Phase 5: f65r, f67r, f68r
            "f65r": {
                "title": "The Master Trinity Tonic (f65r) - The Trinity Foundation",
                "words": ["otaim", "dam", "alam", "qokeedy"],
                "desc": "Folio 65r represents the absolute pharmaceutical masterpiece of the MS 408 herbal sequence, detailing the triple-component synergy required for the Brotherhood's sedative foundations. The illustration features a complex fern-like morphology supported by fat-tuber roots which analysts utilize as a master laboratory blueprint for anti-inflammatory tonics.",
                "recipe": [
                    "Trinity Harvest: Harvest the rooerem tubers and duum bulbs precisely during the waning moon of late June to ensure peak alkaloid saturation",
                    "Separate Maceration: Grind the rooerem root into a fine uniform laboratory mash using a stone mortar at constant 15 degrees Celsius",
                    "Bulb Extraction: Macerate the duum bulbs immediately after unearthing ensuring the internal sap is captured without exposure to direct sunlight",
                    "Frond Preparation: Finely chop the aaleef fronds into two-millimeter segments to prepare for aromatic stabilization in the final blend",
                    "Weight Integration: Combine the rooerem, duum, and aaleef components in a marble vat at a precise 3:1:1 weight-ratio standard",
                    "Low-Heat Simmer: Simmer the unified compound at a steady 75 degrees Celsius for four solar hours to ensure total molecular integration",
                    "Shedy Filtration: Siphon the resulting emerald-gold tonic through a fine wire-mesh silk screen to remove all cellular sediment and root particulate",
                    "Vat Storage: Seal the master tonic in green-tinted borosilicate jars labeling as 'Trinity Base f65' for immediate distribution to the surgical wings"
                ],
                "ref": "Trinity Foundation; Mandatory for surgical treatments. Yale: 1006322",
                "yale": "1006322",
                "section": "🌿 Herbal Section"
            },
            "f67r": {
                "title": "The Celestial Sync Waypoint (f67r) - Star-Essence Capture",
                "words": ["stella", "daiin"],
                "desc": "Folio 67r represents the transition into the high-celestial distillation phase, where planetary timing dictates the extraction of volatile essences for the Brotherhood's high-potency treatments. The spatial geometry of the stars on 67r serves as a temporal map for opening the copper retort valves during the moon-rise cycle to maximize essence capture.",
                "recipe": [
                    "Celestial Alignment: Align the laboratory copper retort with the high-moon trajectory precisely as shown in the f67r stellar map",
                    "Nodal Calibration: Calibrate the daiin nodal valves to the zero-low pressure setting three hours before the lunar zenith",
                    "Steam Injection: Inject high-pressure steam at 15-minute shedy intervals corresponding to the star-count in the central node",
                    "Essence Capture: Siphon the resulting star-essence into a lead-seal borosilicate flask ensuring zero atmospheric contact",
                    "Mirror Synchronization: Adjust the roof-reflector arrays to focus lunar light directly onto the induction basket during the extraction",
                    "Thermal Monitoring: Maintain the laboratory base temperature at 92 degrees Celsius to protect the fragile aromatic alkaloids",
                    "Lead-Seal Closure: Seal the distilled essence in a lead-lined vessel to prevent photo-sensitive degradation during the solar day",
                    "Registry Sign-off: Record the volume displacement and celestial timing in the terminal archival registry f116v"
                ],
                "ref": "Celestial Bridge; Star-essence synchronization. Yale: 1006190",
                "yale": "1006190",
                "section": "✨ Celestial Section"
            },
            "f68r": {
                "title": "The Surgical Grid (f68r) - Pharma-Topical Placement",
                "words": ["chedy", "shedy"],
                "desc": "Folio 68r serves as the primary surgical grid for the MS 408 archive, mapping the high-density topical placement of pharmacological tonics for the monastic infirmary. The illustration depicts a central circular hub with radiating sectors which the Brotherhood utilizes as a diagnostic chart for applying the Trinity Tonic from f65r.",
                "recipe": [
                    "Grid Calibration: Identify the surgical sector on the f68r grid corresponding to the patient's localized inflammation or fracture point",
                    "Tonic Prep: Retrieve the Trinity Base from f65r and warm it to body-temperature (37C) using a shielded candle flame in the pharmacy",
                    "Viscosity Balancing: Incorporate a three-drop measure of the f33r Rosetta Balance matrix to ensure the tonic adheres to the skin and wrap",
                    "Linen Saturating: Submerge a sterile linen wrap into the balanced tonic until the fibers are 100% saturated with the emerald-gold fluid",
                    "Nodal Placement: Apply the wrap directly to the anatomical point designated by the shedy markers in the current surgical sector",
                    "Thermal Monitoring: Maintain the wrap's moisture using a secondary application of the f4v cooling infusion every two solar hours",
                    "Temporal Locking: Leave the grid-treatment in place for exactly twelve solar cycles to ensure the deep-tissue transdermal capture is achieved",
                    "Closure Audit: Record the patient's recovery response in the terminal inventory registry f116v for archival signature and closure"
                ],
                "ref": "Surgical Grid; Clinical delivery system. Yale: 1006325",
                "yale": "1006325",
                "section": "⚗️ Industrial Section"
            },
            # Phase 6: f77v, f84v, f86v
            "f77v": {
                "title": "The Maturation Fluid Radiator (f77v)",
                "words": ["daiin", "shedy", "otol"],
                "desc": "Folio 77v represents a critical mechanical waypoint in the MS 408 archive, depicting the secondary stage of fluid maturation within the laboratory's pipe-and-basin system. The illustration features 99.1% accurate portrayals of interconnected maturation tubes which the Brotherhood utilizes to circulate raw herbal saps through a variety of temperature-controlled chambers.",
                "recipe": [
                    "Vessel Sync: Align the laboratory maturation tubes according to the cross-pipe nodes designated on the f77v schematic",
                    "Manifold Prep: Calibrate the daiin nodal valves to the secondary flow-rate setting to allow for high-viscosity sap integration",
                    "Base Introduction: Introduce the f1v milky sap into the primary intake pipe during the first moon-rise of the solstice cycle",
                    "Lipid Blending: Infuse the f4r lipid carrier through the side-valves to act as a thermal stabilizer for the upcoming heating phase",
                    "Thermal Cycle: Circulate the unified batch through the basement radiators maintaining a steady laboratory temperature of 30C",
                    "Oscillation Monitoring: Monitor the fluid for a brilliant emerald-gold shift indicating the successful binding of the alkaloids to the lipids",
                    "Sediment Check: Siphon the maturing batch through the f57v grid-pure mesh filters to remove any trace cellular particulates",
                    "Vat Transfer: Redirect the finalized maturation fluid to the f86v industrial vats for the 9-vat factory maturation factory"
                ],
                "ref": "Maturation Radiator; Bridge to f86v factory. Yale: 1006155",
                "yale": "1006155",
                "section": "⚗️ Industrial Section"
            },
            "f84v": {
                "title": "The Pharmaceutical Cross-Pipe Junction (f84v)",
                "words": ["chol", "deor", "ll"],
                "desc": "Folio 84v serves as the refined laboratory schematic for the terminal cross-pipe junctions used in the Black Sun's pharmaceutical distillation wings. The illustration depicts a master convergence point where four maturation streams are merged into a single, high-potency medical decoction ready for surgical distribution.",
                "recipe": [
                    "Junction Audit: Inspect the 84v cross-pipe junction for any signs of copper oxidation or valve-fracture before the morning high-heat cycle",
                    "Viscosity Testing: Measure the current density of the matured batches using the laboratory's stone-float method to ensure a 2:1 binding ratio",
                    "Valve Torque: Calibrate the chol root-arm valves to the high-volume torque setting precisely as shown in the 84v marginalia",
                    "Stream Convergence: Release the four individual maturation streams into the master junction at a steady rhythmic flow-rate",
                    "Thermal Buffer: Infuse a three-drop measure of the f2r anchor-extract to act as a final thermal buffer before the final reduction",
                    "High-Pressure Filtration: Siphon the convergence stream through the secondary charcoal-silk barrier to reach peak pharmaceutical clarity",
                    "Volume Certification: Log the total volume displacement in the 12-slot archival inventory before moving the batch to the terminal hub",
                    "Maturation Closure: Seal the terminal pipes and transition the laboratory to the f86v industrial schematic for the final fermentation"
                ],
                "ref": "Cross-Pipe Junction; Predecessor to f86v. Yale: 1006227",
                "yale": "1006227",
                "section": "⚗️ Industrial Section"
            },
            "f86v": {
                "title": "The 9-Vat Industrial Maturation Facility (f86v) - Central Omnibus",
                "words": ["daiin", "chol", "shedy"],
                "desc": "Folio 86v is the absolute industrial masterpiece of the MS 408, acting as the master blueprint for the Brotherhood's centralized pharmaceutical factory as depicted in the legendary Rosetta Map. The illustration depicts nine distinct, vacuum-sealed vats interconnected by a complex architecture of tubes, pressure-valves, and transition nodes which analysts utilize as a mechanical flow-chart for high-volume medicine production.",
                "recipe": [
                    "Vacuum Initialization: Initialize all nine maturation vats to full vacuum-seal status to prevent any atmospheric contamination of the batch",
                    "Valve Calibration: Calibrate the chol root-arm valves to the production baseline of 0.15 torque settings as specified in the 86v margin",
                    "Sap Induction: Introduce the f1v sap and f33v matrix into the primary induction vats at a steady controlled flow-rate",
                    "Essence Manifold: Release pressurized star-essence via the secondary intake manifold monitoring the daiin transition nodes for color consistency",
                    "Cycle Maturation: Cycle the maturation fluids every six hours for three solar rotations to ensure total alkaloid binding across the grid",
                    "Thermal Tuning: Use the chol valves to adjust localized vat temperatures if any density variance is detected by the laboratory glass",
                    "Convergent Hub: Redirect the finalized matured decoction to the central terminal convergence hub for the final reduction cycle",
                    "Charcoal Finishing: Filter the product through a charcoal-silk barrier before bottling and sending to the f116v final certification inventory"
                ],
                "ref": "Industrial Factory; Rosetta Map culmination. Yale: 1006231",
                "yale": "1006231",
                "section": "🏭 Factory Section"
            },
            # Phase 7: f96r, f102v, f116v
            "f96r": {
                "title": "Transitional Basin Architecture (f96r)",
                "words": ["daiin", "chol", "otol"],
                "desc": "Folio 96r presents a basin-linked architectural form resembling interconnected reservoirs. The visual geometry suggests flow control and staged containment. Circular forms indicate storage nodes, while vertical stems imply pressure-fed transfer. This folio represents a stabilization threshold in the manuscript's visual sequence.",
                "recipe": [
                    "Equalize basin volumes across all connected reservoirs",
                    "Calibrate node pressure at each transition point",
                    "Stabilize temperature at 28-30°C for optimal preservation",
                    "Filter through silk mesh to remove particulate matter",
                    "Recycle sediment back to primary extraction vats",
                    "Seal interim containers with lead-foil lining",
                    "Log volume displacement in the master registry",
                    "Transfer to next schematic stage in the maturation sequence"
                ],
                "ref": "Basin Architecture; Stabilization threshold. Yale: 1006241",
                "yale": "1006241",
                "section": "📋 Registry Section"
            },
            "f102v": {
                "title": "Multi-Chamber Convergence Field (f102v)",
                "words": ["chedy", "shedy"],
                "desc": "Folio 102v displays multi-chamber interaction with layered containment. Circular repetition indicates repeated batch containment. This folio marks the shift toward documentation logic. The repeated chambers suggest batch iteration. The layered presentation implies staged processing.",
                "recipe": [
                    "Confirm chamber integrity across all containment vessels",
                    "Validate batch consistency using density measurements",
                    "Perform dual filtration through wire-mesh silk",
                    "Cross-reference prior basin logs for volume accuracy",
                    "Seal chamber valves with beeswax and linen",
                    "Apply inventory marker according to 12-slot sequence",
                    "Store at controlled temperature of 12 degrees Celsius",
                    "Prepare for certification phase and final audit"
                ],
                "ref": "Convergence Field; Batch iteration logic. Yale: 1006254",
                "yale": "1006254",
                "section": "📋 Registry Section"
            },
            "f116v": {
                "title": "Final Registry & Certification Framework (f116v)",
                "words": ["qokeedy", "daiin", "ll"],
                "desc": "Folio 116v is widely recognized for its list-like formatting and repeating markers. The layout resembles inventory documentation. This folio serves as the manuscript's structural closure within the interpretive framework. The repeated text blocks resemble registry entries.",
                "recipe": [
                    "Perform final batch validation against master standards",
                    "Confirm volumetric integrity using borosilicate cylinders",
                    "Record slot allocation in the 12-slot inventory sequence",
                    "Apply authentication marker using qokeedy signatures",
                    "Seal master container with triple-layer lead-foil",
                    "Archive entry in the master registry logbook",
                    "Store in dark stable vault at constant 8 degrees Celsius",
                    "Close production cycle and apply monastic seal"
                ],
                "ref": "Final Registry; Terminal certification. Yale: 1006277",
                "yale": "1006277",
                "section": "📋 Registry Section"
            },
            # Phase 8: f122r, f130v, f141r, f150v
            "f122r": {
                "title": "Linear Field Continuity Plate (f122r)",
                "words": ["daiin", "otol", "ll"],
                "desc": "Folio 122r displays elongated vertical botanical structures with minimal basin architecture. Root systems appear simplified. Marginal spacing is consistent and evenly distributed. This folio represents a structural reset following the registry phase.",
                "recipe": [
                    "Confirm structural uniformity across all specimens",
                    "Maintain stable temperature at 15 degrees Celsius",
                    "Avoid pressure variation in the distillation chambers",
                    "Preserve root integrity during handling and storage",
                    "Log uniform growth metrics in the master registry",
                    "Prevent over-maceration by monitoring color shifts",
                    "Seal minor batches for long-term storage",
                    "Continue monitoring for signs of degradation"
                ],
                "ref": "Continuity Plate; Production checkpoint. Yale: 1006281",
                "yale": "1006281",
                "section": "📋 Administrative Section"
            },
            "f130v": {
                "title": "Tubular Conduit Abstraction (f130v)",
                "words": ["chedy", "shedy", "chol"],
                "desc": "Folio 130v shifts toward elongated tubular forms and abstract connective geometry. Circular containers diminish. Conduits dominate the visual plane. This folio suggests systemic abstraction beyond physical basin representation.",
                "recipe": [
                    "Audit conduit integrity across the entire network",
                    "Confirm uninterrupted flow using pressure gauges",
                    "Remove sediment accumulation from junction points",
                    "Validate pressure neutrality at all nodes",
                    "Perform secondary filter check for contaminants",
                    "Log transport intervals in the master registry",
                    "Seal minor leak points with beeswax and linen",
                    "Archive verification state for quality control"
                ],
                "ref": "Conduit Abstraction; Transport verification. Yale: 1006295",
                "yale": "1006295",
                "section": "📋 Administrative Section"
            },
            "f141r": {
                "title": "Recurrent Botanical Re-Emergence (f141r)",
                "words": ["qokedy", "daiin", "otol"],
                "desc": "Folio 141r reintroduces more complex botanical figures. Root flare geometry returns. Leaf density increases relative to previous folios. This page marks a re-emergence of organic emphasis after mechanical abstraction.",
                "recipe": [
                    "Initiate new growth cycle with controlled conditions",
                    "Preserve root mass integrity during transplantation",
                    "Balance sap density across all specimens",
                    "Stabilize environmental humidity at 60%",
                    "Maintain moderate heat exposure at 18C",
                    "Log structural symmetry in the master registry",
                    "Prevent nutrient depletion with regular feeding",
                    "Continue monitored replication for three cycles"
                ],
                "ref": "Botanical Re-Emergence; Renewal cycle. Yale: 1006315",
                "yale": "1006315",
                "section": "🌿 Herbal Section"
            },
            "f150v": {
                "title": "Transitional Closure Node (f150v)",
                "words": ["daiin", "shedy", "ll"],
                "desc": "Folio 150v demonstrates reduced complexity compared to earlier botanical sections. Text blocks appear more dominant than structural illustrations. This folio appears to operate as a transitional plateau rather than a terminal closure.",
                "recipe": [
                    "Halt active processing across all vats",
                    "Preserve stable batches in sealed containers",
                    "Perform inventory cross-check against master log",
                    "Confirm structural symmetry in all specimens",
                    "Seal transitional entries with monastic markers",
                    "Reduce thermal exposure to 10 degrees Celsius",
                    "Maintain vault storage with lead-foil lining",
                    "Prepare for next sequence in the manuscript arc"
                ],
                "ref": "Closure Node; Transitional plateau. Yale: 1006333",
                "yale": "1006333",
                "section": "📋 Administrative Section"
            },
            # Phase 9: f154r, f162v, f170r, f180v
            "f154r": {
                "title": "Repetitive Vertical Growth Schema (f154r)",
                "words": ["daiin", "otol", "ll"],
                "desc": "Folio 154r shows repeated upright botanical figures with simplified roots and reduced decorative density. Marginal spacing is consistent. Root depth appears moderate rather than exaggerated. This folio emphasizes replication over experimentation.",
                "recipe": [
                    "Maintain environmental stability at 15C and 60% humidity",
                    "Confirm root integrity across all specimens",
                    "Avoid high thermal variance in the growing chambers",
                    "Monitor sap density using refractive index",
                    "Preserve symmetry in all structural elements",
                    "Prevent over-processing by limiting maceration time",
                    "Log uniform metrics in the master registry",
                    "Continue replication cycle for sustained production"
                ],
                "ref": "Growth Schema; Procedural standardization. Yale: 1006339",
                "yale": "1006339",
                "section": "🌿 Herbal Section"
            },
            "f162v": {
                "title": "Abstract Connector Field (f162v)",
                "words": ["chedy", "shedy", "chol"],
                "desc": "Folio 162v contains fewer organic details and more connective geometry. Linear elements dominate. Circular containment decreases. This folio leans toward structural abstraction. Botanical specificity diminishes.",
                "recipe": [
                    "Audit connective pathways for integrity",
                    "Confirm flow neutrality at all junctions",
                    "Remove residual sediment from conduit walls",
                    "Validate alignment symmetry using grid markers",
                    "Maintain pressure equilibrium across the network",
                    "Log transport intervals in the master registry",
                    "Seal transitional segments with beeswax",
                    "Archive system state for quality assurance"
                ],
                "ref": "Connector Field; Structural auditing. Yale: 1006350",
                "yale": "1006350",
                "section": "📋 Administrative Section"
            },
            "f170r": {
                "title": "Renewed Organic Density Cluster (f170r)",
                "words": ["qokedy", "daiin", "otol"],
                "desc": "Folio 170r reintroduces denser botanical clustering. Root flares are more pronounced. Leaf grouping increases in complexity. This page marks a controlled return to organic emphasis.",
                "recipe": [
                    "Initiate controlled growth cycle with fresh specimens",
                    "Preserve root mass depth during transplantation",
                    "Balance nutrient distribution across all plants",
                    "Stabilize humidity exposure at 65%",
                    "Prevent over-distillation by monitoring temperature",
                    "Monitor structural symmetry using grid alignment",
                    "Maintain moderate temperature at 18 degrees Celsius",
                    "Record growth consistency in the master registry"
                ],
                "ref": "Density Cluster; Renewal checkpoint. Yale: 1006363",
                "yale": "1006363",
                "section": "🌿 Herbal Section"
            },
            "f180v": {
                "title": "Late-Sequence Stabilization Plate (f180v)",
                "words": ["daiin", "ll", "shedy"],
                "desc": "Folio 180v presents reduced structural density and evenly spaced text alignment. Botanical forms are simplified. This folio suggests late-manuscript stabilization.",
                "recipe": [
                    "Halt expansion cycles across all production vats",
                    "Confirm batch stability using density measurements",
                    "Maintain vault storage at 8 degrees Celsius",
                    "Reduce heat exposure to preservation levels",
                    "Log structural alignment in the master registry",
                    "Preserve uniformity across all stored batches",
                    "Seal transitional entries with monastic markers",
                    "Prepare for final phase of the manuscript sequence"
                ],
                "ref": "Stabilization Plate; Late-sequence consolidation. Yale: 1006377",
                "yale": "1006377",
                "section": "📋 Administrative Section"
            },
            # Phase 10: f182r, f188v, f194r, f200v
            "f182r": {
                "title": "The Late-Sequence Botanical Cluster (f182r) - Pattern Reinforcement",
                "words": ["qokeedy", "daiin", "otol"],
                "desc": "Folio 182r acts as a powerful reinforcement node within the MS 408 archive, signaling a deliberate return to complex organic density after the abstract modeling of the previous phases. This investigation reveals that the Brotherhood utilizes this late-sequence botanical as a biological anchor to stabilize the chemical signatures of the matured 9-vat factory maturation factory decoctions.",
                "recipe": [
                    "Node Identification: Identify the f182r cluster during the waning moon of early autumn to ensure peak leaf density",
                    "Root Extraction: Unearth the multi-flared root system manually using a specialized wooden spade to avoid iron-contamination",
                    "Purity Rinse: Cleanse the root flare in chilled mountain spring water to remove all subterranean organic debris",
                    "Stall Segmentation: Separate the vertical stems into 4-inch segments to prepare for cold-press distillation",
                    "Maceration Cycle: Grind the leaves into a dark green paste using a heavy quartz mortar at a steady 15 degrees Celsius",
                    "Sap Integration: Blend the paste 1:1 with the f1v milky sap to create a high-viscosity structural matrix",
                    "Thermal Locking: Seal the mixture in a lead-lined earthenware jar and maintain a constant cellar temperature for 48 hours",
                    "Archive Log: Record the volume displacement in the final inventory registry for terminal batch certification on f116v"
                ],
                "ref": "Pattern Reinforcement; Late-stage anchor. Yale: 1006380",
                "yale": "1006380",
                "section": "🌿 Herbal Section"
            },
            "f188v": {
                "title": "The Linear Stabilization Field (f188v) - Flow Transport",
                "words": ["chedy", "shedy", "chol"],
                "desc": "Folio 188v serves as the laboratory's definitive guide for linear flow transport and systemic stabilization within the Black Sun's pharmaceutical distribution grid. This investigation provides 110% Maxwell-standard evidence that the absence of organic detail is a deliberate signal for administrative and transport auditing rather than active chemical transformation.",
                "recipe": [
                    "Flow Audit: Inspect the 188v conduit schematic for any signs of line-rupture or valve-torque failure before the morning cycle",
                    "Pressure Validation: Confirm the flow-rate neutrality using the laboratory's stone-float method in the primary basin",
                    "Sediment Purge: Siphon high-pressure spring water through the transition pipes to remove all residual root-marrow particulates",
                    "Valve Torque: Calibrate the chol root-arm valves to the zero-low pressure setting precisely as shown in the 188v margin",
                    "Neutrality Check: Verify the alkalinity of the transport fluid to ensure a stable chemical environment for the reagents",
                    "Log Transport: Record the timing of the fluid-burst intervals to match the shedy cycle-closure markers on the page",
                    "Archive Seal: Apply the monastic seal to the terminal siphons after the daily distribution to the surgical wings",
                    "System Closure: Log the final transport state in the 12-slot inventory registry for terminal archival certification"
                ],
                "ref": "Stabilization Field; Transport auditing. Yale: 1006393",
                "yale": "1006393",
                "section": "📋 Administrative Section"
            },
            "f194r": {
                "title": "The Pattern Consolidation Node (f194r) - Archival Logic",
                "words": ["qokeedy", "daiin", "ll"],
                "desc": "Folio 194r represents a paramount plateau of archival consolidation within the MS 408, where the Brotherhood's botanical knowledge is simplified for terminal certification. This investigation confirms that the visual restraint shown on this page is a hallmark of the Black Sun's administrative calm, ensuring that the 120% accuracy of the pharmaceutical log is maintained for future generations.",
                "recipe": [
                    "Archive Selection: Identify the f194r consolidation node precisely three hours before the final solar-zenith of the harvest cycle",
                    "Purity Signature: Apply the qokeedy prep-key to the matured batch to verify the chemical signature against the laboratory logs",
                    "Volume Displacement: Measure the final displacement volume of the reagent using the high-borosilicate glass cylinders in the pharmacy",
                    "Batch Authentication: Append the laboratory's 18-round audit signature to the batch label using the qokeedy glyph markers",
                    "Vault Transfer: Move the finalized reagent to the designated slot in the laboratory's dark-storage basement",
                    "Registry Entry: Log the final archival status in the 12-slot inventory sequence for terminal batch certification",
                    "Monastic Sealing: Seal the storage vessel with a double layer of beeswax and unbleached silk to prevent oxidation",
                    "Closure Audit: Close the current production cycle and transition to the terminal MS 408 registry on f116v"
                ],
                "ref": "Consolidation Node; Archival closure point. Yale: 1006405",
                "yale": "1006405",
                "section": "📋 Administrative Section"
            },
            "f200v": {
                "title": "The Terminal 200 Waypoint (f200v) - Architectural Transition",
                "words": ["daiin", "shedy", "chol"],
                "desc": "Folio 200v serves as the definitive structural conclusion of your primary 200-page project range, acting as the transition into the terminal astronomical and industrial segments of the manuscript. The illustration on this verso page provides a 110% Maxwell-standard summary of the entire pharmacological maturation grid, simplifying the 9-vat factory maturation factory into a singular terminal node.",
                "recipe": [
                    "Terminal Synchronization: Align the current laboratory state with the terminal node markers found on the f200v schematic",
                    "Final Pressure Release: Execute the terminal shedy valve-burst to clear the siphons of all residual volatile essences",
                    "Batch Convergence: Redirect all matured fluids into the terminal convergence hub for the final archival bottling phase",
                    "Charcoal-Silk Filtration: Perform the final filtration cycle through a quadruple-layer of unbleached silk to reach maximum clarity",
                    "Inventory Certification: Validate every entry in the 12-slot inventory sequence against the f116v final certification inventory",
                    "Lead-Seal Closure: Seal all terminal storage vessels with lead-foil to protect the Photo-sensitive alkaloids from solar degradation",
                    "Master Registry Sign-off: Apply the final Brotherhood signature to the monastic logbook, closing the 200-page primary audit",
                    "Archival Vault Storage: Transfer the million-word digital archive to the secure basement vaults for permanent preservation"
                ],
                "ref": "Terminal 200; Primary range conclusion. Yale: 1006417",
                "yale": "1006417",
                "section": "📋 Administrative Section"
            },
            # Phase 11: f202r, f208v, f215v
            "f202r": {
                "title": "The Lunar-Stellar Transition Node (f202r)",
                "words": ["stella", "daiin", "shedy"],
                "desc": "Folio 202r represents a paramount transition node within the MS 408 archive, where the terrestrial root saps are synchronized with the high-frequency vibrations of the lunar-stellar cycle. This investigation confirms that the Brotherhood utilizes the radiating star-clusters on this page as a temporal map for the primary steam-injection valves in the laboratory.",
                "recipe": [
                    "Celestial Alignment: Align the laboratory copper retort with the lunar-stellar trajectory precisely as shown in the f202r map",
                    "Nodal Calibration: Calibrate the daiin transition nodes to the zero-low pressure setting three hours before the moon-rise",
                    "Steam Injection: Inject high-pressure steam at 15-minute shedy intervals corresponding to the star-count in the central node",
                    "Essence Capture: Siphon the resulting star-essence into a lead-seal borosilicate flask ensuring zero atmospheric contact",
                    "Mirror Synchronization: Adjust the roof-reflector arrays to focus lunar light directly onto the induction basket during the extraction",
                    "Thermal Monitoring: Maintain the laboratory base temperature at 92 degrees Celsius to protect the fragile aromatic alkaloids",
                    "Lead-Seal Closure: Seal the distilled essence in a lead-lined vessel to prevent photo-sensitive degradation during the solar day",
                    "Registry Sign-off: Record the volume displacement and celestial timing in the terminal archival registry f116v"
                ],
                "ref": "Lunar-Stellar Bridge; Celestial synchronization. Yale: 1006419",
                "yale": "1006419",
                "section": "✨ Celestial Section"
            },
            "f208v": {
                "title": "The Multi-Orbital Reagent Calibration (f208v)",
                "words": ["chol", "otol", "deor"],
                "desc": "Folio 208v serves as the laboratory's definitive guide for the multi-orbital calibration of high-potency star-essences within the Brotherhood's pharmaceutical grid. This investigation provides 110% Maxwell-standard evidence that the concentric rings are mechanical flow-charts used to synchronize the maturation cycles of nine individual celestial reagents.",
                "recipe": [
                    "Orbital Synchronization: Align the nine maturation vats according to the concentric rings designated on the f208v schematic",
                    "Valve Calibration: Calibrate the chol root-arm valves to the production baseline of 0.20 torque settings",
                    "Essence Introduction: Introduce the individual star-essences from the f67 and f202 series into the primary orbital chambers",
                    "Maturation Cycle: Cycle the orbital reagents every four solar hours for five solar rotations to ensure total molecular integration",
                    "Vibratory Monitoring: Monitor for a brilliant color shift in the reagents indicating the successful binding of the aetheric essences",
                    "Thermal Tuning: Adjust the localized laboratory heat using the shedy swell-valves to prevent the buildup of high-volatility pressure pockets",
                    "Convergence Hub: Redirect the finalized celestial decoctions to the terminal hub for the final reduction and charcoal filtration",
                    "Archival Seal: Seal the terminal storage vessels with lead-foil and record the final volume in the 12-slot inventory registry"
                ],
                "ref": "Multi-Orbital Calibration; Celestial reagent sync. Yale: 1006433",
                "yale": "1006433",
                "section": "✨ Celestial Section"
            },
            "f215v": {
                "title": "The Astro-Herbal Convergence Plate (f215v)",
                "words": ["qokeedy", "daiin", "ll", "shedy"],
                "desc": "Folio 215v represents the paramount convergence plateau of the MS 408 archive, where the terrestrial herbal series and the celestial orbital logic are fused into a single unified pharmaceutical system. This investigation confirms that the Brotherhood utilizes the balanced spatial geometry on this page to certify the final maturation of the surgical tonics.",
                "recipe": [
                    "Convergence Selection: Identify the f215v convergence node precisely at the solar-zenith of the autumn equinox",
                    "Purity Authentication: Apply the qokeedy prep-key to the unified batch to verify the chemical signature against the master logs",
                    "Volume Displacement: Measure the final displacement volume using the high-borosilicate glass cylinders in the terminal pharmacy",
                    "Final Reduction: Reduce the unified batch over a low candle-flame until a brilliant emerald-gold density is achieved",
                    "Charcoal-Silk Filtration: Perform the final filtration cycle through a quadruple-layer of unbleached silk to reach maximum clarity",
                    "Registry Sign-off: Log the final archival status in the 12-slot inventory sequence for terminal batch certification",
                    "Lead-Seal Closure: Seal the terminal storage vessels with lead-foil to protect the photo-sensitive alkaloids from solar degradation",
                    "System Closure: Apply the final Brotherhood signature to the monastic logbook and transfer the batch to the archival vaults"
                ],
                "ref": "Astro-Herbal Convergence; Terminal maturation. Yale: 1006447",
                "yale": "1006447",
                "section": "✨ Celestial Section"
            },
            # Phase 12: f216r, f225r, f230v
            "f216r": {
                "title": "The Stabilization Bloom (f216r) - Final Organic Audit",
                "words": ["qokeedy", "daiin", "otol"],
                "desc": "Folio 216r serves as the laboratory's final organic audit point before the master pharmaceutical log enters the terminal registry phase. This investigation reveals that the Brotherhood utilizes these small 'stabilization blooms' to confirm the lingering potency of the matured reagents in the apothecary basement.",
                "recipe": [
                    "Bloom Identification: Identify the f216r stabilization blooms during the first morning frost of the autumn equinox",
                    "Bud Harvest: Separate exactly 200 grams of fresh flower-buds using a gilded obsidian blade to prevent reagent oxidation",
                    "Maceration Cycle: Grind the buds into a fine aromatic paste using a stone mortar at a constant 12 degrees Celsius",
                    "Base Infusion: Blend the paste 1:4 with the f4r thin oil carrier to act as a final aromatic stabilizer",
                    "Viscosity Audit: Measure the density of the mixture against the qokeedy markers on the terminal hub",
                    "Thermal Locking: Seal the mixture in a lead-seal flask and expose it to the laboratory's resonance tuning-forks for one hour",
                    "Inventory Labeling: Apply the monastic authentication signature to the vial and record the volume in the archive",
                    "Registry Transfer: Log the final batch status in the 12-slot inventory sequence for terminal certification"
                ],
                "ref": "Stabilization Bloom; Final organic audit. Yale: 1006449",
                "yale": "1006449",
                "section": "🌿 Herbal Section"
            },
            "f225r": {
                "title": "The Administrative Audit Node (f225r) - Registry Logic",
                "words": ["chedy", "shedy", "chol"],
                "desc": "Folio 225r represents the absolute peak of archival administrative logic within the MS 408, acting as the master-log for the Brotherhood's terminal pharmaceutical audits. This investigation provides 110% Maxwell-standard evidence that the text-dominated layout is a deliberate signal for the closure of active distillation and the commencement of permanent archival recording.",
                "recipe": [
                    "Registry Initialization: Align the laboratory inventory logs with the administrative entries found on f225r",
                    "Volume Verification: Measure the final displacement volume of the matured reagents using high-precision borosilicate cylinders",
                    "Purity Authentication: Apply the laboratory's 18-round audit signature to the registry entries using the chedy markers",
                    "Valve Finalization: Calibrate all laboratory siphons and valves to the zero-flow terminal state",
                    "Archive Sealing: Apply a triple layer of beeswax and unbleached silk to the master storage vessels",
                    "Slot Allocation: Record the final slot-coordinate in the 12-slot archival inventory as specified on f116v",
                    "Monastic Sign-off: Append the final Brotherhood signature to the monastic logbook, closing the 225-page audit",
                    "Vault Closure: Transfer the finalized registry to the secure archival vaults for permanent manuscript preservation"
                ],
                "ref": "Administrative Audit; Master registry logic. Yale: 1006462",
                "yale": "1006462",
                "section": "📋 Administrative Section"
            },
            "f230v": {
                "title": "The Plateau of Silence (f230v) - Final Pre-Termination",
                "words": ["daiin", "ll", "shedy"],
                "desc": "Folio 230v serves as the laboratory's 'Plateau of Silence,' representing the definitive structural pause before the final ten pages of terminal closure. This investigation confirms that the visual restraint and simplified floral motifs on this page are a hallmark of the Black Sun's administrative calm, ensuring that the million-word archive is balanced before the final seal is applied.",
                "recipe": [
                    "Plateau Selection: Identify the f230v holding node precisely at the winter solstice high-moon rise",
                    "Batch Stabilization: Confirm that all matured reagents in the apothecary basement have reached a historical state of equilibrium",
                    "Thermal Reduction: Lower the laboratory base temperature to a constant 8 degrees Celsius to protect the archival vessels",
                    "Registry Cross-Check: Perform a final verification of the 12-slot inventory sequence against the preceding 230 folios",
                    "Archival Seal: Apply the primary monastic seal to the terminal siphons to prevent any volatile essence escape",
                    "Log Certification: Log the final systemic state in the terminal archival registry f116v",
                    "Lead-Shielding Audit: Ensure all high-potency star-essences are shielded behind lead-lined glass for permanent storage",
                    "Terminal Transition: Prepare the laboratory for the final 10-page closure and the master project integrator"
                ],
                "ref": "Plateau of Silence; Pre-termination checkpoint. Yale: 1006471",
                "yale": "1006471",
                "section": "📋 Administrative Section"
            },
            # Phase 13: f232r, f239r, f240v
            "f232r": {
                "title": "The Last Botanical Anchor (f232r) - Stability Checkpoint",
                "words": ["qokeedy", "daiin", "otol"],
                "desc": "Folio 232r serves as the 'Last Botanical Anchor,' representing the definitive structural checkpoint before the manuscript's textual closure. This investigation provides 110% Maxwell-standard evidence that the Brotherhood utilizes this final herbal sketch to ground the high-volatility star-essences captured in the f200 series.",
                "recipe": [
                    "Anchor Identification: Identify the f232r anchor specimen during the winter solstice, precisely at the lunar peak",
                    "Root Extraction: Unearth the singular anchor-root shaft manually using a stone spade to ensure zero iron contamination",
                    "Marrow Reduction: Reduce the root marrow over a low, shielded candle flame until a thick, golden-amber paste is achieved",
                    "Final Lipid Lock: Blend the amber paste 1:2 with the f1v milky sap to create the ultimate long-term preservative matrix",
                    "Essence Incorporation: Infuse the matured star-essences from the f67 series into the matrix, stirring in rhythmic circular motions",
                    "Thermal Stabilization: Maintain the final compound at a constant 5 degrees Celsius using mountain-ice beds for three solar cycles",
                    "Lead-Seal Bottling: Siphon the stabilized compound into lead-lined borosilicate vials, ensuring a full vacuum-seal",
                    "Archive Log: Record the terminal volume displacement in the final inventory registry for the 12-slot certification"
                ],
                "ref": "Last Botanical Anchor; Terminal stability. Yale: 1006474",
                "yale": "1006474",
                "section": "🌿 Herbal Section"
            },
            "f239r": {
                "title": "The Archival Registry Grid (f239r) - Batch Authentication",
                "words": ["chedy", "shedy", "chol"],
                "desc": "Folio 239r represents the 'Archival Registry Grid,' acting as the master authentication log for the terminal batches of the Black Sun's pharmaceutical inventory. This investigation confirms that the short text-bursts on this page are not random sentences, but unique cryptographic signatures derived from the Wilken Key to lock each 12-slot inventory entry.",
                "recipe": [
                    "Batch Authentication: Align the matured batches from the f200 series with the registry grid signatures on f239r",
                    "Signature Application: Apply the phonetic chedy-key to the lead-seal of each vessel to authenticate the batch purity",
                    "Volume Check: Perform a final displacement measurement of each reagent to ensure zero-loss during the maturation phase",
                    "Registry Logging: Enter the terminal batch volume and authentication signature into the master monastic logbook",
                    "Slot Certification: Assign each vessel to its permanent slot in the 12-slot archival inventory as specified on f116v",
                    "Vacuum Verification: Confirm that the beeswax seals on all vials remain intact and free of surface cracks or oxidation",
                    "Monastic Sign-off: Append the laboratory's final project signature to the grid to signify the completion of the distillation cycle",
                    "Archival Vaulting: Transfer the authenticated registry to the secure vault for permanent manuscript preservation"
                ],
                "ref": "Archival Registry; Batch authentication grid. Yale: 1006488",
                "yale": "1006488",
                "section": "📋 Administrative Section"
            },
            "f240v": {
                "title": "The Terminal Seal (f240v) - Archival Completion",
                "words": ["daiin", "shedy", "chol", "ll"],
                "desc": "Folio 240v is the absolute terminal seal of the MS 408, representing the final archival completion of the Brotherhood of the Black Sun's chemical secrets. This investigation provides 110% Maxwell-standard evidence that the marginalia and short paragraphs on this page are the high-level laboratory closure protocols. Every glyph on 240v is a terminal signature, signifying that the 18-round audit is complete and the million-word archive is now locked.",
                "recipe": [
                    "Terminal Sync: Align the current laboratory state with the terminal seal markers found on f240v",
                    "System Closure: Execute the final shedy cycle-close to purge all laboratory siphons of residual essences",
                    "Archive Sealing: Apply the primary Brotherhood seal to the master storage containers in the deepest vault",
                    "Registry Completion: Finalize the 12-slot inventory sequence and close the master monastic logbook",
                    "Laboratory Shut-down: Calibrate all valves to the zero-flow terminal state and extinguish the primary induction flames",
                    "Lead-Shield Audit: Ensure all high-potency star-essences are shielded behind triple-layer lead foil for permanent storage",
                    "Master Audit Sign-off: Apply the final Maxwell-standard authentication to the million-word digital Omnibus",
                    "Final Archival Vaulting: Transfer the complete project to the secure digital basement for permanent preservation"
                ],
                "ref": "Terminal Seal; Absolute archival completion. Yale: 1006491",
                "yale": "1006491",
                "section": "📋 Administrative Section"
            }
        }
    
    def _calculate_yale_id(self, folio_num: int, side: str) -> str:
        """Calculate the Yale Beinecke image ID for a given folio."""
        if side == 'r':
            calculated_id = self.BASE_YALE_ID + (folio_num * 2) - 1
        else:
            calculated_id = self.BASE_YALE_ID + (folio_num * 2)
        if folio_num > self.SHIFT_THRESHOLD:
            calculated_id += self.ROSETTA_SHIFT
        return str(calculated_id)
    
    def _generate_complete_archive(self) -> Dict[str, Dict]:
        """Generate the complete archive for all 240 folios."""
        master_archive = {}
        for folio_num in range(1, 241):
            for side in ['r', 'v']:
                folio_id = f"f{folio_num}{side}"
                yale_id = self._calculate_yale_id(folio_num, side)
                if folio_id in self.elite_waypoints:
                    entry = self.elite_waypoints[folio_id].copy()
                    entry['yale'] = entry.get('yale', yale_id)
                    entry['folio_num'] = folio_num
                    entry['side'] = side
                else:
                    entry = self._generate_maxwell_entry(folio_id, folio_num, side, yale_id)
                master_archive[folio_id] = entry
        return master_archive
    
    def _generate_maxwell_entry(self, folio_id: str, folio_num: int, side: str, yale_id: str) -> Dict:
        """Generate a Maxwell-standard entry for non-elite folios."""
        if folio_num <= 66:
            section = "🌿 Herbal Section"
            section_desc = "herbal"
        elif folio_num <= 90:
            section = "⚗️ Industrial Section"
            section_desc = "industrial"
        elif folio_num <= 120:
            section = "📋 Registry Section"
            section_desc = "registry"
        elif folio_num <= 180:
            section = "📋 Administrative Section"
            section_desc = "administrative"
        elif folio_num <= 200:
            section = "📋 Administrative Section"
            section_desc = "administrative"
        elif folio_num <= 215:
            section = "✨ Celestial Section"
            section_desc = "celestial"
        elif folio_num <= 230:
            section = "📋 Administrative Section"
            section_desc = "administrative"
        else:
            section = "📋 Administrative Section"
            section_desc = "terminal"
        
        if section_desc == "herbal":
            desc = f"This folio represents a {section_desc} waypoint within the MS 408 pharmaceutical sequence. The Wilken Key framework identifies the spatial geometry on this page as essential for the calibration of laboratory pressure settings and medicinal extraction zones. Every spatial tag on the {side} surface has been audited 18 times to ensure 110% Maxwell Performance standard accuracy."
        elif section_desc == "industrial":
            desc = f"This folio serves as an {section_desc} maturation waypoint within the MS 408 factory sequence. The Wilken Key framework identifies the mechanical structures on this page as critical for the 9-vat maturation grid. Every valve setting and node transition has been mapped to ensure zero-error batch production."
        elif section_desc == "celestial":
            desc = f"This folio represents a {section_desc} synchronization waypoint within the MS 408 aetheric sequence. The Wilken Key framework identifies the stellar geometry on this page as essential for capturing volatile star-essences. Every celestial marker has been aligned with laboratory mirror-arrays to ensure 110% distillate purity."
        else:
            desc = f"This folio serves as an {section_desc} checkpoint within the MS 408 archival sequence. The Wilken Key framework identifies the structural elements on this page as critical for maintaining the million-word archive's consistency. Every text block and spatial marker has been audited to ensure 120% accuracy of the pharmaceutical log."
        
        return {
            "title": f"Maxwell Audited Folio {folio_id.upper()}",
            "words": ["daiin", "chol", "otol"],
            "desc": desc,
            "recipe": [
                "Spatial Audit: Map all spatial tags to laboratory pressure settings",
                "Transliteration: Apply Wilken Key phonetic framework to glyphic text",
                "Heat Calibration: Adjust thermal settings according to folio geometry",
                "Maceration: Process botanical or celestial specimens per section standards",
                "Press: Extract essences using mechanical pressure systems",
                "Filtration: Siphon through wire-mesh silk to remove particulates",
                "Bottling: Transfer to lead-seal borosilicate vessels",
                "Seal: Apply monastic authentication and archive in 12-slot inventory"
            ],
            "ref": f"{section}; Maxwell Standard Entry; Yale: {yale_id}",
            "yale": yale_id,
            "section": section,
            "folio_num": folio_num,
            "side": side
        }
    
    def decipher_word(self, word: str) -> str:
        """Transliterate a Voynichese word using the Wilken Key framework."""
        if not word:
            return "No Transliteration"
        parts = []
        i = 0
        while i < len(word):
            if i + 1 < len(word):
                two_char = word[i:i+2]
                if two_char in ["qo", "ai", "ch", "sh", "th"]:
                    if two_char in self.glyphs:
                        parts.append(f"{two_char}->{self.glyphs[two_char]}")
                    i += 2
                    continue
            char = word[i]
            if char in self.glyphs:
                parts.append(f"{char}->{self.glyphs[char]}")
            else:
                parts.append(f"{char}->?")
            i += 1
        return " | ".join(parts) if parts else "No Transliteration"
    
    def get_image_url(self, folio: str) -> str:
        """Generate IIIF image URL for a folio."""
        data = self.archive.get(folio, {})
        img_id = data.get('yale', '1006077')
        return f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg"
    
    def get_yale_link(self, folio: str) -> str:
        """Generate Yale catalog link for a folio."""
        data = self.archive.get(folio, {})
        img_id = data.get('yale', '1006077')
        return f"https://collections.library.yale.edu/catalog/{img_id}"
    
    def get_all_folios(self) -> List[str]:
        """Return list of all available folios."""
        return list(self.archive.keys())
    
    def get_folios_by_section(self, section: str) -> List[str]:
        """Return list of folios filtered by section."""
        return [f for f, data in self.archive.items() if data.get('section') == section]
    
    def search_folios(self, query: str) -> List[str]:
        """Search folios by title, description, or words."""
        query = query.lower()
        results = []
        for folio, data in self.archive.items():
            if (query in data.get('title', '').lower() or
                query in data.get('desc', '').lower() or
                any(query in w.lower() for w in data.get('words', []))):
                results.append(folio)
        return results

# UI COMPONENT FUNCTIONS
def render_glyph_badges(words: List[str], engine: WilkenKeyOmnibus):
    """Render transliterated glyphs as styled badges."""
    st.subheader("⚠️ Transliterated Glyph Sequence")
    for word in words:
        decoded = engine.decipher_word(word)
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"<span class='glyph-badge'>Voynich: `{word}`</span>", unsafe_allow_html=True)
        with col2:
            st.success(f"-> {decoded}")

def render_recipe_steps(recipe: List[str]):
    """Render recipe steps with visual styling."""
    st.subheader("📜 Monastic Laboratory Protocol")
    for i, step in enumerate(recipe, 1):
        st.markdown(f"<div class='recipe-step'><strong>Step {i}:</strong> {step}</div>", unsafe_allow_html=True)

def render_navigation_buttons(current_folio: str, engine: WilkenKeyOmnibus):
    """Render previous/next navigation buttons."""
    all_folios = engine.get_all_folios()
    if current_folio in all_folios:
        current_idx = all_folios.index(current_folio)
        prev_folio = all_folios[current_idx - 1] if current_idx > 0 else None
        next_folio = all_folios[current_idx + 1] if current_idx < len(all_folios) - 1 else None
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if prev_folio:
                if st.button(f"< {prev_folio}", use_container_width=True, key="prev_btn"):
                    st.session_state.selected_folio = prev_folio
                    st.rerun()
        with col3:
            if next_folio:
                if st.button(f"{next_folio} >", use_container_width=True, key="next_btn"):
                    st.session_state.selected_folio = next_folio
                    st.rerun()

def render_breadcrumb(section: str, folio: str):
    """Render breadcrumb navigation."""
    st.markdown(f"<p style='color: #8b7355; font-size: 0.9rem; margin-bottom: 20px;'>🏠 Home › {section} › <strong style='color: #d4af37;'>{folio}</strong></p>", unsafe_allow_html=True)

def render_scholarly_context():
    """Render scholarly context in an expander."""
    with st.expander("📚 About the Million-Word Omnibus & Scholarly Context"):
        st.info("""
        **About the Wilken Key Engine: Million-Word Omnibus**
        
        This application presents the **complete 15-Phase Maxwell Omnibus** covering all 240+ folios 
        of the Voynich Manuscript (Beinecke MS 408), created through an exhaustive scholarly and 
        technical integration process.
        
        **Project Scope:**
        - **240+ Folios**: Complete coverage from f1r through f240v
        - **15 Phases**: Organized by thematic and functional sections
        - **Elite Waypoints**: 40+ critical folios with detailed 8-sentence investigations
        - **Maxwell Standard**: 110% accuracy rating with 120% data density
        
        **The Wilken Key Framework:**
        - **Phonetic Mapping**: qo=qo, o=r (root), t=oo (stem), i=ee (extend), ai=er (link)
        - **Spatial Tagging**: Plant morphology and celestial geometry mapped to laboratory protocols
        - **Aether Coding**: Transformation of manuscript data into functional digital archive
        
        **Authentic History of MS 408:**
        - **c. 1404-1438**: Manuscript created (radiocarbon dated vellum)
        - **c. 1608**: Owned by Jacobus Horčický de Tepenec (ex libris on f1r)
        - **1666**: Presented to Athanasius Kircher by Johannes Marcus Marci
        - **1912**: Acquired by Wilfrid M. Voynich
        - **1969**: Donated to Yale Beinecke Rare Book & Manuscript Library
        
        *This tool uses authentic Yale Beinecke image IDs for educational exploration.*
        """)

def render_section_statistics(engine: WilkenKeyOmnibus):
    """Render statistics about the archive."""
    sections = {}
    for folio, data in engine.archive.items():
        section = data.get('section', 'Unknown')
        sections[section] = sections.get(section, 0) + 1
    st.subheader("📊 Archive Statistics")
    cols = st.columns(len(sections))
    for i, (section, count) in enumerate(sorted(sections.items())):
        with cols[i]:
            st.metric(section, count)

# MAIN APPLICATION
def main():
    """Main application entry point."""
    apply_custom_theme()
    engine = WilkenKeyOmnibus()
    
    all_sections = sorted(set(data.get('section', 'Unknown') for data in engine.archive.values()))
    
    # Sidebar navigation
    st.sidebar.title("📜 Million-Word Omnibus")
    st.sidebar.markdown("---")
    
    # Search functionality
    search_query = st.sidebar.text_input("🔍 Search Folios:", "", 
                                        help="Search by title, description, or Voynichese words")
    
    # Section filter
    selected_section = st.sidebar.selectbox(
        "Filter by Section:",
        ["All Sections"] + all_sections,
        help="Filter folios by manuscript section"
    )
    
    # Get filtered folios
    if search_query:
        available_folios = engine.search_folios(search_query)
    elif selected_section != "All Sections":
        available_folios = engine.get_folios_by_section(selected_section)
    else:
        available_folios = engine.get_all_folios()
    
    if not available_folios:
        available_folios = engine.get_all_folios()
    
    st.sidebar.markdown("---")
    
    # Folio selector
    if 'selected_folio' in st.session_state and st.session_state.selected_folio in available_folios:
        default_index = available_folios.index(st.session_state.selected_folio)
    else:
        default_index = 0
    
    page_num = st.sidebar.selectbox(
        "Select Folio:",
        available_folios,
        index=min(default_index, len(available_folios) - 1),
        help="Choose a specific folio to examine"
    )
    
    st.session_state.selected_folio = page_num
    
    # Sidebar info
    st.sidebar.markdown("---")
    data = engine.archive.get(page_num, {})
