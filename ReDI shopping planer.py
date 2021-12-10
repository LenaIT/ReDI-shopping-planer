# You have a cookbook and you want to plan what to cook next week. 
# You select a few recipes and the program automatically calculates what you need to buy and prints you the shopping list.
# All user inputs (Yes, No, Omelette, Bread, Carbonara, Pizza, Pancakes) must be written with a capitalised initial letter.

Cookbook = {'Omelette':['Eggs', 'Olive Oil', 'Salt'], 'Bread':['Flour','Salt','Yeast'],'Carbonara':['Pasta', 'Eggs', 'Cheese', 'Pork', 'Pepper'],
            'Pizza':['Flour', 'Salt', 'Yeast', 'Olive Oil', 'Tomatoes', 'Cheese', 'Onions', 'Olives'], 'Pancakes':['Eggs', 'Milk', 'Butter']}
all_ingredients = []
answer = 'Yes'
continue_to_choose = 'Yes'
print('Welcome! Do you want to cook something from the Cookbook?')
answer = input('Are you ready for a shopping tour? Yes or No? ')
if answer == 'Yes':
  while continue_to_choose == 'Yes':
    which_recipe = input('Which recipe do you prefer? Omelette, Bread, Carbonara, Pizza or Pancakes? ')
    if which_recipe in Cookbook:
      for ingredients in Cookbook[which_recipe]:
        all_ingredients.append(ingredients)
      continue_to_choose = input("Do you want to choose another recipe? ")
  print('Here is your shopping list!')
  print(all_ingredients)  
elif answer == 'No':
  print('We are sorry to hear that. Goodbye! See you next time! ')
