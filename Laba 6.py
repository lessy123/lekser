import hashlib
import matplotlib.pyplot as plt

class guards_date:   #является ячейкой помяти
    def __init__(self,text):
        self.id=text[1]     #код хранимой информации
        self.text=text[0]  #хранит информацию
    def delet(self):    #функция удаления
        self.id=None
        self.text=None


class key_date:     #хранит информацию о ключе
    def __init__(self, name,pair):
        self.name=str(name)      #ключ
        self.pair=[]        #ссылка на элемент памяти :guards_date
        if pair:
            self.pair.append(guards_date(pair))
    def add_pair(self,pair):    #добавление ссылки на ячейку памяти
        for i in self.pair:
            if i.text==pair[0]:
                return
        self.pair.append(guards_date(pair))
    def del_key(self):          #удаление ключа
        self.id=None
        for i in self.pair:
            i.delet()
        self.pair=None
    def del_pair(self,number):
        self.pair[number].delet()
        self.pair.pop(number)

class key_list:             #"ключница"
    def __init__(self):     #
        self.key=[]         #содержит ссылку на ключи :key_date
    def new_pair(self,key,pair_text): #создает новую связь 
        point=self.search_key(str(key))
        if point>=0:                     #если ключ совпадает в связке с другим
            self.key[point].add_pair(pair_text)      #то к нему приписывается новая ячейка
        else:
            self.new_key(key,pair_text)  #иначе создается новый ключ

    def new_key(self,key,pair_text):     #создает новый ключ
        self.key.append(key_date(key,pair_text))


    def search_key(self,key):    #ищет совпадения ключей, ищет по имени
        for i in range(len(self.key)):
            if self.key[i].name==key:    #если находит
                return i                 #то возвращает его номер
        return -1                #иначе возвращает -1(значащее "не нашел")

    def del_key(self,number:int):   #удаляет ключ под номером number
        self.key[number].del_key()
        self.key.pop(number)
    def del_key(self,text:str):
        point=self.search_key(text)
        if point>=0:                     #если ключ совпадает в связке с другим
            self.key[point].del_key()      #то к нему приписывается новая ячейка
        else:
            print("Ключ не найден")
    def view_key(self):
        for i in self.key:
            print(i.name+":")
            for j in i.pair:
                print("---"+str(j.text)+": "+ str(j.id))
    def hist(self):
        index = [i for i in range(len(self.key))]
        values = []
        for key in self.key:
            if len(key.pair):
                values.append(len(key.pair))                        
            else:
                values.append(0)
        plt.bar(index, values)
        plt.show()

#Хеш функции
#Хэш-функция берем сумму первой и последней букв слова
def MyHashFunction(word):
    if word != '':
        return (ord(word[0])+ord(word[-1]))
    return None
#Хэш-функция берем все букву и умножаем на их порядковый номер
def MyHashNumberFunction(word):
    if word != '':
        sum=0
        for i in range(len(word)):
            sum+=i*ord(word[i])
        return sum
    return None
#Хэш-функция MD5 
def HashMD5(word):
    if word != '':
        return hashlib.md5(word.encode()).hexdigest()
    return None

if __name__ == '__main__':
    pair=[None]
    if pair[0]:
        print(pair)
    key=key_list()
    #id_text=0
    with open('text6.txt', 'r') as file:
        for index, word in enumerate(file.read().split(' ')):
            word = ''.join(letter for letter in word if letter.isalpha())
            #print(index, word)
     #       id_text+=1
            key.new_pair(MyHashFunction(word),[word,index])
    key.view_key()
    key.hist()
    print('')
    print('------------------------------')
    print('')
    key2=key_list()
    with open('text6.txt', 'r') as file:
        for index, word in enumerate(file.read().split(' ')):
            word = ''.join(letter for letter in word if letter.isalpha())
            #print(index, word)
            key2.new_pair(MyHashNumberFunction(word),[word,index])
    key2.view_key()
    key2.hist()
    print('')
    print('------------------------------')
    print('')
    key3=key_list()
    with open('text6.txt', 'r') as file:
        for index, word in enumerate(file.read().split(' ')):
            word = ''.join(letter for letter in word if letter.isalpha())
            #print(index, word)
            key3.new_pair(HashMD5(word),[word,index])
    key3.view_key()
    key3.hist()

    '''
    Figure 1 - первый построенный график. Метод хеширования - сумма первой и последней буквы
    Figure 2 - второй построенный график. Метод хеширования - сумма произведений букв на их порядковый номер в слове
    Figure 3 - третьий построенный график. Метод хеширования - MD5 
    209:
---live: 0
---can: 20
215:
---in: 1
---look: 12
219:
---virtue: 2
---heavens: 39
---keep: 40
221:
---no: 3
201:
---desire: 4
---die: 53
217:
---the: 6
---theyre: 65
204:
---grave: 7
---gone: 31
207:
---an: 8
---ashen: 73
212:
---angels: 9
---one: 19
---as: 27
---hell: 114
213:
---choir: 10
---goddamn: 47
---apart: 59
---paradise: 76
238:
---you: 11
227:
---to: 13
---sleep: 33
214:
---heaven: 14
---clouds: 29
197:
---and: 15
233:
---wonder: 16
240:
---why: 17
216:
---see: 21
---fear: 43
---turned: 69
225:
---them: 22
---seen: 37
---must: 112
236:
---sky: 25
222:
---just: 26
205:
---have: 30
---angel: 50
---fading: 66
199:
---be: 36
198:
---alone: 41
---behind: 62
237:
---they: 44
223:
---question: 45
226:
---not: 48
---so: 72
229:
---when: 51
210:
---i: 52
224:
---never: 57
211:
---from: 60
232:
---us: 61
230:
---souls: 67
220:
---whove: 68
---white: 74
206:
---ice: 71
None:
---: 118

------------------------------

644:
---live: 0
110:
---in: 1
---an: 8
1654:
---virtue: 2
111:
---no: 3
---to: 13
---so: 72
1607:
---desire: 4
306:
---the: 6
1066:
---grave: 7
---ashen: 73
---white: 74
1626:
---angels: 9
1097:
---choir: 10
345:
---you: 11
654:
---look: 12
1603:
---heaven: 14
310:
---and: 15
1605:
---wonder: 16
346:
---why: 17
312:
---one: 19
317:
---can: 20
303:
---see: 21
633:
---them: 22
---seen: 37
349:
---sky: 25
695:
---just: 26
---must: 112
115:
---as: 27
---us: 61
1656:
---clouds: 29
636:
---have: 30
---when: 51
634:
---gone: 31
1061:
---sleep: 33
101:
---be: 36
2293:
---heavens: 39
639:
---keep: 40
1064:
---alone: 41
637:
---fear: 43
669:
---they: 44
3089:
---question: 45
2204:
---goddamn: 47
343:
---not: 48
1051:
---angel: 50
0:
---i: 52
307:
---die: 53
1096:
---never: 57
1112:
---apart: 59
663:
---from: 60
1564:
---behind: 62
1630:
---theyre: 65
1567:
---fading: 66
1129:
---souls: 67
1084:
---whove: 68
1579:
---turned: 69
301:
---ice: 71
2938:
---paradise: 76
641:
---hell: 114
None:
---: 118

------------------------------

d0dbe915091d400bd8ee7f27f0791303:
---live: 0
13b5bfe96f3e2fe411c9f66f4a582adf:
---in: 1
abb312ffe8441d0732785228769d6dba:
---virtue: 2
7fa3b767c460b54a2be4d49030b349c7:
---no: 3
99e0d947e01bbc0a507a1127dc2135b1:
---desire: 4
8fc42c6ddf9966db3b09e84365034357:
---the: 6
386a023bd38fab85cb531824bfe9a879:
---grave: 7
18b049cc8d8535787929df716f9f4e68:
---an: 8
82a7c395a86348dd4bfd11bb05b71cbf:
---angels: 9
b84d02569b3283c267820c62f9ab6e72:
---choir: 10
639bae9ac6b3e1a84cebb7b403297b79:
---you: 11
8c4291f6956da81515a5c0caec2976d0:
---look: 12
01b6e20344b68835c5ed1ddedf20d531:
---to: 13
eb31870669f13fd8444c2bc918375f09:
---heaven: 14
be5d5d37542d75f93a87094459f76678:
---and: 15
10cf1fdf6ad958eeffa9853f6885cec9:
---wonder: 16
531e70a6745d07a8befbd79e5cc7e4c1:
---why: 17
f97c5d29941bfb1b2fdab0874906ab82:
---one: 19
2c61ebff5a7f675451467527df66788d:
---can: 20
1e8e42b87a65326b98ced7d3af717a72:
---see: 21
e886b5e8a9e6a8b1a306ac1efb18ec84:
---them: 22
900bc885d7553375aec470198a9514f3:
---sky: 25
8134b84030cca5285ed0e0b31ba06f10:
---just: 26
f970e2767d0cfe75876ea857f92e319b:
---as: 27
073caed738eb89c95a716053cea97b7c:
---clouds: 29
b42dad5453b2128a32f6612b13ea5d9f:
---have: 30
50c1f58be7f5e47e0f53d64c094783c2:
---gone: 31
c9fab33e9458412c527c3fe8a13ee37d:
---sleep: 33
910955a907e739b81ec8855763108a29:
---be: 36
d5b4a9a5a6b50466e8837c3cd98c3442:
---seen: 37
78e72fc837d102b2762379476ce20eb7:
---heavens: 39
18ccf61d533b600bbf5a963359223fe4:
---keep: 40
c42bbd90740264d115048a82c9a10214:
---alone: 41
eb88d7636980738cd0522ea69e212905:
---fear: 43
2bb3d86d95234affa7c5bd68c4bab606:
---they: 44
5494af1f14a8c19939968c3e9e2d4f79:
---question: 45
fd3c5173c6b328e2e98f7e40d6ba6246:
---goddamn: 47
d529e941509eb9e9b9cfaeae1fe7ca23:
---not: 48
f4f068e71e0d87bf0ad51e6214ab84e9:
---angel: 50
df491a4de50739fa9cffdbd4e3f4b4bb:
---when: 51
865c0c0b4ab0e063e5caa3387c1a8741:
---i: 52
81b63b9d54b303edeaf9765a6915ee13:
---die: 53
c7561db7a418dd39b2201dfe110ab4a4:
---never: 57
bce1c9ffaf9d636a55ad1e0b5d704053:
---apart: 59
d98a07f84921b24ee30f86fd8cd85c3c:
---from: 60
0b3b97fa66886c5688ee4ae80ec0c3c2:
---us: 61
9da3be8f92c0bbfd7a7d6d6ec0b3fad3:
---behind: 62
f9c2115ec3c5ef45b945fe51fdb1c459:
---theyre: 65
7001728411006ee87fe76f849ff7b0bf:
---fading: 66
6e312578632aa2656088edd44a39ae9c:
---souls: 67
2748aee1d2a1927bf7c6db8dfa76144a:
---whove: 68
e5412b8b872f9bbe68d8e825dd9f1d5c:
---turned: 69
7bdff76536f12a7c5ffde207e72cfe3a:
---ice: 71
b807023f87e63b8ada92f79f546ff9cc:
---so: 72
eea1fefe34baa4e9d2cd6c3bb84dc326:
---ashen: 73
d508fe45cecaf653904a0e774084bb5c:
---white: 74
96ac9a11d94d8f982ba476aa4b5ef503:
---paradise: 76
d0e6ef34e76c41b0fac84f608289d013:
---must: 112
4229d691b07b13341da53f17ab9f2416:
---hell: 114
None:
---: 118
'''
