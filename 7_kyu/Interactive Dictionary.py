class Dictionary():
    def __init__(self):
        self.dict = {}

    def newentry(self, word, definition):
        self.dict[word]=definition

    def look(self, key):
        try:
            return self.dict[key]
        except:
            return "Can't find entry for {}".format(key)