import tkinter as tk
from collections import deque

def event_queue():
    # Create a deque to store the queue of teams
    team_queue = deque()

    # Function to handle submission of new team numbers
    def add_team():
        team_number = team_input.get()
        if team_number:
            team_queue.append(team_number)
            team_input.delete(0, tk.END)  # Clear the input field
            update_display_window()

    # Function to handle popping the next team from the queue
    def pop_next_team():
        if team_queue:
            # Pop the next team from the front of the queue
            next_team = team_queue.popleft()
            # Set the popped team as "Next In Line" and "Ready to Go to Station"
            next_in_line_label.config(text=f"Next In Line: {next_team}")
            ready_to_go_label.config(text=f"Ready to Go to Station: {next_team}")
            # Update the display window to reflect the removal of the team from the queue
            update_display_window()

    # Function to edit a team number in the queue
    def edit_team():
        if team_queue:
            # Ask for the index to edit
            index = tk.simpledialog.askinteger("Edit Team", "Enter the index of the team you want to edit (1-based index):") - 1
            # Check if the index is valid
            if 0 <= index < len(team_queue):
                new_team_number = tk.simpledialog.askstring("Edit Team", "Enter the new team number:")
                if new_team_number:
                    team_queue[index] = new_team_number
                    update_display_window()

    # Function to update the display window with the current queue
    def update_display_window():
        # Display the teams in line
        if len(team_queue) > 0:
            in_line_label.config(text=f"In Line: {', '.join(team_queue)}")
        else:
            in_line_label.config(text="In Line: None")

        # Update the 'Next In Line' and 'Ready to Go to Station' labels
        if len(team_queue) > 0:
            next_in_line_label.config(text=f"Next In Line: {team_queue[0]}")
        else:
            next_in_line_label.config(text="Next In Line: None")

    # Create the input window
    input_root = tk.Tk()
    input_root.title("Input Window")

    # Entry for team number
    team_input = tk.Entry(input_root, font=("Arial", 14), width=20)
    team_input.grid(row=0, column=0, padx=10, pady=10)

    # Add team button
    add_button = tk.Button(input_root, text="Add Team", command=add_team)
    add_button.grid(row=0, column=1, padx=10, pady=10)

    # Pop next team button
    pop_button = tk.Button(input_root, text="Move Next Team", command=pop_next_team)
    pop_button.grid(row=1, column=0, padx=10, pady=10)

    # Create the display window
    display_root = tk.Toplevel(input_root)
    display_root.title("Display Window")

    # Labels to visualize the queue
    in_line_label = tk.Label(display_root, text="In Line: None", font=("Arial", 16))
    in_line_label.grid(row=0, column=0, padx=10, pady=10)

    next_in_line_label = tk.Label(display_root, text="Next In Line: None", font=("Arial", 16))
    next_in_line_label.grid(row=1, column=0, padx=10, pady=10)

    ready_to_go_label = tk.Label(display_root, text="Ready to Go to Station: None", font=("Arial", 16))
    ready_to_go_label.grid(row=2, column=0, padx=10, pady=10)

    # Run the GUI
    input_root.mainloop()

# Call the function to run the program
event_queue()
