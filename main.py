podstroka=input("Введите строку ")#пользователь вводит строку
kolstr=0#говорим что количество всех строк ,содержащих искомую подстроку=0
stroki=[]#говорим что список всех строк, которые содержат искомую подстроку пуст 
with open("text.txt","r",encoding="utf-8")as file:#открываем файл и говорим что будем читать его 
    alltext=file.readlines()#считываем и записываем результат в переменную
for line in alltext:#перебираем каждую линию в тексте
    if podstroka in line:#проверяем условие
        kolstr=+1#если условие верное прибавляем к количеству всех строк ,содержащих искомую подстроку 1
        stroki.append(line.strip())#если условие верное добавляем к списку строку без первого и последнего пробелов удовлетворяющюю условию 
sortedlines=sorted(stroki,key=len)#отсортировываем все строки в порядке возростания по длине строки
print("Все строки, которые содержат искомую подстроку: ")#выводим все строки, которые содержат искомую подстроку
for line in stroki:#перебираем каждую строку в списке
    print(line)#выводим каждую строку
print(f"Количество всех строк ,содержащих искомую подстроку: {kolstr}")#выводим количество всех строк ,содержащих искомую подстроку
print(f"Отсортированные строки в порядке их длины : {sortedlines}")#выводим отсортированные строки в порядке их длины