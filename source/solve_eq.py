import numpy as np


def runge_kutta(f,y0:float,interval:tuple,n:int=10)->list:
    """

    Parameters
    ----------
    f
    y0
    interval
    n

    Returns
    -------

    """
    x=interval[0]
    h=(interval[1]-interval[0])/n
    y_est=y0
    curve=[]
    for i in range(1,n+1):
        k1=h*f(x=x,y=y_est)
        k2=h*f(x=x+h/2,y=y_est+k1/2)
        k3=h*f(x=x+h/2,y=y_est+k2/2)
        k4=h*f(x=x+h,y=y_est+k3)

        # Add point to curve
        curve.append( ( x, y_est) )

        # Update
        y_est+=(k1+2*k2+2*k3+k4)/6
        x+=h
    return curve

