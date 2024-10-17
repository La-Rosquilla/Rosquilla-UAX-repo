def motion_calculator():
    x0 = float(input("Enter the initial position (x0) in meters: ")) 
    u = float(input("Enter the initial velocity (u) in meters/second: ")) 
    t = float(input("Enter the time (t) in seconds: "))
    a = float(input("Enter the acceleration (a) in meters/second^2: ")) 
    
    v = u + a * t
    
    x = x0 + u * t + 0.5 * a * (t ** 2)
    
    print("\n--- Results ---")
    print(f"Final velocity (v): {v:.2f} m/s")
    print(f"Final position (x): {x:.2f} meters")
    print(f"Acceleration (a): {a:.2f} m/s² (constant)")
    
motion_calculator()