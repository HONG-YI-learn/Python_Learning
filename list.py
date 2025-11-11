shopping_list = []
shopping_list.append("洗衣液" )
shopping_list.append("牙膏")
shopping_list.append("垃圾袋" )
print(shopping_list)
shopping_list.remove("牙膏")
print(shopping_list)
shopping_list[1] = "垃圾桶"
print(shopping_list)

price = [15 , 464 , 654 , 4 , 68 , 89]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)
print(max_price)
print(min_price)
print(sorted_price)