data = """

# *************************************************************
# Abstract Declaration with parameters and nested functions with attempt and findout blocks
# *************************************************************

lock string _Global_var = "This is a global variable."@
unlock int _COUNT = (0 + 2 + 3)@
lock int _Assignment@
_Assignment = (5+7)*9@



abstract OUTER_FUNCTION(int _TEN, float _PI, bool _BINARY){
    # Enclosing variable
    lock string _Enclosing_var = "This is an enclosing variable."@

    attempt{
        if _TEN > _PI{
            scribe("TEN is greater than PI")@
        }
        else{
            scribe("PI is greater than TEN")@
        }
        if _BINARY{
            scribe("BINARY is true")@
        }
        else{
            scribe("BINARY is false")@
        }
    }
    findout exception{
        scribe("This is an exception")@
    }

    abstract INNER_FUNCTION(){
        # Local variable
        lock string _Local_var = "This is a local variable."@
        
        # Accessing variables from different scopes
        scribe("Inside INNER_FUNCTION:")@
        scribe("Local variable:", _Local_var)@
        scribe("Enclosing variable:", _Enclosing_var)@
    }
    # hail will Call the inner function
    hail INNER_FUNCTION()@

    # Trying to access the local variable outside its scope
    # scribe("Trying to access _Local_var outside its scope:", _Local_var)@
}

hail OUTER_FUNCTION(10, 3.14, true)@

for _I in range(2, 8){
  scribe("Hello is is the for loop")@
}
for _K in "banana"{
  scribe("This is another for loop")@
}


aslongas (_COUNT >= 0){
    _COUNT = (_COUNT - 1)@
    # scribe(_Count)@
    lock int _Inside_WHILE = 5@
    scribe("This is _Inside_WHILE", _Inside_WHILE)@
}
scribe(_COUNT)@

"""
