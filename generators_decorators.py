import time

# ЧАСТЬ 1

def odd_numbers_generator(start, end):
    """Генерирует нечетные числа в диапазоне от start до end."""
    for i in range(start, end + 1):
        if i % 2 != 0:
            yield i  

def exclude_range_generator(input_list, start, end):
    """Возвращает числа из списка, которые НЕ входят в диапазон [start, end]."""
    for item in input_list:
        if not (start <= item <= end): 
            yield item


# ЧАСТЬ 2

def draw_horizontal(symbol):
    """Рисует горизонтальную линию."""
    print(symbol * 20)

def draw_vertical(symbol):
    """Рисует вертикальную линию."""
    for _ in range(5):
        print(symbol)

def show_line(symbol, function_to_call):
    print(f"\n--- Рисуем линию символом '{symbol}' ---")
    function_to_call(symbol)


# ЧАСТЬ 3


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs) 
        end_time = time.time()   
        
        execution_time = end_time - start_time
        print(f"\n[Декоратор] Функция '{func.__name__}' выполнилась за {execution_time:.5f} сек")
        return result
    return wrapper

@measure_time
def get_evens_fixed():
    numbers = [x for x in range(0, 100001) if x % 2 == 0]
    return numbers

@measure_time
def get_evens_dynamic(start, end):
    numbers = [x for x in range(start, end + 1) if x % 2 == 0]
    return numbers


# БЛОК ПРОВЕРКИ

if __name__ == "__main__":
    
    print("--- Задание 1 (Нечетные 10-20) ---")
    for num in odd_numbers_generator(10, 20):
        print(num, end=" ")
    print("\n")


    print("--- Задание 2 (Исключить диапазон 5-15) ---")
    my_list = [1, 4, 6, 10, 12, 18, 20, 25]
    print(f"Исходный список: {my_list}")
    result = list(exclude_range_generator(my_list, 5, 15))
    print(f"Результат: {result}\n")

    print("--- Задание 3 (Линии) ---")
    show_line("*", draw_horizontal) 
    show_line("#", draw_vertical)

    print("\n--- Задание 4 (Замер времени 0-100000) ---")
    evens = get_evens_fixed()
    print(f"Получено чисел: {len(evens)}") 

    print("\n--- Задание 5 (Замер времени с параметрами) ---")
    evens_dyn = get_evens_dynamic(0, 2000000)
    print(f"Получено чисел: {len(evens_dyn)}")