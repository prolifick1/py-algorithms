def merge(lst1, lst2):
    mergedLst = list()
    p1 = 0
    p2 = 0
    while(p1 < len(lst1) and p2 < len(lst2)):
        if(lst1[p1] < lst2[p2]):
            mergedLst.append(p1)
            p1+=1
        else:
            mergedLst.append(p2)
            p2+=1
    if(p1 < len(lst1)):
        mergedLst += lst1[p1:]
    if(p2 < len(lst2)):
        mergedLst += lst2[p2:]
    return mergedLst

def mergesort(lst):
    if(len(lst) < 2):
        return lst
    mid = len(lst)//2
    left_half = lst[:mid]
    right_half = lst[mid:]
    return(merge(mergesort(left_half), merge_sort(right_half)))
