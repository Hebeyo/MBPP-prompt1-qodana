def min_flip_to_make_string_alternate(str): 
	count1 = 0
	count2 = 0
	for i in range(len(str)): 
		if i % 2 == 0: 
			# count1 is for 01010101... 
			if str[i] == '1': 
				count1 += 1
			# count2 is for 10101010... 
			else: 
				count2 += 1
		else: 
			# count1 is for 10101010... 
			if str[i] == '0': 
				count1 += 1
			# count2 is for 01010101... 
			else: 
				count2 += 1
	return min(count1, count2)
