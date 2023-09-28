class Sample:
    x=200
    y=699
    def fun(self):
        print('fun function .....')
        

print(Sample.x) #class and static properties we can call directly or with class name so no need to create object
 
Sample.x=250
print(Sample.x)

obj=Sample()
obj.x=350    # so see here is not changed value we can not change class or static vars with obj but we can change with class
print(Sample.x)

