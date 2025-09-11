import numpy as np

def task2_1():
    arr1 = np.array([0, 10, 20, 40, 60])
    arr2 = np.array([10, 30, 40])
    print("1. Дано два массива ... ")
    print(f"1й массив: {arr1}")
    print(f"2й массив: {arr2}")
    print(f"Пересекающиеся элементы: {np.intersect1d(arr1, arr2)}\n")

def task2_2():
    print(f"\n2. Оставляем только уникальные элементы.")
    arr = np.array([10, 10, 20, 20, 30, 30])
    print(f"Исходный массив: {arr}")
    print(f"Оставляем только уникальные эл-ы: {np.unique(arr)}")
    arr2 = np.array([[1, 1],
            [2, 3]])
    print(f"Исходный массив:\n{arr2}")
    print(f"Оставляем только уникальные эл-ы: {np.unique(arr2)}\n")
    
def task2_3():
    print(f"\n3. Уникальные элементы и их частоты.")
    arr = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])
    print(f"Исходный массив: {arr}")
    
    uniques, counts = np.unique(arr, return_counts=True)
    print(f"Элементы: {uniques},\nЧастоты: {counts}\n")

def task2_4():
    print(f"\n4. Получить массив путём повторения данного.")
    arr = np.array([1, 2, 3, 4])
    print(f"1 повторение:\n{np.tile(arr, 1)}")
    print(f"2 повторения:\n{np.tile(arr, 2)}")
    print(f"3 повторения:\n{np.tile(arr, 3)}\n")
    

def task2_5():
    arr = np.array([200., 300., np.nan, np.nan, np.nan, 700.])
    print(f"\n5. Почистить массив от nan.")
    print(f"Исходный массив: {arr}")
    print(f"Почистим: {arr[~np.isnan(arr)]}")
    
    arr2 = np.array([[1., 2., 3.],
              [np.nan, 0., np.nan],
              [6., 7., np.nan]])
    print(f"\n Для 2D массива:\n{arr2}")
    print(f"Почистим: {arr2[~np.isnan(arr2)]}\n")
    
def task2_6():
    arr = np.array([1., 7., 8., 2., 0.1, 3., 15., 2.5])
    print(f"\n6. Получить массив k наименьших значений.")
    print(f"Исходный массив: {arr}")
    print(f"Его 4 наименьших значения:\n{np.sort(arr)[:4]}\n")
    # т.е. сортируем по возрастанию и берём срез
    
def task2_7():
    arr = np.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49])
    target = 3.09066280756759
    index = np.abs(arr - target).argmin()
    print(f"\n7. Найти ближайший по значению к заданному числу элемент массива.")
    print(f"{arr[index]}\n")
    
def task2_8():
    arr1 = np.array(['Python', 'PHP'])
    arr2 = np.array(['Java', 'C ++'])
    print(f"\n8. Объединить два массива со строками поэлементным объединением.")
    print(f"1й массив: {arr1},\n2й массив:{arr2}")
    print(f"Объединим: {np.char.add(arr1 + ' ', arr2)}\n")

def task2_9():
    print(f"\n9. Получить массив с частой встречаемости буквы «P».")
    arr = np.array(['Python', 'PHP', 'JS', 'examples', 'html'])
    print(f"Частота встречаемости «P»: {np.char.count(arr, 'P')}\n")  

def task2_10():
    print(f"\n10. Найти корни полиномов.")
    print(f"Для a. x^2 - 4х + 7:\n{np.roots([1, -4, 7])}")
    print(f"Для b. x^4 - 11х^3 + 9х^2 + 11х - 10:\n{np.roots([1, -11, 9, 11, -10])}\n")
    
    
task2_1()
task2_2()
task2_3()
task2_4()
task2_5()
task2_6()
task2_7()
task2_8()
task2_9()
task2_10()