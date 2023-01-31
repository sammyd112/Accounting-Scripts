"""Print out all the melons in our inventory."""


from melons import  melons_dic


def print_melon(name):
    print(name)
    for characteristics, values in melons_dic[name].items():
        print(characteristics, values)

print_melon('Casaba')

