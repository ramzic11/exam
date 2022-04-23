

n = [2, 5, 4, -2, -4, -5]

def count(list):
    x = sum(i>0 for i in list)
    y = sum(i<0 for i in list)
    print([x, y])    
count(n)          