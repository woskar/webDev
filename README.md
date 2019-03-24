# webDev

This is a repo for snippets related to web development. 
If you want to learn with a course, you should check out the free onlinecourse [CS50's Web Programming with Python and JavaScript](https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/) from Harvard University. The following are notes to this lecture. 

Versioncontrol with git
- ```git clone <url>``` creates copy of remote repo on local machine
- ```git add <filename>``` track file to be uploaded with next commit
- ```git commit -m "message"``` take a snapshot of added files
- ```git push``` send changes to repository
- ```git status``` tells you what's going on with the repository
- ```git pull``` get changes on remote server to your local files
- ```git log``` shows history of changes and commits
- ```git reset --hard <commit>```resets to the <commit>-version
  ```git reset --hard origin/master``` reset local changes to the remote

Merge conflict: changes locally and remotely on same line
```
a = 1
<<<<< HEAD
b = 2 // your changes on your machine before you did the pull
=====
b = 0 // remote changes
>>>>> 1292165c3324799df2387194 // name (hash) of the conflicting commit
c = 3
```
you need to remove all the lines from < to > and leave only what you want in between.
```
a = 1
b = 2
c = 3
```
Then add, commit and push again.

HTML Webpages
```
<!DOCTYPE html>
<html>
  <head>
    <title>My Webpage!</title>
  </head>
  <body>
    Hello, world!
  </body>
</html>
```