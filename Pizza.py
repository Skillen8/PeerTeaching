# create a pizza class
class Pizza:
    pizza_num = []

    def __init__(self, topping, size):
        self._topping = topping
        self._size = size
        self.pizza_num.append(self)

    def set_size(self, size):
        self._size = size

    def get_size(self):
        return self._size

    def set_topping(self, topping):
        self._topping = topping

    def get_topping(self):
        return self._topping

    def display(self):
        print("Size: ", self._size, "Topping: ", self._topping)
