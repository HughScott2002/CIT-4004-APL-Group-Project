data = """
# Testing the declaration of variables
unlock int _COUNT = 4@
# lock string _Global_var = "This is a global variable."@
lock int _TEN = 10@

# Testing declaration of variables without assignment
# lock string _This_String@
# _This_String = "This is a string."@


# Testing the mutex declaration
# lock float _PI = 3.14@ 
unlock bool _BINARY = true@
#_PI = 3.15@
#_BINARY = false@
#_BINARY = true@

lock int _Wrong@ 
_Wrong = 11@

# lock int _Sum = _TEN + _Wrong@
# lock int _SUMMER = 1 + 2@

#Testing the print statement
#scribe("This is a comment.", _Wrong)@
#_Wrong = 121@
#  attempt{
#      scribe("This is a try block.")@
#     #  _BINARY = false@
# }
# findout unboundlocalerror{
#    scribe("UnboundLocalError: _Local_var is not defined in this scope.")@
# }
# abstract IS_B_GREATER_THAN_A(bool _X, int _Y){
#    # this _X should be passed as a parameter and used in the function
#    scribe(_X)@
#    #This should be local to IS_B_GREATER_THAN_A
#    lock bool _Inside_Abstract = true@   
# }

# hail IS_B_GREATER_THAN_A(_BINARY,_Wrong)@


#Testing the arithmetic operations
# lock int _B@
# _B = 5@
# lock int _A = 5+_B@
# lock int _EQQ  = 8.8@


#Testing the True and False
# lock bool _TEST = !true+9@
# lock bool _TEST = !true@

#Testing Equavalence
# lock bool _TEST = 00 == 1@
# lock bool _TEST = 1 == 1@


#Testing Comparisons
# lock bool _TEST1 = 1 > 1@
# lock bool _TEST2 = 1 < 2@
# lock bool _TEST3 = 1 != 2@
# lock bool _TEST4 = 1 <= 2@
# lock bool _TEST5 = 1 >= 2@

#Testing Comparisons with Variables
# unlock bool _TEST1 = 1 > 1@ #false
# _TEST1 = 1 < 2@ #true
# lock bool _TEST2 = 1 < 2@ #true
# lock bool _TEST3 = _TEST1 != _TEST2@ #true
# lock bool _TEST4 = !_TEST3@ #false

# abstract FUNCTION(int _A, int _B){
#     scribe("_A")@
# }
# hail FUNCTION(1+2,2+4)@

#Testing the conditionals

# If statement
# if (9 > 10){
#     scribe("a is greater than b")@
# }


# IF_Elif statement
# if (_TEN > _Wrong){
#     scribe("10 is greater than 11")@
# } 
# else {
#     scribe("b is greater than a")@
# }


# IF_Elif_Else statement
# lock int _Switcher = 3@
# if (_Switcher == 1){ scribe("Switcher is 1")@ }
# elif (_Switcher == 2){ scribe("Switcher is 2")@ }
# elif (_Switcher == 3){ scribe("Switcher is 3")@ }
# else{ scribe("Switcher is not 1, 2, or 3")@ }

# For statements
# for _X in range(2, 6){
#   scribe("_X")@
# }
# for _X in "banana"{
#   scribe("_X2")@
# }
# Aslongas statement
aslongas (_COUNT >= 0){
    scribe("count")@
    _COUNT = _COUNT + 1@
}

aslongas _BINARY{
    scribe("1 times 2 is less than 3")@
}
# if (_BINARY == true){
#     scibe("This is true")@
# }
# else{
#     scribe("This is false")@
# }
# lock bool _Z = true@
# aslongas _Z == true{
#     scribe("This is true")@
#     _Z = false@
# }
"""
