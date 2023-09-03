"""
You are given four points A,B,C  and D in a 3-dimensional Cartesian coordinate system. 
You are required to print the angle between the plane made by the points A,B,C and B,C,D in degrees(not radians). 
Let the angle be PHI.
Cos(PHI) = (X.Y)/|X||Y| where X = AB x BC and Y = BC x CD.
Here, X.Y means the dot product of X and Y, and AB x BC means the cross product of vectors AB and BC.
Also, AB=B-A .

Input Format
One line of input containing the space separated floating number values of the X,Y and Z coordinates of a point.
"""
import math

def dotProduct(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])
if __name__ =='__main__':
    A = list(map(float, input().split()))
    B = list(map(float, input().split()))
    C = list(map(float, input().split()))
    D = list(map(float, input().split()))
    
    AB = [B[i]-A[i] for i in range(len(A))]
    BC = [C[i]-B[i] for i in range(len(B))]
    CD = [D[i]-C[i] for i in range(len(C))]
    
    X = [AB[1]*BC[2]-AB[2]*BC[1], AB[2]*BC[0]-AB[0]*BC[2], AB[0]*BC[1]-AB[1]*BC[0]]
    Y = [BC[1]*CD[2]-BC[2]*CD[1], BC[2]*CD[0]-BC[0]*CD[2], BC[0]*CD[1]-BC[1]*CD[0]]
    
    print("%.2f" %(math.degrees(math.acos(dotProduct(X, Y)/(math.sqrt(dotProduct(X, X))*math.sqrt(dotProduct(Y, Y)))))))