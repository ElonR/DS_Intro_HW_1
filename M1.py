def my_func(x1, x2, x3):
    try:
     if (not isinstance(x1, float)) or (not isinstance(x2, float)) or (not isinstance(x3, float)): #check if float
           return ("Error: parameters should be float")
     num = (x1+x2+x3)*(x2+x3)*x3
     denominator = x1+x2+x3
     value = float(num/denominator)
     return value
    except:
        return ("Not a number – denominator equals zero")

def convert(hours, minutes):
    if hours < 0 or minutes < 0: #check that the numbers are bigger than 0
        return ("Input error!")
    secInHours = hours * 60 * 60
    secInMin = minutes * 60
    return secInHours + secInMin
