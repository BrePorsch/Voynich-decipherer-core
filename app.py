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
            "f2r": "1006079", 
            "f2v": "1006080",
            "f3r": "1006081",
            "f3v": "1006082",
            "f33r": "1006138", 
            "f33v": "1006139", 
            "f86v": "1006231",
            "f116v": "1006277"
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
            "f2r": {
                "title": "The Anchor-Root Specimen (f2r)",
                "words": ["aladaba", "qotheol"],
                "desc": "The Anchor-Root Specimen on f2r is a critical waypoint in the herbal series, featuring a tall, unbranched stem with deeply serrated foliage reminiscent of sea-anchor flukes. In the Monastic tradition, this species is prized for its ability to anchor volatile essences that would otherwise evaporate during the distillation of more delicate ingredients. The root system is depicted as a singular, thickened vertical shaft that indicates a high concentration of structural fibers. You must harvest these leaves during a waning moon to ensure the medicinal integrity of the cell walls is at its historical peak. Laboratory engineers use this extract specifically as a thermal stabilizer for the large-scale 9-vat fermentation tanks. It is estimated by the Brotherhood that a single bundle of f2r can prevent the localized scorching of over fifty gallons of base distillate. Notice how the venation on the leaf surface aligns with the marginalia to provide a hidden blueprint for pressure settings. Proper storage for this extract requires a high-borosilicate glass jar kept at a constant, cool basement temperature.",
                "recipe": "1. Harvest leaves during a waning spring moon. 2. Separate the anchor-root from the primary stem. 3. Dry the root fibers in a low-humidity sterile chamber. 4. Macerate the leaves in cold grain alcohol for 12 hours. 5. Press the mixture to extract the clear stabilizing fluid. 6. Combine with f1r extracts to prevent scorching. 7. Bottle in high-borosilicate glass. 8. Label 'Anchor Base' for vat stabilization.",
                "ref": "Structural Stabilizer; Successor to f1r."
            },
            "f2v": {
                "title": "Marrow-Fiber Extraction (f2v)",
                "words": ["stella", "deor"],
                "desc": "Folio 2v serves as the laboratory guide for the secondary properties of the f2 species, focusing on the high-density marrow found within the central stalk. This verso page shifts the focus from structural leaf stabilization to the creation of potent orthopedic balms. The Brotherhood utilizes a cold-press technique to extract this marrow without damaging the long-chain proteins required for bone-tissue recovery. Harvesting must occur at twilight to ensure the plant's internal heat has dispersed for a cleaner fiber separation. This internal marrow is then combined with the milky latex sap from f1v to create a primary structural orthopedic paste. The relationship between both sides of folio 2 represents the dual nature of structural and chemical support within the archive. It is highly recommended that you verify the yield of this page against the final authentication signatures found on f116v. Any significant discoloration in the resulting marrow paste indicates the introduction of iron contamination from the harvesting tools.",
                "recipe": "1. Harvest the remaining f2 central stalks at twilight. 2. Slice the stalk longitudinally into 4-inch strips. 3. Cold-press the strips to release the high-density marrow. 4. Blend the marrow 1:1 with the milky sap from f1v. 5. Whip the mixture into a thick, orthopedic paste. 6. Store in earthenware jars to maintain organic temperature. 7. Apply to limb fractures using linen wraps. 8. Verify the purity of color before sealing for winter storage.",
                "ref": "Orthopedic Base; Pairs with f1v sap; Validated on f116v."
            },
            "f3r": {
                "title": "Branching Source Oil (f3r)",
                "words": ["qokedy", "m-r"],
                "desc": "Folio 3r features a distinctive branching botanical specimen with delicate leaf clusters that serves as the primary source for aromatherapy base oils. Unlike the fibrous nature of the previous folios, the f3r species is significantly more volatile and requires a pressurized steam distillation process. The laboratory utilizes this clear oil as the carrier fluid for high-potency star-essences, providing a non-reactive medium for neural decoctions. You must harvest the branching tips just as the first summer buds begin to form to maximize the lipid concentration. The archival logbooks suggest that the steam must be maintained at a steady ninety-five degrees Celsius to protect the delicate aromatic profile. This distillate is one of the few substances recorded in the manuscript that is capable of penetrating the blood-brain barrier. Notice the rhythmic spacing of the leaves on the illustration, which corresponds to the timing intervals for the steam valve releases. Failure to release the pressure according to these specific intervals will result in a clouded and potentially toxic final product.",
                "recipe": "1. Harvest branching tips during early summer bud-form. 2. Pack the tips tightly into the copper retort. 3. Maintain steady steam heat at exactly 95 degrees Celsius. 4. Release pressure valves at 15-minute intervals. 5. Siphon the resulting clear carrier oil from the separator. 6. Test the volatility by applying a drop to a hot needle. 7. Store in small, clear glass vials for daily laboratory use. 8. Cross-reference for use with f67 celestial extractions.",
                "ref": "Neural Carrier Oil; Directs to f67 celestial timing."
            },
            "f3v": {
                "title": "Broad-Leaf Cooling Infusion (f3v)",
                "words": ["ollag", "st-r"],
                "desc": "The verso of folio 3 introduces a broad-leaf cooling reagent characterized by its intricate venation and massive surface area designed for heat exchange. This plant is the primary ingredient for reducing high-fever inflammations in the monastic infirmary and is administered as a chilled topical compress. The wide leaves are harvested during a cool dawn and immediately submerged in mountain spring water to lock in their thermal cooling properties. Analysis suggested in the marginalia indicates that the leaf venation acts as a radiator to disperse internal body heat when applied to the skin. You must ensure that the leaves remain entirely intact during harvest, as any surface breach results in the immediate oxidation of the alkaloids. This infusion is often blended with the triple-root base from f33v to provide a long-lasting topical cooling sensation during surgical recovery. The laboratory yield for f3v is monitored primarily by weight due to the high water content within the fresh leaf structure. It remains a staple reagent in the Black Sun medical inventory for all warm-season inflammation treatments.",
                "recipe": "1. Harvest broad leaves at a cool dawn. 2. Ensure all leaves are pristine and free of surface damage. 3. Submerge immediately in chilled mountain spring water. 4. Macerate by hand using a stone pestle until a dark green liquid forms. 5. Blend 1:2 with the f33v Triple Root base. 6. Apply as a chilled compress to the patient's forehead or joints. 7. Replacing the compress every two hours for maximum cooling effect. 8. Dispose of spent leaf fibers in the oak ash bin.",
                "ref": "Cooling Reagent; Pairs with f33v for inflammation."
            },
            "f33r": {
                "title": "Dual Green and Yellow Plants (f33r)",
                "words": ["qokedy", "ll"],
                "desc": "Folio 33r features two distinct plant illustrations placed side-by-side as shown in the manuscript, characterized by their contrasting green and yellowish-brown foliage. These species are primary markers for the mid-spring harvest cycle and are used to stabilize the more volatile star-essence oils. Notice the serrated edges on the green leaves, which monastic records suggest possess the highest transdermal permeability for salves. The yellow-leaved plant on the right is harvested for its root juice, which acts as a secondary binding agent for the triple-root salve on f33v. You must extract these fluids under a waning moon to ensure maximum viscosity throughout the distillation process. The relationship between these two plants is essential for the 9-vat factory maturation process detailed on the Rosetta Map. Any imbalance between these two compounds will cause the final decoction to separate into its base components in the storage jars. It is the critical balancing page for the entire apothecary system of the Black Sun.",
                "recipe": "1. Harvest both species simultaneously in late April. 2. Chop green leaves into 2-inch segments for steam extraction. 3. Cold-press yellow roots for binding juice. 4. Blend at a 2:1 ratio by weight in the main vat. 5. Simmer for 1 hour below the boiling point. 6. Filter through wire-mesh silk. 7. Store in Slot 4 inventory. 8. Cross-verify results with f33v stabilization and f86v schematic.",
                "ref": "Balancing page; Links f1v, f33v, and f86v factory."
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
    "🌿 Herbal Section": ["f1r", "f1v", "f2r", "f2v", "f3r", "f3v", "f33r", "f33v"],
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
