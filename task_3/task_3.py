import os
from colorama import Fore, Style

def directory(path):
    if not os.path.exists(path):
        print(f"Шлях '{path}' не існує.")

    # Рекурсія 
    for root, dirs, files in os.walk(path):
        current_dir = os.path.relpath(root, path)
        print(Fore.BLUE + Style.BRIGHT + f"Папка: {current_dir}")

        for file in files:
            print(Fore.LIGHTMAGENTA_EX + "<<<< " + Fore.YELLOW + Style.BRIGHT + 
                  f"Файл: {os.path.join(current_dir, file)} " + Fore.LIGHTMAGENTA_EX + ">>>>") 
        print('')  

if __name__ == '__main__':
    import sys

    path = sys.argv[1]
    directory(path)