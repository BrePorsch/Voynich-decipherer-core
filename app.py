import streamlit as st
def apply_style():
    st.markdown("""
        
        .stApp {
            background-color: f4ece1 !important;
            background-image: url("https://www.transparenttextures.com/patterns/papyrus.png") !important;
            background-size: cover !important;
            background-attachment: fixed !important;
        }
        [data-testid="stSidebar"] {
            background-color: 3e2723 !important;
            border-right: 2px solid 8d6e63 !important;
        }
        / This makes the Table of Contents Title visible! /
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] .stMarkdown {
            color: d7ccc8 !important;
            font-family: 'Georgia', serif !important;
        }
        h1, h2, h3, p, span, label, .stMarkdown {
            color: 2d2926 !important;
            font-family: 'Georgia', serif !important;
        }
        .stAlert {
            background-color: fff9f0 !important;
            border: 1px solid d7ccc8 !important;
            border-left: 10px solid 8d6e63 !important;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1) !important;
        }
        div[data-baseweb="select"], div[data-baseweb="input"] {
            background-color: ffffff !important;
            border: 1px solid 8d6e63 !important;
        }
    
      """, unsafe_allow_html=True)
 
class WilkenKeyEngine:
    def __init__(self):
        self.glyphs = {"qo": "🗝️", "a": "🌿", "o": "🌀", "l": "⚖️", "i": "✨", "r": "⚓", "m": "🥇", "t": "📏", "p": "🧪", "k": "🔪", "s": "📜", "d": "🩸", "g": "🪦", "e": "🌾", "f": "🔥", "u": "💧", "b": "🪵", "h": "🕯️", "n": "🌑"}
        self.image_map = {
            1: "1006139", 2: "1006140", 3: "1006141", 9: "1006147", 33: "1006159", 66: "1006176",
            98: "1006188", 109: "1006193", 127: "1006197", 129: "1006201", 133: "1006208",
            134: "1006209", 135: "1006211", 136: "1006213", 155: "1006216", 158: "1006222",
            160: "1006230", 161: "1006234", 162: "1006237", 163: "1006241", 165: "1006244",
            169: "1006248", 175: "1006254", 179: "1006258", 189: "1006268", 195: "1006274",
            201: "1006280", 211: "1006290", 218: "1006294", 232: "1006243"
        }
        self.archive = {
            1: {"title": "General Protocol (1r)", "words": ["oladaba", "qothol"], "desc": "Cleanse tools and wait for March Strike.", "recipe": "Scrub copper vessels with ash. Initiate botanical cycle.", "ref": "See Page 133 (March Strike)."},
            2: {"title": "The Tear-Root (1v)", "words": ["deor", "ollag"], "desc": "Extract milky sap from the root mound.", "recipe": "Harvest milky sap. Filter through linen.", "ref": "Storage on Page 165."},
            3: {"title": "The Forked Anchor (2r)", "words": ["qokedy", "ll"], "desc": "Macerate serrated leaves in double-distillation.", "recipe": "Double-distill serrated leaves.", "ref": "Cooling for blood heat."},
            9: {"title": "The Spiky Stem (5r)", "words": ["qop-k", "oladaba"], "desc": "Prepare the spiky stem for surface application.", "recipe": "Boil spiky stem for surface use.", "ref": "Cleansing protocol Page 1."},
            33: {"title": "The Broad Leaf (17r)", "words": ["k-l", "otol"], "desc": "Release the essence of the broad leaf.", "recipe": "High-flow leaf essence release.", "ref": "Joint swelling reduction."},
            66: {"title": "The Triple Root (33v)", "words": ["t-r-l", "dy"], "desc": "Dose the triple root and lock the essence.", "recipe": "Triple root dose, lock into salve.", "ref": "Winter storage."},
            98: {"title": "The Steam Vat (49v)", "words": ["a-o-l", "qothol"], "desc": "Process the steam-sap in the cleansing vat.", "recipe": "Steam sap processing.", "ref": "Factory phase Page 155."},
            109: {"title": "The Oil Press (55r)", "words": ["i-r", "ll"], "desc": "Measure the oil dose for high-flow release.", "recipe": "Oil dose measurement.", "ref": "Pharma jars Page 165."},
            127: {"title": "Zodiac Rotation 1 (67r)", "words": ["mrt-l", "otol"], "desc": "Spring timing for the first release.", "recipe": "Spring harvest alignment.", "ref": "Page 133 Aries trigger."},
            129: {"title": "Zodiac Rotation 2 (68r)", "words": ["mrt-r", "dy"], "desc": "Measure the timing for the second lock.", "recipe": "Second lock timing.", "ref": "Page 134 Taurus."},
            133: {"title": "Zodiac Aries (70v)", "words": ["mrt", "otoldy"], "desc": "March timing trigger for high-flow root medicine.", "recipe": "Sun in Aries at dawn.", "ref": "General Protocol Page 1."},
            134: {"title": "Zodiac Taurus (71r)", "words": ["mrt-k", "ll"], "desc": "April timing for surface leaf flow.", "recipe": "Leaf harvest peak spring.", "ref": "Page 135 Gemini."},
            135: {"title": "Zodiac Gemini (72r)", "words": ["mrt-f", "o"], "desc": "May timing for flower-sap extraction.", "recipe": "Flower sap extraction.", "ref": "Page 136 Cancer."},
            136: {"title": "Zodiac Cancer (73r)", "words": ["mrt-p", "i"], "desc": "June timing for stem-oil essence.", "recipe": "Stem oil extraction.", "ref": "Page 133 Aries start."},
            155: {"title": "The Pharma Vat (75r)", "words": ["qop-k-l", "dy"], "desc": "Boiling stems for topical surface lock.", "recipe": "Copper vat boiling.", "ref": "Rosettes map Page 162."},
            158: {"title": "The Triple Pipe (78r)", "words": ["o-l-r", "qothol"], "desc": "Triple pipe flow for deep cleansing.", "recipe": "Three-stage cooling.", "ref": "Page 98 steam vat."},
            160: {"title": "The Cooling Basin (82r)", "words": ["a-l", "dy"], "desc": "Steam release and final cooling lock.", "recipe": "Condense essence.", "ref": "Page 155 vats."},
            161: {"title": "The High-Flow Root (84r)", "words": ["t-ll", "otol"], "desc": "Maximum root flow for internal medicine.", "recipe": "Liquefy solid root.", "ref": "Page 2 tear-root."},
            162: {"title": "The Rosettes Map (86v)", "words": ["oladaba", "stella"], "desc": "The central processing hub map (The Factory).", "recipe": "9-vat system blueprint.", "ref": "Page 155 pharma vats."},
            165: {"title": "The Pharma Jars (88r)", "words": ["otol", "qokedy"], "desc": "The 12-slot storage system for all decoctions.", "recipe": "Glazed jar inventory.", "ref": "Page 2 storage."},
            169: {"title": "The Star Essence (90r)", "words": ["stella", "i"], "desc": "Extract the star-essence oil.", "recipe": "Night cycle extraction.", "ref": "Page 162 rosettes."},
            175: {"title": "The Flow Command (93r)", "words": ["l-r", "dy"], "desc": "Final flow measure and lock command.", "recipe": "Dose consistency.", "ref": "Page 66 triple root."},
            179: {"title": "The Spiky Cluster (95r)", "words": ["f-k-l", "oll"], "desc": "Spiky cluster high-flow for abscess burst.", "recipe": "Abscess treatment.", "ref": "Page 9 spiky stem."},
            189: {"title": "The Milestone Root (100r)", "words": ["otol-l", "dy"], "desc": "Great flow lock for the 100th-folio milestone.", "recipe": "Milestone salve.", "ref": "Page 66 triple root."},
            195: {"title": "The Double Star (103r)", "words": ["stella-stella", "o"], "desc": "Double star sap for high-potency dose.", "recipe": "Synergistic sap.", "ref": "Page 169 star essence."},
            201: {"title": "The Multi-Star Grid (106r)", "words": ["stella-oll", "i"], "desc": "High-potency star oil for celestial balance.", "recipe": "Planetary grid oil.", "ref": "Page 195 double star."},
            211: {"title": "The Final Steam (111r)", "words": ["a-l-r", "dy"], "desc": "Final steam release and measure lock.", "recipe": "Season cycle close.", "ref": "Page 155 vats."},
            218: {"title": "The Author's Note (114v)", "words": ["ams", "portas"], "desc": "Note from 'Ams' regarding the gateways of healing.", "recipe": "Healing gateways note.", "ref": "Page 232 authorization."},
            232: {"title": "The Master Authorization (116v)", "words": ["michiton", "ams"], "desc": "Final signatures of the Monastic Authors.", "recipe": "SOP certification.", "ref": "Entire archive."}
        }
    def decipher_word(self, word):
        parts = []
        if "qo" in word: parts.append(self.glyphs["qo"])
        for char in word:
            if char in self.glyphs and char not in ["q", "o"]:
                parts.append(self.glyphs[char])
        return " + ".join(parts) if parts else "Proprietary Command"
    def get_image_url(self, page):
        img_id = self.image_map.get(page, "1006139")
        return f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg"
    def get_yale_link(self, page):
        img_id = self.image_map.get(page, "1006139")
        return f"https://collections.library.yale.edu/catalog/{img_id}"
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
apply_style()
engine = WilkenKeyEngine()
st.sidebar.title("📜 Table of Contents")
sections = {
    "🌿 Botanical SOPs": list(range(1, 67)),
    "♈ Zodiac Timing": list(range(127, 137)),
    "🛁 Factory Vats": list(range(155, 163)),
    "🏺 Pharma Storage": list(range(165, 180)),
    "⭐ Star Protocols": list(range(189, 212)),
    "📜 Final Authorizations": list(range(218, 233))
}
selected_section = st.sidebar.selectbox("Select Section:", list(sections.keys()))
page_num = st.sidebar.selectbox("Select Page:", sections[selected_section])
st.title("🗝️ The Wilken Key Engine Decipherment Core")
st.markdown(" The complete digital archive of the Brotherhood of the Black Sun.")
img_url = engine.get_image_url(page_num)
yale_link = engine.get_yale_link(page_num)
data = engine.archive.get(page_num, {
    "title": f"Folio Page {page_num}",
    "words": [],
    "desc": "Information coming soon... The Wilken Key is processing this folio.",
    "recipe": "Recipe pending.",
    "ref": "Cross-reference pending."
})
if page_num in [162, 133, 155, 86]:
    st.warning("📜 Fold-out Detected: Full wide view.")
    st.image(img_url, use_container_width=True)
else:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("📜 Yale Beinecke Source")
        st.image(img_url, caption=f"High-Res Folio Page {page_num}", use_container_width=True)
        st.markdown(f"🔗 Yale Archive: [{yale_link}]({yale_link})")
    with col2:
        st.subheader(f"🧪 {data['title']}")
        st.info(f"Recipe: {data['recipe']}")
        st.warning(f"Wilken Key Analysis: {data['desc']}")
        st.caption(f"Cross-Ref: {data['ref']}")
if data['words']:
    st.markdown("Operational Commands:")
    for w in data['words']:
        st.success(f"Voynich: `{w}` → {engine.decipher_word(w)}")
st.markdown("---")
st.caption("brea Intelligence Core | Full Batches 1-13 Archive")
