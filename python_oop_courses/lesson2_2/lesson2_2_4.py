class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists):
        self.assists += assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
