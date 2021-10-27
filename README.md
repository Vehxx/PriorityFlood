# PriorityFlood

### Overview
A simple and efficient depression-filling algorithm for Digital Elevation Models (DEMs). Priority Flood is a Pythonic implementation of 'Improved Priority Flood', described in the paper here: https://arxiv.org/pdf/1511.04463.pdf.
 
The algorithm accepts a Digital Elevation Model in the form of a 2D array of values which correspond to the height at that location, it returns a DEM which is free of internally-draining pits and digital dams. All locations which are not able to drain to the edge of the model are raised to a level which allows them to drain to a lower elevation.

Below is a before and after comparison of a heightmap which was run through the algorithm. The values in the heightmap were filled with fractal noise to emulate terrain.

![fill_comparison](https://user-images.githubusercontent.com/10524511/138981607-4d13fa2a-23fd-4794-908b-2c369a60c748.png)

This is the same comparison, rendered in 3D using the Cycles Engine.

![fill_comparison_render](https://user-images.githubusercontent.com/10524511/138981609-c6e3c197-b208-4619-afdb-4be801e9fc10.png)

### Efficiency

The algorithm works in O(n) time for DEMs with integer values and O(n log n) time for floating point data. This is the fastest time-complexity achieved for any depression-filling algorithm.

### The Algorithm

Priority Flood works by making use of both a priority queue and a plain queue. The priority queue is initialized with the locations at the edges of the DEM. locations with lower elevations are prioritized. The DEM is progressively flooded by pushing neighbors of each location in the priority queue into either the priority queue or the plain queue. Locations which are lower in elevation to the current cell are pushed to the plain queue because they have the same priority as the cell which pushed them. This improves efficiency drastically, due to the fact that a plain queue has a time-complexity of O(1). The algorithm runs until both of the queues are empty.
