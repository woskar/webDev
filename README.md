# webDev

This is a repo for snippets related to web development. 
If you want to learn with a course, you should check out the free onlinecourse [CS50's Web Programming with Python and JavaScript](https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/) from Harvard University. The following are notes to this lecture. 

### Versioncontrol with git
- ```git clone <url>``` creates copy of remote repo on local machine
- ```git add <filename>``` track file to be uploaded with next commit
- ```git commit -m "message"``` take a snapshot of added files
- ```git push``` send changes to repository
- ```git status``` tells you what's going on with the repository
- ```git pull``` get changes on remote server to your local files
- ```git log``` shows history of changes and commits
- ```git reset``` reverts git add
- ```git reset --hard <commit>```resets to the <commit>-version
- ```git reset --hard origin/master``` reset local changes to the remote

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

### HTML Webpages
```
<!DOCTYPE html>                   <!-- tells browser this is written in HTML Version 5 -->
<html>                            <!-- start of html content -->
  <head>                          <!-- metadata about the page, does not show up -->
    <title>My Webpage!</title>
  </head>
  <body>                          <!-- content of the page  -->
    Hello, world!
  </body>
</html>
```

Headings: Large text, comes in size 1 (biggest) to 6 (smalles)
```<h1>This is the largest headline</h1>```

Lists: Hold elements
- <ul>: unordered list: bullet points
- <ol>: ordered list: numbered elements
```
<ul>
  <li>One.</li>
  <li>Two.</li>
</ul>
```

Pictures: 
```<img src="cat.jpg" width=300>```
- Image tag has no closing tag
- src is an "html-attribute" providing additional information
- width=300 makes picture 300 pixels wide, height automatically chosen
- width=50% makes picture 50% of screensize

Tables: 
```
<table>
      <tr>
        <th>First Column</th>
        <th>Second Column</th>
      </tr>
      <tr>
        <td>A</td>
        <td>B</td>
      </tr>
    </table>
```

Forms: 
```
<form>
  <input type="text" placeholder="Full Name" name="name">
  <button>Submit!</button>
</form>
```
- type: can be "text", "email", "date", "number" etc.
- placeholder: gray text to indicate what should go there
- name: reference the input field for later processing

Divisions: containers for something
```
<div>
  Something in here.
</div>
```  

Document Object Model: structure of html page when thought of as a tree

### CSS: style html pages

(1) Style attributes in elements ```style="color:blue; text-align:center;"```
- contain CSS-properties
- style attribute can be used in elements, e.g.: ```<h1 style="color:blue; text-align:center;">Hello, world!</h1>```
- color-property: blue or HEX value like #09c125
- text-align-property: center

(2) Introduce style-rules in the header to separate content from style
```
<style>
  h1 {
    color: blue; 
    text-align: center;
  }
</style>
```
- rules for whole site
- more readable 
- reuse of code

(3) Use seperate file called stylesheet and add only reference in the header, allows to use style across multiple html documents
```<link rel="stylesheet" href="styles.css">```

Colors: 
- RGB: Red Green Blue ```rgb(9, 193, 37)```
- HEX: hex-values for rgb: ```#09c125```

Fonts: 
```font-family: Arial, sans-serif```
- First Arial gets chosen
- If not available: some sans-serif Font will be selected

Referencing with /# and .:
- Pound sign /# in CSS is short for "id"; ```#top{...}``` refers to ```<div id="top">```
- Dot sign . means class; ```.name{...}``` refers to ```<span class="name">somename</span>```
- note the difference: id's are unique, only one element per id, classes can be used in multiple elements.
