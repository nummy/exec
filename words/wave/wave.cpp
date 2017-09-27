#include <iostream>
#include <iomanip>
using namespace std;

const double Plank = 6.626e-034;
const double MinLength = 1e-20 ;
const double MaxLength= 10 ;
const double speedOfLight = 3e8 ;

int main( )
    cout<<" please input the wavelength : " ;
    double length = 0.0 ;
    //input the length
    cin>>length;
of your wavelength
while (length < MinLength| |length >
MaxLength) //re-enter if your input if it is out of
range
cout<< "please input a wavelength
between 1* 10e-20 and 10 :" ;
cin>>length;
double enegy = Plank * speedofLight /
length;
//Calculation the enegy base the
wavelength you input
//what the wave is based the wavelength of
your input ,the energy should be output using 4
significant figures
if (length < 1e-11)
cout<<length<< " meters corresponds
to Gamma Rays and has an energy of "
<<setprecision (4 )<<enegy<<" joules." ;
}else if (length >= 1e-11&& length < 1e-
8)
cout<<length<< " meters corresponds
to X Rays and has an energy of "<<setprecision( 4 )
joules." ;
<<enegy<<"
else if (length >= 1e-8 && length < 4e-7 )
cout<<length<<'
meters corresponds
to Ultraviolet and has an energy of "
<<setprecision (4 )<<enegy<<" joules." ;
else if (length >= 4e-7 && length < 7e-7 )
cout<<length<< " meters corresponds
to Visible Light and has an energy of '
<<setprecision (4 )<<enegy<<" joules." ;

