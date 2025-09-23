#!/usr/bin/env python3

'''
Popis programu:
Opakuje input zadaným počtem
'''

def opakuj():
    promenna = input("Zadej, co mam zopakovat: ")
    pocet = int(input("Kolikrat to mam zopakovat: "))
    for i in range(pocet):
        if i == 6:
            print("*****")
        print(i, promenna)
  
if __name__ == '__main__':
      opakuj()
    

#print((promenna + '\n') * pocet)
        #jednodussi verze loopu
        #extra radek eliminujes takto: print((promenna + '\n') * pocet, end='')
        #btw cely blok kodu muzes zakomentovat tremi apostrofy


        #bruh, nevim jak spustit tu funkci z terminalu
