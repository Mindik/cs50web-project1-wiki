# Project 1
CS50’s Web Programming with Python and JavaScript
---

Project completed in [CS50W](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript) course.

The project was implemented in [PyCharm](https://www.jetbrains.com/pycharm/) 2020.1.2 (Professional Edition).
Applied technology [Django](https://www.djangoproject.com/), [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5), [CSS3](https://www.w3schools.com/css/) ([SASS](https://sass-lang.com/)).

The task can be viewed at the link - [Project 1: Wiki](https://cs50.harvard.edu/web/2020/projects/1/wiki/).

>"Design a Wikipedia-like online encyclopedia."


## Project structure

1. [encyclopedia](encyclopedia)

    Encyclopedia Application Folder

    * [static](encyclopedia/static/encyclopedia)
 
         Contains images and CSS files
             
        * [styles.scss](encyclopedia/static/encyclopedia/styles.scss)
     
             SASS file containing CSS markup for all pages of the application.
        
    * [templates](encyclopedia/templates/encyclopedia)
    
    Page Templates
    
    * [urls.py](encyclopedia/urls.py)
    
    File url for Encyclopedia Application
    
    * [views.py](encyclopedia/views.py)
    
    A view function, or view for short, is a Python function that takes a Web request and returns a Web response.
    
2. [entries](entries)

    This directory contains all saved encyclopedia entries. I added some myself
    
3. [manage.py](manage.py)

    Main file Django
    
    
## App appearance

#### Entry Page

![Entry Page](https://i.ibb.co/VxZF586/page-Entry.jpg)

The page receives the contents of the file (Markdown) and presents it as HTML.

#### Index Page

![Index Page](https://i.ibb.co/P1vrbs2/index.jpg)

Home page. Each list item will lead to a entry page.

#### Search

![Search](https://i.ibb.co/0ybTNYD/result-search.jpg)

Search Results Page (not case sensitive!)

#### Edit Page

![Edit Page](https://i.ibb.co/4MqgQPB/edit.jpg)

Edit page with pre-filled form data

#### Random Page

![Menu](https://i.ibb.co/F4LW05h/menu.jpg)

when you click on "random page" will go to the random record page

#### Markdown to HTML Conversion

Conversion using [python-markdown2](https://github.com/trentm/python-markdown2)
        
        pip3 install markdown2

        md = Markdown()
        pageHtml = md.convert(pageMd)

