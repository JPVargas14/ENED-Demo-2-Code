# The following module contains the code for a PTA grader at a
# Subtask station to be able to grade a student on their performance
# at said Subtask. When this module is called, it will open a checkbox
# to input the scores and it will return the scores in a CSV format.
# The input is the subtask name this will be graded.

import tkinter as tk
import SubtaskGenerator

def RunSubtaskStationGrader(currentSubtaskName, selected_options_first_try, selected_options_retry, teamNumber):

    def submit():
        for i, var in enumerate(var_first_try):
            if var.get():
                selected_options_first_try.append(str(i + 1))
        for i, var in enumerate(var_retry):
            if var.get():
                selected_options_retry.append(str(i + 1))
        root.destroy()  # Close the window

    subtaskInfo = SubtaskGenerator.GetSubtaskInfo()
    currentSubtaskNumberOfZones = subtaskInfo[currentSubtaskName]

    # Generate options
    options = []

    for i in range(currentSubtaskNumberOfZones):
        options.append(str(i + 1))

    # Create the main window
    root = tk.Tk()
    root.title(currentSubtaskName + " Score: Team " + str(teamNumber))
    root.geometry("730x500")  # Set the size of the window

    # Labels for titles
    tk.Label(root, text=(currentSubtaskName + " Score: Team " + str(teamNumber)), font=("Arial", 30), anchor="center").grid(row=0, columnspan=6, sticky="nsew")
    tk.Label(root, text="First Try Zones", font=("Arial", 24), anchor="center").grid(row=2, columnspan=6, sticky="nsew")
    tk.Label(root, text="Retry Zones", font=("Arial", 24), anchor="center").grid(row=6, columnspan=6, sticky="nsew")

    # Empty labels for whitespace
    tk.Label(root, text="", font=("Arial", 20)).grid(row=1, columnspan=6)
    tk.Label(root, text="", font=("Arial", 20)).grid(row=3, columnspan=6)
    tk.Label(root, text="", font=("Arial", 20)).grid(row=5, columnspan=6)
    tk.Label(root, text="", font=("Arial", 20)).grid(row=7, columnspan=6)
    tk.Label(root, text="", font=("Arial", 20)).grid(row=9, columnspan=6)


    # Variables to store checkbox states
    var_first_try = [tk.BooleanVar() for _ in range(6)]
    var_retry = [tk.BooleanVar() for _ in range(6)]

    # Create checkboxes for first try
    for i, var in enumerate(var_first_try):
        checkbox = tk.Checkbutton(root, text="Zone " + str(i+1), font=("Arial", 20), variable=var, anchor="center",)
        checkbox.grid(row=4, column=i, sticky="nsew")

    # Create checkboxes for retry   
    for i, var in enumerate(var_retry):
        checkbox = tk.Checkbutton(root, text="Zone " + str(i+1), font=("Arial", 20), variable=var, anchor="center")
        checkbox.grid(row=8, column=i, sticky="nsew")

    # Submit button
    submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=submit, anchor="center")
    submit_button.grid(row=10, column=2, columnspan=2, sticky="nsew")

    # Run the GUI
    root.mainloop()


# emptyList1 = []
# emptyList2 = []
# RunSubtaskStationGrader('Subtask A', emptyList1, emptyList2, 342)