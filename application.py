import streamlit as st
import anthropic
import pandas as pd

# Set your Claude API key here
client = anthropic.Anthropic(api_key="sk-ApiKey")

st.set_page_config(page_title="Viral Post Generator", layout="centered")
st.title("Viral Post Generator")
st.markdown("Generate viral tweets and LinkedIn posts based on your ideas, voice, and real-world inspiration.")

# User input: story or idea
idea = st.text_area("💡 What's your story, idea, or script?")

# Select voice/persona
persona = st.selectbox("🎭 Choose your voice/persona", [
    "Funny and insightful",
    "Professional and motivational",
    "Bold and controversial",
    "Warm and personal"
])

# Optional: past posts/scripts
scripts = st.text_area("📜 Paste past scripts/posts (optional, improves consistency)")

# Optional: upload viral tweet inspiration
uploaded_file = st.file_uploader("📁 Upload a CSV of viral tweets (optional)", type="csv")

# Store tweets if uploaded
tweet_inspo_text = ""
if uploaded_file:
    tweet_df = pd.read_csv(uploaded_file)
    st.markdown("### 📈 Uploaded Tweet Inspiration")
    st.dataframe(tweet_df)

    tweet_inspo_text = "\n".join(tweet_df["Tweet"].astype(str).tolist())
    scripts += f"\n\nHere are some recent viral tweets to match tone:\n{tweet_inspo_text}"

# Button to generate viral posts
if st.button("🚀 Generate Viral Posts"):
    if not idea:
        st.warning("Please enter an idea or story to generate posts.")
    else:
        with st.spinner("Talking to Claude..."):
            # Build prompt for Claude
            context = f"Persona: {persona}\n"
            if scripts:
                context += f"\nMy style:\n{scripts}\n"

            prompt = f"""
You are a viral content strategist and ghostwriter.

{context}

The user wants to generate social media content for the following idea:
\"\"\"{idea}\"\"\"

Generate:
- 5 short, high-impact Twitter posts
- 5 thoughtful, professional LinkedIn posts

Each post should:
- Match the selected persona
- Be platform-appropriate
- Include a virality score (1–10) based on potential reach and engagement

Format:
Platform: Twitter
1. "Post text"
   Virality Score: x/10

Platform: LinkedIn
1. "Post text"
   Virality Score: x/10
"""

            try:
                response = client.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=1200,
                    temperature=0.9,
                    messages=[{"role": "user", "content": prompt}]
                )

                output = response.content[0].text
                st.markdown("## 🧠 Generated Viral Posts")
                st.write(output)

            except Exception as e:
                st.error(f"Error talking to Claude: {e}")
