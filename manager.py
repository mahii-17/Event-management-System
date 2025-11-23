import os
import webbrowser
from event import Event


class EventManager:
    def __init__(self, filename="events_data.txt"):
        self.filename = filename
        self.events = []
        self.load_from_file()

    def load_from_file(self):
        try:
            if not os.path.exists(self.filename):
                return

            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        new_event = Event(
                            data[0], data[1], float(data[2]), int(data[3]))
                        self.events.append(new_event)
        except Exception as e:
            print(f"Error loading file: {e}")

    def save_to_file(self):
        try:
            with open(self.filename, "w") as file:
                for event in self.events:
                    file.write(
                        f"{event.name},{event.date},{event.price},{event.attendees}\n")
            print("Data saved successfully.")
        except IOError as e:
            print(f"Could not save data: {e}")

    def add_event(self):
        print("\n--- Add New Event ---")
        name = input("Event Name: ")
        date = input("Event Date (YYYY-MM-DD): ")

        while True:
            try:
                price = float(input("Ticket Price: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number for price.")

        new_event = Event(name, date, price, 0)
        self.events.append(new_event)
        self.save_to_file()
        print("Event added!")

    def book_ticket(self):
        print("\n--- Book Ticket ---")
        if not self.events:
            print("No events available.")
            return

        for i, event in enumerate(self.events):
            print(f"{i + 1}. {event.name} (Price: ${event.price})")

        while True:
            try:
                choice = int(input("Select Event Number: "))
                if 1 <= choice <= len(self.events):
                    selected_event = self.events[choice - 1]
                    selected_event.attendees += 1
                    print(f"Ticket booked for {selected_event.name}!")
                    self.save_to_file()
                    break
                else:
                    print("Invalid choice number.")
            except ValueError:
                print("Please enter a valid integer.")

    def generate_html_report(self):
        html_content = """
        <html>
        <head>
            <title>Event Management Dashboard</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 20px; }
                h1 { color: #333; }
                table { width: 100%; border-collapse: collapse; margin-top: 20px; box-shadow: 0 0 20px rgba(0,0,0,0.1); }
                th, td { padding: 15px; text-align: left; border-bottom: 1px solid #ddd; background-color: white; }
                th { background-color: #009879; color: white; }
                tr:hover { background-color: #f5f5f5; }
                .card { background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
            </style>
        </head>
        <body>
            <h1>Event Management System Report</h1>
            <div class="card">
                <h3>Total Events: """ + str(len(self.events)) + """</h3>
            </div>
            <table>
                <tr>
                    <th>Event Name</th>
                    <th>Date</th>
                    <th>Price</th>
                    <th>Attendees Booked</th>
                    <th>Total Revenue</th>
                </tr>
        """

        for event in self.events:
            revenue = event.price * event.attendees
            html_content += f"""
                <tr>
                    <td>{event.name}</td>
                    <td>{event.date}</td>
                    <td>${event.price}</td>
                    <td>{event.attendees}</td>
                    <td>${revenue}</td>
                </tr>
            """

        html_content += """
            </table>
        </body>
        </html>
        """
        report_path = "reports/dashboard.html"
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        with open("dashboard.html", "w") as f:
            f.write(html_content)

        print("HTML Report Generated!")
        file_path = os.path.abspath("dashboard.html")
        webbrowser.open("file://" + file_path)
