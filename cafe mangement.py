menu={
    'Pizza':140,
    'Pasta':100,
    'Burger':70,
    'Salad':40,
    'Sandwich':60,
    'Coffee':80,
}
print('Welcome to the Cafe')
print(f"Our Cafe Menu is:\n{'Pizza: Rs140\nPasta: Rs100\nBurger: Rs70\nSalad: Rs40\nSandwich: Rs60\nCoffee: Rs80'}")
order_total=0
while True:
    item = input("Enter the item you want to order:")
    if item in menu:
        order_total+=menu[item]
    else:
        print("sorry,we don't have that item on the menu")
    another_order= input("Do you want to add another item?(yes/n0):")
    if another_order!='yes':
        break
print(f"The total amount to pay is{order_total} Rs")
