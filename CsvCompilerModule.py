import SubtaskGenerator
import csv
import os

def CsvCompilerForMasterFile():
    # Directory containing all of the target grading files
    gradingTargetDirectory = "Z:\Grading\Exam5\FinalDemoGradingTestFolder"

    # Filename and directory of the master file
    masterFilename = "MASTER_DemoGrading.csv"
    masterFileDirectory = "Z:\Grading\Exam5"
    masterFilePath = os.path.join(masterFileDirectory, masterFilename)

    # Iterate through every file in the target directory to add their
    # contents into one dictionary
    masterListOfDicts = []

    for filename in os.listdir(gradingTargetDirectory):
        currentFilePath = os.path.join(gradingTargetDirectory, filename)

        with open(currentFilePath, 'r') as currentFile:
            dictReader = csv.DictReader(currentFile)
            listOfDicts = list(dictReader)

        masterListOfDicts += listOfDicts


        # print(masterListOfDicts)
        # print("\n--------------------------------------------------\n")

    dictOfGradedTeamNumbers = {}

    index = 0
    while index < len(masterListOfDicts):

        # Check if team number exists and deletes dictionary if not
        if masterListOfDicts[index]['Team Number']:
            currentTeamNumber = masterListOfDicts[index]['Team Number']
        else:
            del masterListOfDicts[index]
            continue

        if currentTeamNumber in dictOfGradedTeamNumbers.keys(): # case where grades exist for this team
            # Find first instance of team number
            originalIndex = dictOfGradedTeamNumbers[currentTeamNumber]
    
            # Loop through the values in dictionary to append values where empty and override values when greater
            for key in masterListOfDicts[originalIndex]: 
                # Score for this subtask exists
                if masterListOfDicts[originalIndex][key]:
                    if masterListOfDicts[index][key] and key != 'Team Number':
                        # Find which one is better and make the better one the retry
                        originalScore = list(masterListOfDicts[originalIndex][key].split(", "))
                        newScore = list(masterListOfDicts[index][key].split(", "))

                        # replace the orignal score with the new one if the new one is greater
                        if len(newScore) >  len(originalScore):
                            masterListOfDicts[originalIndex][key] = masterListOfDicts[index][key]
                            
                else:
                    # replace
                    masterListOfDicts[originalIndex][key] = masterListOfDicts[index][key]
            del masterListOfDicts[index]
            index -= 1
                    
        else:
            dictOfGradedTeamNumbers[currentTeamNumber] = index
        index += 1

    # Print to master file
    with open(masterFilePath, 'w', encoding='utf8', newline='') as masterFile:
        fc = csv.DictWriter(masterFile, 
                            fieldnames=masterListOfDicts[0].keys(),

                        )
        fc.writeheader()
        fc.writerows(masterListOfDicts)
           
        
CsvCompilerForMasterFile()
