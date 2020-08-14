from validator import check_task, exit_script

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        exit_script("Need to input number of task")

    try:
        task_number = int(sys.argv[1])
        path_to_repo = sys.argv[2]
        check_task(task_number, path_to_repo)
    except ValueError:
        exit_script("Need to input number of task")
