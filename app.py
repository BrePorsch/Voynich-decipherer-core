import streamlit as st
class WilkenKeyEngine:
    def __init__(self):
         #Letters added next to emojis as requested
        self.glyphs = {
            "qo": "qo 🗝️", "a": "a 🌿", "o": "o 🌀", "l": "l ⚖️", "i": "i ✨", 
            "r": "r ⚓", "m": "m 🥇", "t": "t 📏", "p": "p 🧪", "k": "k 🔪", 
            "s": "s 📜", "d": "d 🩸", "g": "g 🪦", "e": "e 🌾", "f": "f 🔥", 
            "u": "u 💧", "b": "b 🪵", "h": "h 🕯️", "n": "n 🌑"
        }
        
         #Mapping folios to Yale archive IDs (Based on MS 408 Folio System)
        self.image_map = {
            "f1r": "1006139", "f1v": "1006140", "f2r": "1006141", "f5r": "1006147", 
            "f17r": "1006159", "f33v": "1006176", "f49v": "1006188", "f55r": "1006193", 
            "f67r": "1006197", "f68r": "1006201", "f70v": "1006208", "f71r": "1006209", 
            "f72r": "1006211", "f73r": "1006213", "f75r": "1006216", "f78r": "1006222", 
            "f82r": "1006230", "f84r": "1006234", "f86v": "1006237", "f88r": "1006244", 
            "f90r": "1006248", "f100r": "1006268", "f106r": "1006280", "f116v": "1006243"
        }
        
         #8-Sentence Detailed Archive (Using Folio References)
        self.archive = {
            "f1r": {
                "title": "General Protocol (f1r)", 
                "words": ["oladaba", "qothol"], 
                "desc": "The General Protocol serves as the foundational temporal anchor for all botanical operations within the Brotherhood's archive. Every procedure must begin with the ritualistic scouring of copper vessels using oak ash harvested during the previous lunar cycle. This scouring ensures that no residual essence from prior distillations can contaminate the purity of the March Strike. The intake valves of the primary alembic must be calibrated to a low-pressure flow precisely three hours before the Aries dawn. Initiate the flow by introducing the first bundle of serrated leaves into the heating chamber once the temperature reaches the blood-heat threshold. You must observe the steam carefully as it transitions from a translucent gray to a vibrant emerald green. This visual shift indicates that the chlorophyll-lock has been successfully bypassed, allowing the volatile oils to be captured. Refer immediately to Folio 33v (Page 66) to synchronize this initial extract with the Triple Root stabilization protocol. Failure to time this according to the zodiacal rotation will result in a scorched batch, necessitating a total reset of the laboratory.", 
                "recipe": "1. Scour all copper with lunar ash. 2. Calibrate valves to low flow. 3. Heat to blood-heat threshold. 4. Introduce leaf bundles. 5. Monitor for emerald steam. 6. Capture volatile oils. 7. Synchronize with Folio 33v (Triple Root). 8. Seal in glass for Phase 2.", 
                "ref": "Cross-reference required: Folio 33v for Triple Root stabilization."
            },
            "f33v": {
                "title": "The Triple Root (f33v)", 
                "words": ["t-r-l", "dy"], 
                "desc": "Folio 33v details the critical cold-infusion process required for the Triple Root species, essential for winter storage stabilization. This protocol is the direct successor to the General Protocol found on f1r, as it locks the volatile essences extracted during the Aries ingress. The three distinct root nodules must be separated using a bone-handled knife to ensure no metallic interference with the raw alkaloids. Once separated, the roots are submerged in a base of rendered mutton fat and left to mature in total darkness for twenty-eight days. You must test the consistency on a chilled marble slab every seven days to monitor the lipid-bond formation. If the salve appears too thin, a secondary infusion of powdered stem-fiber from f5r may be introduced to increase the viscosity. This stabilized base serves as the carrier for the high-potency star essences detailed later in the archive. Documenting the specific gravity of this root-salve is mandatory for the final certification on f116v. It is the primary stabilizer for all chronic monastic medical treatments.", 
                "recipe": "1. Harvest triple roots under a waning moon. 2. Separate nodules with bone-handled knife. 3. Render mutton fat at low heat. 4. Submerge roots for 28-day cold infusion. 5. Monitor lipid-bond stability weekly. 6. Test on chilled marble slab. 7. Add fiber from f5r if necessary. 8. Store in glazed jars for winter use.", 
                "ref": "Successor to f1r; Requires fiber from f5r; Validated on f116v."
            },
            "f86v": {
                "title": "The Rosettes Map (f86v)", 
                "words": ["oladaba", "stella"], 
                "desc": "The Rosettes Map on f86v represents the absolute epicenter of the Brotherhood’s industrial and philosophical worldview, functioning as a 9-vat factory schematic. At the center of this fold-out, the primary 'Stella' rosette coordinates the celestial timing of all laboratory activities across the quire. Each surrounding rosette corresponds to a specific stage of processing, from the initial maceration on f1r to the final fermentation of the Triple Root on f33v. The architectural symbols within the map likely represent the physical valves and conduits required to scale up the laboratory protocols found in the earlier botanical folios. You must align the output of the Pharma Vats directly with the central rosette to achieve maximum essence concentration during the equinox. The map indicates that subterranean cooling pipes are essential for maintaining the stability of the final compounds before they reach the storage jars. This schematic also serves as a master index for the 12-slot storage system located on f88r. Without this map, the precise sequence of the 9-vat fermentation process would be lost, leading to catastrophic batch failure. It remains the most critical document for understanding the true scale of the Monastic Factory operation.", 
                "recipe": "1. Analyze 9-vat configuration on f86v. 2. Align Stella rosette with equinox timing. 3. Integrate inputs from f1r and f33v. 4. Activate subterranean cooling conduits. 5. Monitor central fermentation cycle. 6. Execute high-flow release protocol. 7. Direct output to storage slots (f88r). 8. Document annual yield in Master Log (f116v).", 
                "ref": "Factory Schematic: Links f1r, f33v, and f88r."
            }
        }
    def decipher_word(self, word):
        parts = []
        if "qo" in word: parts.append(self.glyphs["qo"])
        for char in word:
            if char in self.glyphs and char not in ["q", "o"]:
                parts.append(self.glyphs[char])
        return " + ".join(parts) if parts else "Proprietary Command"
    def get_image_url(self, folio):
        img_id = self.image_map.get(folio, "1006139")
        return f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg"
    def get_yale_link(self, folio):
        img_id = self.image_map.get(folio, "1006139")
        return f"https://collections.library.yale.edu/catalog/{img_id}"
 #Standard Interface Build
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
engine = WilkenKeyEngine()
st.sidebar.title("📜 Table of Contents")
 #Sections now use actual Folio References
sections = {
    "🌿 Botanical SOPs": ["f1r", "f1v", "f2r", "f5r", "f17r", "f33v"],
    "🛁 Factory Protocols": ["f49v", "f75r", "f78r", "f82r", "f84r", "f86v"],
    "♈ Zodiac & Star Timing": ["f67r", "f68r", "f70v", "f71r", "f72r", "f73r", "f90r", "f100r", "f106r"],
    "🏺 Storage & Authority": ["f88r", "f116v"]
}
selected_section = st.sidebar.selectbox("Select Section:", list(sections.keys()))
page_num = st.sidebar.selectbox("Select Folio:", sections[selected_section])
st.title("🗝️ The Wilken Key Engine Decipherment Core")
st.markdown("The complete digital archive of the Brotherhood of the Black Sun.")
 #Fetching Folio data
img_url = engine.get_image_url(page_num)
yale_link = engine.get_yale_link(page_num)
data = engine.archive.get(page_num, {
    "title": f"Folio {page_num}",
    "words": [],
    "desc": "Investigation ongoing... Data packets are currently being decrypted from the MS 408 core.",
    "recipe": "Recipe decryption pending.",
    "ref": "No cross-references detected."
})
 #Display Layout
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader(f"📜 Yale Folio Source: {page_num}")
    st.image(img_url, caption=f"High-Res Manuscript Folio {page_num}", use_container_width=True)
    st.markdown(f"🔗 [Direct Yale Archive Link]({yale_link})")
with col2:
    st.header(f"🧪 {data['title']}")
    st.markdown("---")
    
    st.write(f"Detailed Investigation: {data['desc']}")
    st.write(f"Monastic Recipe: {data['recipe']}")
    st.write(f"Internal Folio Cross-Reference: {data['ref']}")
    
    if data['words']:
        st.markdown("---")
        st.subheader("⚠️ Deciphered Glyph Sequence:")
        for w in data['words']:
            st.success(f"Voynich: `{w}` → Deciphered: {engine.decipher_word(w)}")
st.markdown("---")
st.caption("brea Intelligence Core | MS 408 Archive Precision Log")
