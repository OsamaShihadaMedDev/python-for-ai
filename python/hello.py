class subjects:
    def __init__(self, text, diff):
        self.name = text
        self.hard = diff

    def assess(self):
        if (self.hard == True):
            print(f"{self.name} is a hard subject")
        return self

topic_chooser = subjects("cardiology", True)
topic_chooser.assess()
print(topic_chooser.name)