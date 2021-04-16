from pprint import pprint
from math import floor
from numpy.random import randint

from typing import List,TypeVar,Callable
from typing_extensions import TypedDict

T=TypeVar("T")
Comparator=Callable[[T,T],int]

def qsort1(array:List[T],comparator:Callable[[T,T],int],partial:int=0)->List[T]:
    """bootstrap qsort"""
    return qsort(array,comparator,0,len(array)-1,partial)

def qsort(array:List[T],comparator:Comparator,start:int,end:int,partial:int)->List[T]:
    """the qsort"""
    if not start<end:
        return array

    medOfThree(array,comparator,start,end)
    newPivot:int=partition(array,comparator,start,end)

    qsort(array,comparator,start,newPivot-1,partial)

    if partial<=0 or newPivot<partial-1:
        qsort(array,comparator,newPivot+1,end,partial)

    return array

def partition(array:List,comparator:Comparator,start:int,end:int)->int:
    """perform partition operation. mutates array and returns the new pivot index"""
    pivot:T=array[end]
    p:int=start
    for x in range(start,end+1):
        if comparator(array[x],pivot)<0:
            swap(array,p,x)
            p+=1

    swap(array,p,end)
    return p

def swap(array:List[T],index1:int,index2:int)->List[T]:
    """mutating swap of array"""
    temp:T=array[index1]
    array[index1]=array[index2]
    array[index2]=temp
    return array

def medOfThree(array:List[T],comparator:Comparator,start:int,end:int)->List[T]:
    """performs medium of three, placing the new pivot in array[end]"""
    mid:int=floor((start+end)/2)

    if comparator(array[mid],array[start])<0:
        swap(array,start,mid)
    if comparator(array[end],array[start])<0:
        swap(array,end,start)
    if comparator(array[mid],array[end])<0:
        swap(array,mid,end)

    return array

if __name__=="__main__":
    class TestThing(TypedDict):
        data:str
        val:int

    def thingCompare(a:TestThing,b:TestThing)->int:
        """comparator function should return:
        >0 (+1): if a>b
        0: if a==b
        <0 (-1): if a<b
        """
        return a["val"]-b["val"]

    example:List[int]=[4,3,7,2,9,1,8,8,5]
    example2:List[int]=[1,2,3,4]
    example3:List[int]=[4,1,3,2]
    example4:List[int]=randint(0,100,20)

    def convertToThingList(array:List[int])->List[TestThing]:
        def convertToThing(num:int)->TestThing:
            return {
                "data":f"thing {num}",
                "val":num
            }

        return [convertToThing(x) for x in array]

    pprint(qsort1(convertToThingList(example),thingCompare))
    print()
    pprint(qsort1(convertToThingList(example2),thingCompare))
    print()
    pprint(qsort1(convertToThingList(example3),thingCompare))
    print()
    pprint(qsort1(convertToThingList(example4),thingCompare,3))