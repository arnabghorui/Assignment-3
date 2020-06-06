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
	int n = 64;
	double gauss[n];
	float x_min = -5;
	float x_max = 5;
	float dx = (x_max - x_min) / (n - 1);



	for(int i=0; i < n; ++i)//Define the sinc function
	{
		gauss[i] = exp(-(x_min+i*dx,2)*(x_min+i*dx,2));
	}

	double _Complex FT[n];
	double k[n];
	float q;
	FILE *data;
	data = fopen("problem4.txt","w");
	for(int i = 0; i < n; i++)
	{
		q = -n/2+i;
		k[i]=2*M_PI*q/(n*dx);

		FT[i] = sqrt(1/(2*M_PI))*cexp(-I*k[i]*x_min)*DFT(gauss, n, q)*dx;

		fprintf(data,"%f\t\t%f\n",k[i],creal(FT[i]));
	}
	fclose(data);	
}
// gcc problem4.c -lm -lgsl -lgslcblas
// ./a.out
