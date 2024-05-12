data = """
#This is a comment

# *************************************************************
# Global variables
# *************************************************************
# unlock int _COUNT = (0 + 2 + 3)@ #Declaration
lock string _Global_var = "This is a global variable."@
# _Global_var = 1@
# lock int _TEN = 10@
# lock float _PI = 3.14@ 
# unlock bool _BINARY = true@
# *************************************************************



# *************************************************************
# Assignment
# *************************************************************
# lock int _Assignment@ #Declaration
# _Assignment = 5+7@ #Assignment
# scribe("hey")@
# scribe("This is _Assignment", _Assignment)@
# scribe("This is Assignment", _Assignment)@
# scribe(_Assignment, _Assignment)@

# lock int _Wrong@ 
# _Wrong = 11@
# *************************************************************

abstract IS_IT_TRUE(bool _X, bool _Y){
  if (_X == _Y){
    scribe("X and Y are equivalent")@

  }else{
    scribe("X and Y are not equivalent")@
  }
}
hail IS_IT_TRUE(true, false)@

# *************************************************************
# Scribe statements
# *************************************************************
# scribe("This is a scribe")@
# scribe(_TEN)@
# scribe("This is an INTEGER", _TEN)@
# scribe(_PI, _TEN)@
# *************************************************************


# *************************************************************
# Attempt and Findout Blocks
# *************************************************************

# attempt{
#     scribe("Trying to access _Global_var in global its scope:", _Global_var)@
#     lock bool _Inside_Attempt = true@
#     scribe("This is _Inside_Attempt", _Inside_Attempt)@
# }
# findout unboundlocalerror{
#     scribe("UnboundLocalError: _Global_var is defined in this scope.")@
# }

# attempt{
#     scribe("Will this be too")@
# }
# findout unboundlocalerror{
#     scribe("This is not going to be printed")@
# }

# *************************************************************
# USE THIS TO TEST THE SCOPE |
#                            V
# *************************************************************
# scribe("This is _Inside_Attempt", _Inside_Attempt)@
# *************************************************************



# *************************************************************
# Abstract Declaration with no parameters
# *************************************************************
# abstract PLUS(){
#     #Declaration within the function
#     lock float _A = 5.5+9@
#     lock float _B = 10.5@
#     lock float _SUM = _A + _B@
#     scribe(_SUM)@
#     scribe("This is A inside the function:", _A)@
# }

# hail PLUS()@

# *************************************************************
# Declareing _A outside the function and with a different type
# *************************************************************
# lock bool _A = true@
# scribe("This is _A is outside the function:", _A)@
# *************************************************************



# *************************************************************
# Abstract Declaration with parameters
# *************************************************************
# abstract MINUS(int _X, int _Y){
#     lock int _Difference = _X - _Y@
#     lock int _III@
#     _III = (7+2)*4@
    
#     scribe("This is the difference",_Difference)@
# }

# lock int _X = 5+1+9@
# lock int _Y = 19-9@
# hail MINUS(_X, _Y)@

#OR
# hail MINUS(3, 2)@

#NOT Supported |
#              V
# hail MINUS(1+1+2, 2+3)@
# *************************************************************

# abstract IS_IT_TRUE(bool _X, bool _Y){
#     scribe("This _X", _X)@
#     scribe("This _Y", _Y)@
# }

# hail IS_IT_TRUE(true, false)@


# *************************************************************
# *************************************************************
# Conditional Statements
# *************************************************************
# IF Statement
# *************************************************************
# if (9 > 10){
#     lock bool _Inside_IF = true@
#     scribe("This is _Inside_IF", _Inside_IF)@
#     scribe("a is greater than b")@
# }

# *************************************************************
# IF_Else statement
# *************************************************************
# if (_TEN > _Wrong){
#     lock bool _Inside_IF = true@
#     scribe("This is _Inside_IF", _Inside_IF)@
#     scribe("10 is greater than 11")@
#     # _TEN = 11@
# } 
# else {
#     lock bool _Inside_ELSE = false@
#     scribe("This is _Inside_ELSE", _Inside_ELSE)@
#     # scribe("This is _Inside_IF", _Inside_IF)@
#     scribe("b is greater than a")@
# }

# *************************************************************
# IF_Elif_Else statement
# *************************************************************
# lock int _Switcher = 3@

# if(_Switcher == 1){ scribe("Switcher is 1")@ }
# elif(_Switcher == 3){ scribe("Switcher is 3")@ }
# else{ scribe("Switcher is not 1, 2, or 3")@ }
# *************************************************************
# For statements
# *************************************************************
# for _I in range(2, 8){
#   scribe("Hello")@
# }
# for _K in "banana"{
#   scribe("w")@
# }
# *************************************************************
# Aslongas statement
# *************************************************************
# aslongas (_COUNT >= 0){
#     _COUNT = (_COUNT - 1)@
#     # scribe(_Count)@
#     lock int _Inside_WHILE = 5@
#     scribe("This is _Inside_WHILE", _Inside_WHILE)@
# }
# scribe(_COUNT)@
# *************************************************************




"""
