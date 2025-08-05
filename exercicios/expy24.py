# o nome da cidade começa com 'SANTO'?
cid = input('digite a sua cidade: ').strip()
cidm = cid.upper()
print('o resultado é:', 'SANTO' in cidm[:5])
# print(cidm[:5] == 'SANTO')
