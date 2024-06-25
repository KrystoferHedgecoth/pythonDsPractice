def list_manipulation(lst, command, location, value=None):
    if command == "remove":
        if location == "beginning":
            return lst.pop(0)
        elif location == "end":
            return lst.pop()
        else:
            return None
    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
        elif location == "end":
            lst.append(value)
        else:
            return None
    else:
        return None

    return lst