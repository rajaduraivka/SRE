import os
import time

# List of directories to scan
directories = [
    "/Users/bijak/Documents",
    "/Users/bijak/Downloads",
    "/Users/bijak/Desktop"
]  # Add more paths if needed

# Get current time
current_time = time.time()

# Define file extensions to delete
extensions = (".docx", ".mkv")

# Time threshold (7 days in seconds)
time_threshold = 7 * 24 * 60 * 60  

# Iterate over multiple directories
for directory in directories:
    if os.path.exists(directory):  # Check if directory exists
        print(f"Scanning directory: {directory}")
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Check if it's a file and has the correct extension
            if os.path.isfile(file_path) and file_path.lower().endswith(extensions):
                file_modified_time = os.path.getmtime(file_path)  # Get last modified time

                # Check if file is older than a week
                if current_time - file_modified_time > time_threshold:
                    print(f"Deleting: {file_path}")
                    os.remove(file_path)  # Delete the file
    else:
        print(f"Directory not found: {directory}")

print("Cleanup complete!")

