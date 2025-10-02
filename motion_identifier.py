# Motion Type Identifier



def convert_velocity(value, unit):

    if unit == "m/s": return value

    elif unit == "ft/s": return value * 0.3048

    elif unit == "km/s": return value * 1000

    elif unit == "mi/s": return value * 1609.34

    else: return None



def convert_acceleration(value, unit):

    if unit == "m/s²": return value

    elif unit == "ft/s²": return value * 0.3048

    elif unit == "km/s²": return value * 1000

    elif unit == "mi/s²": return value * 1609.34

    else: return None



def motion_type(v, a):

    if v == 0: return "At Rest"

    elif a == 0: return "Uniform Motion"

    elif a > 0: return "Accelerated Motion"

    else: return "Decelerated Motion"



# --- Main Program ---

v = convert_velocity(float(input("Enter velocity value: ")), input("Enter velocity unit (m/s, ft/s, km/s, mi/s): "))

a = convert_acceleration(float(input("Enter acceleration value: ")), input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): "))



print("\n--- Results ---")

print(f"Velocity = {v:.3f} m/s")

print(f"Acceleration = {a:.3f} m/s²")

print(f"Motion Type = {motion_type(v, a)}")