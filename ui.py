from logger import input_data, print_data

def interface():
    print("Добрый день. ""Это телефонный справочник, разработка DonIgnasio") 
    \n 1 - запись данных  \n 2 - вывод данных")
    command = int(input("Введите число: "))

    while command != 1 and command != 2 :
        print("Вы ввели неверное число!")
        command = int(input("Введите число: "))

    if command == 1:
        input_data()

    elif command == 2:
        print_data()







interface()
