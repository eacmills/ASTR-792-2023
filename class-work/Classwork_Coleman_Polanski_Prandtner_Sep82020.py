#Brandon Coleman, Alex Polanski, Anja Prandtner
#This is the work for part 2 on the class work for September 8, 2020


import numpy as np                          # I use this for maths and sometimes arrays.
                                            # "np" is just an abbreviation since we call this package so often!
import pylab                                # I use this for arrays and plotting sometimes
import matplotlib.pyplot as plt                    # Standard plotting package
import scipy

from astropy import units as u              # This one helps with unit conversion



                                            # Super important!! 
                                            # This embeds plots in the Jupyter window 
                                            # (instead of showing them as pop-ups)
%matplotlib inline                             

plt.rc('font', family='sans-serif')  # Set plot fonts
#plt.rc('text', usetex=True)      
plt.rc('text', usetex=False)        # This is a quick fix if you don't have latex on your computer


temps = [10.000,20.000,30.000,40.000,60.000,80.000,110.00,160.00,220.00,320.00,450.00,630.00,890.00,1260.0,1780.0,2510.0,3550.0,5010.0,8000.0]

Hcollrates = [7.0204e-11 , 8.2028e-11 , 9.0584e-11 , 9.8459e-11 , 1.1421e-10 , 1.3039e-10 , 1.5488e-10 , 1.9425e-10 , 2.3747e-10 , 2.9974e-10 , 3.6597e-10 , 4.3801e-10 , 5.1576e-10 , 5.9551e-10 , 6.7682e-10 , 7.6338e-10 , 8.6209e-10 , 9.7867e-10 , 1.1762e-09]
Hecollrates =[1.6482e-11 , 1.8573e-11,  2.1463e-11,  2.4598e-11,  3.0966e-11,  3.7104e-11,  4.5611e-11 , 5.7945e-11,  7.0394e-11 , 8.7752e-11 , 1.0736e-10,  1.3238e-10 , 1.6591e-10,  2.0812e-10,  2.5733e-10 , 3.1253e-10,  3.7520e-10,  4.4631e-10,  5.5849e-10]
pH2collrates =[1.1818e-10 , 1.2795e-10,  1.3314e-10,  1.3766e-10,  1.4621e-10,  1.5405e-10,  1.6409e-10 , 1.7678e-10,  1.8771e-10 , 2.0139e-10 , 2.1690e-10,  2.3769e-10 , 2.6604e-10,  3.0174e-10,  3.4447e-10 , 3.9528e-10,  4.5692e-10,  5.2977e-10,  6.3237e-10]
oH2collrates =[1.3258e-10 , 1.3972e-10,  1.4475e-10,  1.4972e-10,  1.5993e-10 , 1.7007e-10 , 1.8457e-10 , 2.0635e-10 , 2.2904e-10 , 2.6107e-10 , 2.9598e-10 , 3.3664e-10 , 3.8519e-10 , 4.4088e-10 , 5.0314e-10 , 5.7270e-10 , 6.5175e-10 , 7.3905e-10 , 8.5173e-10]
Hpluscollrates =[2.4006e-11,	4.4688e-11,	6.4277e-11,	8.3187e-11,	1.1965e-10,	1.5485e-10	,2.0602e-10,	2.8826e-10,	3.8350e-10	,5.3660e-10,	7.2842e-10,	9.8488e-10,	1.3424e-09	,1.8334e-09,	2.4990e-09,	3.4007e-09,	4.6401e-09	,6.3190e-09,	9.6131e-09]

fig = plt.figure()

plt.semilogy(temps,Hcollrates,c='red',label='Hydrogen')
plt.plot(temps,Hecollrates,c='blue',label='Helium')
plt.plot(temps,pH2collrates,c='purple',label='p-Hydrogen2')
plt.plot(temps,oH2collrates,c='black',label='o-Hydrogen2')
plt.plot(temps,Hpluscollrates,c='orange',label='H plus')
plt.ylabel(r"Collisional Rate Coeff ($cm^3 s^{-1}$)")
plt.xlabel("Temperature (K)")
plt.legend()
plt.show()
