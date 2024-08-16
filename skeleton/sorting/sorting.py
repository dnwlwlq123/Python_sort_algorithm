my_list = [3,5,9,8,1,2,6,4,10,54,24,12,65,43,12,13,46,25,76]

# def get_insert_idx(res, elem,
#         cmp = lambda x, y: x if x > y else y, ):
#
#     for i, e in enumerate(res):
#         case = cmp(elem, e)
#         if elem == cmp(elem, e): # elem > e:
#             return i
#
#     return len(res)
#
#
# def sort3_insert(lst, cmp = lambda x, y: x if x > y else y):
#     res = []
#
#     for elem in lst:
#         new_idx = get_insert_idx(res, elem, cmp = cmp)
#         res.insert(new_idx, elem)
#
#     return res
# final_sort = sort3_insert((my_list))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

    return arr

def merge_sort(lst, cmp = lambda x, y: x if x > y else y):
    if len(lst) <= 1:
        return lst
    def merged(left,right):
        my_sort_merge = []
        i = j = 0
        while i < len(left) and j < len(right):
            if cmp(left[i], right[j]) == right[j]:
                my_sort_merge.append(left[i])
                i+=1
            else:
                my_sort_merge.append(right[j])
                j+=1
        my_sort_merge.extend(left[i:])
        my_sort_merge.extend(right[j:])
        return my_sort_merge

    mid = len(lst) // 2
    left_mid = merge_sort(lst[:mid], cmp)
    right_mid = merge_sort(lst[mid:], cmp)
    return merged(left_mid, right_mid)


final_lst_asc = merge_sort(my_list)
final_lst_desc = merge_sort(my_list, cmp = lambda x, y: x if x<y else y)

print(f'merge 오름차순 {final_lst_asc}')
print(f'merge 내림차순 {final_lst_desc}')
print()


def quick_sort(lst, cmp = lambda x, y: x if x > y else y):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = [x for x in lst[1:] if cmp(x, pivot) != x]
    right = [x for x in lst[1:] if cmp(x, pivot) == x]

    sorted_left = quick_sort(left, cmp)
    sorted_right = quick_sort(right, cmp)

    return sorted_left + [pivot] + sorted_right

quick_final_asc = quick_sort(my_list)
print(f'quick 오름차순: {quick_final_asc}')
quick_final_desc = quick_sort(my_list, cmp=lambda x, y: x if x<y else y)
print(f'quick 내림차순: {quick_final_desc}')


def tim_sort(lst, run_size=32):
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def tim_sort_help(arr):





final_sort_tim = tim_sort(my_list)
print(f'tim {final_sort_tim}')









