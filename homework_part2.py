# ЧАСТЬ 2 

def fibonacci_generator(start, end):
    a, b = 0, 1
    while a <= end:
        if a >= start:
            yield a
        a, b = b, a + b

def sum_lists_generator(list1, list2):
    max_len = max(len(list1), len(list2))
    
    for i in range(max_len):
        val1 = list1[i] if i < len(list1) else 0
        val2 = list2[i] if i < len(list2) else 0
        
        yield val1 + val2


def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def calculate(list_to_work, function_to_call):
    results = []
    for item in list_to_work:
        results.append(function_to_call(item))
    return results


def report_simple_format(func):
    def wrapper(*args, **kwargs):
        print("\n--- Простой отчет ---")
        result = func(*args, **kwargs)
        print(f"Итого: {result}")
        print("---------------------")
        return result
    return wrapper

def report_official_format(func):
    def wrapper(*args, **kwargs):
        print("\n*** ОФИЦИАЛЬНЫЙ ГОСУДАРСТВЕННЫЙ ОТЧЕТ ***")
        result = func(*args, **kwargs)
        print(f"СУММА К УПЛАТЕ: {result} UAH")
        print("Подпись: _________________")
        return result
    return wrapper

@report_simple_format
def get_report_simple(revenue, expenses):
    return revenue - expenses

@report_official_format
def get_report_official(revenue, expenses):
    return revenue - expenses


# === ПРОВЕРКА ===
if __name__ == "__main__":
    
    print(">>> ЗАДАНИЕ 1 (Фибоначчи 5-100)")
    print(list(fibonacci_generator(5, 100)))

    print("\n>>> ЗАДАНИЕ 2 (Сумма списков)")
    l1 = [1, 2, 3]
    l2 = [4, 5, 6, 7, 8] 
    print(f"Список 1: {l1}")
    print(f"Список 2: {l2}")
    print(f"Сумма:    {list(sum_lists_generator(l1, l2))}")

    print("\n>>> ЗАДАНИЕ 3 (Квадраты и кубы)")
    nums = [2, 3, 4]
    print(f"Квадраты: {calculate(nums, square)}")
    print(f"Кубы:     {calculate(nums, cube)}")

    print("\n>>> ЗАДАНИЕ 4 (Отчеты)")
    get_report_simple(1000, 300)
    get_report_official(1000, 300)