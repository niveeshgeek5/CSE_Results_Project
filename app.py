import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------
# Load data
# ----------------------
# Batch 23 (Sem 4)
df23 = pd.read_csv("Sem4_Results_820423.csv")
df23.replace("UA", "U", inplace=True)

# Batch 24 (Sem 2)
df24 = pd.read_csv("CSE_Sem2_Batch24.csv")
df24.replace("UA", "U", inplace=True)

st.title("📊 CSE Department April 2025 Results")

# Tabs for batches
batch24, batch23, batch22, batch21 = st.tabs(["Batch 24", "Batch 23", "Batch 22", "Batch 21"])

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
# Placeholders for other batches
# ----------------------
with batch22:
    st.subheader("Batch 22 Results")
    st.info("🔒 Coming soon...")

with batch21:
    st.subheader("Batch 21 Results")
    st.info("🔒 Coming soon...")
