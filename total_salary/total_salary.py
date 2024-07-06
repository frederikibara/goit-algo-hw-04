from pathlib import Path

def total_salary(path) -> tuple:
    """
    Function takes a file path. Extracts only digits, sums them up, 
    calculate average(convert to int). Return -> tuple: of two values."
    """
    numbers = []
    
    try:    
        with open(path, encoding='utf-8') as file:
            for char in file:
                char = char.split(',')
                numbers.append(int(char[1]))         
                   
            total = sum(numbers)
            average = int(total / len(numbers))
            return total, average                    

    except FileNotFoundError:
        return f'Файл не існує!'
    

total, average = total_salary('total_salary\salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")