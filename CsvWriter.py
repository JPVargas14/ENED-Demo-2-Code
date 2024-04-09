import csv
import os

def create_csv_with_username(directory_path):
    # Ensure the directory exists
    os.makedirs(directory_path, exist_ok=True)
    
    # Ask the user to input their username
    username = input("Please enter your username: ")

    # Construct file name
    filename = username + "_DemoGradingFile"
    
    # Construct the full path to the CSV file
    csv_file_path = os.path.join(directory_path, f"{filename}.csv")
    
    # Check if the file already exists
    file_exists = os.path.isfile(csv_file_path)
    
    # Open the CSV file in append mode
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # If the file doesn't exist, write a header row
        if not file_exists:
            writer.writerow(["Team Number", "Subtask A Zones", "Subtask B Zones", "Subtask C Zones", "Full Track Zones", 
                             "Subtask A Retry Zones", "Subtask B Retry Zones", "Subtask C Retry Zones"])  # Adjust headers as needed
            print(f"CSV file '{filename}.csv' created successfully.")
        else:
            print(f"CSV file '{filename}.csv' already exists.")

def write_list_to_csv(input_list, directory_path, file_name):
    # Ensure the directory exists
    os.makedirs(directory_path, exist_ok=True)
    
    # Construct the full path to the CSV file
    csv_file_path = os.path.join(directory_path, file_name)
    
    # Determine whether the file already exists
    file_exists = os.path.isfile(csv_file_path)
    
    # Open the CSV file in append mode
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # If the file doesn't exist, write the list with header
        if not file_exists:
            writer.writerow(["Column1", "Column2"])  # Adjust headers as needed
            writer.writerow(input_list)
        else:
            writer.writerow(input_list)

# Example usage:
my_list = ["Value1", "Value2"]  # Example list to be written to CSV
directory = "Z:\Grading\Exam5\FinalDemoGradingTestFolder"  # Path to the directory where CSV file will be located
filename = "vargasjp_FinalDemoGrading.csv"  # Name of the CSV file

# Call the function to write the list to the CSV file
#write_list_to_csv(my_list, directory, filename)

# Call the function to create a CSV file with the username as filename
create_csv_with_username(directory)