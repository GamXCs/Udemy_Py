def checkPasswd(password1, password2):
    if password1 == password2:
        return "Password changed"
    elif password1.casefold() == password2.casefold():
        return "Please check cases and try again"
    else:
        return "Passwords do not match"


print(checkPasswd("myPass", "mypass"))
