class Row:
    
    def toString(self):
        return self.user + " - " + self.location + " - " + self.text

    def __init__(self, user, location, text):
        self.user = user
        self.location = location
        self.text = text