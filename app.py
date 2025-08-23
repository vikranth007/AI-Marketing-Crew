import streamlit as st
import os
from datetime import datetime
from crewai import LLM
from blog_marketing_crew import TheMarketingCrew  # 👈 import your crew class file

# --- Streamlit UI ---
st.set_page_config(page_title="AI Marketing Crew", layout="wide")
st.title("🤖 AI Marketing Crew (CrewAI + Streamlit)")

# --- Manual Gemini API Key Input ---
gemini_key = st.text_input("🔑 Enter your Gemini API Key:", type="password")

if gemini_key:
    os.environ["GEMINI_API_KEY"] = gemini_key  # set it for CrewAI
    st.success("Gemini API Key set successfully ✅")
else:
    st.warning("Please enter your Gemini API Key to continue.")

# --- User Inputs for Marketing Crew ---
st.header("📌 Product Details")
product_name = st.text_input("Product Name", "AI Powered Excel Automation Tool")
target_audience = st.text_input("Target Audience", "Small and Medium Enterprises (SMEs)")
product_description = st.text_area("Product Description", "A tool that automates repetitive tasks in Excel using AI, saving time and reducing errors.")
budget = st.text_input("Marketing Budget", "Rs. 50,000")

if st.button("🚀 Run Marketing Crew") and gemini_key:
    with st.spinner("Running Marketing Crew... ⏳"):
        try:
            inputs = {
                "product_name": product_name,
                "target_audience": target_audience,
                "product_description": product_description,
                "budget": budget,
                "current_date": datetime.now().strftime("%Y-%m-%d"),
            }
            crew = TheMarketingCrew()
            result = crew.marketingcrew().kickoff(inputs=inputs)
            st.success("✅ Marketing Crew finished!")
            st.subheader("📢 Crew Output")
            st.write(result)
        except Exception as e:
            st.error(f"❌ Error running crew: {e}")
