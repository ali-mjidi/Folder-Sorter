import os

os.system("clear")

home_directory = os.environ["HOME"]
directory = f"{home_directory}/Desktop/test"
directory_files = os.listdir(directory)

extension_exporter = lambda file: file[file.find(".")+1::1]

files_extensions = list(set(map(extension_exporter, directory_files)))
    
for folder in files_extensions:
    folder_path = f"{directory}/{folder}"
    if not os.path.exists(folder_path):
        os.system(f"mkdir {folder_path}")

for file in directory_files:
    if os.path.isfile(f"{directory}/{file}"):
        os.system(f"mv {directory}/{file} {directory}/{extension_exporter(file)}")

print("Done Successfully :)")