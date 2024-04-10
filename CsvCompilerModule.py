import SubtaskGenerator
import csv
import os

def CsvCompilerForMasterFile():
    # Directory containing all of the target grading files
    gradingTargetDirectory = "Z:\Grading\Exam5\FinalDemoGradingTestFolder"

    # Filename and directory of the master file
    masterFilename = "MASTER_DemoGrading.csv"
    masterFileDirectory = "Z:\Grading\Exam5"

    # Iterate through every file in the target directory to add their
    # contents into one dictionary
    combinedListOfDicts = []

    for filename in os.listdir(gradingTargetDirectory):
        currentFilePath = os.path.join(gradingTargetDirectory, filename)

        with open(currentFilePath, 'r') as currentFile:
            dictReader = csv.DictReader(currentFile)
            listOfDicts = list(dictReader)

        combinedListOfDicts += listOfDicts

        print(combinedListOfDicts)
        print("\n--------------------------------------------------\n")

    listOfGradedTeamNumbers = []
    masterListOfDicts = {}
    for d in combinedListOfDicts:
        currentTeamNumber = d['Team Number']
        if currentTeamNumber in listOfGradedTeamNumbers: # case where grades exist for this team
            # Loop through the values in dictionary to append values where empty and override values when greater
            print(combinedListOfDicts)
        else:
            listOfGradedTeamNumbers.append(currentTeamNumber)
           
        
CsvCompilerForMasterFile()
