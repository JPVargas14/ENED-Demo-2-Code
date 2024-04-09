import csv
import os

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
write_list_to_csv(my_list, directory, filename)