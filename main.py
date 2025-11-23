from manager import EventManager

if __name__ == "__main__":
    app = EventManager()

    while True:
        print("\n=== EVENT MANAGER SYSTEM ===")
        print("1. Add New Event")
        print("2. Book Ticket")
        print("3. Generate HTML Report")
        print("4. Exit")

        user_input = input("Enter choice: ")

        if user_input == '1':
            app.add_event()
        elif user_input == '2':
            app.book_ticket()
        elif user_input == '3':
            app.generate_html_report()
        elif user_input == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")
