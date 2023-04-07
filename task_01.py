# Найдите сумму цифр трехзначного числа.

# Метод математический
n= int(input("Введите число: ")) 
sum = 0
while n>0:
    sum = sum + n%10
    n = n //10
print (sum)

# Метод строчный
n= input("Ведите число: ")
i=0
s =0
while i<len(n):
    k= int (n[i])
    s += k
    i += 1
print (s)
