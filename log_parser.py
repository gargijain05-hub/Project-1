def parse_log_file(log_file):
    info_count = 0
    warning_count = 0
    error_count = 0

    with open(log_file, "r") as file:
        for line in file:
            if "INFO" in line:
                info_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "ERROR" in line:
                error_count += 1

    report = (
        "LOG ANALYSIS REPORT\n"
        "===================\n\n"
        f"INFO messages: {info_count}\n"
        f"WARNING messages: {warning_count}\n"
        f"ERROR messages: {error_count}\n"
    )

    print("\n----- LOG SUMMARY -----")
    print(f"INFO messages: {info_count}")
    print(f"WARNING messages: {warning_count}")
    print(f"ERROR messages: {error_count}")

    with open("log_report.txt", "w") as report_file:
        report_file.write(report)

    print("\nLog report saved as log_report.txt")

    return info_count, warning_count, error_count