int_item = 10
comp_item = 18
mult_int = (int_item * 2)
item_2 = True
item_3 = False
item_4 = 0
item_5 = 1

usd_item = "usd"
usd_usd_rate = 1

eur_item = "eur"
usd_eur_rate = 0.86

uah_item = "uah"
usd_uah_rate = 26.23

chf_item = "chf"
usd_chf_rate = 0.91

rub_item = "rub"
usd_rub_rate = 71.88

byn_item = "byn"
usd_byn_rate = 2.46

if mult_int > comp_item:
    print("mult_int >", comp_item)

div_int = (int_item / 2)

if div_int < comp_item:
    print("div_int <", comp_item)

item_1 = (int_item + 10)
if item_1 < comp_item:
    print("item_1 <", comp_item)
else:
    print("item_1 >=", comp_item)

if item_2 < comp_item:
    print("item_2 =", item_2)
else:
    print("item_2 =", item_3)

if item_3 < comp_item:
    print("item_3 =", item_2)
else:
    print("item_3 =", item_3)

if item_5 < comp_item:
    print("item_5 =", item_5)
else:
    print("item_5 =", item_4)

if item_4 < comp_item:
    print("item_4 =", item_5)
else:
    print("item_4 =", item_4)

currency_convertor = item_2
if currency_convertor < comp_item:
    currency_usd = usd_item
    target_currency = eur_item
    target_currency_amount = 50
    currency_result = 0
    if target_currency == eur_item:
        currency_result = (target_currency_amount / usd_eur_rate)
        print(target_currency_amount, eur_item, "=", round(currency_result, 2), usd_item)
    elif target_currency == uah_item:
        currency_result = (target_currency_amount / usd_uah_rate)
        print(target_currency_amount, uah_item, "=", round(currency_result, 2), usd_item)
    elif target_currency == chf_item:
        currency_result = (target_currency_amount / usd_chf_rate)
        print(target_currency_amount, chf_item, "=", round(currency_result, 2), usd_item)
    elif target_currency == rub_item:
        currency_result = (target_currency_amount / usd_rub_rate)
        print(target_currency_amount, rub_item, "=", round(currency_result, 2), usd_item)
    elif target_currency == byn_item:
        currency_result = (target_currency_amount / usd_byn_rate)
        print(target_currency_amount, byn_item, "=", round(currency_result, 2), usd_item)
    else:
        print("Unknow currency")
else:
    print("currency_convertor =", item_3 )