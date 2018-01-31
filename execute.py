def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

def parse_token(token):
    return float(token) if token.find('.')>-1 else int(token)

OPERATOR_TO_LAMBDA = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
};
def split_tokens(expr):
    count_num = count_opr = 0
    index = 0
    valid_nums = '1234567890.'
    valid_opr = '+-/*'    
    out_expr=''
    for symb in expr:
        index= index + 1
        str_tmp = out_expr.split(' ')
        if symb == ' ':
            if str_tmp[len(str_tmp)-1]!="": out_expr+=symb
            continue
        elif (symb == '.' and out_expr and str_tmp[len(str_tmp)-1]!="" and symb not in str_tmp[len(str_tmp)-1] and str_tmp[len(str_tmp)-1] not in valid_opr) or symb.isdigit():
            out_expr +=symb if not out_expr or out_expr and (out_expr[len(out_expr)-1]==' ' or out_expr[len(out_expr)-1] in valid_nums) else " "+symb
            continue
        elif symb in valid_opr and out_expr:
            count_opr+=1
            out_expr += symb if symb in valid_nums or out_expr[len(out_expr)-1]==' ' else " "+symb           
            continue
        raise ValueError("Symbol '{0}' with position = {1} is not a valid input".format(symb,index))
    out_expr = out_expr.split(" ")
    count_num = len(out_expr)-count_opr
    if count_num-count_opr>1:
        raise Exception("Number of numbers more than number of operations")
    if count_num-count_opr<1:
        raise Exception("Number of operations more than number of numbers")

    return out_expr

def execute(expr):
    if type(expr) is not str: raise Exception("Expression should have a string type!")
    if expr=="": raise Exception("Expression is empty!")
    stack = []
    tokens = split_tokens(expr)
    index=-1
    for token in tokens:
        index += 1
        if token in OPERATOR_TO_LAMBDA:
            try:
                num2, num1 = stack.pop(), stack.pop()
            except:
                raise Exception("\nReverse Polish Notation isn't correct.\n{0}\n Token '{1}' with position = {2}".format(tokens,token,index))
            if type(num1) is float or type(num2) is float:
                stack.append((OPERATOR_TO_LAMBDA[token](num1,num2)))
            else:
                stack.append(int(OPERATOR_TO_LAMBDA[token](num1,num2)))                
        else:
            stack.append(parse_token(token))
    return stack.pop()
