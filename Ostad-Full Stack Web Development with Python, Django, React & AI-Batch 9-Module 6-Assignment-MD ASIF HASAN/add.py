import utility


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter student roll number: ")
    email = input("Enter student email: ")
    department = input("Enter student department: ")

    # Validate input first
    if not (utility.is_name(name) and
            utility.is_roll(roll) and
            utility.is_email(email) and
            utility.is_dept(department)):
        print("Invalid input. Student not added.")
        return

    # Check duplicate roll
    try:
        with open("students.csv", "r", encoding="utf-8") as file:
            lines = file.readlines()[1:]  # skip header

            for line in lines:
                line = line.strip()

                if not line:
                    continue  # skip empty lines

                parts = line.split(",")

                if len(parts) < 2:
                    continue  # skip malformed lines

                existing_roll = parts[1].strip()

                if roll == existing_roll:
                    print("Roll number already exists. Student not added.")
                    return

    except FileNotFoundError:
        pass  # file will be created later

    # Add student
    with open("students.csv", "a", newline="", encoding="utf-8") as file:
        file.write(f"{name},{roll},{email},{department}\n")

    print("Student added successfully.")
