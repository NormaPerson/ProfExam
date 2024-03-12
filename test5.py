def hash(q, p=200, m=11800):
    # из-за другой кодировки, хоть и рекомендуется 118 но я решил взять большее число 11800
    hash_summ = 0
    for j, i in enumerate(q):
        hash_summ += ord(i) * p ** j
    return hash_summ % m, hex(hash_summ % m)
# открываем файл для чтения и записываем информацию о заголовке в head, а оставшиеся данные в data
with open('game.txt', encoding='UTF-8') as f:
    data = f.readlines()
    head = data[0]
    # при записи в data очищаем строку от лишних смиволов (\n) и разделяем по символу $
    data = [i.strip().split('$') for i in data[1:]]

with open('game_with_hash.csv', 'w', encoding="UTF-8") as f:
    head = ", ".join(['hash'] + head.strip().split("$"))
    file_data = [', '.join([str(hash(''.join( i[0].split(' ') + i[1].split(' ') ))[0])] + i) for i in data]
    print(head + '\n' + '\n'.join(file_data), file=f)
