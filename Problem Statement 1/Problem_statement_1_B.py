import requests
import matplotlib.pyplot as plt


# Step 1: API URL
api_url = "http://127.0.0.1:5000/scores"


# Step 2: Fetch data from API
response = requests.get(api_url, timeout=10)


# Step 3: Check response
if response.status_code == 200:

    students = response.json()

    print("Student data fetched successfully!\n")

else:

    print("Failed to fetch student data.")
    raise SystemExit


# Step 4: Display student scores
print("STUDENT TEST SCORES")
print("-" * 40)

for student in students:
    print(f"{student['name']}: {student['score']}")


# Step 5: Calculate average score
if not students:
    print("No student data available.")
    raise SystemExit

total_score = 0

for student in students:
    total_score += student["score"]

average_score = total_score / len(students)

print("-" * 40)
print(f"Average Score: {average_score:.2f}")


# Step 6: Prepare data for bar chart
names = []
scores = []

for student in students:
    names.append(student["name"])
    scores.append(student["score"])


# Step 7: Create bar chart
plt.figure(figsize=(10, 6))

plt.bar(names, scores)

plt.axhline(
    y=average_score,
    linestyle="--",
    label=f"Average: {average_score:.2f}"
)

plt.xlabel("Student Names")
plt.ylabel("Test Scores")
plt.title("Student Test Score Analysis")

plt.xticks(rotation=45, ha="right")
plt.ylim(0, 100)
plt.legend()
plt.tight_layout()

plt.show()