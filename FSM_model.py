from enum import Enum
import Lexema as Lex
import Litera as Lit

class StateType(Enum):
    S0 = 0      # Начальное состояние автомата (Ожидание первого символа)
    NXTLIT = 1  # Ожидание следующей литеры идентификатора 
    STOP = 2    # Конец текста (Завершиющее состояние)
    ERR = 3     # Ошибка (Завершающее состояние)

class Synterm(Enum):    #код типа символа
    LETTER = 0              #буквы
    DIGIT = 1               #цыфры
    SPACE = 2               #символ табуляции
    ENDFILE = 3             #файл закончен
    NOALP = 4               #запрещенный символ


class FSM_Model:
    '''
        Класс автомата, хранящий возможные состояния автомата,
        потоки ввода и вывода, текущее состояние автомата, и 
        функции переходов в состояния конечного автомата.
    '''

    input = None
    output = None
    currentState = None

    def __init__(self, input, output):
        self.input = input            #входная информация
        self.output = output          #выходная информация
        self.currentState = StateType.S0  #текущий режим автомата

    def Start(self):
        litera = Lit.Litera()
        ident = Lex.Lexema()

        while True:
            litera.GetLit(self.input)

            if self.currentState == StateType.S0:         #если автомат в режиме ожидания первого символа
                self.Process_S0(litera, ident)
            elif self.currentState == StateType.NXTLIT:   #если автомат в режиме ожидания следующего символа
                self.Process_NXTLIT(litera, ident)
            elif self.currentState == StateType.STOP:     #если автомат в режиме завершения работы
                self.Process_STOP()
                break
            elif self.currentState == StateType.ERR:      #если автомат в режиме "найденна ошибка"
                self.Process_ERR()
                break        

    def Process_S0(self, litera, ident):
        synterm = litera.GetSynterm()
        
        if synterm == Synterm.SPACE:
            self.currentState = StateType.S0          #перевод автомата в режим ожидания первого символа в лексеме
        elif synterm == Synterm.LETTER:
            ident.LexFirst(litera)                    #запись в лексему литеру  
            self.currentState = StateType.NXTLIT      #перевод автомата в режим ожидания следующего символа
        elif synterm == Synterm.ENDFILE:
            self.currentState = StateType.STOP        #перевод автомата в режим завершения работы
        else:
            self.currentState = StateType.ERR         #перевод автомата в режим "найденна ошибка"
        
    def Process_NXTLIT(self, litera, ident):
        synterm = litera.GetSynterm()
        
        if synterm == Synterm.SPACE:                        #если символ пробел или символ табуляции
            ident.LexStop()                                 #разделяет лексему
            ident.Print(self.output)
            self.output.write('\n')
            self.currentState = StateType.S0              #переключение автомата в начальное состояние автомата
        elif synterm in [Synterm.LETTER, Synterm.DIGIT]:    #если символ цифра или буква
            ident.LexNext(litera)                           #то записываем букву в лексему
            self.currentState = StateType.NXTLIT          #переклучение автомата в режим ожидания нового символа
        elif synterm == Synterm.ENDFILE:
            ident.LexStop()
            ident.Print(self.output)
            self.output.write('\n')
            self.currentState = StateType.STOP            #переключение автомата в режим конца текста
        else:
            self.currentState = StateType.ERR             #переключение автомата в режим ошибки

    def Process_STOP(self):
        self.output.write('Stopped successfully\n')

    def Process_ERR(self):
        self.output.write('Stopped in error state\n')
