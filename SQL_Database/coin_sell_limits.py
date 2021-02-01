

def sell_limits(current_price):
	sell_limits_list  = list()
	first_sell_limit  = current_price + (current_price * 0.15) 
	second_sell_limit = current_price + (current_price * 0.30)  
	third_sell_limit  = current_price + (current_price * 0.45)
	fourth_sell_limit = current_price + (current_price * 0.60) 
	sell_limits_list  = [first_sell_limit, second_sell_limit, third_sell_limit, fourth_sell_limit]
    
	return sell_limits_list

def buy_limits(current_price):
	buy_limits_list  = list()
	first_buy_limit  = current_price - (current_price * 0.15)
	second_buy_limit = current_price - (current_price * 0.30)
	third_buy_limit  = current_price - (current_price * 0.45)
	fourth_buy_limit = current_price - (current_price * 0.60)
	buy_limits_list  = [first_buy_limit, second_buy_limit, third_buy_limit, fourth_buy_limit]

	return buy_limits_list

def main():
	while True:
		current_price = input("Please enter current_price('q' for quit): ")
		
		if(current_price == 'q'):
			break

		else:
			print("SELL LIMITS")
			i = j = 1
			for sell_limit in sell_limits(float(current_price)):
				print(str(i) + ". sell limit point: " + str(format(sell_limit,'.5f')))
				i += 1
			print("*"*20)
			print("BUY LIMITS")
			for buy_limit in buy_limits(float(current_price)):
				print(str(j) + ". buy limit point: " + str(format(buy_limit,'.5f')))
				j += 1
			print('*'*30)

main()