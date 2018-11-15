def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range (iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx]=list[idx+1]
                list[idx+1] = temp

if __name__ == "__main__":
    list = [19,3,31,45,6,11,121,27]

    selection = input("type bubble, merge, insertion, sheel, selection")
    print(selection)
    if selection == "bubble":
        bubblesort(list)
        print(list)

