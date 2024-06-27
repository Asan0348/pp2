import sample
data = sample.data

# Вывод заголовков таблицы
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<7} {:<5}".format("DN", "Description", "Speed", "MTU"))
print("-" * 50 + " " + "-" * 20 + " " + "-" * 7 + " " + "-" * 5)

# Обход и вывод данных для каждого интерфейса
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')
    
    print("{:<50} {:<20} {:<7} {:<5}".format(dn, description, speed, mtu))
