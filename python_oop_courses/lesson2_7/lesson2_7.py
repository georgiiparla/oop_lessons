class Notebook:
    def __init__(self, notes: list):
        self._notes = notes

    @property
    def notes_list(self):
        for i in range(0, len(self._notes)):
            print(f'{i+1}.{self._notes[i]}')
