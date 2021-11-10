print('Умножение чисел')

a = float(input('Введите число A: '))
b = float(input('Введите число B: '))
print('Введите действие: \n1 - суммировать; \n2 - вычесть; \n3 - умножить; \n4 - разделить')
c = int(input())

if c == 1:
	print(a, '+', b, '=', a+b)
elif c == 2:
	print(a, '-', b, '=', a-b)
elif c == 3:
	print(a, '*', b, '=', a*b)
elif c == 4:
	print(a, '/', b, '=', a/b)
else:
	print('Такое действие недопустимо!')	

