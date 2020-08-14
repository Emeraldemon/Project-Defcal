#project UADI
print('by Ayush Dutta')


def phase():
    call = str(input('enter geometrical function(only in terms of area and perimeter)'))
    '''
    objective:to enable specific commands to run only under the user's command to the variable 'call'
    input parameters:sides,length,breadh,height,diameter,radius
    encouragement:best of luck UADI!
    '''
    # 2d shapes
    if call == 'perimeter of a square':
        s = float(input('enter side of square in decimal numbers'))
        p = 4 * s
        print('perimeter of square with given sides =', p)
    elif call == 'area of a square':
        sideforarea = float(input('enter side of square in decimal numbers'))
        areaofsquare = sideforarea ** 2
        print('area of square with given sides =', areaofsquare)
    elif call == 'perimeter of rectangle':
        lengthforperimeter = float(input('enter the length of the rectangle in decimal numbers:'))
        breadthforperimeter = float(input('enter the breadth of the rectangle in decimal numbers:'))
        perimeterofrectangle = 2 * (lengthforperimeter * breadthforperimeter)
        print('perimetr of the rectangle with given sides=', perimeterofrectangle)
    elif call == 'area of rectangle':
        lengthforarea = float(input('enter the length of the rectangle in decimal numbers:'))
        breadthforarea = float(input('enter the breadth of the rectangle in decimal numbers:'))
        areaofrectangle = lengthforarea * breadthforarea
        print('area of the given rectangle = ', areaofrectangle)
    elif call == 'circumference of circle':
        radiusofcircle = float(input('enter the radius of circle in decimal numbers'))
        circumference = 2 * 3.14 * radiusofcircle
        print('the circumference of the given circle =', circumference)
    elif call == 'area of circle':
        rofcircle = float(input('enter the raadius of circle in decimal numbers'))
        areaofcircle = 3.14 * (rofcircle ** 2)
        print('area of the circle with given radius =', areaofcircle)
    elif call == 'perimeter of triangle':
        side_A = float(input('enter first side of the triangle in decimal numbers'))
        side_B = float(input('enter second side of the triangle in decimal numbers'))
        side_C = float(input('enter third side of the triangle in decimal numbers'))
        triangle_perimeter = side_A + side_B + side_C
        print('perimeter of triangle with given side =', triangle_perimeter)
    elif call == 'area of triangle':
        side_A_BETA = float(input('enter base of the triangle in decimal numbers'))
        side_B_BETA = float(input('enter height of the triangle in decimal numbers'))
        area_triangle = 1 / 2 * side_A_BETA * side_B_BETA
        print('area of the right triangle with given sides', area_triangle)
    # project yui 2nd phase
    # 3d shapes edged
    elif call == 'TSA of cube':
        side_cube = float(input('enter the side of cube in decimal numbers'))
        tsa_cube = 6 * (side_cube ** 2)
        print('TSA of the cube =', tsa_cube)
    elif call == 'LSA of cube':
        sid_cube = float(input('enter the side of cube in decimal numbers'))
        lsa_cube = 4 * (sid_cube ** 2)
        print('LSA of the cube =', lsa_cube)
    elif call == 'TSA of cuboid':
        length_cuboid = float(input('enter the lenght of cuboid in decimal numbers'))
        breadth_cuboid = float(input('enter the breadth of cuboid in decimal numbers'))
        height_cuboid = float(input('enter the height of cuboid in decimal numbers'))
        tsa_cuboid = 2 * ((length_cuboid * breadth_cuboid) + (breadth_cuboid * height_cuboid) + (
                    height_cuboid * length_cuboid))
        print('TSA of the cuboid = ', tsa_cuboid)
    elif call == 'LSA of cuboid':
        length_cuboid = float(input('enter the lenght of cuboid in decimal numbers'))
        breadth_cuboid = float(input('enter the breadth of cuboid in decimal numbers'))
        height_cuboid = float(input('enter the height of cuboid in decimal numbers'))
        lsa_cuboid = (2 * height_cuboid) * (length_cuboid + breadth_cuboid)
        print('LSA of the cuboid =', lsa_cuboid)
    elif call == 'TSA of cylinder':
        radius_face = float(input('enter the radius of the cylinder'))
        height_face = float(input('enter the height of the cylinder'))
        tsa_cylinder = (2 * 3.14 * radius_face) * (radius_face + height_face)
        print('the TSA of the cylinder =', tsa_cylinder)
    elif call == 'CSA of cylinder':
        radius_facepp = float(input('enter the radius of the cylinder'))
        height_facepp = float(input('enter the height of the cylinder'))
        csa_cylinder = 2 * 3.14 * radius_facepp * height_facepp
        print('the CSA of the cylinder =', csa_cylinder)
    elif call == 'TSA of cone':
        radius_hat = float(input('enter the radius of the cone'))
        slant_hat = float(input('enter the slant height of the cone'))
        tsa_hat = 3.14 * radius_hat * (radius_hat + slant_hat)
        print('TSA of the cone = ', tsa_hat)
    elif call == 'LSA of cone':
        radius_cone = float(input('enter the radius of the cone'))
        slant_cone = float(input('enter the slant height of the cone'))
        lsa_cone = 3.14 * radius_cone * slant_cone
        print('LSA of the cone = ', lsa_cone)
    # project yui 3rd phase
    # 3d shapes curved
    elif call == 'surface area of sphere':
        radius_ball = float(input('enter the radius of the sphere'))
        surface_area_ball = 4 * 3.14 * (radius_ball ** 2)
        print('surface area of the given sphere =', surface_area_ball)
    elif call == 'CSA of hemisphere':
        radius_egg = float(input('enter the radius of hemisphere'))
        csa_egg = 2 * 3.14 * (radius_egg ** 2)
        print('CSA of hemispere =', csa_egg)
    elif call == 'TSA of hemisphere':
        radius_shell = float(input('enter the radius of hemisphere'))
        csa_shell = 3 * 3.14 * (radius_shell ** 2)
        print('TSA of hemisphere =', csa_shell)
    # project yui phase 4
    # volume
    elif call == 'volume of cube':
        rod_cube = float(input('enter the side of cube in decimal numbers'))
        volume_cube = rod_cube ** 3
        print('volume of given cube =', volume_cube)
    elif call == 'volume of cuboid':
        long_cuboid = float(input('enter the lenght of cuboid'))
        wide_cuboid = float(input('enter the breadth of cuboid'))
        high_cuboid = float(input('enter the height of cuboid'))
        volume_cuboid = long_cuboid * wide_cuboid * high_cuboid
        print('volume of the given cuboid', volume_cuboid)
    elif call == 'volume of cylinder':
        radon_cylinder = float(input('enter the radius of cuboid'))
        tall_cylinder = float(input('enter the height of cuboid'))
        volume_cylinder = 3.14 * (radon_cylinder ** 2) * tall_cylinder
        print('volume of the given cylinder =', volume_cylinder)
    elif call == 'volume of cone':
        radon_cone = float(input('enter the radius of cone'))
        tent_cone = float(input('enter the perpendicular height of the cone'))
        volume_cone = 1 / 3 * 3.14 * (radon_cone ** 2) * tent_cone
        print('the volume of the given cone =', volume_cone)
    elif call == 'volume of sphere':
        radon_sphere = float(input('enter the radius of sphere'))
        volume_sphere = 4 / 3 * 3.14 * (radon_sphere ** 3)
        print('volume of the given sphere =', volume_sphere)
    elif call == 'volume of hemisphere':
        radon_hemi = float(input('enter the radius of hemisphere'))
        volume_hemi = 2 / 3 * 3.14 * (radon_hemi ** 3)
        print('volume of the given hemisphere =', volume_hemi)
    # project UADI phase1 finished on 25th july at 1:23 p.m (IST)
    # made with help of ATOM,PYCHARM,NOTEPAD++



    
