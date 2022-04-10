import discord


class User:

    def __init__(self, members):
        self.name = str(members)
        self.counter = 0
        self.roles = members.roles

    def __repr__(self):
        return self.name

    
    def __str__(self):
        return self.name


