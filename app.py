import streamlit as st
def apply_style():
    st.markdown("""
.stApp { background-color: f4ece1 !important; background-image: url("https://www.transparenttextures.com/patterns/papyrus.png"); }
[data-testid="stSidebar"] { background-color: 3e2723 !important; }
[data-testid="stSidebar"]  { color: d7ccc8 !important; font-family: 'Georgia', serif; }
h1, h2, h3, p, span, label { color: 3e2723 !important; font-family: 'Georgia', serif !important; }
.stAlert { background-color: fff9f0 !important; border: 1px solid d7ccc8 !important; border-left: 5px solid 8d6e63; }
div[data-baseweb="input"], div[data-baseweb="select"] { background-color: ffffff !important; border: 1px solid 8d6e63 !important; }
""", unsafe_allow_html=True)
class WilkenKeyEngine:
    def __init__(self):
        self.glyphs = {"qo": "Prepared/Boiled", "t": "Root/Solid", "k": "Leaf/Surface", "p": "Stem/Stalk", "f": "Flower/Head", "o": "Liquid/Sap", "a": "Steam/Air", "i": "Oil/Essence", "l": "Release/Flow", "r": "Dose/Measure", "dy": "Lock/Finish"}
        self.archive = {
            1: {"title": "General Protocol (1r)", "desc": "The Brotherhood SOP for tool preparation. All copper vessels must be scrubbed with ash. Page 1 initiates the botanical cycle."},
            2: {"title": "The Tear-Root Extraction (1v)", "desc": "Protocol for harvesting milky white sap from primary root mounds. Essential for treating topical skin heat and redness."},
            3: {"title": "The Forked Anchor Maceration (2r)", "desc": "Double-distillation protocol for serrated leaves. Used to cool internal 'blood-fires' through high-potency essential oils."},
            9: {"title": "The Spiky Stem Refining (5r)", "desc": "Refining the alkaloid-rich spiky stems for surface-level wound repair and monastic antiseptic cleansing."},
            33: {"title": "The Broad Leaf Release (17r)", "desc": "Protocol for broad-leaf essence. High-flow extraction used by traveling healers to reduce joint swelling and fluid retention."},
            66: {"title": "The Triple Root Salve (33v)", "desc": "The Triple-Root measure. A heavy, solid-base protocol designed to be locked (Dy) into a shelf-stable salve for winter storage."},
            98: {"title": "The Steam Vat (49v)", "desc": "Thermal refinement phase. Using high-pressure steam to separate volatile oils from fibrous plant stalks."},
            109: {"title": "The Oil Press (55r)", "desc": "Mechanical extraction of essence. Measuring the oil dose for high-flow release in medicinal salves."},
            127: {"title": "Zodiac Rotation 1 (67r)", "desc": "The first temporal trigger. Timing the spring harvest to align with the release of primary nutrients."},
            129: {"title": "Zodiac Rotation 2 (68r)", "desc": "The second temporal trigger. Measuring the exact moment to lock the essence for maximum shelf-life."},
            133: {"title": "THE MARCH TRIGGER (70v)", "desc": "THE MASTER TEMPORAL KEY. When the sun enters Aries, the 'High-Flow' root extractions must begin to capture peak life-force."},
            134: {"title": "The April Leaf Protocol (71r)", "desc": "SOP for harvesting surface-level leaf nutrients during the peak spring growth cycle for maximum vitamins."},
            135: {"title": "The May Flower Protocol (72r)", "desc": "Extracting liquid sap from flowering heads before the summer heat thickens the resin into unusable wax."},
            136: {"title": "The June Stem Protocol (73r)", "desc": "Moving extraction focus to the oils found within the stalk as the plant reaches full height and solar absorption."},
            155: {"title": "Thermal Vat Processing (75r)", "desc": "The Factory Phase. Boiling stems in copper vats to release alkaloids. Monitor steam pipes (Phoneme 'A') to maintain constant heat."},
            158: {"title": "The Triple Pipe Flow (78r)", "desc": "Complex distillation protocol. Using a three-stage cooling system to purify the botanical liquid for deep cleansing."},
            160: {"title": "The Cooling Basin (82r)", "desc": "Final steam release and cooling lock. Preparing the essence for transition into the storage phase."},
            161: {"title": "The High-Flow Root (84r)", "desc": "Maximum root flow protocol. Designed for internal medicine where the solid root base must be fully liquefied."},
            162: {"title": "THE MASTER ROSETTES BLUEPRINT (86v)", "desc": "THE HEART OF THE ENGINE. Detailed map of the 9-vat central processing hub where raw botanicals are converted into monastic medicine."},
            165: {"title": "The Pharmaceutical Inventory (88r)", "desc": "Inventory of the 12-slot storage system. Jars are glazed and sealed with wax to prevent oxidation of volatile leaf decoctions."},
            169: {"title": "The Star Essence (90r)", "desc": "Celestial extraction protocol. Using specific timing to capture the 'essence' of the plant during the night cycle."},
            175: {"title": "The Flow Command (93r)", "desc": "Final flow measure and lock command. This SOP ensures the dose is consistent across all monastic batches."},
            179: {"title": "The Spiky Cluster (95r)", "desc": "Protocol for treating deep abscesses using spiky flower clusters refined through the secondary flow-lock process."},
            189: {"title": "The Spiky Cluster Milestone (100r)", "desc": "100th-Page Milestone. Protocol for bursting abscesses using spiky flower clusters refined in the primary flow-lock."},
            195: {"title": "The Double Star (103r)", "desc": "High-potency dose protocol. Combining two separate star-essences for a synergistic healing effect."},
            201: {"title": "The Multi-Star Grid (106r)", "desc": "Celestial balance protocol. Using a grid-based extraction method to align the medicine with planetary cycles."},
            211: {"title": "The Final Steam (111r)", "desc": "Final steam release and measure lock. Completing the pharmaceutical cycle for the season."},
            218: {"title": "The Author's Note (114v)", "desc": "A note from Scribe 'Ams' regarding the gateways of healing and the importance of the March Strike."},
            232: {"title": "Master Authorizations (116v)", "desc": "The signatures of the Scribe 'Ams' and the Master 'Michiton' certifying the SOPs in this archive as consistent and safe."}
        }
    def get_image_data(self, page):
        overrides = {1: "1006139", 2: "1006140", 133: "1006208", 155: "1006216", 162: "1006241", 165: "1006244", 232: "1006243"}
        img_id = overrides.get(page, str(1006138 + page))
        return f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg", f"https://collections.library.yale.edu/catalog/{img_id}"
    def get_generic_desc(self, page_num):
        if page_num <= 130: return "Botanical Phase: Detailed SOP for root and leaf extractions based on the Wilken Key phonetic commands."
        elif 131 <= page_num <= 150: return "Timing Phase: Astronomical synchronization for determining the 'Strike' time of seasonal harvests."
        elif 151 <= page_num <= 170: return "Processing Phase: Refinement of raw botanicals into pharmaceutical-grade oils using monastic thermal vats."
        else: return "Storage Phase: Inventory, storage jars, and final monastic authorizations for the Brotherhood's medicine chest."
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
apply_style()
engine = WilkenKeyEngine()
st.sidebar.title("🧬 Navigator")
choice = st.sidebar.radio("Go to:", ["The Decipherment Core", "Intelligence Archive", "About the Engine"])
if choice == "The Decipherment Core":
    st.title("🗝️ The Wilken Key Engine Decipherment Core")
    page_num = st.number_input("Enter Page Number (1 - 232):", min_value=1, max_value=232, value=1)
    img_url, yale_link = engine.get_image_data(page_num)
    data = engine.archive.get(page_num, {"title": f"Scientific Folio: Page {page_num}", "desc": engine.get_generic_desc(page_num)})
    
    if page_num in [162, 133, 155]:
        st.warning("📜 Wide-Format Fold-out Detected: Displaying High-Res Architectural View.")
        st.image(img_url, use_container_width=True)
        st.markdown(f"Keynote: [🔗 View Original High-Res PDF at Yale Beinecke Library]({yale_link})")
        st.subheader(f"🧪 {data['title']}")
        st.info(f"Wilken Key Analysis: {data['desc']}")
    else:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("📜 Manuscript Source")
            st.image(img_url, caption=f"Wilken Key Engine Scan: Page {page_num}")
            st.markdown(f"Keynote: [🔗 View Original High-Res PDF at Yale Beinecke Library]({yale_link})")
        with col2:
            st.subheader(f"🧪 {data['title']}")
            st.info(f"Wilken Key Analysis: {data['desc']}")
            st.write("Operational Commands detected:")
            st.success("Phoneme 'Qo' → Prepared/Boiled | 'O-L' → Flow | 'Dy' → Lock")
elif choice == "Intelligence Archive":
    st.title("🏛️ The Intelligence Core")
    st.write("Brotherhood of the Black Sun: 15th-century monastic traveling pharma-techs.")
elif choice == "About the Engine":
    st.title("💻 The Wilken Key Digital Engine")
    st.success("Designed by bre with the brea Intelligence Interface. ⚖️✨")
