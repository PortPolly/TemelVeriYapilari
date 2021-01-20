"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c

Deltayı Hesaplama:  b ** 2 -  4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök :  (-b - delta ** 0.5) / (2*a)

"""

a = int(input("Denklemin a Değeri : "))

b = int(input("Denklemin b Değeri : "))

c = int(input("Denklemin c Değeri : "))

delta  = b ** 2 - 4  * a * c

x1 =   (-b - delta ** 0.5) / (2*a)

x2 =   (-b - delta ** 0.5) / (2*a)

print("Birinci Kök : {}\nİkinc Kök : {}\n.".format(x1,x2))