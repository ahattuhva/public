a = [20, 2, 5, 0, 10, 5] #создаем список
g=1 #создаем переменную g, которая будет контролировать условие while
while g==1: #пока g равно 1, то условие выполняется
    for i in range(len(a)-1): #то в интервале длины списка а; [len(a)-1] нужно для того, чтобы сравнивать пары значений, без неё последнее значение не имело бы пары
        if (a[i]>a[i+1]): #если первое число больше чем второе
            a[i],a[i+1]=a[i+1],a[i] #первое число и второе менются местами
    print(a) #принтуем фильтрованный список 
    if all(a[i]<=a[i+1] for i in range(len(a)-1)) : # если первое число меньше или равно второму в интервале a (см. выше) - истина 
        g=2 # то g равно 2, то есть условие while прерывается
print(a) #принтуем конечный список
# ура
