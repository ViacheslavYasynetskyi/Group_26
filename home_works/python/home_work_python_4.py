
count = 0
range_count = 10
for_count = 0
run = True
# while run:
#     print("Hello Cycle")

# while run:
#     print("Step =",count)
#     count +=1

# while count < range_count:
#     print("Step =",count)
#     count += 1

# while count < range_count:
#     print("Step =",count)
#     count += 1
#     if count == 3:
#         print("Step =",count, "If body")

# while count < range_count:
#     print("Step =",count)
#     count += 1
#     if count == range_count:
#         print("STOP", count)
#         break
#
# for item in range(for_count, range_count):
#     print("Step = ", item)

# for item in range(0, 30):
#     print("Step = ", item)
#     if item == 5:
#         print("Item =", item)
#     if item == 10:
#         print("Item =", item)
#     if item < 4:
#         print("Item <", item)
#     if item >= 27:
#         print("Item >=", item)

# for item in range(0, range_count+1):
#     print("Step =", item)
#     if item == 7:
#         inner_count = 0
#         print("-- inner_count =", inner_count)
#         for inner_item in range(0, item):
#             print("-------- Inner_Step =", inner_item)
#             if inner_item == 5:
#                 inner_count = inner_item
#         print("-- inner_count =", inner_count)

# for item in range(0, 20):
#     print("Step =", item)
#     if 7<item>12:
#         print("If_item =", item)
#         continue
#     print("End_iteration =", item)

usd_uah_rate = 26.23
eur_uah_rate = 31.88
chf_uah_rate = 30.91
gbp_uah_rate = 36.63
cny_uah_rate = 4.26

 # №1
# while True:
#     input_value = input("You enter UAH:")
#     nn = int(input_value) / usd_uah_rate
#     print("USD =",round(nn,2))
#     break
#  №2
# while True:
#     input_value = input("You enter UAH:")
#     usd = int(input_value) / usd_uah_rate
#     eur = int(input_value) / eur_uah_rate
#     chf = int(input_value) / chf_uah_rate
#     gbp = int(input_value) / gbp_uah_rate
#     cny = int(input_value) / cny_uah_rate
#     print(" USD =",round(usd,2),"\n",
#           "EUR =",round(eur, 2),"\n",
#           "CHF =",round(chf, 2),"\n",
#           "GBP =",round(gbp, 2),"\n",
#           "CNY =",round(cny, 2),"\n",)
#     break
#  №3
dict_cash = {"USD": 26.23, "EUR": 31.88, "CHF": 30.91, "GBP": 36.63, "CNY": 4.26}
while True:
    input_value = input()
    print("You enter UAH:", input_value)
    try:
        if len(input_value) == 0:
            print("You entered an empty field. Enter a number.")
            break
        if float(input_value) <= 0:
            print("Enter a positive number.")
            break
        for k, v in dict_cash.items():
            c = float(input_value)/v
            print(k, round(c, 2))
        break
    except:
        print("You did not enter a number. Enter a number.")
        break