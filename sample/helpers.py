
def choice():
    """
    Purpose: Capture user input
    """

    return int(input(">>> "))

def menu_question(*args):
    """
    Purpose: Provide structure to menu questions
    """

    return input("What {} {} {}? ".format(args[0], args[1], args[2])).upper()

