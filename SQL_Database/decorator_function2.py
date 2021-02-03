


def extra(function):
	def wrapper(numbers):
		even_numbers_sum = 0
		even_numbers_count = 0 
		uneven_numbers_sum = 0
		uneven_numbers_count = 0

		for number in numbers:
			if (number % 2 == 0):
				even_numbers_sum += number
				even_numbers_count += 1
			else:
				uneven_numbers_sum += number
				uneven_numbers_count += 1

		print("Uneven numbers average: ",uneven_numbers_sum/even_numbers_count)
		print("Even numbers average: ", even_numbers_sum/even_numbers_count)

		function(numbers)
	return wrapper


@extra
def average_find(numbers):
	sum = 0

	for number in numbers:
		sum += number

	return sum

average_find([1,2,3,4,5,6,7,8])