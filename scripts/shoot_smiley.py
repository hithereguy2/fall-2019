# 1 Initial values
#d = 10. 
#h = 7.
v = 20.

d = float(input("Enter smiley's distance: "))
h = float(input("Enter smiley's height  : "))

# 2 point the gun
import math
theta = math.atan(h/d) 
print(f'Angle = {math.degrees(theta):.2f} deg.')

# 3 paintball velocity

# initial projectile velocity-x-component
vxp0 = v*math.cos(theta)
# initial projectile velocity-y-component
vyp0 = v*math.sin(theta)

print(f'vxp0 = {vxp0:.2f}, vyp0 = {vyp0:.2f}, v = {math.sqrt(vxp0**2+vyp0**2):.2f} ; all in m/s')

# 4 time of flight
# The flight ends when the projectile reaches Smiley’s vertical path.
# In this case, only the horizontal movement of the projectile is required for the computation. 
t = d/vxp0 
print(f'time of flight = {t:.2f} secs.')

# 5,6 compute heights

# Projectile
g = -9.8
hp = vyp0 * t + 0.5 * g *t**2  # note we are using time = t, h = 0, v = vyp0


# Smiley
hs = h + 0.5 * g *t**2  # note we are using time = t, h = 10, v =0

# 7
print(f'Height of projectile = {hp:.2f}')
print(f'Height of smiley = {hs:.2f}')

