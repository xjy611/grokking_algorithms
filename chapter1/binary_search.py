# _*_ coding : UTF-8 _*_
# 开发人员 : 16092
# 开发时间 : 2020/7/8 13:58
# 文件名称 : binary_search.PY
# 开发工具 : PyCharm


def binary_search(list, item):
    """
    二分查找法
    Args:
        list: 需要查找的列表
        item:需要查找的元素

    Returns:
        mid:元素索引
        None:查找不到返回空
    """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, 2))
