def my_func(x1, x2, x3):
    try:
     if (not isinstance(x1, float)) or (not isinstance(x2, float)) or (not isinstance(x3, float)):
           return ("Error: parameters should be float")
     num = (x1+x2+x3)*(x2+x3)*x3
     denominator = x1+x2+x3
     value = float(num/denominator)
     return value
    except:
        return ("Not a number – denominator equals zero")
