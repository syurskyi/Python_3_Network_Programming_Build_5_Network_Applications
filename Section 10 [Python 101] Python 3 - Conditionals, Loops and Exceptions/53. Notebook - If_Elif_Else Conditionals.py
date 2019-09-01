# If / Elif / Else conditionals - executing code based on one or more conditions being evaluated as True or False; the "elif" and "else" clauses are optional
x = 5

if x > 5:  # if the "x > 5" expression is evaluated as True, the code indented under the "if" clause gets executed, otherwise the execution jumps to the "elif" clause...
    print("x is greater than 5")
elif x == 5:  # ...if the "x == 5" expression is evaluated as True, the code indented under the "elif" clause gets executed, otherwise the execution jumps to the "else" clause
    print("x IS 5")
else:  # this covers all situations not covered by the "if" and "elif" clauses; the "else" clause, if present, is always the last clause in the code block
    print("x is NOT greater than 5")

# result of the above "if" block
x IS 5