import time

# def squared_calculation(numbers):
# 	result = []
# 	start_time = time.time()

# 	for number in numbers:
# 		result.append(number ** 2)
# 	print("This function took about " + str(time.time() - start_time) + " second.")

# def cube_calculation(numbers):
# 	result = []
# 	start_time = time.time()
# 	for number in numbers:
# 		result.append(number ** 3)
# 	print("This function took about " + str(time.time() - start_time) + " second.")



# print(squared_calculation(range(100000)))
# print(cube_calculation(range(100000)))
# print(squared_calculation(range(100000)))


def time_calculation(myfunction):
	def wrapper(numbers):
		start_time = time.time()
		result = myfunction(numbers)
		finish_time = time.time()
		print(myfunction.__name__ + " " + str(finish_time - start_time) + " second.")
		#return result
	return wrapper


@time_calculation
def squared_calculation(numbers):
	result = []

	for number in numbers:
		result.append(number ** 2)
	return result

@time_calculation
def cube_calculation(numbers):
	result = []
	for number in numbers:
		result.append(number ** 3)
	return result




print(squared_calculation(range(100000)))
print(cube_calculation(range(100000)))
print(squared_calculation(range(100000)))
