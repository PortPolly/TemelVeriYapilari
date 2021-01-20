print('''
Vücut Kitle İndeksi Hesaplayıcı
Boyunuzu ve Kilonuzu giriniz ve sonucunuzu alınız.
Boyunuzu m(metre cinsinden), kilonuzu kg(kilogram cinsinden) giriniz.
''')

print("Vücut Kitle İndeksi Hesaplayıcı")

boy = float(input("Boyunuzu giriniz : "))

kilo = int(input("Kilonuzu giriniz : "))

Vücut_Kitle_İndeksi = kilo/(boy**2)

if Vücut_Kitle_İndeksi < 18.5:
    print("Vücut kitle indeksinize göre zayıfsınız.")
elif 18.5 < Vücut_Kitle_İndeksi < 25:
    print("Vücut kitle indeksinize göre normalsiniz.")
elif 25 < Vücut_Kitle_İndeksi <  30:
    print("Vücut kitle indeksinize göre fazla kilolusunuz.")
elif 30 < Vücut_Kitle_İndeksi:
    print("Vücut kitle indeksinize göre obezsiniz.")

