# python3
import threading
from sys import maxsize
class BinaryHeap:
  def __init__(self):
    self.heap = [] # for storing the element of the heap
    self.length # length of the heap
    
  # for giving the parent index of the given index
  def parent(self, i):
    return (i-1)//2
  
  #left children
  def leftChild(self, i):
    return i*2 + 1
  
  # right child 
  def rightChild(self, i):
    return i*2 + 2
  
  #shiftUp method
  def shiftUp(self, i):
    #check whether the i is greater r not
    #then parent is less or not ten swap
    while(i>0 and (self.heap[self.parent(i)] < self.heap[i])):
      #swap
      self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
      # now make the i as the parent of i 
      i = self.parent(i)
      
  # shiftDown method
  def shiftDown(self, i):
    maxIndex = i# assign i as the maxIndex 
    
    left = self.leftChild(i)# get the left child of the i
    # now compare where the left index is greater then the heap length
    # compare whether heap at left is greater or not
    if left<self.length and self.heap[left] > self.heap[maxIndex]:
      maxIndex = left
      
    right = self.rightChild(i)
    # again check length and then the value at rigght index with maxIndex in heap
    if right<self.length and self.heap[right] > self.heap[maxIndex]:
      maxIndex = right
      
    # now check the i and maxIndex
    if maxIndex!=i:
      #swap
      self.heap[maxIndex], self.heap[i] = self.heap[i], self.heap[maxIndex]
      
      #now again call shiftDown
      self.shiftDown(maxIndex)
      
  # insert new element
  def insert(self, key):
    self.heap.append(key)# append at the end of the binary tree
    self.length+=1 # increase the length of the heap
    
    #call the shift up function to compare andbalance the heap
    self.shiftUp(self.length-1)
    
    return
  
  # extractMax
  def extractMax(self):
    if self.length==0:
      return None
    else:
      # get the first element
      ret = self.heap[0]
      
      #now at the place of the 0th index have the last index
      self.heap[0] = self.heap[-1]
      
      # now delete the last element from the heap
      self.heap.pop()
      
      # decrease the length
      self.length-=1
      
      #call the shiftDown for the balance of the bnary heap tree if after deleting last the tree is not empty
      if self.length!=0:
        self.shiftDown(0)
      
      return ret # return the first that is max 
    
  # remove the element at the particular index
  def remove(self, i):
    # if length is 0 index i is greater or equal to length then return
    if self.length==0 or i>=self.length:
      return
    else:
      # now change the value of the heap[i] to infinity that is maxsize+1
      self.heap[i] = maxsize+1
      # now update the shiftUp
      self.shiftUp(i)
      
      # now change it with  the last element and delete the last element and do shiftDown
      self.heap[0] = self.heap[-1]
      
      self.heap.pop()# pop the last eleemnt
      self.length-=1
      self.shiftDown(0)
      
      return
  #change Priority  
  def changePriority(self, *args):
    i = args[0][0]
    newKey = args[0][1]
    if self.length==0 or i>=self.length:
      return
    # having the old data
    oldKey = self.heap[i]
    
    #change the dataa
    self.heap[i] = newKey
    
    # now check whether it is greater or less
    if oldKey > newKey:
      self.shiftDown(i)# if newKey is less then surely we have to check whether it s greater then t's child or not
    else:
      self.shiftUp(i)# if greater then check with bthe parent
      
    return
  
  # get the max key
  def getMax(self):
    return self.heap[0] if self.length>=1 else None
    
    
      
def main():
  heap = BinaryHeap()
  while(True):
    print('1 --> add new key')
    print('2 --> extract max')
    print('3 --> get max')
    print('4 --> remove element at index')
    print('5 --> change priority')
    print('6 --> print heap')
    print('0 --> EXIT')
    
    userInput = int(input('select from the above -->\t'))
    
    if userInput == 1:
      heap.insert(int(input('key to be inserted --> \t')))
    elif userInput == 2:
      print(heap.extractMax())
    elif userInput==3:
      print(heap.getMax())
    elif userInput == 4:
      heap.remove(int(input('index to be deleted --> \t')))
    elif userInput == 5:
      heap.changePriority([int(x) for x in input('index key').split()])
    elif userInput == 6:
      print(*heap.heap, sep='\t')
    elif userInput==7:
      break
    else:
      print('chosse correctly!!!')
threading.Thread(target=main).start()
