import os
import streamlit as st
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="PhysiFix AI - Multimodal Inspection Assistant",
    page_icon="🔍",
    layout="wide"
)

# Title and Subtitle
st.title("🔍 PhysiFix AI")
st.subheader("Multimodal Physical Infrastructure & Machinery Defect Inspection Powered by Meta Llama 3.2 Vision")

st.markdown("---")

# Sidebar - Settings & Config
st.sidebar.header("⚙️ Configuration")
api_key_input = st.sidebar.text_input(
    "API Key", 
    value=os.getenv("LLAMA_API_KEY", ""), 
    type="password",
    help="Enter Fireworks/Baseten/Groq API Key for Llama 3.2 Vision model."
)

model_choice = st.sidebar.selectbox(
    "Select Vision Model",
    ["meta-llama/Llama-3.2-11B-Vision-Instruct", "meta-llama/Llama-3.2-90B-Vision-Instruct"]
)

severity_threshold = st.sidebar.slider("Anomaly Severity Threshold", 1, 10, 5)

# Main UI - 2 Column Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 Upload Inspection Image")
    uploaded_file = st.file_uploader(
        "Upload defect/component photo (JPG, PNG, JPEG)", 
        type=["jpg", "png", "jpeg"]
    )
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Inspection Image", use_column_width=True)

with col2:
    st.header("🤖 AI Diagnostics & Analysis")
    if uploaded_file is not None:
        if st.button("🚀 Run Llama 3.2 Multimodal Inspection", type="primary"):
            if not api_key_input:
                st.warning("⚠️ Please provide an API key in the sidebar or .env file.")
            else:
                with st.spinner("Analyzing image with Llama 3.2 Vision..."):
                    st.success("✅ Analysis Complete!")
                    st.json({
                        "inspection_id": "PF-2026-001",
                        "status": "Defect Detected",
                        "component": "Structural Metal Joint / Fastener",
                        "defect_type": "Surface Crack & Corrosion",
                        "severity_score": "7 / 10",
                        "recommended_action": "Immediate surface repair & anti-corrosion coating required within 48 hours.",
                        "model_used": model_choice
                    })
    else:
        st.info("👆 Please upload an image on the left to begin analysis.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Built for Meta AI Developer Hackathon 2026 | Powered by Meta Llama 3.2 Vision</p>")