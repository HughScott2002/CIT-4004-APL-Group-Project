data = """
#This is a comment

# *************************************************************
# Global variables
# *************************************************************
unlock int _COUNT = (0 + 2 + 3)@ #Declaration
lock string _Global_var = "This is a global variable."@
lock int _TEN = 10@
lock float _PI = 3.14@ 
unlock bool _BINARY = true@
# *************************************************************



# *************************************************************
# Assignment
# *************************************************************
lock int _Assignment@ #Declaration
_Assignment = 5+7@ #Assignment
scribe("hey")@
scribe("This is _Assignment", _Assignment)@
scribe("This is Assignment", _Assignment)@
scribe(_Assignment, _Assignment)@

lock int _Wrong@ 
_Wrong = 11@
# *************************************************************



# *************************************************************
# Scribe statement
# *************************************************************
# scribe("This is a scribe")@
# scribe(_TEN)@
# scribe("This is an INTEGER", _TEN)@
# scribe(_PI, _TEN)@
# scribe("This is an INTEGER", _TEN)@
# scribe("My name is {name} and I am {age} years old.")@ #TODO: Fix this
# scribe(_PII, _TEN)@
# *************************************************************


# *************************************************************
# Attempt and Findout Blocks
# *************************************************************

attempt{
    scribe("Trying to access _Global_var in global its scope:", _Global_var)@
    lock bool _Inside_Attempt = true@
    scribe("This is _Inside_Attempt", _Inside_Attempt)@
}
findout unboundlocalerror{
    scribe("UnboundLocalError: _Global_var is defined in this scope.")@
}
attempt{
    scribe("Will this be too")@
}
findout unboundlocalerror{
    scribe("This is not going to be printed")@
}

# scribe("This is _Inside_Attempt", _Inside_Attempt)@
# *************************************************************



# *************************************************************
# Abstract Declaration with no parameters
# *************************************************************
abstract PLUS(){
    #Declaration within the function
    lock float _A = 5.5+9@
    lock float _B = 10.5@
    lock float _SUM = _A + _B@
    scribe(_SUM)@
    scribe("This is A inside the function:", _A)@
}

# Try and call the function
hail PLUS()@

# Declareing _A outside the function and with a different type
# hail PLUS()@
lock bool _A = true@


#Try and use a variable that is not defined globally but was defined in the function
scribe("This is _A is outside the function:", _A)@
# *************************************************************



# *************************************************************
# Abstract Declaration with parameters
# *************************************************************
abstract MINUS(int _X, int _Y){
    lock int _Difference = _X - _Y@
    lock int _III@
    _III = (7+2)*4@
    
    scribe("This is the difference",_Difference)@
}

# Try and call the function
hail MINUS(1+1+2, 2+3)@
# hail MINUS(1+1+2, 7-8)@
lock int _X = 5@
lock int _Y = 19@
hail MINUS(_X, _Y)@


# abstract IS_IT_TRUE(bool _X, bool _Y){
    
#     scribe("This _X", _X)@
#     scribe("This _Y", _Y)@
# }


# hail IS_IT_TRUE(true, false)@


#Try and use a variable that is not defined globally but was defined in the function
# scribe(_A)@
# *************************************************************
# *************************************************************
# Conditional Statements
# *************************************************************
#IF Statement
# *************************************************************
# If statement
# if (9 > 10){
#     lock bool _Inside_IF = true@
#     scribe("This is _Inside_IF", _Inside_IF)@
#     scribe("a is greater than b")@
# }
# scribe("This is _Inside_IF", _Inside_IF)@
# *************************************************************
# IF_Elif statement
# *************************************************************
if (_TEN < _Wrong){
    lock bool _Inside_IF = true@
    scribe("This is _Inside_IF", _Inside_IF)@
    scribe("10 is greater than 11")@
} 
else {
    lock bool _Inside_ELSE = false@
    scribe("This is _Inside_ELSE", _Inside_ELSE)@
    # scribe("This is _Inside_IF", _Inside_IF)@
    scribe("b is greater than a")@
}
# scribe("This is _Inside_ELSE", _Inside_ELSE)@
# scribe("This is _Inside_IF", _Inside_IF)@
# *************************************************************
# IF_Elif_Else statement
# *************************************************************
lock int _Switcher = 3@
# TODO: Fix the if statement
if(_Switcher == 1){ scribe("Switcher is 1")@ }
elif(_Switcher == 3){ scribe("Switcher is 3")@ }
else{ scribe("Switcher is not 1, 2, or 3")@ }
# *************************************************************
# For statements
# *************************************************************
for _I in range(2, 8){
  scribe("wssw")@
}
for _K in "banana"{
  scribe("w")@
}
# *************************************************************
# Aslongas statement
# *************************************************************
aslongas (_COUNT >= 0){
    scribe("count")@
    _COUNT = (_COUNT + 1)@
    lock int _Inside_WHILE = 5@
    scribe("This is _Inside_WHILE", _Inside_WHILE)@
}
# scribe(_COUNT)@
# # scribe("This is _Inside_WHILE", _Inside_WHILE)@
# aslongas _COUNT >= 0{
#     scribe("1 times 2 is less than 3")@
# }
# *************************************************************



# *************************************************************
# Abstract Declaration with parameters and nested functions with attempt and findout blocks
# *************************************************************

abstract OUTER_FUNCTION(int _TEN, float _PI, bool _BINARY){
    # Enclosing variable
    lock string _Enclosing_var = "This is an enclosing variable."@

    scribe("INTEGER", _TEN)@
    scribe("FLOAT", _PI)@
    scribe("BOOLEAN", _BINARY)@

    abstract INNER_FUNCTION(){
        # Local variable
        lock string _Local_var = "This is a local variable."@

        # Accessing variables from different scopes
        scribe("Inside INNER_FUNCTION:")@
        scribe("Local variable:", _Local_var)@
        scribe("Enclosing variable:", _Enclosing_var)@
        scribe("Global variable:", _Global_var)@
    }
    # hail will Call the inner function
    hail INNER_FUNCTION()@

    # Trying to access the local variable outside its scope
    # This will raise an UnboundLocalError
    # attempt{
    #     scribe("Trying to access _Local_var outside its scope:", _Local_var)@
    # }
    # findout unboundlocalerror{
    #     scribe("UnboundLocalError: _Local_var is not defined in this scope.")@
    # }
}
# hail will call the outer function
hail OUTER_FUNCTION(_TEN, _PI, _BINARY)@
# *************************************************************


"""
