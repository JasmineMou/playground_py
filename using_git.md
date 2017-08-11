rws1-JMou:brainz_v3 jmou$ git add --all
rws1-JMou:brainz_v3 jmou$ git commit -m "Refactor pull_data.py as pull_data_v2.py"
rws1-JMou:brainz_v3 jmou$ git push -u origin master

to create a branch and send pull request
https://www.atlassian.com/git/tutorials/making-a-pull-request

git checkout -b new-branch
# edit code
git commit add --all 
	or
git status //check out available changes
git add changed_file1.sql
git add changed_file2.sql

git push -u origin new-branch

go to the website to choose source(new-branch) and destination(master) to create a pull request.
