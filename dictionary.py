class Dictionary:
    def __init__(self):
        self.diz = []

    def loadDictionary(self,dict):
        """
        leggo il file dizionario
        :param dict: 
        :return: 
        """""
        with open(dict,'r',encoding="utf-8") as file:
            for row in file:
                parola = row.strip.split(" ")
                self.diz.append(parola.lower())

    def printAll(self):
        pass


    @property
    def dict(self):
        return self._dict