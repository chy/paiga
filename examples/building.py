
# Lot                    --> Footprint("just an example")

# Footprint(height,area) --> t(0,0,1) 
                           # extrude(height) 
                           # Envelope(area)
                           
# Footprint(text)        --> print(text)

from pyga.builders.literal import Literal as literal
# from boa import Script
# from boa import Rule
#
# # Given a RuleBuilder object 'rule', fills it out.
# # You can make rules with python functions!
# def Lot(rule):
#   rule.name("Lot")
#     .literal("Footprint('just an example')")
#
# # This is our entry point to Boa.
# # Script is a python representation of a CGA script.
# # It keeps track of various CGA Entities you add to it
# # (rules, functions, attrs, etc).
# script = Script()
#
# # This constructs and returns a RuleBuilder called "Lot"
# # script owns the builder
# Lot = script.rule("Lot")
# # you can do various things on a RuleBuilder. Primarily,
# # you add Successors.
# # Anything you pass in quotes will be inserted literally
# # into the output script.
# Lot.literal("Envelope('just an example')")
#
# print script.write()
#
# # We can also make RuleBuilders directly.
# # The class is called 'Rule' rather than 'RuleBuilder'
# # because you'll probably be typing it a lot...
# Envelope = Rule("Envelope")
#   .literal(boa.ops.Split("y", {"~4": "Floor."}))
#
# script.rule("Lot")
#   .literal("Footprint('just an example')")
#
# script.parameterized_rule("Footprint", "text")
#   .literal("print(text)")
#
# print script.write()
# from boa.script import Script
from pyga.script import Script

script = Script()



script.add(pyga.literal("attr display_textures = true"))

Lot = script.rule("Lot")
Lot.add(literal("Envelope('just an example')")).add(literal('extrude(10)'))

Building = script.rule("Envelope").add(literal("A"))
Building.add(literal("extrude(10)"))


c2 = script.cond().case(literal("second"), literal("B")).then(literal("C"))

c1 = script.cond().case(literal("1 < 2"), literal("B"))
c1.case(literal("3 < 4"), c2).then(literal("NIL"))

for i in range(2):
  Fun1 = script.function("BenBernanke" + str(i)).param("abba").param("beth")
  Fun1.add(c1)


Fun2 = script.function("A").param("abba").param("beth")
Fun2.add(literal("{0} + {1}".format(Fun2.parameters[0], Fun2.parameters[1])))

# cond = script.cond("1 < 2", "B", "NIL")

# condc = script.cond().case("21 < 3", "C").case("324324234 < 3", "D").Else("Sadface")
print(script.write())