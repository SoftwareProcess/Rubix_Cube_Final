import math
import platform


# Outward facing method(s)
def prob(parmDictionary):
    ERROR_HEADER = "error: "
    ERROR_KEY = "error"
    SOLUTION_KEY = "probability"
    DEFAULT_TAILS = 2
    resultDict = {}


    # Validate input parameter values
    try:
        # Validate n
        if(not("n" in parmDictionary)):
            raise ValueError("missing n")
        n = parmDictionary["n"]
        if(n == ''):
            raise ValueError("missing n")
        try:
            nNumeric = float(n)
            if(nNumeric - int(nNumeric) > 0):
                raise ValueError("non int n")
            n = int(n)
        except:
            raise ValueError("non-integer n")
        if (n < 2):
            raise ValueError("out-of-bounds n")
        if(n > 32):
            raise ValueError("out-of-bounds n")

        # Validate t
        if (not ("t" in parmDictionary)):
            raise ValueError("missing t")
        t = parmDictionary["t"]
        if(t == ''):
            raise ValueError("missing t")
        try:
            t = float(t)
        except:
            raise ValueError("non-float t")
        if (t < 0.0):
            raise ValueError("out-of-bounds t")
        
        # Validate tails
        if (not ("tails" in parmDictionary)):
            tails = DEFAULT_TAILS
        else:
            tails = parmDictionary["tails"]
            if(tails == " "):
                resultDict['egg'] = platform.platform()
                tails = DEFAULT_TAILS
            if(tails == ''):
                raise ValueError("invalid tails")
            else:
                try:
                    tails = int(tails)
                except:
                    raise ValueError("non-integer tails")
                if ((tails != 1) & (tails != 2)):
                    raise ValueError("invalid tails")
    # Catch validation problems and return error diagnostic
    except Exception as e:
        result = ERROR_HEADER + e.args[0]
        resultDict[ERROR_KEY] = result
        return resultDict

    # Calculate probability
    constant = _calculateConstant(n)
    integration = _integrate(t, n, _f)
    if (tails == 1):
        result = constant * integration + 0.5
    else:
        result = constant * integration * 2
       
    resultDict[SOLUTION_KEY] = result 
    return resultDict


#---------------------------------------------------------------------------
# Internal methods
def _gamma(x):
    if (x == 1):
        return 1
    if (x == 0.5):
        return math.sqrt(math.pi)
    return (x - 1) * _gamma(x - 1)


def _calculateConstant(n):
    n = float(n)
    numerator = _gamma((n + 1.0) / 2.0)
    denominator = _gamma(n / 2.0) * math.sqrt(n * math.pi)
    result = numerator / denominator
    return result


def _f(u, n):
    n = float(n)
    base = (1 + (u ** 2) / n)
    exponent = -(n + 1.0) / 2.0
    result = base ** exponent
    return result


# ----------- PLEASE COMPLETE THE FUNCTION BELOW ----------
def _integrate(t, n, _f):
    ERROR_HEADER = "error: "
    ERROR_KEY = "error"
    SOLUTION_KEY = "probability"
    DEFAULT_TAILS = 2
    resultDict = {}
    DEFAULT_EPSILON = 0.001
    
    try:
    # Validate S
        if (not ("s" in parmDictionary)):
            raise ValueError("missing s")
        s = parmDictionary["s"]
        if(s == ''):
            raise ValueError("missing s")
        try:
            s = float(s)
        except:
            raise ValueError("non-float s")
        if (s < 0.0):
            raise ValueError("out-of-bounds s")
        
        # Validate lowBound
        if (not ("lowBound" in parmDictionary)):
            raise ValueError("missing lowBound")
        lowBound = parmDictionary["lowBound"]
        if(lowBound == ''):
            raise ValueError("missing lowBound")
        try:
            lowBound = float(lowBound)
        except:
            raise ValueError("non-float lowBound")
        if (lowBound < 0.0):
            raise ValueError("out-of-bounds lowBound")
        
        # Validate highBound
        if (not ("highBound" in parmDictionary)):
            raise ValueError("missing highBound")
        highBound = parmDictionary["highBound"]
        if(highBound == ''):
            raise ValueError("missing highBound")
        try:
            highBound = float(highBound)
        except:
            raise ValueError("non-float highBound")
        if (highBound < 0.0):
            raise ValueError("out-of-bounds highBound")
        
        # Validate epsilon - added
        if (not ("epsilon" in parmDictionary)):
            epsilon = DEFAULT_EPSILON
        else:
            epsilon = parmDictionary["epsilon"]
            if (epsilon == " "):
                resultDict["egg"] = platform.platform()
                epsilon = DEFAULT_EPSILON
            if(epsilon == ''):
                raise ValueError("invalid epsilon")
            else:
                try:
                    epsilon = int(epsilon)
                except:
                    raise ValueError("invalid epsilon")
   # Catch validation problems and return error diagnostic
    except Exception as e:
        result = ERROR_HEADER + e.args[0]
        resultDict[ERROR_KEY] = result
        return resultDict             
    
    
    epsilon = 0.001
    simpsonOld = 0.0
    simpsonNew = epsilon
    s = 4
    while (abs((simpsonNew - simpsonOld) / simpsonNew) > epsilon):
        simpsonOld = simpsonNew
        w = (highBound - lowBound) / s
        simpsonNew = (w/3) * (_f(lowBound,n) + 4*_f(lowBound + w, n) + 2*_f(lowBound + 2w, n)
                              + 4*_f(lowBound + 3w, n) + 2*_f(lowBound + 4w, n) 
                              + 4*_f(highBound-w,n) _f(highBound, n))
    
    
    
        s = s * 2
    return simpsonNew
    
