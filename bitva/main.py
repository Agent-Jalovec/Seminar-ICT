#!/usr/bin/env python3

from simple import Kostka
from lod import Lod, Stihac, Korbačik

class Sektor:
    """

    Sprava souboje dvou lodi
    """

    def __init__(self, lod_1, lod_2, kostka, jmeno="bez nazvu"):
        self._jmeno = jmeno
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
        #print(f'Trup: {lod._trup}\n')
        print(f'Trup: {lod.graficky_trup()}')
        if isinstance(lod, Stihac):
            print(f'Energie: {lod.graficka_energie()}')

        """
        nemusi tu byt print lod jmeno protoze mame v lodi timto zadefinovanou textovou podobu toho souboru  
            
        def __str__(self):
            return str(self._jmeno)
            """

    def _vykresli(self):
        self._vycisti()
        print(f'======================= Sektor {self._jmeno} ======================= \n')
        print('Lodě\n')
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)

        

    def souboj(self):
        print(f"Vítej v sektoru {self._jmeno}!")
        print("======================")
        print(f"Dnes se utkají loďe:")
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print("Zahajit souboj...")
        input()

        import random
        if random.randint(0, 1):
            self._lod_1, self._lod_2 = self._lod_2, self._lod_1


            """
            pomocna_promenna = self._lod_1
            self._lod_1 = self._lod_2
            self.lod_2 = pomocna_promenna

            nevim proc nefunguje
            """

        




            

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
            _time.sleep(.5)

if __name__ == '__main__':
    k = Kostka(10)
    lodicka = Lod("Queen Anne's Revenge", 500, 30, 20, k)
    clun = Lod("Iron Lung", 95, 55, 45, k)
    lod3 = Lod("Bomboklad", kostka=k, trup=80, utok=60, stit=70)
    fighter = Stihac("Dingle", 90, 50, 60, k, 100, 90)
    lod4 = Korbačik("Korbačik", 60, 90, 90, k)

    orion = Sektor(lodicka, fighter, k, "Orion")
    #orion = Sektor(lodicka, clun, k, "Orion")
    gamma = Sektor(lod3, lod4, k, "Gamma")

    orion.souboj()
    gamma.souboj()