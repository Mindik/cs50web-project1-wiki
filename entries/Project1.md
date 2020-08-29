# Project 1
Web Programming with Python and JavaScript (old CS50 Web)
---

Project completed in [CS50W](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript) course.
Used Goodreads [API](https://www.goodreads.com/api) and [Heroku](https://www.heroku.com/postgres) PostgreSQL database.


The project was implemented in [PyCharm](https://www.jetbrains.com/pycharm/) 2020.1.2 (Professional Edition).
Applied technology [Flask](https://flask.palletsprojects.com/en/1.1.x/), 
[Jinja2](https://jinja.palletsprojects.com/en/2.11.x/), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), 
[HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5), [CSS3](https://www.w3schools.com/css/) ([SASS](https://sass-lang.com/)).

The task can be viewed at the link - [Project 1: Books](https://docs.cs50.net/web/2020/x/projects/1/project1.html).


The task sounds like this:
>In this project, you will build a book review website. Users will be able to register for your website and 
><br>then log in using their username and password. Once they log in, they will be able to search for books, 
><br>leave reviews for individual books, and see the reviews made by other people. You will also use the a third-party 
><br>API by Goodreads, another book review website, to pull in ratings from a broader audience. Finally, 
><br>users will be able to query for book details and book reviews programmatically via your website is API.

Data for connecting to the database is specified in the application.py file. The 10,000 rows Heroku provided for free 
<br>was not enough for me, so I temporarily bought the next database plan (10,000,000 rows), which costs $ 9 per month. 
<br>After checking my project, I will not pay for the database, so it may not work. In addition, Heroku periodically 
<br>changes connection data when using its first tariffs, so the database may stop working before I cancel my
 subscription.


## Project structure
#### Core files
1. [requirements.txt](https://github.com/Mindik/project1/blob/master/requirements.txt)

    The file contains a list of libraries used to run the application.
        
        pip3 install -r requirements.txt 
    
2. [application.py](https://github.com/Mindik/project1/blob/master/application.py)

    The main file that initializes the application. This file links the application, consisting of different files, into
    a single whole. Here are the keys to the Heroku database Goodreads URI APIs.
    To launch the application, use the commands:
    
        set FLASK_APP=application.py

        flask run

3. [config.py](https://github.com/Mindik/project1/blob/master/config.py)

    Project configuration file. Contains the basic settings for the application. Flask_mail settings and so on.

4. [views.py](https://github.com/Mindik/project1/blob/master/views.py)

    File of the main application paths. The basic logic for the application is described here. 
    <br>Which implements certain functions when navigating to a specific URL.

5. [forms.py](https://github.com/Mindik/project1/blob/master/forms.py)

    Contains helper objects. Here I tried to use the basics of OOP. Uses FlaskForm. Most database queries are described here.

6. [helpers.py](https://github.com/Mindik/project1/blob/master/helpers.py)

    This is a file from CS50 Finance.
    Authorization Check Function. I added the function of checking the extension of the downloaded files to this file and sending a message to the email address.

7. [static](https://github.com/Mindik/project1/tree/master/static)

    The directory where the application files are located (image, CSS, JS)

    * [script.js](https://github.com/Mindik/project1/blob/master/static/script.js)
 
         The main script written in JavaScript. I tried to leave detailed comments, but my knowledge of English is low :(.
         
         *My experience in JS is minimal. I was looking for information on Google to implement certain functions.*
    
    * [style.scss](https://github.com/Mindik/project1/blob/master/static/style.scss)
 
         SASS file containing CSS markup for all pages of the application.
    
    * [img](https://github.com/Mindik/project1/tree/master/static/img)
    
        A directory with 5,000 book covers downloaded! :) (minimum file size)
        
    * [ava](https://github.com/Mindik/project1/tree/master/static/ava)
    
        Directory of user images.
    
8. [templates](https://github.com/Mindik/project1/tree/master/templates)

    The directory where the HTML markup templates are located. The main [layout.html](templates/layout.html) template. 
    <br>The rest are related to him, thanks to [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)

9. Database [schema](https://adminer.cs50.net/?pgsql=ec2-3-222-30-53.compute-1.amazonaws.com&username=jkjcpacwmyvinj&db=d99t3klcu7ronr&ns=public&schema=books%3A26.792x19.5874_users%3A27.3923x28.8933_reviews%3A41.4262x28.7432_rating%3A34.747x1.8011_img_text%3A33.3961x11.4823)
    
    ![schema DB](https://i.ibb.co/PWN8wp3/Screenshot-2.png)

#### Additional files

1. [secretKey.py](secretKey.py)

    Secret key generation ([more](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY))

2. [start.txt](start.txt)

    An additional file for debugging, so as not to write commands every time.

3. [import.py](import.py)

    Program for reading books.csv and subsequent import into Heroku Database
    
    To start use the command:
    
    *Set the environment variable DATABASE_URL to be the URI of your database, which you should be able to see from
     the credentials page on Heroku.*
    
        python import.py
    
4. [parc_img_text.py](parc_img_text.py)

    Additional file for downloading book covers and text book descriptions.

    Images will be saved in the specified directory. Text and file name will be added to the database.
    
    *Set the environment variable DATABASE_URL to be the URI of your database, which you should be able to see from
     the credentials page on Heroku.*
     
        python parc_img_text.py


## App appearance


### Sign up
![Sign up](https://i.ibb.co/mqkGgrv/register.png)

To use the functions of the site you need to register, indicating the name, surname, email address and password. 
<br>Using [Bootstrap 4](https://getbootstrap.com/docs/4.5/components/forms/#validation) validation.

![Validation](https://i.ibb.co/f4k29yX/register-valid.png)

Additionally, the function of checking the coincidence of passwords and viewing the entered passwords is implemented.

![Password check and view](https://i.ibb.co/mXBbJw4/register-pass.png)

After entering the data and submitting the form, the server will process the request, 
<br>enter the new data into the database and send an email with a link to confirm the mailbox.

![Send email](https://i.ibb.co/N2XC35v/register-send-email.png)

![Activate](https://i.ibb.co/6bzWmSP/05register-email.png)

If the specified mailbox address is already in use, you will see a message about this.

![Error](https://i.ibb.co/Q9Cqy2h/04-1-reg-error-email.png)


*ATTENTION! The mailbox name is not case sensitive (MyEMail@exaMPLe.com == myemail@example.com), unlike the rest of
 the fields.*

If the user tries to enter the site without confirming the mailbox, the application will not allow this, and the sign in form will offer to re-send the letter.

![Resend](https://i.ibb.co/4fx3FFg/08resend-email.png)

On the page for re-sending the letter, you need to specify your mailing address. If you specify a mailbox that 
<br>is not in the database or it has already been verified, you will receive an error message.

![Resend form](https://i.ibb.co/hKHY3Pn/10resend-error.png)

Otherwise, you will receive a letter to the specified mailbox, in which there will be a link with a GET request.

![Resend mail](https://i.ibb.co/r4RTjhC/12resend-get.png)

![GET](https://i.ibb.co/MSnb9Ft/06reg-validation-get.png)

After clicking on the link from the letter, you will automatically activate your account.

![Reg fine](https://i.ibb.co/0BWCm6q/07reg-fine.png)

### Sign in

After activation, you can log in with your account.

![Sign in](https://i.ibb.co/pLF0r3z/14fg.png)

Forgot your password? Do not despair! It can be reset! How? Again through your mailing address.

![Forgot password](https://i.ibb.co/BKJQMFJ/15fg-reset.png)

You need to go to the forgot password link and specify the address of your mailbox. If such an address exists, then 
<br>a letter will be sent to you, and on the screen you will see a message

![Ok reset](https://i.ibb.co/WfLWW3Q/16fg-ok-send-email.png)

In case of an error, the message will be different!

![Error reset password](https://i.ibb.co/LtDb0VQ/Screenshot-1.png)

After clicking on the link from the letter, you will see a form that will allow you to change your password.
When you submit a login form, if you provide an incorrect username or password, you will receive a message about this. 
<br>Otherwise, you will be taken to the main page of the site.

![Sign in form](https://i.ibb.co/tJ213H1/22sign-in-error.png)


### Index page

![Index page](https://i.ibb.co/x67jTd0/main-page.png)

1. Personal profile

    Pressing 
    
    ![Botton profile](https://i.ibb.co/dKhrK9w/main-profile-btn.png). 
    
    A form of personal information will open
     before you, which no one sees, except you.
    The page has your photo, the number of your ratings and reviews.
    You also have the right to upload a new photo, no larger than 5 MB.
    
    ![View profile](https://i.ibb.co/n1kbMG2/main-prof-page.png)
    
    *I was not able to test error 413 on either the local or AWS EB server. The @ app.errorhandler (413) handler refuses
     to process it [more details](https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#improving-uploads).*
     
    In the forms below you can change your password or email. 
    In case of input errors, you will also receive error messages.
    
    ![Others form error](https://i.ibb.co/2P7b10r/main-prof-error-change-pass.png)
    
    ![Others form error](https://i.ibb.co/qBp0hKn/main-prof-change-email-error-email.png)
    
    ![Others form error](https://i.ibb.co/K5rLbfz/main-prof-change-email-error-pass.png)
    
    If you succeeded in successfully changing the password or email, then you will receive a success message.
    
    ![Others form ok](https://i.ibb.co/ChP01LH/main-prof-change-pass-ok.png)
    
    ![Others form ok](https://i.ibb.co/QcvtCZ8/main-prof-change-pass-ok-send-email.png)
    
    The password can be changed by confirming your account by entering the old password.
    Changing the mailbox address will require confirmation through the new address.
    
    ![Change email](https://i.ibb.co/9bM2Cp0/main-change-pass-email-mail.png)

2. Information Button

    By clicking on the icon 
    
    ![Info](https://i.ibb.co/CVmWVX7/main-info.png)
    
    You will see a window with general statistics showing the number of books, reviews and registered users.
    
    ![Info](https://i.ibb.co/kSM5hvr/main-info-page.png)

3. The main function is the search!
    By clicking on the icon 
    
    ![Search botton form](https://i.ibb.co/0ccD152/main-search.png)
    
    You will see a search box
    
    ![Window search](https://i.ibb.co/vq9bnGd/main-search-form.png)
    
    You can enter isbn. Title, author book. Both fully and partially. Register does not matter at all.
    
    ![Isbn full](https://i.ibb.co/Z2CFy00/main-search-isbn-full.png)
    
    ![Isbn min](https://i.ibb.co/5LTKNRp/main-search-isbn-min.png)
    
    ![Author](https://i.ibb.co/cbyXVK6/main-search-author-more.png)
    
    ![Title min](https://i.ibb.co/K690Hkt/main-search-title-min.png)
    
    ![Title full](https://i.ibb.co/RpNZDM9/main-search-title-full.png)
    
    The search form responds to Enter (Numpad Enter), but you can use the search button.
    By the way, do not worry about the number of books in the search! On the screen you will see a maximum of 
    <br>20 books on one page and 20 pages. Pages can be switched by ArrayLeft / ArrayRight.
    
    ![Page number](https://i.ibb.co/qDsG6dy/main-search-page-number.png)
    
    ![Page number](https://i.ibb.co/Nybxjss/main-search-page-number2.png)
    
    The text and image for the books were taken from the goodreads website, using the small Python code I wrote ([parc_img_text.py](parc_img_text.py)).
    <br>I attached this code to the project. I hope that goodreads are not against the use of their materials for educational (and only!) Purposes.
    
    If the book already has grades, then the stars will be colored proportionally! Check it out!
    
    ![Rating books](https://i.ibb.co/k5Hfcqn/main-search-stars-rating.png)

4. Log out
    By clicking on the button on the home page
     
    ![Log out](https://i.ibb.co/cFbdhCV/log-out.png)
    
    you will end your session and sign out.