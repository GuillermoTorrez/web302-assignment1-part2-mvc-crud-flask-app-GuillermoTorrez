# To accept data through forms we need to use Flask WTF and create some classes.
# First we need to import the FlaskForm class form the flask_wtf
from flask_wtf import FlaskForm

# We also need to import the String Field, SelectField, BooleanField and HiddenField classes from the wtforms package and DataRequired class from validators property of the wtforms package.

from wtforms import StringField, SelectField, BooleanField, HiddenField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
# To use FlaskWTF to accept form data we need to create a new class.
# This class will represent whichever form we are accepting data from and will be a child class of the FlaskForm class.

# We want this form to accept data to add new premiers to the View Premiers page so we will call it PremierForm.

# It will have have a class variable attribute for each field which exists in the form.
# These variables will use WTForm's StringField, SelectField and BooleanField depending on the type data wich we want to accept.

class PremierForm(FlaskForm):
    name = StringField('Full Name:', validators=[DataRequired()])
    photo = SelectField('Photo:', validators=[DataRequired()],
        choices=[
            ('Alexander.Mackenzie.jpg', 'Alexander.Mackenzie'),
            ('Arthur.Meighen.jpg', 'Arthur.Meighen'),
            ('Brian.Mulroney.jpg', 'Brian.Mulroneyn'),
            ('Charles.Tupper.jpg', 'Charles.Tupper'),
            ('Jean.Chretien.jpg', 'Jean.Chretien'),
            ('Joe.Clark.jpg', 'Joe.Clark'),
            ('John.Abbott.jpg', 'John.Abbott'),
            ('John.Diefenbaker.png', 'John.Diefenbaker'),
            ('John.Macdonald.jpg', 'John.Macdonald'),
            ('John.Thompson.jpg', 'John.Thompson'),
            ('John.Turner.jpg', 'John.Turner'),
            ('Justin.Trudeau.jpg', 'Justin.Trudeau'),
            ('Kim.Campbell.jpg', 'Kim.Campbell'),
            ('Lester.Pearson.jpg', 'Lester.Pearson'),
            ('Louis.Laurent.jpg', 'Louis.Laurent'),
            ('Mackenzie.Bowel.jpg', 'Mackenzie.Bowel'),
            ('Paul.Martin.jpg', 'Paul.Martin'),
            ('Pierre.Trudeau.jpg', 'Pierre.Trudeau'),
            ('Stephen.Harper.jpg', 'Stephen.Harper'),
            ('Wilfrid.Laurier.jpg', 'Wilfrid.Laurier'),
            ('William.Mackenzie.jpg', 'William.Mackenzie')
        ]
    )    
    deceased = BooleanField('Is it a deceased?')
    birthdate = DateField('Birthdate:', format='%Y-%m-%d', validators=[DataRequired()])

# we will also need separate form classes for editing and deleting premiers.
# The edit form class will need to include all of the same fields as the add form will need make a lass called EditPremierForm wich will be a child class of PremierForm.
# This class needs one extra field wich will be a required HiddenField which collects the ID of the premier to specify which premier is being edited.

class EditPremierForm(PremierForm):
    id = HiddenField(validators=[DataRequired()])

# The delete form will be very similar except it should be a child class of FlaskForm instead of PremierForm.

# It still needs a field for the ID to specify which premier is being deleted

class DeletePremierForm(FlaskForm):
    id = HiddenField(validators=[DataRequired()])    