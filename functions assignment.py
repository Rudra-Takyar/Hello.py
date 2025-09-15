# area of circle
def area_circle(pi, radius):
    return pi * (radius ** 2)
radius = float(input("Enter radius of circle: "))
area = area_circle(3.1416, radius)
print(f"Area of Circle: {area:.2f}")

# Tax
def total_due(money, tax):
    return money + (money * tax)
money = float(input("Enter amount of money: "))
tax_rate_percent = float(input("Enter tax rate (in %): "))
total = total_due(money, tax_rate_percent / 100)
print(f"Total Due: {total:.2f}")

# convert Fahrenheit to Celsius
def to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = to_celsius(fahrenheit)
print(f"Celsius: {celsius:.5f}")


