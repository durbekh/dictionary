# # 1
# # Boshlang'ich dictionary: student_grades
# student_grades = {"Matematika": 90, "Fizika": 85, "Informatika": 95}
#
# # 1-vazifa: Yangi fan ("Kimyo", 88) qo‘shish
# # Kalit orqali qo‘shish: Dictionaryga yangi kalit-qiymat juftligini qo‘shish uchun kalitni to‘g‘ridan-to‘g‘ri ishlatamiz
# # Nima uchun ishlatildi: Dictionaryga yangi fan va uning bahosini qo‘shish uchun
# student_grades["Kimyo"] = 88
# result1 = student_grades
# print("1-vazifa natijasi:", result1)  # Natija: {'Matematika': 90, 'Fizika': 85, 'Informatika': 95, 'Kimyo': 88}
#
# # 2-vazifa: "Fizika" bahosini 87 ga o‘zgartirish
# # Kalit orqali o‘zgartirish: Mavjud kalitning qiymatini yangi qiymat bilan almashtirish
# # Nima uchun ishlatildi: "Fizika" fanining bahosini yangilash uchun
# student_grades["Fizika"] = 87
# result2 = student_grades
# print("2-vazifa natijasi:", result2)  # Natija: {'Matematika': 90, 'Fizika': 87, 'Informatika': 95, 'Kimyo': 88}
#
# # 3-vazifa: "Informatika" fanini o‘chirish
# # del operatori: Dictionarydan kalit-qiymat juftligini o‘chirish uchun ishlatiladi
# # Nima uchun ishlatildi: "Informatika" fanini dictionarydan olib tashlash uchun
# del student_grades["Informatika"]
# result3 = student_grades
# print("3-vazifa natijasi:", result3)  # Natija: {'Matematika': 90, 'Fizika': 87, 'Kimyo': 88}
#
# # 4-vazifa: Barcha baholar yig‘indisini topish
# # values() metodi: Dictionaryning faqat qiymatlarini ro‘yxat sifatida qaytaradi
# # sum() funksiyasi: Iterable (masalan, ro‘yxat) elementlarining yig‘indisini hisoblaydi
# # Nima uchun ishlatildi: Barcha baholarni yig‘ish uchun
# result4 = sum(student_grades.values())
# print("4-vazifa natijasi:", result4)  # Natija: 265
#
# # 5-vazifa: Baholar o‘rtachasini hisoblash
# # values() metodi: Dictionaryning qiymatlarini olish uchun
# # sum() funksiyasi: Qiymatlar yig‘indisini hisoblash uchun
# # len() funksiyasi: Dictionaryning uzunligini (elementlar sonini) qaytaradi
# # Nima uchun ishlatildi: Baholar o‘rtachasini hisoblash uchun (yig‘indi / elementlar soni)
# result5 = sum(student_grades.values()) / len(student_grades)
# print("5-vazifa natijasi:", result5)  # Natija: 88.333...
#
# # 6-vazifa: Eng yuqori bahoni topish
# # values() metodi: Dictionaryning qiymatlarini olish uchun
# # max() funksiyasi: Iterable ichidagi eng katta elementni qaytaradi
# # Nima uchun ishlatildi: Eng yuqori bahoni aniqlash uchun
# result6 = max(student_grades.values())
# print("6-vazifa natijasi:", result6)  # Natija: 90
#
# # 7-vazifa: Eng past bahoni topish
# # values() metodi: Dictionaryning qiymatlarini olish uchun
# # min() funksiyasi: Iterable ichidagi eng kichik elementni qaytaradi
# # Nima uchun ishlatildi: Eng past bahoni aniqlash uchun
# result7 = min(student_grades.values())
# print("7-vazifa natijasi:", result7)  # Natija: 87
#
# # 8-vazifa: Fanlar ro‘yxatini chop etish
# # keys() metodi: Dictionaryning faqat kalitlarini ro‘yxat sifatida qaytaradi
# # list() funksiyasi: keys() natijasini ro‘yxatga aylantirish uchun
# # Nima uchun ishlatildi: Faqat fanlar nomini ro‘yxat sifatida olish uchun
# result8 = list(student_grades.keys())
# print("8-vazifa natijasi:", result8)  # Natija: ['Matematika', 'Fizika', 'Kimyo']
#
# # 9-vazifa: Baholar ro‘yxatini chop etish
# # values() metodi: Dictionaryning faqat qiymatlarini ro‘yxat sifatida qaytaradi
# # list() funksiyasi: values() natijasini ro‘yxatga aylantirish uchun
# # Nima uchun ishlatildi: Faqat baholarni ro‘yxat sifatida olish uchun
# result9 = list(student_grades.values())
# print("9-vazifa natijasi:", result9)  # Natija: [90, 87, 88]
#
# # 10-vazifa: Dictionary bo‘sh yoki yo‘qligini tekshirish
# # len() funksiyasi: Dictionaryning uzunligini (elementlar sonini) qaytaradi
# # == 0: Uzunlik 0 ga teng bo‘lsa, dictionary bo‘sh deb hisoblanadi
# # Nima uchun ishlatildi: Dictionaryda element bor yoki yo‘qligini tekshirish uchun
# result10 = len(student_grades) == 0
# print("10-vazifa natijasi:", result10)  # Natija: False
# #2
# # Boshlang'ich dictionary: fruits
# fruits = {"olma": 5000, "banan": 12000, "uzum": 8000}
#
# # 1-vazifa: "anor" mevani 10000 so‘m bilan qo‘shish
# # Kalit orqali qo‘shish: Dictionaryga yangi kalit-qiymat juftligini qo‘shish
# # Nima uchun ishlatildi: Yangi meva va narxini qo‘shish uchun
# fruits["anor"] = 10000
# result1 = fruits
# print("1-vazifa natijasi:", result1)  # Natija: {'olma': 5000, 'banan': 12000, 'uzum': 8000, 'anor': 10000}
#
# # 2-vazifa: "banan" narxini 15000 ga o‘zgartirish
# # Kalit orqali o‘zgartirish: Mavjud kalitning qiymatini yangi qiymat bilan almashtirish
# # Nima uchun ishlatildi: "banan" narxini yangilash uchun
# fruits["banan"] = 15000
# result2 = fruits
# print("2-vazifa natijasi:", result2)  # Natija: {'olma': 5000, 'banan': 15000, 'uzum': 8000, 'anor': 10000}
#
# # 3-vazifa: "uzum" ni o‘chirish
# # del operatori: Dictionarydan kalit-qiymat juftligini o‘chirish uchun ishlatiladi
# # Nima uchun ishlatildi: "uzum" mevani dictionarydan olib tashlash uchun
# del fruits["uzum"]
# result3 = fruits
# print("3-vazifa natijasi:", result3)  # Natija: {'olma': 5000, 'banan': 15000, 'anor': 10000}
#
# # 4-vazifa: Narxlarning umumiy summasini topish
# # values() metodi: Dictionaryning faqat qiymatlarini ro‘yxat sifatida qaytaradi
# # sum() funksiyasi: Iterable elementlarining yig‘indisini hisoblaydi
# # Nima uchun ishlatildi: Barcha mevalar narxlarini yig‘ish uchun
# result4 = sum(fruits.values())
# print("4-vazifa natijasi:", result4)  # Natija: 30000
#
# # 5-vazifa: Eng qimmat mevani topish
# # max() funksiyasi: Iterable ichidagi eng katta elementni qaytaradi
# # key=fruits.get: max() funksiyasiga dictionary qiymatlari bo‘yicha taqqoslashni ko‘rsatadi
# # Nima uchun ishlatildi: Eng yuqori narxga ega mevani aniqlash uchun
# result5 = max(fruits, key=fruits.get)
# print("5-vazifa natijasi:", result5)  # Natija: banan
#
# # 6-vazifa: Eng arzon mevani topish
# # min() funksiyasi: Iterable ichidagi eng kichik elementni qaytaradi
# # key=fruits.get: min() funksiyasiga dictionary qiymatlari bo‘yicha taqqoslashni ko‘rsatadi
# # Nima uchun ishlatildi: Eng past narxga ega mevani aniqlash uchun
# result6 = min(fruits, key=fruits.get)
# print("6-vazifa natijasi:", result6)  # Natija: olma
#
# # 7-vazifa: Narxlar ro‘yxatini tartiblang
# # values() metodi: Dictionaryning qiymatlarini olish uchun
# # sorted() funksiyasi: Iterable elementlarini tartiblab ro‘yxat sifatida qaytaradi (o‘sish tartibida)
# # Nima uchun ishlatildi: Narxlarni kichikdan kattaga tartiblash uchun
# result7 = sorted(fruits.values())
# print("7-vazifa natijasi:", result7)  # Natija: [5000, 10000, 15000]
#
# # 8-vazifa: Dictionary uzunligini topish
# # len() funksiyasi: Dictionaryning elementlar sonini qaytaradi
# # Nima uchun ishlatildi: Dictionaryda nechta meva borligini aniqlash uchun
# result8 = len(fruits)
# print("8-vazifa natijasi:", result8)  # Natija: 3
#
# # 9-vazifa: "olma" narxini chop etish
# # get() metodi: Dictionarydan kalit bo‘yicha qiymatni olish uchun ishlatiladi
# # Nima uchun ishlatildi: "olma" ning narxini xavfsiz tarzda olish uchun
# result9 = fruits.get("olma")
# print("9-vazifa natijasi:", result9)  # Natija: 5000
#
# # 10-vazifa: Barcha mevalarni alifbo tartibida chop etish
# # keys() metodi: Dictionaryning kalitlarini ro‘yxat sifatida qaytaradi
# # sorted() funksiyasi: Kalitlarni alifbo tartibida tartiblash uchun
# # Nima uchun ishlatildi: Mevalar nomini alifbo tartibida ko‘rish uchun
# result10 = sorted(fruits.keys())
# print("10-vazifa natijasi:", result10)  # Natija: ['anor', 'banan', 'olma']
# # 3
# cities = {"Toshkent": 2500000, "Samarqand": 550000, "Buxoro": 280000}
# cities["Andijon"] = 600000
# cities1 = cities
# print("1-vazifa natijasi:", cities1)
# cities["Toshkent"] = 2600000
# cities2 = cities
# print("2-vazifa natijasi:", cities2)
# del cities["Buxoro"]
# cities3 = cities
# print("3-vazifa natijasi:", cities3)
# cities4 = sum(cities.values())
# print("4-vazifa natijasi:", cities4)
# cities5 = sum(cities.values()) / len(cities)
# print("5-vazifa natijasi:", cities4)
# cities6= max(cities, key=cities.get)
# print("6-vazifa natijasi:", cities5)
# cities7 = min(cities, key=cities.get)
# print("7-vazifa natijasi:", cities6)
# cities8 = list(cities.keys())
# print("8-vazifa natijasi:", cities8)
# cities9= sorted(cities.values())
# print("9-vazifa natijasi:", cities9)
# cities10 = len(cities) == 0
# print("10-vazifa natijasi:", cities10)
# # 4
# books = {"Alximik": "Paulo Koelyo", "Shaytanat": "Tohir Malik", "1984": "George Orwell"}
# books["O'tgan kunlar"] = "Abdulla Qahhor"
# books1 = books
# print("1-vazifa natijasi:", books1)
# books["Alximik"] = "Paulo Coelyo"
# books2 = books
# print("2-vazifa natijasi:", books2)
# del books1["1984"]
# books3 = books
# print("3-vazifa natijasi:", books3)
# books4 = len(books.keys())
# print("4-vazifa natijasi:", books4)
# books5= list(books.values())
# print("5-vazifa natijasi:", books5)
# books6 = sorted(books.keys())
# print("6-vazifa natijasi:", books6)
# books7 = books.get("Shaytanat")
# print("7-vazifa natijasi:", books7)
# books8 = len(books)
# print("4-vazifa natijasi:", books8)
# books9 = "O'tgan kunlar" in books
# print("9-vazifa natijasi:", books9)
# books10 = books.clear()
# print("10-vazifa natijasi:", books10)
# # 5
# currencies = {"USD": 12600, "EUR": 13500, "RUB": 140}
# currencies["GBP"] = 16000
# currencies1 = currencies
# print("1-vazifa natijasi:", currencies1)
# currencies["USD"] = 12000
# currencies2 = currencies
# print("2-vazifa natijasi:", currencies2)
# del currencies["RUB"]
# currencies3 = currencies
# print("3-vazifa natijasi:", currencies3)
# currencies4 = sum(currencies.values())
# print("4-vazifa natijasi:", currencies4)
# currencies5= max(currencies, key=currencies.get)
# print("5-vazifa natijasi:", currencies5)
# currencies6 = min(currencies, key=currencies.get)
# print("6-vazifa natijasi:", currencies6)
# currencies7 = list(currencies.keys())
# print("7-vazifa natijasi:", currencies7)
# currencies8 = sorted(currencies.values())
# print("8-vazifa natijasi:", currencies8)
# currencies9 = currencies.get("EUR")
# print("9-vazifa natijasi:", currencies9)
# currencies10 = len(currencies) == 0
# print("10-vazifa natijasi:", currencies10)
# # 6
# inventory = {"suv": 50, "non": 100, "shokolad": 20}
# inventory["cola"] = 30
# inventory1 = inventory
# print("1-vazifa natijasi:", inventory1)
# inventory["non"] = 80
# inventory2 = inventory
# print("2-vazifa natijasi:", inventory2)
# del inventory["shokolod"]
# inventory3 = inventory
# print("3-vazifa natijasi:", inventory3)
# inventory4 = sum(inventory.values())
# print("4-vazifa natijasi:", inventory4)
# inventory5= max(inventory, key=inventory.get)
# print("5-vazifa natijasi:", inventory5)
# inventory6 = min(inventory, key=inventory.get)
# print("6-vazifa natijasi:", inventory6)
# inventory7 = list(inventory.keys())
# print("7-vazifa natijasi:", inventory7)
# inventory8 = sorted(inventory.values())
# print("8-vazifa natijasi:", inventory8)
# inventory9 = inventory.get("EUR")
# print("9-vazifa natijasi:", inventory9)
# inventory10 = len(inventory) == 0
# print("10-vazifa natijasi:", inventory10)
# # # 7
# athletes = {"Ali": 150, "Vali": 120, "Sardor": 180}
# athletes["Nodir"] = 130
# athletes1 = athletes
# print("1-vazifa natijasi:", athletes1)
# athletes["vali"] = 140
# athletes2 = athletes
# print("2-vazifa natijasi:", athletes2)
# del athletes["Sardor"]
# athletes3 = athletes
# print("3-vazifa natijasi:", athletes3)
# athletes4 = sum(athletes.values())
# print("4-vazifa natijasi:", athletes4)
# athletes5 = sum(athletes.values()) / len(athletes)
# print("5-vazifa natijasi:", athletes5)
# athletes6 = max(athletes, key=athletes.get)
# print("6-vazifa natijasi:", athletes6)
# athletes7 = min(athletes, key=athletes.get)
# print("7-vazifa natijasi:", athletes7)
# athletes8 = list(athletes.keys())
# print("8-vazifa natijasi:", athletes8)
# athletes9 = sorted(athletes.values())
# print("9-vazifa natijasi:", athletes9)
# athletes10 = len(athletes) == 0
# print("10-vazifa natijasi:", athletes10)
# # # 8
# menu = {"osh": 25000, "shashlik": 30000, "somsa": 5000}
# menu["lag'mon"] = 20000
# menu1 = menu
# print("1-vazifa natijasi:", menu1)
# menu["somsa"] = 6000
# menu2 = menu
# print("2-vazifa natijasi:", menu2)
# del menu["shashlik"]
# menu3 = menu
# print("3-vazifa natijasi:", menu3)
# menu4 = sum(menu.values())
# print("4-vazifa natijasi:", menu4)
# menu5 = max(menu, key=menu.get)
# print("5-vazifa natijasi:", menu5)
# menu6 = min(menu, key=menu.get)
# print("6-vazifa natijasi:", menu6)
# menu7 = list(menu.keys())
# print("7-vazifa natijasi:", menu7)
# menu8 = sorted(menu.values())
# print("8-vazifa natijasi:", menu8)
# menu9  = menu.get("osh")
# print("9-vazifa natijasi:", menu9)
# menu10 = len(menu) == 0
# print("10-vazifa natijasi:", menu10)
# # # 9
# faculties = {"IT": 120, "Matematika": 80, "Filologiya": 60}
# faculties["Fizika"] = 90
# faculties1 = faculties
# print("1-vazifa natijasi:", faculties1)
# faculties["IT"] = 130
# faculties2 = faculties
# print("2-vazifa natijasi:", faculties2)
# del faculties["Filologiya"]
# faculties3 = faculties
# print("3-vazifa natijasi:", faculties3)
# faculties4 = sum(faculties.values())
# print("4-vazifa natijasi:", faculties4)
# faculties5 = sum(faculties.values()) / len(faculties)
# print("5-vazifa natijasi:", faculties5)
# faculties6 = max(faculties, key=faculties.get)
# print("6-vazifa natijasi:", faculties6)
# faculties7 = min(faculties, key=faculties.get)
# print("7-vazifa natijasi:", faculties7)
# faculties8 = list(faculties.keys())
# print("8-vazifa natijasi:", faculties8)
# faculties9 = sorted(faculties.values())
# print("9-vazifa natijasi:", faculties9)
# faculties10 = len(faculties) == 0
# print("10-vazifa natijasi:", faculties10)
# # # 10
# destinations = {"Parij": 500, "Dubay": 300, "Istanbul": 200}
# destinations["London"] = 450
# destinations1 = destinations
# print("1-vazifa natijasi:", destinations1)
# destinations["Istanbul"] = 250
# destinations2 = destinations
# print("2-vazifa natijasi:", destinations2)
# del destinations["Dubay"]
# destinations3 = destinations
# print("3-vazifa natijasi:", destinations3)
# destinations4 = sum(destinations.values())
# print("4-vazifa natijasi:", destinations4)
# destinations5 = max(destinations, key=destinations.get)
# print("5-vazifa natijasi:", destinations5)
# destinations6 = min(destinations, key=destinations.get)
# print("6-vazifa natijasi:", destinations6)
# destinations7 = list(faculties.keys())
# print("7-vazifa natijasi:", destinations7)
# destinations8 = sorted(destinations.values())
# print("8-vazifa natijasi:", destinations8)
# destinations9 = destinations.get("Parij")
# print("9-vazifa natijasi:", destinations9)
# destinations10 = len(destinations) == 0
# print("10-vazifa natijasi:", destinations10)






