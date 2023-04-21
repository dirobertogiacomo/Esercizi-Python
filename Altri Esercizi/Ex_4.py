# Find m such that 137^m mod 14731 = 6849

def mybemodn (b,e,n):
    """
    This function computes b^e mod n iteratively as c=(b c) mod n.
    
    Giacomo Di Roberto, February 2022, version 1.0

    """
     
    c = 1
    b = b%n

    for i in range(e):
        c = (b*c)%n
    
    return c

b = 137
r = 6849
n = 14731
c = 0
m = 2

while c != r:
    c = mybemodn(b,m,n)
    m += 1

m -= 1
print(m)

