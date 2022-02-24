Output of device properties code

    ubuntu@ip-172-31-7-76:~/code/aws_ec2/projects/cuda_by_example/device_properties$ nvcc device_properties.cu -o device_properties
    ubuntu@ip-172-31-7-76:~/code/aws_ec2/projects/cuda_by_example/device_properties$ ./device_properties
    Found 1 CUDA devices.
      --- General Info for device 0 ---
    Name: Tesla T4
    Compute capability: 7.5
    Clock rate: 1590000
    Device copy overlap: Enabled
    Kernel execition timeout: Disabled
      --- Memory Information for Device 0 ---
    Total global memory: 15843721216
    Total constant memory: 65536
    Max mem pitch: 2147483647
    Texture Alignment: 512
      --- MP Information for device 0 ---
    Multiprocessor count: 40
    Shared mem per mp: 49152
    Registers per mp: 65536
    Threads in warp: 32
    Max threads per block: 1024
    Max thread dimensions: (1024, 1024, 64)
    Max grid dimensions: (2147483647, 65535, 65535)
