import numpy as np

def task1_1():
    arr = np.array([1, 7, 13, 105])
    
    allocated_mem = arr.nbytes
    print(f"1. Занимаемая массивом память: {allocated_mem} байт.")
    
    np.savetxt('txt_array.txt', arr, fmt='%d')
    np.save('bin_array.npy', arr)
    
    print(f"Загрузим массив из текстового файла, вывод на экран: ")
    txt_arr = np.loadtxt('txt_array.txt', dtype=int)
    # требуется уточнение типа данных т.к. по умолчанию читает любые как 
    # числа с плавающей точкой
    print(f"{txt_arr}\n")
    
    print(f"Загрузим массив из бинарного файла, вывод на экран: ")
    bin_arr = np.load('bin_array.npy')
    print(f"{bin_arr}")
    
def task1_2():
    print(f"\n2. Массив нулей: {np.zeros(10, dtype=int)}")
    print(f"Массив единиц: {np.ones(10, dtype=int)}")
    print(f"Массив пятёрок: {np.full(10, 5, dtype=int)}")
    
def task1_3():
    print(f"\n3. Массив чётных [30; 70]:")
    print(f"{np.arange(30, 70+1, 2, dtype=int)}")
    
def task1_4():
    print(f"\n4. Массив равномер. распр. значений между 5 и 50:")
    print(f"{np.linspace(5, 50, 10, dtype=int)}")

def task1_5():
    print(f"\n5. Массив 3х3х3 из 27 случайных чисел в диапазоне [1; 100]:")
    print(f"{np.random.randint(1, 100+1, size=(3, 3, 3))}")

def task1_6():
    print(f"\n6. Массив 3х4 со значениями в [30; 41]:")
    distributed_arr = np.arange(30, 41+1, 1, dtype=int)
    resized_arr = distributed_arr.reshape(3, 4)
    print(resized_arr)

def task1_7():
    arr = np.zeros((10, 10), dtype=int)
    arr[0, :] = 1
    arr[-1, :] = 1
    arr[:, 0] = 1
    arr[:, -1] = 1
    print(f"\n7. Массив 10х10 из нулей с граничными 1:")
    print(arr)
    
def task1_8():
    arr = np.zeros((5, 5), dtype=int)
    for i in range(5):
        arr[i, i] = i + 1
    print(f"\n8. Массив 5х5 из 0 с глав. диаг = [1, 2, 3, 4, 5]:")
    print(arr)

def task1_9():
    print(f"\n9. Массив 4х4, 0 и 1 в шахматном порядке:")
    arr = np.zeros((4, 4), dtype=int)
    for i in range(4):
        for j in range(4):
            if (i+j) % 2 != 0:
                arr[i, j] = 1
    print(arr)

def task1_10():
    march_2017 = np.arange('2017-03-01', '2017-04-01', dtype='datetime64[D]')
    print(f"\nВсе дни марта 2017:")
    print(march_2017)

task1_1()
task1_2()
task1_3()
task1_4()
task1_5()
task1_6()
task1_7()
task1_8()
task1_9()
task1_10()