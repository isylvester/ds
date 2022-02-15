'''
----------------------------------------------------------------------------
asg_01_password_validator.py

A simple Python program to Input and Validate a password String
ps:Regular Expression (regex) NOT to be Used

DataScience Course Assignment

Date: 19 Jan 2022
Author: SYLVESTER THOMAS
Copyright: SYLVESTER THOMAS

----------------------------------------------------------------------------
'''

minLen = 6
maxLen = 15
sc = "!@#$%^&*()-+,._=~"

def checkUCA( pS ):
 return any(c.isupper() for c in pS )

def checkLCA( pS ):
 return any(c.islower() for c in pS )

def checkD( pS ):
 return any(c.isdigit() for c in pS )

def checkSC( pS, pSC ):
 for c in pSC:
  if c in pS:
   return True

 return False

def validatePW( pw ):
 pwIV = 0

 print("\nThank you, your pw is: ",pw )

 if( len(pw) >= minLen and len(pw) <= maxLen ):
  pwIV=pwIV+1
  print( " Length is {0} characters". format(len(pw)))
 else:
  print( " Length is {0} characters, should be Min:{1} Max:{2} ".format(len(pw), minLen, maxLen) )

 if( checkUCA(pw) ):
  pwIV=pwIV+1
  print( " Contains UPPER Case alphabet")
 else:
  print( " Does NOT Contain UPPER Case alphabet" )

 if( checkLCA(pw) ):
  pwIV=pwIV+1
  print( " Contains LOWER Case alphabet")
 else:
  print( " Does NOT Contain LOWER Case alphabet" )

 if( checkD(pw) ):
  pwIV=pwIV+1
  print( " Contains NUMBER")
 else:
  print( " Does NOT Contain NUMBER" )

 if( checkSC(pw, sc) ):
  pwIV=pwIV+1
  print( " Contains SPECIAL character")
 else:
  print( " Does NOT Contain SPECIAL character" )
 print("\n")

 return pwIV

def showUsage():
 print( "The password length should be Min: {minLen} and Max {maxLen} characters")
 print(  "The password should contain atleast:")
 print(  " 1 UPPER Case alphabet")
 print(  " 1 LOWER Case alphabet")
 print(  " 1 NUMERIC value, between 0 and 9")
 print( " 1 SPECIAL character ({sc})")
 print("\n")

#------------------------------  main -----

showUsage()

pwVC = 0
while( pwVC != 5 ):

 pw = input(' Please enter your password >>> ')
 
 pwVC = validatePW( pw )

print( "\nCongratulations!! Your password {pw} is Valid\n")
