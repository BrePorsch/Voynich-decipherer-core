import streamlit as st
def apply_style():
    style_code = """
    
    .stApp {
        background-color: f4ece1 !important;
        background-image: url("https://www.transparenttextures.com/patterns/papyrus.png") !important;
    }
    [data-testid="stSidebar"] {
        background-color: 3e2723 !important;
    }
    [data-testid="stSidebar"]  {
        color: d7ccc8 !important;
        font-family: 'Georgia', serif !important;
    }
    h1, h2, h3, p, span, label, .stMarkdown {
        color: 3e2723 !important;
        font-family: 'Georgia', serif !important;
    }
    .stAlert {
        background-color: fff9f0 !important;
        border: 1px solid d7ccc8 !important;
        border-left: 5px solid 8d6e63 !important;
    }
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: ffffff !important;
        border: 1px solid 8d6e63 !important;
    }
    
    """
    st.markdown(style_code, unsafe_allow_html=True)
class WilkenKeyEngine:
    def __init__(self):
        self.glyphs = {
            "qo": "Prepared/Boiled", "t": "Root/Solid", "k": "Leaf/Surface",
            "p": "Stem/Stalk", "f": "Flower/Head", "o": "Liquid/Sap",
            "a": "Steam/Air", "i": "Oil/Essence", "l": "Release/Flow",
            "r": "Dose/Measure", "dy": "Lock/Finish", "ol": "Flow/Release"
        }
        
        self.archive = {
            1: {"title": "General Protocol (1r)", "words": ["oladaba", "qothol"], "desc": "The Brotherhood's opening SOP. All copper vessels must be scrubbed with ash. Page 1 initiates the botanical cycle and the March Strike protocol."},
            2: {"title": "The Tear-Root Extraction (1v)", "words": ["deor", "ollag"], "desc": "Protocol for harvesting the milky white sap from primary root mounds. Essential for treating topical skin inflammation and redness."},
            3: {"title": "The Forked Anchor Maceration (2r)", "words": ["qokedy", "ll"], "desc": "Double-distillation protocol for serrated leaves. Used to cool internal 'blood-fires' through high-potency essential oils."},
            9: {"title": "The Spiky Stem Refining (5r)", "words": ["qop-k", "oladaba"], "desc": "Refining the alkaloid-rich spiky stems for surface-level wound repair and monastic antiseptic cleansing."},
            33: {"title": "The Broad Leaf Release (17r)", "words": ["k-l", "otol"], "desc": "Protocol for broad-leaf essence. High-flow extraction used by traveling healers to reduce joint swelling and fluid retention."},
            66: {"title": "The Triple Root Salve (33v)", "words": ["t-r-l", "dy"], "desc": "The Triple-Root measure. A heavy, solid-base protocol designed to be locked (Dy) into a shelf-stable salve for winter storage."},
            133: {"title": "THE MARCH TRIGGER (70v)", "words": ["mrt", "otoldy"], "desc": "THE MASTER TEMPORAL KEY. When the sun enters Aries, the 'High-Flow' root extractions must begin to capture peak botanical life-force."},
            134: {"title": "The April Leaf Protocol (71r)", "words": ["mrt-k", "ll"], "desc": "SOP for harvesting surface-level leaf nutrients during the peak spring growth cycle for maximum vitamins."},
            135: {"title": "The May Flower Protocol (72r)", "words": ["mrt-f", "o"], "desc": "Extracting liquid sap from flowering heads before the summer heat thickens the resin into unusable wax."},
            136: {"title": "The June Stem Protocol (73r)", "words": ["mrt-p", "i"], "desc": "Moving extraction focus to the oils found within the stalk as the plant reaches full height and solar absorption."},
            155: {"title": "Thermal Vat Processing (75r)", "words": ["qop-k-l", "dy"], "desc": "The Factory Phase. Boiling stems in copper vats to release alkaloids. Monitor steam pipes to maintain constant heat."},
            162: {"title": "THE MASTER ROSETTES BLUEPRINT (86v)", "words": ["oladaba", "stella"], "desc": "THE HEART OF THE ENGINE. Detailed map of the 9-vat central processing hub where raw botanicals are converted into monastic medicine."},
            165: {"title": "The Pharmaceutical Inventory (88r)", "words": ["otol", "qokedy"], "desc": "Inventory of the 12-slot storage system. Jars are glazed and sealed with wax to prevent oxidation of volatile leaf decoctions."},
            189: {"title": "The Spiky Cluster Milestone (100r)", "words": ["otol-l", "dy"], "desc": "100th-Page Milestone. Protocol for treating deep abscesses using spiky flower clusters refined through the secondary flow-lock process."},
            232: {"title": "Master Authorizations (116v)", "words": ["michiton", "ams"], "desc": "The signatures of the Scribe 'Ams' and the Master 'Michiton' certifying the SOPs in this archive as consistent and safe."}
        }
    def decipher_word(self, word):
        parts = []
        if "qo" in word: parts.append(self.glyphs["qo"])
        for char in word:
            if char in self.glyphs and char not in ["q", "o"]:
                parts.append(self.glyphs[char])
        return " + ".join(parts) if parts else "Proprietary Command"
    def get_image_data(self, page):
        overrides = {1: "1006139", 2: "1006140", 133: "1006208", 155: "1006216", 162: "1006241", 165: "1006244", 232: "1006243"}
        img_id = overrides.get(page, str(1006138 + page))
        return f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg", f"https://collections.library.yale.edu/catalog/{img_id}"
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
apply_style()
engine = WilkenKeyEngine()
st.sidebar.title("🧬 Navigator")
choice = st.sidebar.radio("Go to:", ["The Decipherment Core", "Intelligence Archive", "About the Engine"])
if choice == "The Decipherment Core":
    st.title("🗝️ The Wilken Key Engine Decipherment Core")
    page_num = st.number_input("Enter Page Number (1 - 232):", min_value=1, max_value=232, value=1)
    img_url, yale_link = engine.get_image_data(page_num)
    
    data = engine.archive.get(page_num, {
        "title": f"Scientific Folio: Page {page_num}",
        "words": [],
        "desc": "Information coming soon... The Wilken Key is currently processing this folio."
    })
    
    if page_num in [162, 133, 155]:
        st.warning("📜 Wide-Format Fold-out Detected.")
        st.image(img_url, use_container_width=True)
        st.markdown(f"Keynote: [🔗 View Original at Yale Library]({yale_link})")
        st.subheader(data['title'])
        st.info(data['desc'])
        if data['words']:
            for w in data['words']:
                st.success(f"Voynich: `{w}` → {engine.decipher_word(w)}")
    else:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(img_url, caption=f"Page {page_num}")
            st.markdown(f"Keynote: [🔗 View Original at Yale Library]({yale_link})")
        with col2:
            st.subheader(data['title'])
            st.info(data['desc'])
            if data['words']:
                st.write("Operational Commands detected:")
                for w in data['words']:
                    st.success(f"Voynich: `{w}` → {engine.decipher_word(w)}")
elif choice == "Intelligence Archive":
    st.title("🏛️ The Intelligence Core")
    st.write("Brotherhood of the Black Sun: 15th-century monastic traveling pharma-techs.")
elif choice == "About the Engine":
    st.title("💻 The Wilken Key Digital Engine")
    st.success("Designed by bre with the Wilken Key Intelligence Core. ⚖️✨")
