x = float(input("შეიტანეთ რიცხვი: "))

oper = input("აირჩიეთ ოპერაცია: +, -, /, *, ^ ")

y = float(input("შეიტანეთ რიცხვი: "))

if oper == "+":
	print(x + y)
elif oper == "-":
	print(x - y)
elif oper == "/":
	if y != 0:
		print(x / y)
elif oper == "*":
	print(x * y)		
elif oper == "^":
	print(x ** y)	
else:
	print("არჩეული ოპერაცია მცდარია, სცადეთ თავიდან.")
