#!/usr/bin/env python3

from simple import Kostka
from lod import Lod

class Sektor:
    """

    Sprava souboje dvou lodi
    """

    def __init__(self, lod_1, lod_2, kostka):
        self._lod_1 = lod_1
        self._lod_2 = lod_2
        self._kostka = kostka

    def _vycisti(self):
        #podtrzitko znamena, ze tu metodu muze pustit jen sam ten objekt a ne nikdo jiny
        import sys as _sys
        import subprocess as _subprocess
        #modul je importovan a pomoci "as" prejmenovan, aby bylo mozne ho spoustet pouze timto objektem
        if _sys.platform.startswith('win'):
            _subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subprocess.call(['clear'])

    def _vypis_lod(self, lod):
        print(lod)
        print(f'Trup: {lod._trup}\n')
        ###nemusi tu byt print lod jmeno protoze mame v lodi timto zadefinovanou textovou podobu toho souboru  
            
        #def __str__(self):
            #return str(self._jmeno)

    def _vykresli(self):
        self._vycisti()
        print('======================= Sektor Orion =======================\n')
        print('Lodě\n')
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)

        

    def souboj(self):
        print("Vítej v sektoru Orion!")
        print("======================")
        print(f"Dnes se utkají loďe:")
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print("Zahajit souboj...")
        input()

        while self._lod_1.je_operacni() and self._lod_2.je_operacni():
            self._lod_1.utoc(self._lod_2)
            self._vykresli()
            self._vypis_zpravu(self._lod_1.vypis_zpravu())
            self._vypis_zpravu(self._lod_2.vypis_zpravu())

            if self._lod_2.je_operacni():
                self._lod_2.utoc(self._lod_1)
                self._vykresli()
                self._vypis_zpravu(self._lod_2.vypis_zpravu())
                self._vypis_zpravu(self._lod_1.vypis_zpravu())



    
    def _vypis_zpravu(self, zprava):
        import time as _time
        if zprava:
            print(zprava)
            _time.sleep(.2)

if __name__ == '__main__':
    k = Kostka(10)
    lodicka = Lod("Queen Anne's Revenge", 100, 40, 50, k)
    clun = Lod("Iron Lung", 40, 20, 30, k)
    orion = Sektor(lodicka, clun, k)

    orion.souboj()