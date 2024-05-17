# DELIVERABLE 2 REPORT
### AUTHORS: Maria Azcona Garcia, Neus Fernández Valls, Eric Hernández Rodríguez & Marçal Piró Patau

## Introduction
This project contains the implementation of a web-based application, called MOVIED, which is the deliverable project for the Web Project subject in computer engineering (UdL).

## Project idea and implementation
Our website, named MOVIED, is designed to allow users to make reservations to watch movies at different cinemas. The users can create a profile, enter their personal area, check the cinemas and movies available in each cinema, get tickets for the movie they are interested in, check their reservations, and cancel or modify them. Additionally, it provides detailed information about the movies and their showtimes. We can find data such as TITLE (movie title), GENRE (movie genre), PRICE (movie visualization price), and DESCRIPTION (brief description of the movie). Although our original idea was to create a website for users to rate films (as seen in deliverable 1), we have made the decision to change the idea in order to find a better way to implement the API. This way, we have been able to assign better roles to both models and users' actions (reservtions being the objects created, edited or deleted by clients).

The registration process focuses on both Log-In and Sign Up, the access to the personal area is required to do the restricted actions (book tickets, access personal area to check and modify reservations...). The Sign-Up section checks password formats for security purposes. To facilitate navigation, we have added a header that displays the available options on all pages. Users can easily move around the site using the menu in the top bar.

To display the information of the movies available, we used a free API: https://api.andrespecht.dev/movies 

As for the page's style, we aimed to contrast an image with different colours and shapes with a white frame to highlight the buttons. We have also included our logo on the website, as well as a button with the name MOVIED that redirects to the main page. Our priority has been the simplicity of the page so that all the buttons, information and different functionalities can be seen and used easily by the final user, and at the same time we used vivid colours so that the web application is attractive and appealing. 

## How to run the web appplication
### Step 1 - Migrations
Run the following commands in the project terminal to make the migrations and apply them. This is necessary to create the models used in the application.
```
python manage.py makemigrations
python manage.py migrate
```

### Step 2 - Run the project
Make sure that you have installed poetry in your computer. Run the project in your local host by entering the following command in the project terminal:
```
poetry run python manage.py runserver
```

### Step 3 - Import data
Now the web application should be running in your local host, but the data is not yet imported. To do so, go to the following path, which will execute the code necessary to import the movie infomation from the API: 
```
http://localhost:8000/movied/add-movies
```
The movie data is now imported. Access this other path to import the cinema information: 
```
http://localhost:8000/movied/add-cinemas
```

### Step 4 - Navigate through the application
The application should be running in your browser with the data imported. You can now navigate through it, create a profile, check the cinemas, movies, book tickets, access your personal area to check your reservations, modify and cancel your tickets. To acces the admin website, we have created the following superuser: username:superuser, password:superuser.

## Step 5 - Testing
The testing of the project has been implemented using the playwright tool. There are tests for every action (create, edit, delete) implemented for one and multiple objects at the same time. We also tested the signup, login and logout. 

To run the tests you need to open a new terminal while the project is running and execute this command: 

*Make sure that the tests are being run in the order that indicate the numbers of the test files. 

```
pytest
```



* Note that despite github only showing commits from one or two people, all members of the group have worked equally during the implementation of this project.
