import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st

night_theme = """
<style>
/* Dark animated gradient background */
.stApp {
  background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #000000);
  background-size: 400% 400%;
  animation: nightGradient 30s ease infinite;
  color: #f0f0f0;
}
@keyframes nightGradient {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}

/* Glowing moon */
.moon {
  position: fixed;
  top: 60px;
  right: 60px;
  width: 100px;
  height: 100px;
  background: radial-gradient(circle, #fdfdfd 60%, #cfcfcf 100%);
  border-radius: 50%;
  box-shadow: 0 0 40px #ffffff88;
  animation: glow 5s ease-in-out infinite alternate;
}
@keyframes glow {
  from { box-shadow: 0 0 20px #ffffff55; }
  to { box-shadow: 0 0 60px #ffffffcc; }
}

/* Twinkling stars */
.star {
  position: absolute;
  width: 3px;
  height: 3px;
  background: white;
  border-radius: 50%;
  animation: twinkle 2s infinite alternate;
}
@keyframes twinkle {
  from {opacity: 0.2;}
  to {opacity: 1;}
}
</style>

<!-- Add moon -->
<div class="moon"></div>

<!-- Stars -->
<div class="star" style="top:20%; left:15%; animation-delay:0s;"></div>
<div class="star" style="top:30%; left:40%; animation-delay:1s;"></div>
<div class="star" style="top:50%; left:70%; animation-delay:0.5s;"></div>
<div class="star" style="top:65%; left:25%; animation-delay:1.5s;"></div>
<div class="star" style="top:80%; left:85%; animation-delay:2s;"></div>
"""
st.markdown(night_theme, unsafe_allow_html=True)


# ----------------------
# Load data
# ----------------------
# Batch 23 (Sem 4)
df23 = pd.read_csv("Sem4_Results_820423.csv")
df23.replace("UA", "U", inplace=True)

# Batch 24 (Sem 2)
df24 = pd.read_csv("CSE_Sem2_Batch24.csv")
df24.replace("UA", "U", inplace=True)

# Batch 21 (Sem 8)
df21 = pd.read_csv("sem8.csv")
df21.replace("UA", "U", inplace=True)

# Batch 22 (Sem 6)
df22 = pd.read_csv("sem6.csv")
df22.replace("UA", "U", inplace=True)

st.title("📊 CSE Department April-2025 Results")

# Tabs for batches
batch24, batch23, batch22, batch21,Overall = st.tabs(["Batch 24", "Batch 23", "Batch 22", "Batch 21","Overall"])

# ----------------------
# Subject mapping
# ----------------------
subject_map_sem4 = {
    "CS3401": "Algorithms",
    "CS3451": "Introduction to Operating Systems",
    "CS3452": "Theory of Computation",
    "CS3461": "Operating Systems Laboratory",
    "CS3481": "Database Management Systems Laboratory",
    "CS3491": "Artificial Intelligence and Machine Learning",
    "CS3492": "Database Management Systems",
    "GE3451": "Environmental Sciences and Sustainability",
    "NM1075": "Employability Based Project Learning"
}

subject_map_sem2 = {
    "BE3251": "Basic Electrical and Electronics Engineering (BEEE)",
    "CS3251": "Programming in C",
    "CS3271": "Programming in C Laboratory",
    "GE3251": "Engineering Graphics",
    "GE3252": "Tamils and Technology",
    "GE3271": "Engineering Practices Laboratory",
    "GE3272": "Communication Laboratory / Foreign Language",
    "HS3252": "Professional English – II",
    "MA3251": "Statistics and Numerical Methods (SNM)",
    "PH3256": "Physics for Information Science"
}

subject_map_sem6 = {
    "CCS335": "Cloud Computing",
    "CCS354": "Network Security",
    "CCS356": "Object Oriented Software Engineering",
    "CCS374": "Web Application Security",
    "CS3691": "Embedded Systems and IoT",
    "MX3085": "Well Being with Traditional Practices - Yoga, Ayurveda and Siddha",
    "NM1104": "Speech Recognition Techniques Project: Language Translation via Speech",
    "0EE351": "Renewable Energy System"
}

subject_map_sem8 = {
    "CS3811": "Project work/internship"
}

# Grade order for visualization
grade_order = ["O", "A+", "A", "B+", "B", "C", "U"]

# ----------------------
# Batch 23 (Sem 4)
# ----------------------
with batch23:
    st.subheader("Semester 4 Results - Batch 23")

    # Keep only valid subjects
    subjects = [sub for sub in subject_map_sem4.keys() if sub in df23.columns]

    # Subject-wise grade distribution
    st.header("📚 Subject-wise Grade Distribution")
    for subject in subjects:
        grade_counts = df23[subject].value_counts().reindex(grade_order, fill_value=0)

        fig, ax = plt.subplots()
        grade_counts.plot(kind="bar", ax=ax)
        ax.set_title(f"{subject} – {subject_map_sem4[subject]}")
        ax.set_ylabel("Number of Students")
        st.pyplot(fig)

        # Summary
        total = grade_counts.sum()
        fails = grade_counts["U"]
        passes = total - fails
        st.write(f"*Summary:* {subject} – {subject_map_sem4[subject]} → "
                 f"Pass: {passes}, Fail: {fails}, Most common grade: {grade_counts.idxmax()}")

    # Pass vs Fail Visualization
    st.header("✅ Pass vs Fail Analysis")
    df23["Result"] = df23[subjects].apply(lambda row: "Pass" if "U" not in row.values else "Fail", axis=1)
    pass_fail_counts = df23["Result"].value_counts()

    fig, ax = plt.subplots()
    pass_fail_counts.plot(kind="pie", autopct='%1.1f%%', ax=ax, colors=["green", "red"])
    ax.set_ylabel("")
    ax.set_title("Pass vs Fail (Batch 23 - Sem 4)")
    st.pyplot(fig)

    st.write(f"*Summary:* Out of {len(df23)} students → "
             f"{pass_fail_counts.get('Pass', 0)} Passed, {pass_fail_counts.get('Fail', 0)} Failed.")

# ----------------------
# Batch 24 (Sem 2)
# ----------------------
with batch24:
    st.subheader("Semester 2 Results - Batch 24")

    # Keep only valid subjects
    subjects = [sub for sub in subject_map_sem2.keys() if sub in df24.columns]

    # Subject-wise grade distribution
    st.header("📚 Subject-wise Grade Distribution")
    for subject in subjects:
        grade_counts = df24[subject].value_counts().reindex(grade_order, fill_value=0)

        fig, ax = plt.subplots()
        grade_counts.plot(kind="bar", ax=ax)
        ax.set_title(f"{subject} – {subject_map_sem2[subject]}")
        ax.set_ylabel("Number of Students")
        st.pyplot(fig)

        # Summary
        total = grade_counts.sum()
        fails = grade_counts["U"]
        passes = total - fails
        st.write(f"*Summary:* {subject} – {subject_map_sem2[subject]} → "
                 f"Pass: {passes}, Fail: {fails}, Most common grade: {grade_counts.idxmax()}")

    # Pass vs Fail Visualization
    st.header("✅ Pass vs Fail Analysis")
    df24["Result"] = df24[subjects].apply(lambda row: "Pass" if "U" not in row.values else "Fail", axis=1)
    pass_fail_counts = df24["Result"].value_counts()

    fig, ax = plt.subplots()
    pass_fail_counts.plot(kind="pie", autopct='%1.1f%%', ax=ax, colors=["green", "red"])
    ax.set_ylabel("")
    ax.set_title("Pass vs Fail (Batch 24 - Sem 2)")
    st.pyplot(fig)

    st.write(f"*Summary:* Out of {len(df24)} students → "
             f"{pass_fail_counts.get('Pass', 0)} Passed, {pass_fail_counts.get('Fail', 0)} Failed.")

# ----------------------
# Batch 22 (Sem 6)
# ----------------------
with batch22:
    st.subheader("Semester 6 Results - Batch 22")

    # Subject-wise grade distribution
    st.header("📚 Subject-wise Grade Distribution")
    
    # Mapping for Semester 6
    subject_map_sem6 = {
        "CCS335": "Cloud Computing",
        "CCS354": "Network Security",
        "CCS356": "Object Oriented Software Engineering",
        "CCS374": "Web Application Security",
        "CS3691": "Embedded Systems and IoT",
        "MX3085": "Well Being with Traditional Practices - Yoga, Ayurveda and Siddha",
        "NM1104": "Speech Recognition Techniques Project: Language Translation via Speech",
        "0EE351": "Renewable Energy System"
    }
    
    # Keep only valid subjects
    subjects = [sub for sub in subject_map_sem6.keys() if sub in df22.columns]

    for subject in subjects:
        grade_counts = df22[subject].value_counts().reindex(grade_order, fill_value=0)

        fig, ax = plt.subplots()
        grade_counts.plot(kind="bar", ax=ax)
        ax.set_title(f"{subject} – {subject_map_sem6[subject]}")
        ax.set_ylabel("Number of Students")
        st.pyplot(fig)

        # Summary
        total = grade_counts.sum()
        fails = grade_counts["U"]
        passes = total - fails
        st.write(f"*Summary:* {subject} – {subject_map_sem6[subject]} → "
                 f"Pass: {passes}, Fail: {fails}, Most common grade: {grade_counts.idxmax()}")

    # Pass vs Fail Visualization
    st.header("✅ Pass vs Fail Analysis")
    df22["Result"] = df22[subjects].apply(lambda row: "Pass" if "U" not in row.values else "Fail", axis=1)
    pass_fail_counts = df22["Result"].value_counts()

    fig, ax = plt.subplots()
    pass_fail_counts.plot(kind="pie", autopct='%1.1f%%', ax=ax, colors=["green", "red"])
    ax.set_ylabel("")
    ax.set_title("Pass vs Fail (Batch 22 - Sem 6)")
    st.pyplot(fig)

    st.write(f"*Summary:* Out of {len(df22)} students → "
             f"{pass_fail_counts.get('Pass', 0)} Passed, {pass_fail_counts.get('Fail', 0)} Failed.")

with batch21:
    st.subheader("Semester 8 Results - Batch 21")

    # Keep only valid subjects
    subjects = [sub for sub in subject_map_sem8.keys() if sub in df21.columns]

    # Subject-wise grade distribution
    st.header("📚 Subject-wise Grade Distribution")
    for subject in subjects:
        grade_counts = df21[subject].value_counts().reindex(grade_order, fill_value=0)

        fig, ax = plt.subplots()
        grade_counts.plot(kind="bar", ax=ax)
        ax.set_title(f"{subject} – {subject_map_sem8[subject]}")
        ax.set_ylabel("Number of Students")
        st.pyplot(fig)

        # Summary
        total = grade_counts.sum()
        fails = grade_counts["U"]
        passes = total - fails
        st.write(f"*Summary:* {subject} – {subject_map_sem8[subject]} → "
                 f"Pass: {passes}, Fail: {fails}, Most common grade: {grade_counts.idxmax()}")

    # Pass vs Fail Visualization
    st.header("✅ Pass vs Fail Analysis")
    df21["Result"] = df21[subjects].apply(lambda row: "Pass" if "U" not in row.values else "Fail", axis=1)
    pass_fail_counts = df21["Result"].value_counts()

    fig, ax = plt.subplots()
    pass_fail_counts.plot(kind="pie", autopct='%1.1f%%', ax=ax, colors=["green", "red"])
    ax.set_ylabel("")
    ax.set_title("Pass vs Fail (Batch 21 - Sem 8)")
    st.pyplot(fig)

    st.write(f"*Summary:* Out of {len(df21)} students → "
             f"{pass_fail_counts.get('Pass', 0)} Passed, {pass_fail_counts.get('Fail', 0)} Failed.")
with Overall:
    st.subheader("📊 CSE Department April-2025 Results")
    st.info("🔒 Coming soon...")
