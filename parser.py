import toml

# Load the TOML file
with open("classes.toml", "r") as f:
    data = toml.load(f)

# Access user information
user = data.get("user", {})
print(f"User: {user.get('name')} (ID: {user.get('student_id')})")
print(f"Semester: {user.get('semester')}")

# Access class preferences
preferences = data.get("preferences", {}).get("desired_classes", [])
print("\nDesired Classes:")
for course in preferences:
    print(f" - {course}")

# Access the schedule of available classes
print("\nClass Schedule:")
schedule = data.get("schedule", [])
for class_info in schedule:
    course_code = class_info.get("course_code")
    course_name = class_info.get("course_name")
    section = class_info.get("section")
    days = ", ".join(class_info.get("days", []))
    start_time = class_info.get("start_time")
    end_time = class_info.get("end_time")

    print(f"{course_code} - {course_name} (Section {section})")
    print(f"  Days: {days}")
    print(f"  Time: {start_time} to {end_time}")
    print()


