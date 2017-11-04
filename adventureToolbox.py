import random
import time
import cmd

random.seed(int(time.time()))
queue = True

class adventureShell(cmd.Cmd):
    intro = """
+++++++++++++++++++++++++++++++++++++++
 _____   _             _               
|  _  |_| |_ _ ___ ___| |_ _ _ ___ ___ 
|     | . | | | -_|   |  _| | |  _| -_|
|__|__|___|\_/|___|_|_|_| |___|_| |___|
                                       
 _____         _ _                     
|_   _|___ ___| | |_ ___ _ _           
  | | | . | . | | . | . |_'_|          
  |_| |___|___|_|___|___|_,_|   
  
+++++++++++++++++++++++++++++++++++++++
Type 'help' or ? for a list of commands.
"""
    prompt = '#> '
    file = None

    def do_roll(self, arg):
        print(arg)


adventureShell().cmdloop()