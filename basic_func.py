def inverse(a):
    if a==-1:
        b = 1
    elif a==1:
        b = -1
    else:
        b = 'wrong'
    return b
    
def string_inv(a):
    b = [-1]*len(a)
    for i in range(len(a)):
        b[i] = inverse(a[i])
    return b
