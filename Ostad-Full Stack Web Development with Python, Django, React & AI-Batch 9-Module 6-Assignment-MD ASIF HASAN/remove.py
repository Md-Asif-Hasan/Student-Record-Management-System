def remove_student():
    roll = input("Enter the roll number of the student to delete: ")
    final_check = input(f"Are you sure you want to delete student with roll number {roll}? (y/n): ")
    
    #if user wants to delete the record
    if final_check == "y":
        #Reads all the lines in the file
        with open("students.csv","r") as file:
            lines = file.readlines()
            
        #Then adds them back to the file except the user specified one
        with open("students.csv", "w") as file:
            for index, line in enumerate(lines):
                if index == 0:  # write header
                    file.write(line)
                else:
                    parts = line.strip().split(",")
                    if len(parts) > 1 and parts[1] != roll:
                        file.write(line)
        print("Student record deleted successfully!")
    
    #Otherwise the user will be exited
    else:
        print("Thank you for using the Student Record Management System. Goodbye!")

    