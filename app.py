import streamlit as st
def apply_custom_style():
    st.markdown(
        """
        
        .stApp {
            background-color: f4ece1;
            background-image: url("https://www.transparenttextures.com/patterns/papyrus.png");
        }
        section[data-testid="stSidebar"] {
            background-color: 3e2723 !important;
        }
        section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] label {
            color: d7ccc8 !important;
        }
        h1, h2, h3 {
            color: 2d2926;
            font-family: 'Georgia', serif;
            border-bottom: 1px solid 8d6e63;
        }
        .stMarkdown, p, span {
            color: 3e2723;
            font-family: 'Georgia', serif;
        }
        .stAlert {
            background-color: fff9f0 !important;
            border: 1px solid d7ccc8 !important;
            border-radius: 5px;
        }
        input {
            background-color: ffffff !important;
            border: 1px solid 8d6e63 !important;
        }
        
        """,
        unsafe_allow_html=True
    )
class WilkenKeyEngine:
    def __init__(self):
        self.glyphs = {
            "qo": "Prepared/Boiled", "t": "Root/Solid", "k": "Leaf/Surface",
            "p": "Stem/Stalk", "f": "Flower/Head", "o": "Liquid/Sap",
            "a": "Steam/Air", "i": "Oil/Essence", "l": "Release/Flow",
            "r": "Dose/Measure", "dy": "Lock/Finish"
        }
        self.image_map = {
            "1r": "1006139", "1v": "1006140", "2r": "1006141", "2v": "1006142",
            "70v": "1006208", "86v": "1006241", "88r": "1006244", "116v": "1006243"
        }
        self.folios = {
            "1r": {"title": "General Protocol", "words": ["oladaba", "qothol"], "desc": "Cleanse tools and wait for March Strike."},
            "1v": {"title": "The Tear-Root", "words": ["deor", "ollag"], "desc": "Extract milky sap from the root mound."},
            "70v": {"title": "Zodiac - Aries", "words": ["mrt", "otoldy"], "desc": "March timing trigger for high-flow root medicine."},
            "86v": {"title": "The Rosettes Map", "words": ["oladaba", "stella"], "desc": "The central processing hub map (The Factory)."},
            "88r": {"title": "The Pharma Jars", "words": ["otol", "qokedy"], "desc": "The 12-slot storage system for all decoctions."},
            "116v": {"title": "The Master Authorization", "words": ["michiton", "ams"], "desc": "Final signatures of the Monastic Authors."}
        }
    def get_image_url(self, folio):
        img_id = self.image_map.get(folio, "1006139")
        return f"https://collections.library.yale.edu/iiif/2/{img_id}/full/!800,800/0/default.jpg"
    def decipher_word(self, word):
        components = [self.glyphs[c] for c in word if c in self.glyphs]
        return " + ".join(components) if components else "Proprietary Label"
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
apply_custom_style()
engine = WilkenKeyEngine()
st.sidebar.title("🧬 Navigator")
page = st.sidebar.radio("Go to:", ["The Decipherment Core", "Intelligence Archive", "About the Engine"])
if page == "The Decipherment Core":
    st.title("🗝️ The Wilken Key Engine Decipherment Core")
    st.markdown(" Decoding the world's most mysterious medical manuscript.")
    query = st.text_input("Enter Folio ID (e.g., 1r, 70v, 86v, 116v):").strip().lower()
    if query:
        if query in engine.folios:
            data = engine.folios[query]
            col1, col2 = st.columns([1, 1])
            with col1:
                st.subheader("📜 Yale Beinecke Source")
                st.image(engine.get_image_url(query), caption=f"High-Res Scan: Folio {query}")
            with col2:
                st.subheader(f"🧪 {data['title']}")
                st.info(f"Description: {data['desc']}")
                st.write("Operational Commands detected:")
                for w in data['words']:
                    st.success(f"Voynich: `{w}` → {engine.decipher_word(w)}")
        else:
            st.error("Folio ID not found in the 'Locked' database.")
elif page == "Intelligence Archive":
    st.title("🏛️ The Intelligence Core")
    st.markdown(" 1. WHO ARE THE AUTHORS?")
    st.write("The 'Brotherhood of the Black Sun' (Alpine-Irish Monastics).")
    st.markdown(" 2. WHAT IS THE MANUSCRIPT?")
    st.write("A Functional Medical Field Manual from the 15th century.")
elif page == "About the Engine":
    st.title("💻 The Wilken Key Digital Engine")
    st.info("Bridges the visual and textual data of MS 408 using Recursive Phonetic Analysis.")
    st.success("Designed by bre with the Wilken Key Intelligence Core. ⚖️✨")
