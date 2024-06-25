def extract_full_names(people):
    full_names = []
    
    for person in people:
        full_name = f"{person['first']} {person['last']}"
        full_names.append(full_name)
    
    return full_names