def view_students():
    print("===== All Students =====")
    with open("students.csv", "r", encoding = "utf-8") as file:
        lines = file.readlines()[1:]  # skip header
        count = 0
        for line in lines:
            line = line.strip()
            if not line:  # skip empty lines
                continue
            name, roll, email, dept =  line.split(",")
            count += 1
            print(f"{count}. Name: {name}\nRoll: {roll}\nEmail: {email}\nDepartment: {dept}")           
    print("========================")
        