data = """
# unlock int _COUNT = 4@
# lock string _Global_var = "This is a global variable."@
# lock int _TEN = 10@
# lock float _PI = 3.14@ 
# unlock bool _BINARY = true@

# lock string _This_String@
# _This_String = "This is a string."@

#_PI = 3.15@
#_BINARY = false@
#_BINARY = true@

# lock int _Wrong@ 
# _Wrong = 11@

# lock int _Sum = _TEN + _Wrong@
# lock int _SUMMER = 1 + 2@
#scribe("This is a comment.", _Wrong)@
#_Wrong = 121@
# attempt{
#      scribe("This is a try block.")@
#      _BINARY = false@
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


# if (9 > 10){
#     scribe("a is greater than b")@
# } else {
#     scribe("b is greater than a")@
# }
# if 1 > 2 {
#     scribe("1 is greater than 2")@
# } elif 1 < 2{
#     scribe("1 is less than 2")@
# }
# 24 != 25
# 26 < 27
# 28 > 29
# 30 <= 31
# 32 >= 33


#Testing the arithmetic operations
# lock int _B@
# _B = 5@
# lock int _A = 5+_B@
# lock int _EQQ  = _A@


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
lock bool _TEST1 = 1 > 1@ #false
lock bool _TEST2 = 1 < 2@ #true
lock bool _TEST3 = _TEST1 != _TEST2@ #true
lock bool _TEST4 = !_TEST3@ #false


#Testing the conditionals
# aslongas _BINARY{
#     scribe("1 times 2 is less than 3")@
# }
# if (_BINARY == true){
#     scibe("This is true")@
# }
# else{
#     scibe("This is false")@
# }
# lock bool _Z = true@
# aslongas _Z == true{
#     scribe("This is true")@
#     _Z = false@
# }
"""
