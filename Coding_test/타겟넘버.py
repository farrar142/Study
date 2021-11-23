numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    answer = 0
    bin_tree = [[numbers[0],-numbers[0]]]
    for i in range(1,len(numbers)):
        bin_tree_column = []
        for j in range(0,len(bin_tree[i-1])):        
            bin_tree_column.append(bin_tree[i-1][j]+numbers[i])
            bin_tree_column.append(bin_tree[i-1][j]-numbers[i])
        bin_tree.append(bin_tree_column)  
    return bin_tree[-1].count(target)

solution(numbers,target)