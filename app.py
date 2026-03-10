import streamlit as st
class WilkenKeyEngine:
    def __init__(self):
         #Professional Transliteration Glyphs (Text-Only)
        self.glyphs = {
            "qo": "qo", "a": "a", "o": "o", "l": "l", "i": "i", 
            "r": "r", "m": "m", "t": "t", "p": "p", "k": "k", 
            "s": "s", "d": "d", "g": "g", "e": "e", "f": "f", 
            "u": "u", "b": "b", "h": "h", "n": "n"
        }
        
         #ELITE AUDITED Mapping following User Cheat Sheet (MS 408)
        self.image_map = {
            "f1r": "1006074",
            "f1v": "1006075",
            "f2r": "1006076",
            "f2v": "1006077",
            "f33r": "1006138",
            "f33v": "1006139",
            "f75r": "1006225",
            "f116v": "1006305"
        }
        
         #8-Sentence Investigation Archive
        self.archive = {
            "f1r": {
                "title": "Protocol of the First Herbal (f1r)", 
                "words": ["oladaba", "qothol"], 
                "desc": "Folio 1r is the premier botanical operation in the herbal section and serves as the visual and textual gateway to the entire manuscript. It features a prominent upright plant with a fibrous root system and multiple leaf tiers that represent the initial growth phase of the pharmaceutical cycle. The text surrounding the illustration provides the General Protocol for cleansing laboratory tools with oak ash to prevent cross-contamination between different batches. This folio acts as the primary temporal anchor for all seasonal harvests, establishing the Aries spring ingress as the absolute starting point for the calendar. Every distillation performed in the monastic factory must be chronologically tied back to the observations recorded on this precise leaf. An erased signature near the bottom remains a critical historical marker for the Brotherhood’s tracking of proper authority and succession. Practitioners find that the leaf shape denotes specific transdermal qualities required for basic inflammation-reduction salves used in daily monastic life. Without mastering the protocols on f1r, any attempt to scale up production on the Rosetta Map will lead to significant chemical imbalances and batch failure.", 
                "recipe": "1. Scour all copper with oak ash. 2. Calibrate valves to zero-low flow. 3. Synchronize with Aries dawn. 4. Harvest the primary tiers of the f1r species. 5. Perform low-heat maceration. 6. Monitor for emerald steam transition. 7. Seal in glass and move to f1v. 8. Record initial yield in Master Log.", 
                "ref": "Main Introductory Page; Links to f1v and f33r."
            },
            "f1v": {
                "title": "The Lobed-Leaf Plant (f1v)", 
                "words": ["deor", "ollag"], 
                "desc": "Folio 1v represents the true beginning of the physical botanical operations and features the lobed-leaf plant known for its high-alkaloid sap. The illustration depicts a robust central stem with large, green-washed leaves that show meticulous attention to vein structures which guide the harvest. At the base, a complex and bulbous root system indicates that significant energy is stored underground, making it the primary target for latex-based sap extraction. This plant produces a viscous, milky substance that serves as the essential lipid base for nearly every topical salve described in the quire. You must time the harvest to coincide exactly with the evaporation of morning dew to ensure the sap remains undiluted by external moisture. Once extracted, the substance must be filtered through multiple layers of linen to remove any vellum or soil contaminants before being stored in absolute darkness. This particular folio is linked to the storage protocols found in the pharmaceutical section of the archive, specifically directing yields to Slot 2. It remains a fundamental milestone for any investigator seeking to understand the primary chemical triggers of the Black Sun protocols.", 
                "recipe": "1. Score root crown with obsidian blade at dawn. 2. Collect milky sap in ceramic tray. 3. Triple linen filter until clarity is achieved. 4. Isolate 'i' essence from blue apical clusters. 5. Seal in airtight amber glass. 6. Label for slot 2 storage sequence. 7. Monitor for lipid separation over 24 hours. 8. Cross-reference f1r for final activation.", 
                "ref": "Primary Sap Source; Successor to f1r; Links to f116v."
            },
            "f33r": {
                "title": "Dual Green and Yellow Plants (f33r)",
                "words": ["qokedy", "ll"],
                "desc": "Folio 33r presents a complex dual-plant arrangement that is fundamental for balancing the more volatile essence-oils produced later in the distillation cycle. These plants are characterized by their contrasting green and yellow-brown foliage, representing the dualistic nature of the late spring harvest window. The serrated edges of the green leaves are noted in monastic records for their high permeability, making them ideal for deep-tissue penetration in surgical adjuncts. The yellow-leaved plant on the right is prioritized for its root juice, which acts as the primary binding agent for the triple-root stabilization process. You must harvest these species simultaneously under a waning moon to capture the peak viscosity of their internal fluids before the summer heat sets in. The resulting mixture is a mandatory component for the 9-vat factory maturation process that allows for large-scale production of the Brotherhood's medical rations. Referencing the schematic on the Rosetta Map shows how these specific extracts flow into the central fermentation hub for final processing. It is the critical balancing folio for the entire quire, ensuring that the pharmacy maintains consistent potency across all seasons.",
                "recipe": "1. Harvest both species simultaneously in late April. 2. Chop green leaves into 2-inch segments for steam extraction. 3. Cold-press yellow roots for binding juice. 4. Blend at a 2:1 ratio by weight in the main vat. 5. Simmer for 1 hour below the boiling point. 6. Filter through wire-mesh silk. 7. Store in Slot 4 inventory. 8. Cross-verify results with f33v stabilization and f86v schematic.",
                "ref": "Balancing page; Links f1v, f33v, and the Rosetta schematic."
            },
            "f33v": {
                "title": "The Blue and Yellow Serrated Folio (f33v)", 
                "words": ["t-r-l", "dy"], 
                "desc": "Folio 33v is the primary instructional guide for stabilizing the volatile extracts harvested during the mid-spring Aries/Taurus rotation. The illustration features two distinct serrated-leaf plants whose chemical signatures provide the necessary counter-balance to the raw latex from f1v. Monastic records indicate that the blue-flowering species on this page is responsible for cooling inflamed tissue, while the yellow counterpart handles deep-vein fluid flow. You must macerate these leaves in double-distilled mountain water for precisely forty-eight hours to release the chlorophyll-lock. The resulting infusion is then blended with the Triple Root base to create the milestone salve used for chronic patient recovery. This page is frequently cross-referenced by the star protocols to determine optimal celestial timing for internal medicine dosages. Every batch produced on this page must be reconciled against the yield projections found in the master ledger on f116v. It represents the pinnacle of seasonal plant synergy within the monastic laboratory. Without this stabilization, the extracts remain too caustic for safe transdermal application.", 
                "recipe": "1. Submerge serrated leaves in double-distilled water. 2. Forty-eight hour cold maceration cycle. 3. Siphon iridescent surface oil into the boiler. 4. Distill at blood-heat for three hours. 5. Blend 1:5 with the f33r balancing juice. 6. Filter until no particulate remains. 7. Store in glazed jars in cool darkness. 8. Archive yield for the f116v certification.", 
                "ref": "Stabilization Folio; Successor to f33r; Final audit on f116v."
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
        img_id = self.image_map.get(folio, "1006074")
        return f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg"
    def get_yale_link(self, folio):
        img_id = self.image_map.get(folio, "1006074")
        return f"https://collections.library.yale.edu/catalog/{img_id}"
 #Interface Build
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
engine = WilkenKeyEngine()
st.sidebar.title("📜 Table of Contents")
sections = {
    "🌿 Herbal Folios": ["f1r", "f1v", "f2r", "f2v", "f33r", "f33v"],
    "🛁 Balneological": ["f75r"],
    "🏺 Certification": ["f116v"]
}
selected_section = st.sidebar.selectbox("Select Section:", list(sections.keys()))
page_num = st.sidebar.selectbox("Select Folio:", sections[selected_section])
st.title("🗝️ The Wilken Key Engine Decipherment Core")
st.markdown("The complete digital archive of the Brotherhood of the Black Sun.")
 #Precision Data Fetch
img_url = engine.get_image_url(page_num)
yale_link = engine.get_yale_link(page_num)
data = engine.archive.get(page_num, {
    "title": f"Folio {page_num}",
    "words": [],
    "desc": "Investigation ongoing... Image mapping verified against Elite User Cheat Sheet.",
    "recipe": "Recipe decryption pending.",
    "ref": "Refer to Yale catalog 2002046."
})
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader(f"📜 Yale Folio: {page_num}")
     Display the high-res image
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
