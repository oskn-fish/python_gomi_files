# 動的計画法による部分和問題

# 組み合わせテーブル例
# table[3] = [[1,2], [3,0]]

# 問題が小さいため，brute forceのほうが早い

import time

# 和を取る個数
COMB_LENGTH = 3
# 和の値
ANS_SUM = 100


list_element_3x3 = [34, 19, 40, 39, 31, 25, 54, 38, 28]
list_element_4x4 = [57, 60, 55, 23, 50, 30, 29, 56, 53, 19, 33, 39, 36, 32, 46, 54]

def sum_DP(list_element):
    table = [set() for _ in range(ANS_SUM+1)]

    # 初めに要素を一つだけ使うものをtableに追加
    # setのsetにするにはimmutableなsetであるfrozensetを用いる．
    # https://stackoverflow.com/questions/37105696/how-to-have-a-set-of-sets-in-python
    for element in list_element:
        table[element].add(frozenset([element]))
        
    # 和が 1, 2, 3, ..., 100 になるような順で組み合わせを考える
    for current_sum in range(1, ANS_SUM+1):
        for element in list_element:
            if current_sum-element<0: continue
            
            if table[current_sum-element]:
                for comb in table[current_sum-element]:
                    if len(comb)<=COMB_LENGTH-1 and not element in comb: table[current_sum].add(comb|frozenset([element]))
    ans = list(filter(lambda x: len(x)==COMB_LENGTH, table[100]))
    print(ans)
                
                
time_before = time.time()                
sum_DP(list_element_3x3)
time_dp_3x3 = time.time()-time_before
print("time for 3x3 = "+str(time_dp_3x3))
time_before = time.time()
sum_DP(list_element_4x4)
time_dp_4x4 = time.time()-time_before
print("time for 4x4 = "+str(time_dp_4x4))



# 総当り
def brute_force(list_element):
    for smallest_i in range(len(list_element)-2):
        for middle_i in range(smallest_i+1, len(list_element)-1):
            for biggeset_i in range(middle_i+1, len(list_element)):
                if list_element[smallest_i]+list_element[middle_i]+list_element[biggeset_i] == ANS_SUM:
                    print({list_element[smallest_i], list_element[middle_i], list_element[biggeset_i]})
    

print("---------------------------------")
time_before = time.time()                
brute_force(list_element_3x3)
time_brute_3x3 = time.time()-time_before
print("time for 3x3 = "+str(time_brute_3x3))
time_before = time.time()
brute_force(list_element_4x4)
time_brute_4x4 = time.time()-time_before
print("time for 4x4 = "+str(time_brute_4x4))
print("---------------------------------")
print("time difference between dp and brute force:")
print("3x3: "+str(time_brute_3x3-time_dp_3x3))
print("4x: "+str(time_brute_4x4-time_dp_4x4))