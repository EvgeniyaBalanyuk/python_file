import os
from pprint import pprint

if __name__ == '__main__':
    with open('recipes.txt', encoding='utf-8') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish_name = line.strip()
            ingredients_list = []
            ingredients_quantity = file_obj.readline()
            for item in range(int(ingredients_quantity)):
                ingredients_dict = {}
                ingredient_name, quantity, measure = file_obj.readline().split(' | ')
                ingredients_dict['ingredient_name'] = ingredient_name
                ingredients_dict['quantity'] = int(quantity)
                ingredients_dict['measure'] = measure.strip()
                ingredients_list.append(ingredients_dict)
            cook_book[dish_name] = ingredients_list
            file_obj.readline()


    def get_shop_list_by_dishes(dishes, person_count):
        shop_dict = {}
        for dish in dishes:
            if dish in cook_book.keys():
                for recipe in cook_book[dish]:
                    if recipe['ingredient_name'] in shop_dict:
                        shop_dict[recipe['ingredient_name']]['quantity'] += recipe['quantity'] * person_count
                    else:
                        shop_dict[recipe['ingredient_name']] = {'measure': recipe['measure'],
                                                                'quantity': (recipe['quantity'] * person_count)}
            else:
                return 'Блюда нет в кулинарной книге'
        return shop_dict


    pprint(cook_book, sort_dicts=False, width=100)
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), sort_dicts=False)