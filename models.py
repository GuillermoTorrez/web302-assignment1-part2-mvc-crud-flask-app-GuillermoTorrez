from utilities import filter_input, format_name

# We are going to make a crud app using a object-oriented and following the MVC pattern.

# The first thing we need to do is create a class for our Model which represent the data we are using in our app.

# We will be making a premier database so we will mage a Premier class.

class Premier:
    """
    This class defines a Premier.
    """
    def __init__(self, form):
        self.name = form.name.data
        self.photo = form.photo.data
        self.birthdate = form.birthdate.data     
        self.deceased = form.deceased.data
        
    # In order to keep our attributes encapsulated we will want to use properties with getters and setters.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = format_name(value)
        return self.__name

    @property
    def photo(self):
        return self.__photo

    @photo.setter
    def photo(self, value):
        self.__photo = filter_input(value, r"([^a-zA-Z0-9_\-.]+)")
        return self.photo

    @property
    def deceased(self):
        return self.__deceased

    @deceased.setter
    def deceased(self, value):
        self.__deceased = value
        return self.__deceased 

    @property
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value):
        self.__birthdate = value
        return self.__birthdate 
