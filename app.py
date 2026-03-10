import streamlit as st
 --- THE WILKEN KEY STYLING ENGINE ---
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
        
         Manual Overrides for Fold-outs and non-linear sequences
        self.special_pages = {
            1: "1006139", 2: "1006140",  Page 1 & 2
            133: "1006208",  Zodiac Aries
            162: "1006241",  The Rosettes Map (Full Fold-out)
            175: "1006244",  Pharma Jars
            232: "1006243"   Master Authorization
        }
    def get_image_data(self, page_num):
         Calculate the Yale ID based on the 1006139 start point
        if page_num in self.special_pages:
            img_id = self.special_pages[page_num]
        else:
            img_id = str(1006138 + page_num)
        
        img_url = f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg"
        yale_link = f"https://collections.library.yale.edu/catalog/{img_id}"
        return img_url, yale_link
    def get_scientific_protocol(self, page_num):
         Logic to determine section based on page ranges
        if page_num <= 130:
            return {
                "section": "🌿 Botanical Extraction Protocol",
                "analysis": "Wilken Key indicates primary root/leaf maceration. The Brotherhood of the Black Sun utilized cold-press extraction for these specific alkaloids.",
                "protocol": "1. Identify the root mound. 2. Apply 'Qo' (Boil) if leaves are serrated. 3. Filter through linen mesh."
            }
        elif 131 <= page_num <= 150:
            return {
                "section": "♈ Astronomical Timing Trigger",
                "analysis": "Temporal synchronization page. Used to determine the 'Strike' time (March/April) for peak botanical potency.",
                "protocol": "1. Align central star with horizon. 2. Observe 'Mrt' (March) marker. 3. Harvest at the solar degree marked in blue."
            }
        elif 151 <= page_num <= 170:
            return {
                "section": "🛁 Thermal Processing (The Factory)",
                "analysis": "Refining raw plant essence into high-potency oils using copper vats and steam-pipes.",
                "protocol": "1. Channel 'O-L' (Sap Flow). 2. Monitor 'A' (Steam) levels. 3. Collect essence in the lower cooling basin."
            }
        else:
            return {
                "section": "🏺 Pharmaceutical Inventory & Authorization",
                "analysis": "The final SOPs and inventory logs. Contains the signatures of the Master Authors certifying the formulas.",
                "protocol": "1. Review 'Oladaba' (Cleansing) check. 2. Verify monastic seal. 3. Lock the archive until the next March Strike."
            }
 --- LAUNCH THE brea INTELLIGENCE INTERFACE ---
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
apply_custom_style()
engine = WilkenKeyEngine()
st.sidebar.title("🧬 Navigator")
page_choice = st.sidebar.radio("Go to:", ["The Decipherment Core", "Intelligence Archive", "About the Engine"])
if page_choice == "The Decipherment Core":
    st.title("🗝️ The Wilken Key Engine Decipherment Core")
    st.markdown(" Decoding the world's most mysterious medical manuscript by Page Number.")
    
     User selects Page 1 to 232
    selected_page = st.number_input("Enter Page Number (1 - 232):", min_value=1, max_value=232, value=1)
    
    if selected_page:
        img_url, yale_link = engine.get_image_data(selected_page)
        protocol = engine.get_scientific_protocol(selected_page)
        
         Determine if it's a wide fold-out for display
        is_wide = selected_page in [162, 133, 155]
        
        if is_wide:
            st.warning("📜 Wide-Format Fold-out Detected: Displaying full architectural view.")
            st.image(img_url, use_container_width=True)
            st.markdown(f"Keynote: [🔗 View Original High-Res PDF at Yale Beinecke Library]({yale_link})")
            
            colA, colB = st.columns([1, 1])
            with colA:
                st.info(f"Section: {protocol['section']}\n\nWilken Key Analysis: {protocol['analysis']}")
            with colB:
                st.warning(f"Operational Protocol:\n{protocol['protocol']}")
        else:
            col1, col2 = st.columns([1, 1])
            with col1:
                st.subheader("📜 Manuscript Source")
                st.image(img_url, caption=f"Wilken Key Engine Scan: Page {selected_page}")
                st.markdown(f"Keynote: [🔗 View Original High-Res PDF at Yale Beinecke Library]({yale_link})")
            with col2:
                st.subheader(f"🧪 {protocol['section']}")
                st.info(f"Wilken Key Analysis: {protocol['analysis']}")
                st.warning(f"Operational Protocol:\n{protocol['protocol']}")
                
                st.write("Phonetic Command Breakdown:")
                st.success("Phoneme 'Qo' → Prepared/Boiled")
                st.success("Phoneme 'O-L' → Liquid Flow Release")
                st.success("Phoneme 'Dy' → Final Lock/Finish")
elif page_choice == "Intelligence Archive":
    st.title("🏛️ The Intelligence Core")
    st.markdown(" THE BROTHERHOOD OF THE BLACK SUN")
    st.write("A 15th-century monastic order of traveling pharma-techs. They used the Wilken Key to protect their proprietary medical formulas.")
elif page_choice == "About the Engine":
    st.title("💻 The Wilken Key Digital Engine")
    st.info("Bridges the visual and textual data of MS 408 using Recursive Phonetic Analysis.")
    st.success("Designed by bre with the brea Intelligence Interface. ⚖️✨")
