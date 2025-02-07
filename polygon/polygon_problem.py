import math
import reading_json


SideRadius, TC, passing_criteria = reading_json.read_json("/home/vikasdw/python/polygon/input.json")


class polygon:
    def __init__(self,i):
        self.n_side = i[0]
        self.radius = i[1]
    def __repr__(self):
        return (f"number of sides are {self.n_side} and radius is {self.radius}")
        

    def get_interior_angle(self):
        interior_angle= []
        for x in self.n_side:          
            interior_angle.append((x - 2)*(180/x))
        # interior_angle = (self.n_side - 2)*(180/(self.n_side))
        return interior_angle
    @property
    def p_get_interior_angle(self):
        interior_angle= []
        for x in self.n_side:          
            interior_angle.append((x - 2)*(180/x))
        return interior_angle
    
    def get_edge_length(self):
        edge_length =[]
        for x in self.n_side:
            edge_length.append(2*x*math.sin(180/self.radius[0]))
        return edge_length
    @property 
    def p_get_edge_length(self):
        edge_length = 2*self.radius*math.sin(180/self.n_side)
        return edge_length    

    def get_apothem(self):
        apothem= []
        for x in self.n_side:
            apothem.append(self.radius[0]*math.cos(180/x))
        return apothem

    def get_area(self):
        edge_length = self.get_edge_length()
        apothem = self.get_apothem()
        area = []
        for x in enumerate(self.n_side): 
                area.append(x[1]*edge_length[x[0]]*apothem[x[0]]/2)
        return area

    def get_perimeter(self):
        edge_length = self.get_edge_length()
        perimeter = []
        for x in enumerate(self.n_side):
            perimeter.append(x[1]*edge_length[x[0]])
        return perimeter

    def __eq__(self, other):
        if isinstance(other, polygon):
            return self.n_side == other.n_side and self.radius == other.radius

    def __gt__(self, other):
        if isinstance(other, polygon):
            return self.radius > other.radius
# p = polygon(([4], [4]))
# q = polygon(([4], [5]))
# print(p.get_interior_angle())
# # print(p.p_get_interior_angle)
# # print(format(p.get_edge_length(),".2f"))
# # print(format(p.get_apothem(),".2f"))
# # print(format(p.get_area(),".2f"))
# # print(format(p.get_perimeter(),".2f"))
# print(q>p)

class polygon_sequence(polygon):
    def __init__(self,i,l):
        super().__init__(i)
        self.n_side=[]
        self.radius=[]
        self.l = l
        for x in self.l:
            self.n_side.append(x[0])
            self.radius.append(x[1])
    



# l =[(3,4),(4,4,),(5,4)]

# p = polygon_sequence((0,0),SideRadius)

# print(f"p.side is {p.n_side}")
# print(p.get_edge_length())
# print(p.get_perimeter())
# for tc in TC:
#     print(tc)
#     print(getattr(p, tc)())



###### working with ZIP#####
# final_TC= list(zip(TC, SideRadius, passing_criteria))
# print(final_TC)
# for tc in final_TC:
#     p = polygon_sequence((0,0),[tc[1]])
#     result= (getattr(p, tc[0])())
#     if result[0] < tc[2]:
#         print(f"TC is Pass as {result[0]} is less than {tc[2]}")
