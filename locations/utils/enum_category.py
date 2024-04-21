from utils.enum_parent import EnumParent


class EnumCategoryLayer1(EnumParent):
    """
    this class is for the top level organization
    """

    SELL = "sell"
    RENT = "rent"


class EnumCategoryLayer2(EnumParent):
    HOUSE = "house"
    APARTMENT = "apartment"
    SHOP = "shop"
    OFFICE = "office"
