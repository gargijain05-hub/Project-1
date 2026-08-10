import os
import shutil


def organize_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()

            if extension in [".jpg", ".jpeg", ".png", ".gif"]:
                folder = "Images"

            elif extension in [".pdf", ".docx", ".txt", ".xlsx"]:
                folder = "Documents"

            elif extension in [".mp3", ".wav"]:
                folder = "Audio"

            elif extension in [".mp4", ".avi", ".mkv"]:
                folder = "Videos"

            elif extension in [".zip", ".rar", ".7z"]:
                folder = "Archives"

            else:
                folder = "Others"

            folder_path = os.path.join(destination_folder, folder)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.move(file_path, os.path.join(folder_path, filename))

    print("File organization completed successfully.")