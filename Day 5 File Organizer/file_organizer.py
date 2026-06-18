import os
import shutil

SOURCE_FOLDER = "test_folder"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"]
}


def organize_files():

    for file_name in os.listdir(SOURCE_FOLDER):

        file_path = os.path.join(SOURCE_FOLDER, file_name)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file_name)[1].lower()

            moved = False

            for folder, extensions in FILE_TYPES.items():

                if extension in extensions:

                    destination_folder = os.path.join(
                        SOURCE_FOLDER,
                        folder
                    )

                    os.makedirs(destination_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(destination_folder, file_name)
                    )

                    print(
                        f"Moved {file_name} → {folder}"
                    )

                    moved = True
                    break

            if not moved:

                other_folder = os.path.join(
                    SOURCE_FOLDER,
                    "Others"
                )

                os.makedirs(other_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(other_folder, file_name)
                )

                print(
                    f"Moved {file_name} → Others"
                )


organize_files()

print("\nFiles Organized Successfully!")