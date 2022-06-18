import numpy as np

def F(a_1, b_1, c_1, a_2, b_2, c_2, R, h, alpha_tol, h_tol, R_tol):

    side = (R+R_tol) + (h+h_tol)*np.sin(alpha_tol * np.pi/180) - (R+R_tol)*(1-np.cos(alpha_tol * np.pi/180))

    top = (h+h_tol) + (R+R_tol)*np.sin(alpha_tol * np.pi/180) - (h+h_tol)*(1-np.cos(alpha_tol * np.pi/180))

    bottom = (R+R_tol)*np.sin(alpha_tol * np.pi/180)

    if (( -bottom < c_1 ) or ( top > c_2 ) or ( side > np.min([np.abs(a_1), np.abs(b_1), np.abs(a_2), np.abs(b_2)]) )):
        return -R-h
    else:
        return np.min([h_tol, R_tol, (R_tol + h_tol)*np.sin(alpha_tol * np.pi/180)/2])
