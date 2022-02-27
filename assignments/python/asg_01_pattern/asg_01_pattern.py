'''
----------------------------------------------------------------------------
asg_01_pattern.py

Python program to show various loop based number or character patterns
with variying complexity of addition or substraction increments

DataScience Course Assignment

Date     : 19 Jan 2022
Author   : SYLVESTER THOMAS
Copyright: SYLVESTER THOMAS (c) 2022-TillDate
Version  : 2.0

ps: utilizing function pointers :-) for code optimization
do not change function names. 
Exception handler will detect Method NOT FOUND and continue

ToDo:

------------------------------------------------------------------------------
'''

import datetime
def asg_1_1():
	cChar = "5"
	for i in range(5,0,-1):
		print(' '+(cChar+' ') * i)

def asg_1_2():
	for x in range(6,1,-1):
		for y in range(0,x):
			print(' '+str(y), end='')
		print("")

def asg_1_3():
	n=0
	for x in range(1,10,2):
		n+=1
		print(' '+(str(x)+' ')*n)

def asg_1_4():
	for i in range(1,6):
		for j in range(i,0,-1):
			print( " "+str(j), end=" ")
		print("")

def asg_1_5():
	incr=2
	i = 1
	while i < 11:
		for j in range(i,(i-(incr-1)),-1):
			print(" "+str(j),end=' ')
		print("")
		i=i+incr
		incr+=1
	# ugly! there surely must be a better way - but 2am my covid brain is ???? 

def asg_1_6():
	mR=7
	mC=7
	mB = [[1 for columns in range(mC)] for rows in range(mR)]
	for i in range(2,mR):
		for j in range(1,i):
			if(i > 1):
				if( j != 0 ):
					mB[i][j]=(mB[i-1][j-1]+mB[i-1][j])
	for i in range(0,mR):
		for j in range(0,i+1):
			print(" ",mB[i][j],end="")
		print("")
	print("")
	# oh maan.... multi dimensional list creation was !! :(

def asg_1_7():
	for i in range(1,6):
		for j in range(1,6):
			if( j < i ):
				print(" "+str(i),end=" ")
			else:
				print(" "+str(j),end=" ")
		print("")
	# simple logic, unnecessarily took long

def asg_1_8():
	for i in range(1,9):
		for j in range(i,((i*i)+1),i):
			print(" "+str(j),end=" ")
		print("")

def asg_1_9():
	iL=6
	for i in range(iL,0,-1):
		print( (" "*10+("* " * i).center(iL*2)))

def asg_1_10():
	iL=8
	for i in range(iL):
		print( (" "*10+(" * " * i).center(iL*3)))
	
def asg_1_11():
	for i in range(7):
		print(" *"*i)
	print("")
	for i in range(6,0,-1):
		print(" *"*i)

def asg_1_12():
	for i in range(5):
		print(" *"*i)
	for i in range(5,0,-1):
		print(" *"*i)

def asg_1_13():
	for i in range(5):
		print(" "*(5-i)*2+" *"*i)
	for i in range(5,0,-1):
		print(" "*(5-i)*2+" *"*i)

def asg_1_14():
	iL=5
	for i in range(iL,0,-1):
		print( (" *" * i).center(iL*2))

def asg_1_15():
	iL=6
	for i in range(iL):
		print( (" *" * i).center(iL*2))

def asg_1_15():
	incr=0
	for i in range(7,0,-1):
		print(" "+"*" * i+"_"*incr+"*" * i)
		incr+=2


#------------------------ [ Helper Functions ] --------------------------------

def dispAsgHdr(subC):
	print("\n","-"*20," [  Assignment 1 - "+str(subC)," ] ","-"*20+"\n")

def showUsage():
	dt = datetime.datetime.now()
	uL=75
	print( uL*'-')
	print( "asg_01_patterns.py  - Version 2.0  9.Feb.2022 ")
	print( "Assignment 01 (15) - Sylvester Thomas")
	#print( "2022 - {0}".format(dt.year))
	print( "Dynamic function references are generated and executed" )
	print( uL*'-')

#------------------------------- [ Main ] --------------------------------------

def main():

	iTotAsg = 15
	print("\n","-"*22,"  Assignment 1 - Patterns  ","-"*22)
	showUsage()

	for i in range(1,iTotAsg+1):
		try:
			dispAsgHdr(i)
			fPtr = ("asg_1_"+str(i))
			globals()[fPtr]()
		except KeyError:
			print ("*"*20, "   Method ",fPtr," is NOT FOUND")

		#	except Exception as e:
		#		print(e)

if __name__ == "__main__":
	main()

"""
Actual output from this program

 --------------------   Assignment 1 - Patterns   --------------------
---------------------------------------------------------------------------
Assignment 01 - Sylvester Thomas 08-Feb-2022
This is work in progress - the rest will be completed tomorrow
---------------------------------------------------------------------------

 --------------------  [  Assignment 1 - 1  ]  --------------------

 5 5 5 5 5 
 5 5 5 5 
 5 5 5 
 5 5 
 5 

 --------------------  [  Assignment 1 - 2  ]  --------------------

 0 1 2 3 4 5
 0 1 2 3 4
 0 1 2 3
 0 1 2
 0 1

 --------------------  [  Assignment 1 - 3  ]  --------------------

 1 
 3 3 
 5 5 5 
 7 7 7 7 
 9 9 9 9 9 

 --------------------  [  Assignment 1 - 4  ]  --------------------

 1 
 2  1 
 3  2  1 
 4  3  2  1 
 5  4  3  2  1 

 --------------------  [  Assignment 1 - 5  ]  --------------------

 1 
 3  2 
 6  5  4 
 10  9  8  7 

 --------------------  [  Assignment 1 - 6  ]  --------------------

  1
  1  1
  1  2  1
  1  3  3  1
  1  4  6  4  1
  1  5  10  10  5  1
  1  6  15  20  15  6  1


 --------------------  [  Assignment 1 - 7  ]  --------------------

 1  2  3  4  5 
 2  2  3  4  5 
 3  3  3  4  5 
 4  4  4  4  5 
 5  5  5  5  5 

 --------------------  [  Assignment 1 - 8  ]  --------------------

 1 
 2  4 
 3  6  9 
 4  8  12  16 
 5  10  15  20  25 
 6  12  18  24  30  36 
 7  14  21  28  35  42  49 
 8  16  24  32  40  48  56  64 

 --------------------  [  Assignment 1 - 9  ]  --------------------

          * * * * * * 
           * * * * *  
            * * * *   
             * * *    
              * *     
               *      

 --------------------  [  Assignment 1 - 10  ]  --------------------

                                  
                     *            
                    *  *          
                  *  *  *         
                 *  *  *  *       
               *  *  *  *  *      
              *  *  *  *  *  *    
            *  *  *  *  *  *  *   

 --------------------  [  Assignment 1 - 11  ]  --------------------


 *
 * *
 * * *
 * * * *
 * * * * *
 * * * * * *

 * * * * * *
 * * * * *
 * * * *
 * * *
 * *
 *

 --------------------  [  Assignment 1 - 12  ]  --------------------


 *
 * *
 * * *
 * * * *
 * * * * *
 * * * *
 * * *
 * *
 *

 --------------------  [  Assignment 1 - 13  ]  --------------------

          
         *
       * *
     * * *
   * * * *
 * * * * *
   * * * *
     * * *
       * *
         *

 --------------------  [  Assignment 1 - 14  ]  --------------------

 * * * * *
  * * * * 
   * * *  
    * *   
     *    

 --------------------  [  Assignment 1 - 15  ]  --------------------

 **************
 ******__******
 *****____*****
 ****______****
 ***________***
 **__________**
 *____________*


"""

# End of asg_01_pattern.py
