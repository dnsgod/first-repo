for i in range(20):
	if i % 3 == 0 and i % 5 != 0:
		print("year")
	elif i % 5 == 0 and i % 3 != 0:
		print("dream")
	if i % 3 == 0 and i % 5 == 0:
		print("yeardream")
	else:
		print(i)

