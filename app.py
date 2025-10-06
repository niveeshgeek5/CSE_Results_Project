import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
classy_night = """
<style>
/* Smooth animated gradient background */
.stApp {
  background: linear-gradient(-45deg, #0d1b2a, #1b263b, #415a77, #0f2027);
  background-size: 400% 400%;
  animation: auroraBG 25s ease infinite;
  color: #e0e0e0;
}
@keyframes auroraBG {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}

/* Soft floating orbs */
.orb {
  position: fixed;
  border-radius: 50%;
  opacity: 0.3;
  background: radial-gradient(circle, #ffffff33, transparent);
  animation: floatOrb 20s ease-in-out infinite alternate;
}
@keyframes floatOrb {
  from { transform: translateY(0px) translateX(0px); }
  to { transform: translateY(-50px) translateX(30px); }
}

/* Aurora wave effect */
.aurora {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(120deg, #4e54c8aa, #8f94fb55 200px, transparent 400px);
  mix-blend-mode: screen;
  animation: wave 15s linear infinite;
}
@keyframes wave {
  from { background-position: 0 0; }
  to { background-position: 1000px 0; }
}
</style>

<!-- Aurora overlay -->
<div class="aurora"></div>

<!-- Orbs -->
<div class="orb" style="top:20%; left:15%; width:150px; height:150px; animation-duration:18s;"></div>
<div class="orb" style="top:60%; left:70%; width:200px; height:200px; animation-duration:22s;"></div>
<div class="orb" style="top:40%; left:40%; width:100px; height:100px; animation-duration:25s;"></div>
"""
st.markdown(classy_night, unsafe_allow_html=True)
st.markdown("<style>body, .stApp { color: black; }</style>", unsafe_allow_html=True)
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
batch24, batch23, batch22, batch21,Overall, Students_Result_viewer= st.tabs(["Batch 24", "Batch 23", "Batch 22", "Batch 21","Overall","Students Result viewer"])


# Subject mapping

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
    st.subheader("Overall Department Result")

    # Function to calculate results
    def calculate_results(df, subjects):
        df["Result"] = df[subjects].apply(lambda row: "Pass" if "U" not in row.values else "Fail", axis=1)
        pass_count = df["Result"].value_counts().get("Pass", 0)
        fail_count = df["Result"].value_counts().get("Fail", 0)
        return pass_count, fail_count, len(df)

    # Batch-wise results
    pass23, fail23, total23 = calculate_results(df23, [sub for sub in subject_map_sem4.keys() if sub in df23.columns])
    pass24, fail24, total24 = calculate_results(df24, [sub for sub in subject_map_sem2.keys() if sub in df24.columns])
    pass22, fail22, total22 = calculate_results(df22, [sub for sub in subject_map_sem6.keys() if sub in df22.columns])
    pass21, fail21, total21 = calculate_results(df21, [sub for sub in subject_map_sem8.keys() if sub in df21.columns])

    # Totals
    total_students = total21 + total22 + total23 + total24
    total_pass = pass21 + pass22 + pass23 + pass24
    total_fail = fail21 + fail22 + fail23 + fail24
    overall_percentage = (total_pass / total_students) * 100 if total_students > 0 else 0

    # --- Animated Circular Gauge with Burst Particles ---
    st.markdown(f"""
    <style>
    .container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 40px auto;
    }}
    .circle {{
        width: 260px;
        height: 260px;
        border-radius: 50%;
        background: conic-gradient(#00ff88 0% {overall_percentage}%, #111 {overall_percentage}% 100%);
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 40px #00ff88, 0 0 80px #00ff88, 0 0 120px #00ff88;
        animation: popIn 1.5s ease-out forwards;
        overflow: visible;
    }}
    .percent-text {{
        font-size: 2.5rem;
        font-weight: bold;
        color: #fff;
        text-shadow: 0 0 15px #00ff88, 0 0 30px #00ffaa;
        animation: glowPulse 2s infinite alternate;
    }}
    @keyframes popIn {{
        0% {{ transform: scale(0.3); opacity: 0; }}
        70% {{ transform: scale(1.2); opacity: 1; }}
        100% {{ transform: scale(1); }}
    }}
    @keyframes glowPulse {{
        from {{ text-shadow: 0 0 10px #00ff88; }}
        to   {{ text-shadow: 0 0 25px #00ffaa, 0 0 50px #00ffaa; }}
    }}
    .particle {{
        position: absolute;
        width: 6px;
        height: 6px;
        background: #00ff88;
        border-radius: 50%;
        animation: shoot 1.2s ease-out forwards;
    }}
    @keyframes shoot {{
        from {{ transform: translate(0,0) scale(1); opacity: 1; }}
        to   {{ transform: translate(var(--x), var(--y)) scale(0.2); opacity: 0; }}
    }}
    </style>

    <div class="container">
        <div class="circle">
            <div class="percent-text">{overall_percentage:.1f}%</div>
            <!-- burst particles -->
            <div class="particle" style="--x:-120px; --y:-60px;"></div>
            <div class="particle" style="--x:100px; --y:-80px;"></div>
            <div class="particle" style="--x:-90px; --y:90px;"></div>
            <div class="particle" style="--x:120px; --y:100px;"></div>
            <div class="particle" style="--x:-140px; --y:20px;"></div>
        </div>
        <p style="color:#eee; font-size:1.1rem; margin-top:20px;">
            👥 Total Students: <b>{total_students}</b> | ✅ Passed: <b>{total_pass}</b> | ❌ Failed: <b>{total_fail}</b>
        </p>
    </div>
    """, unsafe_allow_html=True)



with Students_Result_viewer:
    st.subheader("Student Result")
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt

    

    df = pd.read_csv("CSE_Sem2_Batch24.csv")

    regno = st.number_input("Enter Register Number",min_value=1, step=1)

    if regno:
      student = df[df["Reg No"] == regno]
    if student.empty:
        st.error("No student found.")
    else:
        subjects = df.columns[2:]
        grades = student.iloc[0, 2:].tolist()
        grade_order = ["U", "C", "B", "B+", "A", "A+", "O"]
        grade_values = [grade_order.index(g) for g in grades]

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(subjects, grade_values, color="red", edgecolor="black")
        ax.set_xticklabels(subjects, rotation=45, ha='right')
        ax.set_yticks(range(len(grade_order)))
        ax.set_yticklabels(grade_order)
        ax.set_title(f"Grades for {student.iloc[0,1]} ({regno})")
        ax.set_xlabel("Subjects")
        ax.set_ylabel("Grades")
        st.pyplot(fig)
#else:
    #st.info("🔒 Coming soon")

 
