# ENGR-113-CV
Design project for Drexel University's ENGR 113 Spring 2019. 

The goal of this project was to manipulate a magnetic sphere through a hydrogel across a circular path.
In context of a real-world problem, the goal is to develop a non-invasive medical device for brain surgery and deep brain stimulation.

The design uses 3D printed housings for a magnet and a petri dish whose relative position to each other can be adjusted using a rail.
The magnet pulls the magnetic sphere in the petri dish in a linear path towards it, but a motor is used to rotate the petri dish to make this path circular. 
To do this, a camera looks top-down onto the petri dish, 
and a Python program uses the video feed to identifiy the positions of the specific circular path (inscribed below the gel) and the magnetic sphere. 
The program then sends instructions to a motor accordingly, such that the sphere is always moving tangent to the circular path.

The blog for the project has videos that demonstrate the design: https://du2019-grp066-05.blogspot.com/
