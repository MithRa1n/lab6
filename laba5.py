class Flower:

    def __init__(self, name, height, size, color, price, quantity, deliveryrate):
        if price < 0:
            raise ValueError("Ціна квітки не може бути від'ємною.")
        self.name = name
        self.height = height
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.deliveryrate = deliveryrate

    def __lt__(self, other):
        return self.price < other.price
    
    def __str__(self):
        return f"Параметри квітки: Назва - {self.name}, Висота - {self.height} см, Розмір - {self.size}, Колір - {self.color}, Ціна - {self.price} грн, Кількість {self.quantity} шт, Рейтинг доставки - {self.deliveryrate}." 
class FlowerShop:
    def __init__(self):
        self.flower_shop_inventory = []

    def add_shop_flower(self, *args):
        self.flower_shop_inventory.extend(args)

    def remove_shop_flower(self, flower):
        if flower in self.flower_shop_inventory:
            self.flower_shop_inventory.remove(flower)
        else:
            raise ValueError("Квітка відсутня в магазині")
        
    def get_most_expensive_flowers(self, flowers_amount):
        most_expensive_flowers = [] 
        inventory_copy = list(self.flower_shop_inventory)
        for _ in range(flowers_amount):
            if not inventory_copy:
               break
            max_flower = max(inventory_copy)
            most_expensive_flowers.append(max_flower)
            inventory_copy.remove(max_flower)
        return most_expensive_flowers    
    def __str__(self):
        result = "Bci квіти в магазині Flower World:\n"
        for _ in self.flower_shop_inventory:
            result += str(_) + "\n"
        return result
class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower, quantity):
        self.flowers.extend([flower] * quantity)

    def get_total_cost(self):
        total_price = sum(flower.price for flower in self.flowers)
        return f"Загальна ціна букету - {total_price} грн"
    
if __name__ == "__main__":
    rose = Flower("Троянда", 30, "середній", "червоний", 225, 20, 2)
    tulip = Flower("Тюльпан", 25, "маленький", "жовтий", 133, 30, 1)
    lily = Flower("Лілія", 40, "великий", "білий", 127, 15, 5)
    daisy = Flower("Ромашка", 18, "маленький", "білий", 2500, 25, 1)
    Flower_World = FlowerShop()
    Flower_World.add_shop_flower(lily, rose ,tulip)
    print(Flower_World)
    bouquet1 = Bouquet()
    bouquet1.add_flower(tulip, 5)
    bouquet1.add_flower(lily, 3)
    print(bouquet1.get_total_cost())
    expensive_flowers = Flower_World.get_most_expensive_flowers(99)
    print("Найдорожчі квіти в магазині:")
    for flower in expensive_flowers:
        print(f"{flower.name} , Ціна: {flower.price} грн")
