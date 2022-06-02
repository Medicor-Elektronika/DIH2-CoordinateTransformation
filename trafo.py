import numpy as np
from numpy.linalg import inv
import math

# import input data part later

# Global CS (in mm): center of the bottom cylinder of the robot, X points to the right, where the canopy is located, Y points forward, where the laser cutter is placed and Z point upwards
# The canopy is grabbed at the middle of its top (GP->grab point), while the laser operates under LP (laser point)
# Canopy data


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def is_float(input):
    input = float(input)
    if input < 0.0:
        input = -input
    return isfloat(input)


def check_inputs(gp_data, lp_data):
    if len(gp_data) == 7 and len(lp_data) == 4:
        data_list = gp_data + lp_data
        for data in data_list:
            if not is_float(data):
                return "Non-numerical value"
        return True
    else:
        return "Incorrect amount of data"


def get_coordinates(num):
    str = input()
    list = str.split(';')
    while("" in list):
        list.remove("")
    num_bool = [is_float(x) for x in list]
    if all(num_bool) == True:
        list = [float(x) for x in list]
        if len(list) == num:
            return list
        else:
            msg = "Incorrect amount of data"
            return msg
    else:
        msg = "Not number"
        return msg


def coordinate_transformation(gp_data, lp_data, select_list):

    # used estimated data for GP
    # Gripper=0 #the gripper's length which offsets from the end of the robot
    # GP_x=1000
    # GP_y=0
    # GP_z=500+Gripper

    GP = np.array([[float(gp_data[0]), float(gp_data[4])],
                   [float(gp_data[1]), float(gp_data[5])],
                   [float(gp_data[2])+float(gp_data[3]), float(gp_data[6])]])

    # Estimated laser data

    # LP_x=0
    # LP_y=1300
    # LP_z=1200-Focus
    # Focus=200

    LP = np.array([[float(lp_data[0])],
                   [float(lp_data[1])],
                   [float(lp_data[2])-float(lp_data[3])]])

    # Local CS data: if there is a LCS at GP with the same orientation as GCS, data from model measurements

    xyz_1 = np.array([[234], [-362], [-445]])
    oat_1 = np.array([[math.pi/2], [-math.pi/2], [0]])

    xyz_2 = np.array([[228], [-362], [-78.15]])
    oat_2 = np.array([[math.pi/2], [-math.pi/6], [0]])

    xyz_3 = np.array([[89.43], [-362], [0]])
    oat_3 = np.array([[math.pi/2], [0], [0]])

    xyz_4 = np.array([[-228], [362], [-78.15]])
    oat_4 = np.array([[-math.pi/2], [math.pi/6], [0]])

    xyz_5 = np.array([[-234], [367], [-445]])
    oat_5 = np.array([[-math.pi/2], [math.pi/2], [0]])

    xyz_6 = np.array([[-234], [-367], [-445]])
    oat_6 = np.array([[0], [-math.pi/2], [0]])

    xyz_7 = np.array([[234], [367], [-445]])
    oat_7 = np.array([[0], [math.pi/2], [0]])

    # list of LCS xyz and OAT data
    xyz = np.column_stack(
        (xyz_1, xyz_2, xyz_3, xyz_4, xyz_5, xyz_6, xyz_7))
    oat = np.column_stack(
        (oat_1, oat_2, oat_3, oat_4, oat_5, oat_6, oat_7))
    gcs_xyz = 0

    for i in range(len(xyz[0, :])):
        phi = oat[0, i]
        theta = oat[1, i]
        psi = oat[2, i]

        # ZXZ rotational matrix
        R_phi = np.array([[math.cos(phi), math.sin(
            phi), 0], [-math.sin(phi), math.cos(phi), 0], [0, 0, 1]])
        R_theta = np.array([[1, 0, 0], [0, math.cos(theta), math.sin(theta)], [
            0, -math.sin(theta), math.cos(theta)]])
        R_psi = np.array([[math.cos(psi), math.sin(
            psi), 0], [-math.sin(psi), math.cos(psi), 0], [0, 0, 1]])
        R = np.dot(np.dot(R_phi, R_theta), R_psi)

        # calculating the coordinates in GCS
        gcs_akt = LP + \
            np.reshape(np.dot(R, xyz[:, i]), (len(xyz[:, i]), 1))
        if i == 0:
            gcs_xyz = gcs_akt
        else:
            gcs_xyz = np.column_stack((gcs_xyz, gcs_akt))

        # print(gcs_xyz[:,1])

    print(range(len(gcs_xyz[0, :])))
    for i in range(len(gcs_xyz[0, :])):
        print(select_list[i])
        if select_list[i] == True:
            akt_xyz = np.reshape(gcs_xyz[:, i], (3, 1))
            akt_oat = np.reshape(oat[:, i], (3, 1))
            akt_oat = akt_oat/math.pi*180+np.reshape(GP[:, 1], (3, 1))
            akt = np.column_stack((akt_xyz, akt_oat))
            print(
                "#", i+1, "side coordinates data (xyz [mm], oat [deg]):", "\r")
            print(akt)
