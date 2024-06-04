# Orbital-ChopeYourSpot

What is this Project about?
ChopeYourSpot is a Web Application that allows for the reservation and booking of common office spaces in corporate companies.
Have you ever been in this situation where you wanted to use a common space but often assume that it is too crowded or felt this is not the right time and ended up never using it? We have developed this solution where corporate companies can register with us and purchase a license using which all users can create a free account, using it to book common spaces in their office. By using our applications, now our corporate users better utilize these common spaces.


User Stories

 -> As an employer/employee, I am able to login to this app to book a slot (timing & location) for meetings within the office space
 -> As a company administrator, I am able to manage the availability of slots (increase it on demand) and manage user accounts (creation and deletion)
 -> As a system administrator, I am able to handle company registration of the service docs


Features

- User Authentication (with 2FA and captcha)
- Booking common spaces
- Searching for available facilities
- customized interface for different user groups
- Messaging among users
- Payment for company registration
- Feedback system


Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript
- GitHub


How to try this project?

->To begin with, create a normal directory in any desired location. Using terminal/command promp/.. navigate to the folder which you have created
->Create a virtual environment
    windows user   -> py -m venv venv
    mac/linux user -> python -m venv venv
-> activate the virtual env
    windows user   -> cd virtualenv\Scripts
                    - activate
    mac/linux user -> source venv/bin/activate

  (Note: to deactivate virtual env, type - "deactivate")

  -> copy the entire repo to your folder
  so now your directory looks like 

  (In github pls view this under code and NOT preview)
    project/
    ├── venv/
    │   ├── Include/
    │   ├── Lib/
    │   ├── Scripts/
    │   ├── pyvenv.cfg
    ├── ChopeYourSpot
        ├── ChopeYourSpot
        ├── Company_Admin
        ├── manage.py
        (and other files)


-> cd to ChopeYourSpot directory (the outer one)
-> run command - pip install django
-> run command python manage.py runserver (for linux/mac users)
               py manage.py runserver (for windows users)

-> a link will be displayed in terminal/cmd eg: (http://127.0.0.1:8000/)
    open it in browser and use it



Other Notes

Since the system administrator page is not created yet, to manually approve companies perform the following strops

- python manage.py shell
  
 (in shell type the following)
  from login.models import registeredDomains

  registeredDomains.objects.all().values() – to find the index value

  x = registeredDomains.objects.all()[<replace with entry number>]

  x.approved = True

  x.save()

