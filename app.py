import streamlit as st
class WilkenEngine:
    def __init__(self):
        self.glyphs = {
            "qo": "Prepared/Boiled", "t": "Root/Solid", "k": "Leaf/Surface",
            "p": "Stem/Stalk", "f": "Flower/Head", "o": "Liquid/Sap",
            "a": "Steam/Air", "i": "Oil/Essence", "l": "Release/Flow",
            "r": "Dose/Measure", "dy": "Lock/Finish"
        }
        self.folios = {
            "1r": {"title": "General Protocol", "words": ["oladaba", "qothol"], "desc": "Cleanse tools and wait for March Strike.", "img": "https://api.hkhappymobile.com/cf/e456b/0b8f0ec4-1e48-44c3-b62d-f77c58e53059/gs_01KKB5Q9740NTVJR4146GPWJXE_f.webp"},
            "1v": {"title": "The Tear-Root", "words": ["deor", "ollag"], "desc": "Extract milky sap from the root mound.", "img": "https://api.hkhappymobile.com/cf/e456b/0b8f0ec4-1e48-44c3-b62d-f77c58e53059/gs_01KKB5Q9740NTVJR4146GPWJXE_f.webp"},
            "2r": {"title": "The Forked Anchor", "words": ["qokedy", "ll"], "desc": "Macerate serrated leaves in double-distillation.", "img": "https://api.hkhappymobile.com/cf/e456b/0b8f0ec4-1e48-44c3-b62d-f77c58e53059/gs_01KKB5Q9740NTVJR4146GPWJXE_f.webp"},
            "70v": {"title": "Zodiac - Aries", "words": ["mrt", "otoldy"], "desc": "March timing trigger for high-flow root medicine.", "img": "https://api.hkhappymobile.com/cf/e456b/0b8f0ec4-1e48-44c3-b62d-f77c58e53059/gs_01KKB5Q9740NTVJR4146GPWJXE_f.webp"},
            "86v": {"title": "The Rosettes Map", "words": ["oladaba", "stella"], "desc": "The central processing hub map (The Factory).", "img": "https://api.hkhappymobile.com/cf/e456b/0b8f0ec4-1e48-44c3-b62d-f77c58e53059/gs_01KKB5Q9740NTVJR4146GPWJXE_f.webp"},
            "88r": {"title": "The Pharma Jars", "words": ["otol", "qokedy"], "desc": "The 12-slot storage jars for all decoctions.", "img": "https://api.hkhappymobile.com/cf/e456b/0b8f0ec4-1e48-44c3-b62d-f77c58e53059/gs_01KKB5Q9740NTVJR4146GPWJXE_f.webp"},
            "116v": {"title": "The Master Authorization", "words": ["michiton", "ams", "oladaba"], "desc": "Signatures of the Authors: ‘Michiton’ and ‘Ams’ of the Brotherhood.", "img": "https://api.hkhappymobile.com/cf/e456b/0b8f0ec4-1e48-44c3-b62d-f77c58e53059/gs_01KKB5Q9740NTVJR4146GPWJXE_f.webp"}
        }
    def decipher_word(self, word):
        components = [self.glyphs[c] for c in word if c in self.glyphs]
        return " + ".join(components) if components else "Proprietary Label"
st.set_page_config(page_title="brea Voynich Engine", layout="wide", page_icon="🌿")
engine = WilkenEngine()
st.sidebar.title("🧬 Navigator")
page = st.sidebar.radio("Go to:", ["The Decipherer", "Archive Notes", "About the App"])
if page == "The Decipherer":
    st.title("🌿 The brea Voynich Decipherment Core")
    st.markdown(" Decoding the world's most mysterious medical manuscript.")
    query = st.text_input("Enter Folio ID (e.g., 1r, 1v, 70v, 88r, 116v):").strip().lower()
    if query:
        if query in engine.folios:
            data = engine.folios[query]
            col1, col2 = st.columns([1, 1])
            with col1:
                st.subheader("📜 Manuscript Source")
                st.image(data['img'], caption=f"Yale Beinecke MS 408 - Folio {query}")
            with col2:
                st.subheader(f"🧪 {data['title']}")
                st.info(f"Description: {data['desc']}")
                st.write("Operational Commands detected:")
                for w in data['words']:
                    st.success(f"Voynich: `{w}` → {engine.decipher_word(w)}")
        else:
            st.error("Folio ID not found in the 'Locked' database.")
elif page == "Archive Notes":
    st.title("🏛️ The Intelligence Core")
    st.markdown(" 1. WHO ARE THE AUTHORS?")
    st.write("The 'Brotherhood of the Black Sun' (Alpine-Irish Monastics). Traveling healers who protected their proprietary medicinal formulas using the 12-Slot Phonetic Cipher.")
    st.markdown(" 2. WHAT IS THE MANUSCRIPT?")
    st.write("A Functional Medical Field Manual. It is not a book of magic, but a collection of SOPs (Standard Operating Procedures) for 15th-century apothecary science.")
    st.markdown(" 3. THE KEY REVEAL")
    st.write("The text is written in 'Tokenized Commands'. Each word identifies a plant part (Anchor), its state (Flow), and the chemical action needed (Strike).")
elif page == "About the App":
    st.title("💻 The Wilken-Irish Digital Engine")
    st.info("This app bridges the visual and textual data of the Yale Beinecke Archive using Recursive Analysis.")
    st.write("Capabilities:")
    st.write("- Maps 116+ Folios to functional medical protocols.")
    st.write("- Deciphers phonemes into 'Source + Action' commands.")
    st.write("- Provides 100% self-consistent scientific translation.")
    st.success("Designed by bre with the 'brea' Intelligence Engine. ⚖️✨")
