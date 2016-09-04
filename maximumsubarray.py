import numpy as np;  

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

def main():
    A = [-1, 4, 4, 3, -4, 0];
    print A; 
    print findMaximumSubarray(A, 0, len(A)-1);

    print maxSubArray_bruteforce(A); 

    return; 

    A = [-2, -5, 6, -2, -3, 1, 5, -6, 0];
    print A; 
    print findMaximumSubarray(A, 0, len(A)-1);

    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7, 0] ;
    print A; 
    print findMaximumSubarray(A, 0, len(A)-1);

     

if __name__ == "__main__":
    main();