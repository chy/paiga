import unittest
from writer import Writer
from entity import *


a = LiteralEntity("A")
b = LiteralEntity("B")
c = LiteralEntity("C")
f = LiteralEntity("F")
g = LiteralEntity("center(xz)")

print("Testing literal entities.")
writer = Writer()
a.accept(writer)
print(writer.done())


condition_1 = ConditionEntity()
condition_1.children = {a:b}
condition_1.else_ = c

condition_2 = ConditionEntity()
condition_2.children = {a:b, c:condition_1, f : g}
condition_2.else_ = g

condition_3 = ConditionEntity()
condition_3.children = {c:condition_2, a:b}
condition_3.else_ = a

stochastic = StochasticEntity()
stochastic.children = {LiteralEntity("20"):c}
stochastic.else_ = b

stochastic_2 = StochasticEntity()
stochastic_2.children = {LiteralEntity("40"):stochastic}
stochastic_2.else_ = f

writer = Writer()
stochastic.accept(writer)
print(writer.done())

print("\nTesting condition entities.")

writer = Writer()
condition_3.accept(writer)
print(writer.done())

print("\nTesting rule entities.")
rule = RuleEntity()
rule.name = "Envelope"
rule.parameters = [a, b, c]
rule.children = [condition_2]

writer = Writer()
rule.accept(writer)
print(writer.done())

print("\nStochastic rule.")
rule = RuleEntity()
rule.name = "Footprint"
rule.parameters = [a, b, c]
rule.children = [stochastic]

writer = Writer()
rule.accept(writer)
print(writer.done())


print("\nTesting function entities.")
function = FunctionEntity()
function.name = "getHeight"
function.parameters = [a, b, c]
function.children = [condition_1]

writer = Writer()
function.accept(writer)
print(writer.done())

