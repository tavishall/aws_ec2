// reading a text file
#include <iostream>
#include <fstream>
#include <string>

#include <cuda.h>
#include <cuda_runtime.h>
using namespace std;

__global__ void vector_simple_change(double *out, double *a, int n) {
    int index = threadIdx.x;
    int stride = blockDim.x;

    for(int i = index; i < n; i += stride){
        out[i] = a[i] + 1.0;
    }
}

int main () {
    int num_lines = 1000;
    double darray[num_lines];
    double out[num_lines]; // For storing final answer
    double value;

    int line_num = 0;
    string line;
    ifstream myfile ("data.txt");
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
          //cout << line << '\n';
          printf("WORKING ON CURRENT LINE: %s\n", line.c_str());
          value = stod(line); // Convert to double
          printf("Setting darray[%d] to %f\n", line_num, value);
          darray[line_num] = value;
          line_num++;
        }
        myfile.close();
    } else
    {
        cout << "Unable to open file";
    }

    for (int array_index = 0; array_index < num_lines; array_index++) {
        printf("darray[%d] = %.17f\n", array_index, darray[array_index]);
    }

    // Allocate device memory on GPU
    double *device_darray;
    double *device_out;
    cudaMalloc((void**)&device_darray, sizeof(double) * num_lines);
    cudaMalloc((void**)&device_out, sizeof(double) * num_lines);

    cudaMemcpy(device_darray, darray, sizeof(double) * num_lines, cudaMemcpyHostToDevice);

    // Executing kernel
    vector_simple_change<<<1,256>>>(device_out, device_darray, num_lines);

    cudaMemcpy(out, device_out, sizeof(double) * num_lines, cudaMemcpyDeviceToHost);

    for (int array_index = 0; array_index < num_lines; array_index++) {
        printf("out[%d] = %.17f\n", array_index, out[array_index]);
    }

    cudaFree(device_darray);
    cudaFree(device_out);

    return 0;
}
