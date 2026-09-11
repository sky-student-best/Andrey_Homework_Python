from address import Address
from mailing import Mailing

sender_address = Address("101060", "Москва", "ул. Лаврентьева", "д. 5", "кв. 51")
receiver_address = Address("196200", "Казань", "Казанский проспект", "д. 8", "кв. 156")

my_mailing = Mailing(
    to_address=receiver_address,
    from_address=sender_address,
    cost=550,
    track="RU123456789"
)

from_addr_str = (
    f"{my_mailing.from_address.index}, "
    f"{my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, "
    f"{my_mailing.from_address.house} - "
    f"{my_mailing.from_address.apartment}"
)

to_addr_str = (
    f"{my_mailing.to_address.index}, "
    f"{my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, "
    f"{my_mailing.to_address.house} - "
    f"{my_mailing.to_address.apartment}"
)

print(
    f"Отправление {my_mailing.track} из {from_addr_str} "
    f"в {to_addr_str}. Стоимость {my_mailing.cost} рублей."
)
