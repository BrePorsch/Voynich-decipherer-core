import streamlit as st
def apply_custom_style():
    parchment_css = """
    
    .stApp {
        background-color: f4ece1 !important;
        background-image: url("https://www.transparenttextures.com/patterns/papyrus.png");
    }
    [data-testid="stSidebar"] {
        background-color: 3e2723 !important;
    }
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: d7ccc8 !important;
    }
    h1, h2, h3, .stMarkdown p, .stText {
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
    
    """
    st.markdown(parchment_css, unsafe_allow_html=True)
class WilkenKeyEngine:
    def __init__(self):
        self.glyphs = {
            "qo": "Prepared/Boiled", "t": "Root/Solid", "k": "Leaf/Surface",
            "p": "Stem/Stalk", "f": "Flower/Head", "o": "Liquid/Sap",
            "a": "Steam/Air", "i": "Oil/Essence", "l": "Release/Flow",
            "r": "Dose/Measure", "dy": "Lock/Finish"
        }
        self.special_pages = {
            1: "1006139", 2: "1006140", 133: "1006208", 162: "1006241", 175: "1006244", 232: "1006243"
        }
    def get_image_data(self, page_num):
        if page_num in self.special_pages:
            img_id = self.special_pages[page_num]
        else:
            img_id = str(1006138 + page_num)
        img_url = f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg"
        yale_link = f"https://collections.library.yale.edu/catalog/{img_id}"
        return img_url, yale_link
    def get_scientific_protocol(self, page_num):
        if page_num <= 130:
            return {"section": "🌿 Botanical Extraction Protocol", "analysis": "Wilken Key indicates primary root/leaf maceration.", "protocol": "1. Identify root mound. 2. Apply 'Qo' (Boil). 3. Filter sap."}
        elif 131 <= page_num <= 150:
            return {"section": "♈ Astronomical Timing Trigger", "analysis": "Temporal synchronization page for peak potency.", "protocol": "1. Align star. 2. Observe 'Mrt' marker. 3. Harvest at solar degree."}
        elif 151 <= page_num <= 170:
            return {"section": "🛁 Thermal Processing (The Factory)", "analysis": "Refining raw essence using thermal pipes.", "protocol": "1. Channel Flow. 2. Monitor Steam. 3. Collect essence."}
        else:
            return {"section": "🏺 Pharmaceutical Inventory & Authorization", "analysis": "Final SOPs and Monastic certification.", "protocol": "1. Review Cleansing. 2. Verify seal. 3. Lock Archive."}
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
apply_custom_style()
engine = WilkenKeyEngine()
st.sidebar.title("🧬 Navigator")
page_choice = st.sidebar.radio("Go to:", ["The Decipherment Core", "Intelligence Archive", "About the Engine"])
if page_choice == "The Decipherment Core":
    st.title("🗝️ The Wilken Key Engine Decipherment Core")
    selected_page = st.number_input("Enter Page Number (1 - 232):", min_value=1, max_value=232, value=1)
    if selected_page:
        img_url, yale_link = engine.get_image_data(selected_page)
        protocol = engine.get_scientific_protocol(selected_page)
        if selected_page in [162, 133, 155]:
            st.warning("📜 Wide-Format Fold-out Detected.")
            st.image(img_url, use_container_width=True)
            st.markdown(f"Keynote: [🔗 View Original at Yale Beinecke]({yale_link})")
            st.info(f"Section: {protocol['section']}\n\nWilken Key Analysis: {protocol['analysis']}")
        else:
            col1, col2 = st.columns([1, 1])
            with col1:
                st.subheader("📜 Manuscript Source")
                st.image(img_url, caption=f"Wilken Key Engine Scan: Page {selected_page}")
                st.markdown(f"Keynote: [🔗 View Original at Yale Beinecke]({yale_link})")
            with col2:
                st.subheader(f"🧪 {protocol['section']}")
                st.info(f"Wilken Key Analysis: {protocol['analysis']}")
                st.warning(f"Operational Protocol:\n{protocol['protocol']}")
                st.success("Phoneme 'Qo' → Prepared/Boiled | 'O-L' → Flow | 'Dy' → Lock")
elif page_choice == "Intelligence Archive":
    st.title("🏛️ The Intelligence Core")
    st.write("Brotherhood of the Black Sun: 15th-century monastic pharma-techs.")
elif page_choice == "About the Engine":
    st.title("💻 The Wilken Key Digital Engine")
    st.success("Designed by bre with the brea Intelligence Interface. ⚖️✨")
