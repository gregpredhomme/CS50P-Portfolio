x_str, y, z_str = input("write an expression").split(" ")

x = float(x_str)
z = float(z_str)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print(f"{result:.1f}")
