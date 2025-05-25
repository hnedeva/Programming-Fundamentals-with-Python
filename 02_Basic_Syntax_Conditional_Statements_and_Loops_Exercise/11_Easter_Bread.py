my_budget = float(input())
flour_price = float(input())

egg_price = flour_price * 0.75
milk_price_per_liter = flour_price * 1.25
milk_for_bread = milk_price_per_liter / 4

bread = flour_price + egg_price + milk_for_bread

loaves = 0
colored_eggs = 0

while my_budget >= bread:
    loaves += 1
    my_budget -= bread
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {my_budget:.2f}BGN left.")
