
import hashlib
import matplotlib.pyplot as plt

#from my_laba import MyHashFunction,MyHashNumberFunction,HashMD5
#Хеш функции
#Хэш-функция берем сумму первой и последней букв слова 
def MyHashFunction(word):
    if word != '':
        return (ord(word[0])+ord(word[-1]))//10
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

class guards_date:   #является ячейкой помяти
    def __init__(self,text=None):
        if text:
            self.id=text[1]     #код хранимой информации
            self.text=text[0]  #хранит информацию
        else: 
            self.id=text    #код хранимой информации
            self.text=text  #хранит информацию
    def delet(self):    #функция удаления
        self.id=None
        self.text=None  #функция удаления

class key_date:     #хранит информацию о ключе
    def __init__(self, name,pair=None):
        self.key_name=str(name)      #ключ
        self.pair=guards_date(pair)        #ссылка на элемент памяти :guards_date

    def replacement_pair(self,pair):    #замена ссылки на ячейку памяти
        self.pair=guards_date(pair)            #замена ссылки на ячейку памяти
    def del_key(self):          #удаление ключа
        self.key_name=None
        self.pair.delet()
        self.pair=None                      #удаление ключа

class hash:
    def __init__(self, name,key=None,pair=None):
        self.hash_name=str(name)      #хеш
        self.keys=[]        #ссылка на ключи :key_date
        if key!=None:
            self.keys.append(key_date(key))
            if pair!=None:
                self.keys[len(self.keys)-1].replacement_pair(pair)    #хранит ключи
    def add_key(self,key,pair):    #добавление ссылки на ячейку памяти
        for i in self.keys:
            if i.key_name==key:
                i.replacement_pair(pair)
                return True
        self.keys.append(key_date(key, pair))              #добавляет или заменяет ключ и данные его
        return False
    def del_hash(self):          #удаление хеша
        self.hash_name=None
        for i in self.keys:
            i.del_key()
        self.keys=None                      #удаление хеша
    def del_key_number(self,number): #удаление ключа по номерному порядку
        if number>len(self.keys)-1:
            return False
        self.keys[number].del_key()
        self.keys.pop(number)
        return True         #удаление ключа по номерному порядку
    def del_key_text(self,text): #удаление ключа по содержанию
        x=self.search_key(text)
        if x>=0:
            self.keys[x].del_key()
            self.keys.pop(x)
            return True
        else: 
            return False             #удаление ключа по содержанию
    def search_key(self,text):                  #поиск ключа по содержанию
        for i in range(len(self.keys)):
            if self.keys[i].key_name==str(text):
                return i        
        return -1               #поиск ключа по содержанию
    def return_value_key(self,text):
        x=self.search_key(text)
        if x>=0:
            return self.keys[x].pair
        return None         #выводит значение данного ключа
                    
class hash_table:
    def __init__(self,name='Name_table'):
        self.hash_table_name=str(name)      #название хеш-таблицы
        self.hash_table=[]        #хранит список кеша  :hash
    def search_hash(self,text):                  #поиск hash
        for i in range(len(self.hash_table)):
            if self.hash_table[i].hash_name==str(text):
                return i        
        return -1                   #поиск hash
    def add_hash(self,name_hash,name_key,pair):    #добавляет пару в хеш-таблицу
        x=self.search_hash(name_hash)
        if x>=0:
            self.hash_table[x].add_key(name_key,pair)
        else:    
            self.hash_table.append(hash(name_hash,name_key,pair))   #добавляет пару в хеш-таблицу
    def del_hash_table(self):          #удаление хеш-таблицы
        self.hash_table_name=None
        for i in self.hash_table:
            i.del_hash()
        self.hash_table=None                     #удаление хеш-таблицы
    def return_key(self,name_hash,name_key):
        x=search_hash(name_hash)
        if x>=0:
            y=self.hash_table[x].keys.search_key(name_key)
            if y>=0:
                return self.hash_table[x].keys[y].pair
        return -1      #получение доступа к элементу памяти                     
    def hist(self):
        index = [i for i in range(len(self.hash_table))]
        values = []
        for key in self.hash_table:
            if len(key.keys):
                values.append(len(key.keys))                        
            else:
                values.append(0)
        plt.bar(index, values)
        plt.show()
    def view(self):
        print(self.hash_table_name)
        t1='-'
        t2='--'
        t3='---'
        for i in self.hash_table:
            print(t1+str(i.hash_name))#хеш - значение
            for j in i.keys:
                print(t2+str(j.key_name))#ключ - значение
                print(t3,j.pair.id,j.pair.text)


if __name__ == '__main__':
    pair=[None]
    if pair[0]:
        print(pair)
    hash_tab=hash_table()
    #id_text=0
    with open('text6.txt', 'r') as file:
        for index, word in enumerate(file.read().split(' ')):
            word = ''.join(letter for letter in word if letter.isalpha())
            #print(index, word)
     #       id_text+=1
            hash_tab.add_hash(MyHashFunction(word),word,[word,index])
    hash_tab.view()
    hash_tab.hist()
    print('')
    print('------------------------------')
    print('')
    key2=hash_table()
    with open('text6.txt', 'r') as file:
        for index, word in enumerate(file.read().split(' ')):
            word = ''.join(letter for letter in word if letter.isalpha())
            #print(index, word)
            key2.add_hash(MyHashNumberFunction(word),word,[word,index])
    key2.view()
    key2.hist()
    print('')
    print('------------------------------')
    print('')
    key3=hash_table()
    with open('text6.txt', 'r') as file:
        for index, word in enumerate(file.read().split(' ')):
            word = ''.join(letter for letter in word if letter.isalpha())
            #print(index, word)
            key3.add_hash(HashMD5(word),word,[word,index])
    key3.view()
    key3.hist()
