def contain_duplicate(lst):
    for i in lst:
        if lst.count(i)>1:
            return True
        else:
            return False

nums=[1,2,3,1]
print(contain_duplicate(nums))
