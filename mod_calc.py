import logg

def sum(a, b):
    res = a + b
    logg.logging.info(f'Sum: {a} + {b} = {res}')
    return res
    
def sub(a, b):
    res = a - b
    logg.logging.info(f'Sub: {a} - {b} = {res}')
    return res
    
def mult(a, b):
    res = a * b
    logg.logging.info(f'Mult: {a} * {b} = {res}')
    return res
    
def div1 (a, b):
    if b == 0:
        return 'Division is impossible'
    res = a / b
    logg.logging.info(f'Div: {a} / {b} = {res}')
    return res
    
def div2(a, b):
    if b == 0:
        return 'Division is impossible'
    res = a // b
    logg.logging.info(f'Div: {a} // {b} = {res}')
    return res
    
def div3(a, b):
    if b == 0:
        return 'Division is impossible'
    res = a % b
    logg.logging.info(f'Div: {a} % {b} = {res}')
    return res
    
def pow(a, b):
    res = a ** b
    logg.logging.info(f'Pow: {a} ** {b} = {res}')
    return res
    
def sqrt(a):
    res = a ** 0.5
    logg.logging.info(f'Sqrt: {a} ** 0.5 = {res}')
    return res
    