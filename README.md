# point_project

This project tracks a persons eye location in order to draw a little top head near their head. It depends on the **poseNet** network from **jetson-inference**. 

## The Algorithm

This algorithm gets the distance between the eyes, uses that to find the midpoint between the eyes and draws a line up from there. It is at this location that a hat is drawn. This project uses the CUDA image manipulation library to draw shapes based on the algorithm above.

## Running this project

1. Follow [these](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md) instructions to install the project from source.
2. Download this repo.
3. Change directories into this directory. 
4. Use <code>python3 hat_live.py</code> to run the live demo.

