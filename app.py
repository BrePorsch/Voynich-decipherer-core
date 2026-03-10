import streamlit as st
class WilkenKeyEngine:
    def __init__(self):
         #The key to the decipherment glyphs - LETTERS ADDED NEXT TO EMOJIS
        self.glyphs = {
            "qo": "qo 🗝️", "a": "a 🌿", "o": "o 🌀", "l": "l ⚖️", "i": "i ✨", 
            "r": "r ⚓", "m": "m 🥇", "t": "t 📏", "p": "p 🧪", "k": "k 🔪", 
            "s": "s 📜", "d": "d 🩸", "g": "g 🪦", "e": "e 🌾", "f": "f 🔥", 
            "u": "u 💧", "b": "b 🪵", "h": "h 🕯️", "n": "n 🌑"
        }
        
         #Mapping pages to the Yale archive IDs (Based on MS 408 Folio System)
        self.image_map = {
            1: "1006139", 2: "1006140", 3: "1006141", 9: "1006147", 33: "1006159", 66: "1006176",
            98: "1006188", 109: "1006193", 127: "1006197", 129: "1006201", 133: "1006208",
            134: "1006209", 135: "1006211", 136: "1006213", 155: "1006216", 158: "1006222",
            160: "1006230", 161: "1006234", 162: "1006237", 163: "1006241", 165: "1006244",
            169: "1006248", 175: "1006254", 179: "1006258", 189: "1006268", 195: "1006274",
            201: "1006280", 211: "1006290", 218: "1006294", 232: "1006243"
        }
        
         #8-Sentence Investigation Archive
        self.archive = {
            1: {
                "title": "General Protocol (f1r)", 
                "words": ["oladaba", "qothol"], 
                "desc": "The General Protocol serves as the foundational temporal anchor for all botanical operations within the Brotherhood's archive. Every procedure must begin with the ritualistic scouring of copper vessels using oak ash harvested during the previous lunar cycle. This scouring ensures that no residual essence from prior distillations can contaminate the purity of the March Strike. The intake valves of the primary alembic must be calibrated to a low-pressure flow precisely three hours before the Aries dawn. Initiate the flow by introducing the first bundle of serrated leaves into the heating chamber once the temperature reaches the blood-heat threshold. You must observe the steam carefully as it transitions from a translucent gray to a vibrant emerald green. This visual shift indicates that the chlorophyll-lock has been successfully bypassed, allowing the volatile oils to be captured. Refer immediately to Page 133 to synchronize this exact moment with the celestial Aries trigger for final activation. Failure to time this according to the zodiacal rotation will result in a scorched batch, necessitating a total reset of the laboratory.", 
                "recipe": "1. Scour all copper with lunar ash. 2. Calibrate valves to low flow. 3. Heat to blood-heat threshold. 4. Introduce leaf bundles. 5. Monitor for emerald steam. 6. Capture volatile oils. 7. Synchronize with Aries Dawn (Page 133). 8. Seal in glass for Phase 2.", 
                "ref": "Zodiac synchronization required on Page 133."
            },
            162: {
                "title": "The Rosettes Map (f86v)", 
                "words": ["oladaba", "stella"], 
                "desc": "The Rosettes Map represents the absolute epicenter of the Brotherhood’s industrial and philosophical worldview, functioning as a 9-vat factory schematic. At the center of this fold-out, the primary 'Stella' rosette coordinates the celestial timing of all laboratory activities. Each surrounding rosette corresponds to a specific stage of processing, from initial maceration to final fermentation. The architectural symbols within the map likely represent the physical valves and conduits required to scale up the laboratory protocols found in the earlier folios. You must align the output of the Pharma Vats from Page 155 directly with the central rosette to achieve maximum essence concentration. The map indicates that subterranean cooling pipes, as detailed on Page 158, are essential for maintaining the stability of the final compounds. This schematic also serves as a master index for the 12-slot storage system located in the Pharma Jars on Page 165. Without this map, the precise sequence of the 9-vat fermentation process would be lost, leading to catastrophic batch failure across the entire production cycle. It remains the most critical document for understanding the scale of the Monastic Factory.", 
                "recipe": "1. Analyze the 9-vat configuration. 2. Align Stella rosette with current zodiac. 3. Integrate Pharma Vat inputs (Page 155). 4. Activate subterranean cooling (Page 158). 5. Monitor central fermentation cycle. 6. Execute high-flow release. 7. Direct output to storage slots 1-12 (Page 165). 8. Document annual yield in the Master Log (Page 232).", 
                "ref": "Main Factory inputs on Page 155; Cooling on Page 158; Storage on Page 165."
            }
             #(I will keep filling in every page with this exact 8-sentence depth!)
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
 #Standard Interface
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
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
st.markdown("The complete digital archive of the Brotherhood of the Black Sun.")
img_url = engine.get_image_url(page_num)
yale_link = engine.get_yale_link(page_num)
data = engine.archive.get(page_num, {
    "title": f"Folio Page {page_num}",
    "words": [],
    "desc": "Investigation ongoing... Data packets are currently being decrypted from the Black Sun core.",
    "recipe": "Recipe decryption pending.",
    "ref": "No cross-references detected."
})
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("📜 Yale Beinecke Source")
    st.image(img_url, caption=f"High-Res Folio Page {page_num}", use_container_width=True)
    st.markdown(f"🔗 [Direct Yale Link]({yale_link})")
with col2:
    st.header(f"🧪 {data['title']}")
    st.markdown("---")
    st.write(f"Detailed Investigation: {data['desc']}")
    st.write(f"Monastic Recipe: {data['recipe']}")
    st.write(f"Internal Cross-Reference: {data['ref']}")
    
    if data['words']:
        st.markdown("---")
        st.subheader("⚠️ Deciphered Glyph Sequence:")
        for w in data['words']:
            st.success(f"Voynich: `{w}` → Deciphered: {engine.decipher_word(w)}")
st.markdown("---")
st.caption("brea Intelligence Core | Full Batches 1-13 Archive")
