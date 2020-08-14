import sys
import os
from enum import Enum
from git import Repo, InvalidGitRepositoryError, NoSuchPathError


class TaskType(Enum):
	initialSetup = 1


def check_task(task_number, path):
	if task_number == TaskType.initialSetup.value:
		try:
			repo = Repo(path)
		except InvalidGitRepositoryError:
			print("Your repo is not initialised!")
			exit_script("Please use git initialisation command")
		except NoSuchPathError:
			print("Cannot find folder")
			exit_script("Please make sure your path is correct")


def exit_script(text):
	print(text)
	sys.exit()
