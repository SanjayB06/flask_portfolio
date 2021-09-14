## AP CSP Period 4: Team Gaico
## [Flask Portfolio Starter](https://nighthawkcodingsociety.com/projectsearch/details/Flask%20Portfolio%20Starter)
Runtime link: https://portfolio.nighthawkcodingsociety.com/
### Idea
Starter code should be fun and practical.
### Visual thoughts
#### Organize with Bootstrap menu
#### Add some color and fun through VANTA Visuals (birds, halo, solar, net)
#### Show some practical and fun links (hrefs) like Twitter, Git, Youtube
#### Show project specific links (hrefs) per page

### Implementation progress (August 13th, 2021)
#### Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
#### The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for index, kangaroos, walruses, and hawkers.
#### The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
#### WSGI templates: index.html, kangaroos.html, ... are aligned with routes in main.py.
#### Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
#### The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
#### The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files.
#### Jinja2 variables usage is to isolate data and allow redefinitions of attributes in templates.  Observe "{% set variable = %}" syntax for definition and "{{ variable }}" for reference.
#### The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
#### A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.

### IDE management (things that happened beyond plan)
#### Recall on ".gitignore" solution to the pains of temporary files.  Start a ".gitignore" and avoid promoting temporary files to Git, for instance IDE xml files.
#### A project needs to establish a "requirements.txt" to keep track of Python packages used by the project.  This help in other IDEs and Deployment.  IntelliJ has menu Tool -> Sync Python Requirements to start file.


## AP CSP Period 4: Team Gaico
## [Scrum Board](https://github.com/SanjayB06/flask_portfolio/projects)
## [Insights with Contributors and Commits](https://github.com/SanjayB06/flask_portfolio/graphs/contributors)

## Table of Contents
## 1. [Contributors](https://github.com/SanjayB06/flask_portfolio/graphs/contributors)
## 2. [Pair Share Journal 1 Gavin & Matthew](https://docs.google.com/document/d/15cVsCQSUeyoJkEMfILLqKer-sS05JoyyKEIUflzvqqg/edit?usp=sharing)
## 2.5 [Pair Share Journal 2 Samuel & Sanjay](https://docs.google.com/document/d/1i3fQiK66CaWRttSvIi_TQ9aSXb4Agyx7Tqr5Q7ZF0ek/edit?usp=sharing)
## 3. Project Ideation - We are going to make a trivia game
## 4. Sprint 0: Introduction - we installed intellij, we made a fork of the repository, setup intellij

## Contributors
| Names | Profile | Tasks | Scrumboard | Commits|
| - | - | - | - | - |
|Sanjay| [SanjayB06](https://github.com/SanjayB06) | [Tasks](https://github.com/SanjayB06/flask_portfolio/issues/assigned/SanjayB06) | [Scrumboard](https://github.com/SanjayB06/flask_portfolio/projects/1?card_filter_query=assignee%3Asanjayb06) | [Commits](https://github.com/SanjayB06/flask_portfolio/commits?author=SanjayB06)  
|Matthew| [Pqhantom](https://github.com/Pqhantom) | [Tasks](https://github.com/SanjayB06/flask_portfolio/issues/assigned/Pqhantom) | [Scrumboard](https://github.com/SanjayB06/flask_portfolio/projects/1?card_filter_query=assignee%3Apqhantom) | [Commits](https://github.com/SanjayB06/flask_portfolio/commits?author=Pqhantom)  
|Gavin| [GavinYWu](https://github.com/GavinYWu) | [Tasks](https://github.com/SanjayB06/flask_portfolio/issues/assigned/GavinYWu) | [Scrumboard](https://github.com/SanjayB06/flask_portfolio/projects/1?card_filter_query=assignee%3Agavinywu) | [Commits](https://github.com/SanjayB06/flask_portfolio/commits?author=GavinYWu)  
|Samuel| [Samuelwaang](https://github.com/Samuelwaang) | [Tasks](https://github.com/SanjayB06/flask_portfolio/issues/assigned/Samuelwaang) | [Scrumboard](https://github.com/SanjayB06/flask_portfolio/projects/1?card_filter_query=assignee%3Asamuelwaang) | [Commits](https://github.com/SanjayB06/flask_portfolio/commits?author=Samuelwaang)

## Pair Share Journals
| Names | Journal |
| - | - |
|Sanjay|[Samuel & Sanjay](https://docs.google.com/document/d/1i3fQiK66CaWRttSvIi_TQ9aSXb4Agyx7Tqr5Q7ZF0ek/edit?usp=sharing)
|Gavin|[Gavin & Matthew](https://docs.google.com/document/d/15cVsCQSUeyoJkEMfILLqKer-sS05JoyyKEIUflzvqqg/edit?usp=sharing)
|Matthew|[Gavin & Matthew](https://docs.google.com/document/d/15cVsCQSUeyoJkEMfILLqKer-sS05JoyyKEIUflzvqqg/edit?usp=sharing)
|Samuel|[Samuel & Sanjay](https://docs.google.com/document/d/1i3fQiK66CaWRttSvIi_TQ9aSXb4Agyx7Tqr5Q7ZF0ek/edit?usp=sharing)

##Project Ideation:
##Idea: A fun and interactive trivia game/website that can be used as a studying tool or simply just for fun. 
| Names | Link to Commits |
| - | - |
|Sanjay|[Dummy Text](https://www.lipsum.com/)
|Gavin|[Dummy Text](https://www.lipsum.com/)
|Matthew|[Dummy Text](https://www.lipsum.com/)
|Samuel|[Dummy Text](https://www.lipsum.com/)