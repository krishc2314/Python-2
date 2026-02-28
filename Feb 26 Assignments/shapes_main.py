import shapes

print("Choose your shape:")
print("Type 1 for Circle")
print("Type 2 for Rectangle")
print("Type 3 for Triangle")

choice = int(input("Enter choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    print("Area of the circle:", shapes.circle(r))

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of rectangle:", shapes.rectangle(l, w))

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area of triangle:", shapes.triangle(b, h))

else:
    print("Invalid choice")
