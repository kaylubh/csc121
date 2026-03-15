#
# Caleb Hemphill
# 03/15/2026
# Log file category counter
#

def main():
    """
    Counts the number or each type of error message (CRITICAL, ERROR, WARNING, INFO) in a log file named 'program.log'
    and stored in the same directory level and displays the counts to the user.
    """
    critical_count = 0
    error_count = 0
    warning_count = 0
    info_count = 0
    other_count = 0

    # open file and handle missing file error
    try:
        log_file = open('program.log', 'r')
    except FileNotFoundError:
        print('File program.log not found')
        return

    # count error message types
    for line in log_file:
        line_parts = line.split()
        error_category = line_parts[3]

        if error_category == 'CRITICAL':
            critical_count += 1
        elif error_category == 'ERROR':
            error_count += 1
        elif error_category == 'WARNING':
            warning_count += 1
        elif error_category == 'INFO':
            info_count += 1
        else:
            other_count += 1

    # display error counts
    print(f'CRITICAL: {critical_count}')
    print(f'ERROR: {error_count}')
    print(f'WARNING: {warning_count}')
    print(f'INFO: {info_count}')
    print(f'UNKNOWN: {other_count}')

    log_file.close()


main()
