import os

while True:
    os.system("clear")

    if not (directory := input("Enter path the folder that you want to sort: ")):
        directory = "./"

    if os.path.exists(directory):
        break
    else:
        input("\nDirectory doesn't exists or not a folder\nPress ENTER to Try Again...")

directory_files = os.listdir(directory)

def extension_exporter(file): return file[file.find(".")+1::1]

files_extensions = list(set(map(extension_exporter, directory_files)))

for folder in files_extensions:
    folder_path = f"{directory}/{folder}"
    if not os.path.exists(folder_path):
        os.system(f"mkdir {folder_path}")

for file in directory_files:
    if os.path.isfile(f"{directory}/{file}"):
        os.system(
            f"mv {directory}/{file} {directory}/{extension_exporter(file)}")

input("Done Successfully :)\nPress ENTER To Exit...")
