
def merge(list1, list2):
    p1 = 0
    p2 = 0
    merged_list = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            merged_list.append(list1[p1])
            p1 += 1
        else:
            merged_list.append(list2[p2])
            p2 += 1
    if p1 < len(list1):
        merged_list.extend(list1[p1:])
    if p2 < len(list2):
        merged_list.extend(list2[p2:])
    return merged_list


def merge_sort(list):
    if len(list) < 2:
        return list
    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

