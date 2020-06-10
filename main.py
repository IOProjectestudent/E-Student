"""
Należy mieć umieszczoną bazę danych we wspólnym folderze z plikiem .py by program działał poprawnie.
Uczeń o nr_indeksu: 45392 ma wstawione oceny by można było sprawdzić działanie zaimplementowanych rozwiazan.3
"""

import sqlite3
from collections import namedtuple
import os
connection = sqlite3.connect("./students.db")
cursor = connection.cursor()

Student = namedtuple("Student", "nr_indeksu imie nazwisko grupa")
doOceny = namedtuple("Oceny", "nr_indeksu ocena")

def tabela_plastyka():
    cursor.execute("DROP TABLE IF EXISTS tabela_plastyka")
    cursor.execute("""
        CREATE TABLE tabela_plastyka(
          nr_indeksu INTEGER,
          przedmiot TEXT,
          ocena INTEGER,
          waga INTEGER
          )
        """)
    connection.commit()

def tabela_geografia():
    cursor.execute("DROP TABLE IF EXISTS tabela_geografia")
    cursor.execute("""
        CREATE TABLE tabela_geografia(
          nr_indeksu INTEGER,
          przedmiot TEXT,
          ocena INTEGER,
          waga INTEGER
          )
        """)
    connection.commit()    
    
def tabela_fizyka():
    cursor.execute("DROP TABLE IF EXISTS tabela_fizyka")
    cursor.execute("""
        CREATE TABLE tabela_fizyka(
          nr_indeksu INTEGER,
          przedmiot TEXT,
          ocena INTEGER,
          waga INTEGER
          )
        """)
    connection.commit()    
    
def tabela_matematyka():
    cursor.execute("DROP TABLE IF EXISTS tabela_matematyka")
    cursor.execute("""
        CREATE TABLE tabela_matematyka(
          nr_indeksu INTEGER,
          przedmiot TEXT,
          ocena INTEGER,
          waga INTEGER
          )
        """)
    connection.commit()  

def dodaj_studenta(nr_indeksu,imie, nazwisko, grupa):
    sql = """
        INSERT INTO tabela_student (nr_indeksu,imie, nazwisko, grupa)
        VALUES ({},"{}", "{}", "{}")
    """.format(nr_indeksu,imie, nazwisko, grupa)
    cursor.execute(sql)
    connection.commit()

def wyswietl_wszystkich_studentow():
    sql = "SELECT * FROM students"
    rows = cursor.execute(sql)
    student_rows = rows.fetchall()
    return [ Student(*student_row) for student_row in student_rows ]

def wyszukaj(nr_indeksu):
    sql = "SELECT * FROM students WHERE nr_indeksu = {}".format(nr_indeksu)
    rows = cursor.execute(sql)
    student_row = rows.fetchone() 
    if student_row == None:
      return "Student o podanym numerze indeksu nie figuruje w bazie."
    else:
      return Student(*student_row)

def dodaj_ocene1(nr_indeksu,przedmiot,ocena,waga):
    sql = """
        INSERT INTO tabela_plastyka (nr_indeksu,przedmiot,ocena,waga)
        VALUES ({},"{}",{},{})
    """.format(nr_indeksu,przedmiot,ocena,waga)
    cursor.execute(sql)
    connection.commit()

def dodaj_ocene2(nr_indeksu,przedmiot,ocena,waga):
    sql = """
        INSERT INTO tabela_geografia (nr_indeksu,przedmiot,ocena,waga)
        VALUES ({},"{}",{},{})
    """.format(nr_indeksu,przedmiot,ocena,waga)
    cursor.execute(sql)
    connection.commit()
    
def dodaj_ocene3(nr_indeksu,przedmiot,ocena,waga):
    sql = """
        INSERT INTO tabela_fizyka (nr_indeksu,przedmiot,ocena,waga)
        VALUES ({},"{}",{},{})
    """.format(nr_indeksu,przedmiot,ocena,waga)
    cursor.execute(sql)
    connection.commit()

def dodaj_ocene4(nr_indeksu,przedmiot,ocena,waga):
    sql = """
        INSERT INTO tabela_matematyka (nr_indeksu,przedmiot,ocena,waga)
        VALUES ({},"{}",{},{})
    """.format(nr_indeksu,przedmiot,ocena,waga)
    cursor.execute(sql)
    connection.commit()


def wyszukaj_studenta2(nr_indeksu):
    sql = "SELECT * FROM students WHERE nr_indeksu = {}".format(nr_indeksu)
    cokolwiek = 1
    rows = cursor.execute(sql)
    ocena_row = rows.fetchone()
    if ocena_row==None:
      return("Student o podanym numerze indeksu nie figuruje w bazie.")
    else:
      return cokolwiek
      

" w tym miejsciu muszą byc 4 funkcje o podobnej budowie.W innym przypadku zapytanie sql musialoby byc w menu co byloby rownoznaczne z wadliwym naliczaniem lacznych punktow ECTS"

def srednia1(nr_indeksu,przedmiot):
  sql = "SELECT * FROM tabela_plastyka WHERE nr_indeksu = {} AND przedmiot = '{}'".format(nr_indeksu,przedmiot)

  rows = cursor.execute(sql)
  ocena_row = rows.fetchone()
  tab = []
  for row in cursor.execute(sql):
    tab.append(row)
  
  srednia = 0
  suma_wag = 0
  
  for i in range(0,len(tab),1):
    srednia += (tab[i][2]*tab[i][3])
    suma_wag += tab[i][3] 

  if srednia == 0:
    return("Podano bledny numer indeksu lub przedmiot")
  else:
    srednia = round((srednia / suma_wag),3)
    return srednia


def srednia2(nr_indeksu,przedmiot):
  sql = "SELECT * FROM tabela_geografia WHERE nr_indeksu = {} AND przedmiot = '{}'".format(nr_indeksu,przedmiot)

  rows = cursor.execute(sql)
  ocena_row = rows.fetchone()
  tab = []
  for row in cursor.execute(sql):
    tab.append(row)
  
  srednia = 0
  suma_wag = 0
  
  for i in range(0,len(tab),1):
    srednia += (tab[i][2]*tab[i][3])
    suma_wag += tab[i][3] 

  if srednia == 0:
    return("Podano bledny numer indeksu lub przedmiot")
  else:
    srednia = round((srednia / suma_wag),3)
    return srednia



def srednia3(nr_indeksu,przedmiot):
  sql = "SELECT * FROM tabela_fizyka WHERE nr_indeksu = {} AND przedmiot = '{}'".format(nr_indeksu,przedmiot)

  rows = cursor.execute(sql)
  ocena_row = rows.fetchone()
  tab = []
  for row in cursor.execute(sql):
    tab.append(row)
  
  srednia = 0
  suma_wag = 0
  
  for i in range(0,len(tab),1):
    srednia += (tab[i][2]*tab[i][3])
    suma_wag += tab[i][3] 

  if srednia == 0:
    return("Podano bledny numer indeksu lub przedmiot")
  else:
    srednia = round((srednia / suma_wag),3)
    return srednia


def srednia4(nr_indeksu,przedmiot):
  sql = "SELECT * FROM tabela_matematyka WHERE nr_indeksu = {} AND przedmiot = '{}'".format(nr_indeksu,przedmiot)

  rows = cursor.execute(sql)
  ocena_row = rows.fetchone()
  tab = []
  for row in cursor.execute(sql):
    tab.append(row)
  
  srednia = 0
  suma_wag = 0
  
  for i in range(0,len(tab),1):
    srednia += (tab[i][2]*tab[i][3])
    suma_wag += tab[i][3] 
  
  if srednia == 0:
    return("Podano bledny numer indeksu lub przedmiot")
  else:
    srednia = round((srednia / suma_wag),3)
    return srednia


tabela_przedmioty = ['plastyka','geografia','fizyka','matematyka']

while True:
  print("""
  1. Wyświetl listę studentów
  2. Wyszukaj studenta
  3. Dopisz ocene
  4. Wyswietl oceny, srednia, punkty ECTS
  """)

  choice = input("  Podaj operacje (1-4): ")

  if choice == "1": #wyswietl
    all_students = wyswietl_wszystkich_studentow()
    for student in all_students:
      print("{}, {} {}, {}".format(*student))
      
  elif choice == "2": #wyszukaj
    os.system('clear')
    zmienna_boolowska = True
    while zmienna_boolowska == True:
      indeks = input("Podaj nr indeksu: ")
      if len(indeks) != 5:
        print("Podano niewłaściwy numer indeksu.\n")
      if len(indeks) == 5:
        sprawdzenie =  wyszukaj(indeks)
        if isinstance(sprawdzenie, str):
          print("Podany numer indeksu nie figuruje w bazie.")
        else:
          print(sprawdzenie)
          break 


  elif choice == "3": #dopisz ocene
    os.system('clear')

    zmienna_boolowska = True

    while zmienna_boolowska == True:
      nazwiskoo = input("Podaj nr indeksu: ")
      czy_w_bazie = wyszukaj_studenta2(nazwiskoo)
      if len(nazwiskoo) == 5 and czy_w_bazie == 1 :
        break
      else:
        print("Uczeń o podanym numerze indeksu nie figuruje w bazie")
        continue

    zmienna_boolowska = True
    while zmienna_boolowska == True:
      przedmiot = input("Podaj przedmiot: ")
      if przedmiot != 'plastyka' and przedmiot != 'geografia' and przedmiot != 'fizyka' and przedmiot != 'matematyka':
        print("Podany przedmiot nie figuruje w bazie / błąd w pisowni")
      else:
        break

    zmienna_boolowska = True

    while zmienna_boolowska == True:
      ocena = int(input("Podaj ocene: "))
      if ocena > 5:
        print("Podano ocene spoza przedziału.\n")
      if ocena <= 5:
        break

    waga = input("Podaj wage: ") # brak ograniczen do wagi

    if przedmiot == 'plastyka':
      dodaj_ocene1(nazwiskoo,przedmiot,ocena,waga)
    if przedmiot == 'geografia':
      dodaj_ocene2(nazwiskoo,przedmiot,ocena,waga)
    if przedmiot == 'fizyka':
      dodaj_ocene3(nazwiskoo,przedmiot,ocena,waga)
    if przedmiot == 'matematyka':
      dodaj_ocene4(nazwiskoo,przedmiot,ocena,waga)
    

  elif choice == "4": #wyswietl oceny, srednia, punkty ECTS
    os.system('clear')
    print("Numer indeksu ma zawsze 5 cyfr.")
    print("Wszystkie litery przedmiotu muszą być z małej litery.")
    print("\n")

    zmienna_boolowska = True

    while zmienna_boolowska == True:
      indeks = input("Podaj nr indeksu: ")
      if len(indeks) != 5:
        print("Podano niewłaściwy numer indeksu.\n")
      if len(indeks) == 5:
        sprawdzenie =  wyszukaj(indeks)
        if isinstance(sprawdzenie, str):
          print("Podany numer indeksu nie figuruje w bazie.")
        else:
          break 

    przedmiot = input("Podaj przedmiot: ")

    srednia11 = srednia1(indeks,'plastyka')
    srednia22 = srednia2(indeks,'geografia')
    srednia33 = srednia3(indeks,'fizyka')
    srednia44 = srednia4(indeks,'matematyka')


    if isinstance(srednia11, float) and srednia11 > 3.000:
      ECTS1 = 5
    if isinstance(srednia11, str):
      ECTS1 = 0
    if isinstance(srednia11, float) and srednia11 <= 3.000:
      ECTS1 = 0 

    if isinstance(srednia22, float) and srednia22 > 3.000:
      ECTS2 = 5
    if isinstance(srednia22, str):
      ECTS2 = 0
    if isinstance(srednia22, float) and srednia22 <= 3.000:
      ECTS2 = 0 

    if isinstance(srednia33, float) and srednia33 > 3.000:
      ECTS3 = 5
    if isinstance(srednia33, str):
      ECTS3 = 0
    if isinstance(srednia33, float) and srednia33 <= 3.000:
      ECTS3 = 0 
    
    if isinstance(srednia44, float) and srednia44 > 3.000:
      ECTS4 = 5
    if isinstance(srednia44, str):
      ECTS4 = 0
    if isinstance(srednia44, float) and srednia44 <= 3.000:
      ECTS4 = 0  
    
    if przedmiot == 'plastyka':
      if isinstance(srednia11, str):
        print("Średnia: ","BRAK OCEN")
      else:
        print("Średnia: ",srednia11)
      
      print("ECTS: ", ECTS1)
      print("Łączna liczba ECTS: ",ECTS1+ECTS2+ECTS3+ECTS4,"/ 20")

    if przedmiot == 'geografia':
      if isinstance(srednia22, str):
        print("Średnia: ","BRAK OCEN")
      else: 
        print("Średnia: ",srednia22)
      print("ECTS: ", ECTS2)
      print("Łączna liczba ECTS: ",ECTS1+ECTS2+ECTS3+ECTS4,"/ 20")

    if przedmiot == 'fizyka':
      if isinstance(srednia33, str):
        print("Średnia: ","BRAK OCEN")
      else: 
        print("Średnia: ",srednia33)
      print("ECTS: ", ECTS3)
      print("Łączna liczba ECTS: ",ECTS1+ECTS2+ECTS3+ECTS4,"/ 20")
 
    if przedmiot == 'matematyka':
      if isinstance(srednia44, str):
        print("Średnia: ","BRAK OCEN")
      else: 
        print("Średnia: ",srednia44)
      print("ECTS: ", ECTS4)
      print("Łączna liczba ECTS: ",ECTS1+ECTS2+ECTS3+ECTS4,"/ 20")
    
    if przedmiot != 'plastyka' and przedmiot != 'geografia' and przedmiot != 'fizyka' and przedmiot != 'matematyka':
      print("Podany przedmiot nie figuruje w bazie / błąd w pisowni")

  else:
    os.system('clear')
    print("Wybrano opcje spoza dostępnego przedzialu (1-4)")
      
 

