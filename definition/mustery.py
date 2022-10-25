def double(arg):
    print('Before: ', arg)
    arg=arg*2
    print('After: ', arg)

def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)

nums=[1,6,3,7,9]
num=10
double(nums)
print(num)
print(nums)
print()
change(nums)
print(nums)