# Write a recursive function that given a number returns the sum of integers from 1 to that number. Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.

def rsigma(num):
    if num <= 0:
        return 0
    else:
        return num + rsigma(num-1)

print(rsigma(5))
print(rsigma(2.5))
print(rsigma(-1))

# Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. If not an integer, truncate. Experts tell us 0! is 1. rFact(3) = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).

def rFact(num):
    if num <= 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * rFact(int(num-1))
    
print(rFact(3))
print(rFact(6.5))
print(rFact(0))
print(rFact(-1))


