from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 16", "+79005645658"))
catalog.append(Smartphone("Samsung", "Galaxy S20", "+79004445566"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 9", "+79007555899"))
catalog.append(Smartphone("Google", "Pixel 7", "+79001234567"))
catalog.append(Smartphone("OnePlus", "8 Pro", "+79009879993"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
