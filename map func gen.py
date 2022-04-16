def my_map(func, items):
    for item in items:
        print(eval(func(items[item])))


funct = str(input('Write the function '))
item_list = []
while len(item_list) < 10:
    item_list.append((input()))
my_map(funct, item_list)
