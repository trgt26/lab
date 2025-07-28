def inverse_mod(k, p):
    """Find modular inverse of k mod p."""
    return pow(k, -1, p)

def point_double(x, y, a, p):
    """Compute 2G."""
    s_num = 3 * x**2 + a
    s_den = 2 * y
    s = (s_num * inverse_mod(s_den, p)) % p

    x2 = (s**2 - 2*x) % p
    y2 = (s * (x - x2) - y) % p

    return x2, y2

def point_add(x1, y1, x2, y2, p):
    """Compute P + Q."""
    if x1 == x2 and y1 == y2:
        raise ValueError("Use point_double for doubling.")
    
    s_num = y2 - y1
    s_den = x2 - x1
    s = (s_num * inverse_mod(s_den, p)) % p

    x3 = (s**2 - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p

    return x3, y3

# Parameters from your image
p = 17
a = 2
Gx, Gy = 5, 1

# Compute 2G
x2g, y2g = point_double(Gx, Gy, a, p)
print(f"2G = ({x2g}, {y2g})")

# Compute 3G = G + 2G
x3g, y3g = point_add(Gx, Gy, x2g, y2g, p)
print(f"3G = ({x3g}, {y3g})")
