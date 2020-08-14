from validator import check_task, exit_script

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        exit_script("Need to input number of task")

    try:
        task_number = int(sys.argv[1])
        check_task(task_number)
    except ValueError:
        exit_script("Need to input number of task")
