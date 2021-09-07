# last occurrence of element using Modified Binary Tree
# Assumption and Pre-condition that list is sorted
def get_firstOccurence(l,x):
    left = 0
    right = len(l) -1
    while left <= right:
        mid = (left + right)//2
        if x > l[mid]:
            left = mid + 1
        elif x < l[mid]:
            right = mid - 1
        elif x == l[mid]:
            if  mid + 1 == len(l) or l[mid] != l[mid+1]:
                return mid
            else:
                left = mid + 1

    return -1


if __name__ == '__main__':
    lst = [10,10,10,41,7,20,19]
    lst.sort()
    print(lst)
    print(get_firstOccurence(lst, 10))

    lst1 = [10, 10, 10, 4, 7, 2, 1]
    lst1.sort()
    print(lst1)
    print(get_firstOccurence(lst1, 10))
