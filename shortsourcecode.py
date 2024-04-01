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
# attempt{
#     scribe("This is a try block.")@
# }
# findout exception{
#         scribe("UnboundLocalError: _Local_var is not defined in this scope.")@
#     }
#abstract IS_B_GREATER_THAN_A(){
#    scribe("b is greater than a")@   
#}
"""
