def checkKey(dic, key):
	if key in dic.keys():
		print("Present, ", end =" ")
		print("value =", dic[key])
	else:
		print("Not present")
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)

key = 'w'
checkKey(dic, key)
