import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Sem4_Results_820423.csv")
df.replace("UA", "U", inplace=True)

st.title("📊 CSE Department Results")

# Tabs for batches
batch24, batch23, batch22, batch21 = st.tabs(["Batch 24", "Batch 23", "Batch 22", "Batch 21"])

# ✅ Subject mapping (only your correct subjects)
subject_map = {
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

# ----------------------
# Batch 23 (your batch)
# ----------------------
with batch23:
    st.subheader("Semester 4 Results - Batch 23")

    grade_order = ["O", "A+", "A", "B+", "B", "C", "U"]

    # Keep only valid subjects (from mapping)
    subjects = [sub for sub in subject_map.keys() if sub in df.columns]

    # Subject-wise grade distribution
    st.header("📚 Subject-wise Grade Distribution")

    for subject in subjects:
        # ✅ Clean subject grades
        df[subject] = df[subject].fillna("U").astype(str).str.strip()
        df[subject] = df[subject].apply(lambda g: g if g in grade_order else "U")

        # Count grades
        grade_counts = df[subject].value_counts().reindex(grade_order, fill_value=0)

        # Plot bar chart
        fig, ax = plt.subplots()
        grade_counts.plot(kind="bar", ax=ax)
        ax.set_title(f"{subject} – {subject_map[subject]}")
        ax.set_ylabel("Number of Students")
        st.pyplot(fig)

        # ✅ Correct Summary
        total = grade_counts.sum()
        fails = grade_counts["U"]
        passes = total - fails
        most_common = grade_counts.idxmax()

        st.write(
            f"**Summary:** {subject} – {subject_map[subject]} → "
            f"Total: {total}, Pass: {passes}, Fail: {fails}, Most common grade: {most_common}"
        )

    # Pass vs Fail Visualization
    st.header("✅ Pass vs Fail Analysis")

    # A student fails if ANY subject is U
    df["Result"] = df[subjects].apply(
        lambda row: "Pass" if "U" not in row.values else "Fail", axis=1
    )
    pass_fail_counts = df["Result"].value_counts()

    fig, ax = plt.subplots()
    pass_fail_counts.plot(kind="pie", autopct='%1.1f%%', ax=ax, colors=["green", "red"])
    ax.set_ylabel("")
    ax.set_title("Pass vs Fail (Batch 23 - Sem 4)")
    st.pyplot(fig)

    st.write(
        f"**Summary:** Out of {len(df)} students → "
        f"{pass_fail_counts.get('Pass', 0)} Passed, {pass_fail_counts.get('Fail', 0)} Failed."
    )

# ----------------------
# Placeholders for other batches
# ----------------------
with batch24:
    st.subheader("Batch 24 Results")
    st.info("🔒 Coming soon...")

with batch22:
    st.subheader("Batch 22 Results")
    st.info("🔒 Coming soon...")

with batch21:
    st.subheader("Batch 21 Results")
    st.info("🔒 Coming soon...")
