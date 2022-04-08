# Типы данных в python
# Immutable: str, num, frozenset, bool, None, tuple
# Mutable: list, set, dict

                    # """Numbers"""
# Numbers предназначены для хранения числовых значений и проведения арифметических вычислений над ними
# numbers: int, float, decimal, complex, long
# """int float"""
# abs(int), abs(float) - vozvrawaet modul chislat, floa
# pow(num, degree, remainder)
# divmod(num1, num2) - (num1//num2),(num1%num2)

                    #  """Strings"""
# str - uporyadichennaya posledovatelnost simvolov v odinarnyh ili 2h kavychkah
# Sintax: "", '', """"""", '''''' """
# "hello" * 3 -> "hellohellohello"
# index - numeraciya simvolov v stroke v uporyadochennoi posledovatelnosti
# "h e l l o   w o r l d "
#  0 1 2 3 4 5 6 7 8 9 10
#                   -2 -1
# srezy - chast stroki, podstroka   start<end
# string = 'some string'
# string[index]
# string[start, end, step]

                    # """Bool"""
# logicheskii tip dannyh s dvumya znacheniyami: True False

                    # """List"""
# izm, uporyad tip danny, kotoryi hranit posledovatelnost elementov. Elementami spiska mogut byt' absolyutno lyubye tipy dannyh, v tom chisle i spiski.
# list1 = [1, "str", 3.4, (7, 2), ["str", 6]]
# list2 = list(1, "str", 3.4, (7, 2), ["str", 6])
# list3 = ["str"]*6 -> ["str", "str","str","str","str","str"]
# list4 = list(range())
# range(start, end, step) - funkciya, kotoraya sozdaet posledovztelnost chisel
# list(range(5)) -> [0, ], 2, 3, 4]
# list(range(2, 8)) -> [2, 3, 4, 5, 6, 7]
# list(range(4,8, 2)) -> [4,6]
# len(obj) - vozvr dlinu obj


                    # """Tuple"""
# kortej - neizm uporyad tip dannyh, kotoryi predastavlyaet soboi posledovatelnost elementov. Elementami tuple mogut byt' absolyutno lyubye tipy dannyh, v tom chisle i spiski, i korteji.
# (1, 2, 3)         1, 2, 3         (3,)
                    # """Set"""
# izm neuporyad tip dannyh, kotoryi hranit v sebe tolko unikalnye, neizm znacheniya
# set(iterable)
# {True, False, 2, 0, None, ()}

                    # """Frozenset"""
# neizm mnojetsvo - neizm neuporyad tip dannyh, kotoryi hranit v sebe tolko unikalnye, neizm znacheniya
# syntax: frozenset(iterable)

                    # """Dict"""
# dict - izm, neuporyad tip dannyh, v kotorom hranyatsya pary v vide key:value. Klyuch v slovare - lyuboi neiz tip dannyh. Kajdyi klyuch - unikalnyi. Value - lyuboi tip dannyh
# Syntax: {"key":"value", 5: ["hello"]}     dict(iterable)

                    # """None"""
# neiz tip dannyh, kotoryi ispolzuetsya dlya oboznacheniya pustogo ili otsutstviya znacheniya






                    # """Conditions"""
# usloviya - operator, kotoryi pozvolyaet nam vypolnyat ili ne vypolnyat kakoi-to kusochek koda, kotoryi nahoditsya v tele usloviya
# Synax:

# if True:
#     print("Vse verno")

# Takje my mojem sozdavat konstrukcii iz uslovnyh operatorov. Esli v pervom if uslovie vydalo True, to vypolnitsya eto uslovie. Esli v pervom if vyidet False, proveritsya telo v elif.
# Esli vtoroe elif uslovie vydalo False, to vypolnitsya else

# if i else v kostrukcii mojet byt ispolzovano 1 raz, elif mnogo.
# 

                    # """Ternarnye usloviya"""
# usloviya v odnu stroku
# telo1 if uslovie else telo2
# print("usl vernoe") if True else print("neverno")


                    # """Loops"""
# blok koda, kotoryi budet vypolnyatsya neskolko raz. Kajdyi krug cikla - iteraciya.

# break - insrtukciya, kotoraya nemedlenno preryvaet rabotu cikla.
# continue - instrukciya, kotoraya perehodir k sleduyushei iteracii

# '''For'''
# eto cikl, kotoryi proizvodit iteraciyu nad posledovatel'nost'yu(list, dict, set, str, tuple)
# v cikle for my mojem vypolnyat razlichnye operacii nad kajdym elementom posledovatelnosti.
# Syntax:
# for element in posledovatelnost:
#     kakie-to deistviya


# '''while'''
# while - cikl, kotoryi proizvodit deistviya, poka usloviye budet True
# Syntax:
# while uslovie:
#     kakie-to deistviya


# '''Comprehension'''
# generatory posledovatelnosti - spec konstrukciya, s pomoshyu kotoroi mojno sozdavat posledovatelnosti.
# Syntax:
# # deistvie for element in posledovatelnost' if uslovie
# [x for x in range(1,11) if x%2==0]
# ["chetnoe" if x%2==0 else "nechetnoe" for x in range(1, 11)]


# dlya dict compehension v deistvii doljna byt' para (klyuch:znachenie)
# {x:x**2 for x in range(1,11) if x%2==0}

# init_dict = {"key":"value", "key2":"value2"}
# res = {v:k for k, v in init_dict.items()}


                    # """Try-except"""
# konstrukciya dlya obrabotki isklyuchenii i oshibok
# Syntax Error ne obrabatyvaetsya
# Syntax:


# try:
#     kod, kotoryi mojet vu=yzvat oshibku
# except Isklyuchenie:
#     kod, kotoryi rabitaet, esli oshibka vyshla.
# else:
#     kod, kotoryi rabitaet, esli oshibka ne vyshla
# finally:
#     kod, kotoryi rabotaet v lyubom sluchae


                    # """Funkcii"""

# funkciya - imenovannyi blok koda, vypolnyayushii deistviya i vozvr rezultat. My mojem vyzyvat' funkciyu, obrashayas' k nei po imeni i ispolzuya ().
# kod, kotoryi napisan vnutri funkcii, budet rabotat' tolko pri vyzove fukcii.
# Parametry funkcii - eto lokalnye peremennye, kotorym prisvaivaetsya znachenie pri vyzove funkcii.
# Argumenty funkcii - eto znacheniya, kotoryi my peredaem v parametry funkcii.
# def - instrukciya, s pomoshyu kotoroi opredelyaetsta funkciya.
# return - funkciya, s pomoshyu kotoroi funkciya vozvrawet rezultat. Esli ee ne propisat'. vozvrawaet None po defaultu.

# pozicionnye, imenovannye, param s Defaultom, neobyaz args*, klyuchevye aargs**

# def func(poz, s default, *.**). args - tuple, kwargs - dict.
# func(poz, neobyaz arg, param = znach, klyuch = znach)
# def func(a, b, c, * args)

    # '''Vstroennye funkcii'''
# map(int; ["1", "2"])
# Syntax:
# list_ = ["1", "2", "3", "4", "5"]
# print([int(x) for x in list_])
# print(list(map(int, list_)))

# def my_func(elem):
#     return elem.upper()
# map(my_func, ["hello", "world"])

# '''filter''' - funkciya, kotoraya vozvrawaet posledovatelnost iz elementov, sootvetstvuyushih usloviyu. priimaet 2 args: 1 - funkciya, kotoraya vozvr bulevoe znachenie i prinimaet 1 arg, 2 - posled
# Syntax:
# def myfunc(elem):
#     return elem.isalpha()

# print(list(filter(myfunc, ['1', '2', '3', 'd', 't'])))

# def myfunc(elem):
#     if elem>0:
#         return True
#     else:
#         return False
# filter(myfunc, [-1, 4, -6, 0, 8, 30, -2])


# zip - eto funkciya, kotoraya ob'edinyaet elementy iz neskolkih posledovatelnostei po indexam v tuple, t.e. vse elementy pod indexom 0 v pervyi tuple,
# vse elementy pod indexom 1 vo vtoroi tuple

# list1 = [1, 2, 3, 4, 5]
# list2 = ["a", "b", "c", "d"]
# print(list(zip(list1, list2)))


# reduce - funkciya, kotoruyu nujno importirovat' iz biblioteki functools: from functools import reduce. Ona prinimaet 2 obekta:1. funckiya, kototaya prinimaet 2 args i 2.posledovatelnost
# funkciya reduce beret iz posledovatelnosti 2 elementa, otpravlyaet ih v funckiyu. Rezultat i sled element iz posledovatelnosti snova otpravlyaet v funkciyu i t.d.

# Syntax:
# from functools import reduce

# def myfunc(x,y):
#     return x if len(x)>= len(y) else y

# reduce(myfunc, ["Hello", "world", "ochen dlinnaya stroka", "MAkers"])


# """Lambda""" - anonimnaya funkciya
# Syntax:
# lambda peremennaya: deistvie
# my_func = lambda x:x**2
# print(my_func(5))

# import functools 
# list_ = [1, 2, 3, 4]  
# result = functools.reduce(lambda x, y: x+y, list_)
# print(result)


