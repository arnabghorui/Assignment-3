#include <stdio.h>    
#include <complex.h>
#include <math.h>

double _Complex DFT(double Fn[],int N, float P)
{
	if(N != 1)
	{

		double even[N/2]; 
		double odd[N/2];

		for(int i=0; i < N/2; i++)
		{
			even[i] = Fn[2*i];
			odd[i] = Fn[2*i+1];
		}

		return DFT(even, N/2, P)+cexp(-2*M_PI*I*P/N)* DFT(odd, N/2, P);
	}
	else
	{
		return Fn[0];
	}
}

int main() 
{
	int n = 128;
	double sinc[n];
	float x_min = -10;
	float x_max = 10;
	float dx = (x_max - x_min) / (n - 1);



	for(int i=0; i < n; ++i)//Define the sinc function
	{
		if(x_min + i*dx == 0)
			sinc[i] = 1;	
		else
			sinc[i] = sin(x_min + i*dx) / (x_min + i*dx);
	}
	
	double _Complex FT[n];
	double k[n];
	float q;
	FILE *data;
	data = fopen("problem2.txt","w");
	for(int i = 0; i < n; i++)
	{
		q= -n/2+i;
		k[i]=2*M_PI*q/(n*dx);

		FT[i] = sqrt(1/(2*M_PI))*cexp(-I*k[i]*x_min)*DFT(sinc,n,q)*dx;

		fprintf(data,"%f\t\t%f\n",k[i],creal(FT[i]));
	}
	fclose(data);	
}
// gcc problem2.c -lm -lgsl -lgslcblas
// ./a.out
