import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st

st.markdown("""
<style>
/* Full screen dark night background */
.stApp {
    background: radial-gradient(circle at center, #0d0d0d, #000000);
    overflow: hidden;
    position: relative;
}

/* Particle container */
.particles {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    overflow: hidden;
    z-index: -1;
}

/* Each particle */
.particle {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 215, 0, 0.8); /* golden glow */
    box-shadow: 0 0 10px rgba(255, 215, 0, 0.6),
                0 0 20px rgba(255, 140, 0, 0.4);
    animation: explode 8s infinite ease-in-out;
}

/* Explosion animation */
@keyframes explode {
    0% {
        transform: scale(0.2) translate(0, 0);
        opacity: 1;
    }
    50% {
        transform: scale(1.5) translate(200px, -200px);
        opacity: 0.7;
    }
    100% {
        transform: scale(0.2) translate(0, 0);
        opacity: 0;
    }
}
</style>

<div class="particles">
  <div class="particle" style="width:8px; height:8px; top:20%; left:40%; animation-delay:0s;"></div>
  <div class="particle" style="width:6px; height:6px; top:50%; left:60%; animation-delay:1s;"></div>
  <div class="particle" style="width:10px; height:10px; top:70%; left:30%; animation-delay:2s;"></div>
  <div class="particle" style="width:7px; height:7px; top:80%; left:80%; animation-delay:3s;"></div>
  <div class="particle" style="width:9px; height:9px; top:40%; left:20%; animation-delay:4s;"></div>
  <div class="particle" style="width:5px; height:5px; top:60%; left:10%; animation-delay:5s;"></div>
</div>
""", unsafe_allow_html=True)
import matplotlib.pyplot as plt

# Apply a custom dark theme to all matplotlib plots
plt.style.use("dark_background")

# Customize default color cycle (glowing neon tones)
plt.rcParams["axes.prop_cycle"] = plt.cycler(color=[
    "#00FFFF",  # cyan
    "#FF00FF",  # magenta
    "#00FF7F",  # spring green
    "#FFD700",  # gold
    "#FF4500",  # orange red
    "#1E90FF"   # dodger blue
])

# Font and figure styling
plt.rcParams["figure.facecolor"] = "none"       # transparent (matches bg)
plt.rcParams["axes.facecolor"] = "none"
plt.rcParams["savefig.facecolor"] = "none"
plt.rcParams["axes.edgecolor"] = "#888888"
plt.rcParams["axes.labelcolor"] = "#e0e0e0"
plt.rcParams["xtick.color"] = "#aaaaaa"
plt.rcParams["ytick.color"] = "#aaaaaa"
plt.rcParams["text.color"]  = "#f0f0f0"
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
