import utility

def search_student():
    
    value = input("Enter search term (name/email/roll): ")
    print("Search Result:")
    
    #Opens in reading mode then validates each user input & shows the corresponding record
    with open("students.csv","r",encoding = "utf-8") as file:
        lines = file.readlines()
        header = next(iter(lines))
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) < 4:
                continue
            if utility.is_email(value) == True:
                if parts[2].strip() == value: 
                    print(f"Name: {parts[0]}\nRoll: {parts[1]}\nEmail: {parts[2]}\nDepartment: {parts[3]}")
            if utility.is_name(value) == True:
                if parts[0].strip() == value:
                    print(f"Name: {parts[0]}\nRoll: {parts[1]}\nEmail: {parts[2]}\nDepartment: {parts[3]}")
            if utility.is_roll(value) == True:
                if parts[1].strip() == value:
                    print(f"Name: {parts[0]}\nRoll: {parts[1]}\nEmail: {parts[2]}\nDepartment: {parts[3]}")
                    
                
            
            