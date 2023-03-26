game_map = str(input("Please enter feeding map as a list:"))
print(game_map)
map_list = game_map
game_map = game_map.replace(",'", ", '")
game_map = game_map.split("'], ['")
map_list = map_list.replace(",'", ", '")
map_list = map_list[3:-3]
map_list = map_list.split("'], ['")

list1 = []
list2 = []
list3 = []
for i in game_map:
    if "[['" in i:
        i = i[3:]
        list1.append(i.split("', '"))
    elif "']]" in i:
        i = i[:-3]
        list1.append(i.split("', '"))
    else:
        list1.append(i.split("', '"))

for i in game_map:
    if "[['" in i:
        i = i[3:]
        list3.append(i.split("', '"))
    elif "']]" in i:
        i = i[:-3]
        list3.append(i.split("', '"))
    else:
        list3.append(i.split("', '"))



movement = input("Please enter direction of movements as a list:")
print(movement)
movement = movement.replace(",'", " '")
movement = movement[2:-2]
movement = movement.split("', '")
point = 0
for i in movement:
    move = 0
    for l in list1:
        if "*" in l:
            move2 = l.index("*")
            break
        else:
            move += 1
    if i == "D":
        if move < len(list1) -1 and list1[move+1][move2] != "W":
            if list1[move + 1][move2] == "C":
                list1[move + 1][move2] = "*"
                list1[move][move2] = "X"
                point += 10

            elif list1[move + 1][move2] == "A":
                list1[move + 1][move2] = "*"
                list1[move][move2] = "X"
                point += 5

            elif list1[move + 1][move2] == "M":
                list1[move + 1][move2] = "*"
                list1[move][move2] = "X"
                point -= 5

            elif list1[move + 1][move2] == "X":
                list1[move + 1][move2] = "*"
                list1[move][move2] = "X"

            elif list1[move + 1][move2] == "P":
                list1[move + 1][move2] = "*"
                list1[move][move2] = "X"
                point += 0
                break
        elif move == len(list1):
            continue

    if i >= "U":
        if move > 0 and list1[move-1][move2] != "W":
            if list1[move - 1][move2] == "C":
                list1[move - 1][move2] = "*"
                list1[move][move2] = "X"
                point += 10

            elif list1[move - 1][move2] =="A":
                list1[move - 1][move2] = "*"
                list1[move][move2] = "X"
                point += 5

            elif list1[move - 1][move2] == "M":
                list1[move - 1][move2] = "*"
                list1[move][move2] = "X"
                point -= 5

            elif list1[move - 1][move2] == "X":
                list1[move - 1][move2] = "*"
                list1[move][move2] = "X"

            elif list1[move - 1][move2] == "P":
                list1[move - 1][move2] = "*"
                list1[move][move2] = "X"
                point += 0
                break
        else:
            continue

    if i == "L":
        if move2 != 0 and list1[move][move2 -1] != "W" :
            if  list1[move][move2 -1] == "C":
                list1[move][move2 - 1] ="*"
                list1[move][move2] = "X"
                point += 10

            elif list1[move][move2 -1] == "A":
                list1[move][move2 - 1] = "*"
                list1[move][move2] = "X"
                point += 5

            elif list1[move][move2 -1] == "M":
                list1[move][move2 - 1] = "*"
                list1[move][move2] = "X"
                point -= 5

            elif list1[move][move2 -1] == "X":
                list1[move][move2 - 1] = "*"
                list1[move][move2] = "X"

            elif list1[move][move2 -1] == "P":
                list1[move][move2 - 1] = "*"
                list1[move][move2] = "X"
                point += 0
                break
        else:
            continue

    if i == "R":
        if move2 >= len(list1[move]) -1:
            continue
        elif  list1[move][move2+1] !="W" and move2 < len(list1[move]) -1   :
            if list1[move][move2 +1] == "C":
                list1[move][move2 + 1] = "*"
                list1[move][move2] = "X"
                point += 10

            elif list1[move][move2 +1] == "A":
                list1[move][move2 + 1] = "*"
                list1[move][move2] = "X"
                point += 5

            elif list1[move][move2 +1] == "M":
                list1[move][move2 + 1] = "*"
                list1[move][move2] = "X"
                point -= 5

            elif list1[move][move2 +1] == "X":
                list1[move][move2 + 1] = "*"
                list1[move][move2] = "X"

            elif list1[move][move2 +1] == "P":
                list1[move][move2 + 1] = "*"
                list1[move][move2] = "X"
                point += 0
                break

print("Your board is:")
for a in list3:
    print(*a, end="\n")



print("Your output should be like this:")
for k in list1:
    print(*k, end="\n")
print("Your score is:",point)