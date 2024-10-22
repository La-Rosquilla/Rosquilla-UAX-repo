import math

def free_fall():

    # Take user input for initial values
    h = float(input("Enter the initial height in meters: "))
    g = float(input("Enter the value for gravity in meters per second (the one used for Earth is 9.81ms^-1): ")or 9.81)
    
    # Calculate the time taken to hit the ground using the quadratic formula
    # 0.5 * g * t^2 + 0 * t - h = 0 
    a = 0.5*g
    b = 0
    c = h

    discriminant = 4*a*c
    
    if discriminant < 0:
        print("Error: No real solution exists for those values.")
        return
    else:
        t1 = (-b + math.sqrt(discriminant)) / (2*a)
        t2 = (-b - math.sqrt(discriminant)) / (2*a)

        #choose the maximum of the two
        time = max (t1, t2)

        print(f"\nThe time taken for the object to hit the ground is: {time:.2f} seconds")
    
 # Calculate the final velocity using v = u + g*t
    final_velocity = 0 + g * time
    print(f"The final velocity when the object hits the ground is: {final_velocity:.2f} meters/second")
    
    
if __name__ == "__main__":
    free_fall( )