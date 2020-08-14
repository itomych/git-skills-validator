_Assumed using git command line utility. All commands (like creating files or folders, adding text to files, etc) should be console commands._  
_For each task you should provide console commands that are needed to complete it._

### Basic:

1.  Create folder "GitSkillUp", create git repo
2.  Locally create branch with name "develop" and switch to that branch
3.  Set up name and e-mail address: username user1, user email  [user1@itomy.ch](mailto:user1@itomy.ch)
4.  Create in root folder of project text file base.txt with contents: "This is base file in root folder"
5.  Switch to that branch
6.  Save changes locally in git
7.  Add tag with name "0.0.1"
8.  Simulate error when committing - in base.txt file add "This is not base file" text
9.  In project's root create folder with name "Base"
10.  Move "base.txt" file to folder with name "Base"
11.  Commit changes with commit message "Added base file to project"
12.  Revert previous commit
13.  On your favorite code hosting (bitbucket or github) create remote repo with name "Git-skillup"
14.  Add link to remote repo
15.  Give this link a short name
16.  On code hosting create branch "develop". Set your local branch "develop" track changes of remote branch "develop"
17.  Print list of remote branches
18.  Download contents of remote "develop" branch. Print changes of git database.
19.  Push changes to remote repo
20.  Simulate second user - download repo to another folder
21.  Setup second user name and email username user2, user email  [user2E@itomy.ch](mailto:user2E@itomy.ch)
22.  As user user2 in project's root create file "changes_history.txt" with text "Created project", commit changes with message "Added history file" and push them

  

### Git flow branching:

1.  As user user1 create feature with name "derived-file-feature"
2.  Create text file "derived1.txt" with text "This is derived file"
3.  Commit changes
4.  Simulating conflict: as user user2 in "develop" branch create file with name "derived1.txt". Add text "This is derived file" to this file
5.  Commit & push changes to remote repo
6.  As user user1 try to finish feature "derived-file-feature" (feature branch should NOT be deleted)
7.  As user user1 resolve conflicts
8.  As user user1 finish feature "derived-file-feature" (feature branch should NOT be deleted)
9.  As user user1 append this text to file "changes_history.txt" "Added derived file". Commit and push changes with message "Updated history file"
10.  As user user2 create feature with name "readme"
11.  As user user2 create file "[readme.md](http://readme.md/)" with text "This is readme file with general info about project"
12.  As user user2 append this text to file "changes_history.txt" "Added readme". Commit and push changes with message "Updated history file"
13.  As user user2 commit with message "Created readme file" and push changes to remote
14.  As user user1 move commit from "readme" branch to develop and push changes
15.  As user user1 make sure that file "[readme.md](http://readme.md/)" is not included by vcs folder
16.  As user user2 delete feature-branch "readme"
17.  As user user2 create branch named "git-ignore" from develop and switch to it
18.  As user user2 create ignore file. Your repo should ignore files with extensions .md, .DS_Store, .fseventsd, .Trashes. Commit your changes with message "Added ignore file", then push them
19.  As user user1 create branch with name "code-review" for code review of "git-ignore" branch. This branch should have no history
20.  As user user1 in project's root create folder with name "CodeReviews". This branch should remain empty but should be presented in repository.
21.  As user user1 commit changes with message "Code review folder created". Push changes to repo
22.  As user user1 merge branch "code-review" to "develop" branch
23.  As user user1 change author of commit with message "Added ignore file" to user1

  

### Git-flow commits manipulation:

1.  As user user1 create feature with name "text-messages" and switch to it
2.  As user user1 in project's root create folder "Messages"
3.  As user user1 in folder "Messages" create file "Text1" with text "This is message text file #1" and commit changes with message "Added txt file 1"
4.  As user user1 in folder "Messages" create file "Text2" with text "This is message text file #2" and commit changes with message "Added txt file 2"
5.  As user user1 in folder "Messages" create file "Text3" with text "This is message text file #3" and commit changes with message "Added txt file 3"
6.  As user user1 in folder "Messages" create file "Text4" with text "This is message text file #4" and commit changes with message "Added txt file 4"
7.  As user user1 push changes to remote repo
8.  As user user1 merge last four commits in feature-branch "text-messages" into one with commit message "Added text messages"
9.  As user user1 push changes to remote repo
10.  As user user2 create feature branch with name "localization" and switch to it
11.  As user user2 create folder "Localization" and file "localizable.txt" in it
12.  As user user2 commit created file with commit message "Added localization file"
13.  As user user2 commit created folder with commit message "Added localization folder"
14.  As user user2 reorder last two commits: first should be commit with commit message "Added localization folder", second should be commit with commit message "Added localization file"
15.  As user user2 commit and push changes, then finish feature "localization" (feature branch should NOT be deleted)
16.  As user user2 append this text to file "changes_history.txt" "Added localization". Commit and push changes with message "Updated history file"

  

### Git-flow branch recovering:

1.  As user user1 create feature with name "script" and switch to it
2.  As user user1 create in project's root create folder "Script"
3.  As user user1 in folder "Script" create file with name "script.php"
4.  As user user1 commit changes with message "Added script folder and file"
5.  As user user1 remove last commit
6.  As user user1 recover that commit and move it to branch with name "recovery-branch"
7.  As user user1 merge that branch to feature branch "script"
8.  As user user1 finish feature "script" (feature branch should NOT be deleted)
9.  As user user1 append this text to file "changes_history.txt" "Added script". Commit and push changes with message "Updated history file"

  

### Git-flow release process:

1.  Simulate release: let's assume that release of version "1.0" will contain features "script" and "text-messages". As user user1 create "release" branch
2.  As user user1 merge corresponding feature branches into "release" branch
3.  As user user1 merge "release" branch into "master" branch. Add tag "1.0". As user user1 push all changes
4.  As user user1 merge "release" branch into "develop" branch.
5.  As user user1 remove branch "release"
6.  Simulate fixing issues on production: as user user1 create branch "hotfix" from master branch
7.  As user user1 append this text to file "changes_history.txt" "Applying hotfixes on prod". Commit and push changes with message "Hotfix". Add tag "1.0.1" to commit
8.  Merge branch "hotfix" to "master" and "develop" branches

  

### Git-flow cleanup:

1.  As user user1 remove all feature branches on remote and also locally
2.  Reset "changes_history.txt" to commit with message "Added history file"
3.  Create branch without history named "master"
4.  Rebase all commits from "develop" to that branch

  

### Git submodules:

1.  As user user1 create new repo named "ExternalLib" locally
2.  Create branch named "develop"
3.  Add "library.txt" file in project's root
4.  Create new remote repo on your favorite code hosting provider
5.  Create branch "develop" in remote repo. Set local branch "develop" of "ExternalLib" track changes of remote branch "develop"
6.  Push changes to remote repo
7.  In "GitSkillUp" repo add "ExternalLib" as git submodule
8.  In "ExternalLib" in project's root add file "new_version.txt". Commit with message "New lib version" and push changes to remote repo
9.  In "GitSkillUp" repo update "ExternalLib" submodule