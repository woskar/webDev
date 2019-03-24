# webDev

This is a repo for snippets related to web development. 
If you want to learn with a course, you should check out the free onlinecourse [CS50's Web Programming with Python and JavaScript](https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/) from Harvard University. The following are notes to this lecture. 

### Versioncontrol with git
- ```git clone <url>``` creates copy of remote repo on local machine
- ```git add <filename>``` track file to be uploaded with next commit
- ```git commit -m "message"``` take a snapshot of added files
- ```git commit -am "message"``` add all changed files and commit with message
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


Branching: different versions of project to implement features
- HEAD refers to where (on which branch) you currently are
- ```git branch``` shows all current branches
- ```git branch <some new branch>``` creates new branch
- ```git checkout branch_name``` switches to branch branch_name
- ```git merge feature``` take what's in branch feature into the branch I'm currently on
- ```git push --set-upstream origin feature``` being on the local feature brach, commit to a new remote branch feature

Remotes: repository that lives somwhere else, not locally
- ```git fetch``` go to remote and download what's there
- ```git merge origin/master``` combine what's remote and what's local on local machine
- ```git pull``` this is the combination of the two above, fetch and merge

Fork: entirely seperate version of repository, just copied to yourself, changes won't effect the original one
- pull request: suggest your changes to someone else's repository

### HTML Webpages
Document Object Model: structure of html page when thought of as a tree
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
- ```<ul>```: unordered list: bullet points
- ```<ol>```: ordered list: numbered elements
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
  <input type="password" placeholder="Password" name="password">
  <input name="country" list="countries" placeholder="Country">
  <datalist id="countries">
     <option value="USA">
     <option value="Germany">
     <option value="China">
  </datalist>
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

Hyperreference: 
Link to another site: ```<a href="hello.html">Click here!</a>```
Link to different part: ```<a href="#section1">Click here!</a>``` where there exists an element with id="section1"

Organization of Webpage: 
| HTML4 | HTML5 |
| :----: | :----: | 
| ```<div class="header">``` |```<header>``` |
| ```<div class="nav">``` | ```<nav>``` |
| ```<div class="section">``` | ```<section>``` | 
| ```<div class="footer">``` | ```<footer>``` |
| ```...``` | ```...``` |
| - | | ```<audio>```|
| - | | ```<video>```|
| - | | ```<datalist>```|

```<datalist>``` is for autocompletion


### CSS: Cascading Style sheets
- add style to html pages
- separate content from design
- reuse code
- three options to get style in page

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


Selecting Elements of the tree structure for styling: 
```
<ol>
  <li>one</li>
  <ul>
    <li>two</li>
  </ul>
</ol>
<ul>
  <li>three</li>
</ul>
```

| a, b | Multiple Element Selector |
| a b | Descendant Selector | 
| a > b | Immediate Child Selector | 
| a + b | Adjacent Sibling Selector |
| [a=b] | Attribute Selector | 
| a:b | Pseudoclass Selector | 
| a::b | Pseudoelement Selector | 

```ol li {...}``` selects all li elements inside an ol element (one and two) => " " = "Descendant selector"
```ol > li {...}``` only selects li elements that are immediate children of ol (only one) => ">" = "Immediate child selector"
```input[type=text]{...}``` style only input fields which take text

State-Syntax with colons:
```button:hover{background-color:orange;}``` changes color when cursor moves over button

```a::before{content: "Somme text: ";}``` adds "Some text " before all "a"-Elements (e.g. ```<a href="#">link</a>``` will appear as "Some text link")

Change how highlighting something on the page looks:
```
p::selection {
  color: red; 
  background-color: yellow;
}
```

### Responsive Design


Media Queries
define Rules for displaying content
```
@media print { 
  .screen-only{    /* refers to class screen-only*/
    display: none; /* don't display
  } 
}

@media (min-width: 500px){
  body {
    background-color: red;
  }
}

@media (max-width: 499px){
  body{
    background-color: blue;
  }
}
```


viewport
```<meta name="viewport" content="width=device-width, initial-scale=1.0">``` scales the page to the width of the actual device, sizing stays the same and gets not shrinked down

Flexbox
Content in boxes which get ordered on the screen depending on its size
```
.container {
  display: flex;    /* makes the container a flexbox */
  flex-wrap: wrap;  /* boxes in line, start new line when edge reached */
}

```
```
<div class="container">
  <div>A </div>
  <div>B </div>
</div>
```

Grids
```
.grid{
  display: grid;
  grid-template-columns: 100px auto; /* first_col: 100px width, second_col: automatic width (adjusts to screen size) */
  grid-column-gap: 20px;
  grid-row-gap: 20px;
}
``` 

```
<div class="grid">
  <div class="grid-item">1</div>
  <div class="grid-item">2</div>
</div>
```

Bootstrap: 
- predefined stylesheets
- Every page devided in 12 columns, bootstrap has a grid-layout
- ```div class="col-3"``` is a div that takes up 3 of those 12 columns
- ```col-lg-3 col-sm-6``` on a large screen 3 columns, on small one 6 columns
- website: [getbootstrap.com](getbootstrap.com)


### Sass
- Extension to CSS
- let's you programmatically define stylesheets
- sass-file-extension: .scss
Example: variables.scss
```
$color: red;  // define the variable $color to have the value red
ul {
  font-size: 14px;
  color: $color; // use the color stored in the variable $color
}
```
- browser does not understand the .scss file out of the box, we only link the .css file to the html file via ```<link rel="stylesheet" href="variables.css">```
- .scss-file has to be converted in a .css-file using the command ```sass variables.scss variables.css``` in terminal
- this simply puts in the color (red) where the variable $color was used
- the compilation can be automated so we don't have to do the compilation manually after every change: ```sass --watch variables.scss:variales.css```
- nowadays, many systems (e.g. github pages) have this included


Sass allows nesting of CSS-rules: 

Sass-file:
```
div {
  font-size: 18px;
  p {               // here we have nesting
    color: blue;    // only p's inside of div's will be blue
  }
}
```

Compiled CSS-file: 
```
div {
  font-size: 18px;}
div p { 
  color: blue; }
```

Inheritance in Sass
```
%message { // define a generic message
  font-family: sans-serif; 
  border: 1px solid black;
}

.success { 
  @extend %message; // inherit the attributes from the class message
  background-color: green;
}
```













