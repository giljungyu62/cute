members = ["김상희", "김아현", "김지환"]

def members_list(array):
    list_member = ""
    for members in array:
        list_member += "<li>" + members + "</li>"
    return list_member

print(members_list(members))