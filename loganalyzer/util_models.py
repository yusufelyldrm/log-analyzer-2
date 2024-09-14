class Log:
    def __init__(self, date, text):
        self.date = date
        self.text = text

    def __repr__(self):
        return f"{self.date} {self.text}"
