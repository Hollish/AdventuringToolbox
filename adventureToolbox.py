import cmd
import diceRoller
import initiativeTracker as tracker

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
        """Rolls Dice and does simple math. | roll (2d20 + 5d6) * 2"""
        if arg.find("#") >= 0:
            arg = arg[:arg.find("#")]
        diceRoller.regexRollStr(arg)
    
    def do_initAdd(self, arg):
        """Adds an entry to the tracker. | initAdd <Name> <Roll> <T>"""
        tracker.addInit(arg)
        tracker.writeToConsole()
    
    def do_initSort(self, arg):
        """Sorts the list for play."""
        tracker.fixOrder()
        tracker.writeToConsole()
    
    def do_initNext(self, arg):
        """Moves 1 to the bottom."""
        tracker.nextInit()
        tracker.writeToConsole()

    def do_initClear(self, arg):
        """Clears all temporary flagged entries."""
        tracker.clearInit()
        tracker.writeToConsole()

    def do_initRemove(self, arg):
        """Removes an entry based on current order."""
        tracker.removeInit(int(arg))
        tracker.writeToConsole()
    
    def do_initChange(self, arg):
        """Changes an entry's initiative value based on current order."""
        tracker.changeInit(arg)
        tracker.writeToConsole()
    
    def do_init(self, arg):
        """Print order."""
        tracker.writeToConsole()


adventureShell().cmdloop()