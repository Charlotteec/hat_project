# point_project

This project tracks a persons shoulder and wrist locations and draws a dot on the screen where the person is pointing. It works on both left and right arms. It depends on the **poseNet** network from **jetson-inference**. 

## The Algorithm

This algorithm gets the vector between the shoulder and wrist, and uses that to create a dot further from the wrist indicating what direction the person is pointing. This project uses the CUDA image manipulation library to draw a dot based on the above algorithm. 

## Running this project

1. Follow [these](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md) instructions to install the project from source.
2. Download this repo.
3. Change directories into this directory. 
4. Use <code>python3 point_live.py</code> to run the live demo.

