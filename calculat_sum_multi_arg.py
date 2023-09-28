#with multi argument passing with return statement
def calculat_sum_multi_arg(x,y):
    
    add=x+y
    sub=x-y
    multi=x*y
    div=x/y
    
    return add,sub,multi,div

result=calculat_sum_multi_arg(4,3)
print(result)
