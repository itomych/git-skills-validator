import sys
import os
from enum import Enum


class TaskType(Enum):
	initialSetup = 1


def check_task(task_number):
	if task_number == TaskType.initialSetup.value:
		if os.path.isdir("./repo"):
			exit_script("All correct! Nice one!")
		else:
			exit_script("Folder is not created")


def exit_script(text):
	print(text)
	sys.exit()
