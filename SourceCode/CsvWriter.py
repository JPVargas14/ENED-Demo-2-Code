import csv
import os
import SubtaskGenerator

def create_csv_with_username(directory_path, username):
    # Ensure the directory exists
    os.makedirs(directory_path, exist_ok=True)

    # Construct file name
    filename = username + "_DemoGradingFile.csv"
    
    # Construct the full path to the CSV file
    csv_file_path = os.path.join(directory_path, filename)
    
    # Check if the file already exists
    file_exists = os.path.isfile(csv_file_path)
    
    # Open the CSV file in append mode
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # If the file doesn't exist, write a header row
        if not file_exists:
            writer.writerow(SubtaskGenerator.GetSubtaskGradingColumns())  # Adjust headers as needed
            print(f"CSV file '{filename}' created successfully.")
        else:
            print(f"CSV file '{filename}' already exists.")

    return filename

def InputGradesToCsv(firstTryGradeList, retryGradeList, teamNumber, directoryPath, fileName, subtaskName):
    # Ensure the directory exists
    os.makedirs(directoryPath, exist_ok=True)
    
    # Construct the full path to the CSV file
    csv_file_path = os.path.join(directoryPath, fileName)

    subtaskGradingColumns = SubtaskGenerator.GetSubtaskGradingColumns()
    with open(csv_file_path, 'a') as gradingFile: 
        writer = csv.DictWriter(gradingFile, fieldnames=subtaskGradingColumns)

        firstTryColumnName = subtaskName + " Zones"
        firstTryOutputString = ', '.join(firstTryGradeList)

        # If there is a grade for the retries
        if len(retryGradeList ) != 0:
            retryColumnName = subtaskName + " Retry Zones"
            retryOutputString = ', '.join(retryGradeList)

            writer.writerow({'Team Number':teamNumber, firstTryColumnName:firstTryOutputString, retryColumnName:retryOutputString})
        else:
            writer.writerow({'Team Number':teamNumber, firstTryColumnName:firstTryOutputString})

# Example usage:
my_list = ["Value1", "Value2"]  # Example list to be written to CSV
directory = "Z:\Grading\Exam5\FinalDemoGradingTestFolder"  # Path to the directory where CSV file will be located
filename = "vargasjp_FinalDemoGrading.csv"  # Name of the CSV file

# Call the function to write the list to the CSV file
#write_list_to_csv(my_list, directory, filename)

# Call the function to create a CSV file with the username as filename
# create_csv_with_username(directory)