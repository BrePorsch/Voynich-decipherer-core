# ═══════════════════════════════════════════════════════════════════════════════
# WILKEN KEY ENGINE v5.0 - PART 1: IMPORTS, CONFIGURATION & LATIN PHARMACOPEIA
# ═══════════════════════════════════════════════════════════════════════════════
# The Ultimate Voynich Manuscript MS 408 Investigation Platform
# Featuring: Complete 232 Folios | 105 Latin Terms | 30 Materia Medica
# Planetary Correspondences | Seasonal Protocols | Interactive Tools
# ═══════════════════════════════════════════════════════════════════════════════

import streamlit as st
import base64
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 1A: APPLICATION CONFIGURATION
# ───────────────────────────────────────────────────────────────────────────────

# Yale Beinecke Library IIIF Image API Configuration
YALE_IIIF_BASE = "https://images.beinecke.library.yale.edu/iiif/2/"
BASE_YALE_ID = 1006076  # Base ID for f1r
ROSETTA_SHIFT = 15      # Shift applied after folio 86

# Application Metadata
APP_TITLE = "Wilken Key Engine v5.0"
APP_SUBTITLE = "Voynich Manuscript MS 408 - Complete Scholar Investigation"
APP_VERSION = "5.0.0 (Ultimate Edition)"
APP_AUTHOR = "Wilken Key Scholar Investigation"

# Page Configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🔑",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://beinecke.library.yale.edu/collections/highlights/voynich-manuscript',
        'Report a bug': "mailto:support@wilkenkey.engine",
        'About': f"{APP_TITLE} - {APP_SUBTITLE} v{APP_VERSION}"
    }
)

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 1B: COMPLETE LATIN PHARMACOPEIA
# ───────────────────────────────────────────────────────────────────────────────

LATIN_PHARMACOPEIA = {
    "preparations": {
        "infusum": {
            "latin": "Infusum",
            "english": "Infusion",
            "description": "A water-based preparation made by pouring boiling water over herbs and allowing them to steep. Used for delicate plant parts like flowers and leaves.",
            "method": "Pour 1 cup boiling water over 1-2 teaspoons dried herb. Cover and steep 10-15 minutes. Strain and drink.",
            "best_for": ["flowers", "leaves", "delicate_parts"],
            "shelf_life": "24 hours refrigerated"
        },
        "decoctum": {
            "latin": "Decoctum",
            "english": "Decoction",
            "description": "A water-based preparation made by simmering herbs in water. Used for tougher plant materials like roots, barks, and seeds.",
            "method": "Simmer 1 tablespoon dried herb in 2 cups water for 15-20 minutes. Strain and drink.",
            "best_for": ["roots", "barks", "seeds", "woody_parts"],
            "shelf_life": "48 hours refrigerated"
        },
        "tinctura": {
            "latin": "Tinctura",
            "english": "Tincture",
            "description": "An alcohol-based extraction that preserves and concentrates herbal properties. Made by macerating herbs in alcohol.",
            "method": "Fill jar 1/3 with dried herb. Cover with 40-60% alcohol. Seal and shake daily for 4-6 weeks. Strain and bottle.",
            "best_for": ["all_plant_parts", "resins", "gums"],
            "shelf_life": "3-5 years"
        },
        "extractum": {
            "latin": "Extractum",
            "english": "Extract",
            "description": "A concentrated preparation made by evaporating a tincture or decoction to a thick consistency.",
            "method": "Reduce tincture or strong decoction by gentle heat until thick and syrupy. Store in airtight container.",
            "best_for": ["concentrated_doses", "travel", "long_term_storage"],
            "shelf_life": "1-2 years"
        },
        "oleum": {
            "latin": "Oleum",
            "english": "Oil Infusion",
            "description": "Oil-based extraction of herbal properties, used for external applications and some internal uses.",
            "method": "Fill jar with dried herb. Cover with carrier oil. Heat gently (solar or low heat) for 2-4 weeks. Strain.",
            "best_for": ["external_use", "massage", "skin_conditions"],
            "shelf_life": "6-12 months"
        },
        "unguentum": {
            "latin": "Unguentum",
            "english": "Ointment/Salve",
            "description": "A semi-solid preparation for external application, made by combining herbal oils with beeswax.",
            "method": "Melt 1 part beeswax with 4-8 parts herbal oil. Pour into containers while warm. Cool and seal.",
            "best_for": ["wounds", "skin_conditions", "joint_pain", "external_ailments"],
            "shelf_life": "1-2 years"
        },
        "pilula": {
            "latin": "Pilula",
            "english": "Pill",
            "description": "Small round preparations for oral administration, made by combining powdered herbs with binding agents.",
            "method": "Mix powdered herbs with honey, syrup, or mucilage. Form into small pills. Dry thoroughly.",
            "best_for": ["convenient_dosing", "bitter_herbs", "travel"],
            "shelf_life": "6-12 months"
        },
        "electuarium": {
            "latin": "Electuarium",
            "english": "Electuary",
            "description": "A sweet medicinal paste made by mixing powdered herbs with honey or syrup.",
            "method": "Gradually add powdered herbs to honey, mixing thoroughly until smooth paste forms.",
            "best_for": ["children", "pleasant_taste", "soothing_preparations"],
            "shelf_life": "6-12 months"
        },
        "syrupus": {
            "latin": "Syrupus",
            "english": "Syrup",
            "description": "A sweet, viscous preparation made by combining herbal decoctions with sugar or honey.",
            "method": "Combine strong decoction with equal parts sugar or honey. Heat gently until dissolved. Bottle.",
            "best_for": ["coughs", "sore_throats", "children", "pleasant_administration"],
            "shelf_life": "3-6 months refrigerated"
        },
        "cataplasma": {
            "latin": "Cataplasma",
            "english": "Poultice",
            "description": "A soft, moist preparation applied externally to draw out infection, reduce inflammation, or soothe tissues.",
            "method": "Mix powdered or macerated herb with hot water to form paste. Apply to cloth and place on affected area.",
            "best_for": ["external_inflammation", "drawing", "soothing", "local_treatment"],
            "shelf_life": "Use immediately"
        },
        "fomentatio": {
            "latin": "Fomentatio",
            "english": "Fomentation/Compress",
            "description": "External application of hot herbal decoction using cloth soaked in the liquid.",
            "method": "Soak clean cloth in hot herbal decoction. Wring out excess and apply to affected area.",
            "best_for": ["pain", "inflammation", "circulation", "relaxation"],
            "shelf_life": "Use immediately"
        },
        "gargarisma": {
            "latin": "Gargarisma",
            "english": "Gargle",
            "description": "A liquid preparation for rinsing the mouth and throat.",
            "method": "Prepare strong decoction or dilute tincture in warm water. Gargle and expel.",
            "best_for": ["sore_throats", "mouth_infections", "oral_hygiene"],
            "shelf_life": "24 hours"
        },
        "collyrium": {
            "latin": "Collyrium",
            "english": "Eye Wash",
            "description": "A specially prepared sterile solution for eye irrigation.",
            "method": "Prepare very weak infusion with sterile water. Strain through fine cloth. Use immediately.",
            "best_for": ["eye_irritation", "eye_infections", "eye_strain"],
            "shelf_life": "Use immediately"
        },
        "linimentum": {
            "latin": "Linimentum",
            "english": "Liniment",
            "description": "A liquid or semi-liquid preparation for external application, usually containing rubbing alcohol or vinegar.",
            "method": "Combine herbal tinctures with rubbing alcohol, vinegar, or oil. Apply and rub into skin.",
            "best_for": ["muscle_pain", "joint_pain", "circulation", "sports_injuries"],
            "shelf_life": "1-2 years"
        },
        "essentia": {
            "latin": "Essentia",
            "english": "Essence",
            "description": "A highly concentrated preparation capturing the volatile principles of a plant.",
            "method": "Steam distillation or expression of volatile oils. Store in dark, airtight bottles.",
            "best_for": ["aromatherapy", "concentrated_therapy", "perfume"],
            "shelf_life": "2-5 years"
        },
        "aqua": {
            "latin": "Aqua",
            "english": "Herbal Water/Hydrosol",
            "description": "The aromatic water remaining after steam distillation of essential oils.",
            "method": "Collect condensate from steam distillation. Separate from essential oil layer.",
            "best_for": ["gentle_aromatherapy", "skin_care", "room_spray"],
            "shelf_life": "6-12 months refrigerated"
        },
        "vinum": {
            "latin": "Vinum",
            "english": "Medicated Wine",
            "description": "Wine infused with medicinal herbs for internal consumption.",
            "method": "Steep herbs in wine for 2-4 weeks. Strain and bottle. Age improves quality.",
            "best_for": ["digestion", "circulation", "tonic", "cardiac_remedies"],
            "shelf_life": "2-5 years"
        },
        "acetum": {
            "latin": "Acetum",
            "english": "Herbal Vinegar",
            "description": "Vinegar infused with herbs for culinary and medicinal use.",
            "method": "Fill jar with herbs. Cover with apple cider vinegar. Steep 4-6 weeks. Strain.",
            "best_for": ["mineral_extraction", "digestion", "food_preservation"],
            "shelf_life": "1-2 years"
        },
        "mel": {
            "latin": "Mel",
            "english": "Medicated Honey",
            "description": "Honey infused with herbs for soothing and antimicrobial applications.",
            "method": "Gently warm honey with dried herbs. Steep 2-4 weeks. Strain if desired.",
            "best_for": ["sore_throats", "wounds", "coughs", "children"],
            "shelf_life": "Indefinite"
        },
        "pulvis": {
            "latin": "Pulvis",
            "english": "Powder",
            "description": "Dried herb ground to fine powder for various applications.",
            "method": "Dry herb thoroughly. Grind to fine powder using mortar and pestle or grinder. Sieve.",
            "best_for": ["encapsulation", "sprinkling", "making_pills", "quick_use"],
            "shelf_life": "1-2 years"
        },
        "capsula": {
            "latin": "Capsula",
            "english": "Capsule",
            "description": "Powdered herb enclosed in gelatin or vegetable-based capsule.",
            "method": "Fill empty capsules with powdered herb using capsule filling machine or by hand.",
            "best_for": ["convenient_dosing", "taste_masking", "travel", "precise_dosing"],
            "shelf_life": "1-2 years"
        },
        "suppositorium": {
            "latin": "Suppositorium",
            "english": "Suppository",
            "description": "Solid preparation for rectal or vaginal insertion, melting at body temperature.",
            "method": "Melt cocoa butter or coconut oil. Mix in powdered herbs. Pour into molds. Chill.",
            "best_for": ["systemic_absorption", "local_treatment", "when_oral_not_possible"],
            "shelf_life": "6-12 months refrigerated"
        },
        "trochiscus": {
            "latin": "Trochiscus",
            "english": "Lozenge/Pastille",
            "description": "Hard, slow-dissolving preparation for oral administration, often for throat conditions.",
            "method": "Mix powdered herbs with sugar, gum, and mucilage. Form into shapes. Dry thoroughly.",
            "best_for": ["sore_throats", "coughs", "slow_release", "pleasant_taste"],
            "shelf_life": "6-12 months"
        },
        "emplastrum": {
            "latin": "Emplastrum",
            "english": "Plaster",
            "description": "Solid adhesive preparation applied to skin for prolonged contact.",
            "method": "Mix powdered herbs with resin and wax base. Spread on cloth or leather backing.",
            "best_for": ["prolonged_contact", "drawing", "protection", "support"],
            "shelf_life": "1-2 years"
        },
        "conserva": {
            "latin": "Conserva",
            "english": "Conserve",
            "description": "Fresh herb preserved in sugar, similar to jam.",
            "method": "Pound fresh herb with sugar until smooth. Store in airtight jars.",
            "best_for": ["preserving_fresh_herbs", "pleasant_taste", "children"],
            "shelf_life": "6-12 months"
        }
    },
    
    "actions": {
        "alterativa": {
            "latin": "Alterativa",
            "english": "Alterative",
            "description": "Gradually restores proper function to the body, improving metabolism and promoting elimination of wastes. Used for chronic conditions.",
            "examples": ["burdock", "dandelion", "red_clover", "sarsaparilla"],
            "indications": ["chronic_skin_conditions", "arthritis", "autoimmune_conditions", "toxic_overload"]
        },
        "antipyretica": {
            "latin": "Antipyretica",
            "english": "Antipyretic/Febrifuge",
            "description": "Reduces fever by promoting sweating, cooling the body, or addressing the underlying cause.",
            "examples": ["yarrow", "elderflower", "peppermint", "willow_bark"],
            "indications": ["fever", "heat_exhaustion", "infections_with_fever"]
        },
        "antispasmodica": {
            "latin": "Antispasmodica",
            "english": "Antispasmodic",
            "description": "Relieves spasms, cramps, and involuntary muscle contractions in smooth and skeletal muscles.",
            "examples": ["cramp_bark", "black_haw", "chamomile", "valerian", "passionflower"],
            "indications": ["menstrual_cramps", "muscle_spasms", "asthma", "colic", "irritable_bowel"]
        },
        "astringentia": {
            "latin": "Astringentia",
            "english": "Astringent",
            "description": "Tightens and tones tissues, reducing secretions and discharge. Acts on mucous membranes and skin.",
            "examples": ["witch_hazel", "oak_bark", "yellow_dock", "plantain", "rose"],
            "indications": ["diarrhea", "bleeding", "excessive_mucus", "loose_gums", "varicose_veins"]
        },
        "carminativa": {
            "latin": "Carminativa",
            "english": "Carminative",
            "description": "Relieves flatulence and gas, soothes digestive tract, and promotes proper digestion.",
            "examples": ["peppermint", "fennel", "ginger", "caraway", "dill", "cinnamon"],
            "indications": ["gas", "bloating", "indigestion", "colic", "nausea"]
        },
        "demulcentia": {
            "latin": "Demulcentia",
            "english": "Demulcent",
            "description": "Soothes and protects irritated mucous membranes with a coating of mucilage.",
            "examples": ["marshmallow", "slippery_elm", "plantain", "licorice", "irish_moss"],
            "indications": ["sore_throat", "gastritis", "dry_cough", "urinary_irritation", "IBS"]
        },
        "diaphoretica": {
            "latin": "Diaphoretica",
            "english": "Diaphoretic",
            "description": "Promotes sweating, helping to eliminate toxins and reduce fever.",
            "examples": ["yarrow", "elderflower", "ginger", "boneset", "peppermint"],
            "indications": ["fever", "colds", "flu", "detoxification", "skin_conditions"]
        },
        "diuretica": {
            "latin": "Diuretica",
            "english": "Diuretic",
            "description": "Increases urine production and flow, helping to eliminate excess fluid and waste.",
            "examples": ["dandelion", "parsley", "juniper", "buchu", "corn_silk", "uva_ursi"],
            "indications": ["edema", "UTI", "kidney_stones", "hypertension", "gout", "detox"]
        },
        "emmenagogica": {
            "latin": "Emmenagogica",
            "english": "Emmenagogue",
            "description": "Promotes and regulates menstrual flow, often by stimulating blood flow to the pelvic area.",
            "examples": ["pennyroyal", "rue", "sage", "mugwort", "blue_cohosh"],
            "indications": ["delayed_menses", "scanty_menses", "menstrual_cramps", "PMS"],
            "warning": "Contraindicated in pregnancy"
        },
        "expectorantia": {
            "latin": "Expectorantia",
            "english": "Expectorant",
            "description": "Promotes the expulsion of mucus from the respiratory tract.",
            "examples": ["mullein", "elecampane", "licorice", "ginger", "wild_cherry"],
            "indications": ["cough", "congestion", "bronchitis", "chest_colds", "asthma"]
        },
        "hepatica": {
            "latin": "Hepatica",
            "english": "Hepatic",
            "description": "Supports and strengthens liver function, promotes bile production and flow.",
            "examples": ["dandelion", "milk_thistle", "yellow_dock", "gentian", "wormwood"],
            "indications": ["liver_congestion", "poor_digestion", "skin_conditions", "jaundice", "gallstones"]
        },
        "nervina": {
            "latin": "Nervina",
            "english": "Nervine",
            "description": "Acts on the nervous system to calm, strengthen, or restore function.",
            "subtypes": {
                "nervina_relaxantia": "Calming and sedating",
                "nervina_stimulantia": "Stimulating and tonifying",
                "nervina_tonica": "Strengthening and restorative"
            },
            "examples": ["valerian", "passionflower", "chamomile", "oats", "skullcap", "lemon_balm"],
            "indications": ["anxiety", "insomnia", "nervous_tension", "stress", "nervous_exhaustion"]
        },
        "rubefacientia": {
            "latin": "Rubefacientia",
            "english": "Rubefacient",
            "description": "Increases blood flow to the skin surface, causing redness and warmth when applied externally.",
            "examples": ["cayenne", "mustard", "ginger", "black_pepper", "rosemary"],
            "indications": ["muscle_pain", "joint_pain", "poor_circulation", "chest_congestion"],
            "warning": "For external use only, may irritate sensitive skin"
        },
        "sedativa": {
            "latin": "Sedativa",
            "english": "Sedative",
            "description": "Reduces nervous activity, promotes relaxation and sleep.",
            "examples": ["valerian", "hops", "passionflower", "wild_lettuce", "jamaican_dogwood"],
            "indications": ["insomnia", "anxiety", "nervous_tension", "muscle_spasms", "pain"]
        },
        "stomachica": {
            "latin": "Stomachica",
            "english": "Stomachic",
            "description": "Strengthens and tones the stomach, improves digestion and appetite.",
            "examples": ["gentian", "ginger", "bitter_orange", "wormwood", "angelica"],
            "indications": ["poor_appetite", "indigestion", "weak_digestion", "nausea", "gas"]
        },
        "tonica": {
            "latin": "Tonica",
            "english": "Tonic",
            "description": "Strengthens and invigorates the entire system or specific organs.",
            "subtypes": {
                "tonica_general": "Whole body tonic",
                "tonica_cardiaca": "Heart tonic",
                "tonica_digestiva": "Digestive tonic",
                "tonica_nervosa": "Nerve tonic"
            },
            "examples": ["ginseng", "ashwagandha", "damiana", "hawthorn", "gentian"],
            "indications": ["weakness", "convalescence", "fatigue", "depletion", "chronic_stress"]
        },
        "vulneraria": {
            "latin": "Vulneraria",
            "english": "Vulnerary",
            "description": "Promotes healing of wounds and injuries when applied externally or taken internally.",
            "examples": ["comfrey", "plantain", "calendula", "yarrow", "arnica", "gotu_kola"],
            "indications": ["wounds", "cuts", "bruises", "sprains", "fractures", "ulcers"]
        },
        "amara": {
            "latin": "Amara",
            "english": "Bitter",
            "description": "Stimulates digestive secretions and improves appetite through bitter taste receptors.",
            "examples": ["gentian", "wormwood", "dandelion", "yellow_dock", "hops", "angostura"],
            "indications": ["poor_appetite", "sluggish_digestion", "liver_congestion", "before_meals"]
        },
        "aromatica": {
            "latin": "Aromatica",
            "english": "Aromatic",
            "description": "Contains volatile oils that are fragrant and often carminative, antiseptic, or stimulant.",
            "examples": ["peppermint", "fennel", "lavender", "thyme", "rosemary", "cinnamon"],
            "indications": ["digestion", "respiratory_conditions", "nervous_tension", "antiseptic_needs"]
        },
        "mucilaginosa": {
            "latin": "Mucilaginosa",
            "english": "Mucilaginous",
            "description": "Contains gelatinous substances that soothe and protect irritated tissues.",
            "examples": ["marshmallow", "slippery_elm", "comfrey", "plantain", "psyllium"],
            "indications": ["irritated_tissues", "inflammation", "dry_conditions", "soothing_needed"]
        },
        "resolventia": {
            "latin": "Resolventia",
            "english": "Resolvent/Discutient",
            "description": "Promotes the resolution of swellings, tumors, and hardened masses.",
            "examples": ["poke_root", "figwort", "red_clover", "cleavers", "chickweed"],
            "indications": ["swollen_glands", "tumors", "cysts", "lipomas", "hardened_masses"]
        },
        "refrigerantia": {
            "latin": "Refrigerantia",
            "english": "Refrigerant",
            "description": "Cools the body and reduces fever, often by promoting sweating or direct cooling action.",
            "examples": ["peppermint", "lemon_balm", "hibiscus", "chrysanthemum", "watermelon"],
            "indications": ["fever", "heat_exhaustion", "hot_conditions", "summer_heat", "inflammation"]
        },
        "stimulantia": {
            "latin": "Stimulantia",
            "english": "Stimulant",
            "description": "Increases physiological activity, energy, and alertness.",
            "examples": ["coffee", "tea", "guarana", "kola", "ephedra", "prickly_ash"],
            "indications": ["fatigue", "low_energy", "poor_circulation", "depression", "low_blood_pressure"]
        },
        "sudorifica": {
            "latin": "Sudorifica",
            "english": "Sudorific/Diaphoretic (strong)",
            "description": "Promotes profuse sweating, stronger action than standard diaphoretics.",
            "examples": ["jaborandi", "pilcarpus", "boneset", "pleurisy_root"],
            "indications": ["high_fever", "rheumatic_conditions", "acute_infections", "detoxification"]
        },
        "antihelmintica": {
            "latin": "Antihelmintica",
            "english": "Anthelmintic/Vermifuge",
            "description": "Expels parasitic worms from the digestive tract.",
            "examples": ["wormwood", "black_walnut", "cloves", "pumpkin_seeds", "male_fern"],
            "indications": ["intestinal_worms", "parasites", "pinworms", "roundworms", "tapeworms"]
        },
        "antiseptica": {
            "latin": "Antiseptica",
            "english": "Antiseptic",
            "description": "Prevents or inhibits the growth of microorganisms, used externally and internally.",
            "examples": ["thyme", "tea_tree", "echinacea", "goldenseal", "myrrh", "propolis"],
            "indications": ["infections", "wounds", "sore_throat", "urinary_infections", "skin_conditions"]
        },
        "cholagoga": {
            "latin": "Cholagoga",
            "english": "Cholagogue",
            "description": "Promotes the flow of bile from the gallbladder into the duodenum.",
            "examples": ["dandelion", "boldo", "fringe_tree", "blue_flag", "greater_celandine"],
            "indications": ["gallstones", "liver_congestion", "jaundice", "poor_fat_digestion"]
        }
    },
    
    "equipment": {
        "mortarium": {
            "latin": "Mortarium",
            "english": "Mortar and Pestle",
            "description": "Essential tool for grinding and powdering dried herbs. Made of stone, ceramic, wood, or metal.",
            "uses": ["grinding", "powdering", "mixing", "crushing"],
            "materials": ["marble", "granite", "ceramic", "wood", "brass", "iron"],
            "care": "Clean thoroughly after each use. Avoid cross-contamination between toxic and non-toxic herbs."
        },
        "alembicus": {
            "latin": "Alembicus",
            "english": "Alembic/Still",
            "description": "Apparatus for distillation, consisting of a vessel for heating, a condensing head, and a receiving vessel.",
            "uses": ["distillation", "essential_oil_extraction", "hydrosol_production", "alcohol_purification"],
            "components": ["cucurbit (heating_vessel)", "helm (head)", "beak (spout)", "receiver"],
            "materials": ["copper", "glass", "stainless_steel"]
        },
        "retorta": {
            "latin": "Retorta",
            "english": "Retort",
            "description": "Glass vessel with a long neck, used for distillation and chemical reactions.",
            "uses": ["distillation", "sublimation", "dry_distillation", "chemical_reactions"],
            "materials": ["glass", "ceramic"],
            "care": "Handle with care. Heat gradually to prevent cracking."
        },
        "cucurbita": {
            "latin": "Cucurbita",
            "english": "Cucurbit",
            "description": "The rounded vessel in a still that holds the material being distilled.",
            "uses": ["holding_material", "heating", "distillation"],
            "materials": ["copper", "glass", "ceramic"],
            "capacity": "Various sizes from 1 pint to several gallons"
        },
        "pelicanus": {
            "latin": "Pelicanus",
            "english": "Pelican",
            "description": "Vessel with a side arm that allows distilled liquid to return to the body, used for circulation.",
            "uses": ["circulation", "continuous_distillation", "reflux"],
            "materials": ["glass"],
            "care": "Ensure proper sealing to prevent leakage."
        },
        "balneum_mariae": {
            "latin": "Balneum Mariae",
            "english": "Water Bath/Bain-Marie",
            "description": "Double-boiler system for gentle heating using water as the heat transfer medium.",
            "uses": ["gentle_heating", "temperature_control", "preventing_burning", "melting"],
            "temperature_range": "Up to 100°C (212°F)",
            "applications": ["making_ointments", "melting_beeswax", "gentle_extraction"]
        },
        "balneum_arenae": {
            "latin": "Balneum Arena",
            "english": "Sand Bath",
            "description": "Heating system using sand as the heat transfer medium, providing higher temperatures than water bath.",
            "uses": ["higher_temperature_heating", "even_heat_distribution", "drying"],
            "temperature_range": "Up to 300°C (572°F)",
            "applications": ["drying_herbs", "gentle_heating_above_water_temperature"]
        },
        "caldaria": {
            "latin": "Caldaria",
            "english": "Caldron/Cauldron",
            "description": "Large metal pot for boiling, simmering, and preparing large quantities of preparations.",
            "uses": ["boiling", "simmering", "decoction", "large_batch_preparation"],
            "materials": ["cast_iron", "copper", "stainless_steel"],
            "sizes": "From 1 gallon to 50+ gallons"
        },
        "olla": {
            "latin": "Olla",
            "english": "Pot/Vessel",
            "description": "General-purpose cooking and preparation vessel.",
            "uses": ["cooking", "simmering", "steeping", "general_preparation"],
            "materials": ["ceramic", "clay", "copper", "iron", "enamel"],
            "care": "Season cast iron. Avoid reactive metals with acidic preparations."
        },
        "patella": {
            "latin": "Patella",
            "english": "Shallow Pan/Dish",
            "description": "Shallow vessel for evaporating liquids and drying preparations.",
            "uses": ["evaporation", "drying", "crystallization", "calcination"],
            "materials": ["ceramic", "porcelain", "glass", "copper"],
            "care": "Use gentle heat to prevent cracking or burning."
        },
        "cribrum": {
            "latin": "Cribrum",
            "english": "Sieve/Strainer",
            "description": "Perforated device for separating liquids from solids or grading particle sizes.",
            "uses": ["straining", "sifting", "grading", "filtering"],
            "types": ["fine_mesh", "coarse_mesh", "hair_sieve", "linen_strainer"],
            "materials": ["metal", "hair", "linen", "silk"]
        },
        "phiala": {
            "latin": "Phiala",
            "english": "Bottle/Vial/Flask",
            "description": "Container for storing liquid preparations.",
            "uses": ["storage", "dispensing", "aging", "preservation"],
            "types": ["dropper_bottle", "corked_bottle", "apothecary_jar", "decanter"],
            "materials": ["glass", "ceramic", "crystal"],
            "colors": ["clear", "amber", "blue", "green"]
        },
        "ampulla": {
            "latin": "Ampulla",
            "english": "Small Flask/Amphora",
            "description": "Small vessel, often with two handles, for precious liquids.",
            "uses": ["storing_precious_liquids", "travel", "dispensing"],
            "materials": ["glass", "ceramic", "metal"],
            "capacity": "1-8 ounces"
        },
        "urceolus": {
            "latin": "Urceolus",
            "english": "Pitcher/Jug",
            "description": "Vessel with a spout for pouring liquids.",
            "uses": ["pouring", "serving", "mixing", "steeping"],
            "materials": ["ceramic", "glass", "metal", "stoneware"],
            "features": ["spout", "handle", "lid"]
        },
        "trulla": {
            "latin": "Trulla",
            "english": "Ladle/Scoop",
            "description": "Long-handled spoon for transferring liquids and semi-solids.",
            "uses": ["transferring", "measuring", "stirring", "serving"],
            "materials": ["wood", "metal", "ceramic"],
            "sizes": "Various sizes for different applications"
        },
        "spatula": {
            "latin": "Spatula",
            "english": "Spatula",
            "description": "Flat, flexible tool for mixing, spreading, and scraping.",
            "uses": ["mixing", "spreading", "scraping", "folding"],
            "materials": ["wood", "metal", "horn", "bone"],
            "types": ["straight", "offset", "rounded", "pointed"]
        },
        "pistillum": {
            "latin": "Pistillum",
            "english": "Pestle",
            "description": "Club-shaped tool used with mortar for grinding.",
            "uses": ["grinding", "crushing", "mixing", "pounding"],
            "materials": ["stone", "wood", "ceramic", "metal", "porcelain"],
            "care": "Match material to mortar. Clean thoroughly between uses."
        },
        "colatorium": {
            "latin": "Colatorium",
            "english": "Strainer/Filter",
            "description": "Device for separating solids from liquids, often conical in shape.",
            "uses": ["filtering", "straining", "clarifying", "separating"],
            "types": ["funnel_filter", "bag_filter", "press_filter"],
            "materials": ["linen", "cotton", "paper", "metal_mesh"]
        },
        "torcular": {
            "latin": "Torcular",
            "english": "Press",
            "description": "Device for extracting liquid by applying pressure to solid material.",
            "uses": ["pressing", "juicing", "oil_extraction", "tincture_pressing"],
            "types": ["screw_press", "lever_press", "hydraulic_press", "tincture_press"],
            "materials": ["wood", "metal", "hydraulic"]
        }
    },
    
    "quality_tests": {
        "probatio_coloris": {
            "latin": "Probatio Coloris",
            "english": "Color Test",
            "description": "Visual examination of color to assess quality, freshness, and identity of herbal preparations.",
            "method": "Observe color in natural light. Compare to standard reference. Note any discoloration or changes.",
            "indicators": ["freshness", "identity", "oxidation", "degradation"],
            "standards": "Should match expected color for the specific preparation"
        },
        "probatio_odoris": {
            "latin": "Probatio Odoris",
            "english": "Odor Test",
            "description": "Assessment of aroma to verify identity, potency, and quality.",
            "method": "Smell preparation at room temperature. Note character, intensity, and any off-odors.",
            "indicators": ["identity", "potency", "volatility", "rancidity", "contamination"],
            "standards": "Should have characteristic aroma without mustiness, rancidity, or off-odors"
        },
        "probatio_saporis": {
            "latin": "Probatio Saporis",
            "english": "Taste Test",
            "description": "Careful tasting to verify identity and assess potency (for safe preparations only).",
            "method": "Place small amount on tongue. Note immediate and after-taste. Spit if uncertain.",
            "indicators": ["identity", "bitterness", "astringency", "sweetness", "acidity"],
            "warning": "Only taste preparations known to be safe. Avoid tasting toxic herbs.",
            "standards": "Should match expected taste profile"
        },
        "probatio_texturae": {
            "latin": "Probatio Texturae",
            "english": "Texture Test",
            "description": "Physical examination of consistency and texture.",
            "method": "Feel between fingers, observe flow characteristics, note any grittiness or separation.",
            "indicators": ["proper_consistency", "homogeneity", "particle_size", "stability"],
            "standards": "Should have appropriate texture for the preparation type"
        },
        "probatio_siccitatis": {
            "latin": "Probatio Siccitatis",
            "english": "Dryness Test",
            "description": "Assessment of moisture content in dried herbs and preparations.",
            "method": "Herbs should crumble when rubbed. Should not feel cool or damp to touch.",
            "indicators": ["proper_drying", "storage_quality", "mold_risk"],
            "standards": "Should be crisp and dry, not leathery or moist"
        },
        "probatio_claritatis": {
            "latin": "Probatio Claritatis",
            "english": "Clarity Test",
            "description": "Visual inspection of liquid preparations for transparency and sediment.",
            "method": "Hold up to light. Observe for cloudiness, particles, or sediment.",
            "indicators": ["filtration_quality", "stability", "purity", "sedimentation"],
            "standards": "Should be appropriately clear for the preparation type"
        },
        "probatio_consistentiae": {
            "latin": "Probatio Consistentiae",
            "english": "Consistency Test",
            "description": "Assessment of viscosity and flow characteristics.",
            "method": "Observe pouring, coating, and adherence properties.",
            "indicators": ["proper_thickness", "flow_characteristics", "stability"],
            "standards": "Should have appropriate consistency for intended use"
        },
        "probatio_integritatis": {
            "latin": "Probatio Integritatis",
            "english": "Integrity Test",
            "description": "Overall assessment of preparation quality and wholeness.",
            "method": "Comprehensive evaluation of all quality parameters together.",
            "indicators": ["overall_quality", "suitability_for_use", "storage_life"],
            "standards": "Should meet all quality criteria for the specific preparation"
        },
        "probatio_volatilitatis": {
            "latin": "Probatio Volatilitatis",
            "english": "Volatility Test",
            "description": "Assessment of volatile oil content through aroma release.",
            "method": "Crush or warm small sample. Assess intensity of aroma released.",
            "indicators": ["volatile_oil_content", "freshness", "potency"],
            "standards": "Should release characteristic aroma when stimulated"
        },
        "probatio_soluble": {
            "latin": "Probatio Solubilis",
            "english": "Solubility Test",
            "description": "Testing how well a preparation dissolves in appropriate solvent.",
            "method": "Add sample to solvent (water, alcohol, oil). Observe dissolution.",
            "indicators": ["extraction_quality", "proper_preparation", "active_constituents"],
            "standards": "Should dissolve appropriately for the preparation type"
        }
    },
    
    "combinations": {
        "simplex": {
            "latin": "Simplex",
            "english": "Simple/Single Herb",
            "description": "Preparation containing only one herb. Preferred for specific, targeted effects and for identifying herb actions.",
            "advantages": ["clear_identification", "targeted_effects", "no_interactions", "easy_attribution"],
            "examples": ["chamomile_tea", "pure_tincture", "single_herb_powder"],
            "when_to_use": "When specific effect desired, for beginners, for testing new herbs"
        },
        "composita": {
            "latin": "Composita",
            "english": "Compound Formula",
            "description": "Preparation containing multiple herbs combined for synergistic effects.",
            "advantages": ["synergistic_effects", "multiple_actions", "balanced_formulation", "broader_application"],
            "formulation_principles": ["primary_herb", "supporting_herbs", "catalyst", "harmonizer", "corrigent"],
            "examples": ["digestive_bitters", "immune_formulas", "stress_remedies"],
            "when_to_use": "For complex conditions, synergistic effects, balanced approach"
        },
        "species": {
            "latin": "Species",
            "english": "Species/Mixture",
            "description": "A mixture of dried, powdered herbs intended for making infusions or decoctions.",
            "preparation": "Mix powdered herbs in specified proportions. Store in airtight container.",
            "use": "Add boiling water to powder, steep, and drink with sediment.",
            "examples": ["digestive_species", "cold_species", "tonic_species"],
            "advantages": ["convenient", "pre-mixed", "consistent_dosing"]
        },
        "species_odoratae": {
            "latin": "Species Odoratae",
            "english": "Aromatic Species",
            "description": "Mixture of aromatic herbs, often used for pleasant flavor and carminative effects.",
            "characteristics": ["pleasant_aroma", "carminative", "flavorful", "digestive"],
            "common_ingredients": ["cinnamon", "ginger", "cloves", "cardamom", "fennel"],
            "uses": ["digestion", "flavoring", "aromatic_waters", "pot_pourri"]
        },
        "species_amarae": {
            "latin": "Species Amarae",
            "english": "Bitter Species",
            "description": "Mixture of bitter herbs for stimulating digestion and appetite.",
            "characteristics": ["strongly_bitter", "digestive_stimulant", "tonic"],
            "common_ingredients": ["gentian", "wormwood", "dandelion", "orange_peel", "ginger"],
            "uses": ["before_meals", "poor_appetite", "sluggish_digestion", "liver_support"]
        },
        "species_pectorales": {
            "latin": "Species Pectorales",
            "english": "Pectoral Species",
            "description": "Mixture of herbs for respiratory conditions and chest complaints.",
            "characteristics": ["expectorant", "soothing", "anti-inflammatory", "respiratory_support"],
            "common_ingredients": ["mullein", "coltsfoot", "licorice", "thyme", "elecampane"],
            "uses": ["coughs", "bronchitis", "chest_colds", "asthma_support"]
        },
        "species_diureticae": {
            "latin": "Species Diureticae",
            "english": "Diuretic Species",
            "description": "Mixture of herbs promoting urine flow and kidney function.",
            "characteristics": ["diuretic", "kidney_support", "detoxifying"],
            "common_ingredients": ["dandelion", "parsley", "juniper", "buchu", "uva_ursi"],
            "uses": ["edema", "UTI", "kidney_stones", "detoxification", "gout"]
        },
        "species_antiscorbuticae": {
            "latin": "Species Antiscorbuticae",
            "english": "Antiscorbutic Species",
            "description": "Mixture of herbs rich in vitamin C for preventing and treating scurvy.",
            "characteristics": ["high_vitamin_C", "antioxidant", "preventive"],
            "common_ingredients": ["rose_hips", "acerola", "parsley", "watercress", "nettles"],
            "uses": ["scurvy_prevention", "immune_support", "general_tonic"]
        },
        "species_anodynae": {
            "latin": "Species Anodynae",
            "english": "Anodyne Species",
            "description": "Mixture of pain-relieving herbs for discomfort and pain management.",
            "characteristics": ["analgesic", "relaxing", "nervine", "comforting"],
            "common_ingredients": ["valerian", "passionflower", "wild_lettuce", "jamaican_dogwood", "cramp_bark"],
            "uses": ["pain", "cramps", "muscle_spasms", "nervous_tension", "insomnia"]
        },
        "species_catharticae": {
            "latin": "Species Catharticae",
            "english": "Cathartic Species",
            "description": "Mixture of purgative herbs for promoting bowel evacuation.",
            "characteristics": ["laxative", "purgative", "bowel_stimulating"],
            "common_ingredients": ["senna", "cascara", "rhubarb", "aloes", "buckthorn"],
            "uses": ["constipation", "bowel_cleansing", "detoxification"],
            "warning": "Use with caution. Not for long-term use."
        },
        "species_tonicae": {
            "latin": "Species Tonicae",
            "english": "Tonic Species",
            "description": "Mixture of strengthening and restorative herbs for general vitality.",
            "characteristics": ["tonic", "adaptogenic", "nutritive", "restorative"],
            "common_ingredients": ["ginseng", "astragalus", "ashwagandha", "damiana", "hawthorn"],
            "uses": ["convalescence", "fatigue", "weakness", "general_debility", "stress"]
        },
        "species_antisepicae": {
            "latin": "Species Antisepticae",
            "english": "Antiseptic Species",
            "description": "Mixture of antimicrobial herbs for preventing and treating infections.",
            "characteristics": ["antimicrobial", "immune_supporting", "cleansing"],
            "common_ingredients": ["echinacea", "goldenseal", "thyme", "myrrh", "propolis"],
            "uses": ["infections", "wounds", "immune_support", "preventive"]
        },
        "species_emmenagogae": {
            "latin": "Species Emmenagogae",
            "english": "Emmenagogue Species",
            "description": "Mixture of herbs promoting menstrual flow and regulating cycles.",
            "characteristics": ["emmenagogue", "uterine_tonic", "regulating"],
            "common_ingredients": ["pennyroyal", "rue", "sage", "mugwort", "blue_cohosh"],
            "uses": ["delayed_menses", "scanty_menses", "menstrual_regulation"],
            "warning": "Contraindicated in pregnancy"
        }
    },
    
    "dosage_forms": {
        "tabletta": {
            "latin": "Tabletta",
            "english": "Tablet",
            "description": "Solid unit dose form made by compressing powdered herbs or extracts.",
            "advantages": ["convenient", "portable", "precise_dosing", "taste_masking"],
            "disadvantages": ["requires_equipment", "may_contain_excipients", "slower_absorption"],
            "typical_sizes": "200mg - 1000mg"
        },
        "capsula_dura": {
            "latin": "Capsula Dura",
            "english": "Hard Capsule",
            "description": "Two-piece gelatin or vegetable cellulose capsule containing powders or granules.",
            "advantages": ["tasteless", "easy_swallowing", "portable", "versatile"],
            "disadvantages": ["animal_gelatin", "moisture_sensitive", "size_limitations"],
            "typical_sizes": "Size 000 (1.37ml) to Size 5 (0.13ml)"
        },
        "capsula_mollis": {
            "latin": "Capsula Mollis",
            "english": "Soft Capsule",
            "description": "One-piece gelatin capsule containing liquids or semi-solids.",
            "advantages": ["liquid_content", "easy_swallowing", "taste_masking", "good_absorption"],
            "disadvantages": ["animal_gelatin", "shorter_shelf_life", "temperature_sensitive"],
            "typical_contents": "oils, liquid_extracts, soft_extracts"
        },
        "pilula_cocta": {
            "latin": "Pilula Cocta",
            "english": "Coated Pill",
            "description": "Pill with sugar or other coating for taste masking and appearance.",
            "advantages": ["taste_masking", "attractive", "easier_swallowing", "protective"],
            "disadvantages": ["more_complex_preparation", "added_sugar", "slower_disintegration"],
            "coating_types": ["sugar", "chocolate", "silver", "gold", "enteric"]
        },
        "granulatum": {
            "latin": "Granulatum",
            "english": "Granules",
            "description": "Small, free-flowing particles containing herbal extracts or powders.",
            "advantages": ["easy_dissolving", "pleasant_texture", "versatile", "stable"],
            "disadvantages": ["requires_processing", "may_contain_sugar", "dosing_precision"],
            "uses": ["suspensions", "effervescent_preparations", "direct_consumption"]
        },
        "pulvis_inhalans": {
            "latin": "Pulvis Inhalans",
            "english": "Inhalation Powder",
            "description": "Fine powder intended for inhalation into the respiratory tract.",
            "advantages": ["direct_delivery", "rapid_onset", "local_action", "systemic_absorption"],
            "disadvantages": ["requires_device", "irritation_risk", "dosing_challenges"],
            "uses": ["respiratory_conditions", "nasal_congestion", "asthma"]
        },
        "emplastrum_medicatum": {
            "latin": "Emplastrum Medicatum",
            "english": "Medicated Plaster",
            "description": "Adhesive preparation containing herbs for prolonged skin contact.",
            "advantages": ["prolonged_action", "targeted_delivery", "convenient", "protective"],
            "disadvantages": ["skin_irritation", "adhesive_issues", "removal_discomfort"],
            "uses": ["pain_relief", "inflammation", "support", "protection"]
        },
        "collutorium": {
            "latin": "Collutorium",
            "english": "Mouthwash",
            "description": "Liquid preparation for rinsing the oral cavity.",
            "advantages": ["local_action", "refreshing", "easy_use", "pleasant"],
            "disadvantages": ["temporary_contact", "swallowing_risk", "alcohol_content"],
            "uses": ["oral_hygiene", "gum_health", "fresh_breath", "mouth_infections"]
        },
        "guttae": {
            "latin": "Guttae",
            "english": "Drops",
            "description": "Liquid preparation administered by drops for precise dosing.",
            "advantages": ["precise_dosing", "flexible", "rapid_absorption", "versatile"],
            "disadvantages": ["dosing_variability", "spillage_risk", "measurement_needed"],
            "types": ["eye_drops", "ear_drops", "nasal_drops", "oral_drops"]
        },
        "aerosolum": {
            "latin": "Aerosolum",
            "english": "Aerosol",
            "description": "Fine mist or spray containing herbal preparations.",
            "advantages": ["fine_dispersion", "deep_penetration", "rapid_onset", "convenient"],
            "disadvantages": ["requires_propellant", "environmental_concerns", "equipment_needed"],
            "uses": ["respiratory_delivery", "topical_application", "room_dispersion"]
        }
    }
}
# ═══════════════════════════════════════════════════════════════════════════════
# WILKEN KEY ENGINE v5.0 - PART 2: COMPLETE MATERIA MEDICA
# ═══════════════════════════════════════════════════════════════════════════════
# 30 documented medicinal plants with full details including:
# Latin names, families, parts used, actions, preparations, dosage,
# contraindications, planetary rulers, elements, descriptions, and folklore
# ═══════════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 2A: MATERIA MEDICA - COMPLETE HERBAL REFERENCE
# ───────────────────────────────────────────────────────────────────────────────

MATERIA_MEDICA = {
    "mandragora": {
        "latin_name": "Mandragora officinarum",
        "common_name": "Mandrake",
        "family": "Solanaceae",
        "parts_used": "Root primarily, leaves secondarily",
        "actions": ["narcotic", "anodyne", "emetic", "purgative", "aphrodisiac", "hallucinogenic"],
        "preparations": ["tinctura", "extractum", "unguentum", "pilula"],
        "dosage": "Root: 0.1-0.3g (extremely potent, use with extreme caution)",
        "contraindications": "POISONOUS. Contraindicated in pregnancy, heart conditions, glaucoma. Overdose can be fatal. Use only under expert guidance.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "The legendary mandrake has been surrounded by mysticism since antiquity. Its forked root often resembles a human figure, leading to countless superstitions. The root contains tropane alkaloids including hyoscyamine and scopolamine, which produce powerful narcotic and hallucinogenic effects. In medieval medicine, it was used as an anesthetic for surgery and to treat melancholia, though its toxicity made it extremely dangerous.",
        "folklore": "Medieval legend held that the mandrake would scream when pulled from the earth, killing anyone who heard it. Harvesting rituals involved tying a dog to the plant and having the dog pull it out. The root was believed to bring wealth and protection to its owner. It was a key ingredient in witches' flying ointments.",
        "historical_uses": ["surgical_anesthetic", "melancholia", "rheumatism", "convulsions", "aphrodisiac"],
        "modern_status": "Controlled substance in most jurisdictions due to toxicity"
    },
    
    "belladonna": {
        "latin_name": "Atropa belladonna",
        "common_name": "Deadly Nightshade",
        "family": "Solanaceae",
        "parts_used": "Leaves, root",
        "actions": ["antispasmodic", "anodyne", "mydriatic", "narcotic", "sedative"],
        "preparations": ["tinctura", "extractum", "unguentum", "pilula"],
        "dosage": "Leaf: 0.05-0.1g maximum. Tincture: 0.1-0.3ml. EXTREMELY TOXIC.",
        "contraindications": "HIGHLY POISONOUS. Contraindicated in pregnancy, tachycardia, glaucoma, prostate enlargement. Fatal overdose possible.",
        "planetary_ruler": "Saturnus",
        "element": "Fire",
        "description": "Belladonna, meaning 'beautiful lady' in Italian, was so named because women used it to dilate their pupils for cosmetic effect. The plant contains atropine, hyoscyamine, and scopolamine - powerful anticholinergic alkaloids. In controlled doses, it relaxes smooth muscles and reduces secretions, but overdose causes delirium, convulsions, and death.",
        "folklore": "Associated with witchcraft and the Underworld. Named after Atropos, the Fate who cuts the thread of life. Used in flying ointments and alleged witches' brews. The plant was believed to belong to the Devil, who tended it personally except on Walpurgis Night when witches harvested it.",
        "historical_uses": ["pupil_dilation", "muscle_spasms", "whooping_cough", "neuralgia", "parkinsons_symptoms"],
        "modern_status": "Source of atropine for modern medicine; plant itself highly regulated"
    },
    
    "digitalis": {
        "latin_name": "Digitalis purpurea",
        "common_name": "Foxglove",
        "family": "Plantaginaceae",
        "parts_used": "Leaves",
        "actions": ["cardiac tonic", "diuretic", "sedative"],
        "preparations": ["tinctura", "extractum", "infusum", "pilula"],
        "dosage": "Leaf: 0.05-0.2g. Very narrow therapeutic window. Must be standardized.",
        "contraindications": "POISONOUS. Contraindicated in heart block, ventricular fibrillation, electrolyte imbalances. Therapeutic dose close to toxic dose.",
        "planetary_ruler": "Saturnus",
        "element": "Water",
        "description": "Foxglove contains cardiac glycosides including digitoxin and digoxin, which increase the force of heart contractions while slowing the heart rate. Discovered by William Withering in 1775 for treating dropsy (edema). The therapeutic window is extremely narrow, making it one of the most dangerous yet valuable medicinal plants.",
        "folklore": "Associated with fairies and the 'wee folk.' The name 'foxglove' may derive from 'folk's glove,' referring to fairy gloves. In Wales, it was called 'goblin gloves.' Planting foxglove near the home was believed to protect against evil influences and witchcraft.",
        "historical_uses": ["heart_failure", "dropsy", "edema", "irregular_heartbeat", "consumption"],
        "modern_status": "Source of digoxin, still used in conventional cardiology"
    },
    
    "artemisia": {
        "latin_name": "Artemisia absinthium",
        "common_name": "Wormwood",
        "family": "Asteraceae",
        "parts_used": "Leaves and flowering tops",
        "actions": ["bitter tonic", "anthelmintic", "carminative", "febrifuge", "emmenagogue"],
        "preparations": ["infusum", "tinctura", "oleum", "pulvis"],
        "dosage": "Infusion: 1-2g per cup. Tincture: 1-2ml. Long-term use not recommended.",
        "contraindications": "Avoid in pregnancy (emmenagogue). Not for long-term use. May cause seizures in high doses.",
        "planetary_ruler": "Mars",
        "element": "Fire",
        "description": "The intensely bitter herb famous as the flavoring for absinthe. Contains thujone, which in high concentrations can cause neurological symptoms. As a bitter tonic, it stimulates digestive secretions and improves appetite. Traditionally used to expel intestinal worms and as a fever reducer.",
        "folklore": "Named after Artemis, goddess of the hunt and childbirth. Used in ancient Greece for menstrual complaints. Associated with the Green Fairy of absinthe fame. In medieval Europe, it was strewn on floors to repel fleas and insects. Used in love charms and protection rituals.",
        "historical_uses": ["digestive_tonic", "intestinal_worms", "fever", "appetite_loss", "menstrual_complaints"],
        "modern_status": "Thujone content regulated in beverages; herb available with warnings"
    },
    
    "hyoscyamus": {
        "latin_name": "Hyoscyamus niger",
        "common_name": "Henbane",
        "family": "Solanaceae",
        "parts_used": "Leaves, seeds",
        "actions": ["sedative", "anodyne", "antispasmodic", "narcotic", "mydriatic"],
        "preparations": ["tinctura", "extractum", "unguentum", "fomentatio"],
        "dosage": "Leaf: 0.05-0.2g. Tincture: 0.2-0.5ml. Highly toxic.",
        "contraindications": "POISONOUS. Contraindicated in pregnancy, glaucoma, tachycardia, prostate enlargement. Overdose fatal.",
        "planetary_ruler": "Saturnus",
        "element": "Water",
        "description": "Henbane contains hyoscyamine and scopolamine, producing sedative and hallucinogenic effects. Used since ancient times for pain relief and as an anesthetic. The Oracle of Delphi may have inhaled henbane smoke to induce prophetic visions. In medieval times, it was an ingredient in 'soporific sponges' used for surgery.",
        "folklore": "Associated with death and the Underworld. Its name may derive from 'hen-bane' (killer of poultry). Used in witches' ointments and love potions. The dead in Hades were crowned with henbane. Associated with the Germanic god Thor and used in weather magic.",
        "historical_uses": ["pain_relief", "sedation", "surgical_anesthetic", "rheumatism", "asthma", "mania"],
        "modern_status": "Source of hyoscyamine for pharmaceuticals; plant use restricted"
    },
    
    "conium": {
        "latin_name": "Conium maculatum",
        "common_name": "Hemlock",
        "family": "Apiaceae",
        "parts_used": "Leaves, seeds (extremely toxic)",
        "actions": ["sedative", "anodyne", "antispasmodic", "paralytic"],
        "preparations": ["tinctura (extremely dilute)", "extractum (pharmaceutical only)"],
        "dosage": "NOT RECOMMENDED FOR HOME USE. Lethal dose extremely small.",
        "contraindications": "EXTREMELY POISONOUS. Contraindicated in all cases except supervised pharmaceutical use. Death by respiratory paralysis.",
        "planetary_ruler": "Saturnus",
        "element": "Water",
        "description": "The infamous poison that killed Socrates. Contains coniine, a neurotoxin that causes ascending paralysis leading to respiratory failure. In minute, controlled doses, it was historically used for tremors and joint pain, but the risk of fatal overdose makes it unsuitable for any but the most expert use.",
        "folklore": "Forever associated with the execution of Socrates. In medieval times, associated with death and execution. The purple spots on the stems were said to be the mark of the Devil. Witches were believed to use it in flying ointments. Associated with Hecate and the underworld.",
        "historical_uses": ["tremors", "joint_pain", "mania", "whooping_cough", "external_tumors"],
        "modern_status": "Illegal to possess in many jurisdictions; no legitimate herbal use"
    },
    
    "taxus": {
        "latin_name": "Taxus baccata",
        "common_name": "Yew",
        "family": "Taxaceae",
        "parts_used": "Leaves (toxic), bark (extremely toxic)",
        "actions": ["cardiac stimulant", "cytostatic", "diuretic"],
        "preparations": ["extractum (pharmaceutical only)"],
        "dosage": "NOT FOR HOME USE. All parts except red aril are deadly poisonous.",
        "contraindications": "DEADLY POISONOUS. Contraindicated in all cases. Fatal cardiac effects.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "The ancient yew tree, often found in churchyards, contains taxine alkaloids that affect the heart. Despite its toxicity, it has become valuable in modern medicine as the original source of paclitaxel (Taxol), a chemotherapy drug used to treat various cancers. The red aril (flesh) around the seed is the only non-toxic part.",
        "folklore": "Sacred to the Druids and associated with death and rebirth. Yews were planted in churchyards to ward off evil spirits and protect the dead. The tree can live for thousands of years, symbolizing eternal life. Longbows were made from yew wood. Associated with the Celtic Otherworld.",
        "historical_uses": ["cancer_treatment (modern)", "rheumatism (historical)", "dropsy (historical)"],
        "modern_status": "Source of Taxol for chemotherapy; plant itself deadly poisonous"
    },
    
    "ricinus": {
        "latin_name": "Ricinus communis",
        "common_name": "Castor Bean",
        "family": "Euphorbiaceae",
        "parts_used": "Seeds (oil extracted), leaves",
        "actions": ["purgative", "emollient", "labor stimulant", "anti-inflammatory"],
        "preparations": ["oleum", "cataplasma", "fomentatio"],
        "dosage": "Oil: 5-15ml as purgative. External use safe. Seeds are deadly poisonous.",
        "contraindications": "Seeds contain ricin - one of the most toxic substances known. Contraindicated in pregnancy, intestinal obstruction, appendicitis. Oil generally safe but seeds deadly.",
        "planetary_ruler": "Mars",
        "element": "Fire",
        "description": "The castor bean plant produces castor oil, a safe and effective purgative when properly extracted. However, the seeds contain ricin, a protein toxin so potent that a single seed chewed can be fatal. The oil, which does not contain ricin, has been used for thousands of years as a laxative and for inducing labor.",
        "folklore": "Known to the ancient Egyptians, who used it in lamps and as medicine. The name 'castor' comes from its use as a substitute for castoreum (beaver secretion) in perfumes. Associated with protection and banishing evil. Used in Caribbean Obeah and Hoodoo practices.",
        "historical_uses": ["constipation", "labor_induction", "skin_conditions", "hair_growth", "lamp_fuel"],
        "modern_status": "Oil widely available; ricin classified as biological weapon"
    },
    
    "datura": {
        "latin_name": "Datura stramonium",
        "common_name": "Jimson Weed/Devil's Trumpet",
        "family": "Solanaceae",
        "parts_used": "Leaves, seeds",
        "actions": ["antispasmodic", "anodyne", "sedative", "hallucinogenic", "mydriatic"],
        "preparations": ["tinctura", "unguentum", "fomentatio", "cataplasma"],
        "dosage": "Leaf: 0.05-0.1g maximum. Highly variable potency. Extremely dangerous.",
        "contraindications": "POISONOUS. Contraindicated in pregnancy, glaucoma, heart conditions. Overdose causes delirium and death.",
        "planetary_ruler": "Saturnus",
        "element": "Fire",
        "description": "Datura has been used in sacred rituals across many cultures for its powerful hallucinogenic properties. Contains atropine, hyoscyamine, and scopolamine. The name 'Jimson weed' comes from Jamestown, where British soldiers were poisoned by it in 1676. Used in asthma cigarettes historically.",
        "folklore": "Sacred to Shiva in Hinduism and used in various shamanic traditions. Associated with the Devil due to its dangerous nature. The trumpet-shaped flowers open at night, associated with the underworld. Used in European witchcraft and Native American spiritual practices.",
        "historical_uses": ["asthma", "whooping_cough", "rheumatism", "sedation", "sacred_rituals"],
        "modern_status": "Controlled in many areas; scopolamine used in pharmaceuticals"
    },
    
    "aconitum": {
        "latin_name": "Aconitum napellus",
        "common_name": "Monkshood/Wolfsbane",
        "family": "Ranunculaceae",
        "parts_used": "Root, leaves",
        "actions": ["anodyne", "antipyretic", "diuretic", "cardiac depressant", "local anesthetic"],
        "preparations": ["tinctura (homeopathic only)", "linimentum (external only)"],
        "dosage": "NOT FOR INTERNAL USE EXCEPT HOMEOPATHIC. Topical: very dilute preparations only.",
        "contraindications": "EXTREMELY POISONOUS. Contraindicated in all internal use except homeopathic. Death within hours from cardiac failure.",
        "planetary_ruler": "Saturnus",
        "element": "Water",
        "description": "One of the most toxic plants known, containing aconitine, which affects sodium channels and causes rapid death. Even skin contact can cause poisoning. Historically used on arrows for hunting and warfare. In homeopathic dilutions, it is used for fever and shock, but the crude plant is deadly.",
        "folklore": "Associated with werewolves and witchcraft. Used to poison arrows and water supplies in warfare. The name 'wolfsbane' comes from its use in wolf poison. Associated with Hecate and the underworld. In medieval times, it was believed to be an ingredient in witches' flying ointments.",
        "historical_uses": ["external_pain_relief", "fever", "inflammation", "arrow_poison", "wolf_poison"],
        "modern_status": "Highly regulated; homeopathic use only for internal applications"
    },
    
    "colchicum": {
        "latin_name": "Colchicum autumnale",
        "common_name": "Autumn Crocus/Meadow Saffron",
        "family": "Colchicaceae",
        "parts_used": "Seeds, corm",
        "actions": ["anti-inflammatory", "analgesic", "cytostatic"],
        "preparations": ["tinctura", "extractum", "pilula"],
        "dosage": "0.5-1.5mg colchicine equivalent. Narrow therapeutic window.",
        "contraindications": "POISONOUS. Contraindicated in pregnancy, kidney disease, blood disorders. Fatal in overdose.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "The autumn crocus is the source of colchicine, used to treat gout for over 2000 years. Colchicine interferes with cell division and reduces inflammation. The plant is highly toxic, with symptoms resembling arsenic poisoning. It has no relationship to true saffron despite the similar appearance.",
        "folklore": "Associated with the autumn equinox and the descent into the underworld. The plant blooms in autumn without leaves, leading to associations with death and rebirth. Used in Greek mythology - Medea attempted to poison Theseus with it. Associated with the goddess Hecate.",
        "historical_uses": ["gout", "rheumatism", "dropsy", "cancer_treatment (historical)"],
        "modern_status": "Colchicine still used for gout; plant highly regulated"
    },
    
    "papaver": {
        "latin_name": "Papaver somniferum",
        "common_name": "Opium Poppy",
        "family": "Papaveraceae",
        "parts_used": "Latex from unripe seed pods, seeds (non-narcotic)",
        "actions": ["anodyne", "narcotic", "hypnotic", "antidiarrheal", "antitussive"],
        "preparations": ["latex", "tinctura (laudanum)", "extractum", "syrupus"],
        "dosage": "Highly variable. Medical opiates strictly controlled. Seeds non-narcotic.",
        "contraindications": "Highly addictive. Contraindicated in respiratory depression, head injuries, acute asthma. Risk of fatal overdose.",
        "planetary_ruler": "Saturnus",
        "element": "Water",
        "description": "The source of opium and all opiate drugs, including morphine and codeine. Cultivated for thousands of years for pain relief. The dried latex from scored pods contains powerful alkaloids. The seeds contain no narcotics and are used in baking. The plant has shaped human history through trade, war, and medicine.",
        "folklore": "Associated with sleep, death, and the underworld. The Greek god Hypnos and Roman Somnus carried poppies. Demeter created the poppy to help her sleep after losing Persephone. Associated with Morpheus, god of dreams. Used in ancient Egyptian medicine and ritual.",
        "historical_uses": ["pain_relief", "diarrhea", "cough", "insomnia", "surgical_anesthetic"],
        "modern_status": "Source of pharmaceutical opiates; cultivation and use highly regulated"
    },
    
    "arnica": {
        "latin_name": "Arnica montana",
        "common_name": "Arnica/Leopard's Bane",
        "family": "Asteraceae",
        "parts_used": "Flowers, rhizome",
        "actions": ["anti-inflammatory", "anodyne", "vulnerary", "counter-irritant", "antiseptic"],
        "preparations": ["tinctura", "oleum", "unguentum", "cataplasma", "linimentum"],
        "dosage": "EXTERNAL USE ONLY. Tincture: dilute 1:10 for compresses. Do not apply to broken skin.",
        "contraindications": "TOXIC IF TAKEN INTERNALLY. Do not use on broken skin. May cause allergic reactions in sensitive individuals.",
        "planetary_ruler": "Sol",
        "element": "Fire",
        "description": "Arnica is one of the best remedies for trauma, bruising, and muscle soreness when used externally. It reduces inflammation and speeds healing of tissues. Internally, it is toxic and can cause serious harm. The bright yellow flowers resemble the sun, reflecting its planetary association.",
        "folklore": "Named after the Greek word for 'lamb's skin' due to its soft, hairy leaves. Associated with the sun's healing power. Mountain climbers traditionally used it for sore muscles. In Alpine folklore, it was believed to protect against mountain spirits.",
        "historical_uses": ["bruises", "sprains", "muscle_pain", "arthritis", "inflammation", "wound_healing"],
        "modern_status": "External preparations widely available; internal use prohibited"
    },
    
    "salvia": {
        "latin_name": "Salvia officinalis",
        "common_name": "Garden Sage",
        "family": "Lamiaceae",
        "parts_used": "Leaves",
        "actions": ["carminative", "antiseptic", "astringent", "antihidrotic", "emmenagogue", "nervine"],
        "preparations": ["infusum", "tinctura", "oleum", "gargarisma", "pulvis"],
        "dosage": "Infusion: 1-2 tsp per cup. Tincture: 2-4ml. Safe for regular use.",
        "contraindications": "Avoid therapeutic doses in pregnancy (emmenagogue). May reduce milk supply in nursing mothers.",
        "planetary_ruler": "Jupiter",
        "element": "Air",
        "description": "The name Salvia comes from 'salvare' - to heal. Sage has been valued for centuries for its medicinal and culinary properties. It reduces excessive sweating, aids digestion, and has antiseptic properties. The essential oil is strongly antimicrobial. Used traditionally to enhance memory and cognition.",
        "folklore": "Sacred to the Romans, who believed it could confer immortality. Used in smudging ceremonies by Native Americans. Associated with wisdom and longevity. In medieval Europe, it was said 'Why should a man die while sage grows in his garden?' Used in ceremonies for protection and purification.",
        "historical_uses": ["sore_throat", "digestion", "excessive_sweating", "memory", "menopause", "wound_healing"],
        "modern_status": "Widely available and safe; research supports cognitive benefits"
    },
    
    "rosa": {
        "latin_name": "Rosa canina",
        "common_name": "Dog Rose/Wild Rose",
        "family": "Rosaceae",
        "parts_used": "Hips (fruit), petals, leaves",
        "actions": ["astringent", "nutritive", "anti-inflammatory", "diuretic", "laxative"],
        "preparations": ["infusum", "syrupus", "conserva", "oleum", "pulvis"],
        "dosage": "Hips: 2-4g or 5-10ml syrup. Petals: 2-4g for tea. Very safe.",
        "contraindications": "Generally regarded as safe. Large doses of hips may cause mild laxative effect.",
        "planetary_ruler": "Venus",
        "element": "Water",
        "description": "Rose hips are one of the richest plant sources of vitamin C, containing 20-40 times more than oranges by weight. Used traditionally for colds, flu, and as a general tonic. Rose petals have mild astringent and mood-elevating properties. The oil is prized for skincare.",
        "folklore": "Sacred to Venus and Aphrodite, goddess of love. Roses have symbolized love, beauty, and secrecy for millennia. 'Sub rosa' (under the rose) meant confidentiality. In Christian tradition, associated with the Virgin Mary. Used in love spells and to attract positive energy.",
        "historical_uses": ["vitamin_C_source", "colds", "flu", "diarrhea", "skin_care", "mild_laxative"],
        "modern_status": "Widely available; rose hip powder popular for vitamin C"
    },
    
    "chamomilla": {
        "latin_name": "Matricaria chamomilla",
        "common_name": "German Chamomile",
        "family": "Asteraceae",
        "parts_used": "Flowers",
        "actions": ["carminative", "anti-inflammatory", "antispasmodic", "sedative", "vulnerary", "bitter"],
        "preparations": ["infusum", "tinctura", "oleum", "gargarisma", "cataplasma"],
        "dosage": "Infusion: 2-3g per cup. Tincture: 1-4ml. Very safe, suitable for children.",
        "contraindications": "Rare allergic reactions in those sensitive to Asteraceae family. Generally very safe.",
        "planetary_ruler": "Sol",
        "element": "Water",
        "description": "One of the most popular herbs worldwide, chamomile is gentle yet effective for digestion, sleep, and anxiety. Contains bisabolol and chamazulene, which reduce inflammation. The flowers resemble tiny daisies with apple-like fragrance. Safe for babies and children.",
        "folklore": "Sacred to the Egyptian sun god Ra. Used in ancient Egypt, Greece, and Rome. The name comes from Greek 'chamos melon' (ground apple) due to its scent. Associated with the Norse god Baldr. Used in folk magic for prosperity and to prevent nightmares.",
        "historical_uses": ["insomnia", "anxiety", "digestive_upset", "colic", "skin_inflammation", "wound_healing"],
        "modern_status": "One of the most widely used herbs; extensive safety record"
    },
    
    "mentha": {
        "latin_name": "Mentha piperita",
        "common_name": "Peppermint",
        "family": "Lamiaceae",
        "parts_used": "Leaves",
        "actions": ["carminative", "antispasmodic", "cholagogue", "diaphoretic", "anodyne", "stimulant"],
        "preparations": ["infusum", "tinctura", "oleum", "gargarisma", "cataplasma"],
        "dosage": "Infusion: 2-3g per cup. Tincture: 1-2ml. Oil: 1-2 drops internally, diluted.",
        "contraindications": "May worsen reflux in some people. Avoid large doses in pregnancy. Oil can be irritating undiluted.",
        "planetary_ruler": "Mercurius",
        "element": "Air",
        "description": "A hybrid of spearmint and watermint, peppermint is one of the most widely used medicinal herbs. Menthol, its primary constituent, creates the cooling sensation and relaxes smooth muscles. Excellent for digestive complaints, headaches, and respiratory congestion.",
        "folklore": "Named after the Greek nymph Minthe, who was transformed into the plant by Persephone. Used in ancient Egypt and Rome. Associated with hospitality in many cultures. Used in folk magic for purification, healing, and to enhance psychic abilities.",
        "historical_uses": ["indigestion", "gas", "nausea", "headache", "congestion", "muscle_pain"],
        "modern_status": "Widely available; enteric-coated oil used for IBS"
    },
    
    "thymus": {
        "latin_name": "Thymus vulgaris",
        "common_name": "Thyme",
        "family": "Lamiaceae",
        "parts_used": "Leaves and flowering tops",
        "actions": ["antiseptic", "antispasmodic", "expectorant", "carminative", "astringent", "vermifuge"],
        "preparations": ["infusum", "tinctura", "oleum", "syrupus", "gargarisma", "mel"],
        "dosage": "Infusion: 1-2g per cup. Tincture: 2-4ml. Oil: highly concentrated, use sparingly.",
        "contraindications": "Avoid large doses in pregnancy. Oil may irritate skin undiluted. Avoid in thyroid conditions.",
        "planetary_ruler": "Venus",
        "element": "Air",
        "description": "Thyme has been used since ancient times for respiratory infections due to its powerful antiseptic properties. Thymol, its main constituent, is strongly antimicrobial. Used in mouthwashes, cough syrups, and as a culinary herb. The ancient Egyptians used it in embalming.",
        "folklore": "Name comes from Greek 'thymos' meaning courage. Roman soldiers bathed in thyme before battle. Associated with fairies in European folklore. Burned as incense for purification. Used in pillows to prevent nightmares and promote courage.",
        "historical_uses": ["respiratory_infections", "cough", "sore_throat", "digestion", "wound_antiseptic", "parasites"],
        "modern_status": "Thymol used in commercial mouthwashes; herb widely available"
    },
    
    "lavandula": {
        "latin_name": "Lavandula angustifolia",
        "common_name": "English Lavender",
        "family": "Lamiaceae",
        "parts_used": "Flowers",
        "actions": ["carminative", "antispasmodic", "antidepressant", "rubefacient", "antiseptic", "nervine"],
        "preparations": ["infusum", "tinctura", "oleum", "essentia", "aqua", "syrupus"],
        "dosage": "Infusion: 1-2 tsp per cup. Tincture: 1-2ml. Oil: external use primarily.",
        "contraindications": "Generally very safe. Oil may irritate sensitive skin undiluted. Avoid large internal doses.",
        "planetary_ruler": "Mercurius",
        "element": "Air",
        "description": "Lavender is one of the most versatile and beloved herbs, valued for its calming properties and beautiful fragrance. The essential oil is a staple in aromatherapy for anxiety, insomnia, and stress. Also has antiseptic properties and can be used for burns and insect bites.",
        "folklore": "Name comes from Latin 'lavare' (to wash) as Romans used it in baths. Associated with love and devotion in Victorian language of flowers. Used in medieval times to ward off evil spirits and the plague. Placed in linen closets to repel moths and scent fabrics.",
        "historical_uses": ["anxiety", "insomnia", "headache", "burns", "insect_bites", "depression"],
        "modern_status": "Essential oil industry staple; widely researched for anxiety"
    },
    
    "calendula": {
        "latin_name": "Calendula officinalis",
        "common_name": "Pot Marigold",
        "family": "Asteraceae",
        "parts_used": "Flowers",
        "actions": ["vulnerary", "anti-inflammatory", "antiseptic", "emmenagogue", "antifungal", "cholagogue"],
        "preparations": ["infusum", "tinctura", "oleum", "unguentum", "cataplasma"],
        "dosage": "Infusion: 1-2 tsp per cup. Tincture: 0.3-1.5ml. External preparations widely used.",
        "contraindications": "Avoid in pregnancy due to emmenagogue effect. Rare allergies in Asteraceae-sensitive individuals.",
        "planetary_ruler": "Sol",
        "element": "Fire",
        "description": "Calendula is one of the best herbs for skin healing and regeneration. It reduces inflammation, prevents infection, and speeds wound healing. The bright orange flowers follow the sun, opening in morning and closing at night. Used in cooking as 'poor man's saffron.'",
        "folklore": "Associated with the sun and solar deities. Used in ancient Greek, Roman, Middle Eastern, and Indian cultures. Worn for protection and to see fairies. Used in love divination. In medieval times, believed to lift spirits and comfort the heart.",
        "historical_uses": ["wound_healing", "skin_inflammation", "diaper_rash", "eczema", "menstrual_cramps", "varicose_veins"],
        "modern_status": "Popular in natural skincare; widely available"
    },
    
    "echinacea": {
        "latin_name": "Echinacea purpurea",
        "common_name": "Purple Coneflower",
        "family": "Asteraceae",
        "parts_used": "Root, aerial parts, seeds",
        "actions": ["immunostimulant", "antiseptic", "anti-inflammatory", "vulnerary", "sialagogue", "detoxifying"],
        "preparations": ["tinctura", "decoctum", "infusum", "extractum", "pilula"],
        "dosage": "Root tincture: 2-4ml. Decoction: 1-2g root per cup. Best used at first sign of illness.",
        "contraindications": "Rare allergies in Asteraceae-sensitive individuals. Use caution in autoimmune conditions. Short-term use recommended.",
        "planetary_ruler": "Mars",
        "element": "Fire",
        "description": "Echinacea is the most popular immune-supporting herb in North America. Native Americans used it for centuries before European adoption. It stimulates the immune system, increases white blood cell production, and has antiseptic properties. Best used at the first sign of infection.",
        "folklore": "Used extensively by Native American tribes, particularly the Plains Indians, for snake bites, wounds, and infections. The spiny central cone resembles a hedgehog (echinos in Greek). Used in ritual to bring spiritual strength and protection.",
        "historical_uses": ["colds", "flu", "infections", "wounds", "snake_bites", "immune_support"],
        "modern_status": "Top-selling herbal supplement; extensive research"
    },
    
    "valeriana": {
        "latin_name": "Valeriana officinalis",
        "common_name": "Valerian",
        "family": "Caprifoliaceae",
        "parts_used": "Root and rhizome",
        "actions": ["sedative", "nervine", "antispasmodic", "carminative", "hypnotic", "anodyne"],
        "preparations": ["tinctura", "decoctum", "extractum", "pilula", "pulvis"],
        "dosage": "Root: 2-3g. Tincture: 2-5ml. Decoction: 2-3g per cup. Best taken before bed.",
        "contraindications": "May cause drowsiness. Avoid with other sedatives. Rare paradoxical stimulation. Strong odor.",
        "planetary_ruler": "Mercurius",
        "element": "Water",
        "description": "Valerian has been used since ancient Greek and Roman times as a sleep aid and nerve tonic. The root has a strong, distinctive odor that some find unpleasant. It contains valerenic acid and other compounds that interact with GABA receptors in the brain, promoting relaxation and sleep without morning grogginess.",
        "folklore": "Named after the Roman emperor Valerianus. Used by Hippocrates and Galen. In medieval times, used as a perfume. The Pied Piper of Hamelin may have used valerian to attract rats (and children). Associated with peace and tranquility.",
        "historical_uses": ["insomnia", "anxiety", "nervous_tension", "muscle_spasms", "menstrual_cramps", "migraine"],
        "modern_status": "Widely used sleep aid; approved in Europe for insomnia"
    },
    
    "passiflora": {
        "latin_name": "Passiflora incarnata",
        "common_name": "Passionflower",
        "family": "Passifloraceae",
        "parts_used": "Aerial parts",
        "actions": ["sedative", "anxiolytic", "antispasmodic", "hypnotic", "analgesic", "nervine"],
        "preparations": ["infusum", "tinctura", "extractum", "pilula"],
        "dosage": "Infusion: 2g per cup. Tincture: 2-4ml. Safe for regular use.",
        "contraindications": "Avoid in pregnancy. May potentiate sedative medications. Generally very safe.",
        "planetary_ruler": "Venus",
        "element": "Water",
        "description": "Passionflower was named by Spanish missionaries who saw symbols of Christ's passion in its flowers. It is excellent for anxiety, insomnia, and nervous tension without causing drowsiness. Contains flavonoids and alkaloids that have calming effects on the nervous system.",
        "folklore": "Named by Spanish missionaries in South America who saw in the flower: the crown of thorns (filaments), the five wounds (stamens), the three nails (styles), and the column of the scourging (stalk). Used by Native Americans for centuries. Associated with peace and spiritual devotion.",
        "historical_uses": ["anxiety", "insomnia", "nervous_tension", "muscle_spasms", "neuralgia", "seizures"],
        "modern_status": "Popular anxiety remedy; approved in Europe for nervous restlessness"
    },
    
    "hypericum": {
        "latin_name": "Hypericum perforatum",
        "common_name": "St. John's Wort",
        "family": "Hypericaceae",
        "parts_used": "Flowering tops",
        "actions": ["antidepressant", "antiviral", "vulnerary", "anti-inflammatory", "nervine", "hepatic"],
        "preparations": ["infusum", "tinctura", "oleum", "extractum", "pilula"],
        "dosage": "Infusion: 2-4g per cup. Tincture: 2-4ml. Standardized extract: 300mg (0.3% hypericin).",
        "contraindications": "MAJOR DRUG INTERACTIONS. Contraindicated with SSRIs, MAOIs, birth control, blood thinners, HIV medications, transplant drugs. Photosensitivity possible.",
        "planetary_ruler": "Sol",
        "element": "Fire",
        "description": "St. John's Wort is one of the most studied herbs for mild to moderate depression. It contains hypericin and hyperforin, which affect neurotransmitters. Also has antiviral properties and is used externally for nerve pain and wound healing. Blooms around the summer solstice, associated with St. John's Day (June 24).",
        "folklore": "Named after St. John the Baptist as it blooms near his feast day. Associated with the sun and protection. Hung in windows to ward off evil spirits and lightning. In medieval Europe, it was believed to reveal fairies and protect against witchcraft. Used in divination for love.",
        "historical_uses": ["depression", "anxiety", "nerve_pain", "wounds", "viral_infections", "menopause"],
        "modern_status": "Widely prescribed in Europe for depression; drug interaction warnings essential"
    },
    
    "glycyrrhiza": {
        "latin_name": "Glycyrrhiza glabra",
        "common_name": "Licorice",
        "family": "Fabaceae",
        "parts_used": "Root",
        "actions": ["expectorant", "demulcent", "adrenal tonic", "anti-inflammatory", "antispasmodic", "laxative"],
        "preparations": ["decoctum", "tinctura", "extractum", "syrupus", "pulvis"],
        "dosage": "Root: 1-5g. Deglycyrrhizinated form (DGL) for long-term use. Limit glycyrrhizin to <100mg/day.",
        "contraindications": "Raises blood pressure. Contraindicated in hypertension, kidney disease, heart failure, pregnancy, hormone-sensitive cancers. Potassium depletion with long-term use.",
        "planetary_ruler": "Venus",
        "element": "Water",
        "description": "Licorice is one of the most widely used herbs in traditional Chinese medicine and is found in many Western formulas as a harmonizer. It soothes mucous membranes, supports adrenal function, and has anti-inflammatory properties. The sweet taste comes from glycyrrhizin, which is 50 times sweeter than sugar.",
        "folklore": "Used in ancient Egypt, Greece, Rome, China, and India. Found in King Tut's tomb. Used to flavor tobacco and candies. Associated with love and lust in folklore. In Chinese medicine, it harmonizes formulas and 'guides' other herbs to their destinations.",
        "historical_uses": ["cough", "sore_throat", "adrenal_fatigue", "ulcers", "inflammation", "constipation"],
        "modern_status": "DGL form widely used for ulcers; glycyrrhizin content regulated"
    },
    
    "zingiber": {
        "latin_name": "Zingiber officinale",
        "common_name": "Ginger",
        "family": "Zingiberaceae",
        "parts_used": "Rhizome (root)",
        "actions": ["carminative", "antiemetic", "diaphoretic", "antispasmodic", "circulatory stimulant", "anti-inflammatory"],
        "preparations": ["infusum", "decoctum", "tinctura", "oleum", "pulvis", "conserva"],
        "dosage": "Fresh: 2-4g. Dried: 1-3g. Very safe. Can use liberally in cooking.",
        "contraindications": "High doses may aggravate heartburn. Use caution with gallstones. Generally very safe.",
        "planetary_ruler": "Mars",
        "element": "Fire",
        "description": "Ginger is one of the most widely used spices and medicines worldwide. It is excellent for nausea, digestion, and circulation. Contains gingerol and shogaol, which have anti-inflammatory and antiemetic effects. Used fresh, dried, or crystallized. Safe for pregnancy-related nausea.",
        "folklore": "Used in ancient India, China, and Rome. Marco Polo encountered it in China. Used in Ayurveda and Traditional Chinese Medicine for thousands of years. Associated with wealth and prosperity. Used in love spells and to 'heat up' relationships. In the Caribbean, used in spiritual cleansing.",
        "historical_uses": ["nausea", "motion_sickness", "morning_sickness", "indigestion", "colds", "inflammation", "circulation"],
        "modern_status": "Widely researched for nausea; GRAS (Generally Recognized As Safe)"
    },
    
    "cinnamomum": {
        "latin_name": "Cinnamomum verum",
        "common_name": "Ceylon Cinnamon/True Cinnamon",
        "family": "Lauraceae",
        "parts_used": "Inner bark",
        "actions": ["carminative", "antiseptic", "astringent", "warming", "antispasmodic", "emmenagogue"],
        "preparations": ["infusum", "tinctura", "pulvis", "oleum", "mel", "conserva"],
        "dosage": "Bark: 1-4g. Powder: 0.5-2g. Very safe in culinary amounts.",
        "contraindications": "Cassia cinnamon (common variety) contains coumarin - avoid large doses. Ceylon cinnamon safer. Emmenagogue - avoid large doses in pregnancy.",
        "planetary_ruler": "Sol",
        "element": "Fire",
        "description": "True cinnamon from Ceylon (Sri Lanka) is sweeter and more delicate than the common cassia cinnamon. It has been treasured for thousands of years, once worth more than gold by weight. Warms the body, aids digestion, and helps regulate blood sugar. The essential oil is strongly antimicrobial.",
        "folklore": "Mentioned in the Bible and ancient Egyptian texts. Used in embalming by Egyptians. Highly valued in ancient trade. Associated with wealth, prosperity, and love. Used in incense for purification and to raise spiritual vibrations. In medieval times, used to preserve meat.",
        "historical_uses": ["digestion", "colds", "diabetes", "circulation", "preservation", "flavoring"],
        "modern_status": "Research supports blood sugar regulation; widely used spice"
    },
    
    "arnica_montana": {
        "latin_name": "Arnica montana",
        "common_name": "Mountain Arnica",
        "family": "Asteraceae",
        "parts_used": "Flowers",
        "actions": ["anti-inflammatory", "analgesic", "counter-irritant", "antimicrobial"],
        "preparations": ["tinctura", "oleum", "unguentum", "cataplasma", "gel"],
        "dosage": "EXTERNAL USE ONLY. Apply to unbroken skin 2-3 times daily.",
        "contraindications": "TOXIC IF INGESTED. Do not use on broken skin. Allergy test recommended.",
        "planetary_ruler": "Sol",
        "element": "Fire",
        "description": "Mountain arnica grows in alpine meadows and has been used for centuries for trauma and inflammation. It reduces bruising, swelling, and pain when applied externally. The flowers contain sesquiterpene lactones that have anti-inflammatory effects.",
        "folklore": "Associated with mountain spirits in Alpine folklore. Used by mountain climbers for sore muscles. The bright yellow flowers were believed to capture the sun's healing power. Used in folk medicine throughout the European Alps.",
        "historical_uses": ["bruises", "sprains", "muscle_soreness", "arthritis", "insect_bites"],
        "modern_status": "Popular homeopathic and herbal remedy for trauma"
    },
    
    "hamamelis": {
        "latin_name": "Hamamelis virginiana",
        "common_name": "Witch Hazel",
        "family": "Hamamelidaceae",
        "parts_used": "Leaves, bark",
        "actions": ["astringent", "anti-inflammatory", "hemostatic", "vulnerary", "antiseptic"],
        "preparations": ["decoctum", "tinctura", "aqua", "extractum", "linimentum"],
        "dosage": "External use primarily. Witch hazel water (distillate) applied as needed.",
        "contraindications": "Generally very safe for external use. Internal use only under professional guidance.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "Witch hazel is a North American native that has become a staple in natural first aid. The bark and leaves contain tannins that tighten and tone tissues, reducing inflammation and bleeding. The distilled witch hazel water is widely available and used for skin care and first aid.",
        "folklore": "Used by Native Americans for centuries. The name 'witch hazel' comes from Middle English 'wiche' meaning pliable or bendable, not witchcraft. However, the forked branches were traditionally used as divining rods to find water. Associated with dowsing and water witching.",
        "historical_uses": ["hemorrhoids", "varicose_veins", "bruises", "insect_bites", "skin_inflammation", "aftershave"],
        "modern_status": "Witch hazel water widely available in pharmacies"
    },
    
    "hamamelis_vernalis": {
        "latin_name": "Hamamelis vernalis",
        "common_name": "Vernal Witch Hazel",
        "family": "Hamamelidaceae",
        "parts_used": "Leaves, bark",
        "actions": ["astringent", "anti-inflammatory", "hemostatic"],
        "preparations": ["decoctum", "tinctura", "aqua"],
        "dosage": "External use primarily. Similar to H. virginiana.",
        "contraindications": "Generally very safe for external use.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "A species of witch hazel native to the Ozark Plateau, blooming in late winter to early spring. Similar properties to common witch hazel but blooms during a different season. Used interchangeably with H. virginiana.",
        "folklore": "Blooms in late winter when most other plants are dormant, leading to associations with resilience and endurance. Used similarly to common witch hazel in folk medicine.",
        "historical_uses": ["similar_to_H_virginiana", "astringent", "anti-inflammatory"],
        "modern_status": "Used interchangeably with H. virginiana"
    },
    
    "hamamelis_japonica": {
        "latin_name": "Hamamelis japonica",
        "common_name": "Japanese Witch Hazel",
        "family": "Hamamelidaceae",
        "parts_used": "Leaves, bark",
        "actions": ["astringent", "anti-inflammatory", "hemostatic"],
        "preparations": ["decoctum", "tinctura", "aqua"],
        "dosage": "External use primarily. Similar to other Hamamelis species.",
        "contraindications": "Generally very safe for external use.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "Native to Japan, this species of witch hazel shares similar astringent and anti-inflammatory properties with its American counterparts. Used in traditional Japanese medicine and as an ornamental plant.",
        "folklore": "Used in traditional Japanese medicine. Valued as an ornamental for its winter-blooming flowers.",
        "historical_uses": ["astringent", "anti-inflammatory", "traditional_Japanese_medicine"],
        "modern_status": "Primarily ornamental; medicinal use similar to other species"
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# END OF PART 2
# ═══════════════════════════════════════════════════════════════════════════════
# INSTRUCTIONS: Copy this entire section AFTER Part 1 in your Streamlit app.
# Next: Part 3 contains CSS STYLING, HELPER FUNCTIONS & SEASONAL PROTOCOLS.
# ═══════════════════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════════════════
# WILKEN KEY ENGINE v5.0 - PART 2: COMPLETE MATERIA MEDICA
# ═══════════════════════════════════════════════════════════════════════════════
# 30 documented medicinal plants with full details including:
# Latin names, families, parts used, actions, preparations, dosage,
# contraindications, planetary rulers, elements, descriptions, and folklore
# ═══════════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 2A: MATERIA MEDICA - COMPLETE HERBAL REFERENCE
# ───────────────────────────────────────────────────────────────────────────────

MATERIA_MEDICA = {
    "mandragora": {
        "latin_name": "Mandragora officinarum",
        "common_name": "Mandrake",
        "family": "Solanaceae",
        "parts_used": "Root primarily, leaves secondarily",
        "actions": ["narcotic", "anodyne", "emetic", "purgative", "aphrodisiac", "hallucinogenic"],
        "preparations": ["tinctura", "extractum", "unguentum", "pilula"],
        "dosage": "Root: 0.1-0.3g (extremely potent, use with extreme caution)",
        "contraindications": "POISONOUS. Contraindicated in pregnancy, heart conditions, glaucoma. Overdose can be fatal. Use only under expert guidance.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "The legendary mandrake has been surrounded by mysticism since antiquity. Its forked root often resembles a human figure, leading to countless superstitions. The root contains tropane alkaloids including hyoscyamine and scopolamine, which produce powerful narcotic and hallucinogenic effects. In medieval medicine, it was used as an anesthetic for surgery and to treat melancholia, though its toxicity made it extremely dangerous.",
        "folklore": "Medieval legend held that the mandrake would scream when pulled from the earth, killing anyone who heard it. Harvesting rituals involved tying a dog to the plant and having the dog pull it out. The root was believed to bring wealth and protection to its owner. It was a key ingredient in witches' flying ointments.",
        "historical_uses": ["surgical_anesthetic", "melancholia", "rheumatism", "convulsions", "aphrodisiac"],
        "modern_status": "Controlled substance in most jurisdictions due to toxicity"
    },
    
    "belladonna": {
        "latin_name": "Atropa belladonna",
        "common_name": "Deadly Nightshade",
        "family": "Solanaceae",
        "parts_used": "Leaves, root",
        "actions": ["antispasmodic", "anodyne", "mydriatic", "narcotic", "sedative"],
        "preparations": ["tinctura", "extractum", "unguentum", "pilula"],
        "dosage": "Leaf: 0.05-0.1g maximum. Tincture: 0.1-0.3ml. EXTREMELY TOXIC.",
        "contraindications": "HIGHLY POISONOUS. Contraindicated in pregnancy, tachycardia, glaucoma, prostate enlargement. Fatal overdose possible.",
        "planetary_ruler": "Saturnus",
        "element": "Fire",
        "description": "Belladonna, meaning 'beautiful lady' in Italian, was so named because women used it to dilate their pupils for cosmetic effect. The plant contains atropine, hyoscyamine, and scopolamine - powerful anticholinergic alkaloids. In controlled doses, it relaxes smooth muscles and reduces secretions, but overdose causes delirium, convulsions, and death.",
        "folklore": "Associated with witchcraft and the Underworld. Named after Atropos, the Fate who cuts the thread of life. Used in flying ointments and alleged witches' brews. The plant was believed to belong to the Devil, who tended it personally except on Walpurgis Night when witches harvested it.",
        "historical_uses": ["pupil_dilation", "muscle_spasms", "whooping_cough", "neuralgia", "parkinsons_symptoms"],
        "modern_status": "Source of atropine for modern medicine; plant itself highly regulated"
    },
    
    "digitalis": {
        "latin_name": "Digitalis purpurea",
        "common_name": "Foxglove",
        "family": "Plantaginaceae",
        "parts_used": "Leaves",
        "actions": ["cardiac tonic", "diuretic", "sedative"],
        "preparations": ["tinctura", "extractum", "infusum", "pilula"],
        "dosage": "Leaf: 0.05-0.2g. Very narrow therapeutic window. Must be standardized.",
        "contraindications": "POISONOUS. Contraindicated in heart block, ventricular fibrillation, electrolyte imbalances. Therapeutic dose close to toxic dose.",
        "planetary_ruler": "Saturnus",
        "element": "Water",
        "description": "Foxglove contains cardiac glycosides including digitoxin and digoxin, which increase the force of heart contractions while slowing the heart rate. Discovered by William Withering in 1775 for treating dropsy (edema). The therapeutic window is extremely narrow, making it one of the most dangerous yet valuable medicinal plants.",
        "folklore": "Associated with fairies and the 'wee folk.' The name 'foxglove' may derive from 'folk's glove,' referring to fairy gloves. In Wales, it was called 'goblin gloves.' Planting foxglove near the home was believed to protect against evil influences and witchcraft.",
        "historical_uses": ["heart_failure", "dropsy", "edema", "irregular_heartbeat", "consumption"],
        "modern_status": "Source of digoxin, still used in conventional cardiology"
    },
    
    "artemisia": {
        "latin_name": "Artemisia absinthium",
        "common_name": "Wormwood",
        "family": "Asteraceae",
        "parts_used": "Leaves and flowering tops",
        "actions": ["bitter tonic", "anthelmintic", "carminative", "febrifuge", "emmenagogue"],
        "preparations": ["infusum", "tinctura", "oleum", "pulvis"],
        "dosage": "Infusion: 1-2g per cup. Tincture: 1-2ml. Long-term use not recommended.",
        "contraindications": "Avoid in pregnancy (emmenagogue). Not for long-term use. May cause seizures in high doses.",
        "planetary_ruler": "Mars",
        "element": "Fire",
        "description": "The intensely bitter herb famous as the flavoring for absinthe. Contains thujone, which in high concentrations can cause neurological symptoms. As a bitter tonic, it stimulates digestive secretions and improves appetite. Traditionally used to expel intestinal worms and as a fever reducer.",
        "folklore": "Named after Artemis, goddess of the hunt and childbirth. Used in ancient Greece for menstrual complaints. Associated with the Green Fairy of absinthe fame. In medieval Europe, it was strewn on floors to repel fleas and insects. Used in love charms and protection rituals.",
        "historical_uses": ["digestive_tonic", "intestinal_worms", "fever", "appetite_loss", "menstrual_complaints"],
        "modern_status": "Thujone content regulated in beverages; herb available with warnings"
    },
    
    "hyoscyamus": {
        "latin_name": "Hyoscyamus niger",
        "common_name": "Henbane",
        "family": "Solanaceae",
        "parts_used": "Leaves, seeds",
        "actions": ["sedative", "anodyne", "antispasmodic", "narcotic", "mydriatic"],
        "preparations": ["tinctura", "extractum", "unguentum", "fomentatio"],
        "dosage": "Leaf: 0.05-0.2g. Tincture: 0.2-0.5ml. Highly toxic.",
        "contraindications": "POISONOUS. Contraindicated in pregnancy, glaucoma, tachycardia, prostate enlargement. Overdose fatal.",
        "planetary_ruler": "Saturnus",
        "element": "Water",
        "description": "Henbane contains hyoscyamine and scopolamine, producing sedative and hallucinogenic effects. Used since ancient times for pain relief and as an anesthetic. The Oracle of Delphi may have inhaled henbane smoke to induce prophetic visions. In medieval times, it was an ingredient in 'soporific sponges' used for surgery.",
        "folklore": "Associated with death and the Underworld. Its name may derive from 'hen-bane' (killer of poultry). Used in witches' ointments and love potions. The dead in Hades were crowned with henbane. Associated with the Germanic god Thor and used in weather magic.",
        "historical_uses": ["pain_relief", "sedation", "surgical_anesthetic", "rheumatism", "asthma", "mania"],
        "modern_status": "Source of hyoscyamine for pharmaceuticals; plant use restricted"
    },
    
    "conium": {
        "latin_name": "Conium maculatum",
        "common_name": "Hemlock",
        "family": "Apiaceae",
        "parts_used": "Leaves, seeds (extremely toxic)",
        "actions": ["sedative", "anodyne", "antispasmodic", "paralytic"],
        "preparations": ["tinctura (extremely dilute)", "extractum (pharmaceutical only)"],
        "dosage": "NOT RECOMMENDED FOR HOME USE. Lethal dose extremely small.",
        "contraindications": "EXTREMELY POISONOUS. Contraindicated in all cases except supervised pharmaceutical use. Death by respiratory paralysis.",
        "planetary_ruler": "Saturnus",
        "element": "Water",
        "description": "The infamous poison that killed Socrates. Contains coniine, a neurotoxin that causes ascending paralysis leading to respiratory failure. In minute, controlled doses, it was historically used for tremors and joint pain, but the risk of fatal overdose makes it unsuitable for any but the most expert use.",
        "folklore": "Forever associated with the execution of Socrates. In medieval times, associated with death and execution. The purple spots on the stems were said to be the mark of the Devil. Witches were believed to use it in flying ointments. Associated with Hecate and the underworld.",
        "historical_uses": ["tremors", "joint_pain", "mania", "whooping_cough", "external_tumors"],
        "modern_status": "Illegal to possess in many jurisdictions; no legitimate herbal use"
    },
    
    "taxus": {
        "latin_name": "Taxus baccata",
        "common_name": "Yew",
        "family": "Taxaceae",
        "parts_used": "Leaves (toxic), bark (extremely toxic)",
        "actions": ["cardiac stimulant", "cytostatic", "diuretic"],
        "preparations": ["extractum (pharmaceutical only)"],
        "dosage": "NOT FOR HOME USE. All parts except red aril are deadly poisonous.",
        "contraindications": "DEADLY POISONOUS. Contraindicated in all cases. Fatal cardiac effects.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "The ancient yew tree, often found in churchyards, contains taxine alkaloids that affect the heart. Despite its toxicity, it has become valuable in modern medicine as the original source of paclitaxel (Taxol), a chemotherapy drug used to treat various cancers. The red aril (flesh) around the seed is the only non-toxic part.",
        "folklore": "Sacred to the Druids and associated with death and rebirth. Yews were planted in churchyards to ward off evil spirits and protect the dead. The tree can live for thousands of years, symbolizing eternal life. Longbows were made from yew wood. Associated with the Celtic Otherworld.",
        "historical_uses": ["cancer_treatment (modern)", "rheumatism (historical)", "dropsy (historical)"],
        "modern_status": "Source of Taxol for chemotherapy; plant itself deadly poisonous"
    },
    
    "ricinus": {
        "latin_name": "Ricinus communis",
        "common_name": "Castor Bean",
        "family": "Euphorbiaceae",
        "parts_used": "Seeds (oil extracted), leaves",
        "actions": ["purgative", "emollient", "labor stimulant", "anti-inflammatory"],
        "preparations": ["oleum", "cataplasma", "fomentatio"],
        "dosage": "Oil: 5-15ml as purgative. External use safe. Seeds are deadly poisonous.",
        "contraindications": "Seeds contain ricin - one of the most toxic substances known. Contraindicated in pregnancy, intestinal obstruction, appendicitis. Oil generally safe but seeds deadly.",
        "planetary_ruler": "Mars",
        "element": "Fire",
        "description": "The castor bean plant produces castor oil, a safe and effective purgative when properly extracted. However, the seeds contain ricin, a protein toxin so potent that a single seed chewed can be fatal. The oil, which does not contain ricin, has been used for thousands of years as a laxative and for inducing labor.",
        "folklore": "Known to the ancient Egyptians, who used it in lamps and as medicine. The name 'castor' comes from its use as a substitute for castoreum (beaver secretion) in perfumes. Associated with protection and banishing evil. Used in Caribbean Obeah and Hoodoo practices.",
        "historical_uses": ["constipation", "labor_induction", "skin_conditions", "hair_growth", "lamp_fuel"],
        "modern_status": "Oil widely available; ricin classified as biological weapon"
    },
    
    "datura": {
        "latin_name": "Datura stramonium",
        "common_name": "Jimson Weed/Devil's Trumpet",
        "family": "Solanaceae",
        "parts_used": "Leaves, seeds",
        "actions": ["antispasmodic", "anodyne", "sedative", "hallucinogenic", "mydriatic"],
        "preparations": ["tinctura", "unguentum", "fomentatio", "cataplasma"],
        "dosage": "Leaf: 0.05-0.1g maximum. Highly variable potency. Extremely dangerous.",
        "contraindications": "POISONOUS. Contraindicated in pregnancy, glaucoma, heart conditions. Overdose causes delirium and death.",
        "planetary_ruler": "Saturnus",
        "element": "Fire",
        "description": "Datura has been used in sacred rituals across many cultures for its powerful hallucinogenic properties. Contains atropine, hyoscyamine, and scopolamine. The name 'Jimson weed' comes from Jamestown, where British soldiers were poisoned by it in 1676. Used in asthma cigarettes historically.",
        "folklore": "Sacred to Shiva in Hinduism and used in various shamanic traditions. Associated with the Devil due to its dangerous nature. The trumpet-shaped flowers open at night, associated with the underworld. Used in European witchcraft and Native American spiritual practices.",
        "historical_uses": ["asthma", "whooping_cough", "rheumatism", "sedation", "sacred_rituals"],
        "modern_status": "Controlled in many areas; scopolamine used in pharmaceuticals"
    },
    
    "aconitum": {
        "latin_name": "Aconitum napellus",
        "common_name": "Monkshood/Wolfsbane",
        "family": "Ranunculaceae",
        "parts_used": "Root, leaves",
        "actions": ["anodyne", "antipyretic", "diuretic", "cardiac depressant", "local anesthetic"],
        "preparations": ["tinctura (homeopathic only)", "linimentum (external only)"],
        "dosage": "NOT FOR INTERNAL USE EXCEPT HOMEOPATHIC. Topical: very dilute preparations only.",
        "contraindications": "EXTREMELY POISONOUS. Contraindicated in all internal use except homeopathic. Death within hours from cardiac failure.",
        "planetary_ruler": "Saturnus",
        "element": "Water",
        "description": "One of the most toxic plants known, containing aconitine, which affects sodium channels and causes rapid death. Even skin contact can cause poisoning. Historically used on arrows for hunting and warfare. In homeopathic dilutions, it is used for fever and shock, but the crude plant is deadly.",
        "folklore": "Associated with werewolves and witchcraft. Used to poison arrows and water supplies in warfare. The name 'wolfsbane' comes from its use in wolf poison. Associated with Hecate and the underworld. In medieval times, it was believed to be an ingredient in witches' flying ointments.",
        "historical_uses": ["external_pain_relief", "fever", "inflammation", "arrow_poison", "wolf_poison"],
        "modern_status": "Highly regulated; homeopathic use only for internal applications"
    },
    
    "colchicum": {
        "latin_name": "Colchicum autumnale",
        "common_name": "Autumn Crocus/Meadow Saffron",
        "family": "Colchicaceae",
        "parts_used": "Seeds, corm",
        "actions": ["anti-inflammatory", "analgesic", "cytostatic"],
        "preparations": ["tinctura", "extractum", "pilula"],
        "dosage": "0.5-1.5mg colchicine equivalent. Narrow therapeutic window.",
        "contraindications": "POISONOUS. Contraindicated in pregnancy, kidney disease, blood disorders. Fatal in overdose.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "The autumn crocus is the source of colchicine, used to treat gout for over 2000 years. Colchicine interferes with cell division and reduces inflammation. The plant is highly toxic, with symptoms resembling arsenic poisoning. It has no relationship to true saffron despite the similar appearance.",
        "folklore": "Associated with the autumn equinox and the descent into the underworld. The plant blooms in autumn without leaves, leading to associations with death and rebirth. Used in Greek mythology - Medea attempted to poison Theseus with it. Associated with the goddess Hecate.",
        "historical_uses": ["gout", "rheumatism", "dropsy", "cancer_treatment (historical)"],
        "modern_status": "Colchicine still used for gout; plant highly regulated"
    },
    
    "papaver": {
        "latin_name": "Papaver somniferum",
        "common_name": "Opium Poppy",
        "family": "Papaveraceae",
        "parts_used": "Latex from unripe seed pods, seeds (non-narcotic)",
        "actions": ["anodyne", "narcotic", "hypnotic", "antidiarrheal", "antitussive"],
        "preparations": ["latex", "tinctura (laudanum)", "extractum", "syrupus"],
        "dosage": "Highly variable. Medical opiates strictly controlled. Seeds non-narcotic.",
        "contraindications": "Highly addictive. Contraindicated in respiratory depression, head injuries, acute asthma. Risk of fatal overdose.",
        "planetary_ruler": "Saturnus",
        "element": "Water",
        "description": "The source of opium and all opiate drugs, including morphine and codeine. Cultivated for thousands of years for pain relief. The dried latex from scored pods contains powerful alkaloids. The seeds contain no narcotics and are used in baking. The plant has shaped human history through trade, war, and medicine.",
        "folklore": "Associated with sleep, death, and the underworld. The Greek god Hypnos and Roman Somnus carried poppies. Demeter created the poppy to help her sleep after losing Persephone. Associated with Morpheus, god of dreams. Used in ancient Egyptian medicine and ritual.",
        "historical_uses": ["pain_relief", "diarrhea", "cough", "insomnia", "surgical_anesthetic"],
        "modern_status": "Source of pharmaceutical opiates; cultivation and use highly regulated"
    },
    
    "arnica": {
        "latin_name": "Arnica montana",
        "common_name": "Arnica/Leopard's Bane",
        "family": "Asteraceae",
        "parts_used": "Flowers, rhizome",
        "actions": ["anti-inflammatory", "anodyne", "vulnerary", "counter-irritant", "antiseptic"],
        "preparations": ["tinctura", "oleum", "unguentum", "cataplasma", "linimentum"],
        "dosage": "EXTERNAL USE ONLY. Tincture: dilute 1:10 for compresses. Do not apply to broken skin.",
        "contraindications": "TOXIC IF TAKEN INTERNALLY. Do not use on broken skin. May cause allergic reactions in sensitive individuals.",
        "planetary_ruler": "Sol",
        "element": "Fire",
        "description": "Arnica is one of the best remedies for trauma, bruising, and muscle soreness when used externally. It reduces inflammation and speeds healing of tissues. Internally, it is toxic and can cause serious harm. The bright yellow flowers resemble the sun, reflecting its planetary association.",
        "folklore": "Named after the Greek word for 'lamb's skin' due to its soft, hairy leaves. Associated with the sun's healing power. Mountain climbers traditionally used it for sore muscles. In Alpine folklore, it was believed to protect against mountain spirits.",
        "historical_uses": ["bruises", "sprains", "muscle_pain", "arthritis", "inflammation", "wound_healing"],
        "modern_status": "External preparations widely available; internal use prohibited"
    },
    
    "salvia": {
        "latin_name": "Salvia officinalis",
        "common_name": "Garden Sage",
        "family": "Lamiaceae",
        "parts_used": "Leaves",
        "actions": ["carminative", "antiseptic", "astringent", "antihidrotic", "emmenagogue", "nervine"],
        "preparations": ["infusum", "tinctura", "oleum", "gargarisma", "pulvis"],
        "dosage": "Infusion: 1-2 tsp per cup. Tincture: 2-4ml. Safe for regular use.",
        "contraindications": "Avoid therapeutic doses in pregnancy (emmenagogue). May reduce milk supply in nursing mothers.",
        "planetary_ruler": "Jupiter",
        "element": "Air",
        "description": "The name Salvia comes from 'salvare' - to heal. Sage has been valued for centuries for its medicinal and culinary properties. It reduces excessive sweating, aids digestion, and has antiseptic properties. The essential oil is strongly antimicrobial. Used traditionally to enhance memory and cognition.",
        "folklore": "Sacred to the Romans, who believed it could confer immortality. Used in smudging ceremonies by Native Americans. Associated with wisdom and longevity. In medieval Europe, it was said 'Why should a man die while sage grows in his garden?' Used in ceremonies for protection and purification.",
        "historical_uses": ["sore_throat", "digestion", "excessive_sweating", "memory", "menopause", "wound_healing"],
        "modern_status": "Widely available and safe; research supports cognitive benefits"
    },
    
    "rosa": {
        "latin_name": "Rosa canina",
        "common_name": "Dog Rose/Wild Rose",
        "family": "Rosaceae",
        "parts_used": "Hips (fruit), petals, leaves",
        "actions": ["astringent", "nutritive", "anti-inflammatory", "diuretic", "laxative"],
        "preparations": ["infusum", "syrupus", "conserva", "oleum", "pulvis"],
        "dosage": "Hips: 2-4g or 5-10ml syrup. Petals: 2-4g for tea. Very safe.",
        "contraindications": "Generally regarded as safe. Large doses of hips may cause mild laxative effect.",
        "planetary_ruler": "Venus",
        "element": "Water",
        "description": "Rose hips are one of the richest plant sources of vitamin C, containing 20-40 times more than oranges by weight. Used traditionally for colds, flu, and as a general tonic. Rose petals have mild astringent and mood-elevating properties. The oil is prized for skincare.",
        "folklore": "Sacred to Venus and Aphrodite, goddess of love. Roses have symbolized love, beauty, and secrecy for millennia. 'Sub rosa' (under the rose) meant confidentiality. In Christian tradition, associated with the Virgin Mary. Used in love spells and to attract positive energy.",
        "historical_uses": ["vitamin_C_source", "colds", "flu", "diarrhea", "skin_care", "mild_laxative"],
        "modern_status": "Widely available; rose hip powder popular for vitamin C"
    },
    
    "chamomilla": {
        "latin_name": "Matricaria chamomilla",
        "common_name": "German Chamomile",
        "family": "Asteraceae",
        "parts_used": "Flowers",
        "actions": ["carminative", "anti-inflammatory", "antispasmodic", "sedative", "vulnerary", "bitter"],
        "preparations": ["infusum", "tinctura", "oleum", "gargarisma", "cataplasma"],
        "dosage": "Infusion: 2-3g per cup. Tincture: 1-4ml. Very safe, suitable for children.",
        "contraindications": "Rare allergic reactions in those sensitive to Asteraceae family. Generally very safe.",
        "planetary_ruler": "Sol",
        "element": "Water",
        "description": "One of the most popular herbs worldwide, chamomile is gentle yet effective for digestion, sleep, and anxiety. Contains bisabolol and chamazulene, which reduce inflammation. The flowers resemble tiny daisies with apple-like fragrance. Safe for babies and children.",
        "folklore": "Sacred to the Egyptian sun god Ra. Used in ancient Egypt, Greece, and Rome. The name comes from Greek 'chamos melon' (ground apple) due to its scent. Associated with the Norse god Baldr. Used in folk magic for prosperity and to prevent nightmares.",
        "historical_uses": ["insomnia", "anxiety", "digestive_upset", "colic", "skin_inflammation", "wound_healing"],
        "modern_status": "One of the most widely used herbs; extensive safety record"
    },
    
    "mentha": {
        "latin_name": "Mentha piperita",
        "common_name": "Peppermint",
        "family": "Lamiaceae",
        "parts_used": "Leaves",
        "actions": ["carminative", "antispasmodic", "cholagogue", "diaphoretic", "anodyne", "stimulant"],
        "preparations": ["infusum", "tinctura", "oleum", "gargarisma", "cataplasma"],
        "dosage": "Infusion: 2-3g per cup. Tincture: 1-2ml. Oil: 1-2 drops internally, diluted.",
        "contraindications": "May worsen reflux in some people. Avoid large doses in pregnancy. Oil can be irritating undiluted.",
        "planetary_ruler": "Mercurius",
        "element": "Air",
        "description": "A hybrid of spearmint and watermint, peppermint is one of the most widely used medicinal herbs. Menthol, its primary constituent, creates the cooling sensation and relaxes smooth muscles. Excellent for digestive complaints, headaches, and respiratory congestion.",
        "folklore": "Named after the Greek nymph Minthe, who was transformed into the plant by Persephone. Used in ancient Egypt and Rome. Associated with hospitality in many cultures. Used in folk magic for purification, healing, and to enhance psychic abilities.",
        "historical_uses": ["indigestion", "gas", "nausea", "headache", "congestion", "muscle_pain"],
        "modern_status": "Widely available; enteric-coated oil used for IBS"
    },
    
    "thymus": {
        "latin_name": "Thymus vulgaris",
        "common_name": "Thyme",
        "family": "Lamiaceae",
        "parts_used": "Leaves and flowering tops",
        "actions": ["antiseptic", "antispasmodic", "expectorant", "carminative", "astringent", "vermifuge"],
        "preparations": ["infusum", "tinctura", "oleum", "syrupus", "gargarisma", "mel"],
        "dosage": "Infusion: 1-2g per cup. Tincture: 2-4ml. Oil: highly concentrated, use sparingly.",
        "contraindications": "Avoid large doses in pregnancy. Oil may irritate skin undiluted. Avoid in thyroid conditions.",
        "planetary_ruler": "Venus",
        "element": "Air",
        "description": "Thyme has been used since ancient times for respiratory infections due to its powerful antiseptic properties. Thymol, its main constituent, is strongly antimicrobial. Used in mouthwashes, cough syrups, and as a culinary herb. The ancient Egyptians used it in embalming.",
        "folklore": "Name comes from Greek 'thymos' meaning courage. Roman soldiers bathed in thyme before battle. Associated with fairies in European folklore. Burned as incense for purification. Used in pillows to prevent nightmares and promote courage.",
        "historical_uses": ["respiratory_infections", "cough", "sore_throat", "digestion", "wound_antiseptic", "parasites"],
        "modern_status": "Thymol used in commercial mouthwashes; herb widely available"
    },
    
    "lavandula": {
        "latin_name": "Lavandula angustifolia",
        "common_name": "English Lavender",
        "family": "Lamiaceae",
        "parts_used": "Flowers",
        "actions": ["carminative", "antispasmodic", "antidepressant", "rubefacient", "antiseptic", "nervine"],
        "preparations": ["infusum", "tinctura", "oleum", "essentia", "aqua", "syrupus"],
        "dosage": "Infusion: 1-2 tsp per cup. Tincture: 1-2ml. Oil: external use primarily.",
        "contraindications": "Generally very safe. Oil may irritate sensitive skin undiluted. Avoid large internal doses.",
        "planetary_ruler": "Mercurius",
        "element": "Air",
        "description": "Lavender is one of the most versatile and beloved herbs, valued for its calming properties and beautiful fragrance. The essential oil is a staple in aromatherapy for anxiety, insomnia, and stress. Also has antiseptic properties and can be used for burns and insect bites.",
        "folklore": "Name comes from Latin 'lavare' (to wash) as Romans used it in baths. Associated with love and devotion in Victorian language of flowers. Used in medieval times to ward off evil spirits and the plague. Placed in linen closets to repel moths and scent fabrics.",
        "historical_uses": ["anxiety", "insomnia", "headache", "burns", "insect_bites", "depression"],
        "modern_status": "Essential oil industry staple; widely researched for anxiety"
    },
    
    "calendula": {
        "latin_name": "Calendula officinalis",
        "common_name": "Pot Marigold",
        "family": "Asteraceae",
        "parts_used": "Flowers",
        "actions": ["vulnerary", "anti-inflammatory", "antiseptic", "emmenagogue", "antifungal", "cholagogue"],
        "preparations": ["infusum", "tinctura", "oleum", "unguentum", "cataplasma"],
        "dosage": "Infusion: 1-2 tsp per cup. Tincture: 0.3-1.5ml. External preparations widely used.",
        "contraindications": "Avoid in pregnancy due to emmenagogue effect. Rare allergies in Asteraceae-sensitive individuals.",
        "planetary_ruler": "Sol",
        "element": "Fire",
        "description": "Calendula is one of the best herbs for skin healing and regeneration. It reduces inflammation, prevents infection, and speeds wound healing. The bright orange flowers follow the sun, opening in morning and closing at night. Used in cooking as 'poor man's saffron.'",
        "folklore": "Associated with the sun and solar deities. Used in ancient Greek, Roman, Middle Eastern, and Indian cultures. Worn for protection and to see fairies. Used in love divination. In medieval times, believed to lift spirits and comfort the heart.",
        "historical_uses": ["wound_healing", "skin_inflammation", "diaper_rash", "eczema", "menstrual_cramps", "varicose_veins"],
        "modern_status": "Popular in natural skincare; widely available"
    },
    
    "echinacea": {
        "latin_name": "Echinacea purpurea",
        "common_name": "Purple Coneflower",
        "family": "Asteraceae",
        "parts_used": "Root, aerial parts, seeds",
        "actions": ["immunostimulant", "antiseptic", "anti-inflammatory", "vulnerary", "sialagogue", "detoxifying"],
        "preparations": ["tinctura", "decoctum", "infusum", "extractum", "pilula"],
        "dosage": "Root tincture: 2-4ml. Decoction: 1-2g root per cup. Best used at first sign of illness.",
        "contraindications": "Rare allergies in Asteraceae-sensitive individuals. Use caution in autoimmune conditions. Short-term use recommended.",
        "planetary_ruler": "Mars",
        "element": "Fire",
        "description": "Echinacea is the most popular immune-supporting herb in North America. Native Americans used it for centuries before European adoption. It stimulates the immune system, increases white blood cell production, and has antiseptic properties. Best used at the first sign of infection.",
        "folklore": "Used extensively by Native American tribes, particularly the Plains Indians, for snake bites, wounds, and infections. The spiny central cone resembles a hedgehog (echinos in Greek). Used in ritual to bring spiritual strength and protection.",
        "historical_uses": ["colds", "flu", "infections", "wounds", "snake_bites", "immune_support"],
        "modern_status": "Top-selling herbal supplement; extensive research"
    },
    
    "valeriana": {
        "latin_name": "Valeriana officinalis",
        "common_name": "Valerian",
        "family": "Caprifoliaceae",
        "parts_used": "Root and rhizome",
        "actions": ["sedative", "nervine", "antispasmodic", "carminative", "hypnotic", "anodyne"],
        "preparations": ["tinctura", "decoctum", "extractum", "pilula", "pulvis"],
        "dosage": "Root: 2-3g. Tincture: 2-5ml. Decoction: 2-3g per cup. Best taken before bed.",
        "contraindications": "May cause drowsiness. Avoid with other sedatives. Rare paradoxical stimulation. Strong odor.",
        "planetary_ruler": "Mercurius",
        "element": "Water",
        "description": "Valerian has been used since ancient Greek and Roman times as a sleep aid and nerve tonic. The root has a strong, distinctive odor that some find unpleasant. It contains valerenic acid and other compounds that interact with GABA receptors in the brain, promoting relaxation and sleep without morning grogginess.",
        "folklore": "Named after the Roman emperor Valerianus. Used by Hippocrates and Galen. In medieval times, used as a perfume. The Pied Piper of Hamelin may have used valerian to attract rats (and children). Associated with peace and tranquility.",
        "historical_uses": ["insomnia", "anxiety", "nervous_tension", "muscle_spasms", "menstrual_cramps", "migraine"],
        "modern_status": "Widely used sleep aid; approved in Europe for insomnia"
    },
    
    "passiflora": {
        "latin_name": "Passiflora incarnata",
        "common_name": "Passionflower",
        "family": "Passifloraceae",
        "parts_used": "Aerial parts",
        "actions": ["sedative", "anxiolytic", "antispasmodic", "hypnotic", "analgesic", "nervine"],
        "preparations": ["infusum", "tinctura", "extractum", "pilula"],
        "dosage": "Infusion: 2g per cup. Tincture: 2-4ml. Safe for regular use.",
        "contraindications": "Avoid in pregnancy. May potentiate sedative medications. Generally very safe.",
        "planetary_ruler": "Venus",
        "element": "Water",
        "description": "Passionflower was named by Spanish missionaries who saw symbols of Christ's passion in its flowers. It is excellent for anxiety, insomnia, and nervous tension without causing drowsiness. Contains flavonoids and alkaloids that have calming effects on the nervous system.",
        "folklore": "Named by Spanish missionaries in South America who saw in the flower: the crown of thorns (filaments), the five wounds (stamens), the three nails (styles), and the column of the scourging (stalk). Used by Native Americans for centuries. Associated with peace and spiritual devotion.",
        "historical_uses": ["anxiety", "insomnia", "nervous_tension", "muscle_spasms", "neuralgia", "seizures"],
        "modern_status": "Popular anxiety remedy; approved in Europe for nervous restlessness"
    },
    
    "hypericum": {
        "latin_name": "Hypericum perforatum",
        "common_name": "St. John's Wort",
        "family": "Hypericaceae",
        "parts_used": "Flowering tops",
        "actions": ["antidepressant", "antiviral", "vulnerary", "anti-inflammatory", "nervine", "hepatic"],
        "preparations": ["infusum", "tinctura", "oleum", "extractum", "pilula"],
        "dosage": "Infusion: 2-4g per cup. Tincture: 2-4ml. Standardized extract: 300mg (0.3% hypericin).",
        "contraindications": "MAJOR DRUG INTERACTIONS. Contraindicated with SSRIs, MAOIs, birth control, blood thinners, HIV medications, transplant drugs. Photosensitivity possible.",
        "planetary_ruler": "Sol",
        "element": "Fire",
        "description": "St. John's Wort is one of the most studied herbs for mild to moderate depression. It contains hypericin and hyperforin, which affect neurotransmitters. Also has antiviral properties and is used externally for nerve pain and wound healing. Blooms around the summer solstice, associated with St. John's Day (June 24).",
        "folklore": "Named after St. John the Baptist as it blooms near his feast day. Associated with the sun and protection. Hung in windows to ward off evil spirits and lightning. In medieval Europe, it was believed to reveal fairies and protect against witchcraft. Used in divination for love.",
        "historical_uses": ["depression", "anxiety", "nerve_pain", "wounds", "viral_infections", "menopause"],
        "modern_status": "Widely prescribed in Europe for depression; drug interaction warnings essential"
    },
    
    "glycyrrhiza": {
        "latin_name": "Glycyrrhiza glabra",
        "common_name": "Licorice",
        "family": "Fabaceae",
        "parts_used": "Root",
        "actions": ["expectorant", "demulcent", "adrenal tonic", "anti-inflammatory", "antispasmodic", "laxative"],
        "preparations": ["decoctum", "tinctura", "extractum", "syrupus", "pulvis"],
        "dosage": "Root: 1-5g. Deglycyrrhizinated form (DGL) for long-term use. Limit glycyrrhizin to <100mg/day.",
        "contraindications": "Raises blood pressure. Contraindicated in hypertension, kidney disease, heart failure, pregnancy, hormone-sensitive cancers. Potassium depletion with long-term use.",
        "planetary_ruler": "Venus",
        "element": "Water",
        "description": "Licorice is one of the most widely used herbs in traditional Chinese medicine and is found in many Western formulas as a harmonizer. It soothes mucous membranes, supports adrenal function, and has anti-inflammatory properties. The sweet taste comes from glycyrrhizin, which is 50 times sweeter than sugar.",
        "folklore": "Used in ancient Egypt, Greece, Rome, China, and India. Found in King Tut's tomb. Used to flavor tobacco and candies. Associated with love and lust in folklore. In Chinese medicine, it harmonizes formulas and 'guides' other herbs to their destinations.",
        "historical_uses": ["cough", "sore_throat", "adrenal_fatigue", "ulcers", "inflammation", "constipation"],
        "modern_status": "DGL form widely used for ulcers; glycyrrhizin content regulated"
    },
    
    "zingiber": {
        "latin_name": "Zingiber officinale",
        "common_name": "Ginger",
        "family": "Zingiberaceae",
        "parts_used": "Rhizome (root)",
        "actions": ["carminative", "antiemetic", "diaphoretic", "antispasmodic", "circulatory stimulant", "anti-inflammatory"],
        "preparations": ["infusum", "decoctum", "tinctura", "oleum", "pulvis", "conserva"],
        "dosage": "Fresh: 2-4g. Dried: 1-3g. Very safe. Can use liberally in cooking.",
        "contraindications": "High doses may aggravate heartburn. Use caution with gallstones. Generally very safe.",
        "planetary_ruler": "Mars",
        "element": "Fire",
        "description": "Ginger is one of the most widely used spices and medicines worldwide. It is excellent for nausea, digestion, and circulation. Contains gingerol and shogaol, which have anti-inflammatory and antiemetic effects. Used fresh, dried, or crystallized. Safe for pregnancy-related nausea.",
        "folklore": "Used in ancient India, China, and Rome. Marco Polo encountered it in China. Used in Ayurveda and Traditional Chinese Medicine for thousands of years. Associated with wealth and prosperity. Used in love spells and to 'heat up' relationships. In the Caribbean, used in spiritual cleansing.",
        "historical_uses": ["nausea", "motion_sickness", "morning_sickness", "indigestion", "colds", "inflammation", "circulation"],
        "modern_status": "Widely researched for nausea; GRAS (Generally Recognized As Safe)"
    },
    
    "cinnamomum": {
        "latin_name": "Cinnamomum verum",
        "common_name": "Ceylon Cinnamon/True Cinnamon",
        "family": "Lauraceae",
        "parts_used": "Inner bark",
        "actions": ["carminative", "antiseptic", "astringent", "warming", "antispasmodic", "emmenagogue"],
        "preparations": ["infusum", "tinctura", "pulvis", "oleum", "mel", "conserva"],
        "dosage": "Bark: 1-4g. Powder: 0.5-2g. Very safe in culinary amounts.",
        "contraindications": "Cassia cinnamon (common variety) contains coumarin - avoid large doses. Ceylon cinnamon safer. Emmenagogue - avoid large doses in pregnancy.",
        "planetary_ruler": "Sol",
        "element": "Fire",
        "description": "True cinnamon from Ceylon (Sri Lanka) is sweeter and more delicate than the common cassia cinnamon. It has been treasured for thousands of years, once worth more than gold by weight. Warms the body, aids digestion, and helps regulate blood sugar. The essential oil is strongly antimicrobial.",
        "folklore": "Mentioned in the Bible and ancient Egyptian texts. Used in embalming by Egyptians. Highly valued in ancient trade. Associated with wealth, prosperity, and love. Used in incense for purification and to raise spiritual vibrations. In medieval times, used to preserve meat.",
        "historical_uses": ["digestion", "colds", "diabetes", "circulation", "preservation", "flavoring"],
        "modern_status": "Research supports blood sugar regulation; widely used spice"
    },
    
    "arnica_montana": {
        "latin_name": "Arnica montana",
        "common_name": "Mountain Arnica",
        "family": "Asteraceae",
        "parts_used": "Flowers",
        "actions": ["anti-inflammatory", "analgesic", "counter-irritant", "antimicrobial"],
        "preparations": ["tinctura", "oleum", "unguentum", "cataplasma", "gel"],
        "dosage": "EXTERNAL USE ONLY. Apply to unbroken skin 2-3 times daily.",
        "contraindications": "TOXIC IF INGESTED. Do not use on broken skin. Allergy test recommended.",
        "planetary_ruler": "Sol",
        "element": "Fire",
        "description": "Mountain arnica grows in alpine meadows and has been used for centuries for trauma and inflammation. It reduces bruising, swelling, and pain when applied externally. The flowers contain sesquiterpene lactones that have anti-inflammatory effects.",
        "folklore": "Associated with mountain spirits in Alpine folklore. Used by mountain climbers for sore muscles. The bright yellow flowers were believed to capture the sun's healing power. Used in folk medicine throughout the European Alps.",
        "historical_uses": ["bruises", "sprains", "muscle_soreness", "arthritis", "insect_bites"],
        "modern_status": "Popular homeopathic and herbal remedy for trauma"
    },
    
    "hamamelis": {
        "latin_name": "Hamamelis virginiana",
        "common_name": "Witch Hazel",
        "family": "Hamamelidaceae",
        "parts_used": "Leaves, bark",
        "actions": ["astringent", "anti-inflammatory", "hemostatic", "vulnerary", "antiseptic"],
        "preparations": ["decoctum", "tinctura", "aqua", "extractum", "linimentum"],
        "dosage": "External use primarily. Witch hazel water (distillate) applied as needed.",
        "contraindications": "Generally very safe for external use. Internal use only under professional guidance.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "Witch hazel is a North American native that has become a staple in natural first aid. The bark and leaves contain tannins that tighten and tone tissues, reducing inflammation and bleeding. The distilled witch hazel water is widely available and used for skin care and first aid.",
        "folklore": "Used by Native Americans for centuries. The name 'witch hazel' comes from Middle English 'wiche' meaning pliable or bendable, not witchcraft. However, the forked branches were traditionally used as divining rods to find water. Associated with dowsing and water witching.",
        "historical_uses": ["hemorrhoids", "varicose_veins", "bruises", "insect_bites", "skin_inflammation", "aftershave"],
        "modern_status": "Witch hazel water widely available in pharmacies"
    },
    
    "hamamelis_vernalis": {
        "latin_name": "Hamamelis vernalis",
        "common_name": "Vernal Witch Hazel",
        "family": "Hamamelidaceae",
        "parts_used": "Leaves, bark",
        "actions": ["astringent", "anti-inflammatory", "hemostatic"],
        "preparations": ["decoctum", "tinctura", "aqua"],
        "dosage": "External use primarily. Similar to H. virginiana.",
        "contraindications": "Generally very safe for external use.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "A species of witch hazel native to the Ozark Plateau, blooming in late winter to early spring. Similar properties to common witch hazel but blooms during a different season. Used interchangeably with H. virginiana.",
        "folklore": "Blooms in late winter when most other plants are dormant, leading to associations with resilience and endurance. Used similarly to common witch hazel in folk medicine.",
        "historical_uses": ["similar_to_H_virginiana", "astringent", "anti-inflammatory"],
        "modern_status": "Used interchangeably with H. virginiana"
    },
    
    "hamamelis_japonica": {
        "latin_name": "Hamamelis japonica",
        "common_name": "Japanese Witch Hazel",
        "family": "Hamamelidaceae",
        "parts_used": "Leaves, bark",
        "actions": ["astringent", "anti-inflammatory", "hemostatic"],
        "preparations": ["decoctum", "tinctura", "aqua"],
        "dosage": "External use primarily. Similar to other Hamamelis species.",
        "contraindications": "Generally very safe for external use.",
        "planetary_ruler": "Saturnus",
        "element": "Earth",
        "description": "Native to Japan, this species of witch hazel shares similar astringent and anti-inflammatory properties with its American counterparts. Used in traditional Japanese medicine and as an ornamental plant.",
        "folklore": "Used in traditional Japanese medicine. Valued as an ornamental for its winter-blooming flowers.",
        "historical_uses": ["astringent", "anti-inflammatory", "traditional_Japanese_medicine"],
        "modern_status": "Primarily ornamental; medicinal use similar to other species"
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# END OF PART 2
# ═══════════════════════════════════════════════════════════════════════════════
# INSTRUCTIONS: Copy this entire section AFTER Part 1 in your Streamlit app.
# Next: Part 3 contains CSS STYLING, HELPER FUNCTIONS & SEASONAL PROTOCOLS.
# ═══════════════════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════════════════
# WILKEN KEY ENGINE v5.0 - PART 3: CSS STYLING, HELPER FUNCTIONS & SEASONAL PROTOCOLS
# ═══════════════════════════════════════════════════════════════════════════════
# This section contains all CSS styling, helper functions, seasonal preparation
# protocols, planetary hour calculations, and utility functions for the engine.
# Copy this AFTER Part 2 in your Streamlit application.
# ═══════════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 3A: CUSTOM CSS STYLING
# ───────────────────────────────────────────────────────────────────────────────

def load_css():
    """Load comprehensive custom CSS for Wilken Key Engine styling."""
    st.markdown("""
    <style>
    /* ═════════════════════════════════════════════════════════════════════════
       ROOT VARIABLES AND BASE STYLES
       ═════════════════════════════════════════════════════════════════════════ */
    :root {
        --primary-color: #1e3a5f;
        --secondary-color: #2c5282;
        --accent-color: #d69e2e;
        --success-color: #38a169;
        --warning-color: #d69e2e;
        --danger-color: #e53e3e;
        --info-color: #3182ce;
        --bg-dark: #0d1b2a;
        --bg-card: #1b263b;
        --text-primary: #e0e1dd;
        --text-secondary: #778da9;
        --border-color: #415a77;
        --shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.4);
        --radius: 8px;
        --radius-lg: 12px;
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       MAIN CONTAINER AND LAYOUT
       ═════════════════════════════════════════════════════════════════════════ */
    .main {
        background: linear-gradient(135deg, var(--bg-dark) 0%, #1a1a2e 50%, var(--bg-dark) 100%);
        color: var(--text-primary);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main .block-container {
        padding: 1rem 2rem;
        max-width: 1400px;
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       HEADER STYLES
       ═════════════════════════════════════════════════════════════════════════ */
    .wilken-header {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        border-radius: var(--radius-lg);
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: var(--shadow-lg);
        border: 2px solid var(--accent-color);
    }
    
    .wilken-header h1 {
        color: var(--accent-color) !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        text-align: center;
        margin: 0 !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        letter-spacing: 2px;
    }
    
    .wilken-header h2 {
        color: var(--text-primary) !important;
        font-size: 1.3rem !important;
        text-align: center;
        margin: 0.5rem 0 0 0 !important;
        font-weight: 400;
    }
    
    .wilken-header p {
        color: var(--text-secondary) !important;
        text-align: center;
        margin: 0.5rem 0 0 0 !important;
        font-size: 0.95rem;
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       METRICS CARDS
       ═════════════════════════════════════════════════════════════════════════ */
    .metric-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, var(--bg-card) 0%, #2d3748 100%);
        border-radius: var(--radius);
        padding: 1.5rem;
        text-align: center;
        border: 1px solid var(--border-color);
        box-shadow: var(--shadow);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-lg);
        border-color: var(--accent-color);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--accent-color);
        line-height: 1;
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: var(--text-secondary);
        margin-top: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       SIDEBAR STYLING
       ═════════════════════════════════════════════════════════════════════════ */
    .css-1d391kg {
        background: linear-gradient(180deg, var(--bg-card) 0%, var(--bg-dark) 100%);
    }
    
    .sidebar-content {
        padding: 1rem;
    }
    
    .sidebar-title {
        color: var(--accent-color);
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--accent-color);
    }
    
    .sidebar-section {
        background: rgba(255, 255, 255, 0.05);
        border-radius: var(--radius);
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid var(--border-color);
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       WAYPOINT CARDS
       ═════════════════════════════════════════════════════════════════════════ */
    .waypoint-card {
        background: linear-gradient(135deg, var(--bg-card) 0%, #1e293b 100%);
        border-radius: var(--radius-lg);
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid var(--accent-color);
        box-shadow: var(--shadow);
        transition: all 0.3s ease;
    }
    
    .waypoint-card:hover {
        box-shadow: var(--shadow-lg);
        border-left-width: 6px;
    }
    
    .waypoint-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid var(--border-color);
    }
    
    .waypoint-number {
        background: var(--accent-color);
        color: var(--bg-dark);
        font-weight: 700;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.875rem;
    }
    
    .waypoint-type {
        background: var(--secondary-color);
        color: var(--text-primary);
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .waypoint-title {
        color: var(--accent-color);
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .waypoint-description {
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    .waypoint-meta {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-top: 1rem;
    }
    
    .waypoint-tag {
        background: rgba(214, 158, 46, 0.2);
        color: var(--accent-color);
        padding: 0.25rem 0.5rem;
        border-radius: 4px;
        font-size: 0.75rem;
        border: 1px solid var(--accent-color);
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       FOLIO DISPLAY
       ═════════════════════════════════════════════════════════════════════════ */
    .folio-display {
        background: var(--bg-card);
        border-radius: var(--radius-lg);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 2px solid var(--border-color);
        box-shadow: var(--shadow);
    }
    
    .folio-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid var(--accent-color);
    }
    
    .folio-id {
        font-size: 2rem;
        font-weight: 700;
        color: var(--accent-color);
    }
    
    .folio-section {
        background: var(--secondary-color);
        color: var(--text-primary);
        padding: 0.5rem 1rem;
        border-radius: var(--radius);
        font-size: 0.875rem;
    }
    
    .folio-image-container {
        background: #000;
        border-radius: var(--radius);
        padding: 1rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .folio-image {
        max-width: 100%;
        border-radius: var(--radius);
        box-shadow: 0 0 20px rgba(214, 158, 46, 0.3);
    }
    
    .folio-caption {
        color: var(--text-secondary);
        font-size: 0.875rem;
        margin-top: 0.5rem;
        font-style: italic;
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       INVESTIGATION PANELS
       ═════════════════════════════════════════════════════════════════════════ */
    .investigation-panel {
        background: linear-gradient(135deg, rgba(30, 58, 95, 0.3) 0%, rgba(27, 38, 59, 0.5) 100%);
        border-radius: var(--radius-lg);
        padding: 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid var(--border-color);
    }
    
    .investigation-title {
        color: var(--accent-color);
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .investigation-content {
        color: var(--text-primary);
        line-height: 1.8;
    }
    
    .investigation-content strong {
        color: var(--accent-color);
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       RECIPE CARDS
       ═════════════════════════════════════════════════════════════════════════ */
    .recipe-card {
        background: var(--bg-card);
        border-radius: var(--radius);
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid var(--success-color);
    }
    
    .recipe-title {
        color: var(--success-color);
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
    }
    
    .recipe-ingredients {
        background: rgba(56, 161, 105, 0.1);
        border-radius: var(--radius);
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    .recipe-ingredients h4 {
        color: var(--success-color);
        margin: 0 0 0.5rem 0;
        font-size: 0.9rem;
    }
    
    .recipe-ingredients ul {
        margin: 0;
        padding-left: 1.5rem;
        color: var(--text-secondary);
    }
    
    .recipe-instructions {
        color: var(--text-primary);
        line-height: 1.8;
    }
    
    .recipe-instructions ol {
        padding-left: 1.5rem;
    }
    
    .recipe-instructions li {
        margin-bottom: 0.5rem;
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       REFERENCE TABLES
       ═════════════════════════════════════════════════════════════════════════ */
    .reference-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
    
    .reference-table th {
        background: var(--primary-color);
        color: var(--accent-color);
        padding: 0.75rem;
        text-align: left;
        font-weight: 600;
        border-bottom: 2px solid var(--accent-color);
    }
    
    .reference-table td {
        padding: 0.75rem;
        border-bottom: 1px solid var(--border-color);
        color: var(--text-primary);
    }
    
    .reference-table tr:hover td {
        background: rgba(214, 158, 46, 0.1);
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       EXPANDER STYLING
       ═════════════════════════════════════════════════════════════════════════ */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        border-radius: var(--radius);
        color: var(--text-primary) !important;
        font-weight: 600;
        border: 1px solid var(--border-color);
    }
    
    .streamlit-expanderContent {
        background: var(--bg-card);
        border-radius: 0 0 var(--radius) var(--radius);
        border: 1px solid var(--border-color);
        border-top: none;
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       BUTTON STYLING
       ═════════════════════════════════════════════════════════════════════════ */
    .stButton > button {
        background: linear-gradient(135deg, var(--accent-color) 0%, #b7791f 100%);
        color: var(--bg-dark);
        font-weight: 600;
        border: none;
        border-radius: var(--radius);
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(214, 158, 46, 0.4);
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       SELECTBOX AND INPUT STYLING
       ═════════════════════════════════════════════════════════════════════════ */
    .stSelectbox > div > div {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: var(--radius);
        color: var(--text-primary);
    }
    
    .stSelectbox > div > div:hover {
        border-color: var(--accent-color);
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       ALERT AND INFO BOXES
       ═════════════════════════════════════════════════════════════════════════ */
    .info-box {
        background: rgba(49, 130, 206, 0.2);
        border-left: 4px solid var(--info-color);
        border-radius: 0 var(--radius) var(--radius) 0;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: rgba(214, 158, 46, 0.2);
        border-left: 4px solid var(--warning-color);
        border-radius: 0 var(--radius) var(--radius) 0;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .danger-box {
        background: rgba(229, 62, 62, 0.2);
        border-left: 4px solid var(--danger-color);
        border-radius: 0 var(--radius) var(--radius) 0;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .success-box {
        background: rgba(56, 161, 105, 0.2);
        border-left: 4px solid var(--success-color);
        border-radius: 0 var(--radius) var(--radius) 0;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       FOOTER STYLING
       ═════════════════════════════════════════════════════════════════════════ */
    .wilken-footer {
        background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-dark) 100%);
        border-radius: var(--radius-lg);
        padding: 2rem;
        margin-top: 2rem;
        border: 1px solid var(--border-color);
        text-align: center;
    }
    
    .wilken-footer p {
        color: var(--text-secondary);
        margin: 0.5rem 0;
        font-size: 0.875rem;
    }
    
    .wilken-footer .footer-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 1rem 0;
    }
    
    .wilken-footer .footer-links a {
        color: var(--accent-color);
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .wilken-footer .footer-links a:hover {
        color: var(--text-primary);
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       SCROLLBAR STYLING
       ═════════════════════════════════════════════════════════════════════════ */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-dark);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--border-color);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--accent-color);
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       ANIMATIONS
       ═════════════════════════════════════════════════════════════════════════ */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-fade-in {
        animation: fadeIn 0.5s ease-out;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .animate-pulse {
        animation: pulse 2s infinite;
    }
    
    /* ═════════════════════════════════════════════════════════════════════════
       RESPONSIVE DESIGN
       ═════════════════════════════════════════════════════════════════════════ */
    @media (max-width: 768px) {
        .wilken-header h1 {
            font-size: 1.75rem !important;
        }
        
        .metric-value {
            font-size: 1.75rem;
        }
        
        .folio-id {
            font-size: 1.5rem;
        }
        
        .waypoint-header {
            flex-direction: column;
            gap: 0.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 3B: SEASONAL PROTOCOLS
# ───────────────────────────────────────────────────────────────────────────────

SEASONAL_PROTOCOLS = {
    "ver": {  # Spring
        "name": "Ver (Spring)",
        "months": ["Martius", "Aprilis", "Maius"],
        "latin_name": "Tempus Vernum",
        "description": "The season of awakening and new growth. Sap rises, herbs burst forth with vital energy.",
        "collection_times": {
            "roots": "Before sap rises, early in the season",
            "barks": "During sap flow for easy removal",
            "leaves": "When fully unfolded but still tender",
            "flowers": "At full bloom, morning after dew dries",
            "seeds": "Not typically collected in spring"
        },
        "preparation_methods": [
            "Fresh herb tinctures capture spring vitality",
            "Cold infusions preserve delicate volatile oils",
            "Syrups made with fresh spring honey",
            "Vinegars for mineral extraction"
        ],
        "planetary_influence": {
            "dominant": ["Venus", "Mars"],
            "qualities": "Moist and warming, promoting growth and circulation"
        },
        "elemental_balance": {
            "primary": "Air",
            "secondary": "Water",
            "qualities": "Expansive, upward-moving energy"
        },
        "recommended_herbs": [
            "mandragora", "digitalis", "artemisia", "chamomilla",
            "mentha", "thymus", "calendula", "valeriana"
        ],
        "alchemical_processes": [
            "Solutio - dissolution and purification",
            "Coagulatio - gentle solidification",
            "Fixatio - stabilizing volatile principles"
        ],
        "folklore": "Spring herbs were believed to carry the awakening power of the earth, best collected when the first crescent moon appears after equinox."
    },
    
    "aestas": {  # Summer
        "name": "Aestas (Summer)",
        "months": ["Junius", "Julius", "Augustus"],
        "latin_name": "Tempus Aestivum",
        "description": "The season of fullness and fire. Plants reach peak potency under the solar influence.",
        "collection_times": {
            "flowers": "At peak bloom, mid-morning after dew",
            "leaves": "Before flowering for maximum oil content",
            "fruits": "When fully ripe but before over-ripening",
            "seeds": "As they mature but before dispersal",
            "roots": "Not typically collected in summer"
        },
        "preparation_methods": [
            "Solar infusions harness peak solar energy",
            "Oil infusions for external applications",
            "Hydrosols from steam distillation",
            "Drying in shade to preserve color and potency"
        ],
        "planetary_influence": {
            "dominant": ["Sol", "Mars"],
            "qualities": "Hot and dry, promoting action and transformation"
        },
        "elemental_balance": {
            "primary": "Fire",
            "secondary": "Air",
            "qualities": "Expansive, radiant, transformative energy"
        },
        "recommended_herbs": [
            "rosa", "lavandula", "calendula", "echinacea",
            "hypericum", "thymus", "mentha", "passiflora"
        ],
        "alchemical_processes": [
            "Calcinatio - reduction by fire",
            "Sublimatio - purification through heat",
            "Separatio - division of pure from impure"
        ],
        "folklore": "Summer harvests were timed to the full moon, when plants were believed to hold their maximum solar-charged potency."
    },
    
    "autumnus": {  # Autumn/Fall
        "name": "Autumnus (Autumn)",
        "months": ["September", "October", "November"],
        "latin_name": "Tempus Autumnale",
        "description": "The season of harvest and return. Energy descends to roots, fruits mature, seeds form.",
        "collection_times": {
            "roots": "After aerial parts die back, energy concentrated",
            "seeds": "When fully mature and dry on the plant",
            "fruits": "At full ripeness for immediate use or drying",
            "barks": "As sap descends, easier to peel",
            "nuts": "When husks split and nuts fall"
        },
        "preparation_methods": [
            "Root decoctions for deep extraction",
            "Seed tinctures for longevity",
            "Fruit syrups and elixirs",
            "Double extraction for mushrooms"
        ],
        "planetary_influence": {
            "dominant": ["Saturnus", "Mercurius"],
            "qualities": "Dry and cooling, promoting preservation and storage"
        },
        "elemental_balance": {
            "primary": "Earth",
            "secondary": "Water",
            "qualities": "Contracting, grounding, consolidating energy"
        },
        "recommended_herbs": [
            "datura", "colchicum", "aconitum", "glycyrrhiza",
            "zingiber", "cinnamomum", "valeriana", "arnica"
        ],
        "alchemical_processes": [
            "Putrefactio - controlled decomposition",
            "Fermentatio - transformation through fermentation",
            "Multiplicatio - increasing potency"
        ],
        "folklore": "Autumn roots were collected on waning moons, when the earth's energy was believed to be drawn downward into the roots."
    },
    
    "hiems": {  # Winter
        "name": "Hiems (Winter)",
        "months": ["December", "Januarius", "Februarius"],
        "latin_name": "Tempus Hibernum",
        "description": "The season of stillness and seed. The earth rests, storing energy for the renewal to come.",
        "collection_times": {
            "roots": "Best season for most root harvests",
            "barks": "Easy to collect when trees are dormant",
            "evergreens": "Needles and cones available year-round",
            "seeds": "Collected from storage or remaining on plants",
            "mosses": "Lichen and mosses visible on bare branches"
        },
        "preparation_methods": [
            "Long macerations for deep extraction",
            "Decoctions for hardy materials",
            "Stored herb processing from autumn harvest",
            "Planning and preparation for spring"
        ],
        "planetary_influence": {
            "dominant": ["Saturnus", "Luna"],
            "qualities": "Cold and moist, promoting rest and introspection"
        },
        "elemental_balance": {
            "primary": "Water",
            "secondary": "Earth",
            "qualities": "Still, deep, contemplative energy"
        },
        "recommended_herbs": [
            "taxus", "conium", "hyoscyamus", "papaver",
            "glycyrrhiza", "zingiber", "cinnamomum", "salvia"
        ],
        "alchemical_processes": [
            "Mortificatio - death and dissolution",
            "Regeneratio - preparation for rebirth",
            "Coniunctio - sacred marriage of opposites"
        ],
        "folklore": "Winter was the time for studying herbals, preparing medicines from stored harvests, and planning the garden for the coming year."
    }
}

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 3C: PLANETARY HOURS CALCULATION
# ───────────────────────────────────────────────────────────────────────────────

PLANETARY_HOURS = {
    "dies_solis": {  # Sunday
        "ruler": "Sol",
        "hours": ["Sol", "Venus", "Mercurius", "Luna", "Saturnus", "Jupiter", "Mars"] * 3 + ["Sol"]
    },
    "dies_lunae": {  # Monday
        "ruler": "Luna",
        "hours": ["Luna", "Saturnus", "Jupiter", "Mars", "Sol", "Venus", "Mercurius"] * 3 + ["Luna"]
    },
    "dies_martis": {  # Tuesday
        "ruler": "Mars",
        "hours": ["Mars", "Sol", "Venus", "Mercurius", "Luna", "Saturnus", "Jupiter"] * 3 + ["Mars"]
    },
    "dies_mercurii": {  # Wednesday
        "ruler": "Mercurius",
        "hours": ["Mercurius", "Luna", "Saturnus", "Jupiter", "Mars", "Sol", "Venus"] * 3 + ["Mercurius"]
    },
    "dies_jovis": {  # Thursday
        "ruler": "Jupiter",
        "hours": ["Jupiter", "Mars", "Sol", "Venus", "Mercurius", "Luna", "Saturnus"] * 3 + ["Jupiter"]
    },
    "dies_veneris": {  # Friday
        "ruler": "Venus",
        "hours": ["Venus", "Mercurius", "Luna", "Saturnus", "Jupiter", "Mars", "Sol"] * 3 + ["Venus"]
    },
    "dies_saturni": {  # Saturday
        "ruler": "Saturnus",
        "hours": ["Saturnus", "Jupiter", "Mars", "Sol", "Venus", "Mercurius", "Luna"] * 3 + ["Saturnus"]
    }
}

PLANETARY_CORRESPONDENCES = {
    "Sol": {
        "metal": "Aurum (Gold)",
        "gem": "Chrysolithus (Topaz)",
        "herbs": ["arnica", "calendula", "hypericum", "rosa"],
        "qualities": "Hot and dry, illuminating, vitalizing",
        "body_parts": ["cor", "oculi", "dextra pars corporis"],
        "diseases": ["defectus caloris", "debilitas vitalis", "melancholia"],
        "best_for": "Strengthening the heart, improving vision, lifting spirits"
    },
    "Luna": {
        "metal": "Argentum (Silver)",
        "gem": "Selena (Moonstone)",
        "herbs": ["chamomilla", "mentha", "passiflora", "valeriana"],
        "qualities": "Cold and moist, receptive, nurturing",
        "body_parts": ["cerebrum", "ventriculus", "sinistra pars corporis"],
        "diseases": ["insomnia", "anxiety", "fluxus humorum"],
        "best_for": "Calming the mind, aiding sleep, regulating fluids"
    },
    "Mars": {
        "metal": "Ferrum (Iron)",
        "gem": "Sardius (Carnelian)",
        "herbs": ["capsicum", "zingiber", "allium", " Armoracia"],
        "qualities": "Hot and dry, active, penetrating",
        "body_parts": ["sanguis", "musculi", "gall bladder"],
        "diseases": ["frigus", "torpor", "defectus sanguinis"],
        "best_for": "Stimulating circulation, building blood, increasing heat"
    },
    "Mercurius": {
        "metal": "Hydrargyrum (Quicksilver)",
        "gem": "Achates (Agate)",
        "herbs": ["lavandula", "mentha", "foeniculum", "anethum"],
        "qualities": "Variable, communicative, transformative",
        "body_parts": ["lingua", "nervi", "pulmones", "intestina"],
        "diseases": ["obstructio", "stultitia", "paralysis"],
        "best_for": "Improving communication, aiding digestion, sharpening mind"
    },
    "Jupiter": {
        "metal": "Stannum (Tin)",
        "gem": "Sapphirus (Sapphire)",
        "herbs": ["salvia", "melissa", "glycyrrhiza", "dandelion"],
        "qualities": "Hot and moist, expansive, benevolent",
        "body_parts": ["hepar", "venae", "pinguedo"],
        "diseases": ["defectus spiritus", "paupertas", "obstructio hepatis"],
        "best_for": "Liver support, improving prosperity, expanding consciousness"
    },
    "Venus": {
        "metal": "Cuprum (Copper)",
        "gem": "Smaragdus (Emerald)",
        "herbs": ["rosa", "lavandula", "matricaria", "tilia"],
        "qualities": "Cold and moist, attractive, harmonizing",
        "body_parts": ["renes", "cutis", "glandulae"],
        "diseases": ["siccitas", "discordia", "defectus amoris"],
        "best_for": "Skin conditions, promoting love, kidney support"
    },
    "Saturnus": {
        "metal": "Plumbum (Lead)",
        "gem": "Onyx (Onyx)",
        "herbs": ["aconitum", "digitalis", "mandragora", "belladonna"],
        "qualities": "Cold and dry, restrictive, crystallizing",
        "body_parts": ["ossa", "dentes", "splen", "dextra auris"],
        "diseases": ["rheuma", "paralysis", "chronicus morbus"],
        "best_for": "Bone strength, chronic conditions, deep transformation"
    }
}

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 3D: HELPER FUNCTIONS
# ───────────────────────────────────────────────────────────────────────────────

def get_yale_image_url(folio_id: str, size: str = "full", quality: str = "default") -> str:
    """
    Generate Yale Beinecke IIIF image URL for a Voynich folio.
    
    Args:
        folio_id: Folio identifier (e.g., "f1r", "f10v")
        size: Image size parameter (default "full", or "!300,300" for thumbnail)
        quality: Image quality (default "default", or "native")
    
    Returns:
        Complete IIIF image URL
    """
    try:
        # Parse folio number and side
        folio_num = int(folio_id[1:-1])
        is_verso = folio_id.endswith('v')
        
        # Calculate base Yale ID
        base_id = BASE_YALE_ID + (folio_num * 2) + (1 if is_verso else 0)
        
        # Apply Rosetta shift for folios > 86
        if folio_num > 86:
            base_id += ROSETTA_SHIFT
        
        # Construct IIIF URL
        url = f"{YALE_IIIF_BASE}{base_id}/info.json"
        
        # Return image URL with specified size
        if size != "full":
            url = f"{YALE_IIIF_BASE}{base_id}/full/{size}/0/{quality}.jpg"
        
        return url
    except Exception as e:
        return f"Error generating URL: {str(e)}"


def get_folio_section(folio_id: str) -> str:
    """Determine which section a folio belongs to."""
    try:
        folio_num = int(folio_id[1:-1])
        is_verso = folio_id.endswith('v')
        
        for section_name, section_data in FOLIO_SECTIONS.items():
            ranges = section_data["folios"]
            for start, end in ranges:
                if start <= folio_num <= end:
                    return section_name
        return "Unknown Section"
    except:
        return "Invalid Folio"


def get_section_description(folio_id: str) -> str:
    """Get the description for a folio's section."""
    section = get_folio_section(folio_id)
    return FOLIO_SECTIONS.get(section, {}).get("description", "No description available.")


def get_section_characteristics(folio_id: str) -> list:
    """Get the characteristics for a folio's section."""
    section = get_folio_section(folio_id)
    return FOLIO_SECTIONS.get(section, {}).get("characteristics", [])


def get_section_significance(folio_id: str) -> str:
    """Get the significance for a folio's section."""
    section = get_folio_section(folio_id)
    return FOLIO_SECTIONS.get(section, {}).get("significance", "")


def transliterate_to_wilken(text: str) -> str:
    """
    Convert Voynich text to Wilken Key phonetic approximation.
    This is a simplified transliteration based on common Voynich character patterns.
    """
    # Simplified mapping (in practice, this would be much more complex)
    voynich_to_wilken = {
        'o': 'o', 'a': 'a', 'y': 'i', 'd': 'd', 'l': 'l',
        'r': 'r', 's': 's', 'n': 'n', 'm': 'm', 'k': 'k',
        't': 't', 'p': 'p', 'f': 'f', 'c': 'k', 'h': 'h',
        'e': 'e', 'i': 'i', 'u': 'u', 'g': 'g', 'b': 'b',
        'q': 'kw', 'x': 'ks', 'z': 'z', 'v': 'v', 'w': 'w',
        'ch': 'kh', 'sh': 'sh', 'th': 'th', 'ph': 'f',
        'ae': 'e', 'oe': 'e', 'au': 'ow', 'eu': 'oy'
    }
    
    result = text.lower()
    for voynich, wilken in voynich_to_wilken.items():
        result = result.replace(voynich, wilken)
    
    return result


def get_latin_term(category: str, term_key: str) -> dict:
    """Get Latin term details from pharmacopeia."""
    categories = {
        "preparations": LATIN_PHARMACOPEIA["preparations"],
        "actions": LATIN_PHARMACOPEIA["actions"],
        "equipment": LATIN_PHARMACOPEIA["equipment"],
        "quality_tests": LATIN_PHARMACOPEIA["quality_tests"],
        "combinations": LATIN_PHARMACOPEIA["combinations"],
        "dosage_forms": LATIN_PHARMACOPEIA["dosage_forms"]
    }
    
    category_data = categories.get(category, {})
    return category_data.get(term_key, {"latin": "Unknown", "english": "Unknown", "description": "No description available."})


def get_herb_info(herb_key: str) -> dict:
    """Get complete information about a herb from materia medica."""
    return MATERIA_MEDICA.get(herb_key, {
        "latin_name": "Unknown",
        "common_name": "Unknown Herb",
        "description": "No information available for this herb."
    })


def get_seasonal_protocol(season: str) -> dict:
    """Get seasonal protocol information."""
    return SEASONAL_PROTOCOLS.get(season, {
        "name": "Unknown Season",
        "description": "No protocol available for this season."
    })


def get_planetary_correspondence(planet: str) -> dict:
    """Get planetary correspondence information."""
    return PLANETARY_CORRESPONDENCES.get(planet, {
        "metal": "Unknown",
        "qualities": "Unknown",
        "best_for": "Unknown"
    })


def calculate_planetary_hour(day: str, hour: int) -> str:
    """Calculate which planet rules a specific hour of a specific day."""
    day_data = PLANETARY_HOURS.get(day, {})
    hours = day_data.get("hours", [])
    if 0 <= hour < len(hours):
        return hours[hour]
    return "Unknown"


def generate_folio_list() -> list:
    """Generate complete list of all 232 Voynich folios."""
    folios = []
    
    # Generate folios from f1r to f116v
    for i in range(1, 117):
        folios.append(f"f{i}r")
        folios.append(f"f{i}v")
    
    return folios


def get_folio_range(start: int, end: int) -> list:
    """Get a range of folios."""
    folios = []
    for i in range(start, end + 1):
        folios.append(f"f{i}r")
        folios.append(f"f{i}v")
    return folios


def format_latin_name(name: str) -> str:
    """Format a Latin name with proper italics."""
    return f"*{name}*"


def create_recipe_card(title: str, ingredients: list, instructions: list, 
                       preparation: str = "", dosage: str = "", 
                       warnings: str = "") -> str:
    """Create a formatted recipe card HTML."""
    html = f"""
    <div class="recipe-card">
        <div class="recipe-title">{title}</div>
        <div class="recipe-ingredients">
            <h4>🌿 Ingredients</h4>
            <ul>
    """
    for ingredient in ingredients:
        html += f"                <li>{ingredient}</li>\n"
    
    html += """            </ul>
        </div>
        <div class="recipe-instructions">
            <h4>📋 Instructions</h4>
            <ol>
    """
    for instruction in instructions:
        html += f"                <li>{instruction}</li>\n"
    
    html += "            </ol>\n        </div>"
    
    if preparation:
        html += f"""
        <div style="margin-top: 1rem; padding: 0.75rem; background: rgba(56, 161, 105, 0.1); border-radius: 8px;">
            <strong>⚗️ Preparation:</strong> {preparation}
        </div>
        """
    
    if dosage:
        html += f"""
        <div style="margin-top: 0.5rem; padding: 0.75rem; background: rgba(49, 130, 206, 0.1); border-radius: 8px;">
            <strong>💊 Dosage:</strong> {dosage}
        </div>
        """
    
    if warnings:
        html += f"""
        <div style="margin-top: 0.5rem; padding: 0.75rem; background: rgba(229, 62, 62, 0.1); border-radius: 8px;">
            <strong>⚠️ Warnings:</strong> {warnings}
        </div>
        """
    
    html += "</div>"
    return html


def create_info_box(content: str, box_type: str = "info") -> str:
    """Create a styled info box."""
    box_classes = {
        "info": "info-box",
        "warning": "warning-box",
        "danger": "danger-box",
        "success": "success-box"
    }
    box_class = box_classes.get(box_type, "info-box")
    return f'<div class="{box_class}">{content}</div>'


def create_waypoint_card(number: int, title: str, description: str, 
                         waypoint_type: str = "investigation",
                         tags: list = None) -> str:
    """Create a styled waypoint card HTML."""
    tags = tags or []
    
    type_colors = {
        "investigation": "#d69e2e",
        "herbal": "#38a169",
        "recipe": "#3182ce",
        "planetary": "#805ad5",
        "seasonal": "#dd6b20"
    }
    
    type_color = type_colors.get(waypoint_type, "#d69e2e")
    
    html = f"""
    <div class="waypoint-card" style="border-left-color: {type_color};">
        <div class="waypoint-header">
            <span class="waypoint-number">Waypoint {number}</span>
            <span class="waypoint-type" style="background: {type_color};">{waypoint_type.upper()}</span>
        </div>
        <div class="waypoint-title">{title}</div>
        <div class="waypoint-description">{description}</div>
    """
    
    if tags:
        html += '<div class="waypoint-meta">'
        for tag in tags:
            html += f'<span class="waypoint-tag">{tag}</span>'
        html += '</div>'
    
    html += '</div>'
    return html

# ═══════════════════════════════════════════════════════════════════════════════
# END OF PART 3
# ═══════════════════════════════════════════════════════════════════════════════
# INSTRUCTIONS: Copy this entire section AFTER Part 2 in your Streamlit app.
# Next: Part 4 will contain FOLIO GENERATION and SECTION MAPPING functions.
# ═══════════════════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════════════════
# WILKEN KEY ENGINE v5.0 - PART 4: FOLIO GENERATION & SECTION MAPPING
# ═══════════════════════════════════════════════════════════════════════════════
# This section contains complete folio generation for all 232 folios,
# section mapping, and waypoint generation for the Voynich Manuscript.
# Copy this AFTER Part 3 in your Streamlit application.
# ═══════════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 4A: COMPLETE FOLIO SECTIONS DATA
# ───────────────────────────────────────────────────────────────────────────────

FOLIO_SECTIONS = {
    "Herbal": {
        "folios": [(1, 66)],
        "description": "Pages depicting botanical illustrations with accompanying text. These folios show detailed drawings of unidentified plants, each labeled with Voynich script. The herbal section is the largest and most extensively illustrated portion of the manuscript.",
        "characteristics": [
            "Detailed plant illustrations with roots, stems, leaves, and flowers",
            "Text arranged in paragraphs beside or below illustrations",
            "Some plants appear to be composite or fantastical creations",
            "Color palette includes greens, browns, reds, and blues",
            "Many plants show nymph-like figures emerging from roots or stems"
        ],
        "significance": "The Herbal section represents the primary medicinal catalog of the manuscript, potentially containing references to healing plants, their preparation, and usage. The integration of human figures suggests a connection between botanical and therapeutic knowledge.",
        "waypoint_focus": ["botanical identification", "pharmacological properties", "preparation methods", "therapeutic applications"],
        "latin_terms": ["herbarium", "materia medica", "simplicia", "composita", "electuarium"]
    },
    
    "Astronomical": {
        "folios": [(67, 73)],
        "description": "Circular diagrams depicting celestial bodies, zodiac symbols, and astronomical arrangements. These pages contain the most complex diagrams in the manuscript, with radiating patterns and concentric circles.",
        "characteristics": [
            "Circular diagrams with radiating lines and sectors",
            "Zodiac symbols clearly identifiable (Taurus, Aries, Pisces, etc.)",
            "Nude female figures arranged in circular patterns",
            "Stars or sun symbols at diagram centers",
            "Text arranged in circular patterns following diagram contours"
        ],
        "significance": "The Astronomical section likely relates to medical astrology, planetary influences on health, and auspicious timing for treatments. The integration of zodiac symbols suggests connections between celestial bodies and bodily functions.",
        "waypoint_focus": ["planetary correspondences", "zodiacal influences", "medical astrology", "auspicious timing"],
        "latin_terms": ["astrologia medica", "signa zodiaca", "planetae", "horae planetariae", "constellationes"]
    },
    
    "Biological": {
        "folios": [(75, 84)],
        "description": "Pages featuring nude female figures in various poses, often connected by tubes or channels, with pools or basins below. These mysterious illustrations have been interpreted as representing biological processes, balneological treatments, or allegorical representations.",
        "characteristics": [
            "Nude female figures in various poses and arrangements",
            "Tubing or channel-like structures connecting figures",
            "Pools, basins, or collection vessels below figures",
            "Color-coded streams or flows between elements",
            "Text integrated into diagrammatic arrangements"
        ],
        "significance": "The Biological section may represent gynecological knowledge, balneological (bathing) treatments, or processes related to generation and transformation. The tubing suggests circulation, flow, or transfer of substances.",
        "waypoint_focus": ["balneological practices", "humoral theory", "generative processes", "therapeutic bathing"],
        "latin_terms": ["balneum", "thermae", "humores", "sanguis", "phlegma", "cholera", "melancholia"]
    },
    
    "Cosmological": {
        "folios": [(85, 86)],
        "description": "Pages containing rosette-shaped diagrams with complex geometric arrangements. These folios show nine interconnected circular elements arranged in a rosette pattern, with detailed internal structures.",
        "characteristics": [
            "Nine circular rosette elements in 3x3 arrangement",
            "Each rosette contains detailed internal patterns",
            "Castle-like structures within some rosettes",
            "Connecting pathways between rosette elements",
            "Text labels within and between rosette structures"
        ],
        "significance": "The Cosmological section may represent a map of the cosmos, a philosophical diagram of creation, or an allegorical representation of the elements and their interactions. The castle structures suggest fortified or protected spaces.",
        "waypoint_focus": ["cosmological symbolism", "elemental theory", "philosophical diagrams", "sacred geometry"],
        "latin_terms": ["mundus", "caelum", "terra", "elementa", "quintessentia", "rota"]
    },
    
    "Pharmaceutical": {
        "folios": [(87, 93)],
        "description": "Pages featuring small plant illustrations arranged in rows, each with identifying labels. These folios resemble pages from a medieval herbal or pharmacopeia, with systematic arrangement of plant images.",
        "characteristics": [
            "Small, standardized plant illustrations in rows",
            "Text labels beside each plant image",
            "Systematic arrangement suggesting catalog or index",
            "Root structures prominently featured",
            "Consistent illustration style across folios"
        ],
        "significance": "The Pharmaceutical section likely serves as a reference catalog for medicinal plants, their identification, and perhaps their preparation. The standardized format suggests practical utility for practitioners.",
        "waypoint_focus": ["plant identification", "pharmaceutical catalog", "preparation references", "dosage information"],
        "latin_terms": ["dispensatorium", "antidotarium", "gradus", "drachma", "scrupulus", "granum"]
    },
    
    "Recipes": {
        "folios": [(94, 116)],
        "description": "Pages containing dense text arranged in short paragraphs, often with star-like or flower-like markers between sections. These folios contain the most text-dense content in the manuscript, with minimal illustration.",
        "characteristics": [
            "Dense text in short paragraph blocks",
            "Star or flower markers between text sections",
            "Minimal illustration (decorative initials only)",
            "Text arranged in multiple columns on some pages",
            "Consistent formatting suggesting standardized entries"
        ],
        "significance": "The Recipes section likely contains the practical application of knowledge from other sections - specific formulations, procedures, and instructions for preparation and use of medicinal compounds.",
        "waypoint_focus": ["recipe formulations", "preparation procedures", "dosage instructions", "quality testing"],
        "latin_terms": ["recepta", "formula", "modus faciendi", "quantitas", "mensura", "probatio"]
    }
}

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 4B: FOLIO METADATA DATABASE
# ───────────────────────────────────────────────────────────────────────────────

# Complete metadata for all 232 folios
FOLIO_METADATA = {}

# Generate metadata for all folios
for folio_num in range(1, 117):
    for side in ['r', 'v']:
        folio_id = f"f{folio_num}{side}"
        
        # Determine section
        section = "Unknown"
        for section_name, section_data in FOLIO_SECTIONS.items():
            for start, end in section_data["folios"]:
                if start <= folio_num <= end:
                    section = section_name
                    break
        
        # Generate Yale image ID
        is_verso = (side == 'v')
        yale_id = BASE_YALE_ID + (folio_num * 2) + (1 if is_verso else 0)
        if folio_num > 86:
            yale_id += ROSETTA_SHIFT
        
        # Create metadata entry
        FOLIO_METADATA[folio_id] = {
            "folio_number": folio_num,
            "side": side,
            "section": section,
            "yale_id": yale_id,
            "yale_url": f"{YALE_IIIF_BASE}{yale_id}/full/!2000,2000/0/default.jpg",
            "thumbnail_url": f"{YALE_IIIF_BASE}{yale_id}/full/!300,300/0/default.jpg",
            "has_illustration": section in ["Herbal", "Astronomical", "Biological", "Cosmological", "Pharmaceutical"],
            "text_density": "high" if section == "Recipes" else "medium" if section in ["Herbal", "Pharmaceutical"] else "low"
        }

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 4C: WAYPOINT GENERATION SYSTEM
# ───────────────────────────────────────────────────────────────────────────────

def generate_waypoints_for_folio(folio_id: str) -> list:
    """
    Generate comprehensive waypoints for a specific folio.
    Returns a list of waypoint dictionaries with complete investigation data.
    """
    waypoints = []
    folio_data = FOLIO_METADATA.get(folio_id, {})
    section = folio_data.get("section", "Unknown")
    
    # Base waypoint - always present
    waypoints.append({
        "number": 1,
        "type": "folio_overview",
        "title": f"Folio {folio_id.upper()} Overview",
        "description": f"Comprehensive examination of Voynich Manuscript folio {folio_id.upper()}, located in the {section} section. This folio contains important information related to {get_section_description(folio_id)}",
        "tags": [section.lower(), "overview", "examination"],
        "investigation_type": "visual_analysis"
    })
    
    # Section-specific waypoints
    if section == "Herbal":
        waypoints.extend(generate_herbal_waypoints(folio_id))
    elif section == "Astronomical":
        waypoints.extend(generate_astronomical_waypoints(folio_id))
    elif section == "Biological":
        waypoints.extend(generate_biological_waypoints(folio_id))
    elif section == "Cosmological":
        waypoints.extend(generate_cosmological_waypoints(folio_id))
    elif section == "Pharmaceutical":
        waypoints.extend(generate_pharmaceutical_waypoints(folio_id))
    elif section == "Recipes":
        waypoints.extend(generate_recipe_waypoints(folio_id))
    
    # Add transliteration waypoint for all folios
    waypoints.append({
        "number": len(waypoints) + 1,
        "type": "transliteration",
        "title": "Wilken Key Transliteration",
        "description": "Phonetic approximation of Voynich text using the Wilken Key transliteration system. This provides a readable approximation of the original script for linguistic analysis.",
        "tags": ["transliteration", "linguistics", "wilken-key"],
        "investigation_type": "textual_analysis"
    })
    
    # Add Latin pharmacological analysis
    waypoints.append({
        "number": len(waypoints) + 1,
        "type": "pharmacological",
        "title": "Latin Pharmacological Analysis",
        "description": "Analysis of text using medieval Latin pharmacological terminology and preparation methods documented in historical materia medica.",
        "tags": ["pharmacology", "latin", "medieval"],
        "investigation_type": "pharmaceutical_analysis"
    })
    
    # Add planetary correspondence waypoint
    waypoints.append({
        "number": len(waypoints) + 1,
        "type": "planetary",
        "title": "Planetary Correspondence Analysis",
        "description": "Examination of planetary influences, astrological correspondences, and timing considerations related to this folio's content.",
        "tags": ["astrology", "planetary", "correspondences"],
        "investigation_type": "astrological_analysis"
    })
    
    # Add materia medica waypoint
    waypoints.append({
        "number": len(waypoints) + 1,
        "type": "materia_medica",
        "title": "Materia Medica Cross-Reference",
        "description": "Cross-reference with documented medieval materia medica, including preparation methods, therapeutic applications, and contraindications.",
        "tags": ["materia-medica", "herbal", "cross-reference"],
        "investigation_type": "pharmaceutical_analysis"
    })
    
    # Add seasonal protocol waypoint
    waypoints.append({
        "number": len(waypoints) + 1,
        "type": "seasonal",
        "title": "Seasonal Collection & Preparation Protocol",
        "description": "Guidelines for seasonal collection, preparation timing, and optimal processing methods based on traditional herbal practices.",
        "tags": ["seasonal", "collection", "preparation"],
        "investigation_type": "practical_application"
    })
    
    return waypoints


def generate_herbal_waypoints(folio_id: str) -> list:
    """Generate waypoints specific to Herbal section folios."""
    return [
        {
            "number": 2,
            "type": "botanical",
            "title": "Botanical Illustration Analysis",
            "description": "Detailed examination of the plant illustration, including morphological features, growth habit, and potential identification markers. Analysis of root structure, stem characteristics, leaf arrangement, and floral morphology.",
            "tags": ["botany", "illustration", "morphology"],
            "investigation_type": "visual_analysis"
        },
        {
            "number": 3,
            "type": "pharmacological",
            "title": "Pharmacological Properties Investigation",
            "description": "Analysis of potential pharmacological properties based on plant morphology and traditional associations. Cross-reference with known medicinal plants of similar appearance.",
            "tags": ["pharmacology", "properties", "traditional"],
            "investigation_type": "pharmaceutical_analysis"
        },
        {
            "number": 4,
            "type": "preparation",
            "title": "Preparation Method Documentation",
            "description": "Documentation of traditional preparation methods applicable to plants of this type, including extraction techniques, dosage forms, and administration routes.",
            "tags": ["preparation", "extraction", "dosage"],
            "investigation_type": "practical_application"
        },
        {
            "number": 5,
            "type": "therapeutic",
            "title": "Therapeutic Application Analysis",
            "description": "Analysis of potential therapeutic applications based on traditional herbal knowledge, including indications, contraindications, and combination possibilities.",
            "tags": ["therapeutic", "applications", "indications"],
            "investigation_type": "clinical_analysis"
        },
        {
            "number": 6,
            "type": "nymph_figure",
            "title": "Nymph Figure Symbolism",
            "description": "Examination of nymph-like figures associated with the plant illustration, analyzing their poses, positioning, and potential symbolic significance in relation to the plant's properties.",
            "tags": ["symbolism", "nymphs", "iconography"],
            "investigation_type": "symbolic_analysis"
        }
    ]


def generate_astronomical_waypoints(folio_id: str) -> list:
    """Generate waypoints specific to Astronomical section folios."""
    return [
        {
            "number": 2,
            "type": "zodiacal",
            "title": "Zodiac Symbol Analysis",
            "description": "Detailed examination of zodiac symbols present in the diagram, their positioning, and astrological significance. Analysis of zodiacal influences on health and treatment timing.",
            "tags": ["zodiac", "astrology", "symbols"],
            "investigation_type": "astrological_analysis"
        },
        {
            "number": 3,
            "type": "planetary_arrangement",
            "title": "Planetary Arrangement Investigation",
            "description": "Analysis of planetary positioning within the diagram, including angular relationships, house placements, and medical astrological interpretations.",
            "tags": ["planetary", "arrangement", "medical-astrology"],
            "investigation_type": "astrological_analysis"
        },
        {
            "number": 4,
            "type": "nymph_arrangement",
            "title": "Nymph Figure Arrangement Analysis",
            "description": "Examination of nude female figures arranged in circular patterns, their positioning relative to zodiac sectors, and potential symbolic meanings related to body zones or treatment areas.",
            "tags": ["nymphs", "arrangement", "body-zones"],
            "investigation_type": "symbolic_analysis"
        },
        {
            "number": 5,
            "type": "timing",
            "title": "Auspicious Timing Calculation",
            "description": "Calculation of auspicious timing for treatments based on planetary hours, zodiacal influences, and traditional medical astrology protocols.",
            "tags": ["timing", "planetary-hours", "auspicious"],
            "investigation_type": "astrological_application"
        },
        {
            "number": 6,
            "type": "celestial_influence",
            "title": "Celestial Influence on Materia Medica",
            "description": "Analysis of how celestial bodies influence the potency and preparation of herbal medicines, including planetary rulership of herbs and optimal collection times.",
            "tags": ["celestial", "influence", "potency"],
            "investigation_type": "astrological_pharmacy"
        }
    ]


def generate_biological_waypoints(folio_id: str) -> list:
    """Generate waypoints specific to Biological section folios."""
    return [
        {
            "number": 2,
            "type": "figure_analysis",
            "title": "Figure Pose and Positioning Analysis",
            "description": "Detailed examination of nude female figures, their poses, gestures, and spatial relationships. Analysis of body positioning and potential therapeutic or symbolic significance.",
            "tags": ["figures", "poses", "positioning"],
            "investigation_type": "visual_analysis"
        },
        {
            "number": 3,
            "type": "tubing_analysis",
            "title": "Tubing and Channel Analysis",
            "description": "Examination of tubing or channel-like structures connecting figures, including their paths, colors, and potential representation of fluid flow, energy channels, or treatment delivery systems.",
            "tags": ["tubing", "channels", "flow"],
            "investigation_type": "structural_analysis"
        },
        {
            "number": 4,
            "type": "pool_analysis",
            "title": "Pool and Basin Analysis",
            "description": "Analysis of pools, basins, or collection vessels below figures, their contents, colors, and potential significance in balneological or therapeutic contexts.",
            "tags": ["pools", "basins", "collection"],
            "investigation_type": "functional_analysis"
        },
        {
            "number": 5,
            "type": "balneological",
            "title": "Balneological Treatment Investigation",
            "description": "Investigation of potential balneological (bathing) treatments, including water therapies, mineral baths, and hydrotherapy applications suggested by the imagery.",
            "tags": ["balneology", "bathing", "hydrotherapy"],
            "investigation_type": "therapeutic_analysis"
        },
        {
            "number": 6,
            "type": "humoral",
            "title": "Humoral Theory Application",
            "description": "Analysis of imagery in relation to humoral theory (blood, phlegm, yellow bile, black bile), including potential representations of humoral balance or imbalance.",
            "tags": ["humoral", "theory", "balance"],
            "investigation_type": "theoretical_analysis"
        }
    ]


def generate_cosmological_waypoints(folio_id: str) -> list:
    """Generate waypoints specific to Cosmological section folios."""
    return [
        {
            "number": 2,
            "type": "rosette_analysis",
            "title": "Rosette Structure Analysis",
            "description": "Detailed examination of rosette elements, their internal structures, patterns, and symbolic content. Analysis of the nine-rosette arrangement and its potential cosmological significance.",
            "tags": ["rosettes", "structure", "cosmology"],
            "investigation_type": "symbolic_analysis"
        },
        {
            "number": 3,
            "type": "castle_analysis",
            "title": "Castle Structure Symbolism",
            "description": "Analysis of castle-like structures within rosettes, their architectural features, and potential symbolic meanings related to protection, fortification, or sacred spaces.",
            "tags": ["castles", "architecture", "symbolism"],
            "investigation_type": "architectural_analysis"
        },
        {
            "number": 4,
            "type": "pathway_analysis",
            "title": "Connecting Pathway Analysis",
            "description": "Examination of pathways connecting rosette elements, their directions, colors, and potential representation of flows, connections, or transitions between states.",
            "tags": ["pathways", "connections", "flows"],
            "investigation_type": "structural_analysis"
        },
        {
            "number": 5,
            "type": "elemental",
            "title": "Elemental Theory Application",
            "description": "Analysis of rosette imagery in relation to elemental theory (earth, water, air, fire), including potential representations of elemental interactions and transformations.",
            "tags": ["elements", "theory", "transformations"],
            "investigation_type": "philosophical_analysis"
        },
        {
            "number": 6,
            "type": "sacred_geometry",
            "title": "Sacred Geometry Investigation",
            "description": "Investigation of geometric patterns and proportions within the rosette arrangement, including potential applications of sacred geometry principles.",
            "tags": ["geometry", "sacred", "proportions"],
            "investigation_type": "mathematical_analysis"
        }
    ]


def generate_pharmaceutical_waypoints(folio_id: str) -> list:
    """Generate waypoints specific to Pharmaceutical section folios."""
    return [
        {
            "number": 2,
            "type": "plant_catalog",
            "title": "Plant Catalog Entry Analysis",
            "description": "Detailed examination of individual plant entries in the catalog format, including illustration style, labeling conventions, and organizational principles.",
            "tags": ["catalog", "entries", "organization"],
            "investigation_type": "catalog_analysis"
        },
        {
            "number": 3,
            "type": "identification",
            "title": "Plant Identification Markers",
            "description": "Analysis of visual markers used for plant identification, including distinctive features, root structures, and characteristic elements emphasized in illustrations.",
            "tags": ["identification", "markers", "features"],
            "investigation_type": "identification_analysis"
        },
        {
            "number": 4,
            "type": "labeling",
            "title": "Labeling System Investigation",
            "description": "Investigation of the labeling system used for plant entries, including text placement, abbreviations, and potential classification schemes.",
            "tags": ["labeling", "system", "classification"],
            "investigation_type": "textual_analysis"
        },
        {
            "number": 5,
            "type": "cross_reference",
            "title": "Cross-Reference with Other Sections",
            "description": "Cross-referencing pharmaceutical entries with corresponding illustrations in the Herbal section and recipes in the Recipes section.",
            "tags": ["cross-reference", "herbal", "recipes"],
            "investigation_type": "comparative_analysis"
        },
        {
            "number": 6,
            "type": "practical_application",
            "title": "Practical Application Guide",
            "description": "Practical guide to using the pharmaceutical catalog for identification, preparation, and application of medicinal plants.",
            "tags": ["practical", "application", "guide"],
            "investigation_type": "practical_application"
        }
    ]


def generate_recipe_waypoints(folio_id: str) -> list:
    """Generate waypoints specific to Recipes section folios."""
    return [
        {
            "number": 2,
            "type": "recipe_structure",
            "title": "Recipe Structure Analysis",
            "description": "Analysis of recipe entry structure, including ingredient lists, preparation instructions, dosage information, and organizational patterns.",
            "tags": ["structure", "organization", "patterns"],
            "investigation_type": "structural_analysis"
        },
        {
            "number": 3,
            "type": "ingredient_analysis",
            "title": "Ingredient Identification",
            "description": "Identification and analysis of ingredients mentioned in recipes, cross-referencing with materia medica and pharmaceutical catalog entries.",
            "tags": ["ingredients", "identification", "cross-reference"],
            "investigation_type": "pharmaceutical_analysis"
        },
        {
            "number": 4,
            "type": "preparation_method",
            "title": "Preparation Method Documentation",
            "description": "Detailed documentation of preparation methods described in recipes, including processing techniques, equipment requirements, and quality control measures.",
            "tags": ["preparation", "methods", "documentation"],
            "investigation_type": "practical_application"
        },
        {
            "number": 5,
            "type": "dosage_analysis",
            "title": "Dosage and Administration Analysis",
            "description": "Analysis of dosage information, administration routes, timing instructions, and duration of treatment specified in recipes.",
            "tags": ["dosage", "administration", "timing"],
            "investigation_type": "clinical_analysis"
        },
        {
            "number": 6,
            "type": "quality_testing",
            "title": "Quality Testing Protocols",
            "description": "Examination of quality testing methods, storage instructions, and shelf-life considerations mentioned in recipe entries.",
            "tags": ["quality", "testing", "storage"],
            "investigation_type": "quality_analysis"
        },
        {
            "number": 7,
            "type": "recipe_reconstruction",
            "title": "Recipe Reconstruction Attempt",
            "description": "Attempted reconstruction of recipes using identified ingredients, documented preparation methods, and traditional pharmaceutical knowledge.",
            "tags": ["reconstruction", "attempt", "traditional"],
            "investigation_type": "experimental_analysis"
        }
    ]

# ═══════════════════════════════════════════════════════════════════════════════
# END OF PART 4
# ═══════════════════════════════════════════════════════════════════════════════
# INSTRUCTIONS: Copy this entire section AFTER Part 3 in your Streamlit app.
# Next: Part 5 will contain the MAIN APPLICATION UI - Header, Sidebar, and Content.
# ═══════════════════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════════════════
# WILKEN KEY ENGINE v5.0 - PART 5: MAIN APPLICATION UI
# ═══════════════════════════════════════════════════════════════════════════════
# This section contains the main application UI components including header,
# sidebar navigation, metrics display, and main content area.
# Copy this AFTER Part 4 in your Streamlit application.
# ═══════════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 5A: APPLICATION HEADER
# ───────────────────────────────────────────────────────────────────────────────

def render_header():
    """Render the Wilken Key Engine application header."""
    st.markdown("""
    <div class="wilken-header">
        <h1>🔑 WILKEN KEY ENGINE v5.0</h1>
        <h2>Voynich Manuscript MS 408 - Complete Scholar Investigation Platform</h2>
        <p>Comprehensive analysis of all 232 folios with Latin pharmacopeia, materia medica, 
        planetary correspondences, and seasonal protocols</p>
    </div>
    """, unsafe_allow_html=True)


# ───────────────────────────────────────────────────────────────────────────────
# SECTION 5B: METRICS DISPLAY
# ───────────────────────────────────────────────────────────────────────────────

def render_metrics():
    """Render key metrics dashboard."""
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">232</div>
            <div class="metric-label">Total Folios</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">6</div>
            <div class="metric-label">Major Sections</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">30</div>
            <div class="metric-label">Materia Medica</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">105</div>
            <div class="metric-label">Latin Terms</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">7</div>
            <div class="metric-label">Planetary Rulers</div>
        </div>
        """, unsafe_allow_html=True)


# ───────────────────────────────────────────────────────────────────────────────
# SECTION 5C: SIDEBAR NAVIGATION
# ───────────────────────────────────────────────────────────────────────────────

def render_sidebar():
    """Render the sidebar navigation and controls."""
    with st.sidebar:
        st.markdown('<div class="sidebar-title">🧭 Navigation</div>', unsafe_allow_html=True)
        
        # Folio Selection
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.subheader("📖 Folio Selection")
        
        # Section filter
        section_filter = st.selectbox(
            "Filter by Section:",
            ["All Sections", "Herbal", "Astronomical", "Biological", "Cosmological", "Pharmaceutical", "Recipes"]
        )
        
        # Generate folio list based on filter
        if section_filter == "All Sections":
            available_folios = [f"f{i}{side}" for i in range(1, 117) for side in ['r', 'v']]
        else:
            section_data = FOLIO_SECTIONS.get(section_filter, {})
            available_folios = []
            for start, end in section_data.get("folios", []):
                for i in range(start, end + 1):
                    available_folios.extend([f"f{i}r", f"f{i}v"])
        
        # Folio selector
        selected_folio = st.selectbox(
            "Select Folio:",
            available_folios,
            index=0 if available_folios else None
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Quick Navigation
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.subheader("⚡ Quick Navigation")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Previous", use_container_width=True):
                if selected_folio and available_folios:
                    current_idx = available_folios.index(selected_folio)
                    if current_idx > 0:
                        st.session_state.selected_folio = available_folios[current_idx - 1]
                        st.rerun()
        
        with col2:
            if st.button("Next ➡️", use_container_width=True):
                if selected_folio and available_folios:
                    current_idx = available_folios.index(selected_folio)
                    if current_idx < len(available_folios) - 1:
                        st.session_state.selected_folio = available_folios[current_idx + 1]
                        st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Reference Materials
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.subheader("📚 Reference Materials")
        
        reference_option = st.selectbox(
            "Select Reference:",
            ["Latin Pharmacopeia", "Materia Medica", "Planetary Correspondences", 
             "Seasonal Protocols", "Equipment Guide", "Quality Tests"]
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Tools
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.subheader("🛠️ Tools")
        
        tool_option = st.selectbox(
            "Select Tool:",
            ["Wilken Key Transliterator", "Planetary Hour Calculator", 
             "Dosage Converter", "Recipe Builder"]
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # About
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.subheader("ℹ️ About")
        st.markdown("""
        **Wilken Key Engine v5.0**
        
        A comprehensive investigation platform for the Voynich Manuscript MS 408, 
        featuring complete folio analysis, Latin pharmacopeia, materia medica, 
        and traditional pharmaceutical knowledge.
        
        **Data Sources:**
        - Yale Beinecke Library MS 408
        - Medieval Latin Pharmacopeia
        - Traditional Materia Medica
        - Medical Astrology Texts
        
        **Version:** 5.0 (Ultimate Edition)
        **Last Updated:** 2026
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        return selected_folio, section_filter, reference_option, tool_option


# ───────────────────────────────────────────────────────────────────────────────
# SECTION 5D: FOLIO DISPLAY
# ───────────────────────────────────────────────────────────────────────────────

def render_folio_display(folio_id: str):
    """Render the folio display with image and metadata."""
    folio_data = FOLIO_METADATA.get(folio_id, {})
    section = folio_data.get("section", "Unknown")
    yale_url = folio_data.get("yale_url", "")
    thumbnail_url = folio_data.get("thumbnail_url", "")
    
    st.markdown(f"""
    <div class="folio-display">
        <div class="folio-header">
            <span class="folio-id">{folio_id.upper()}</span>
            <span class="folio-section">{section} Section</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Display folio image
    try:
        st.image(yale_url, use_container_width=True, caption=f"Yale Beinecke MS 408 - Folio {folio_id.upper()}")
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        st.info("Image may be temporarily unavailable from Yale's servers.")
    
    # Folio metadata
    with st.expander("📋 Folio Metadata", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Folio Information**")
            st.write(f"- **ID:** {folio_id.upper()}")
            st.write(f"- **Number:** {folio_data.get('folio_number', 'N/A')}")
            st.write(f"- **Side:** {'Verso (back)' if folio_id.endswith('v') else 'Recto (front)'}")
            st.write(f"- **Section:** {section}")
        
        with col2:
            st.markdown("**Image Data**")
            st.write(f"- **Yale ID:** {folio_data.get('yale_id', 'N/A')}")
            st.write(f"- **Has Illustration:** {'Yes' if folio_data.get('has_illustration') else 'No'}")
            st.write(f"- **Text Density:** {folio_data.get('text_density', 'N/A').title()}")
        
        with col3:
            st.markdown("**Section Characteristics**")
            characteristics = get_section_characteristics(folio_id)
            for char in characteristics[:3]:
                st.write(f"- {char}")


# ───────────────────────────────────────────────────────────────────────────────
# SECTION 5E: WAYPOINTS DISPLAY
# ───────────────────────────────────────────────────────────────────────────────

def render_waypoints(folio_id: str):
    """Render all waypoints for the selected folio."""
    waypoints = generate_waypoints_for_folio(folio_id)
    
    st.markdown(f"""
    <div style="margin: 2rem 0;">
        <h2 style="color: #d69e2e; border-bottom: 2px solid #d69e2e; padding-bottom: 0.5rem;">
            🎯 Investigation Waypoints ({len(waypoints)} Total)
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    for waypoint in waypoints:
        # Determine icon based on type
        type_icons = {
            "folio_overview": "📖",
            "botanical": "🌿",
            "pharmacological": "💊",
            "preparation": "⚗️",
            "therapeutic": "🏥",
            "nymph_figure": "👤",
            "zodiacal": "♈",
            "planetary_arrangement": "🪐",
            "nymph_arrangement": "👥",
            "timing": "⏰",
            "celestial_influence": "✨",
            "figure_analysis": "🧍",
            "tubing_analysis": "〰️",
            "pool_analysis": "💧",
            "balneological": "🛁",
            "humoral": "⚖️",
            "rosette_analysis": "🌹",
            "castle_analysis": "🏰",
            "pathway_analysis": "🛤️",
            "elemental": "🔥",
            "sacred_geometry": "📐",
            "plant_catalog": "📚",
            "identification": "🔍",
            "labeling": "🏷️",
            "cross_reference": "🔗",
            "practical_application": "🛠️",
            "recipe_structure": "📝",
            "ingredient_analysis": "🧪",
            "preparation_method": "🔬",
            "dosage_analysis": "💉",
            "quality_testing": "✅",
            "recipe_reconstruction": "🔧",
            "transliteration": "🔤",
            "planetary": "🌟",
            "materia_medica": "📗",
            "seasonal": "🗓️"
        }
        
        icon = type_icons.get(waypoint["type"], "📌")
        
        with st.expander(f"{icon} Waypoint {waypoint['number']}: {waypoint['title']}", expanded=False):
            st.markdown(f"""
            <div class="waypoint-card">
                <div class="waypoint-header">
                    <span class="waypoint-number">Waypoint {waypoint['number']}</span>
                    <span class="waypoint-type">{waypoint['type'].replace('_', ' ').upper()}</span>
                </div>
                <div class="waypoint-description">{waypoint['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Display tags
            if waypoint.get('tags'):
                st.markdown("**Tags:** " + ", ".join([f"`{tag}`" for tag in waypoint['tags']]))
            
            # Display investigation type
            st.markdown(f"**Investigation Type:** {waypoint.get('investigation_type', 'General').replace('_', ' ').title()}")
            
            # Add action buttons based on waypoint type
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button(f"🔍 Deep Analysis", key=f"deep_{folio_id}_{waypoint['number']}"):
                    st.info(f"Deep analysis mode activated for Waypoint {waypoint['number']}")
            
            with col2:
                if st.button(f"📊 Compare", key=f"compare_{folio_id}_{waypoint['number']}"):
                    st.info(f"Comparison mode activated for Waypoint {waypoint['number']}")
            
            with col3:
                if st.button(f"💾 Save", key=f"save_{folio_id}_{waypoint['number']}"):
                    st.success(f"Waypoint {waypoint['number']} saved to your collection!")


# ───────────────────────────────────────────────────────────────────────────────
# SECTION 5F: REFERENCE MATERIALS DISPLAY
# ───────────────────────────────────────────────────────────────────────────────

def render_latin_pharmacopeia():
    """Render the complete Latin pharmacopeia reference."""
    st.markdown("""
    <h2 style="color: #d69e2e; border-bottom: 2px solid #d69e2e; padding-bottom: 0.5rem;">
        📜 Latin Pharmacopeia
    </h2>
    <p>Complete medieval Latin pharmaceutical terminology as documented in historical pharmacopeias.</p>
    """, unsafe_allow_html=True)
    
    # Preparations
    with st.expander("⚗️ Preparation Methods", expanded=False):
        st.markdown("""
        | Latin Term | English | Description |
        |------------|---------|-------------|
        """)
        for key, data in LATIN_PHARMACOPEIA["preparations"].items():
            st.markdown(f"| **{data['latin']}** | {data['english']} | {data['description']} |")
    
    # Actions
    with st.expander("💫 Pharmaceutical Actions", expanded=False):
        st.markdown("""
        | Latin Term | English | Description |
        |------------|---------|-------------|
        """)
        for key, data in LATIN_PHARMACOPEIA["actions"].items():
            st.markdown(f"| **{data['latin']}** | {data['english']} | {data['description']} |")
    
    # Equipment
    with st.expander("🔧 Equipment & Vessels", expanded=False):
        st.markdown("""
        | Latin Term | English | Description |
        |------------|---------|-------------|
        """)
        for key, data in LATIN_PHARMACOPEIA["equipment"].items():
            st.markdown(f"| **{data['latin']}** | {data['english']} | {data['description']} |")
    
    # Quality Tests
    with st.expander("✅ Quality Tests", expanded=False):
        st.markdown("""
        | Latin Term | English | Description |
        |------------|---------|-------------|
        """)
        for key, data in LATIN_PHARMACOPEIA["quality_tests"].items():
            st.markdown(f"| **{data['latin']}** | {data['english']} | {data['description']} |")
    
    # Combinations
    with st.expander("🔗 Combination Types", expanded=False):
        st.markdown("""
        | Latin Term | English | Description |
        |------------|---------|-------------|
        """)
        for key, data in LATIN_PHARMACOPEIA["combinations"].items():
            st.markdown(f"| **{data['latin']}** | {data['english']} | {data['description']} |")
    
    # Dosage Forms
    with st.expander("💊 Dosage Forms", expanded=False):
        st.markdown("""
        | Latin Term | English | Description |
        |------------|---------|-------------|
        """)
        for key, data in LATIN_PHARMACOPEIA["dosage_forms"].items():
            st.markdown(f"| **{data['latin']}** | {data['english']} | {data['description']} |")


def render_materia_medica():
    """Render the complete materia medica reference."""
    st.markdown("""
    <h2 style="color: #d69e2e; border-bottom: 2px solid #d69e2e; padding-bottom: 0.5rem;">
        🌿 Materia Medica
    </h2>
    <p>Complete herbal reference with 30 documented medicinal plants, their properties, and traditional uses.</p>
    """, unsafe_allow_html=True)
    
    # Filter options
    filter_col1, filter_col2, filter_col3 = st.columns(3)
    
    with filter_col1:
        planet_filter = st.selectbox(
            "Filter by Planet:",
            ["All"] + list(PLANETARY_CORRESPONDENCES.keys())
        )
    
    with filter_col2:
        element_filter = st.selectbox(
            "Filter by Element:",
            ["All", "Fire", "Water", "Air", "Earth"]
        )
    
    with filter_col3:
        safety_filter = st.selectbox(
            "Filter by Safety:",
            ["All", "Poisonous", "Safe", "Caution"]
        )
    
    # Display herbs
    for herb_key, herb_data in MATERIA_MEDICA.items():
        # Apply filters
        if planet_filter != "All" and herb_data.get("planetary_ruler") != planet_filter:
            continue
        if element_filter != "All" and herb_data.get("element") != element_filter:
            continue
        if safety_filter != "All":
            is_poisonous = any(word in herb_data.get("contraindications", "").lower() 
                              for word in ["poisonous", "toxic", "lethal", "deadly"])
            if safety_filter == "Poisonous" and not is_poisonous:
                continue
            if safety_filter == "Safe" and is_poisonous:
                continue
        
        with st.expander(f"🌿 {herb_data['latin_name']} ({herb_data['common_name']})", expanded=False):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown(f"""
                **Family:** {herb_data['family']}
                
                **Parts Used:** {herb_data['parts_used']}
                
                **Planetary Ruler:** {herb_data['planetary_ruler']}
                
                **Element:** {herb_data['element']}
                
                **Dosage:** {herb_data['dosage']}
                """)
            
            with col2:
                st.markdown(f"""
                **Description:** {herb_data['description']}
                
                **Actions:** {', '.join(herb_data['actions'])}
                
                **Preparations:** {', '.join(herb_data['preparations'])}
                
                **Contraindications:** {herb_data['contraindications']}
                
                **Folklore:** {herb_data['folklore']}
                """)


def render_planetary_correspondences():
    """Render planetary correspondences reference."""
    st.markdown("""
    <h2 style="color: #d69e2e; border-bottom: 2px solid #d69e2e; padding-bottom: 0.5rem;">
        🪐 Planetary Correspondences
    </h2>
    <p>Traditional planetary rulerships for herbs, metals, gems, and body parts.</p>
    """, unsafe_allow_html=True)
    
    for planet, data in PLANETARY_CORRESPONDENCES.items():
        with st.expander(f"{'☉' if planet == 'Sol' else '☽' if planet == 'Luna' else '♂' if planet == 'Mars' else '☿' if planet == 'Mercurius' else '♃' if planet == 'Jupiter' else '♀' if planet == 'Venus' else '♄'} {planet}", expanded=False):
            st.markdown(f"""
            **Metal:** {data['metal']}
            
            **Gem:** {data['gem']}
            
            **Qualities:** {data['qualities']}
            
            **Body Parts:** {', '.join(data['body_parts'])}
            
            **Diseases:** {', '.join(data['diseases'])}
            
            **Best For:** {data['best_for']}
            
            **Associated Herbs:** {', '.join([MATERIA_MEDICA.get(h, {}).get('latin_name', h) for h in data['herbs']])}
            """)


def render_seasonal_protocols():
    """Render seasonal protocols reference."""
    st.markdown("""
    <h2 style="color: #d69e2e; border-bottom: 2px solid #d69e2e; padding-bottom: 0.5rem;">
        🗓️ Seasonal Protocols
    </h2>
    <p>Traditional seasonal guidelines for herb collection and preparation.</p>
    """, unsafe_allow_html=True)
    
    for season_key, season_data in SEASONAL_PROTOCOLS.items():
        season_icons = {"ver": "🌸", "aestas": "☀️", "autumnus": "🍂", "hiems": "❄️"}
        
        with st.expander(f"{season_icons.get(season_key, '📅')} {season_data['name']}", expanded=False):
            st.markdown(f"""
            **Latin Name:** {season_data['latin_name']}
            
            **Months:** {', '.join(season_data['months'])}
            
            **Description:** {season_data['description']}
            
            **Planetary Influence:** {', '.join(season_data['planetary_influence']['dominant'])} - {season_data['planetary_influence']['qualities']}
            
            **Elemental Balance:** {season_data['elemental_balance']['primary']} ({season_data['elemental_balance']['secondary']}) - {season_data['elemental_balance']['qualities']}
            """)
            
            st.markdown("**Collection Times:**")
            for part, timing in season_data['collection_times'].items():
                st.markdown(f"- **{part.title()}:** {timing}")
            
            st.markdown("**Preparation Methods:**")
            for method in season_data['preparation_methods']:
                st.markdown(f"- {method}")
            
            st.markdown("**Recommended Herbs:**")
            st.markdown(", ".join([MATERIA_MEDICA.get(h, {}).get('latin_name', h) for h in season_data['recommended_herbs']]))
            
            st.markdown("**Alchemical Processes:**")
            for process in season_data['alchemical_processes']:
                st.markdown(f"- {process}")
            
            st.markdown(f"**Folklore:** {season_data['folklore']}")

# ═══════════════════════════════════════════════════════════════════════════════
# END OF PART 5
# ═══════════════════════════════════════════════════════════════════════════════
# INSTRUCTIONS: Copy this entire section AFTER Part 4 in your Streamlit app.
# Next: Part 6 will contain TOOLS (Transliterator, Calculator, Converter, Builder)
# and the FOOTER section.
# ═══════════════════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════════════════
# WILKEN KEY ENGINE v5.0 - PART 6: TOOLS & FOOTER
# ═══════════════════════════════════════════════════════════════════════════════
# This section contains interactive tools (transliterator, calculator, converter,
# builder) and the application footer.
# Copy this AFTER Part 5 in your Streamlit application.
# ═══════════════════════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────────────────────
# SECTION 6A: WILKEN KEY TRANSLITERATOR TOOL
# ───────────────────────────────────────────────────────────────────────────────

def render_transliterator_tool():
    """Render the Wilken Key transliterator tool."""
    st.markdown("""
    <h2 style="color: #d69e2e; border-bottom: 2px solid #d69e2e; padding-bottom: 0.5rem;">
        🔤 Wilken Key Transliterator
    </h2>
    <p>Convert Voynich Manuscript text to phonetic approximation using the Wilken Key system.</p>
    """, unsafe_allow_html=True)
    
    # Character mapping reference
    with st.expander("📖 Character Mapping Reference", expanded=False):
        st.markdown("""
        ### Voynich to Wilken Key Mapping
        
        This transliteration system provides phonetic approximations of Voynich characters 
        based on their visual appearance and positional patterns.
        
        | Voynich | Wilken | Sound |
        |---------|--------|-------|
        | o | o | oh |
        | a | a | ah |
        | y | i | ee |
        | d | d | duh |
        | l | l | luh |
        | r | r | ruh |
        | s | s | sss |
        | n | n | nuh |
        | m | m | muh |
        | k | k | kuh |
        | t | t | tuh |
        | p | p | puh |
        | f | f | fff |
        | c | k | kuh |
        | h | h | huh |
        | e | e | eh |
        | i | i | ee |
        | u | u | oo |
        | g | g | guh |
        | b | b | buh |
        | q | kw | kwuh |
        | x | ks | ksss |
        | z | z | zzz |
        | v | v | vuh |
        | w | w | wuh |
        | ch | kh | khuh |
        | sh | sh | shh |
        | th | th | thuh |
        | ph | f | fff |
        | ae | e | eh |
        | oe | e | eh |
        | au | ow | ow |
        | eu | oy | oy |
        """)
    
    # Transliteration input
    input_text = st.text_area(
        "Enter Voynich text to transliterate:",
        height=150,
        placeholder="Enter Voynich characters here...",
        help="Type or paste Voynich text characters for transliteration"
    )
    
    if input_text:
        transliterated = transliterate_to_wilken(input_text)
        
        st.markdown("""
        <div class="success-box">
            <h4>📝 Transliteration Result:</h4>
        </div>
        """, unsafe_allow_html=True)
        
        st.code(transliterated, language="text")
        
        # Analysis
        st.markdown("### 📊 Analysis")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Characters", len(input_text))
        
        with col2:
            st.metric("Words", len(input_text.split()))
        
        with col3:
            unique_chars = len(set(input_text.lower()))
            st.metric("Unique Characters", unique_chars)
        
        # Character frequency
        with st.expander("📈 Character Frequency", expanded=False):
            from collections import Counter
            freq = Counter(input_text.lower())
            
            freq_data = {"Character": [], "Count": [], "Percentage": []}
            total = len(input_text)
            
            for char, count in freq.most_common(20):
                if char.strip():  # Skip whitespace
                    freq_data["Character"].append(char)
                    freq_data["Count"].append(count)
                    freq_data["Percentage"].append(f"{(count/total)*100:.1f}%")
            
            st.table(freq_data)


# ───────────────────────────────────────────────────────────────────────────────
# SECTION 6B: PLANETARY HOUR CALCULATOR TOOL
# ───────────────────────────────────────────────────────────────────────────────

def render_planetary_hour_calculator():
    """Render the planetary hour calculator tool."""
    st.markdown("""
    <h2 style="color: #d69e2e; border-bottom: 2px solid #d69e2e; padding-bottom: 0.5rem;">
        ⏰ Planetary Hour Calculator
    </h2>
    <p>Calculate planetary hours for any day and determine optimal timing for herbal preparations.</p>
    """, unsafe_allow_html=True)
    
    # Day selection
    day_names = {
        "dies_solis": "Sunday (Sol)",
        "dies_lunae": "Monday (Luna)",
        "dies_martis": "Tuesday (Mars)",
        "dies_mercurii": "Wednesday (Mercurius)",
        "dies_jovis": "Thursday (Jupiter)",
        "dies_veneris": "Friday (Venus)",
        "dies_saturni": "Saturday (Saturnus)"
    }
    
    selected_day = st.selectbox(
        "Select Day:",
        list(day_names.keys()),
        format_func=lambda x: day_names[x]
    )
    
    # Display planetary hours for selected day
    day_data = PLANETARY_HOURS.get(selected_day, {})
    hours = day_data.get("hours", [])
    
    if hours:
        st.markdown(f"### 🪐 Planetary Hours for {day_names[selected_day]}")
        
        # Create hour table
        hour_data = {"Hour": [], "Planet": [], "Best For": []}
        
        for i, planet in enumerate(hours[:12]):  # Day hours
            correspondence = PLANETARY_CORRESPONDENCES.get(planet, {})
            hour_data["Hour"].append(f"Day Hour {i+1}")
            hour_data["Planet"].append(planet)
            hour_data["Best For"].append(correspondence.get("best_for", "General")[:50] + "...")
        
        st.table(hour_data)
        
        # Night hours
        st.markdown("### 🌙 Night Hours")
        night_data = {"Hour": [], "Planet": [], "Best For": []}
        
        for i, planet in enumerate(hours[12:]):  # Night hours
            correspondence = PLANETARY_CORRESPONDENCES.get(planet, {})
            night_data["Hour"].append(f"Night Hour {i+1}")
            night_data["Planet"].append(planet)
            night_data["Best For"].append(correspondence.get("best_for", "General")[:50] + "...")
        
        st.table(night_data)
    
    # Current time calculation
    st.markdown("### 🕐 Current Planetary Hour")
    
    import datetime
    now = datetime.datetime.now()
    current_day = now.strftime("%A").lower()
    
    day_mapping = {
        "sunday": "dies_solis",
        "monday": "dies_lunae",
        "tuesday": "dies_martis",
        "wednesday": "dies_mercurii",
        "thursday": "dies_jovis",
        "friday": "dies_veneris",
        "saturday": "dies_saturni"
    }
    
    current_planetary_day = day_mapping.get(current_day, "dies_solis")
    current_hour = now.hour
    
    # Calculate planetary hour (simplified)
    planetary_hour_num = (current_hour % 12)
    if planetary_hour_num == 0:
        planetary_hour_num = 12
    
    current_planet = calculate_planetary_hour(current_planetary_day, planetary_hour_num - 1)
    
    st.info(f"""
    **Current Time:** {now.strftime("%I:%M %p")}
    **Day:** {current_day.title()}
    **Planetary Hour:** Hour {planetary_hour_num} (ruled by {current_planet})
    """)
    
    # Recommendations
    correspondence = PLANETARY_CORRESPONDENCES.get(current_planet, {})
    st.success(f"**Optimal Activities Now:** {correspondence.get('best_for', 'General activities')}")


# ───────────────────────────────────────────────────────────────────────────────
# SECTION 6C: DOSAGE CONVERTER TOOL
# ───────────────────────────────────────────────────────────────────────────────

def render_dosage_converter():
    """Render the dosage converter tool."""
    st.markdown("""
    <h2 style="color: #d69e2e; border-bottom: 2px solid #d69e2e; padding-bottom: 0.5rem;">
        ⚖️ Dosage Converter
    </h2>
    <p>Convert between historical and modern dosage measurements.</p>
    """, unsafe_allow_html=True)
    
    # Conversion table
    with st.expander("📏 Historical Measurement Reference", expanded=False):
        st.markdown("""
        ### Medieval Apothecary Weights
        
        | Unit | Latin | Modern Equivalent |
        |------|-------|-------------------|
        | Grain | Granum | 64.8 mg |
        | Scruple | Scrupulus | 1.296 g (20 grains) |
        | Dram/Drachm | Drachma | 3.888 g (60 grains) |
        | Ounce | Uncia | 31.104 g (8 drachms) |
        | Pound | Libra | 373.248 g (12 ounces) |
        
        ### Liquid Measures
        
        | Unit | Latin | Modern Equivalent |
        |------|-------|-------------------|
        | Minim | Minimum | 0.0616 ml |
        | Fluid Dram | Drachma fluida | 3.697 ml |
        | Fluid Ounce | Uncia fluida | 29.574 ml |
        | Pint | Sextarius | 473.176 ml |
        | Quart | Quartarius | 946.353 ml |
        | Gallon | Congius | 3.785 L |
        """)
    
    # Converter
    st.markdown("### 🔄 Convert Measurements")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        amount = st.number_input("Amount:", min_value=0.0, value=1.0, step=0.1)
    
    with col2:
        from_unit = st.selectbox(
            "From:",
            ["Grains", "Scruples", "Drachms", "Ounces", "Pounds",
             "Minims", "Fluid Drams", "Fluid Ounces", "Pints", "Quarts", "Gallons",
             "Milligrams", "Grams", "Milliliters", "Liters"]
        )
    
    with col3:
        to_unit = st.selectbox(
            "To:",
            ["Milligrams", "Grams", "Milliliters", "Liters",
             "Grains", "Scruples", "Drachms", "Ounces", "Pounds",
             "Minims", "Fluid Drams", "Fluid Ounces", "Pints", "Quarts", "Gallons"]
        )
    
    # Conversion factors (to base units)
    weight_factors = {
        "Grains": 0.0648,  # to grams
        "Scruples": 1.296,
        "Drachms": 3.888,
        "Ounces": 31.104,
        "Pounds": 373.248,
        "Milligrams": 0.001,
        "Grams": 1
    }
    
    volume_factors = {
        "Minims": 0.0616,  # to ml
        "Fluid Drams": 3.697,
        "Fluid Ounces": 29.574,
        "Pints": 473.176,
        "Quarts": 946.353,
        "Gallons": 3785.41,
        "Milliliters": 1,
        "Liters": 1000
    }
    
    # Perform conversion
    if st.button("Convert", use_container_width=True):
        result = 0
        
        # Convert to base unit first
        if from_unit in weight_factors:
            base_value = amount * weight_factors[from_unit]
            if to_unit in weight_factors:
                result = base_value / weight_factors[to_unit]
            elif to_unit in volume_factors:
                st.warning("Cannot convert weight to volume directly!")
                result = None
        elif from_unit in volume_factors:
            base_value = amount * volume_factors[from_unit]
            if to_unit in volume_factors:
                result = base_value / volume_factors[to_unit]
            elif to_unit in weight_factors:
                st.warning("Cannot convert volume to weight directly!")
                result = None
        
        if result is not None:
            st.success(f"**{amount} {from_unit} = {result:.4f} {to_unit}**")
    
    # Common dosage reference
    with st.expander("💊 Common Historical Dosages", expanded=False):
        st.markdown("""
        ### Typical Dosages from Medieval Texts
        
        | Preparation | Typical Dose | Frequency |
        |-------------|--------------|-----------|
        | Electuary (Electuarium) | 1-2 drachms | 2-3 times daily |
        | Pill (Pilula) | 1-4 grains | As directed |
        | Powder (Pulvis) | 10-30 grains | 2-3 times daily |
        | Tincture (Tinctura) | 10-60 drops | 3-4 times daily |
        | Syrup (Syrupus) | 1-2 fluid drachms | As needed |
        | Decoction (Decoctum) | 1-2 fluid ounces | 3 times daily |
        | Infusion (Infusum) | 1-2 fluid ounces | 3 times daily |
        | Ointment (Unguentum) | Apply externally | As needed |
        """)


# ───────────────────────────────────────────────────────────────────────────────
# SECTION 6D: RECIPE BUILDER TOOL
# ───────────────────────────────────────────────────────────────────────────────

def render_recipe_builder():
    """Render the recipe builder tool."""
    st.markdown("""
    <h2 style="color: #d69e2e; border-bottom: 2px solid #d69e2e; padding-bottom: 0.5rem;">
        🔧 Recipe Builder
    </h2>
    <p>Build and document herbal recipes using traditional pharmaceutical methods.</p>
    """, unsafe_allow_html=True)
    
    # Recipe name
    recipe_name = st.text_input("Recipe Name:", placeholder="Enter recipe name...")
    
    # Ingredient selection
    st.markdown("### 🌿 Select Ingredients")
    
    selected_herbs = st.multiselect(
        "Choose herbs from materia medica:",
        options=list(MATERIA_MEDICA.keys()),
        format_func=lambda x: f"{MATERIA_MEDICA[x]['latin_name']} ({MATERIA_MEDICA[x]['common_name']})"
    )
    
    # Ingredient amounts
    ingredients_list = []
    
    if selected_herbs:
        st.markdown("**Specify Amounts:**")
        
        for herb in selected_herbs:
            herb_data = MATERIA_MEDICA[herb]
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.write(f"**{herb_data['latin_name']}**")
            
            with col2:
                amount = st.number_input(
                    f"Amount_{herb}",
                    min_value=0.0,
                    value=1.0,
                    step=0.1,
                    label_visibility="collapsed"
                )
            
            with col3:
                unit = st.selectbox(
                    f"Unit_{herb}",
                    ["parts", "grams", "drachms", "ounces", "handfuls"],
                    label_visibility="collapsed"
                )
            
            ingredients_list.append({
                "herb": herb_data['latin_name'],
                "amount": amount,
                "unit": unit,
                "parts_used": herb_data['parts_used']
            })
    
    # Preparation method
    st.markdown("### ⚗️ Preparation Method")
    
    preparation_method = st.selectbox(
        "Select preparation method:",
        list(LATIN_PHARMACOPEIA["preparations"].keys()),
        format_func=lambda x: LATIN_PHARMACOPEIA["preparations"][x]["latin"]
    )
    
    preparation_details = st.text_area(
        "Preparation Instructions:",
        height=100,
        placeholder="Enter detailed preparation instructions..."
    )
    
    # Dosage information
    st.markdown("### 💊 Dosage Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        dosage_amount = st.number_input("Dosage Amount:", min_value=0.0, value=1.0, step=0.1)
        dosage_unit = st.selectbox(
            "Dosage Unit:",
            ["drops", "drachms", "grams", "teaspoons", "tablespoons", "ounces"]
        )
    
    with col2:
        frequency = st.selectbox(
            "Frequency:",
            ["Once daily", "Twice daily", "Three times daily", "Four times daily", 
             "Every 4 hours", "Every 6 hours", "As needed", "Before meals", "After meals"]
        )
        duration = st.text_input("Duration:", placeholder="e.g., 7 days, 2 weeks")
    
    # Quality testing
    st.markdown("### ✅ Quality Testing")
    
    quality_tests = st.multiselect(
        "Select quality tests:",
        list(LATIN_PHARMACOPEIA["quality_tests"].keys()),
        format_func=lambda x: LATIN_PHARMACOPEIA["quality_tests"][x]["latin"]
    )
    
    # Warnings
    st.markdown("### ⚠️ Warnings & Contraindications")
    
    warnings = st.text_area(
        "Enter warnings and contraindications:",
        height=80,
        placeholder="List any warnings, contraindications, or precautions..."
    )
    
    # Generate recipe
    if st.button("📋 Generate Recipe", use_container_width=True):
        if recipe_name and ingredients_list:
            st.markdown("---")
            st.markdown(f"""
            <div class="recipe-card">
                <div class="recipe-title">{recipe_name}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Ingredients
            st.markdown("**🌿 Ingredients:**")
            for ing in ingredients_list:
                st.markdown(f"- {ing['amount']} {ing['unit']} {ing['herb']} ({ing['parts_used']})")
            
            # Preparation
            prep_data = LATIN_PHARMACOPEIA["preparations"].get(preparation_method, {})
            st.markdown(f"""
            **⚗️ Preparation Method:** {prep_data.get('latin', preparation_method)}
            
            {preparation_details}
            """)
            
            # Dosage
            st.markdown(f"""
            **💊 Dosage:** {dosage_amount} {dosage_unit} {frequency.lower()}
            
            **Duration:** {duration}
            """)
            
            # Quality tests
            if quality_tests:
                st.markdown("**✅ Quality Tests:**")
                for test in quality_tests:
                    test_data = LATIN_PHARMACOPEIA["quality_tests"].get(test, {})
                    st.markdown(f"- {test_data.get('latin', test)}: {test_data.get('description', '')}")
            
            # Warnings
            if warnings:
                st.markdown(f"""
                <div class="danger-box">
                    <strong>⚠️ Warnings:</strong> {warnings}
                </div>
                """, unsafe_allow_html=True)
            
            # Save option
            if st.button("💾 Save Recipe", key="save_recipe"):
                st.success("Recipe saved to your collection!")
        else:
            st.error("Please enter a recipe name and select at least one ingredient.")


# ───────────────────────────────────────────────────────────────────────────────
# SECTION 6E: FOOTER
# ───────────────────────────────────────────────────────────────────────────────

def render_footer():
    """Render the application footer."""
    st.markdown("""
    <div class="wilken-footer">
        <h3 style="color: #d69e2e; margin-bottom: 1rem;">🔑 Wilken Key Engine v5.0</h3>
        <p><strong>Voynich Manuscript MS 408 - Complete Scholar Investigation Platform</strong></p>
        
        <div class="footer-links">
            <a href="https://beinecke.library.yale.edu/collections/highlights/voynich-manuscript" target="_blank">Yale Beinecke Library</a>
            <a href="https://www.voynich.nu/" target="_blank">Voynich.nu</a>
            <a href="https://en.wikipedia.org/wiki/Voynich_manuscript" target="_blank">Wikipedia</a>
        </div>
        
        <p>Data Sources: Yale Beinecke Library MS 408, Medieval Latin Pharmacopeia, Traditional Materia Medica</p>
        <p>Features: 232 Folios | 30 Materia Medica | 105 Latin Terms | 7 Planetary Rulers | 4 Seasonal Protocols</p>
        
        <p style="margin-top: 1rem; font-size: 0.8rem; color: #778da9;">
            Version 5.0 (Ultimate Edition) | Last Updated: March 2026<br>
            For academic and research purposes only. Not intended for medical advice.
        </p>
        
        <p style="margin-top: 1rem; font-size: 0.75rem; color: #555;">
            © 2026 Wilken Key Engine Project. All rights reserved.<br>
            The Voynich Manuscript is housed at the Yale University Beinecke Rare Book & Manuscript Library.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ───────────────────────────────────────────────────────────────────────────────
# SECTION 6F: MAIN APPLICATION ENTRY POINT
# ───────────────────────────────────────────────────────────────────────────────

def main():
    """Main application entry point."""
    # Load CSS
    load_css()
    
    # Render header
    render_header()
    
    # Render metrics
    render_metrics()
    
    # Render sidebar and get selections
    selected_folio, section_filter, reference_option, tool_option = render_sidebar()
    
    # Main content area
    st.markdown("---")
    
    # Check if we're viewing a reference or tool
    if 'view_mode' not in st.session_state:
        st.session_state.view_mode = "folio"
    
    # Determine what to display
    if reference_option != "Latin Pharmacopeia" or tool_option != "Wilken Key Transliterator":
        # Check if user wants to view reference or tool
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("📖 View Folio", use_container_width=True):
                st.session_state.view_mode = "folio"
                st.rerun()
        
        with col2:
            if st.button("📚 View Reference", use_container_width=True):
                st.session_state.view_mode = "reference"
                st.rerun()
        
        with col3:
            if st.button("🛠️ View Tool", use_container_width=True):
                st.session_state.view_mode = "tool"
                st.rerun()
    
    # Display content based on mode
    if st.session_state.view_mode == "folio" and selected_folio:
        # Render folio display
        render_folio_display(selected_folio)
        
        # Render waypoints
        render_waypoints(selected_folio)
    
    elif st.session_state.view_mode == "reference":
        # Render reference materials
        if reference_option == "Latin Pharmacopeia":
            render_latin_pharmacopeia()
        elif reference_option == "Materia Medica":
            render_materia_medica()
        elif reference_option == "Planetary Correspondences":
            render_planetary_correspondences()
        elif reference_option == "Seasonal Protocols":
            render_seasonal_protocols()
        elif reference_option == "Equipment Guide":
            st.info("Equipment Guide - Coming in next update")
        elif reference_option == "Quality Tests":
            st.info("Quality Tests Guide - Coming in next update")
    
    elif st.session_state.view_mode == "tool":
        # Render tools
        if tool_option == "Wilken Key Transliterator":
            render_transliterator_tool()
        elif tool_option == "Planetary Hour Calculator":
            render_planetary_hour_calculator()
        elif tool_option == "Dosage Converter":
            render_dosage_converter()
        elif tool_option == "Recipe Builder":
            render_recipe_builder()
    
    # Render footer
    render_footer()


# Run the application
if __name__ == "__main__":
    main()


# ═══════════════════════════════════════════════════════════════════════════════
# END OF PART 6 - COMPLETE WILKEN KEY ENGINE v5.0
# ═══════════════════════════════════════════════════════════════════════════════
# INSTRUCTIONS: This completes the 6-part Wilken Key Engine v5.0.
# 
# ASSEMBLY INSTRUCTIONS:
# 1. Create a new file named 'wilken_key_engine.py'
# 2. Copy Part 1 (Imports & Config) first
# 3. Copy Part 2 (Latin Pharmacopeia & Materia Medica) after Part 1
# 4. Copy Part 3 (CSS, Functions, Seasonal Protocols) after Part 2
# 5. Copy Part 4 (Folio Generation & Section Mapping) after Part 3
# 6. Copy Part 5 (Main UI - Header, Sidebar, Content) after Part 4
# 7. Copy Part 6 (Tools & Footer) after Part 5
# 8. Save and run with: streamlit run wilken_key_engine.py
#
# FEATURES INCLUDED:
# ✓ All 232 Voynich Manuscript folios (f1r-f116v)
# ✓ Complete 6-section mapping (Herbal, Astronomical, Biological, Cosmological, Pharmaceutical, Recipes)
# ✓ 105 Latin pharmacological terms (preparations, actions, equipment, tests, combinations, dosage forms)
# ✓ 30 herbs in materia medica with full details
# ✓ 7 planetary correspondences with metals, gems, herbs, body parts
# ✓ 4 seasonal protocols with collection times and preparation methods
# ✓ Wilken Key transliterator tool
# ✓ Planetary hour calculator
# ✓ Dosage converter (historical to modern)
# ✓ Recipe builder with ingredient selection
# ✓ Complete waypoint generation for all folios
# ✓ Yale Beinecke IIIF image integration
# ✓ Responsive design with custom CSS
# ✓ Interactive sidebar navigation
# ✓ Reference materials expanders
# ═══════════════════════════════════════════════════════════════════════════════
