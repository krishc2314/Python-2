from temperature.celsius_to_fahrenheit import c_to_f
from temperature.fahrenheit_to_celsisu import f_to_c
from temperature.celsius_to_kelvin import c_to_k

print("Temperature Conversion Menu")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter choice: "))

if choice == 1:
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", c_to_f(c))

elif choice == 2:
    f = float(input("Enter Fahrenheit: "))
    print("Celsius:", f_to_c(f))

elif choice == 3:
    c = float(input("Enter Celsius: "))
    print("Kelvin:", c_to_k(c))

else:
    print("Invalid choice")
