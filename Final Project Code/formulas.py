from math import cos, sqrt,sin
def formula1(a,theta,m,mu,fa,desired):
    g=9.8
    if desired=='m':
        m=-(-g*sin(theta) + mu*g*cos(theta)+a)/fa
        return m

    
    fg=m*g*sin(theta)
    fn=m*g*cos(theta)
    
    if desired == 'mu':
        mu=(m*a-fg-fa)/(-fn)
        return mu
    ff=mu*fn
    if desired=='a':
        a=(fg+fa-ff)/m
        return a
    if desired == 'fa':
        fa=m*a-fg+ff
        return fa

def formula2(v1,v2,h,d,desired,ff,fa,m,theta):
    if desired=='v1':
        v1 = sqrt(2*(-1*(fa*d-ff*d - (1/2)*m*v2**2)-m*g*h)/m)
        return v1
    
    if desired=='v2':
        v2 = sqrt((2*(fa*d-ff*d+(m*g*h+(1/2)*m*v1**2))/m))
        return v2
