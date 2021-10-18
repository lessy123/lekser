from FSM_model import Synterm

class Litera:
    '''
        Класс, хранящий входные сигналы автомата, считывающий 
        литеры и определяющей синтерму (продвижение по входной 
        цепочке конечного автомата).
    '''

    def __init__(self):
        self.value = None       #текущий символ
        self.synterm = None     #тип символа(его код)

    def GetLit(self, input):
        self.value = input.read(1)
        if not self.value:              #если не найден символ
            self.synterm = Synterm.ENDFILE    
        elif self.value.isspace():      #проверка, является ли символ пробелом, 
                                        #элементом табуляции и прочее
            self.synterm = Synterm.SPACE
        elif self.value.isdigit():      #если это число
            self.synterm = Synterm.DIGIT
        elif self.value.isalpha():      #если это буква
            self.synterm = Synterm.LETTER
        else:                           #иначе данный символ отмечается как незаконный
            self.synterm = Synterm.NOALP
        return self.synterm

    def GetSynterm(self):
        return self.synterm    
