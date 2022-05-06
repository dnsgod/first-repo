for i in range(1,21):
	if i % 3 == 0 and i % 5 != 0:
		print("year")
	elif i % 5 == 0 and i % 3 != 0:
		print("dream")
	elif i % 3 == 0 and i % 5 == 0:
		print("yeardream")
	else:
		print(i)

