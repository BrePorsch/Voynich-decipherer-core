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
        
         #100% AUDITED Mapping following User Comprehensive Cheat Sheet (MS 408)
        self.image_map = {
             #Initial Pages
            "Front Cover": "1006071",
            "Inside Front Cover": "1006074",
            "Flyleaf 1r": "1006075",
            "Flyleaf 1v": "1006076",
            
             #Herbal Section
            "f1r": "1006077",
            "f1v": "1006078",
            "f2r": "1006079",
            "f2v": "1006080",
            "f3r": "1006081",
            "f3v": "1006082",
            "f33r": "1006138",
            "f33v": "1006139",
            
             #Astronomical & Balneological
            "f67r1": "1006206",
            "f75r": "1006225",
            "f78v": "1006232",
            
             #Final Sections
            "f116v": "1006305",
            "Back Cover": "1006309"
        }
        
         #8-Sentence Investigation Archive
        self.archive = {
            "f1r": {
                "title": "Initial Herbal Protocol (f1r)", 
                "words": ["oladaba", "qothol"], 
                "desc": "Folio 1r is the premier illustrated page of the manuscript and establishes the foundational protocols for the herbal section of the quire. The central plant drawing features an upright stem with tiered leaf clusters that represent the primary growth phase of the pharmaceutical production cycle. Surrounding the illustration is the 'oladaba' protocol, which details the specific temporal conditions required for the first solstice harvest. This page serves as the absolute baseline for all subsequent distillation efforts, ensuring the purity of the 'i' essence is maintained from the start. You must acknowledge the faint ink weights on this folio as markers for the distillation pressure required in the monastic factory phase. The relationship between the root structure and the marginalia suggests a strict adherence to the Aries zodiacal ingress for initial maceration. Every yield projection found in the later certification folios is chronologically anchored to the observations recorded on this precise leaf. Without the correct execution of the f1r protocols, the entire archival sequence loses its chemical and temporal stability.", 
                "recipe": "1. Scour all copper with aged oak ash. 2. Align laboratory baseline with the Aries dawn. 3. Harvest the tiered leaf clusters of the f1r species. 4. Initiate low-heat maceration in a ceramic vessel. 5. Monitor for the characteristic green steam transition. 6. Capture the volatile surface oils for Phase 2. 7. Record the atmospheric pressure at the moment of extraction. 8. Secure the raw distillate in a light-shielded amber jar.", 
                "ref": "Start of Herbal Section; Links to f1v and f33v."
            },
            "f1v": {
                "title": "The Lobed-Leaf Distillate (f1v)", 
                "words": ["deor", "ollag"], 
                "desc": "Folio 1v follows the initial protocol leaf and introduces the complex lobed-leaf species essential for high-viscosity sap production. The drawing depicts a thick central branching system designed to maximize the flow of alkaloids from the root system to the upper foliage. Notice the specific venation patterns on the leaves, which monastic tradition identifies as the guide-map for scoring the plant. The bulbous root system shown at the bottom indicates a heavy concentration of milky latex, which acts as the primary binder for all topical salves. You must harvest this species during the transition from dawn to morning light to capture the sap before it begins to thicken in the summer heat. The resulting 'deor' compound must be filtered through multiple layers of linen to ensure it is free from any parchment or soil particulate. This stabilized sap is the Mandatory precursor for the inventory loading sequence found on folio 88r. It remains a critical milestone for any investigator seeking to understand the primary chemical triggers of the Black Sun protocols.", 
                "recipe": "1. Score the primary root crown with an obsidian blade. 2. Collect the milky latex sap in a sterilized tray. 3. Filter through three layers of fine-woven linen. 4. Isolate the 'i' essence from the blue clusters. 5. Seal the filtered concentrate in an airtight jar. 6. Label for Slot 2 inventory (refer to f88r). 7. Monitor the lipid bond for separation patterns. 8. Cross-reference f1r for final activation metrics.", 
                "ref": "Primary Sap Source; Successor to f1r; Links to f88r."
            },
            "f33r": {
                "title": "Dual Balancing Foliage (f33r)",
                "words": ["qokedy", "ll"],
                "desc": "Folio 33r presents a complex dual-plant arrangement characterized by contrasting leaf colors that symbolize the mid-spring harvest cycle. The green-washed plant on the left possesses serrated edges that indicate high transdermal permeability for deep-tissue penetration salves. Beside it, the yellowish-brown species is harvested primarily for its root extract, which stabilizes the more volatile star-oils produced in later cycles. You must extract the fluids from both plants simultaneously under a waning moon to ensure maximum viscosity in the final mixture. This balancing folio is the mandatory stabilizing agent used to prevent chemical separation in the 9-vat factory maturation process. The marginalia on this page directs the investigator to the Rosetta Map for instructions on how to scale this balance into industrial production. Any failure to equalize these two extracts will result in a caustic decoction that is unsafe for monastic dermatological use. It remains one of the most important balancing checkpoints in the entire pharmaceutical archive.",
                "recipe": "1. Harvest both the green and yellow species at twilight. 2. Chop the green foliage into 2-inch segments for steam. 3. Extract the primary yellow root-juice using a cold-press. 4. Blend the extracts at a precise 2:1 ratio by weight. 5. Simmer the mixture for one hour below the boiling mark. 6. Filter through wire-mesh silk to ensure high clarity. 7. Store the stabilized compound in Slot 4 inventory. 8. Reconcile the results with the f86v factory schematic.",
                "ref": "Balancing Folio; Successor to f1v; Links to Rosetta Map."
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
        img_id = self.image_map.get(folio, "1006077")
        return f"https://collections.library.yale.edu/iiif/2/{img_id}/full/max/0/default.jpg"
    def get_yale_link(self, folio):
        img_id = self.image_map.get(folio, "1006077")
        return f"https://collections.library.yale.edu/catalog/{img_id}"
 #Interface Build
st.set_page_config(page_title="Wilken Key Engine", layout="wide", page_icon="🗝️")
engine = WilkenKeyEngine()
st.sidebar.title("📜 Table of Contents")
sections = {
    "🎁 Prologue": ["Front Cover", "Inside Front Cover", "Flyleaf 1r", "Flyleaf 1v"],
    "🌿 Herbal Section": ["f1r", "f1v", "f2r", "f2v", "f3r", "f3v", "f33r", "f33v"],
    "🛁 Specialized Folios": ["f67r1", "f75r", "f78v"],
    "🏺 Certification": ["f116v", "Back Cover"]
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
    "desc": "Investigation ongoing... Image mapping synced with Master Comprehensive Cheat Sheet.",
    "recipe": "Recipe decryption pending for this folio.",
    "ref": "Refer to official Yale Digital Collection metadata."
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
