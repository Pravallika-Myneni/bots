import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

#pyrosim.Send_Cube(name="Box", pos=[0,0,0] , size=[1,1,1])
#pyrosim.Send_Cube(name="Box2", pos=[1,0,1] , size=[1,1,1])

pos_x, pos_y, pos_z = 0,0,1
size_ = [1,1,1]

for tower_1 in range(5):
    for tower_2 in range(5):
        for tower_3 in range(10):
            pyrosim.Send_Cube(name="Box", pos=[pos_x, pos_y, pos_z] , size=size_)
            pos_z +=1
            print(size_)
            size_ = [0.9 * _ for _ in size_]
        pos_y = pos_y+1
        pos_z = 1
        size_ = [1,1,1]
    pos_y = 0
    pos_x +=1

pyrosim.End()