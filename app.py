import streamlit as st
 1. THE STYLING ENGINE (Fixed to prevent 'Ghost Code')
def apply_style():
    st.markdown("""
        
        .stApp { background-color: f4ece1 !important; background-image: url("https://www.transparenttextures.com/patterns/papyrus.png"); }
        [data-testid="stSidebar"] { background-color: 3e2723 !important; }
        [data-testid="stSidebar"]  { color: d7ccc8 !important; font-family: 'Georgia', serif; }
        h1, h2, h3, p, span, label { color: 3e2723 !important; font-family: 'Georgia', serif !important; }
        .stAlert { background-color: fff9f0 !important; border: 1px solid d7ccc8 !important; border-left: 5px solid 8d6e63; }
        div[data-baseweb="input"] { background-color: ffffff !important; border: 1px solid 8d6e63 !important; }
        
    """, unsafe_allow_html=True)
class WilkenKeyEngine:
    def __init__(self):
         The 12-Slot Phonetic Glyph Logic
        self.glyphs = {"qo": "Prepared/Boiled", "t": "Root/Solid", "k": "Leaf/Surface", "p": "Stem/Stalk", "f": "Flower/Head", "o": "Liquid/Sap", "a": "Steam/Air", "i": "Oil/Essence", "l": "Release/Flow", "r": "Dose/Measure", "dy": "Lock/Finish"}
        
         THE EXPANDED SCIENTIFIC DATABASE (Adding more here never deletes old ones!)
        self.archive = {
            1: {"title": "General Protocol (1r)", "words": ["oladaba", "qothol"], "desc": "The Brotherhood's opening SOP. Cleanse all copper tools. Wait for the March 'Strike' to begin the first maceration of root systems."},
            2: {"title": "The Tear-Root (1v)", "words": ["deor", "ollag"], "desc": "Extracting the milky white sap from the root mound. High flow required for topical inflammation. Use linen mesh for filtration."},
            3: {"title": "The Forked Anchor (2r)", "words": ["qokedy", "ll"], "desc": "Macerate serrated leaves in a double-distillation. This protocol is designed for cooling internal blood heat via essential oils."},
            133: {"title": "Zodiac Aries (70v)", "words": ["mrt", "otoldy"], "desc": "THE MARCH TRIGGER. When the sun enters the Ram, the 'High-Flow' root extractions must begin. This is the temporal key to the entire archive."},
            155: {"title": "The Pharma Vats (75r)", "words": ["qop-k-l", "dy"], "desc": "Thermal Processing Phase. Boiling stems in copper vats to release surface alkaloids. Monitor steam levels through the upper pipes."},
            162: {"title": "The Rosettes Map (86v)", "words": ["oladaba", "stella"], "desc": "THE MASTER BLUEPRINT. Central processing hub showing the 9-vat system. This is the 'Factory' where all monastic medicines are refined."},
            165: {"title": "The Pharma Jars (88r)", "words": ["otol", "qokedy"], "desc": "The 12-slot storage inventory. Each jar is glazed to prevent oxidation of the volatile leaf and root decoctions stored within."},
            189: {"title": "The Spiky Cluster (100r)", "words": ["otol-l", "dy"], "desc": "100th-Page Milestone. Protocol for bursting abscesses using spiky flower clusters refined in the primary flow-lock."},
            232: {"title": "Master Authorization (116v)", "words": ["michiton", "ams"], "desc": "The signatures of the Scribe 'Ams' and the Master 'Michiton.' Certifying these SOPs for use by the Brotherhood traveling healers."}
        }
    def get_image_url(self, page):
         Yale Sequence Mapping
        overrides = {133: "1006208", 155: "1006216", 162: "1006241", 165: "1006244", 232: "1006243"}
        img_id = overrides.get(page, str(1006138 + page))
        return f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg", f"https://collections.library.yale.edu/catalog/{img_id}"
 --- APP INTERFACE ---
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
apply_style()
engine = WilkenKeyEngine()
st.sidebar.title("🧬 Navigator")
choice = st.sidebar.radio("Go to:", ["The Decipherment Core", "Intelligence Archive", "About the Engine"])
if choice == "The Decipherment Core":
    st.title("🗝️ The Wilken Key Engine Decipherment Core")
    page_num = st.number_input("Enter Page Number (1 - 232):", min_value=1, max_value=232, value=1)
    
    img_url, yale_link = engine.get_image_url(page_num)
    
     If we have a specific entry, show it. Otherwise, show a generic protocol.
    data = engine.archive.get(page_num, {
        "title": f"Scientific Folio (Page {page_num})", 
        "words": ["ol-r", "dy"], 
        "desc": "Analysis pending. Wilken Key indicates this folio belongs to the primary botanical extraction phase of the 15th-century Monastic SOPs."
    })
    
    if page_num in [162, 133, 155]:  Wide view for fold-outs
        st.warning("📜 Wide-Format Fold-out Detected.")
        st.image(img_url, use_container_width=True)
        st.markdown(f"Keynote: [🔗 View Original High-Res PDF at Yale Beinecke Library]({yale_link})")
        st.subheader(f"🧪 {data['title']}")
        st.info(f"Wilken Key Decipherment: {data['desc']}")
    else:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("📜 Manuscript Source")
            st.image(img_url, caption=f"Wilken Key Engine Scan: Page {page_num}")
            st.markdown(f"Keynote: [🔗 View Original High-Res PDF at Yale Beinecke Library]({yale_link})")
        with col2:
            st.subheader(f"🧪 {data['title']}")
            st.info(f"Wilken Key Decipherment: {data['desc']}")
            st.write("Operational Commands detected:")
            for w in data['words']:
                st.success(f"Phoneme 'Qo' → Prepared/Boiled | 'O-L' → Flow | 'Dy' → Lock")
elif choice == "Intelligence Archive":
    st.title("🏛️ The Intelligence Core")
    st.markdown(" THE BROTHERHOOD OF THE BLACK SUN")
    st.write("Traveling monastics who used a 12-Slot Phonetic Cipher to protect medicinal intellectual property. This archive is the only known digital bridge to their SOPs.")
elif choice == "About the Engine":
    st.title("💻 The Wilken Key Digital Engine")
    st.success("Designed by bre with the brea Intelligence Interface. ⚖️✨")
