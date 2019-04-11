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


### CSS: Cascading Style Sheets
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
| Syntax| Selector                  |
|:-----:| :-------------------------|
| a, b  | Multiple Element Selector |
|  a b  | Descendant Selector       | 
| a > b | Immediate Child Selector  | 
| a + b | Adjacent Sibling Selector |
| [a=b] | Attribute Selector        | 
|  a:b  | Pseudoclass Selector      | 
| a::b  | Pseudoelement Selector    | 

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
- website: [getbootstrap.com](www.getbootstrap.com)


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

### Python
```print("Hello, world!")```
```name = input()``` # define variable storing input
```print(f"hello, {name}!")``` # format-string
```print("{} squared is {}".format(i, square(i)))```
```
for i in range(5):
  print(i)
```
```
dictionary = {"A": 1, "Key": value}
dictionary["B"] = 2
```

To use custom.py files as modules, declare everything as functions, especially declare the main code as main function and add a call to it (see last two lines in following example), otherwise the code would be run if only one function of .py file is imported somwhere else: 
example: functions.py
```
def square(x): // a function we want to reuse later
  return x * x

def main(): // the main job of the .py file
  for i in range(10):
    print ("{} squared is {}".format(i, square(i)))

if __name__ == "__main__": //special syntax to run with 'python functions.py'
  main()
```

Classes: 
```
class Point: 
  def __init__(self, x, y):
    self.x = x
    self.y = y

point = Point(3, 5)
print(point.x)
```

### Flask
- micro-framework to generate websites
- written in python
- start flask with command ```flask run```
- environment variable has to be set, so that flask knows which file is the starting point: ```export FLASK_APP=application.py```


main file: application.py
```
from flask import Flask # import the flask module
app = Flask(__name__)   # create new flask-webapplication represented by current file

# route determines which file you request, simple / is default page
@app.route("/") # decorator-line, if / is requested, function below is executed
def index():    # Function is executed which prints "Hello, world!"
  return "Hello, world!"
```

making the route react to any name we get a dynamic webpage
```
@app.route("/<string:name")
def hello(name):
  name = name.capitalize()
  return f"<h1>Hello, {name}!</h1>"
```

Now we tie html and the power of python together: 
```
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  headline = "Hello, world!"
  return render_template("index.html", headline=headline) // display the index.html file
```
```
<!DOCTYPE html>
<html>
  <head>
    <title>My Website</title>
  </head>
  <body>
    <h1>{{ headline }}</h1> // headline will be filled in as variable when rendering occurs
  </body>
</html>
```
the {{ }} is Element of the language ginger2
with this syntax we can create if-else-statements: 
```
<body>
  {% if new_year %}
    <h1>Yes! Happy New Year!</h1>
  {% else %}
    <h1>NO</h1>
  {% endif %}
</body>
```
we can also generate Loops: 
```
<body>
  <h1>Names</h1>
  <ul>
    {% for name in names %} //names being a python list provided via render_tamplate
      <li>{{ name }}</li>
    {% endfor %}
  </ul>
</body>
```

Create a reference: 'more' and 'index' are the names of the python functions
```<a href="{{ url_for('more') }}">See more...</a>```
```<a href="{{ url_for('index') }}">Go back...</a>```


Template inheritance: 
- factor out code that is identical in the different html-files: 

layout.html is: 
```
<!DOCTYPE html>
<html>
  <head>
    <title>My Website</title>
  </head>
  <body>
    <h1>{% block heading %}{% endblock %}</h1>
    {% block body %}{% endblock %}
  </body>
</html>
```

then index.html just extends this file: 
```
{% extends "layout.html" %}
{% block heading %}First Page{% endblock %}
{% block body %}
  <p>Some text</p>
  <a href="{{ url_for('more') }}">See more...</a>"
{% endblock %}
```

and more.html looks quite similar: 
```
{% extends "layout.html" %}
{% block heading %}Second Page{% endblock %}
{% block body %}
  <p>Some other text</p>
  <a href="{{ url_for('index') }}">Go back to first page.</a>"
{% endblock %}
```

Forms in Flask: 
```
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/hello", methods=["Post"]) // to this route, data will be submitted via post
def hello():
  name = request.form.get("name")
  return render_template("hello.html", name=name)
```

index.html: here we can fill our name in, submitting will trigger the hello fuction and pass the data over to it
```
{% extends "layout.html" %}
{% block heading %}First Page{% endblock %}
{% block body %}
  # Action says where should form be submitted to
  # method is the kind of HTTP-request we need
  <form action="{{ url_for('hello') }}" method="post">
    <input type="text" name="name" placeholder="Enter Your Name"
    <button>Submit</button>
  </form>
{% endblock %}
```

hello.html: takes the name the user just inserted and returns a dynamically generated page
```
{% extends "layout.html" %}
{% block heading %}Hello!{% endblock %}
{% block body %}
  Hello, {{ name }}!
{% endblock %}
```

Sessions: store data specific to user account and retrieve it later
Example: Note taking application.py
```
#Option 1: One global list of notes shared across users
from flask import Flask, render_template, request, session
from flas_session import Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = [] # list as global variable shared across whole server

@app.route("/", mehtods=["GET", "POST"])
def index():
  if request.method == "POST": 
    note = request.form.get("note")
    notes.append(note) #save the newly received note in list
  return render_template("index.html", notes=notes) #render page again
```

```
#Option 2: Notes tied to individual sessions: 
from flask import Flask, render_template, request, session
from flas_session import Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", mehtods=["GET", "POST"])
def index():
  if session.get("notes") is None: 
    session["notes"] = [] # define new list for notes that's only available to one user/session
  if request.method == "POST": 
    note = request.form.get("note")
    session["notes"].append(note) #save the newly received note in list
  return render_template("index.html", notes=session["notes"]) #render page again
```

```
#index.html
{% extends "layout.html" %}
{% block heading %}First Page{% endblock %}
{% block body %}
  <ul>
    {% for note in notes %} #print all the notes
      <li>{{ note }}</li>
    {% endfor %}
  </ul>

  <form action="{{ url_for('index') }}" method="post">
    <input type="text" name="note" placeholder="Enter Note Here"
    <button>Add Note</button>
  </form>
{% endblock %}
```

### SQL (PostgreSQL)
- Language to interact with databases
- Data Types: Integer, Decimal, Serial (automatic increase), Varchar (variable length character), Timestamp, Boolean, Enum (one of discrete possible values)
- Constraints: NOT NULL, UNIQUE, PRIMARY KEY, DEFAULT, CHECK
- Functions: SUM, COUNT, MIN, MAX, AVG

```
CREATE TABLE flights (
  id SERIAL PRIMARY KEY,         // primary way to reference a flight
  origin VARCHAR NOT NULL,       // origin column cannot be empty, constraint
  destination VARCHAR NOT NULL,  // text for destination
  duration INTEGER NOT NULL      // every flight has a duration
);
```

Commands in terminal: 
- ```psql``` let's you type in Postgres commands
- ```\d``` shows all data in database

```
INSERT INTO flights 
  (origin, destination, duration)
  VALUES ('New York', 'London', 415);
```
```
SELECT * FROM flights; 
SELECT origin, destination FROM flights; 
SELECT * FROM flights WHERE id = 3; 
SELECT * FROM flights WHERE duration > 500 AND destination = 'Paris'; 
SELECT * FROM flights WHERE origin LIKE '%a%'; // origin has a in it
SELECT * FROM flights WHERE origin IN ('New York', 'Moscow', 'Lima');
SELECT AVG(duration) FROM flights WHERE origin = 'New York'; 
SELECT COUNT(*) FROM flights; 
SELECT * FROM flights LIMIT 2; 
SELECT * FROM flights ORDER BY duration ASC LIMIT 3; // the three shortest flights 
SELECT origin, COUNT(*) FROM flights GROUP BY origin;
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;  
```
```
UPDATE flights
  SET duration = 430
  WHERE origin = 'New York'
  AND destination = 'London'; 
```
```
DELETE FROM flights
  WHERE destination = 'Tokyo'; 
```

Foreign Keys: 
```
CREATE TABLE passengers (
  id SERIAL PRIMARY KEY, 
  name VARCHAR NOT NULL, 
  flight_id INTEGER REFERENCES flights
);
```

```
SLEECT origin, destination, name //two columns from flights, one from passengers
  FROM flights JOIN passengers // default is inner join = only things that match
  ON passengers.flight_id = flights.id; 
```
Joins: 
- INNER JOIN (=default): both have to match
- LEFT JOIN: all elements from left table are in result
- RIGHT JOIN: all elements from right table are in result


Hacking via SQL-Injection: 
```
SELECT * FROM users
WHERE (username = username)
AND (password = password);
```

```
Hakcer uses:
username: hacker
password: 1' OR '1' = '1
```

leads to ```password = '1' OR '1' = '1'``` which returns true
this type of problem has to be avoided, check user-input first, then execute query.

Race Conditions: 
operations in messed-up order can lead to problems.
Solution: Use Transactions, which have to be executed without interruption.
SQL-commands: ```Begin``` and ```Commit```


SQLAlchemy: Pyhton-Library to run SQL-queries with python code.
```
# list.py
# Run Select query with python and display the results

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# create engine which "talks" to the database
engine = create_engine(os.getenv("DATABASE_URL")) #Environment variables
# creating different sessions for different people in the next line
db = scoped_session(sessionmaker(bind=engine))

def main(): 
  # Run query on db-instance and fetchall=get all the results
  flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
  # flights is list of all results
  for flight in flights: 
    print(f"{flight.origin} to {flight.destination} minutes.")

if __name__ == "__main__":
  main()
```

```
# import.py
# INSERT into database with python
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
  # open file that contains data to be imported
  f = open("flights.csv")
  # import csv file with module csv
  reader = csv.reader(f)
  # loop over every line the reader has
  for orig, dest, dur in reader: 
    db.execute("INSERT INTO flights (origin, destination, duration) VALUES
                (:origin, : destination, :duration)", # use colon-syntax for :placeholder
                {"origin": orig, "destination": dest, "duration": dur}) # dictionary with elements "placeholder": element; note: this notation is save (SQL-injections etc)
    print(f"Added flight from {orig} to {dest} lasting {dur} minutes.")
    db.commit() #do the transaction, save the changes

if __name__ == "__main__":
  main()
```
```
# passengers.py
# Gives text-based way to what passengers are on the flight
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
  # List all flights. 
  flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
  # print resulting rows to screen
  for flight in flights: 
    print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes.")

  # Prompt user to choose a flight
  flight_id = int(input"\nFlight ID: "))
  flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id",
                       {"id": flight_id}).fetchone()
  # if no result: just print error message
  if flight is None: 
    print("Error: No such flight.")
    return 
  # else list passengers
  passengers = db.execute("SELECT name from passengers WHERE flight_id = :flight_id",
                           {"flight_id": flight_id}).fetchall()
  print("\nPassengers:")
  for passenger in passengers: 
    print(passenger.name)
  if len(passengers) == 0: 
    print("No passengers.")
```
Using SQLAlchemie inside of an Flask-Application: 
```
# application.py
import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/") # default route
def index(): 
  # get flights with SELECT query
  flights = db.execute("SELECT * FROM flights").fetchall()
  # render site with those selected flights
  return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book(): 
  """Book a flight."""

  # Get form information (being the name) and save it in the variable called name
  name = request.form.get("name")
  try:
    flight_id = int(request.form.get("flight_id")) #refers to drop-down-menu in index.html
  # if converting to an integer fails present Error via the error-html-page
  except ValueError:
    return render_template("error.html", message="Invalid flight number.")

  # Now we have a int-number (flight_id), make sure that a flight exists with this id.
  # .rowcount is operator which returns the number of rows of the query-results
  if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
    # no flights have the id flight_id
    return render_template("error.html", message="No such flight with that id.")
  # else we have a valid flight_id
  db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)", 
              {"name": name, "flight_id": flight_id})
  db.commit()
  return render_template("success.html")

@app.route("/flights")
def flights():
  """Lists all flights."""
  flights = db.execute("SELECT * FROM flights").fetchall()
  return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
  """Lists details about a single flight."""

  # Make sure flight exists.
  flights = db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()
  if flight is None:
    return render_template("error.html", message="No such flight.")

  # else we can continue to get all passengers
  passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                          {"flight_id": flight_id}).fetchall()
  return render_template("flight.html", flight=flight, passengers=passengers)

```
```
<!-- layout.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>{% block title %}{% endblock %}</title>
      <link rel="stylesheet" href="https://maxcdn.bootstrap.com/bootstrap" </head>
  </head>
  <bod>
      <div class="container">
        {% block body %}
        {% endblock %}
  </bod>
</html>
```
```
<!--index.html-->
{% extends "layout.html" %}
{% block title %}Flights{% endblock %}
{% block body %}
  <h1>Book a Flight</h1>
  <!-- Form with post request to the function called book -->
  <form action="{{ url_for('book') }}" method="post">
    <div class="form-group">
      <select class="form-control" name=flight_id">
        <!-- loop over the flights that are given as list in application.py-->
        {% for flight in flights %}
          <!-- double curly braces {{ }} are used to plug in values -->
          <option value="{{ flight.id }}">{{ flight.origin }} to {{ flight.destination }}</option>
        {% endfor %}
      </select>
    </div>
    <div class="form-group">
      <input class="form-control" name="name" placeholder="Passenger Name">
    </div>
    <div class="form-group">
      <button class="btn btn-primary">Book Flight</button>   
    </div>
  </form>
{% endblock %}
```
```
<!-- error.html -->
{% extends "layout.html" %}
{% block title %}Error{% endblock %}
{% block body %}
  <h1>Error</h1>
  {{ message }}
{% endblock %}
```
```
<!-- success.html -->
{% extends "layout.html" %}
{% block title %}Sucess!{% endblock %}
{% block body %}
  <h1>Success!</h1>
  You have successfully booked your flight.
{% endblock %}
```
```
<!-- flights.html -->
{% extends "layout.html" %}
{% block title %}Flights{% endblock %}
{% block body %}
  <h1>All Flights</h1>
  <ul>
    {% for flight in flights %}
      <li>
        <!-- flight_id is inserted in function flights in application.py -->
        <a href="{{ url_for('flight', flight_id=flight.id) }}">
          {{ flight.origin }} to {{ flight.destination}}
        </a>
      </li>
    {% endfor %}
  </ul>
{% endblock %}
```
```
<!-- flight.html -->
{% extends "layout.html" %}
{% block title %}Flight{% endblock %}
{% block body %}
  <h1>Flight Details</h1>
  <ul>
    <li>Origin: {{ flight.origin }}</li>
    <li>Destination: {{ flight.destination }}</li>
    <li>Duration: {{ flight.duration }} minutes</li>
  </ul>

  <h2>Passengers</h2>
  <ul>
    {% for passenger in passengers %}
      <li>{{ passenger.name }}</li>
    {% else %}
      <li>No passengers.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

Lecture ORM and API's

### Object-Oriented Programming

```
#classes.py
#easy example for a class in python

class Flight: 

  counter = 1

  # init method is a special method to declare/initialize objects
  def __init__(self, origin, destination, duration):

    # Keep track of id number
    self.id = Flight.counter
    Flight.counter += 1

    # Keep track of passengers
    self.passengers = []

    # self references object, could be named something else, calling it self is convention
    self.origin = origin
    self.destination = destination
    self.duration = duration

  # method to print information
  def print_info(self): 
    print(f"Flight origin: {self.origin}")
    print(f"Flight destination: {self.destination}")
    print(f"Flight duration: {self.duration}")
    print()
    print("Passengers:")
    for passenger in self.passengers: 
      print(f"{passenger.name}")


  def delay(self, amount): 
    self.duration += amount

  def add_passenger(self, p): 
    self.passengers.append(p)
    p.flight_id = self.id

class Passenger: 

  def __init__(self, name):
    self.name = name


def main():
  # create flight
  # self argument is implicit doesn't have to be stated
  # optional to name types if parameters in right order
  f1 = Flight(origin="New York", destination="Paris", duration=540)

  # create passengers
  alice = Passenger(name="Alice")
  bob = Passenger(name="Bob")

  # add passengers
  f1.add_passenger(alice)
  f1.add_passenger(bob)

  # change values
  f1.duration += 10

  # read values
  print(f1.origin)
  f1.print_info()
  f1.delay(10)
  f1.print_info()

if __name__ == "__main__":
  main()
```

### Object-Relational Mapping (ORM)
tie the two worlds of objects in python and SQL databases together
using Flasd-SQLAlchemy

```
# models.py
# define database-model
# key idea: for every table in the database, there's one class in this models-file

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Flight(db.Model):
  # class Flight should correspond with the table-name flights
  __tablename__ = "flights"
  # define Columns inside the flights-table
  id = db.Column(db.Integer, primary_key=True)
  origin = db.Column(db.String, nullable=False)
  destination = db.Column(db.String, nullable=False)
  duration = db.Column(db.Integer, nullable=False)

class Passenger(db.Model): 
  __tablename__ = "passengers"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)

# up to there the CREATE TABLE-syntax is basically rewritten in python code.
'''
so the above corresponds to: 
CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  origin VARCHAR NOT NULL, 
  destination VARCHAR NOT NULL, 
  duration VARCHAR NOT NULL
);
'''
# the actual creation is done via the command
# db.create_all()
```
```
# create.py
# python file to create database

from flask import Flask, render_template, request
from models import * # our file defined above to define the classes/tables

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # tie this database with this flask application

def main():
  db.create_all()

if __name__ == "__main__":
  with app.app_context(): # we need this to properly interact with flask-application
    main()
```
+ Example for importing from csv-file into database: 
```
f = open("flights.csv")
reader = csv.reader(f)
for origin, destination, duration in reader: 
  flight = Flight(origin=origin, destination=destination, duration=duration)
  db.session.add(flight) # add this flight to database, equiv. to INSERT command
  print(f"Added flight from {origin} to {destination} lasting {duration})
db.session.commit() # make the change happen
```
+ Example for listing results of a query
```
flights = Flight.query.all() # returns objects
for flight in flights:  # loop over objects
  print(f"{flight.origin} to {flight.destination}) # print values
```

### Translating SQL into SQLAlchemy-Python-Syntax: 

+ Inserting into tables:
```
# SQL-Syntax
INSERT INTO flights
  (origin, destination, duration)
  VALUES
  ('New York', 'Paris', 540)
```
```
# Corresponding syntax in python with SQLAlchemy
flight = Flight(origin="New York", destination="Paris", duration="540")
db.session.add(flight)
```
+ Selecting everything from a table:
```
SELECT * FROM flights; 
```
```
Flight.query.all()
```
+ Selection with WHERE-clause:
```
SELECT * FROM flights WHERE origin = 'Paris'; 
```
```
Flight.query.filter_by(origin="Paris").all()
```
+ Only selecting one element:
```
SELECT * FROM flights WHERE origin = 'Paris' LIMIT 1;
```
```
Flight.query.filter_by(origin="Paris").first()
```
+ Selecting by ID: 
```
SELECT * FROM flights WHERE id = 28;
```
```
# two equivalent options here
Flight.query.filter_by(id=28).first()
Flight.query.get(28) # returns none if no id=28 
```
+ Count objects:
```
SELECT COUNT(*) FROM flights WHERE origin = 'Paris';
```
```
Flight.query.filter_by(origin="Paris").count()
```
+ Updating table-entries: 
```
UPDATE flights SET duration = 280 WEHRE id = 6; 
```
```
flight = Flight.query.get(6)
flight.duration = 280
```
+ Delete table-entries: 
```
DELETE FROM flights WHERE id = 28;
```
```
flight = Flight.query.get(28)
db.session.delete(flight)
```
+ Get ordered set of results: 
```
SELECT * FROM flights ORDER BY origin DESC; 
```
```
Flight.query.oder_by(Flight.origin.desc()).all()
```
+ Select all except for special constraints: 
```
SELECT * FROM flights WHERE origin != "Paris"
```
```
Flight.query.filter(Flight.origin != "Paris").all()
```
+ Select flights that contain letter 'a' within them: 
```
SELECT * FROM flights WHERE origin LIKE "%a%"
```
```
Flight.query.filter(Flight.origin.like("%a%")).all()
```
+ Selection contained in list:
```
SELECT * FROM flights WHERE origin IN ('Tokyo', 'Paris');
```
```
Flight.query.filter(Flight.origin.in_(["Tokyo", "Paris"])).all()
# in_ with underscore because in is a python keyword
```
+ Combined boolean expressions
```
SELECT * FROM flights WHERE origin = "Paris" AND duration > 500; 
```
```
Flight.query.filter(and_(Flight.origin == "Paris", Flight.duration > 500)).all()
# similarly or_
```
+ Joining multiple tables together: 
```
SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id; 
```
```
db.session.query(Flight, Passenger).filter(
  Flight.id == Passenger.flight_id).all()
```








