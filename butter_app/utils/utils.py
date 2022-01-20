def get_choices_for_enum(enum_class) -> list:
    return [(item.value, item.name) for item in enum_class]
