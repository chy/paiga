
from pyga import Script
from pyga.builders import Condition, Function, Literal, Rule

def add_readme_comments(script):
  pass

def add_inspector_attributes(script):
  pass

def add_constants(script):
  pass

def add_imports(script):
  pass

# Why is this separate from defining the attributes?
def set_attributes(script):
  pass

# Sets internal attributes and constants
def set_internal_utilities(script):
  pass

def add_function_definitions(script):
  pass

def add_rule_definitions(script):
  pass

if __name__ == '__main__':
  script = Script()

  add_readme_comments(script)
  add_imports(script)
  add_inspector_attributes(script)
  add_constants(script)

  set_attributes(script)
  set_internal_utilities(script)
  add_function_definitions(script)
  add_rule_definitions(script)

  print(script.compile())
