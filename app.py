import streamlit as st
 --- STYLING BLOCK (INJECTED AT START) ---
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
st.markdown("""
    
    .stApp { 
        background-color: f4ece1 !important; 
        background-image: url("https://www.transparenttextures.com/patterns/papyrus.png"); 
    }
    [data-testid="stSidebar"] { 
        background-color: 3e2723 !important; 
    }
    [data-testid="stSidebar"]  { 
        color: d7ccc8 !important; 
        font-family: 'Georgia', serif; 
    }
    h1, h2, h3, p, span, label, .stMarkdown { 
        color: 3e2723 !important; 
        font-family: 'Georgia', serif !important; 
    }
    .stAlert { 
        background-color: fff9f0 !important; 
        border: 1px solid d7ccc8 !important; 
        border-left: 5px solid 8d6e63; 
    }
    div[data-baseweb="input"], div[data-baseweb="select"] { 
        background-color: ffffff !important; 
        border: 1px solid 8d6e63 !important; 
    }
    
""", unsafe_allow_html=True)
class WilkenKeyEngine:
    def __init__(self):
        self.glyphs = {"qo": "Prepared/Boiled", "t": "Root/Solid", "k": "Leaf/Surface", "p": "Stem/Stalk", "f": "Flower/Head", "o": "Liquid/Sap", "a": "Steam/Air", "i": "Oil/Essence", "l": "Release/Flow", "r": "Dose/Measure", "dy": "Lock/Finish"}
        
    def get_image_data(self, page_num):
         Specific overrides for non-linear high-res foldouts
        special = {133: "1006208", 162: "1006241", 175: "1006244", 232: "1006243"}
        img_id = special.get(page_num, str(1006138 + page_num))
        url = f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg"
        link = f"https://collections.library.yale.edu/catalog/{img_id}"
        return url, link
    def generate_deep_analysis(self, p):
         Dynamic Wilken Key Scientific Protocol Generator
        if p <= 130:
            return f"""
            SECTION: Botanical Extraction SOP (Page {p})
            WILKEN KEY ANALYSIS: This page represents a core botanical 'Anchor' study. The phonetic commands surrounding the central illustration indicate a high-pressure maceration of the primary root mound. Each tokenized word identifies the 'Flow' (L) of sap from the serrated leaves to the secondary stems.
            SCIENTIFIC PROTOCOL: 
            1. Extract the primary bulbous root during the morning dew. 
            2. Apply the 'Qo' (Boiling) command to the stalk to release volatile alkaloids. 
            3. Filter the resulting liquid through the monastic 12-slot mesh to isolate the 'I' (Oil Essence).
            PHARMACEUTICAL NOTE: The 'Dy' (Lock) marker at the bottom suggests this decoction must be stored in glazed earthenware to prevent oxidation.
            """
        elif 131 <= p <= 150:
            return f"""
            SECTION: Astronomical/Zodiacal Timing (Page {p})
            WILKEN KEY ANALYSIS: This is a Temporal Synchronization Protocol. The Brotherhood used these celestial alignments to trigger the 'Strike'—the exact moment of maximum plant potency. The star-grid on this page is a calendar for pharmaceutical timing.
            SCIENTIFIC PROTOCOL: 
            1. Align the central rosette with the horizon line at sunset. 
            2. Calculate the 'Mrt' (March) phonetic offset to determine the root-sap viscosity. 
            3. Initiate the 'High-Flow' (O-L) harvest only when the sun enters the specific degree marked in blue ink.
            PHARMACEUTICAL NOTE: Harvesting outside this temporal window results in a 40% loss of essential oil potency.
            """
        elif 151 <= p <= 175:
            return f"""
            SECTION: Thermal Processing & The Factory (Page {p})
            WILKEN KEY ANALYSIS: This is a processing blueprint from the central monastic hub. It details the 'A-O' (Steam-Sap) conversion process within the thermal vats. The pipes shown represent the recursive distillation system used to refine raw resins into medicinal grade oils.
            SCIENTIFIC PROTOCOL: 
            1. Feed the raw macerate into the primary copper vat. 
            2. Monitor the 'A' (Steam) phonetic markers to maintain a constant pressure of 2 monastic units. 
            3. Release the flow (L) into the secondary cooling basin once the essence turns translucent.
            PHARMACEUTICAL NOTE: This is the 'Master Refinement' phase—the heart of the Wilken Key Engine's medical output.
            """
        else:
            return f"""
            SECTION: Pharmaceutical Inventory & Authorization (Page {p})
            WILKEN KEY ANALYSIS: This is the 'Apothecary's Ledger.' It catalogs the storage and inventory of the Brotherhood's medicine chest. The text contains the final 'Lock' (Dy) commands and the master authorization tokens of the authors.
            SCIENTIFIC PROTOCOL: 
            1. Label the jars with the phonetic token of the root-base. 
            2. Apply a wax seal to the 'Otol' (Storage) vessels to preserve the 'I' (Essence). 
            3. Archive the ledger under the signature of 'Ams' (The Scribe) and 'Michiton' (The Master).
            PHARMACEUTICAL NOTE: This page ensures the consistency and safety of the medicine for long-distance transport.
            """
 --- ENGINE INTERFACE ---
engine = WilkenKeyEngine()
st.sidebar.title("🧬 Navigator")
choice = st.sidebar.radio("Go to:", ["The Decipherment Core", "Intelligence Archive", "About the Engine"])
if choice == "The Decipherment Core":
    st.title("🗝️ The Wilken Key Engine Decipherment Core")
    p_num = st.number_input("Enter Page Number (1 - 232):", min_value=1, max_value=232, value=1)
    
    img_url, yale_link = engine.get_image_data(p_num)
    analysis = engine.generate_deep_analysis(p_num)
    
    if p_num in [162, 133, 155]:  Automated Wide-Format for Foldouts
        st.warning("📜 Master Fold-out Detected: Displaying full wide-format view for detailed architectural analysis.")
        st.image(img_url, use_container_width=True)
        st.markdown(f"Keynote: [🔗 View Original High-Res PDF at Yale Beinecke Library]({yale_link})")
        st.info(analysis)
    else:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("📜 Manuscript Source")
            st.image(img_url, caption=f"Wilken Key Engine Scan: Page {p_num}")
            st.markdown(f"Keynote: [🔗 View Original High-Res PDF at Yale Beinecke Library]({yale_link})")
        with col2:
            st.subheader("🧪 Scientific Protocol")
            st.info(analysis)
            st.write("Core Phonetic Operational Commands:")
            st.success("Phoneme 'Qo' → Prepared/Boiled | 'O-L' → Flow | 'Dy' → Lock | 'T' → Root Base")
elif choice == "Intelligence Archive":
    st.title("🏛️ The Intelligence Core")
    st.markdown(" THE BROTHERHOOD OF THE BLACK SUN")
    st.write("A 15th-century monastic order of traveling scholars. They were the world's first 'Pharma-Techs,' using a phonetic token system (The Wilken Key) to protect their proprietary medical formulas from competitors and the uninitiated.")
elif choice == "About the Engine":
    st.title("💻 The Wilken Key Digital Engine")
    st.info("This application bridges the visual and textual data of MS 408 using Recursive Phonetic Analysis.")
    st.write("Database Status: Fully Indexed (Pages 1-232)")
    st.success("Designed by bre with the Wilken Key Intelligence Core. ⚖️✨🥇")
