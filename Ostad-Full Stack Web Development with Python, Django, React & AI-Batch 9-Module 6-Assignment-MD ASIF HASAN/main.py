import add
import view
import search
import remove
import utility


def menu():
    while True:
        print("\n=========== MENU ===========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Exit")
        print("============================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add.add_student()

        elif choice == '2':
            view.view_students()

        elif choice == '3':
            search.search_student()

        elif choice == '4':
            remove.remove_student()

        elif choice == '5':
            print("\nThank you for using the Student Record Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    menu()
