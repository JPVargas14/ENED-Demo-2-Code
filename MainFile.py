import SubtaskGenerator
import SubtaskStationGrader
import CsvWriter

def main():

    # Initialize given variables for specific demo
    subtaskInfo = SubtaskGenerator.GetSubtaskInfo()

    # Request user inputs to setup conditions
    subtaskStationName = "blank"
    while subtaskStationName not in subtaskInfo:
        if subtaskStationName != "blank":
            print("\nSubtask Name invalid. Please try again\n")

        subtaskStationName = input('Which subtask are you grading?\nEnter the letter corresponding to the station (A for Subtask A, B for Subtask B, etc, or F for the Final Track): ')

        if subtaskStationName == "F":
            subtaskStationName = "Final Track"

        else:
            subtaskStationName = "Subtask " + subtaskStationName

    correctSixPlusTwo = "N"
    while correctSixPlusTwo != "Y":
        sixPlusTwo = input("\nWhat is your 6+2? ")

        print("\nYou inputted {0} as your 6+2. Is this correct?".format(sixPlusTwo))
        correctSixPlusTwo = input("Y for Yes or N for No ")

    # Create the necessary grading sheet if it does not exist and create the column headers.
    directory = "Z:\Grading\Exam5\FinalDemoGradingTestFolder"
    gradingFilename = CsvWriter.create_csv_with_username(directory, sixPlusTwo)

    # Grading Loop
    isGradingHappening = True
    while isGradingHappening == True:
        # Input the team number for the team about to be graded
        isTeamNumberCorrect = "N"
        while isTeamNumberCorrect != "Y":
            currentTeamNumber = input("\nInput the current team number ")
            print("\nYou inputted {0} as the team number. Is this correct?".format(currentTeamNumber))
            isTeamNumberCorrect = input("Y for Yes or N for No ")

        # Run the Subtask Station Grader for the current team
        currentGradeList = []
        SubtaskStationGrader.RunSubtaskStationGrader(subtaskStationName, currentGradeList)

        # Output the results to the CSV file
        CsvWriter.InputGradesToCsv(currentGradeList, currentTeamNumber, directory, gradingFilename, subtaskStationName)

        gradeAgainStatus = "blank"
        while gradeAgainStatus != "Y" and gradeAgainStatus != "N":
            print("\nWould you like to grade the same station again?")
            gradeAgainStatus = input("Y for Yes or N for No ")

        if gradeAgainStatus == "Y":
            isGradingHappening = True
            isTeamNumberCorrect = "N"

        elif gradeAgainStatus == "N":
            isGradingHappening = False

main()