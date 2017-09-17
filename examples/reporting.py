# In a typical script, this would be
# from pyga import Script, Condition, Literal
from .. import Script, Condition, Literal

#This file is not current. Test first.

# define the attributes
greenspacePercentage = Attribute("greenspacePercentage", "30") \
  .annotate("Group", ("City Attributes", 0))

mixedOffice = Attribute("mixedOffice", "0.2") \
  .annotate("Group", "City Attributes")

landuseType = Attribute("landuseType", "Mixed")

buildingHeightFactor = Attribute("buildingHeightFactor", 1) \
  .annotate("Group", ('"Mapped"', "99"))

nFloor = Attribute("nFloor",
                   Condition() \
                     .case(landuseType.name + ' == "Office"',
                           'ceil(rand(6, 15) * buildingHeightFactor')
                     .case('landuseType == "Office',
                           'ceil(rand(3, 12) * ' + buildingHeightFactor.name())
                     .then('ceil(rand(1, 3) * ' + buildingHeightFactor.name())
                   ) \
  .annotate("Group", "Building attributes")

baseFloors = Attribute("baseFloors",
                   Condition() \
                     .case(landuseType.name + ' == "Residential"', '0')
                     .then('ceil(rand(0, 3)')
                   ) \
  .annotate("Group", "Building attributes")

floorHeight = Attribute("floorHeight", Condition() \
                          .case(landuseType.name + ' == "Office"', 'rand(5, 6)')
                          .case(landuseType.name + ' == "Mixed"', 'rand(4, 5)')
                          .then('rand(3, 4')) \
  .annotate("Group", "Building attributes")

distanceStreet = Attribute("distanceStreet", Stochastic() \
                           .case('20%', 0)
                           .then('rand(3, 6'))\
  .annotate("Group", '"Footprint"', '3').annotate("Range", ('3', '6'))

distanceBuildings = Attribute("distanceBuildings", Stochastic() \
                           .case('50%', 0)
                           .then('rand(4, 8'))\
  .annotate("Group", '"Footprint"').annotate("Range", ('4', '8'))

vizMode = Attribute("VizMode", '"massAndFloors"')\
  .annotate("Viz", "4").annotate("Range", ('"massOnly"', "floors", ''"massAndFloors"''))

script = Script()
script.add(
  Literal(
    "# ---------------------------------------"
    "# Attributes                             "
    "# ---------------------------------------"
  )
)
# Add the attributes
script.add([greenspacePercentage, mixedOffice, landuseType, buildingHeightFactor, nFloor, baseFloors,\
            floorHeight, distanceStreet, distanceBuildings, vizMode])

# Add the rules.
script.add(Lot(greenspacePercentage))
script.add(LotInner())
script.add(LotCorner())
script.add(BuildingLot(floorHeight, nFloor, distanceStreet))
script.add(Parcel(distanceBuildings))
script.add(Subparcel(landuseType))

script.add(RetailBase)
script.add(Mixed(baseFloors, floorHeight, nFloor))


script.add(MassViz())
script.add(GreenSpace())
script.add(OpenSpace())
script.add(Ground())

print(script.compile())
