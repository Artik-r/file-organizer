import os
import shutil
from pathlib import Path

# ==========================================================
# Target Folder
# ==========================================================

TARGET_FOLDER = "test_folder"


# ==========================================================
# File Categories
# ==========================================================

FILE_TYPES = {

    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],

    "Documents": [".pdf", ".doc", ".docx", ".txt"],

    "Videos": [".mp4", ".mkv", ".avi", ".mov"],

    "Music": [".mp3", ".wav", ".aac"],

    "Python": [".py"],

    "Archives": [".zip", ".rar", ".7z"]

}



# ==========================================================
# Get All Files
# ==========================================================

def get_files():

    folder = Path(TARGET_FOLDER)

    if not folder.exists():

        print("❌ Folder not found.")
        return []

    files = []

    for item in folder.iterdir():

        if item.is_file():

            files.append(item)

    return files
# ==========================================================
# Get File Extension
# ==========================================================

def get_extension(file):

    return file.suffix.lower()
# ==========================================================
# Get Category
# ==========================================================

def get_category(extension):

    for category, extensions in FILE_TYPES.items():

        if extension in extensions:

            return category

    return "Others"


# ==========================================================
# Create Folder
# ==========================================================

def create_folder(category):

    folder_path = Path(TARGET_FOLDER) / category

    folder_path.mkdir(exist_ok=True)

    return folder_path


# ==========================================================
# Move File
# ==========================================================

def move_file(file, destination):

    shutil.move(

        str(file),

        str(destination / file.name)

    )


# ==========================================================
# Organize Files
# ==========================================================

def organize_files():

    files = get_files()

    if not files:

     print("\n✅ Everything is already organized!")
     print("No new files were found in the target folder.")

    return

    moved = 0

    print("\nStarting organization...\n")

    for file in files:

        extension = get_extension(file)

        category = get_category(extension)

        destination = create_folder(category)

        move_file(file, destination)

        print(f"✅ {file.name}  →  {category}")

        moved += 1

    print("\n" + "=" * 60)
    print("           ORGANIZATION COMPLETE")
    print("=" * 60)
    print(f"\nFiles Organized : {moved}")

# ==========================================================
# Main
# ==========================================================

def main():

    print("\n" + "=" * 60)
    print("                FILE ORGANIZER")
    print("=" * 60)

    print("\nAutomatically organizes files into folders.")
    print("\nSupported Categories")
    print("-" * 60)

    print("📷 Images")
    print("📄 Documents")
    print("🎵 Music")
    print("🎥 Videos")
    print("🐍 Python")
    print("📦 Archives")
    print("📁 Others")

    input("\nPress Enter to start organizing...")

    organize_files()

    print("\n🎉 Thank you for using File Organizer!")

if __name__ == "__main__":
    main()
