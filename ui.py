import streamlit as st
import google.generativeai as genai

# Base class to load the model
class AI_Model:
    def getmodel(self):
        Google_API_KEY = st.secrets["GOOGLE_API_KEY"]  # Use Streamlit secrets for API keys
        try:
            genai.configure(api_key=Google_API_KEY)
            model = genai.GenerativeModel("gemini-1.5-flash")
            return model
        except Exception as e:
            st.error(f"❌ Error loading model: {e}")
            return None

# Career guidance class
class Career_guide(AI_Model):
    def __init__(self):
        st.title("🎯 Career Guidance App")
        st.write("Welcome! Fill out the form below to get started.")
        self.get_user_input()

    def get_user_input(self):
        self.name = st.text_input("Enter your name")
        self.interest = st.text_input("Enter your interest")
        self.skills = st.text_input("Enter your skills")
        self.education = st.text_input("Enter your education")

        if self.name and self.interest and self.skills and self.education:
            career_options = [
                "Software Engineer", "Data Scientist", "Product Manager",
                "UX Designer", "Business Analyst", "Marketing Specialist",
                "Sales Representative"
            ]

            career_choice = st.selectbox("Choose a career path", career_options)
            if st.button("Suggest Career Path"):
                self.suggest_career_path(career_choice)

            st.markdown("---")
            if st.button("Suggest Certifications"):
                self.get_certification()

            if st.button("Suggest Job Opportunities"):
                self.get_job_opportunities()

            if st.button("Suggest Additional Skills"):
                self.get_skills()

            if st.button("Suggest Further Education"):
                self.get_education()

    def suggest_career_path(self, career_interest):
        model = super().getmodel()
        if not model:
            return
        prompt = f"""Suggest a career path for someone with:
Interest: {career_interest}
Skills: {self.skills}
Education: {self.education}
Career Path:"""
        try:
            response = model.generate_content(prompt)
            st.success("✅ Career suggestions:")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")

    def get_certification(self):
        model = super().getmodel()
        if not model:
            return
        prompt = f"Suggest some certifications for someone interested in {self.interest}."
        try:
            response = model.generate_content(prompt)
            st.success("✅ Certification suggestions:")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")

    def get_job_opportunities(self):
        model = super().getmodel()
        if not model:
            return
        prompt = f"Suggest some job opportunities for someone interested in {self.interest}."
        try:
            response = model.generate_content(prompt)
            st.success("✅ Job opportunities:")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")

    def get_skills(self):
        model = super().getmodel()
        if not model:
            return
        prompt = f"Suggest some additional skills for someone with {self.skills}."
        try:
            response = model.generate_content(prompt)
            st.success("✅ Skill suggestions:")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")

    def get_education(self):
        model = super().getmodel()
        if not model:
            return
        prompt = f"Suggest further education for someone with {self.education} background."
        try:
            response = model.generate_content(prompt)
            st.success("✅ Education suggestions:")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Run the app
if __name__ == "__main__":
    Career_guide()
