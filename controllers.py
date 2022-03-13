# We will aslo need a Controller for our Premier Model wich will control the flow of data from the Model to the view and from the View to the Model.
# Our Controller will manage our CRUD operations using six functions.

# First we need to import the Flask class from the flask package as well as the render template, the request object and the redirect functions.

from flask import Flask, render_template, request, redirect, flash

# We will need to import our Premier model from our model module, our PremierForm, EditPremierForm, and DeletePremierForm classes from our module and our site_title, mydb and mycursor objects from our setting module.
from models import Premier
from forms import PremierForm, EditPremierForm, DeletePremierForm
from settings import site_title, mydb, mycursor
from flask_wtf.csrf import CSRFProtect

# we also need to import the os module in order to set the value for SECRET_KEY as a random string
import os

# we also need to create a new instance of the Flask class using the __name__ attribute as the Arguments.

premier_app = Flask(__name__)

# The config property is a dictionary with keys which are associaed with different configuration options.
# There is one cofiguration option which we would almost want to set when using forms with FLASK called 'SECRET_KEY' which sets key thtat is used when CSRF proteccion is enabled in forms.
# To set the 'SECRET_KEY' option we will create a variable called SECRET_KEY a set it to a string of random characters which we will generate using urandom() method the os Module
# the urandom()

SECRET_KEY = os.urandom(32)
premier_app.config['SECRET_KEY'] = SECRET_KEY

# The first function we will make will be an add() function which will load and add Premier page with a form which will allow the user to add a new premier.

@premier_app.route("/add-premier")
def add():
    # In this function we will want to use the get() method of the request object to collect GET data from URL.
    # this data will be used to check if there are any errors when the form is submitted.
    get = {
        "add": request.args.get("add")        
    }

    # Then we will create a new instance of our PremierForm class and set csfr_enabled to True.
    # All Flask WTF form objects which have the cstf_enabled argument set to true must have a CSRF (Cross-site-request_Forgery) token.
    # A CSRF token is a unique randomized number/character string which is generated each time the form is submmitted and is stored both in the submitted form data and in a cookie which s stored in the user's browser.
    # The CSRF token form, the form data is then checked against the CSRF token in the users's browser to ensure that an outside party can not access the data submited form the form.
    # The value of our CSRF token will be set by SECRET_KEY variable we created earlier.

    form = PremierForm(csrf_token=True)
    
    # Finally, we will pass our get and form variable to the Jinja template.

    return render_template(
        'add-premier.html.j2',
        site_title = site_title,
        page_title = site_title + " - Create",
        get = get,
        form = form
    ) 

# our create() funtion will use the @app.route decorator to point to an address of "/create-premier" and must have another arugments of methods('GET', 'POST') to accept data from GET request and POST requests.

# The Address will not point to a corresponding Jinja template.
# Instead it will process the data from our form and will redirect to a different address.

@premier_app.route("/create-premier", methods=('GET' , 'POST'))
def create():
    # We will created a new instance of our Premier class, use the request.for, object which will get the request method (GET or POST) as the first argument and set csrf_enabled to True.
    form = PremierForm(request.form, csrf_enabled=True)
    # We will check to see if our required fields have been filled out.
    if form.validate_on_submit:
        # we will create a new instance of our Premier class and its constructor method will take the form object.
        premier = Premier(form)
        # Now that our object has been created we will use an INSERT INTO statement to add the object's properties to our database.
        query = "INSERT INTO `premier` (`name`,`photo`, `deceased`, `birthdate` ) VALUES (%s, %s, %s, %s)"
        value = (premier.name, premier.photo, premier.deceased, premier.birthdate)
        mycursor.execute(query, value)
        mydb.commit()
        flash('There premier was successfully added!')
        return redirect('/?add=success')
        # if the required fields have been filled our add the premier to the  database and redirect to the View Premier page with GET data to display a success message, else go back to the add premier page with GET data to display an error message.
    else:
        flash('An error was ocurred when adding premier!')
        return redirect('/add-premier?add=error')

# the Read() function will be used to retrieve data from the database and diplay it on a View Premier page.
# In this function e will want to use the get() method of args property o the request object to collect GET data from the URL.
# This data will be used to display success and error messages when forms are redirect to this page.

@premier_app.route("/")
def read():
    get = {
            "add": request.args.get("add"),
            "edit": request.args.get("edit"),
            "delete": request.args.get("delete")
    }

    # we will then use a SELECT * FROM stament to collect all of the rows in the database and the fechtall() method to return them in a dictionary.

    query = "SELECT * FROM `premier`"
    mycursor.execute(query)
    premiers = mycursor.fetchall()

    # The View premier page will also have a delete button which allow the user to delete a premier.
    # Therefore we will need to create a new instance of our DeletePremierForm class and set csrf_enabled=True
    form = DeletePremierForm(csrf_enabled=True)
    
    return render_template(
            "view-premier.html.j2",
            site_title = site_title,
            page_title = site_title + " - View",
            get = get,
            premiers = premiers,
            form = form
    )

# We will need and edit() function which will load and Edit Premier page with form which allow the user to edit an existing premier. In this function we will want to use the get() method of the args property of the request object to collect GET DATA from the URL.
# This data will be used to check if there are any errors when the form is submitted as well as to get the ID of the specific premier we are editing.

@premier_app.route("/edit-premier")
def edit():
    get = {
        "edit": request.args.get('edit'),
        "id": request.args.get('id')
    }

    # we will use a SELECT * FROM statment and interpolate the ID which was passed to the script which GET data to find the matching database row using the WHERE clause and the fecthone() method to return the premier we are currently editing in a dictionary.
    query= f"SELECT * FROM `premier` WHERE id='{get['id']}'"
    mycursor.execute(query)
    premier = mycursor.fetchone()

    # then we will create a new instance of our EditPremierForm class and set csrf_enabled to True.
    # This will allow us to set the values of each form field to the already existing values which are stored in the database by assigning the data attribute of each attribute of the form object to the corresponding values of the premier object.

    form = EditPremierForm(csrf_enabled=True)
    form.name.data = premier["name"]
    form.birthdate.data = premier["birthdate"]
    form.photo.data = premier["photo"]
    form.deceased.data = premier["deceased"]

    # The ID attribute will be sent using the ID which is passed to the edit Premier page using a link with GET data.
    form.id.data = get["id"]

    # Finally we  will pass out premier and form variables to the template
    #  

    return render_template(
        "edit-premier.html.j2",
        site_title = site_title,
        page_title = site_title + "- Update",
        premier = premier,
        get = get,
        form = form
    )

# Our update() function will be very similar to the create() function with samll diference.

@premier_app.route("/update-premier", methods=('GET' , 'POST'))
def update():
    # We will created a new instance of our EditPremier class, use the request.form, object which will get the request method (GET or POST) as the first argument and set csrf_enabled to True.

    form = EditPremierForm(csrf_enabled=True)
    # Unlike the create() function we will need to retrieve the ID of the premier which is being updated by accessng the data id atribute of the form object.

    id = form.id.data 
    # We will check to see if our required fields have been filled out.
    if form.validate_on_submit:
        # we will create a new instance of our Premier class and its constructor method will take the form object.
        premier = Premier(form)
        # Now that our object has been created we will use an UPDATE statement and interpolate the ID of the premier to find a matching database row using the WHERE clause to update that row with the new object's properties

        query = f"UPDATE `premier` SET name=%s, photo=%s, deceased=%s, birthdate=%s WHERE id='{id}'"
        value = (premier.name, premier.photo, premier.deceased, premier.birthdate)
        mycursor.execute(query, value)
        mydb.commit()
        flash('There premier was successfully edited!')
        return redirect('/?edit=success')
        # if the required fields have been filled our add the premier to the  database and redirect to the View Premier page with GET data to display a success message, else go back to the add premier page with GET data to display an error message.
    else:
        flash('An error was occurred when editing premier!')
        return redirect('/edit-premier?edit=error')

# The delete() function will be very similar to the update() function.
# We still need to collect the ID of the premier from the form to identify which premier we are deleting.
# However, we don't need to create a new instance of the premier as we are simply deleting.

@premier_app.route("/delete-premier", methods=('GET', 'POST'))
def delete():
    # We will create a new instance of our DeletePremierForm class, use the request.form object which will get the request method (GET or POST) as the first argument and csrf_enabled to True

    form = DeletePremierForm(csrf_enabled=True)

    # Unlike the create() function we will need to retrieve the ID of the premier which is being updated by accessing the data attribute of the id attribute of the forn object. 

    id = form.id.data
    
    # We will chech to see if our requeried fields have been filled out.
    if form.validate_on_submit():
       # we will check to ensure that ID has been submitted, use a DELETE statement and interpolate the ID of the premier to find a matching database row to delete using the WHERE clause.
       query = f"DELETE FROM `premier` WHERE id='{id}'"
       mycursor.execute(query) 
       mydb.commit()
       flash('There premier was successfully deleted!')
       return redirect('/?delete=success')
    else:
       flash('An error was ocurred when deleting premier')
       return redirect('/?delete=error')