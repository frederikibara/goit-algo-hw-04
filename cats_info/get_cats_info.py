from pathlib import Path

def get_cats_info(path) -> list[dict()]:
    """
    Function read file, converts each line into a dictionary. 
    Return -> list of dictionaries
    """
    cats_list = []
    
    try:
        with open (path, encoding= 'utf-8') as file:
            for cat in file:
                value = cat.strip().split(',')               
                cats_dict = {
                'id'   : value[0],
                'name' : value[1],
                'age'  : value[2],
                }
                cats_list.append(cats_dict)                       
            return cats_list
        
    except FileNotFoundError:
        print('Файл не існує!')


cat_info = get_cats_info('cats_info\cats.txt')
print(cat_info)


