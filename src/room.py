# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, desc, cont):
        self.name = name
        self.desc = desc
        self.cont = cont
    def __str__(self):
        return '\n-----\n'+self.name+'\n-----\n'+self.desc+'\n------\n'
