import pyinputplus as pyinp

print('========================================')
print('============Sandwich Maker==============')
print('========================================')
print()

total_cost = 0

type_of_sandwich = pyinp.inputMenu(choices=['wheat', 'white', 'sourdough'], numbered=True,
                                   prompt="What type of Sandwich do you want?\n")
# Cost of sandwich type
match type_of_sandwich:
    case 'wheat':
        total_cost += 2
    case 'white':
        total_cost += 1
    case 'sourdough':
        total_cost += 3
    case _:
        total_cost = total_cost

type_of_protein = pyinp.inputMenu(choices=['chicken', 'turkey', 'ham', 'tofu'], numbered=True,
                                  prompt="What type of protein do you want?\n")
# cost of protein
match type_of_protein:
    case 'chicken':
        total_cost += 2
    case 'turkey':
        total_cost += 3
    case 'ham':
        total_cost += 2
    case 'tofu':
        total_cost += 3
    case _:
        total_cost = total_cost

cheese = pyinp.inputYesNo(prompt="Do you want Cheese?\n", yesVal="yes", noVal="no")
type_of_cheese = None
if cheese == "yes":
    type_of_cheese = pyinp.inputMenu(choices=['cheddar', 'Swiss', 'mozzarella'], numbered=True,
                                       prompt="What type of Cheese do you want?\n")
    # Cost of cheese
    match type_of_cheese:
        case 'cheddar':
            total_cost += 2
        case 'Swiss':
            total_cost += 4
        case 'mozzarella':
            total_cost += 3
        case _:
            total_cost = total_cost

mayo = pyinp.inputYesNo(prompt="Do you want Mayo?\n", yesVal="yes", noVal="no")
if mayo == 'yes':
    total_cost += 3

mustard = pyinp.inputYesNo(prompt="Do you want Mustard?\n", yesVal="yes", noVal="no")
if mustard == 'yes':
    total_cost += 2

lettuce = pyinp.inputYesNo(prompt="Do you want Lettuce?\n", yesVal="yes", noVal="no")
if lettuce == 'yes':
    total_cost += 2

tomato = pyinp.inputYesNo(prompt="Do you want Tomato?\n", yesVal="yes", noVal="no")
if tomato == 'yes':
    total_cost += 1

num_of_sandwiches = pyinp.inputInt(prompt="How many sandwiches do you want?\n", min=1)
if num_of_sandwiches > 1:
    total_cost = total_cost * num_of_sandwiches

print('========================================')
print(f"Total cost of you order: ${total_cost}")
print('========================================')
