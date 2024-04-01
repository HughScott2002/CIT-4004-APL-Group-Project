data = """
unlock int _COUNT = 4@
lock string _Global_var = "This is a global variable."@
lock int _TEN = 10@
lock float _PI = 3.14@ 
unlock bool _BINARY = true@

lock string _This_String@
_This_String = "This is a string."@

#_PI = 3.15@
_BINARY = false@
_BINARY = true@

lock int _Wrong@ 
_Wrong = 11@

# lock int _Sum = _TEN + _Wrong@
# lock int _SUMMER = 1 + 2@
scribe("This is a comment.", _Wrong)@
#_Wrong = 121@
attempt{
     scribe("This is a try block.")@
     _BINARY = false@
}
findout unboundlocalerror{
   scribe("UnboundLocalError: _Local_var is not defined in this scope.")@
}
abstract IS_B_GREATER_THAN_A(){
   scribe("This is from inside an abstract")@
   lock bool _Inside_Abstract = true@   
}
hail IS_B_GREATER_THAN_A()@
"""
