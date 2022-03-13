from controllers import premier_app

# Finally, use an if statment to make sure that this module has not been imported into another module by checking if the __name__ variable is equal to "__main__" and if so, run the app using the .run() method of the app object.
# if we want to the .run() method to display error debuggin messages we can set the debug parameter to true.

if __name__ == "__main__":
    premier_app.run(debug = True)

