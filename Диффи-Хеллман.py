p = int(input("p = "))
q = int(input("q = "))

n = p * q
phi = (p - 1) * (q - 1)

print("n =", n)
print("phi =", phi)

e = int(input("e = "))

d = 1
while (d * e) % phi != 1:
    d += 1

print("d =", d)
print("5 d:", d, d+phi, d+2*phi, d+3*phi, d+4*phi)
