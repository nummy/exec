/**
CMPSC 201-FALL 2017
002R
Purpose: This program is used to calculate the energy of the specified wave
Input: wavelength
Processing: Get the wave length from user input, then calculate the energy, and finally, get the correspond wave name
            and output the infomation
Output: wave's energy and the correspond wave
**/
#include <iostream>
#include <iomanip>
using namespace std;

const double PLANK = 6.626e-034;
const double MINLENGTH = 1e-20 ;
const double MAXLENGTH= 10 ;
const double LIGHTSPEED = 3e8 ;

int main( ){
    double length = 0.0;
    double energy = 0.0;
    cout<<"Please input the wavelength: ";
    cin>>length;
    while(length<MINLENGTH || length>MAXLENGTH){
        //re-enter if your input if it is out of range
        cout<< "Please input the wavelength, it must between 1e-20 and 10: " ;
        cin>>length;
    }
    energy = PLANK*LIGHTSPEED/length;
    if (length < 1e-11){
        cout<<length<<" meters corresponds to Gamma Rays and has an energy of "<<setprecision(4)<<energy<<" joules"<<endl;
    }
    else if(length < 1e-8){
        cout<<length<<" meters corresponds to X Rays and has an energy of "<<setprecision(4)<<energy<<" joules"<<endl;
    }
    else if(length < 4e-7 ){
        cout<<length<<" meters corresponds to Ultraviolet Rays and has an energy of "<<setprecision(4)<<energy<<" joules"<<endl;
    }else if(length < 7e-7){
        cout<<length<<" meters corresponds to Visible Light and has an energy of "<<setprecision(4)<<energy<<" joules"<<endl;
    }else if(length<1e-3){
        cout<<length<<" meters corresponds to Infrared and has an energy of "<<setprecision(4)<<energy<<" joules"<<endl;
    }else if(length<1e-2){
        cout<<length<<" meters corresponds to Microwaves and has an energy of "<<setprecision(4)<<energy<<" joules"<<endl;
    }else{
        cout<<length<<" meters corresponds to Radiowaves and has an energy of "<<setprecision(4)<<energy<<" joules"<<endl;
    }
    return 0;
}


