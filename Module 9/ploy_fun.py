def add(x,y):
    return x + y

def concatante(x,y):
    return str(x) + str(y)

def operate(operation,x,y):
    return operation(x,y)

result_add = operate(add,1,4)
result_con = operate(concatante,"hello ", "hi")

print(result_add)
print(result_con)
