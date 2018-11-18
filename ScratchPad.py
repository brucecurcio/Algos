def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx] > list[idx+1]:
                temp = list[idx+1]
                list[idx+1] = list[idx]
                list[idx] = temp
    return list

def mergesort(unsortedlist):
    if len(unsortedlist)<=1:
        return unsortedlist
    
    middle = len(unsortedlist)//2
    left_half = unsortedlist[:middle]
    right_half = unsortedlist[middle]

    left_half = mergesort(left_half)
    right_half = mergesort(right_half)
    return merge(left_half, right_half)

    def merge(left_half, right_half):
        res = []

        while left_half != 0 and right_half != 0:
            if left_half[0] < right_half[0]:
                res.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                res.append(right_half[0])
                right_half.remove(right_half[0])
            if len(left_half == 0):
                res = res + right_half
            else:
                res = res + left_half
            return res

def insertion_sort(list):
    for i in range(1, len(list)):
        j = i-1
        nxt_element = list[i]

        while (list[j] > nxt_element) and (j >= 0):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = nxt_element
    return list
            

if __name__ == "__main__":
    list = [76,34,1,89,23,67,100,45]

    selection = input("please type bubble, merge, insertion, or selection")
    if selection == "bubble":
        print(bubblesort(list))
    elif selection == 'insertion':
        print(insertion_sort(list))

