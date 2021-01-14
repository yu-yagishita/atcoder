import math

a, b, h, m =map(int,input().split())

th = (h*60+m)/720 * 2*math.pi
tm = m/60 * 2*math.pi

xh = a*math.cos(th)
yh = a*math.sin(th)
xm = b*math.cos(tm)
ym = b*math.sin(tm)

dx = xh-xm
dy = yh-ym

ans = math.sqrt(dx*dx + dy*dy)
print(ans)
