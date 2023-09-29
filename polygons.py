from math import degrees, atan2, atan, cos, sin, tan, radians, pi
from numpy import arccos, arcsin
from functools import reduce
from wikipedia import summary
import turtle

'''PENDING'''
#try to make it more compact and efficient(if possible)
#check the functioning of all functions for parallelogram, tuple, and then other polygons+functions too,

def sum_float(temp_list):
    return reduce(lambda var1, var2: var1+var2, temp_list)

class Polygons:

    def __init__(p, sides): # ALL POLYGONS
        p.sides=sides

    def definition(a): # ALL POLYGONS WITH 3-4 SIDES

        poly_definition={'Triangle': 'A triangle is a polygon that has three sides !',
                         'Quadrilateral': 'A quadrilateral is a closed polygon with four sides',
                         'Parallelogram': 'A parallelogram is a polygon with four sides out of which opposite sides are equal and parallel and opposite angles also equal',
                         'Rhombus': 'A rhombus is a polygon with four sides that are all equal and its diagonals bisect each other ar 90 degrees',
                         'Rectangle': 'A rectangle is a polygon with four sides out of which opposite sides are equal and parallel with all the angles right angled',
                         'Square': 'A square is a four sided polygon with all its side equal and all the angles right angled, the diagonals are also equal and bisect each other at right angles !'}
        
        print(poly_definition[polygon.split('(')[0]]+'\n')

    def info_from_web(a): # ALL POLYGONS
        print(summary(polygon.split('(')[0]), '\n')

    def perimeter(p): # SPECIAL CASE : QUADRILATERAL, PARALLELOGRAM AND RHOMBUS; REST SAME.
            
        if 'Quadrilateral' in polygon or 'Parallelogram' in polygon:
            sides_list=poly.sides_of_quad(); temp_perimeter=sum_float(sides_list)

        elif 'Rhombus' in polygon:
            sides_list=poly.sides(); temp_perimeter=sum_float(sides_list)

        else:
            temp_perimeter=sum_float(p.sides)

        return temp_perimeter
    
    def angles(p): # SQUARE, RECTANGLE, PENTAGON, HEXAGON, HEPTAGON, OCTAGON, NONAGON, DECAGON
        polygon_dat={'Square':(4, 90), 'Rectangle':(4, 90), 'Pentagon':(5, 108), 'Hexagon':(6, 120), 'Heptagon':(7, 900/7), 'Octagon':(8, 135), 'Nonagon':(9, 140), 'Decagon':(10, 144)}

        for polygon.split('(')[0] in polygon_dat:
            return tuple(float(polygon_dat[polygon.split('(')[0]][1]) for i in range(polygon_dat[polygon.split('(')[0]][0]))
    
    def check_validity(p): # ALL POLYGONS
        polygon_dat={'Triangle':3, 'Quadrilateral':4, 'Parallelogram':4, 'Rhombus':2, 'Rectangle':4, 'Square':4, 'Pentagon':5, 'Hexagon':6, 'Heptagon':7, 'Octagon':8, 'Nonagon':9, 'Decagon':10}

        for polygon.split('(')[0] in polygon:
            print(f"Please enter a valid {polygon.split('(')[0]} !\n") or quit() if len(p.sides)!=polygon_dat[polygon.split('(')[0]] else None

        if 'Triangle' in polygon:

            for check in range(3):
                print('Sum of two sides of a triangle cannot be greater than or equal to the third side !\n\nThe program ends here !\n') or quit() if p.sides[check]+p.sides[(check+1)%3]<=p.sides[(check+2)%3] else None

        elif 'Rectangle' in polygon:
            print('The sides of the rectangle entered are either invalid or in the wrong order !\nThe program ends here !\n') or quit() if p.sides[0]!=p.sides[2] or p.sides[1]!=p.sides[3] else None

        elif 'Quadrilateral' in polygon:

            for var1 in range(4):
                check_var=0

                for var2 in range(4):
                    check_var+=1 if p.sides[var1]==p.sides[var2] else 0
                    print('The given vertices do not form a quadrilateral !\n') or quit() if check_var>1 else None

class Triangle(Polygons):

    def area(p):
        temp_sum=sum_float(p.sides)/2
        area_of_triangle=(temp_sum*(temp_sum-p.sides[0])*(temp_sum-p.sides[1])*(temp_sum-p.sides[2]))**0.5

        return area_of_triangle
    
    def angles(p):

        angle_1=degrees(arccos(((p.sides[1]**2 + p.sides[2]**2 - p.sides[0]**2) / (2*p.sides[1]*p.sides[2]))))
        angle_2=degrees(arccos(((p.sides[0]**2 + p.sides[2]**2 - p.sides[1]**2) / (2*p.sides[0]*p.sides[2]))))
        angle_3=degrees(arccos(((p.sides[0]**2 + p.sides[1]**2 - p.sides[2]**2) / (2*p.sides[0]*p.sides[1]))))

        temp_angles=[angle_1, angle_2, angle_3]
        temp_angles.sort(reverse=True)
        temp_angles[1], temp_angles[2]=temp_angles[2], temp_angles[1]

        return tuple(temp_angles)
     
    def diagonals(p):
        print("A triangle doesn't have any diagonals !")

    def display(p):
        temp_angles_triangle=list(poly.angles())

        point=turtle.Turtle(); point.speed(0); point.getscreen().bgcolor('black')
        point.penup(); point.goto(-(0.5*25*sorted(p.sides)[0]), -(0.5*25*sorted(p.sides)[1])); point.pendown()
        point.color('#C080F2')
        point.begin_fill()

        for turn in range(len(temp_angles_triangle)):
            point.forward(sorted(p.sides)[turn]*25); point.left(float(180)-temp_angles_triangle[turn])

        point.end_fill()
        point.hideturtle(); turtle.done()
            
class Quadrilateral(Polygons):

    def sides_of_quad(p):
        quad_sides=((((p.sides[(var+1) % 4][0]-p.sides[var][0])**2 + (p.sides[(var+1) % 4][1]-p.sides[var][1])**2)**0.5) for var in range(len(p.sides)))
        return tuple(quad_sides)
    
    def angles(p):
        temp_slopes, temp_angles=[], []

        def calc_slope(x1, y1, x2, y2):
            dx, dy = x2-x1, y2-y1
            return_val=float('inf') if dx==0 else degrees(atan2(dy, dx))

            return return_val
        
        for side in range(len(p.sides)):

            x1, y1=p.sides[side]
            x2, y2=p.sides[(side+1) % len(p.sides)]

            temp_slope=calc_slope(x1, y1, x2, y2); temp_slopes.append(temp_slope)

        def calc_angle(slope1, slope2):
            
            if slope1==float('inf') or slope2==float('inf'):
                return degrees(pi/2)
            else:
                return degrees(atan(abs((slope2-slope1) / (1+(slope1 * slope2)))))
            
        for slope in range(len(temp_slopes)):
            s1, s2=temp_slopes[slope], temp_slopes[(slope+1) % len(temp_slopes)]

            temp_angle=calc_angle(s1, s2); temp_angles.append(temp_angle)

        return tuple(temp_angles)

    def diagonals(p):
        quad_angles, quad_sides, temp_diagonals=poly.angles(), poly.sides_of_quad(), []
        temp_diagonals=(((quad_sides[i]**2 + quad_sides[i+1]**2 - 2*quad_sides[i]*quad_sides[i+1]*cos(quad_angles[i]))**0.5) for i in (0, 2))

        return tuple(temp_diagonals)

    def area(p):
        quad_angles, quad_sides = poly.angles(), poly.sides_of_quad()
        temp_area=(0.5*quad_sides[i]*quad_sides[i+1]*sin(radians(quad_angles[i])) for i in (0, 2))

        return sum(temp_area)

    def display(p):

        point=turtle.Turtle(); point.speed(0); point.getscreen().bgcolor('black')
        point.color('#1EC8DB') if 'Parallelogram' in polygon else point.color('#DB49C3')
        point.penup(); point.goto(-(0.5*25*poly.sides_of_quad()[0]), -(0.5*25*poly.sides_of_quad()[1])); point.pendown()
        point.begin_fill()

        for turn in range(4):
            point.forward(poly.sides_of_quad()[turn]*25); point.left(float(180)-poly.angles()[turn])

        point.end_fill()
        point.hideturtle(); turtle.done()

class Parallelogram(Quadrilateral):

    def check_validity(p):
        parallelogram_angles, parallelogram_sides = poly.angles(), poly.sides_of_quad()
        check1, check2=0, 0

        for var1 in range(len(parallelogram_angles)):
            check1+=1 if parallelogram_angles.count(parallelogram_angles[var1])>1 else 0

        for var1 in range(len(poly.sides_of_quad())):
            check2+=1 if parallelogram_sides.count(parallelogram_sides[var1])>1 else 0

        print('Please enter a valid Parallelogram !\n') or quit() if check1<=0 or check2<=0 else None

class Rhombus(Polygons):

    def sides(p):
        side_val=((p.sides[0]**2 + p.sides[1]**2)**0.5)/2
        sides_of_rhombus=tuple(side_val for i in range(4))

        return (sides_of_rhombus)
    
    def area(p):
        area_of_rhombus=0.5*p.sides[0]*p.sides[1]
        return area_of_rhombus
    
    def angles(p):
        temp_sides=Rhombus.sides(p)

        angle1=2*degrees(arcsin(p.sides[0]/(2*temp_sides[0])))
        angle2=2*degrees(arcsin(p.sides[1]/(2*temp_sides[0])))

        return (angle1, angle2, angle1, angle2)
    
    def diagonals(p):
        return p.sides
    
    def display(p):

        point=turtle.Turtle(); point.speed(0); point.getscreen().bgcolor('black')
        point.penup(); point.goto(-(0.5*25*Rhombus.sides(p)[0]), -(0.5*25*Rhombus.sides(p)[1])); point.pendown()
        point.color('#DBDB49')
        point.begin_fill()

        for turn in range(len(Rhombus.sides(p))):
            point.forward(Rhombus.sides(p)[turn]*25); point.left(float(180)-Rhombus.angles(p)[turn])

        point.end_fill()
        point.hideturtle(); turtle.done()

class Rectangle(Polygons):

    def diagonals(p):

        dimensions=tuple(p.sides[i] for i in (0, 2))
        diag=(tuple(dimensions)[0]**2 + tuple(dimensions)[1]**2)**0.5
        temp_diagonals=(diag for i in range(2))

        return tuple(temp_diagonals)

    def area(p):
        area_of_rectangle=p.sides[0]*p.sides[1]
        return area_of_rectangle
    
    def display(p):

        point=turtle.Turtle(); point.speed(0); point.getscreen().bgcolor('black')
        point.penup(); point.goto(-(0.5*25*p.sides[0]), -(0.5*25*p.sides[1])); point.pendown()
        point.color('#96CD17') if 'Rectangle' in polygon else point.color('#ECAA11')
        point.begin_fill()

        for turn in range(len(p.sides)):
            point.forward(p.sides[turn]*25); point.left(90)

        point.end_fill()
        point.hideturtle(); turtle.done()

class Square(Rectangle):
    pass
    
class Pentagon(Polygons):

    def definition(p):
        print(f"A {polygon.split('(')[0].lower()} is a closed polygon made up of {len(p.sides)} sides !\n")

    def diagonals(p):
        temp_diag=2*p.sides[0]*sin(radians(36))
        return tuple(temp_diag for i in range(2))

    def area(p):
        area_of_pentagon= (5 * p.sides[0]**2 * tan(radians(36))**-1) / 4
        return area_of_pentagon
    
    def display(p):
        colors_of_polygons={'Pentagon':'#C327D4', 'Hexagon':'#278FD4', 'Heptagon':'#646DDF', 'Octagon':'#D8A33A', 'Nonagon':'#BBD12D', 'Decagon':'#15A855'}

        point=turtle.Turtle(); point.speed(0); point.getscreen().bgcolor('black')
        point.penup(); point.sety(- p.sides[0]*25); point.pendown()
        point.color(colors_of_polygons[polygon.split('(')[0]])

        point.begin_fill()
        point.circle(p.sides[0]*25, steps=len(p.sides))
        point.end_fill()

        point.hideturtle(); turtle.done()

class Hexagon(Pentagon):

    def diagonals(p):
        temp_diag1=2*p.sides[0]*sin(radians(60))
        temp_diag2=2*p.sides[0]

        return tuple(temp_diag1, temp_diag2, temp_diag1)

    def area(p):
        area_of_hexagon=(3 * (3**0.5) * (p.sides[0]**2)) / 2
        return area_of_hexagon

class Heptagon(Pentagon):

    def diagonals(p):
        temp_diag1=2*p.sides[0]*sin(radians(900/(2*7)))
        temp_diag2=p.sides[0]+(2*p.sides[0]*sin(radians(270/7)))

        return tuple(temp_diag1, temp_diag2, temp_diag2, temp_diag1)

    def area(p):
        area_of_heptagon=(7 * (p.sides[0]**2) * ((tan(radians(180/7)))**-1)) / 4
        return area_of_heptagon

class Octagon(Pentagon):

    def diagonals(p):
        temp_diag1=2*p.sides[0]*sin(radians(135/2))
        temp_diag2=p.sides[0]+(2*p.sides[0]*sin(radians(45)))
        temp_diag3=temp_diag1+(2*p.sides[0]*sin(radians(22.5)))

        return tuple(temp_diag1, temp_diag2, temp_diag3, temp_diag2, temp_diag1)

    def area(p):
        area_of_octagon=2 * (p.sides[0]**2) * (1+(2**0.5))
        return area_of_octagon
        
class Nonagon(Pentagon):

    def diagonals(p):
        temp_diag1=2*p.sides[0]*sin(radians(140/2))
        temp_diag2=p.sides[0]+(2*p.sides[0]*sin(radians(50)))
        temp_diag3=temp_diag1+(2*p.sides[0]*sin(radians(30)))

        return tuple(temp_diag1, temp_diag2, temp_diag3, temp_diag3, temp_diag2, temp_diag1)

    def area(p):
        area_of_nonagon=(9 * (p.sides[0]**2) * (tan(radians(20))**-1)) / 4
        return area_of_nonagon  

class Decagon(Pentagon):

    def diagonals(p):
        temp_diag1=2*p.sides[0]*sin(radians(144/2))
        temp_diag2=p.sides[0]+(2*p.sides[0]*sin(radians(54)))
        temp_diag3=temp_diag1+(2*p.sides[0]*sin(radians(36)))
        temp_diag4=temp_diag2+(2*p.sides[0]*sin(radians(18)))

        return tuple(temp_diag1, temp_diag2, temp_diag3, temp_diag4, temp_diag3, temp_diag2, temp_diag1)

    def area(p):
        area_of_decagon=(5 * (p.sides[0]**2) * ((5 + (2 * (5**0.5)))**0.5)) / 2
        return area_of_decagon

print('''\nA polygon is any closed curve consisting of a set of line segments (sides) connected such that no two line segments cross each other
A polygon with all equal sides and angles is also known as an equilateral/regular polygon
On the basis of angles, a polygon with all angles less than 180 is known as a convex polygon, otherwise a concave polygon
Also, if the sides of the polygon do not intersect, then it is known as a simple polygon, otherwise it is known as a complex polygon\n
This program focuses on 'simple/concave/regular+irregular polygons' of sides 3 and 4, and only 'simple/concave/regular' polygons with 5-10 no. of sides\n
Enter the sides of the desired polygon to begin the program\n
The input method should look like this: Polygon([side1, side2, side3, ...])
OR
Incase of a Quadrilateral/Parallelogram, the input method should look like this: Quadrilateral/Parallelogram([(x1, y1), (x2, y2), (x3, y3), (x4, y4)]) where (x, y) are the vertices of the Quadrilateral
OR
Incase of a Rhombus, the input method should look like this: Rhombus([diagonal_1, diagonal_2])\n''')

polygon=input('Enter the desired polygon:')
polygon=polygon.title(); print('')

try:
    poly=eval(polygon)

except:
    print('Please enter a valid Polygon !\n\nThe program ends here !\n'); quit()

poly.definition(); poly.check_validity()

sides=poly.sides_of_quad() if 'Quadrilateral' in polygon or 'Parallelogram' in polygon else None

while True:
    print('''Choose the desired operation, the code for each operation is as follows:
    1. Display the polygon
    2. Perimeter of the polygon
    3. Area of the polygon
    4. The angles of the polygon
    5. Diagonals of the polygons, if any
    6. Sum of all the angles of the polygon
    7. Sum of diagonals of the polygon
    8. Brief info from the web
    9. End of program\n''')

    try:
        choice=int(input('Enter the operation you want to perform:')); print('')

        if choice==1:
            poly.display()

        elif choice==2:
            print(poly.perimeter(), '\n')

        elif choice==3:
            print(poly.area(), '\n')

        elif choice==4:
            for angle in range(len(tuple(poly.angles()))):
                print(f'Angle_{angle+1} = {poly.angles()[angle]}')
            
            print('')

        elif choice==5:

            if 'Triangle' in polygon:
                poly.diagonals()

            else:
                if len(polygon.split(','))>4 or 'Rhombus' in polygon:
                    print(f"The lengths of the diagonals that can be drawn from any vertex of the given {polygon.split('(')[0]} are:\n")

                for diagonal in range(len(tuple(poly.diagonals()))):
                    print(f'Diagonal_{diagonal+1} = {poly.diagonals()[diagonal]}')

            print('')

        elif choice==6:
            print(sum_float(poly.angles()), '\n')

        elif choice==7:
            print(sum_float(poly.diagonals()), '\n')

        elif choice==8:
            poly.info_from_web()

        elif choice==9:
            print('The program ends here !\n'); quit()

        else:
            print('Enter a valid operation code !\n')

        key=input('Wish to continue further? (Y/N)\nEnter your desired choice:'); print('')
        print('The program ends here !\n') or quit() if key!='Y' and key!='y' else None

    except ValueError:
        print('Enter a valid operation code!\n')
