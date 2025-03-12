import dictionary as d
import richWord as rw

dizionari = d.Dictionary()
class MultiDictionary:

    def __init__(self):
        dizEng = dizionari.loadDictionary("English.txt")
        dizIta = dizionari.loadDictionary("Italian.txt")
        dizSpa = dizionari.loadDictionary("Spanish.txt")

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        pass


