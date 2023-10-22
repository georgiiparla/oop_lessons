class Password:
    def __init__(self, password):
        self.password = password

    @property
    def strength(self):
        if len(self.password) < 8:
            return 'Weak'
        elif len(self.password) >= 12:
            return 'Strong'
        else:
            return 'Medium'
