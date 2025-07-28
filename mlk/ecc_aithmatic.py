def mod_inverse(a, p):
    """Return the modular inverse of a mod p"""
    return pow(a, -1, p)  # Same as Fermat's little theorem for prime p

def is_on_curve(x, y, a, b, p):
    """Check if the point (x, y) is on the curve y² = x³ + ax + b (mod p)"""
    return (y * y) % p == (x**3 + a * x + b) % p

def find_points(a, b, p):
    """Find all (x, y) pairs that lie on the curve y² = x³ + ax + b (mod p)"""
    points = []
    for x in range(p):
        rhs = (x**3 + a*x + b) % p
        for y in range(p):
            if (y*y) % p == rhs:
                points.append((x, y))
    return points

def point_add(P, Q, a, p):
    """Add two points P and Q on the curve over F_p"""
    if P == "O":
        return Q
    if Q == "O":
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return "O"  # P and -P = O (point at infinity)

    if P != Q:
        # Slope: λ = (y2 - y1) / (x2 - x1)
        l = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p
    else:
        # P == Q: Point doubling
        # Slope: λ = (3x^2 + a) / (2y)
        l = ((3 * x1**2 + a) * mod_inverse(2 * y1, p)) % p

    x3 = (l**2 - x1 - x2) % p
    y3 = (l * (x1 - x3) - y1) % p
    return (x3, y3)

def point_double(P, a, p):
    """Double a point P = (x, y) on the curve"""
    return point_add(P, P, a, p)



# Example curve: y² ≡ x³ + ax + b mod p
a = 1
b = 1
p = 23  # A small prime

# 1. Find all points on the curve
points = find_points(a, b, p)
print(f"Total points on curve y² = x³ + {a}x + {b} over F_{p}: {len(points)}")
print(points)

# 2. Pick two points and add
P = points[0]
Q = points[1]
R = point_add(P, Q, a, p)
print(f"\nP = {P}, Q = {Q}")
print(f"P + Q = {R}")

# 3. Point doubling
D = point_double(P, a, p)
print(f"2P = {D}")
