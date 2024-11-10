import os
import shutil

# Define file type categories
file_categories = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []
}

# Organize files based on their types
def organize_files(directory):
    # Check if directory exists
    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        return

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)

        # Determine the folder category for the file
        category_folder = "Others"
        for category, extensions in file_categories.items():
            if file_extension.lower() in extensions:
                category_folder = category
                break

        # Create the category folder if it doesn't exist
        category_folder_path = os.path.join(directory, category_folder)
        if not os.path.exists(category_folder_path):
            os.makedirs(category_folder_path)

        # Move the file to the category folder
        shutil.move(file_path, os.path.join(category_folder_path, filename))
        print(f"Moved '{filename}' to '{category_folder}'")

    print("File organization complete!")

# Directory to organize (you can specify any directory here)
directory_to_organize = "C:/Users/YourUsername/Downloads"
organize_files(directory_to_organize)