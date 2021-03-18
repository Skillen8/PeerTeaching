from Pizza import Pizza


pizza_num = []

num_pizza= int(input("enter how many pizzas you want"))

for pizzas in range(num_pizza):
    size = input("enter the size of the pizza")
    topping = input("enter the topping of the pizza")
    pizza = Pizza(size, topping)
    pizza_num.append(pizzas)

for each_pizza in Pizza.pizza_num:
    each_pizza.display()

