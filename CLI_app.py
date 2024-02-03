import os

# Assign directory variable to folder path
# If user does not enter anything, directory is the folder where the program is located
while True:
    # To clear cmd/terminal for better experience
    os.system("clear")

    if not (directory := input("Enter path of the folder that you want to sort: ")):
        directory = "./"

    if os.path.exists(directory):
        break
    else:
        input("\nDirectory doesn't exists or not a folder\nPress ENTER to Try Again...")

# List files in directory
directory_files = os.listdir(directory)

# Function to export extension of given file
def extension_exporter(file): return file[file.find(".")+1::1]

# a list of all extensions that exists in directory without duplicates
files_extensions = list(set(map(extension_exporter, directory_files)))

# Create folder for each extension in directory
for folder in files_extensions:
    folder_path = f"{directory}/{folder}"
    if not os.path.exists(folder_path):
        os.system(f"mkdir {folder_path}")

# Move each file to it's own extension folder
for file in directory_files:
    if os.path.isfile(f"{directory}/{file}"):
        os.system(
            f"mv {directory}/{file} {directory}/{extension_exporter(file)}")

# FINISH
input("Done Successfully :)\nPress ENTER To Exit...")
