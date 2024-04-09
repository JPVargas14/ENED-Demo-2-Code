# The following module contains the code for a PTA grader at a
# Subtask station to be able to grade a student on their performance
# at said Subtask. When this module is called, it will open a checkbox
# to input the scores and it will return the scores in a CSV format.
# The input is the subtask name this will be graded.

import tkinter as tk
import SubtaskGenerator

def SubtaskStationGrader(currentSubtaskName):

    def submit():
        selected_options = []
        for i, option_var in enumerate(option_vars):
            if option_var.get():
                selected_options.append(options[i])
        print("Selected options:", selected_options)
        root.destroy()  # Close the window`

    subtaskInfo = SubtaskGenerator.GetSubtaskInfo()
    currentSubtaskNumberOfZones = subtaskInfo[currentSubtaskName]

    # Generate options
    options = []

    for i in range(currentSubtaskNumberOfZones):
        options.append(str(i + 1))

    # Create the main window
    root = tk.Tk()
    root.title("Initial Task Score")

    # Variables to store the checkbox states
    option_vars = []

    # Create checkboxes
    for option in options:
        var = tk.BooleanVar()
        option_vars.append(var)
        checkbox = tk.Checkbutton(root, text=option, variable=var)
        checkbox.pack(anchor='w')

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack()

    # Run the GUI
    root.mainloop()

SubtaskStationGrader('SubtaskA')