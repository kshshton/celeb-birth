
def formatted_name(first_name: str, last_name: str) -> str:
    name = first_name[0].upper() + first_name[1:].lower()
    surname = last_name[0].upper() + last_name[1:].lower()
    return '_'.join([name, surname])
