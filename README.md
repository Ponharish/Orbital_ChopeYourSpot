# Orbital-ChopeYourSpot

# Aim

To create a cutting-edge web application empowering companies to efficiently manage shared spaces through a robust reservation system equipped with advanced features


# Motivation

ChopeYourSpot is a Web Application that allows for the reservation and booking of common office spaces in corporate companies.
Have you ever been in this situation where you wanted to use a common space but often assume that it is too crowded or felt this is not the right time and ended up never using it? We have developed this solution where corporate companies can register with us and purchase a license using which all users can create a free account, using it to book common spaces in their office. By using our applications, now our corporate users better utilize these common spaces.



# Team Information

Team Name

ChopeYourSpot


Proposed Level of Achievement

Gemini


Team Members

Subramanian Pon Harish (Year 1, CS)

Mathivoli Sriganesh (Year 1, CS)


# User Stories


Employer/Employee
 As an Employer/Employee, they can to login to this app to book a slot (timing & location) for meetings within the office space. They can also communicate with other users using the chat functionality

Company Administrator
As a Company Administrator, they can manage the different locations available for booking and assist users in making a booking. They can also communicate with other users using the chat functionality.

A company administrator is a representative from each company to manage the company. A license for each company is purchased with the creation of a company administrator account. This domain name is used to uniquely identify the company and enables users to create accounts.

System Administrator
As a System Administrator, they can manage all the payments made, manage all the registered companies (approve a new company, remove a company), and communicate with other users using the chat functionality


# Features 

User Authentication

A sophisticated login system that requires a username and a domain name to identify an user. The user is authenticated using passwords and 2-factor authentication using a One Time Password sent through email. Moreover, additional security features such as captchas are used. Based on the user type, a different User interface is rendered with the user specified.

Booking common spaces

Bookings can be made to reserve common spaces within the company premises. These bookings can be made by users (employers/employees) or by company administrators for the users. This is the key functionality for this project which features a customised form for the different user groups and extensive validation of data to ensure that bookings do not conflict with existing bookings and they are made within the operating hours as specified by the company administrators and other validations.

Searching for available facilities
This search function is implemented in the user (Employer/Employee) interface and company administrator interface. This feature enables to search for a specific place with their company premise and displays the information such as location ID, name of location, venue and availability in a tabular format. 




Customized interface for different user groups
Based on the 3 different user groups - Employer/ Employee (a standard user), Company Administrator,and System Administrator, a different user interface and functionalities are rendered. These functionalities reflect the different authorization rights they have when using the system.


Messaging
This is a chat functionality that is meant to internally communicate among different users. This platform could be used to communicate among users from different roles to resolve their issues, contact their admin, and for other purposes as well.


Payment for company registration
This feature is integrated with the creation of a system administrator account. Currently, it is a static feature that takes in the payment reference and is later manually verified by the system administrators. This functionality is planned to be further enhanced in future updates by automating the process with a third-party service provider 


Feedback and Enquiries system

Feedback and Enquiries are two pages provided to all users which can be used to communicate their feedback and enquiries to the admins and developers.



# Tech Stack

Python
Python 3.11 is the backend programming language used to implement this project. All the logic and processes were written using python

Django
Django 4.2.13 is the web framework that works with Python to implement MTV architecture which is essentially the backbone of the entire system

SQLite
SQLite is the database used to store all the data related to users, bookings, companies, payment history, and others are stored
HTML
HTML 5 is used to write all the template codes and to design the user interface. 

CSS
CSS is used to add custom style to all the HTML elements which helps to achieve uniformity and an elegant way to display data

JavaScript
JavaScript is used to execute several small instructions on the client side such as searching in a table, rendering ADs

GitHub
GitHub is the primary version control system used to keep track of all the commit history and to deploy the application from

Azure
Microsoft Azure services are used to deploy the web application. Azure student plan is used to host the web app and to store blob data.


# Software Engineering Practices

Modularity and Encapsulation
Modularity is achieved in this project by segmenting the code into different apps - homepage, login, company_admin, system_admin, employer/employee. Under each of these apps, the templates, URLs, static files, and functional code are provided. Each app encapsulates related components, fostering a clear separation of concerns that simplifies debugging, scalability, and collaborative development efforts. This architectural approach ensures that updates and modifications to specific features can be efficiently managed without impacting other parts of the application.

Model-Template-View (MTV) Architecture
This project adheres to the Model-Template-View (MTV) architectural pattern, which enhances organization and maintainability. In this pattern, model represents data stored in the database in the different tables. Template are used to display the data in front end using HTML, CSS and JavaScript. Views are the different functions written in python that manages all the back end functionality by validating the data, processing the data and updating the database.


Separation of Concerns
This project adheres to the principle of Separation of Concerns, which advocates for dividing software into distinct sections, each addressing a separate concern. In our project, this principle is evident through the modular organization of code into separate apps like homepage, login, company_admin, system_admin, and employer/employee. Each app encapsulates related functionality including templates, URLs, static files, and business logic. This modular approach enhances maintainability by allowing developers(us) to focus on specific features without impacting others, facilitates code reuse across different parts of the application, and promotes clarity and scalability in development and maintenance efforts. By adhering to Separation of Concerns, we ensure that our codebase remains organized, flexible, and easier to extend as our project evolves.

Version Control
Version control is integral to our development process, managed primarily through Git, a distributed version control system. Git allows us to track changes to our codebase over time, facilitating collaboration with our team and enabling us to revert to previous versions if necessary. We use Git repositories hosted on GitHub to store our project's code. This ensures that changes are systematically documented, reviewed, and integrated into our project, maintaining a stable and cohesive codebase throughout development iterations. By leveraging version control, we streamline our workflow, enhance accountability, and support continuous improvement and innovation in our project.


# Timeline

Milestone 1

Login Functionality
User registration - Standard users (Employer and Employees) and Company Admins
OTP verification using email
Captcha codes
Milestone 2

User interface for Standard user
User interface for Company Admin
Booking of common spaces (By users and company admin)
Starting and ending session
Adding/ removing common spaces (By Company Admin)
Search functionality to search for common spaces
Basic Admin control (Approving and rejecting companies)

Milestone 3

Admin controls
Chat Functionality
Add an advertisement to homepage
Host web app

# Bugs encountered

Milestone 1

The otp generated and the one tested against did not match
The application was not compatible with chrome but was with safari due to the multiple HEAD HTTP request sent in by chrome which triggered the OTP to be sent indefinetly (until mail server registered an error)
The captcha generated did not match with the one displayed

Milestone 2
Some browsers like chrome store secondary cookies which bypasses the delete command and still manages to retieve user credential after logout
There were some compatibility issue converting time to json
search function implemented made the timings disappear when searched for a facility
There were some issues faced when storing and retrieving date and time as they had to be processed as a datetime object but they had to be stored as a string in DB
All the process happened as expected but after a few error messages were generated upon reaching the acknowledgement page. This was caused due to multiple HEAD request generated by chrome. This was fixed by using a conditional statement

Milestone 3
Ads would not display until a certain traffic is hit
The format for text in About Us was not consistent across different browsers. This was resolved using CSS styling to fit everything into a container
Several bugs were encountered when hosting the web app. The main error was “unable to create/update server farm” - an error on Microsoft end that affected those using the student plan. 


# Sources of revenue

Purchase of liscence
When company admins register their company and create an account, they would make a payment of SGD 50 in order to acquire a license (i.e. an unique domain for their company)

Advertisements
Advertisements will be displayed in the home page to fill in the space and to have another source of revenue as each user views it 


# Link to Page

https://chopeyourspot-cpf0apcqe8f3fqfu.southindia-01.azurewebsites.net/


# Video Demo

Part 1 - Creating an account and logging in to the system

https://drive.google.com/file/d/16ti2Akhvo2gz1IjAy496zaacELdrnoQj/view?usp=drive_link 

Part 2 - Adding common spaces, Making reservations

https://drive.google.com/file/d/1ejvYKYJJywzaVNrQ0o0JOwEmqWskHrPz/view?usp=sharing 


# Link to README (with graphics)
https://docs.google.com/document/d/1gX8nyiyHayE8qKkUcm_gqjzRkcQH0A1fzM0LMwaQ1iw/edit#heading=h.76gx2jj4hzmx
