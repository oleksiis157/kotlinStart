#Write a simple function that calculates price of the door.


price = float(1.57)
type_doore = input("Input type of door (classical, triangle, circle): ")
if (type_doore == "classical"):     
      height = float(input("Input the height of yor door: "))
      width = float(input("Input the width of yor door: "))
      conc_classical = (height*width)*price
      print("The sum of your classical door = ", conc_classical,"$")
elif (type_doore == "triangle"):
      a = float(input("Input 1st side: "))
      b = float(input("Input 2nd side: "))
      c = float(input("Input 3st side: "))
      p_triangle = (a+b+c)/2
      s_triangle = p_triangle*(p_triangle-a)(p_triangle-b)(p_triangle-c)
      print(s_triangle)
      print("The sum of your triangle door = ", s_triangle*price,"$")
elif (type_doore == "circle"):
      p = 3.14
      d_circle = float(input("""Input diametr of circle 
      (just a number): """))
      r_circle = d_circle/2
      print("The square of circle = ", p*(r_circle**2))
      print("The sum of circle door = ", (p*(r_circle**2))*price,"$")  
else:
      print("You don't need a door...") 
