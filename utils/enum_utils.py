from enum import IntEnum


class UserRole(IntEnum):
    ADMIN = 1
    MERCHANT = 2
    CUSTOMER = 3

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]


class Gender(IntEnum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    @classmethod
    def get_gender(cls):
        return [(key.value, key.name) for key in cls]


class DeviceType(IntEnum):
    ANDROID = 1
    WEB = 2
    IOS = 3
    ALL = 4

    @classmethod
    def get_type(cls):
        return [(key.value, key.name) for key in cls]


# This one for promo code discount type
class DiscountType(IntEnum):
    AMOUNT = 1
    PERCENTAGE = 2

    @classmethod
    def get_discount_type(cls):
        return [(key.value, key.name) for key in cls]
