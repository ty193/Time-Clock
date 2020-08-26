
#Time Clock
####This is an application for keeping track of employees time. Employees can login and punch in and out with the push of a button. Administrators can easily search a pay period and see all employees hours. Admins can also easily add an employee acount or remove one if necessary. 
[Deployed Website](https://lyleyoungwelding.herokuapp.com)


##User flow
Employees will see a button that says login. After pushing that they can enter their username and password. Then they will see a page with a button that says "punch clock." After pushing that button, they will be taken back to the home page and should see a message letting them know they have clocked in successfully. Punching out works in the same way. 

Admins can push the "View Hours" button and will then see a screen to enter a start date and end date for a time period. After they push "Submit" they will see all the employees hours for that time period. 

##Technology stack
- Flask
- SQLAlchemy
- WTForms
- Bcrypt


##How to run
Do the following in the terminal.

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python seed.py`
5. `flask run`