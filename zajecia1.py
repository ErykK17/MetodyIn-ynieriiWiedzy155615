
import copy

def new_matrix(a,i):#FUNCTION TO FIND THE NEW MATRIXarr = copy.deepcopy(a) 
    arr = copy.deepcopy(a)
    if len(arr) == 2:
        
        return arr
    else:
        arr.pop(0)
        for j in arr:
            j.pop(i)
            
        return arr


def determinant(a):#FUNCTION TO FIND THE DETERMINANT OF A MATRIX
    if len(a) == 1:
        pro = a[0]
        return pro
    elif len(a) == 2:
        pro = a[0][0]*a[1][1] - a[1][0]*a[0][1]
        return pro
        
    else:
        pro = 0
        for i in range(len(a[0])):
            pro += ((-1)**i)*a[0][i]*determinant(new_matrix(a,i))    
        return pro         

macierz = [[1,-1,0,2],[2,1,-3,1],[3,0,0,-2],[-1,2,0,2]]
print(determinant(macierz))