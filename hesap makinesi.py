def toplama():
    try:
        t = int(input("Birinci sayıyı giriniz: "))
    except ValueError:
        print("Lütfen sayıyı doğru giriniz!")
        return toplama()
    while True:

      t1 = (input("ana menü için 'g' ye basınız\n+ - / * => "))
      if t1 == " " or t1 == "":
        break
      
      try:
        t2 = int(input("=>")) 
      except ValueError:
        print("sayıyı doğru giriniz!")
        
      else:
        if t1 == "+":
          t = t + t2
        elif t1 == "-":
          t = t - t2
        elif t1 == "*":
          t = t * t2
        elif t1 == "/":
          if t2 == 0:
            print("Bir sayı 0'a bölünemez!")
            continue
          t = t / t2
        elif t1 == "g":
          print("Ana menüye dönülüyor...")
          print(menu())
          break
        else:
          print("geçersiz işlem!")
          continue

        print("Sonuç: ", t)
        continue
    return t
def kare():
  print(">" * 15, "KARE ALMA", "<" * 15)
  try:
    a = float(input("ana menü için 'g' ye basınız\nkaresini almak istediğiniz sayıyı giriniz: "))
    if a == "g":
      print("Ana menüye dönülüyor...")
      print(menu())
    return("{} sayısının karesi= {}".format(a, a*a))
  except ValueError:
    return("sayı giriniz!")
def kök():
  print(">" * 15, "KÖK ALMA", "<" * 15)
  try:
    a = float(input("ana menü için 'g' ye basınız\nkökünü almak istediğiniz sayıyı girin: "))
    if a < 0:
      return "negatif sayının kökü olamaz!"
    if a == "g":
      print("Ana menüye dönülüyor...")
      print(menu())
    return("{} sayısının kökü= {}.".format(a, a**0.5))
  except ValueError:
    print("sayı giriniz!")
def küp():
  print(">" * 15, "KÜP ALMA", "<" * 15)
  try:
    a = float(input("ana menü için 'g' ye basınız\nkübünü almak istediğiniz sayıyı yazınız: "))
    if a == "g":  
      print("Ana menüye dönülüyor...")
      print(menu())
    return f"{a} sayısının küpü = {a ** 3}"
  except ValueError:
     return("sayı giriniz!")
def üssü():
  print(">" * 15, "ÜSLÜ HESAPLAMA", "<" * 15)
  try:
   while True:
    a = float(input("ana menü için 'g' ye basınız\ntabanı giriniz "))
    b = float(input("kuvvet'i giriniz: "))
    if a == "g":  
      print("Ana menüye dönülüyor...")
      print(menu())
    return("{}  üzeri {} = {}".format(a, b, pow(a,b)))
  except ValueError:
    return("sayı giriniz!")
def menu():
    while True:
        print("\n" + "="*10 + " HESAP MAKİNESİ MENÜ " + "="*10)
        print("1. Dört İşlem (Toplama/Çıkarma/Çarpma/Bölme)")
        print("2. Kare Alma")
        print("3. Kök Alma")
        print("4. Küp Alma")
        print("5. Üslü Hesaplama")
        print("0. Çıkış")
        secim = input("Seçiminizi girin: ")
        if secim == "1":
            print("Sonuç:", toplama())
        elif secim == "2":
            print(kare())
        elif secim == "3":
            print(kök())
        elif secim == "4":
            print(küp())
        elif secim == "5":
            print(üssü())
        elif secim == "0":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

menu()