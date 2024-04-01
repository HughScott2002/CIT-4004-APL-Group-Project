data = """
#This is a comment
# Global variable
#unlock int _COUNT = (0 + 2 - 3) / 4@ #Declaration
#lock string _Global_var = "This is a global variable."@
#lock int _TEN = 10@
#lock float _PI = 3.14@ 
#unlock bool _BINARY = true@

#lock int _Assignment@#Declaration
#_Assignment = 5@ #Assignment

#scribe("This is an INTEGER", _TEN)@

abstract PLUS(){
    lock float _A = 5.5@
    lock float _B = 10.5@
    lock float _SUM = _A + _B@
}


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
    attempt{
        scribe("Trying to access _Local_var outside its scope:", _Local_var)@
    }
    findout unboundlocalerror{
        scribe("UnboundLocalError: _Local_var is not defined in this scope.")@
    }
}
# hail will call the outer function
hail OUTER_FUNCTION()@

# Function with a loop
abstract IS_B_GREATER_THAN_A(int _B, int _A){
    if _B > _A{
        scribe("b is greater than a")@
    }
    elif _B > _A{
        scribe("a and b are equal")@
    }
    else{
        scribe("a is greater than b")@
    }
}

lock int _B@ 
_B= 5@
lock int _A@
_A= 10@
# Calling the IS_B_GREATER_THAN_A function
hail IS_B_GREATER_THAN_A(int _B, int _A)@

 aslongas true{
     scribe("Count:", _COUNT)@
 }
"""
