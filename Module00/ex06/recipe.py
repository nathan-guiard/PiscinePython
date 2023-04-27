sandwich = {
	'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
	'meal': 'lunch',
	'prep_time': 10,
}

cake = {
	'ingredients': ['flour', 'sugar', 'eggs'],
	'meal': 'dessert',
	'prep_time': 60,
}

salad = {
	'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
	'meal': 'lunch',
	'prep_time': 15,
}

cookbook = {
	'sandwich': sandwich,
	'cake': cake,
	'salad': salad,
}

def print_recipe_names():
	for key, x in cookbook.items():
		print(key)

def print_recipe_details(name):
	try:
		recipe = cookbook[name]
	except Exception as e:
		return e
	
	print(name, ":", recipe['meal'])
	print('Preparation time:', recipe['prep_time'])
	print("Ingredients:")
	for x in recipe['ingredients']:
		print("-", x)

def delete_recipe(name):
	try:
		cookbook.pop(name)
	except KeyError:
		print(name, "is not a current recipe")

def add_recipe():
	ingredients = []
	name = str(input("Enter a name:\n"))

	print("Enter ingredients:")
	while 1:
		input_ingredients = str(input())
		if input_ingredients == '':
			break
		ingredients.append(input_ingredients)
	
	type = str(input("Enter a meal type:\n"))
	time = str(input("Enter a preparation time:\n"))

	cookbook[name] = {
		'ingredients': ingredients,
		'meal': type,
		'prep_time': time,
	}

def help():
	print('Here are you options:')
	print('1: Add a recipe')
	print('2: Delete a recipe')
	print('3: Print a recipe')
	print('4: Print the Cookbook')
	print('5: Quit')
	print('6: Help')

if __name__ == '__main__':
	print('Welcome to the Cookbook!')
	help()

	while 1:
		try:
			option = int(input('Please select an option:\n'))
		except ValueError:
			print('Invalid option, must be 1 to 6')
			continue
		match option:
			case 1:
				add_recipe()
			case 2:
				delete_recipe(str(input("What recipe to delete?\n"))) 
			case 3:
				print_recipe_details(str(input("What recipe to print?\n")))
			case 4:
				print_recipe_names()
			case 5:
				print('Goodbye :)')
				exit()
			case 6:
				help()
			case _:
				print('Invalid option, must be 1 to 6')
