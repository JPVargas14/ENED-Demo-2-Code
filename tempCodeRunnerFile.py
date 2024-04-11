import tkinter as tk
from tkinter import simpledialog
from collections import deque

def event_queue():
    # Create a deque to store the queue of teams
    team_queue = deque()
    
    # Function for the input window
    def add_team():
        team_number = team_input.get()
        if team_number:
            team_queue.append(team_number)
            team_input.delete(0, tk.END)  # Clear the input field
            update_display_window()
    
    def pop_next_team():
        if team_queue:
            team_number = team_queue.popleft()
            next_in_line_label.config(text=f"Next In Line: {team_number}")
            ready_to_go_label.config(text=f"Ready to Go to Station: {team_number}")
            update_display_window()

    def edit_team():
        if team_queue:
            index = simpledialog.askinteger("Edit Team", "Enter the index of the team you want to edit (1-based index):") - 1
            if 0 <= index < len(team_queue):
                new_team_number = simpledialog.askstring("Edit Team", "Enter the new team number:")
                if new_team_number:
                    team_queue[index] = new_team_number
                    update_display_window()
    
    def update_display_window():
        # Update the 'In Line' label with the queue
        in_line_list = list(team_queue)
        if in_line_list:
            # Exclude the next in line team from the 'In Line' list
            in_line_list_str = ', '.join(in_line_list)
        else:
            in_line_list_str = "None"
        in_line_label.config(text=f"In Line: {in_line_list_str}")
        
        # If the queue is empty, set 'Next In Line' and 'Ready to Go' to None
        if team_queue:
            next_in_line = team_queue[0]
            next_in_line_label.config(text=f"Next In Line: {next_in_line}")
        else:
            next_in_line_label.config(text="Next In Line: None")
        
        ready_to_go_label.config(text="Ready to Go to Station: None")
    
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
    pop_button = tk.Button(input_root, text="Pop Next Team", command=pop_next_team)
    pop_button.grid(row=1, column=0, padx=10, pady=10)

    # Edit team button
    edit_button = tk.Button(input_root, text="Edit Team", command=edit_team)
    edit_button.grid(row=1, column=1, padx=10, pady=10)

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
