import copy

# 原始对象
original_list = [1, [2, 3], [4, 5]]

# 创建深层副本
deep_copy_list = copy.deepcopy(original_list)

# 修改原始对象
original_list[1][0] = 'X'

# 输出结果
print("Original List:", original_list)
print("Deep Copy List:", deep_copy_list)