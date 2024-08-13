# if we import something it will be getting run in our program

import mod2

import app
# Giving __name__=="__main__" will execute only in the main file here that is app.py as if we want
# just to use some functionality of app.py not the whole program If(__name__=="__main__") helps us with 
# That.
# here We are importing mod2 so it will not give use dunder __main__ here
print(f"Running Mod1--({__name__})")