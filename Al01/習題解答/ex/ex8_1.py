# ex8_1.py
phone_book = {}                   # 通訊簿的字典
phone_book['Trump'] = '0912111111'
phone_book['Lisa'] = '0922222222'
phone_book['Mike'] = '0932333333'
phone_book['Emergency'] = '119'
name = input('請輸入名字 : ')
if name in phone_book:
    print(f'{name} 的電話號碼是 {phone_book[name]}')
else:
    print(f'{name} 不在通訊簿內 ')

