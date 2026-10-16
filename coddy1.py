import streamlit as st

st.set_page_config(page_title="Graduate Cold Email Generator", page_icon="🎓", layout="wide")

st.title("🎓 Graduate Cold Email Generator System")
st.subheader("Tailored for Ruth Okeniyi | Civil & Structural Engineering")

# Static, locked CV blocks
LOCKED_BACKGROUND_1 = (
    "I graduated with a First-Class BSc in Civil & Environmental Engineering from the University of Lagos, Nigeria. "
    "My final-year project investigated this exact type of matrix solution, evaluating the structural performance "
    "of concrete blocks incorporating periwinkle shells and Konkreto PC-896. Through this work, I gained hands-on "
    "experience with alternative aggregate characterization, mix optimization, and hardened state mechanics. "
    "By pairing a hypersuperplasticizer with parallel testing across variable cement brands (BUA vs. Superset), "
    "I successfully leveraged the shell's water-retaining properties to densify the bond zone and achieve an "
    "optimal 28-day compressive strength of 68 MPa."
)

LOCKED_BACKGROUND_2 = (
    "Because my research involved alternative aggregate mechanics, and I have since expanded into Python-based "
    "concrete crack detection and industrial Non-Destructive Testing (NDT), your work on advanced concrete matrices "
    "and automated damage monitoring is particularly interesting to me. I am highly driven to apply my structural "
    "analysis and computer vision background to help model, test, and monitor new sustainable concrete "
    "configurations during graduate training."
)

CLOSING_TEXT = (
    "I wanted to ask if you might be accepting research based MASc students for upcoming intakes. "
    "I have attached my CV, first-degree certificate, academic transcript, and GRE scores for your review. "
    "I am available for a virtual meeting or further discussion at your convenience to explore how my skills "
    "can contribute to your team.\n\n"
    "Thank you very much for your time and consideration.\n\n"
    "Kind regards,\n"
    "Ruth Okeniyi"
)

col1, col2 = st.columns([1, 1])

with col1:
    st.header("📝 Input Professor & Paper Data")
    prof_name = st.text_input("Professor's Last Name", value="Banthia")
    
    big_question = st.text_area(
        "Step 2: Big Question / Hook",
        value="To what extent can irregular, multi-phase biogenic waste aggregates be integrated into advanced fiber-reinforced composites without disrupting the early-age workability and the uniform network required to control restrained shrinkage cracking?"
    )
    
    proposed_solution = st.text_input(
        "Step 3: Proposed Solution Blueprint",
        value="combine alternative aggregate grading frameworks with advanced multi-objective optimization algorithms to accurately balance material variations and fresh-state parameters"
    )
    
    paper_1_title = st.text_input("Paper 1 Title", value="Recycling Scrap Tire-Derived Fibers in Concrete")
    paper_1_finding = st.text_area("Paper 1 Core Finding", value="value-added reinforcements from scrap tire by-products can achieve up to a 97% reduction in restrained shrinkage cracking under severe environmental exposure")
    
    core_theme = st.text_input("Core Connection Theme (e.g., durability, sustainability)", value="material optimization and sustainability")
    
    paper_2_title = st.text_input("Paper 2 Title", value="Incorporating fairness into mixture design and material procurement for ultra-high-performance concrete")
    paper_2_finding = st.text_area("Paper 2 Core Finding", value="utilizes prediction-optimization frameworks to account for raw material variations, local availability constraints, and environmental footprints")

with col2:
    st.header("📋 Generated Cold Email Output")
    
    # Constructing the email text string
    email_body = (
        f"Dear Prof. {prof_name},\n\n"
        f"{big_question}\n\n"
        f"After reading your research works, I think a viable solution is to {proposed_solution}. "
        f"Specifically, your paper on '{paper_1_title}' stands out for demonstrating that {paper_1_finding}. "
        f"This focus on {core_theme} connects deeply with your study on '{paper_2_title}', "
        f"which successfully {paper_2_finding}.\n\n"
        f"{LOCKED_BACKGROUND_1}\n\n"
        f"{LOCKED_BACKGROUND_2}\n\n"
        f"{CLOSING_TEXT}"
    )
    
    st.text_area("Copy your email text below:", value=email_body, height=600)
    st.success("✨ Email generated successfully! Keep your CV, Transcripts, and GRE documents attached before hitting send.")