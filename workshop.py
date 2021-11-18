print("step0:")

print("success")

print("step1.0:")

fruit = "banana"
quantity = 3
pie_crust = "empty"
isOvenOn = False

print(f"You have {quantity} {fruit} and the pie crust is {pie_crust}, is the oven on? {isOvenOn}")

print("step1.1:")

fruit = "apple"
quantity = 5
pie_crust = "empty"
isOvenOn = True

print(f"You have {quantity} {fruit} and the pie crust is {pie_crust}, is the oven on? {isOvenOn}")

print("step1.2:")

def print_hello_please() :
    print("Hello")

print_hello_please()

def print_hello_with_my_name_please(myName) :
    print("Hello", myName)

print_hello_with_my_name_please("Sébastien")

def calc_my_age_in_two_years(myCurrentAge) :
    my_age_in_two_years = myCurrentAge + 2
    return my_age_in_two_years

my_age_in_two_years = calc_my_age_in_two_years(18)

print (f"In two years I'll be {my_age_in_two_years} years old")

print("step1.2.1")

def prepMyFruit(quantity, fruit, pie_crust) :
    print(f"You put {quantity} {fruit} on the crust")
    pie_crust = "filled with delicious " + fruit
    return pie_crust

pie_crust = prepMyFruit(3, "apple", "empty")
print("my pie is", pie_crust)

print("step 1.2.2")

def turn_on_oven(isOvenOn) :
    isOvenOn = True
    return isOvenOn

pie_crust = prepMyFruit(3, "apple", "empty")
is_oven_on = turn_on_oven(isOvenOn)
print("my pie is", pie_crust)
print("Is the oven turned on ?", isOvenOn)

def cookDaPie(pie_crust) :
    print(f"Your pie {pie_crust} is cooked, Bon appetit")
cookDaPie(pie_crust)

print("step2")

def dice_roll_res(dice_value1, dice_value2) :
    if dice_value1 == dice_value2:
        return ("Same value, play again")
    if dice_value1 == 1 or dice_value2 == 1 :
        return ("too bad you lose")
    elif dice_value1 % 2 == 0 and dice_value2 % 2 != 0 :
        return ("You win")
    else:
        return ("Nothing happen...")

print(dice_roll_res(1 ,3))
print(dice_roll_res(3 ,3))
print(dice_roll_res(6 ,3))
print(dice_roll_res(7 ,3))

def ask_me_about_string(string) :
    if string[0] == 'a' :
        return ("That's an A")
    if len(string) < 5 :
        return ("error, need longer string")
    if string[0] == string[]  :
        return "They are the same O_O"

print(ask_me_about_string("alla"))



