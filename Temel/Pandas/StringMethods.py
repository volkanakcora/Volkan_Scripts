# -*- coding: utf-8 -*-
print ("engin demirog".upper())

import pandas as pd

orders = pd.read_table("orders.tsv")

print(orders.head())
print(orders.columns)
orders.item_name = orders.item_name.str.upper() # item isimlerini büyütür.
print(orders.item_name)

print(orders.item_name.str.contains("CHICKEN"))  # name den sonra str eki koyarak bu işlemleri yapabiliriz.
orders.choice_description = orders.choice_description.str.replace("[","").str.replace("]","")# istediğiniz yerdeki simgeleri değiştirme amacıyla kullanılır