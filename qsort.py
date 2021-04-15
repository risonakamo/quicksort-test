from typing import List

# bootstrap qsort
def qsort1(array:List[int])->List[int]:
    return qsort(array,0,len(array)-1)

# the qsort
def qsort(array:List[int],start:int,end:int)->List[int]:
    if not start<end:
        return array

    initialPivot:int=array[start]
    newPivot:int=partition(array,initialPivot,start,end)

    qsort(array,start,newPivot-1)
    qsort(array,newPivot+1,end)

    print(array)
    return array

# perform partition operation. mutates array and returns the new pivot index
def partition(array:List[int],pivot:int,start:int,end:int)->int:
    p:int=start
    for x in range(start,end+1):
        if array[x]<pivot:
            swap(array,p,x)
            p+=1

    return p

# mutating swap of array
def swap(array:List[int],index1:int,index2:int)->List[int]:
    temp:int=array[index1]
    array[index1]=array[index2]
    array[index2]=temp
    return array

if __name__=="__main__":
    example:List[int]=[4,3,7,2,9,1,8,8,5]
    qsort1(example)