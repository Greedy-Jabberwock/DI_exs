
# ============================= EXERCISE 3 : Restaurant Menu Manager =================================


print('Exercise 3 : Restaurant Menu Manager')


class MenuManager:
    def __init__(self):
        self.menu = []

    def add_item(self, name, price, spice, gluten):
        item = {"name": name,
                "price": price,
                "spice": spice,
                "gluten": gluten}
        self.menu.append(item)
        print(f'\n"{item["name"]}" added to the menu.\n')

    def update_item(self, name, price, spice, gluten):
        item = {"name": name,
                "price": price,
                "spice": spice,
                "gluten": gluten}
        for index, value in enumerate(self.menu):
            if name == value['name']:
                self.menu[index].update(item)
                print(f'\n"{name}" updated in the menu.')
                break
        else:
            print(f'\nThere is no "{name}" in the menu.\n')

    def remove_item(self, name):
        for index, value in enumerate(self.menu):
            if value['name'] == name:
                del self.menu[index]

    def print_menu(self):
        border = '-----------------------------------------------'
        menu = self.menu
        print(border)
        print('Here is the menu:\n')
        for dish in menu:
            values = [str(x) for x in dish.values()]
            print(' - '.join(values))
        print('''\nMeaning: For the spice level:
       • A = not spicy,
       • B = a little spicy,
       • C = very spicy''')
        print(border)


mm = MenuManager()
mm.add_item('jambalaya', 15, 'B', True)
mm.add_item('soup', 10, 'A', False)
mm.add_item('carry', 17, 'C', True)
mm.add_item('shrimps', 25, 'A', False)
mm.add_item('chili', 10, 'C', False)
mm.print_menu()
mm.update_item('carry', 15, 'B', True)
mm.update_item('shrims', 12, 'C', False)
mm.print_menu()
mm.remove_item('shrims')
mm.remove_item('shrimps')
mm.print_menu()
