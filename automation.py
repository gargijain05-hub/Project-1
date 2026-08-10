from file_manager import organize_files
from log_parser import parse_log_file


def run_automation():
    source_folder = "test_files"
    destination_folder = "organized_files"
    log_file = "sample.log"

    print("Starting automated file management...")

    organize_files(source_folder, destination_folder)

    print("\nStarting automated log parsing...")

    parse_log_file(log_file)

    print("\nAutomation completed successfully.")


if __name__ == "__main__":
    run_automation()