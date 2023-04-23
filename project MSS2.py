#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 02:28:27 2022

@author: nd3
"""
import tkinter as tk
import random


window =tk.Tk() # to make a window
window.geometry("500x500") #size of the window
window.title('Find Max sum of SubArray') #the title of the window


"""
//randomized array//
"""     
#Method generates an array with a random size and values  
def randoms():  
    
    f = open("MaxSumSubarray.txt", "w") #creat a file named MaxSumSubarray   
    #size: detrmine a random integer length of the list 
    size= random.randint(0,100)
    #inserting values in the array
    for i in range (0,size):
      #contains random integer valuse from 0 - 100
      #writing each index in the file and seprates them with white space
      f.write(str(random.randint(0, 100))+" ")
    #we should to notify the program that we finished writing by closing the file
    f.close()
    
    f = open("MaxSumSubarray.txt", "r")# we opened the file so we can read the array values
    return f.read().split() #returns the values in an indivsual indexs in a list/array

"""
//Kadane ALGORITHM//
""" 

def kadane(arr):
       
       length= len(arr) # initail a variable contain the length of the array
       cur_sum=0  #consider the current sum is 0
       Max_sum= int(arr[0]) # and the max sum of subarray contains the first index value
       for i in range(0,length): # a for loop start from 0 till the end of length
           cur_sum=cur_sum + int (arr[i]) # update the current sum value 
           if(Max_sum<cur_sum): # compare the max sum with the current sum if the max less than current
               Max_sum=cur_sum #then make the value of the max sum be the value of the current sum
           if(cur_sum<0):# if the value of the current sum less than 0
               cur_sum=0#then make it equal to zero      
       return Max_sum # return the max sum

""" 
//Brute force I ALGORITHM//
"""
def BruteForceApproach1(Array):    
     max_sum = 0 
     for i in range (0,len(Array)): # first for loop to determine the starting point of the sub-array
          for j in range (i, len(Array)): # second for the for loop to determine the end point of the sub-array
              Sum = 0 
              for k in range (i, j+1): # the last for loop to compute the sum between the starting point and ending point
                   Sum = Sum + int(Array[k])
                   if(Sum > max_sum): # if statement to compare the outputs to get the largest value
                       max_sum = Sum  # if Sum larger than max_sum then give the value in Sum to max_sum                        
     return max_sum # return the largest value
 
""" 
//Brute force II ALGORITHM//
"""
def Brute_forceII(arr):
  max_sum = 0 # The max sum of subarray contains the first element value
  for i in range(0, len(arr)): # The outer loop picks the beginning element of the array
    sum = 0 # Consider the sum is 0
    for j in range(i, len(arr)): # The inner loop finds the maximum sum with the first element picked by the outer loop 
      sum = sum + int(arr[j]) # Udate the sum value 
      max_sum = max(sum, max_sum) # Compare the resulting sum with the existing maximum value
  return max_sum # Return the MAX sum

"""
//Auxiliary array ALGORITHM//
"""
def Aux_array(A):
    
      #max_ending: creatin an empty array to store the sum of the subarrays
      max_ending= [] 
      #adding the first element of the recomanded array into the max_ending array
      max_ending.insert(0,int(A[0]))
      
      #the loop will take each element in A and max_ending arrays
      for i in range( 1 , len(A)):
         #sum_arr: contains the sum of each subarray taken
         sum_arr = int (A[i]) + max_ending[i-1] 
         #check if the value of summation is valid it will be stored in max_ending array
         if ( sum_arr > 0 ):
            max_ending.insert(i, sum_arr)
         #if the value of sum_arr is not valid, then the currten element of A[i] will be added into max_ending[i] with the same index
         else:
            max_ending.insert(i, int(A[i]))
      #max_sum: creating a varible with an intial value 0
      max_sum= 0
      #passing on each element in max_ending to detrimane the max sum of A subarrays
      for i in range ( 0 , len(A)):
         #compre each elements to store the value in max_sum 
         max_sum = max(max_sum, int(max_ending[i]))
         
      return max_sum
 
    
"""
//Porogram results//
""" 
#method result: giving the result of all "Max sum subarray" Algorthims
def results():
    
    arr= randoms()#stores the randomaize array, so all algorithms have the same array.
    
    #resultlb1: stores the lable of an informal masseage about kadane(randoms()) value
    resultlb1 = tk.Label(window,text= "the Maximum Sum of the Subarrays is: "+ str(kadane(arr)) +"        ", font="Courier 12 bold")
    resultlb1.place(x=35, y= 120) #to make the lable visable in the window

    #resultlb2: stores the lable of an informal masseage about BruteForceApproach1(randoms()) value
    resultlb2 = tk.Label(window,text= "the Maximum Sum of the Subarrays is: "+ str(BruteForceApproach1(arr)) +"         ", font="Courier 12 bold")
    resultlb2.place(x=35, y= 210) #to make the lable visable in the window
    
    #resultlb3: stores the lable of an informal masseage about Brute force II(randoms()) value
    resultlb3 = tk.Label(window,text= "the Maximum Sum of the Subarrays is: "+ str(Brute_forceII(arr)) +"        ", font="Courier 12 bold")
    resultlb3.place(x=35, y= 290) #to make the lable visable in the window
    
    #resultlb4: stores the lable of an informal masseage about Aux_array(randoms()) value
    resultlb4 = tk.Label(window,text= "the Maximum Sum of the Subarrays is: "+ str(Aux_array(arr)) + "         ", font="Courier 12 bold")
    resultlb4.place(x=35, y= 370) #to make the lable visable in the window   

    

"""
//MANU WINDOW//
""" 
#-- making a hello text --
my_font1=('times', 18, 'bold') # font style declaring
my_font2 =('Helvetica', 12, 'bold')
l3 = tk.Label(window,  text='Welcome To Our Program ', width=33,font=my_font1,
              fg='white',bg='pink4')

#-- make Labels --
lbl1=tk.Label(text='1- Kadane Algorithm      ',font=('Courier',15),bg='LavenderBlush2')
lbl2=tk.Label(text='2- Brute Force approch I ',font=('Courier',15),bg='LavenderBlush2') # to make a label and change the size of the label
lbl3=tk.Label(text='3- Brute Force approch II',font=('Courier',15),bg='LavenderBlush2') 
lbl4=tk.Label(text='4- Auxiliary array       ',font=('Courier',15),bg='LavenderBlush2') 

#-- make Button --
#lbl5: a Button shows the Max sum subarray Algorithm's result by clicking it.
lbl5=tk.Button(text='results',font=('Courier',15),bg='LavenderBlush2', command= results) 


# to add label and button in window
l3.pack(pady= 10)
lbl1.place(x=90, y= 75)
lbl2.place(x=90, y= 160) 
lbl3.place(x=90, y= 250) 
lbl4.place(x=90, y= 330) 
lbl5.place(x=10, y= 430) 

window.mainloop() # listen to user action
    