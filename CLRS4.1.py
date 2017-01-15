import numpy as np;  
import time; 
import random; 

def findMaximumCrossingSubarray(A, low, mid, high):
    """
        Returns left index, right index, and value of maximum crossing subarray.
        A is integer array. Low, mid and high are array indices respectively representing start, mid and end of an integer array A. 
    """
    leftSum = -np.inf; 
    maxLeft = low;
    maxRight = high; 
    
    lSum = 0; 
    for i in range(mid, low-1, -1):
        lSum = lSum + A[i]; 
        if (lSum > leftSum):
            leftSum = lSum;
            maxLeft = i; 
    
    rightSum = -np.Inf;  
    rSum = 0;
    for j in range(mid+1, high):
        rSum = rSum + A[j];
        if (rSum > rightSum):
            rightSum = rSum;
            maxRight = j; 
    return (maxLeft, maxRight, (leftSum + rightSum));

def findMaximumSubarray(A, low, high):
    """
        Finds the maximum subarray and its value using recursive appraoch.
        Returns left index, right index, and value of maximum subarray for given array A. 
        low and high are respecitvley start and end indcies of array A. Right index in not inclusive.
    """
    if (high == low):
        return (low, high, A[low]) 
    else:
        mid = (low + high) / 2 
        
        leftLow, leftHigh, leftSum = findMaximumSubarray(A, low, mid); 
        rightLow, rightHigh, rightSum = findMaximumSubarray(A, mid+1, high); 
        crossLow, crossHigh, crossSum = findMaximumCrossingSubarray(A, low, mid, high);

        if(leftSum >= rightSum and leftSum >= crossSum):
            return leftLow, leftHigh, leftSum;
        elif(rightSum >= leftSum and rightSum >= crossSum):
            return rightLow, rightHigh, rightSum;
        else:
            return (crossLow, crossHigh, crossSum); 

def maxSubArray_bruteforce(A):
    """
       Finds the maximum subarray and its value using a bruteforce approach to maximum subarray problem.
       Input: A an array of integer, 
       Return low and high are indices of low and high and a maxsum 
    
    """
    low = 0; 
    high = len(A)-1; 

    maximum = 0;
    left =low; 
    right = high;  
    
    
    for i in range (low, high):
        current = 0; 
        for j in range (i, high):
            current = current + A[j];
            if (current > maximum):
                maximum = current; 
                left = i; 
                right = j;
    return (left, right, maximum); 
def maxSubArray_LinearTime(A):
    '''
        4.1.5
        At the beginning, the first element is where the max subarray ends, and is
        the total value of maxsubarray
    '''
    maxEndingHere = A[0] #start with first element.
    maxSoFar = A[0] 
    start = 0;
    end = 0; 
    for i in range (1, len(A)):
        #maxEnding here stores the sum of subarray to this index.
        #the start index is reset whenever, sum to this index is less than the value at this index.
        #the end index is reset whever, new element is adde to max sofar.
        if(maxEndingHere + A[i] < A[i]):
            start = i
        maxEndingHere = max(A[i], maxEndingHere + A[i])
        
        if(maxEndingHere > maxSoFar):
            maxSoFar = maxEndingHere
            end = i           
        
    return start, end, maxSoFar

def main():
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7];
    ##Use this switch to simulate the time.
    #A = random.sample(range(-1000,1000),1000); 
    print "Array:       ", A; 
    start = time.time();
    print "Recursive:   ", findMaximumSubarray(A, 0, len(A)-1);
    print "     Finished: ", (time.time() - start)*1000000
    start = time.time();
    print "Brute Force: ", maxSubArray_bruteforce(A); 
    print "     Finished: ", (time.time() - start)*1000000
    start = time.time();
    print "Linear Time: ", maxSubArray_LinearTime(A); 
    print "     Finished: ", (time.time() - start)*1000000
    return;

   #This for loop is for simulation.
    for i in range(0,0,1):
        print 'working on ', i; 
        A = random.sample(range(-1000,1000),i); 
        #print A; 
        start = time.time();  
        result1 =  findMaximumSubarray(A, 0, len(A)-1);
        elapsed1 = (time.time() - start)*1000000000;  
        

        start = time.time();
        result2 =  maxSubArray_bruteforce(A); 
        elapsed2 =(time.time() - start)*1000000000;  

        print "(", i, ")", elapsed1, ":",  result1, " vs ", elapsed2, ":", result2; 

    #return; 
 
     

if __name__ == "__main__":
    main();