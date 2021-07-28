Following this tutorial:
https://cuda-tutorial.readthedocs.io/en/latest/tutorials/tutorial02/


ubuntu@ip-172-31-9-40:~/code/aws_ec2/projects/hello_world/tutorial02$ nvcc vector_add_thread.cu -o vector_add_thread
ubuntu@ip-172-31-9-40:~/code/aws_ec2/projects/hello_world/tutorial02$ nvprof ./vector_add_thread
==4064== NVPROF is profiling process 4064, command: ./vector_add_thread
PASSED
==4064== Profiling application: ./vector_add_thread
==4064== Profiling result:
            Type  Time(%)      Time     Calls       Avg       Min       Max  Name
 GPU activities:   41.11%  28.094ms         1  28.094ms  28.094ms  28.094ms  [CUDA memcpy DtoH]
                   34.62%  23.661ms         1  23.661ms  23.661ms  23.661ms  vector_add(float*, float*, float*, int)
                   24.26%  16.581ms         2  8.2907ms  8.2727ms  8.3088ms  [CUDA memcpy HtoD]
      API calls:   77.41%  248.88ms         3  82.960ms  152.88us  248.57ms  cudaMalloc
                   21.65%  69.607ms         3  23.202ms  8.3973ms  52.717ms  cudaMemcpy
                    0.76%  2.4293ms         3  809.77us  203.64us  1.1360ms  cudaFree
                    0.11%  342.19us         1  342.19us  342.19us  342.19us  cuDeviceTotalMem
                    0.06%  179.97us        96  1.8740us     135ns  76.981us  cuDeviceGetAttribute
                    0.01%  29.756us         1  29.756us  29.756us  29.756us  cudaLaunchKernel
                    0.01%  28.293us         1  28.293us  28.293us  28.293us  cuDeviceGetName
                    0.00%  2.6650us         1  2.6650us  2.6650us  2.6650us  cuDeviceGetPCIBusId
                    0.00%  1.4040us         3     468ns     157ns     982ns  cuDeviceGetCount
                    0.00%     944ns         2     472ns     145ns     799ns  cuDeviceGet
                    0.00%     224ns         1     224ns     224ns     224ns  cuDeviceGetUuid


ubuntu@ip-172-31-9-40:~/code/aws_ec2/projects/hello_world/tutorial02$ nvcc vector_add_grid.cu -o vector_add_grid
ubuntu@ip-172-31-9-40:~/code/aws_ec2/projects/hello_world/tutorial02$ nvprof ./vector_add_grid
==4132== NVPROF is profiling process 4132, command: ./vector_add_grid
PASSED
==4132== Profiling application: ./vector_add_grid
==4132== Profiling result:
            Type  Time(%)      Time     Calls       Avg       Min       Max  Name
 GPU activities:   62.32%  28.192ms         1  28.192ms  28.192ms  28.192ms  [CUDA memcpy DtoH]
                   36.66%  16.585ms         2  8.2927ms  8.2905ms  8.2949ms  [CUDA memcpy HtoD]
                    1.01%  459.07us         1  459.07us  459.07us  459.07us  vector_add(float*, float*, float*, int)
      API calls:   82.84%  244.36ms         3  81.454ms  151.82us  244.05ms  cudaMalloc
                   15.77%  46.529ms         3  15.510ms  8.3757ms  29.640ms  cudaMemcpy
                    1.18%  3.4856ms         3  1.1619ms  200.01us  2.1479ms  cudaFree
                    0.12%  356.71us         1  356.71us  356.71us  356.71us  cuDeviceTotalMem
                    0.06%  181.02us        96  1.8850us     136ns  77.630us  cuDeviceGetAttribute
                    0.01%  30.062us         1  30.062us  30.062us  30.062us  cuDeviceGetName
                    0.01%  28.952us         1  28.952us  28.952us  28.952us  cudaLaunchKernel
                    0.00%  2.8620us         1  2.8620us  2.8620us  2.8620us  cuDeviceGetPCIBusId
                    0.00%  1.4160us         3     472ns     174ns  1.0340us  cuDeviceGetCount
                    0.00%     732ns         2     366ns     151ns     581ns  cuDeviceGet
                    0.00%     242ns         1     242ns     242ns     242ns  cuDeviceGetUuid
