# Run this as 'python -m paiga.examples.building' to get around
# the irritating python import situation.
# from paiga import Script, Condition, Stochastic, Rule, Function
from internal.entity import *
from script import Script
from builders import *

script = Script()
script.add('''# Here's a comment''')
script.add('''# This is a case tree defined in paiga!\n''')

values = ["COM", "RES", "IND"]
return_val = [2, 5, 6]
field_name = "LU"

# c = Condition()
#
# for v, r in zip(values, return_val):
#   c.case(field_name + " = " + v, str(r))
# c.then("0")
#
# script.add(c)
# print(script.serialize())

# You can define a Condition on its own
c1 = Condition()

c1.case('A = "INDUSTRIAL"', '3')
c1.case('B', '4')
c1.else_('54')

# You can nest conditions
c2 = Condition()
c2.case('A || B', c1)
c2.case('C', '57')
c2.else_('543')

s = Stochastic()
s.case("20", "C")
s.case("30", "F")

lot = Rule("Lot")
lot.add("s('0.8, '1, '0.8) center(xz) extrude(20) Envelope", c2)

e = Function("E", ["A", "B", "C"])
e.add("s('0.8, '1, '0.8) center(xz) extrude(20) Envelope", c2)

# Or you can use method chaining
script.add(lot).add(e)
script.add('''# Here's a comment''')
print(script.serialize())
