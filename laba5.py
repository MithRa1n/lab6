class Flower:
    """
    Represents a flower.
    """
    def __init__(self, name, height, size, color, price, quantity, deliveryrate):
        """
        Initializes a flower object.
        """
        if price < 0:
            raise ValueError("Flower price cannot be negative.")
        self.name = name
        self.height = height
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.deliveryrate = deliveryrate

    def __lt__(self, other):
        """
        Compares flowers based on price.
        """
        return self.price < other.price
    
    def __str__(self):
        """
        String representation of a flower.
        """
        return f"Flower - {self.name}, price - {self.price}, quantity - {self.quantity} " 

class FlowerShop:
    """
    Class containing flowers.
    """
    def __init__(self):
        """
        Initializes list of flowers
        """
        self.flower_shop_inventory = []

    def add_shop_flower(self, *args):
        """
        Adds flowers to the shop.
        """
        self.flower_shop_inventory.extend(args)

    def remove_shop_flower(self, flower):
        """
        Removes flowers from the shop.
        """
        if flower in self.flower_shop_inventory:
            self.flower_shop_inventory.remove(flower)
        else:
            raise ValueError("Flower isn't in the shop")
        
    def get_most_expensive_flowers(self):
        """
        Gets ordered list of the most expensive flowers in the shop.
        """
        return sorted(self.flower_shop_inventory, reverse=True, key=lambda x: x.price) 
    
    def __str__(self):
        """
        String representation of the flower shop.
        """
        result = "All flowers in Flower World:\n"
        for _ in self.flower_shop_inventory:
            result += str(_) + "\n"
        return result

class Bouquet:
    """
    Class which contains flowers and combine them into bouquet.
    """
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower, quantity):
        """
        Adds flowers to the bouquet.
        """
        self.flowers.extend([flower] * quantity)

    def get_total_cost(self):
        """
        Calculates the total cost of the bouquet.
        """
        total_price = sum(flower.price for flower in self.flowers)
        return f"Total cost of the bouquet - {total_price} UAH"
    
if __name__ == "__main__":
    rose = Flower("Rose", 30, "medium", "red", 225, 20, 2)
    tulip = Flower("Tulip", 25, "small", "yellow", 133, 30, 1)
    lily = Flower("Lily", 40, "large", "white", 127, 15, 5)
    daisy = Flower("Daisy", 18, "small", "white", 2500, 25, 1)

    Flower_World = FlowerShop()
    Flower_World.add_shop_flower(lily, rose ,tulip)
    print(Flower_World)

    bouquet1 = Bouquet()
    bouquet1.add_flower(tulip, 5)
    bouquet1.add_flower(lily, 3)
    print(bouquet1.get_total_cost())

    expensive_flowers = Flower_World.get_most_expensive_flowers()
    print("Most expensive flowers in shop:")
    for flower in expensive_flowers:
        print(f"{flower.name} , Ціна: {flower.price} грн")
