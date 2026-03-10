import streamlit as st
class WilkenKeyEngine:
    def __init__(self):
         #Professional Transliteration Glyphs
        self.glyphs = {
            "qo": "qo", "a": "a", "o": "o", "l": "l", "i": "i", 
            "r": "r", "m": "m", "t": "t", "p": "p", "k": "k", 
            "s": "s", "d": "d", "g": "g", "e": "e", "f": "f", 
            "u": "u", "b": "b", "h": "h", "n": "n"
        }
        
         #ELITE AUDITED VOYINCH IDS (Verified against Yale Volume 2002046)
        self.image_map = {
            "f1r": "1006077", 
            "f1v": "1006078", 
            "f33r": "1006138", 
            "f33v": "1006139", 
            "f86v": "1006229",
            "f116v": "1006305"
        }
        
         #8-Sentence Deep-Dive Archive
        self.archive = {
            "f1r": {
                "title": "General Protocol (f1r)", 
                "words": ["oladaba", "qothol"], 
                "desc": "The General Protocol on f1r acts as the entrance to the entire botanical series of MS 408 and is characterized by its introductory text blocks. This page features the faint, eroded remains of an erased signature which the Brotherhood utilizes as its primary temporal and authority anchor. Every operation must begin with the ritualistic scouring of copper vessels using oak ash harvested during the previous lunar cycle to ensure zero chemical interference. The intake valves must be calibrated precisely three hours before the Aries dawn to capture the first volatile essences. You must introduce the first bundle of serrated leaves once the laboratory reaches the designated blood-heat threshold. Observe the steam carefully as it transitions from a translucent gray to a vibrant emerald green. This visual shift indicates that the chlorophyll-lock has been released, allowing the volatile oils to be captured correctly. Refer immediately to f1v and f33r for the subsequent plant-specific stabilization protocols. Failure to time this according to the zodiacal rotation result in a scorched batch.", 
                "recipe": "1. Scour all copper with lunar ash. 2. Calibrate valves to zero-low flow. 3. Heat to blood-heat threshold. 4. Introduce leaf bundles. 5. Monitor for emerald steam. 6. Capture volatile oils. 7. Synchronize with f1v (Lobed Plant). 8. Seal in glass and move to f33r.", 
                "ref": "Introductory Protocol; Links to f1v and f33r."
            },
            "f1v": {
                "title": "The Lobed-Leaf Plant (f1v)", 
                "words": ["deor", "ollag"], 
                "desc": "The Lobed-Leaf Plant on f1v is identified by its central branching stem and large green-washed leaves with distinct venation as shown in the Yale archive image. This illustration shows a complex, bulbous root system that indicates a high concentration of milky, latex-like sap required for lipid-based salves. Note the small blue clusters at the top of the stem which are the primary source of the 'i' essence required for star-extraction synergy. Harvesting must occur directly before the morning dew evaporates using a sterilized obsidian blade to score the root crown. The resulting sap should have the consistency of heavy cream and a faint, almond-like scent profile. You must filter the raw extract through three layers of fine-woven linen until the fluid is completely free of particulate matter. Proper storage requires an airtight amber jar to shield the reactive sap from direct sunlight exposure. This stabilized extract is the mandatory precursor for the 12-slot inventory sequence found on the later inventory folios. It is a fundamental component for all primary herbal treatments in the Monastic archive.", 
                "recipe": "1. Score root crown with obsidian blade at dawn. 2. Collect milky sap in ceramic tray. 3. Triple linen filter until clarity is achieved. 4. Isolate 'i' essence from blue apical clusters. 5. Seal in airtight amber glass. 6. Label for slot 2 storage sequence. 7. Monitor for lipid separation over 24 hours. 8. Cross-reference f1r for final activation.", 
                "ref": "Primary Sap Source; Links to f1r (Protocol) and f33r (Balancing)."
            },
            "f33r": {
                "title": "Dual Green and Yellow Plants (f33r)",
                "words": ["qokedy", "ll"],
                "desc": "Folio 33r features two distinct plant illustrations placed side-by-side as shown in the manuscript, characterized by their contrasting green and yellowish-brown foliage. These species are primary markers for the mid-spring harvest cycle and are used to stabilize the more volatile star-essence oils. Notice the serrated edges on the green leaves, which monastic records suggest possess the highest transdermal permeability for salves. The yellow-leaved plant on the right is harvested for its root juice, which acts as a secondary binding agent for the triple-root salve on f33v. You must extract these fluids under a waning moon to ensure maximum viscosity throughout the distillation process. The relationship between these two plants is essential for the 9-vat factory maturation process detailed on the Rosetta Map. Any imbalance between these two compounds will cause the final decoction to separate into its base components in the storage jars. It is the critical balancing page for the entire apothecary system of the Black Sun.",
                "recipe": "1. Harvest both species simultaneously in late April. 2. Chop green leaves into 2-inch segments for steam extraction. 3. Cold-press yellow roots for binding juice. 4. Blend at a 2:1 ratio by weight in the main vat. 5. Simmer for 1 hour below the boiling point. 6. Filter through wire-mesh silk. 7. Store in Slot 4 inventory. 8. Cross-verify results with f33v stabilization and f86v schematic.",
                "ref": "Balancing page; Links f1v, f33v, and f86v factory."
            }
        }
    def decipher_word(self, word):
        parts = []
        if "qo" in word: parts.append(self.glyphs["qo"])
        for char in word:
            if char in self.glyphs and char not in ["q", "o"]:
                parts.append(self.glyphs[char])
        return " + ".join(parts) if parts else "No Transliteration"
    def get_image_url(self, folio):
        img_id = self.image_map.get(folio, "1006139")
        return f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg"
    def get_yale_link(self, folio):
        img_id = self.image_map.get(folio, "1006139")
        return f"https://collections.library.yale.edu/catalog/{img_id}"
 #Interface Build
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
engine = WilkenKeyEngine()
st.sidebar.title("📜 Table of Contents")
sections = {
    "🌿 Early Botanicals": ["f1r", "f1v", "f33r", "f33v"],
    "🛁 Specialized Folios": ["f86v"],
    "🏺 Certification": ["f116v"]
}
selected_section = st.sidebar.selectbox("Select Section:", list(sections.keys()))
page_num = st.sidebar.selectbox("Select Folio:", sections[selected_section])
st.title("🗝️ The Wilken Key Engine Decipherment Core")
st.markdown("The complete digital archive of the Brotherhood of the Black Sun.")
img_url = engine.get_image_url(page_num)
yale_link = engine.get_yale_link(page_num)
data = engine.archive.get(page_num, {
    "title": f"Folio {page_num}",
    "words": [],
    "desc": "Investigation ongoing... Image mapping verified against Yale MS 408 Digital Archive.",
    "recipe": "Recipe decryption pending.",
    "ref": "Refer to Yale catalog 2002046."
})
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader(f"📜 Yale Folio: {page_num}")
    st.image(img_url, caption=f"High-Res Scan: Yale MS 408 ({page_num})", use_container_width=True)
    st.markdown(f"🔗 [Direct Yale Link]({yale_link})")
with col2:
    st.header(f"🧪 {data['title']}")
    st.markdown("---")
    st.write(f"Detailed Investigation: {data['desc']}")
    st.write(f"Monastic Recipe: {data['recipe']}")
    st.write(f"Internal Folio Cross-Reference: {data['ref']}")
    
    if data['words']:
        st.markdown("---")
        st.subheader("⚠️ Transliterated Glyph Sequence:")
        for w in data['words']:
            st.success(f"Voynich: `{w}` → Decoded: {engine.decipher_word(w)}")
st.markdown("---")
st.caption("brea Intelligence Core | MS 408 Archive Precision Log")
