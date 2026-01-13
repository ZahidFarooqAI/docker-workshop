# Import Path class from pathlib module
from pathlib import Path

# Get the current working directory
current_directory = Path.cwd()

# Get the name of the current Python file
current_file = Path(__file__).name

# Print which directory we are listing
print(f"Files in {current_directory}:")

# Loop through all items in the current directory
for filepath in current_directory.iterdir():
    
    # Skip the current script file itself
    if filepath.name == current_file:
        continue
    
    # Print the name of the file/folder
    print(f" - {filepath.name}")
    
    # If the item is a file, read and print its content
    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"  Content:\n{content}\n")

        
