"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""


class Pavilion:
    def __init__(self,length,width,height,material,fabrication_method):
        self.length=length
        self.width=width
        self.height=height
        self.material=material
        self.fabrication_method=fabrication_method
    
    def volume(self):
        return self.length*self.width*self.height
    def cost_estimate(self):
        material_costs = {"wood":50,"steel":100,"concrete":80}
        fabrication_costs = {"prefab":30,"on-site":50}
        return self.volume()*material_costs[self.material]+self.volume()*fabrication_costs[self.fabrication_method]
    def co2_emissions(self):
        material_emissions = {"wood":20,"steel":70,"concrete":50}
        fabrication_emissions = {"prefab":10,"on-site":30}
        return self.volume()*material_emissions[self.material]+self.volume()*fabrication_emissions[self.fabrication_method]  
   
        
class Columns(Pavilion):
    def __init__(self,length,width,height,material,fabrication_method):
        super().__init__(length,width,height,material,fabrication_method)
    def volume(self):
        return super().volume()
    def column_cost(self):
        return super().cost_estimate()
    def column_emissions(self):
        return super().co2_emissions()

class Walls(Pavilion):
    def __init__(self,length,width,height,material,fabrication_method):
        super().__init__(length,width,height,material,fabrication_method)
    def volume(self):
        return super().volume()
    def wall_cost(self):
        return super().cost_estimate()
    def wall_emissions(self):
        return super().co2_emissions()
    
class Roofs(Pavilion):
    def __init__(self,length,width,height,material,fabrication_method):
        super().__init__(length,width,height,material,fabrication_method)
    def volume(self):
        return super().volume()
    def roof_cost(self):
        return super().cost_estimate()
    def roof_emissions(self):
        return super().co2_emissions()


c1=Columns(0.2,0.2,5,"steel","prefab")
c2=Columns(0.3,0.3,5,"steel","on-site")
w1=Walls(4,0.2,5,"concrete","on-site")
w2=Walls(3,0.3,5,"concrete","prefab")
r1=Roofs(4,5,0.2,"wood","on-site")
pavillion_cost=c1.column_cost()+c2.column_cost()+w1.wall_cost()+w2.wall_cost()+r1.roof_cost()
pavillion_emissions=c1.column_emissions()+c2.column_emissions()+w1.wall_emissions()+w2.wall_emissions()+r1.roof_emissions()
c1_cost=c1.column_cost()
c1_esmissions=c1.column_emissions()
c2_cost=c2.column_cost()
c2_emissions=c2.column_emissions()
w1_cost=w1.wall_cost()
w1_emissions=w1.wall_emissions()
w2_cost=w2.wall_cost()
w2_emissions=w2.wall_emissions()
r1_cost=r1.roof_cost()
r1_emissions=r1.roof_emissions()

print(f'''In the Pavilion,the columns costs are {c1_cost} and {c2_cost},the co2 emissions are {c1_esmissions} and {c2_emissions}.
      The walls costs are {w1_cost} and {w2_cost},the co2 emissions are {w1_emissions} and {w2_emissions}).
      The roof cost is {r1_cost} and the co2 emissions is {r1.roof_emissions()}
      the total cost of pavilion is {pavillion_cost} and the total co2 emissions is {pavillion_emissions}.''')

