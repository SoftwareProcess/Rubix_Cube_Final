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
    epsilon = 0.07
    highBound = float(t)
    lowBound = 0.0
    simpsonOld = 0.0
    simpsonNew = epsilon
    s = 8.0
#     while (abs((simpsonNew - simpsonOld) / simpsonNew) > epsilon):
#         #simpsonOld = simpsonNew
    w=(t-lowBound)/s
#     if (s == 4):
#              # w = (highBound - lowBound) / s
#              simpsonNew = (w/3) * (_f(lowBound,n) + 4*_f(lowBound + w, n) + 2*_f(lowBound + 2*w, n)
#                                   + 4*_f(lowBound+3*w, n) + _f(lowBound+4*w, n)) 
#     if (s == 8):
#              simpsonNew = (w/3) * (_f(lowBound,n) + 4*_f(lowBound + w, n) + 2*_f(lowBound + 2*w, n)
#                         + 4*_f(lowBound+3*w, n) + 2*_f(lowBound + 4*w, n) + 4*_f(lowBound + 5*w, n) 
#                         + 2*_f(lowBound + 6*w, n) + 4*_f(lowBound + 7*w, n)
#                         + _f(lowBound+ 8*w, n))
#              
#     if (s == 16):
#             simpsonNew = (w/3) * (_f(lowBound,n) + 4*_f(lowBound + w, n) + 2*_f(lowBound + 2*w, n)
#                         + 4*_f(lowBound+3*w, n) + 2*_f(lowBound + 4*w, n) + 4*_f(lowBound + 5*w, n) 
#                         + 2*_f(lowBound + 6*w, n) + 4*_f(lowBound + 7*w, n) + 2*_f(lowBound+ 8*w, n) 
#                         + 4*_f(lowBound+ 9*w, n) + 2*_f(lowBound + 10*w, n)
#                         + 4*_f(lowBound+ 11*w, n) + 2*_f(lowBound + 12*w, n) + 4*_f(lowBound+ 13*w, n) 
#                         + 2*_f(lowBound + 14*w, n) + 4*_f(lowBound+ 15*w, n) + _f(lowBound + 16*w, n))
# #          
    #aummation of the Simpson
    simpsonNew = _f(lowBound,n)    #start calculating the Simpson
    multiplier = int(1)      #The multiplier in the summations
    while (multiplier < s):
        if ((multiplier % 2) == 1):  #when s is odd
                    simpsonNew = simpsonNew + 4*_f(lowBound + (multiplier * w), n)
        if ((multiplier % 2) == 0):  #when s is even
                    simpsonNew = simpsonNew + 2*_f(lowBound + (multiplier * w), n)
        multiplier = multiplier+1  # next term      
    simpsonNew = (w/3)*(simpsonNew + _f(highBound, n)) # add the last term to the Simpson and multiply * w/3   
        #s = s * 2
    return simpsonNew
    
