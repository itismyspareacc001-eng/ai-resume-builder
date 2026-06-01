# ==========================================================
# AI RESUME BUILDER
# Day 16 - Topic 3
# Streamlit + Gemini
# ==========================================================

import streamlit as st
import google.generativeai as genai

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="📄",
    layout="wide"
)

# ==========================================================
# GEMINI CONFIGURATION
# ==========================================================

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# ==========================================================
# SESSION STATE
# ==========================================================

if "generated_resume" not in st.session_state:
    st.session_state.generated_resume = ""

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("📄 AI Resume Builder")

st.caption(
    "Generate ATS-Friendly Professional Resumes Using Gemini AI"
)

st.markdown("---")

# ==========================================================
# PERSONAL INFORMATION
# ==========================================================

st.header("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Full Name")
    email = st.text_input("Email")

with col2:
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn Profile")

github = st.text_input("GitHub Profile")

# ==========================================================
# CAREER OBJECTIVE
# ==========================================================

st.header("🎯 Career Objective")

objective = st.text_area(
    "Career Objective",
    height=120
)

# ==========================================================
# EDUCATION
# ==========================================================

st.header("🎓 Education")

education = st.text_area(
    "Education Details",
    height=150
)

# ==========================================================
# SKILLS
# ==========================================================

st.header("💻 Technical Skills")

skills = st.text_area(
    "Skills (comma separated)",
    height=120
)

# ==========================================================
# INTERNSHIPS
# ==========================================================

st.header("🏢 Internships")

internships = st.text_area(
    "Internship Details",
    height=150
)

# ==========================================================
# PROJECTS
# ==========================================================

st.header("🚀 Projects")

projects = st.text_area(
    "Project Details",
    height=200
)

# ==========================================================
# CERTIFICATIONS
# ==========================================================

st.header("🏆 Certifications")

certifications = st.text_area(
    "Certification Details",
    height=120
)

# ==========================================================
# ACHIEVEMENTS
# ==========================================================

st.header("🥇 Achievements")

achievements = st.text_area(
    "Achievement Details",
    height=120
)

# ==========================================================
# TEMPLATE SELECTION
# ==========================================================

st.header("🎨 Resume Template")

template = st.selectbox(
    "Select Template",
    [
        "Student Fresher",
        "Modern Professional",
        "Experienced Professional"
    ]
)

# ==========================================================
# GENERATE BUTTON
# ==========================================================

generate_button = st.button(
    "🚀 Generate Resume",
    use_container_width=True
)

# ==========================================================
# RESUME GENERATION
# ==========================================================

if generate_button:

    # Basic Validation

    if not name.strip():

        st.error(
            "Please enter your name."
        )

    else:

        with st.spinner(
            "Generating Professional Resume..."
        ):

            try:

                # ======================================
                # PROMPT ENGINEERING
                # ======================================

                prompt = f"""
You are a professional resume writer.

Create an ATS-friendly resume.

Template:
{template}

Candidate Information

Name:
{name}

Email:
{email}

Phone:
{phone}

LinkedIn:
{linkedin}

GitHub:
{github}

Career Objective:
{objective}

Education:
{education}

Technical Skills:
{skills}

Internships:
{internships}

Projects:
{projects}

Certifications:
{certifications}

Achievements:
{achievements}

Requirements:

1. Create a strong Professional Summary.
2. Organize sections professionally.
3. Improve wording where necessary.
4. Make the resume ATS-friendly.
5. Use professional formatting.
6. Highlight technical strengths.
7. Highlight projects effectively.
8. Return only the resume content.
"""

                # ======================================
                # GEMINI API CALL
                # ======================================

                response = model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": 0.4
                    }
                )

                generated_resume = response.text

                # Store in Session State

                st.session_state.generated_resume = (
                    generated_resume
                )

                st.success(
                    "Resume Generated Successfully!"
                )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

# ==========================================================
# DISPLAY GENERATED RESUME
# ==========================================================

if st.session_state.generated_resume:

    st.markdown("---")

    st.subheader(
        "📄 Generated Resume"
    )

    st.markdown(
        st.session_state.generated_resume
    )

    # ======================================================
    # DOWNLOAD BUTTON
    # ======================================================

    st.download_button(
        label="📥 Download Resume",
        data=st.session_state.generated_resume,
        file_name="ATS_Resume.txt",
        mime="text/plain",
        use_container_width=True
    )