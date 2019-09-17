# -*- coding: utf-8 -*-
# Roy Dolev
# takes values from matrix1 and matrix2 and put the sum of the values in small
# matrix and big matrix.
# small matrix- min num of rows and columns from matrix1 and matrix2
# big matrix- min num of rows and columns from matrix1 and matrix2
    
import numpy as np
def main():
    a1 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]]) # Matrix1
    a2 = np.array([[1,2,3],[3,4,5], [5,6,7],[7,8,9],[9,10,11]]) # Mtrix2
    Small(a1,a2)
    Big(a1,a2)
     

def Small(new1,new2):
#input: two matrix
#output:  print sum matrix of the values that in the min num of rows and
#         columns of both matrix
    a1_t = np.size(new1,1) # num of columns matrix1
    a1_sh = np.size(new1,0) # num of rows matrix1  
    a2_t = np.size(new2,1) # num of columns matrix2
    a2_sh = np.size(new2,0) # num of rows matrix2
    
# target tur-> num min columns(matrix1,matrix2)
# target shura-> num min rows(matrix1,matrix2)
    if a1_t>a2_t:
        target_tur = a2_t
    else:
          target_tur = a1_t
    if a1_sh>a2_sh:
        target_shura = a2_sh
    else:
          target_shura = a1_sh
          
    if a1_sh>target_shura:
        new1 = np.delete(new1,np.s_[target_shura:a1_sh], axis = 0)
        # delete extra rows matrix1
    if a1_t>target_tur:
        new1 = np.delete(new1,np.s_[target_tur:a1_t],axis = 1)
         # delete extra columns matrix1
    
    if a2_sh>target_shura:
        new2 = np.delete(new2,np.s_[target_shura:a2_sh], axis = 0)
         # delete extra rows matrix2
    if a2_t>target_tur:
        new2 = np.delete(new2,np.s_[target_tur:a2_t],axis = 1)
         # delete extra columns matrix1    

    sum_small = np.add(new1,new2)# sum matrix1 and matrix2
    print("sum small: ")
    print (sum_small)

def Big(new1,new2):
#input: two matrix
#output:  print sum matrix of the values that in the max num of rows and
#         columns of both matrix
    a1_t = np.size(new1,1) # num of columns matrix1
    a1_sh = np.size(new1,0) # num of rows matrix1  
    a2_t = np.size(new2,1) # num of columns matrix2
    a2_sh = np.size(new2,0) # num of rows matrix2
    # target tur-> num max columns(matrix1,matrix2)
    # target shura-> num max rows(matrix1,matrix2)
    if a1_t>a2_t:
        target_tur = a1_t
    else:
          target_tur = a2_t
    if a1_sh>a2_sh:
        target_shura = a1_sh
    else:
          target_shura = a2_sh
          
    sum_big = np.zeros((target_shura,target_tur))# biggest matrix all zeros 
    sum_big[:a1_sh,:a1_t]+= new1
    # add numbers from matrix1 to the big matrix (range of matrix1)
    sum_big[:a2_sh,:a2_t]+= new2
    # add numbers from matrix2 to the big matrix (range of matrix2)
    print("sum big: ")
    print (sum_big)

    
if __name__== "__main__":
    main()
  