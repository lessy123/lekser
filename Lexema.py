import Litera

class Lexema:
    '''
        Даныный класс предназначен для регистрации
        очередной лексемы и вывода их в выходной поток.
    '''

    def __init__(self):
        self.value = ''
        self.ix = self.ixLast = 0

    def LexFirst(self, litera):     #регистрация первого символа
        self.ix = 0                   #размер лексемы
        self.ixLast = 30              #максимальный размер лексемы
        self.value = litera.value

    def LexNext(self, litera):      #регистрация следующего символа
        if self.ix != self.ixLast:
            self.ix += 1
            self.value += litera.value

    def LexStop(self):              #разденелие лексем
        self.ix += 1
        self.value += '\0'       

    def Print(self, outputFile):
        outputFile.write(self.value)
