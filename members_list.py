member = ["장승운", "길준규", "장성규"]

def members_list(tag_name, array):
    list_member = "" # 이거 작성하면 코드 마스터함
    for members in array:
        print("배열 구경하기", list_member)
        print("members 구경하기", members)
        list_member += f"<{tag_name}>{members}</{tag_name}>"
    return list_member

print("반환값")
print(members_list("li", member))