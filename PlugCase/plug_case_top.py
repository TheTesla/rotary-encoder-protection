#!/usr/bin/env python3

from numba import njit
from fuzzyometry import bodies as bd
from fuzzyometry import combinations as cmb
from xyzcad import render

@njit
def f(x, y, z):
    if abs(z) > 25:
        return False
    ya = abs(y)
    mp = bd.fz_circle((abs(x+8)-6,ya-12.0),1.2)
    hole = bd.fz_circle((z-1,ya-12.5),1.6)
    cblhole = bd.fz_circle((min(x,7)-7,y),2.7)
    mc = bd.fz_cuboid((x,ya,z-2), (60.,20.,14.8),0.5)
    pc = bd.fz_cuboid((x+25,ya,z-7.4), (16.,31.,6.5),0.5)
    sc = bd.fz_cuboid((x-5,ya,z-6.4), (8.,29.,6.5),0.5)
    body = bd.fz_cuboid((x+8.0,ya,z), (38.,31.,14.8),0.5)
    solid = cmb.fz_or_chamfer(0.5, body, cmb.fz_and_chamfer(0.5, mp, z-13, -z))
    if  cmb.fz_and_chamfer(0.5, solid, -hole, -mc, -sc, -cblhole, -pc) > 0:
        return False
    return True


render.renderAndSave(f, "case_plug_top.stl", 0.2)


