# Smart Study Planner Generator

subjects = {}

n = int(input("Enter number of subjects: "))

for i in range(n):
    name = input("\nEnter subject name: ")
    difficulty = input("Difficulty (easy/medium/hard): ").lower()
    subjects[name] = difficulty

days = int(input("\nEnter number of days left for exam: "))
hours_per_day = int(input("Enter study hours per day: "))

total_hours = days * hours_per_day

weight = {
    "easy": 1,
    "medium": 2,
    "hard": 3
}

total_weight = sum(weight[d] for d in subjects.values())

print("\nSMART STUDY PLAN\n")

for subject, difficulty in subjects.items():
    subject_hours = (weight[difficulty] / total_weight) * total_hours
    print(subject, ":", round(subject_hours, 1), "hours total")

print("\nTip: Study difficult subjects when your mind is fresh!")
