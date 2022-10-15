#%%
import copy

def tow_sum(list1, num):
    for i in list1:
        temp = copy.copy(list1)
        temp.remove(i)
        for j in temp:
            if i + j == num:
                print('True')
                return
    
    print('False')
#%%
tow_sum([1, 3, 4, 5], 10)