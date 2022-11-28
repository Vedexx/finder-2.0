import urllib.parse

b='%C8%E2%E0%ED%EE%E2'
a = 'Иванов'
print(urllib.parse.quote_plus(a,encoding='cp1251'))
print(urllib.parse.unquote(b))