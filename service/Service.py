from HW7.model.vending_machine.VendingMachine import VendingMachine
from HW7.model.products.BottleOfWater import BottleOfWater
from HW7.model.products.HotDrinks import HotDrinks
from HW7.UI.UIConsole import UIConsole


class Service:

    def start(self):
        console = UIConsole()
        list_hot_drinks = [HotDrinks('Coffee', 200, 0.3, 80),
                           HotDrinks('Tea', 100, 0.4, 70),
                           HotDrinks('Milk', 300, 1.0, 65)]
        list_bottle_of_water = [BottleOfWater('Cola', 300, 0.5),
                                BottleOfWater('Sprite', 350, 0.45),
                                BottleOfWater('Fanta', 320, 0.43)]
        vending_machine1 = VendingMachine()
        vending_machine2 = VendingMachine()
        console.print_message('-----���� ������� �������� �������� � �������� �������-----')
        vending_machine1.list_products = list_hot_drinks
        console.print_list_product(vending_machine1.list_products)
        console.print_message('-----���� �������������� �������� �������� � �������� �������-----')
        vending_machine2.list_products = list_bottle_of_water
        console.print_list_product(vending_machine2.list_products)
        console.print_message('-----� ������� ������� ��������� �����-----')
        vending_machine1.add_at_list(HotDrinks('�����', 250, 0.5, 70))
        console.print_list_product(vending_machine1.list_products)
        console.print_message('-----� �������������� ������� ��������� ���������-----')
        vending_machine2.add_at_list(BottleOfWater('���������', 150, 0.5))
        console.print_list_product(vending_machine2.list_products)
        console.print_message('-----��������� Tea �� ��������� ��������-----')
        console.print_message(vending_machine1.get_product('Tea'))
        console.print_message('-----��������� Sprite �� ��������� ��������-----')
        console.print_message(vending_machine2.get_product('Sprite'))