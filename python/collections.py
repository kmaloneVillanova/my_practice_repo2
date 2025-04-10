# lists
cart=["apples","bananas","cherries","cherries"]
print(cart)

cart.append("dounuts")
cart.append("eggs")
cart.append("flour")
print(cart)

cart.remove("cherries")
print(cart)
if "pineapple" in cart:
    cart.remove("pineapple")

cart.pop(3)
print(cart)
cart.pop()
print(cart)

cart.reverse()
print(cart)
cart.sort()
print(cart)

cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

fruit_basket=cart[4:]
print(cart)
print(fruit_basket)

squares=[]
for i in range(1,10):
    squares.append(i*i)
print(squares)

squares=[i*i for i in range(1,10)]
print(squares)

b_items=[item for item in cart if item.startswith("b")]
print(b_items)

inventory=[0]*len(cart)
print(inventory)
inventory[0]=100

# sets
number_set=set()
number_set={1,1,2,3,4,0,10,5}
print(number_set)
number_set.add(-10)
print(number_set)

num_lst=[1,1,4,5,5,6,6]
no_dups=set(num_lst)
print(no_dups)
no_dups=list(no_dups)
print(no_dups)

ns=sorted(number_set)
print(ns)

#dictionary
fav_snacks={}
fav_snacks={
    "kathleen":"tortilla chips",
    "maggie":"pretzels",
    "emily":"buffalo chicken dip",
    "ava":"chocolate"
}
print(fav_snacks)
fav_snacks["wade"]="popcorn"
print(fav_snacks)

print("kathleen's favorite snack is "+fav_snacks["kathleen"])
if "bob" in fav_snacks:
    print("bob's favorite snack is "+fav_snacks["bob"])

for key in fav_snacks:
    print(key+"'s favorit food is "+fav_snacks[key])
    print(f"{key}'s favorite food is {fav_snacks[key]}")

for key,value in fav_snacks.items():
    print(key,value)

keys=fav_snacks.keys()
values=fav_snacks.values()

fav_snacks["alice"]=["chips","nuts"]
print(fav_snacks)