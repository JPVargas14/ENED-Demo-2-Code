# The following module contains the code for a PTA grader at a
# Subtask station to be able to grade a student on their performance
# at said Subtask. When this module is called, it will open a checkbox
# to input the scores and it will return the scores in a CSV format.
# The input is the subtask name this will be graded.

import tkinter as tk
import SubtaskGenerator

def RunSubtaskStationGrader(currentSubtaskName, selected_options_first_try, selected_options_retry):

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
    root.title("Task Score")

    # Variables to store the checkbox states
    option_vars = []

    # Variables to store checkbox states
    var_first_try = [tk.BooleanVar() for _ in range(6)]
    var_retry = [tk.BooleanVar() for _ in range(6)]

    # Create checkboxes for first try
    for i, var in enumerate(var_first_try):
        checkbox = tk.Checkbutton(root, text="Zone " + str(i+1), variable=var)
        checkbox.grid(row=0, column=i)

    # Create checkboxes for retry
    for i, var in enumerate(var_retry):
        checkbox = tk.Checkbutton(root, text="Zone " + str(i+1), variable=var)
        checkbox.grid(row=1, column=i)

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=2, columnspan=6)

    # Run the GUI
    root.mainloop()

# RunSubtaskStationGrader('Subtask A')