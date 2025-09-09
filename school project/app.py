import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load CSV
# -----------------------------
csv_file = 'students_marks_12th_class.csv'
df = pd.read_csv(csv_file)

# -----------------------------
# Subjects detection
# -----------------------------
all_subjects = ["Physics","Chemistry","Maths","Biology",
                "Accounts","Economics","Business",
                "History","Geography","Political","Sociology","English"]

subject_cols = [col for col in all_subjects if col in df.columns]

# -----------------------------
# Calculate Total, Average & Grade
# -----------------------------
df['Total'] = df[subject_cols].apply(pd.to_numeric).sum(axis=1)
df['Average'] = df[subject_cols].apply(pd.to_numeric).mean(axis=1)

# -----------------------------
# grade function
# -----------------------------

def grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B+'
    elif avg >= 60:
        return 'B'
    else: 
        return 'C'

df['Grade'] = df['Average'].apply(grade)

# -----------------------------
# Basic Analysis
# -----------------------------
# Top 5 students overall
print("Top 5 Students Overall:")
print(df[['Student_ID','Name','Stream','Total','Average']].sort_values(by='Total', ascending=False).head())

# Average marks per subject
print("\nAverage Marks per Subject:")
print(df[subject_cols].apply(pd.to_numeric).mean())

# Grade distribution
grade_counts = df['Grade'].value_counts()
print("\nGrade Distribution:")
print(grade_counts)

# -----------------------------
# Visualization
# -----------------------------
# 5a. Grade Distribution Pie Chart
plt.figure(figsize=(6,6))
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Grade Distribution")
plt.show()

#  Average Marks per Subject Bar Chart
plt.figure(figsize=(10,6))
avg_marks = df[subject_cols].apply(pd.to_numeric).mean()
avg_marks.plot(kind='bar', color='skyblue')
plt.ylabel("Average Marks")
plt.title("Average Marks per Subject")
plt.show()

# 5c. Top 10 Students Total Marks Bar Chart
plt.figure(figsize=(10,6))
top10 = df.sort_values(by='Total', ascending=False).head(10)
plt.bar(top10['Name'], top10['Total'], color='orange')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Total Marks")
plt.title("Top 10 Students Total Marks")
plt.show()


# -----------------------------
# 5d. Stream-wise Analysis Table & Comparison
# -----------------------------

# Average total per stream
avg_total = df.groupby("Stream")["Total"].mean().round(2)

# Topper per stream
topper = df.loc[df.groupby("Stream")["Total"].idxmax(), ["Stream","Name"]].set_index("Stream")["Name"]

# Failed count per stream
failed = (df[subject_cols].apply(pd.to_numeric, errors="coerce") < 33).any(axis=1).groupby(df["Stream"]).sum()

# Combine all into one table
stream_table = pd.DataFrame({"Average Total": avg_total,
                             "Topper": topper,
                             "Failed Students": failed})

print("\nStream-wise Analysis Table:")
print(stream_table)

# Bar chart
plt.bar(stream_table.index, stream_table["Average Total"], color=["skyblue","orange","green"])
plt.ylabel("Average Total Marks")
plt.title("Stream-wise Average Total Marks Comparison")
plt.show()


# -----------------------------
# 5e. Stream-wise Toppers Comparison
# -----------------------------

# Stream-wise toppers
toppers_table = df.loc[df.groupby("Stream")["Total"].idxmax(),
                       ["Stream","Name","Total"]]

# Rename columns for clarity
toppers_table.columns = ["Stream","Topper","Total Marks"]

print("\nStream-wise Toppers Comparison:")
print(toppers_table)

# Bar Chart: Stream-wise Topper Total Marks
plt.bar(toppers_table['Stream'], toppers_table['Total Marks'],
        color=['skyblue','orange','green'])
plt.ylabel("Total Marks")
plt.title("Stream-wise Topper Total Marks Comparison")
plt.show()


# -----------------------------
# 6. Stream-wise Failures Details
# -----------------------------
failures_summary = []

for i in range(len(df)):
    name = df.loc[i, 'Name']
    stream = df.loc[i, 'Stream']
    total = df.loc[i, 'Total']
    
    failed_subjects = []
    
    # Check each subject
    for sub in all_subjects:
        try:
            marks = int(df.loc[i, sub])
            if marks < 33:
                failed_subjects.append(sub)
        except:
            pass
    
    if len(failed_subjects) > 0:
        failures_summary.append([stream, name, total, ", ".join(failed_subjects)])

# Convert into DataFrame
failures_table = pd.DataFrame(failures_summary, 
                              columns=['Stream', 'Student Name', 'Total Marks', 'Failed Subjects'])

# Create DataFrame
print("\nFailed Students Details:")
print(failures_table)

# Stream-wise Failed Students Count Bar Chart
failed_counts = failures_table.groupby('Stream').size()
plt.bar(failed_counts.index, failed_counts.values, color=['red','purple','brown'])
plt.ylabel("Number of Failed Students")
plt.title("Stream-wise Failed Students")
plt.show()


# ----------------------------
# Class Rank List
# ----------------------------
df['Class Rank'] = df['Total'].rank(ascending=False).astype(int)
class_rank = df.sort_values('Class Rank')[['Name','Stream','Total','Class Rank']]

print("\nClass Rank List:")
print(class_rank)


# ----------------------------
# Stream-wise Rank List
# ----------------------------
df['Stream Rank'] = df.groupby('Stream')['Total'].rank(ascending=False).astype(int)
print("\nStream-wise Rank List:")
print(df[['Name','Stream','Total','Stream Rank']])

# Pie Chart Stream-wise Toppers 
toppers = df[df['Stream Rank'] == 1]
plt.pie(toppers['Total'], labels=toppers['Stream'])
plt.title("Stream-wise Topper Marks")
plt.show()


# ----------------------------
# Pie Chart: Stream-wise Student Count
# ----------------------------
stream_count = df['Stream'].value_counts()

plt.pie(stream_count, labels=stream_count.index, autopct='%1.1f%%',
        startangle=90, colors=['skyblue','orange','lightgreen'])
plt.title("Stream-wise Student Distribution")
plt.show()

