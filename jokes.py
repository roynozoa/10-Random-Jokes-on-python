# Jokes class

class Jokes:

    # construction
    def __init__(self, joke_type, setup, punchline):
        self.joke_type = joke_type
        self.setup = setup
        self.punchline = punchline

    def __str__(self):
        return f"Type : {self.joke_type} \nSetup : {self.setup} \nPunchline : {self.punchline}\n"
