#price = 100
#dicount = 5
#price_wirh_discount = price - price * dicount / 100
#print(price_wirh_discount)


def discounted(price, discount, max_discounted=50):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discounted = abs(max_discounted)
        if max_discounted > 95:
            raise ValueError('Мвксимальная скидка не может быть более 95%')
        if discount >= max_discounted:
            price_with_discount = price
        else:
            price_with_discount = price - price * discount / 100
        return price_with_discount
    except (ValueError, TypeError):
        print('Неверный тип данных')



#product = {
#    'name': 'iPhone Xs',
#    'stock': 5,
#    'price': 65000.0,
#    'discount': 96
#}

#product['with_discount'] = discounted(product['price'],product['discount'], max_discounted=95)
#print(product)

print(discounted(100, 'sdsd', max_discounted=94))
print(discounted(80, 40, max_discounted=94))