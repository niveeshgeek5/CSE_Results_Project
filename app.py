import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load extracted data
df = pd.read_csv("Sem4_Results_820423.csv")

# Clean: replace UA with U (fail)
df.replace("UA", "U", inplace=True)

# Title
st.title("CSE Department - Semester 4 Results (Batch 820423)")

# --------------------------------
# 1. Subject-wise Grade Distribution
# --------------------------------
st.header("📚 Subject-wise Grade Distribution")

grade_order = ["O", "A+", "A", "B+", "B", "C", "U"]
subjects = [col for col in df.columns if col not in ["RegNo", "Name"]]

for subject in subjects:
    grade_counts = df[subject].value_counts().reindex(grade_order, fill_value=0)

    fig, ax = plt.subplots()
    grade_counts.plot(kind="bar", ax=ax)
    ax.set_title(f"Grade Distribution - {subject}")
    ax.set_ylabel("Number of Students")
    st.pyplot(fig)

    # Small summary
    total = grade_counts.sum()
    fails = grade_counts["U"]
    passes = total - fails
    st.write(f"*Summary:* {subject} → Pass: {passes}, Fail: {fails}, "
             f"Most common grade: {grade_counts.idxmax()}")

# --------------------------------
# 2. Overall Grade Distribution
# --------------------------------
st.header("📊 Overall Grade Distribution")

all_grades = df[subjects].values.flatten()
all_grades_series = pd.Series(all_grades)
all_counts = all_grades_series.value_counts().reindex(grade_order, fill_value=0)

fig, ax = plt.subplots()
all_counts.plot(kind="pie", autopct='%1.1f%%', ax=ax)
ax.set_ylabel("")
ax.set_title("Overall Grade Distribution")
st.pyplot(fig)

st.write(f"*Summary:* Across all subjects → "
         f"Total Grades: {all_counts.sum()}, "
         f"Most common grade: {all_counts.idxmax()}, "
         f"Fails: {all_counts['U']}")

# --------------------------------
# 3. Pass vs Fail Visualization
# --------------------------------
st.header("✅ Pass vs Fail Analysis")

# A student is Pass if no U in their row
df["Result"] = df[subjects].apply(lambda row: "Pass" if "U" not in row.values else "Fail", axis=1)
pass_fail_counts = df["Result"].value_counts()

fig, ax = plt.subplots()
pass_fail_counts.plot(kind="pie", autopct='%1.1f%%', ax=ax, colors=["green", "red"])
ax.set_ylabel("")
ax.set_title("Pass vs Fail (Semester 4)")
st.pyplot(fig)

st.write(f"*Summary:* Out of {len(df)} students → "
         f"{pass_fail_counts.get('Pass', 0)} Passed, {pass_fail_counts.get('Fail', 0)} Failed.")