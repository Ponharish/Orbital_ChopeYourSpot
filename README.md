# Orbital-ChopeYourSpot

What is this Project about?



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
