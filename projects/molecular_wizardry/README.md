Some basic C++ and CUDA stuff.

Read a text file - one double per line.
Load into array of doubles.
Add 1.0 to each value in GPU.
Print new values.

```
ubuntu@ip-172-31-15-177:~/code$ nvcc molecular_wizardry.cu -o molecular_wizardry.o
ubuntu@ip-172-31-15-177:~/code$
ubuntu@ip-172-31-15-177:~/code$ nvprof ./molecular_wizardry.o
darray[0] = 72.86701862580325439
darray[1] = 69.22725610844896948
darray[2] = 61.71013070957119595
darray[3] = 80.30825538338874026
darray[4] = 95.44323748643205363
darray[5] = 55.91081117895065944
darray[6] = 93.57420349882387711
darray[7] = 79.70155437519991892
darray[8] = 61.57455545043497835
darray[9] = 63.35522981075484239
==31283== NVPROF is profiling process 31283, command: ./molecular_wizardry.o
out[0] = 73.86701862580325439
out[1] = 70.22725610844896948
out[2] = 62.71013070957119595
out[3] = 81.30825538338874026
out[4] = 96.44323748643205363
out[5] = 56.91081117895065944
out[6] = 94.57420349882387711
out[7] = 80.70155437519991892
out[8] = 62.57455545043497835
out[9] = 64.35522981075484950
==31283== Profiling application: ./molecular_wizardry.o
==31283== Profiling result:
            Type  Time(%)      Time     Calls       Avg       Min       Max  Name
 GPU activities:   50.18%  4.4160us         1  4.4160us  4.4160us  4.4160us  vector_simple_change(double*, double*, int)
                   26.55%  2.3360us         1  2.3360us  2.3360us  2.3360us  [CUDA memcpy DtoH]
                   23.27%  2.0480us         1  2.0480us  2.0480us  2.0480us  [CUDA memcpy HtoD]
      API calls:   99.63%  204.81ms         2  102.41ms  7.0290us  204.81ms  cudaMalloc
                    0.17%  355.62us         1  355.62us  355.62us  355.62us  cuDeviceTotalMem
                    0.09%  189.16us       101  1.8720us     149ns  80.708us  cuDeviceGetAttribute
                    0.05%  103.61us         2  51.806us  9.6650us  93.948us  cudaFree
                    0.02%  39.841us         2  19.920us  15.545us  24.296us  cudaMemcpy
                    0.02%  32.594us         1  32.594us  32.594us  32.594us  cuDeviceGetName
                    0.01%  25.662us         1  25.662us  25.662us  25.662us  cudaLaunchKernel
                    0.00%  6.2500us         1  6.2500us  6.2500us  6.2500us  cuDeviceGetPCIBusId
                    0.00%  1.5660us         3     522ns     194ns  1.1200us  cuDeviceGetCount
                    0.00%     858ns         2     429ns     179ns     679ns  cuDeviceGet
                    0.00%     316ns         1     316ns     316ns     316ns  cuDeviceGetUuid
```
