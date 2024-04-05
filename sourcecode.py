data = """
#This is a comment

# *************************************************************
# Global variables
# *************************************************************
unlock int _COUNT = (0 + 2 - 3)@ #Declaration
lock string _Global_var = "This is a global variable."@
lock int _TEN = 10@
lock float _PI = 3.14@ 
unlock bool _BINARY = true@
# *************************************************************



# *************************************************************
# Assignment
# *************************************************************
lock int _Assignment@ #Declaration
_Assignment = 5+5@ #Assignment
# *************************************************************



# *************************************************************
# Scribe statement
# *************************************************************
scribe("This is a scribe")@
scribe(_TEN)@
scribe("This is an INTEGER", _TEN)@
scribe(_PI, _TEN)@
scribe("This is an INTEGER", _TEN)@
scribe("My name is {name} and I am {age} years old.")@
# scribe(_PII, _TEN)@
# *************************************************************


# *************************************************************
# Attempt and Findout Blocks
# *************************************************************

attempt{
    scribe("Trying to access _Global_var in global its scope:", _Global_var)@
}
findout unboundlocalerror{
    scribe("UnboundLocalError: _Global_var is defined in this scope.")@
}
# *************************************************************



# *************************************************************
# Abstract Declaration with no parameters
# *************************************************************
# abstract PLUS(){
#     #Declaration within the function
#     lock float _A = 5.5@
#     lock float _B = 10.5@
#     lock float _SUM = _A + _B@
#     scribe(_SUM)@
#     scribe("This is A inside the function:", _A)@
# }

# Try and call the function
# hail PLUS()@

# Declareing _A outside the function and with a different type
# lock bool _A = true@

#Try and use a variable that is not defined globally but was defined in the function
# scribe("This is _A is outside the function:", _A)@
# *************************************************************



# *************************************************************
# Abstract Declaration with parameters
# *************************************************************
# abstract MINUS(int _X, int _Y){
#     lock int _Difference = _X - _Y@
#     scribe("This is the difference",_Difference)@
# }

# Try and call the function
# hail MINUS(1+1+2, 2+3)@
# hail MINUS(1+1+2, 7-8)@
# lock int _X = 5@
# lock int _Y = 19@
# hail MINUS(_X, _Y)@


abstract IS_IT_TRUE(bool _X, bool _Y){
    
    scribe("This _X", _X)@
    scribe("This _Y", _Y)@
}


hail IS_IT_TRUE(true, false)@


#Try and use a variable that is not defined globally but was defined in the function
# scribe(_A)@

# *************************************************************


# *************************************************************

# *************************************************************

# abstract OUTER_FUNCTION(int _TEN, float _PI, bool _BINARY){
#     # Enclosing variable
#     lock string _Enclosing_var = "This is an enclosing variable."@

#     scribe("INTEGER", _TEN)@
#     scribe("FLOAT", _PI)@
#     scribe("BOOLEAN", _BINARY)@

#     abstract INNER_FUNCTION(){
#         # Local variable
#         lock string _Local_var = "This is a local variable."@

#         # Accessing variables from different scopes
#         scribe("Inside INNER_FUNCTION:")@
#         scribe("Local variable:", _Local_var)@
#         scribe("Enclosing variable:", _Enclosing_var)@
#         scribe("Global variable:", _Global_var)@
#     }
#     # hail will Call the inner function
#     hail INNER_FUNCTION()@

#     # Trying to access the local variable outside its scope
#     # This will raise an UnboundLocalError
#     attempt{
#         scribe("Trying to access _Local_var outside its scope:", _Local_var)@
#     }
#     findout unboundlocalerror{
#         scribe("UnboundLocalError: _Local_var is not defined in this scope.")@
#     }
# }
# hail will call the outer function
# hail OUTER_FUNCTION()@
# *************************************************************

# Function with a loop
# abstract IS_B_GREATER_THAN_A(int _B, int _A){
#     if _B > _A{
#         scribe("b is greater than a")@
#     }
#     elif _B > _A{
#         scribe("a and b are equal")@
#     }
#     else{
#         scribe("a is greater than b")@
#     }
# }

# lock int _B@ 
# _B= 5@
# lock int _A@
# _A= 10@
# Calling the IS_B_GREATER_THAN_A function
# hail IS_B_GREATER_THAN_A(_B, _A)@

# aslongas true{
#      scribe("Count:", _COUNT)@
# }
"""
