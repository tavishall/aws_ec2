Following this tutorial:
https://cuda-tutorial.readthedocs.io/en/latest/tutorials/tutorial01/

Output from "Compile and run the program" - before using the cudaMalloc() type calls

	ubuntu@ip-172-31-9-40:~/code/aws_ec2/projects/hello_world$ nvcc vector_add.c -o vector_add
	vector_add.c: In function ‘main’:
	vector_add.c:13:19: warning: implicit declaration of function ‘malloc’ [-Wimplicit-function-declaration]
	     a   = (float*)malloc(sizeof(float) * N);
			   ^~~~~~
	vector_add.c:13:19: warning: incompatible implicit declaration of built-in function ‘malloc’
	vector_add.c:13:19: note: include ‘<stdlib.h>’ or provide a declaration of ‘malloc’

Output from compilation and "time ./vector_add"

	ubuntu@ip-172-31-9-40:~/code/aws_ec2/projects/hello_world$ nvcc vector_add.cu -o vector_add
	ubuntu@ip-172-31-9-40:~/code/aws_ec2/projects/hello_world$ time ./vector_add
	out[0] = 3.000000
	PASSED

	real	0m4.430s
	user	0m0.869s
	sys	0m0.222s

Output of nvprof ./vector_add

	ubuntu@ip-172-31-9-40:~/code/aws_ec2/projects/hello_world$ nvprof ./vector_add
	==3776== NVPROF is profiling process 3776, command: ./vector_add
	out[0] = 3.000000
	PASSED
	==3776== Profiling application: ./vector_add
	==3776== Profiling result:
		    Type  Time(%)      Time     Calls       Avg       Min       Max  Name
	 GPU activities:   94.12%  714.73ms         1  714.73ms  714.73ms  714.73ms  vector_add(float*, float*, float*, int)
			    3.70%  28.079ms         1  28.079ms  28.079ms  28.079ms  [CUDA memcpy DtoH]
			    2.18%  16.592ms         2  8.2962ms  8.2882ms  8.3043ms  [CUDA memcpy HtoD]
	      API calls:   78.02%  760.71ms         3  253.57ms  8.3910ms  743.81ms  cudaMemcpy
			   21.68%  211.39ms         3  70.463ms  151.13us  211.07ms  cudaMalloc
			    0.24%  2.2962ms         3  765.40us  199.41us  1.0508ms  cudaFree
			    0.03%  338.18us         1  338.18us  338.18us  338.18us  cuDeviceTotalMem
			    0.02%  179.94us        96  1.8740us     129ns  77.546us  cuDeviceGetAttribute
			    0.00%  29.875us         1  29.875us  29.875us  29.875us  cudaLaunchKernel
			    0.00%  27.780us         1  27.780us  27.780us  27.780us  cuDeviceGetName
			    0.00%  6.8730us         1  6.8730us  6.8730us  6.8730us  cuDeviceGetPCIBusId
			    0.00%  1.4200us         3     473ns     148ns  1.0560us  cuDeviceGetCount
			    0.00%  1.1390us         2     569ns     169ns     970ns  cuDeviceGet
			    0.00%     230ns         1     230ns     230ns     230ns  cuDeviceGetUuid
