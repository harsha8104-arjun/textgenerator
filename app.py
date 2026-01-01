import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="✨ AI Text Generator",
    page_icon="🤖",
    layout="centered"
)

# Title and description
st.title("🤖 AI Text Generator")
st.markdown(
    """
    Generate text using an AI language model (GPT-2).  
    Type a prompt, adjust settings, and click **Generate**.
    """
)

# Sidebar settings
st.sidebar.header("⚙️ Generation Settings")

max_length = st.sidebar.slider(
    "Max Length",
    min_value=20,
    max_value=200,
    value=60,
    step=10
)

temperature = st.sidebar.slider(
    "Creativity (Temperature)",
    min_value=0.1,
    max_value=1.5,
    value=0.9,
    step=0.1
)

# Load model once (cached)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# Main input area
st.subheader("📝 Enter your prompt")
prompt = st.text_area(
    "Your text prompt",
    placeholder="Example: Artificial intelligence is changing the world because...",
    height=120
)

# Generate button
if st.button("✨ Generate Text", use_container_width=True):
    if not prompt.strip():
        st.warning("⚠️ Please enter a prompt first.")
    else:
        with st.spinner("Generating text..."):
            result = generator(
                prompt,
                max_length=max_length,
                temperature=temperature,
                do_sample=True
            )

        st.subheader("📄 Generated Output")
        st.success(result[0]["generated_text"])
