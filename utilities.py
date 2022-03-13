import re

# To filter generic input we will crate a filter_input method using the strip() function which removes white space from the beginning and end of a string, the re.sub() method to try to remote any HTML tags from a string using a regular expressions.

def filter_input(string, special_characters):
    strip_space = string.strip()
    strip_tags = re.sub(r"(<.*?>)", "", strip_space)
    strip_chars = re.sub(special_characters, "", strip_tags)
    return strip_chars

# We would want to validate and filter each type of data using unique processes. To filter names we would want to run them through our generic filter_input function to remove unwanted characters but may want to remove addditonal characters such as numbers from names from names. Formatting of ames using lower() and title() can be done when user input is collected as well. we will create a format name() function todo do this.

def format_name(name):
    filtered = filter_input(name, r"([^a-zA-Z ]+)")
    formatted = filtered.lower().title()
    return formatted

# Escaping special characters to convert them to plain text using methods such as replace() should normally only be done after retreiving data from a database or file and displaying it as output. this is because you can not properly escape the caracters in your data unless you know the final format which your data will be used in.

#if you are sure that your data will only ever be used in HTML then you could escape your input before saying it to a database. However, if t is posible that it could be used in a different format then you would to avoid doing so until you display the data. This way you can use the escape charancter of whichever language you are using the data as output in on a case by case basis.

# we can make an escape_html() function to escape output to be displayed in our HTML

def escape_html(string):
    neutralize_amp = string.replace("&", "&amp;")
    neutralize_quote = neutralize_amp.replace('"', "&quot;")
    neutralize_lt = neutralize_quote.replace("<", "&lt;")
    neutralize_gt = neutralize_lt.replace(">", "&gt;")
    return neutralize_gt