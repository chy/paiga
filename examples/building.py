from pyga import Script, Condition

script = Script()
script.add('''# Here's a comment''')
script.add('''# This is a case tree defined in pyga!\n''')

values= ["COM","RES","IND"]
return_val= [2,5,6]
field_name= "LU"

# c = Condition()
#
# for v, r in zip(values, return_val):
#   c.case(field_name + " = " + v, str(r))
# c.then("0")
#
# script.add(c)
# print(script.compile())

# You can define a Condition on its own
c1 = Condition()

c1.case('A = "INDUSTRIAL"', '3')
c1.case('B', '4')
c1.then('54')

# You can nest conditions
c2 = Condition()
c2.case('A || B', c1)
c2.case('C', '57')
c2.then('543')

# Or you can use method chaining
script.add(Condition()
           .case('A || B || C', c1)
           .case('D', '42')
           .then('26'))

print(script.compile())