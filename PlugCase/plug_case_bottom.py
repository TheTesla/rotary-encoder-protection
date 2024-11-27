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
    top = cmb.fz_and_chamfer(0.5, solid, -hole, -mc, -sc, -cblhole, -pc)
    


    mcbtm = bd.fz_cuboid((x+8.0,ya,z-6), (33.,20.,14.8),0.5)
    ccbtm = bd.fz_cuboid((x+10.0,ya,z+3), (42.,40.,24.8),0.5)
    bodybtm = bd.fz_cuboid((x+9.5,ya,z-5), (48., 31.,25.), 0.5)
    pcbtm = bd.fz_cuboid((x+22,ya,z-7.4), (8.,30.,16.5),0.5)
    scbtm = bd.fz_cuboid((x-5,ya,z-6.4), (8.,29.,16.5),0.5)
    conhole = bd.fz_circle((min(z,-2)+2+max(z,4)-4,max(ya,7-z/5)-7+z/5),1.5)


    bottom = cmb.fz_and_chamfer(0.5, bodybtm, -top, -mcbtm, -ccbtm, -pcbtm, -scbtm, -conhole, -hole)


    if bottom > 0:
        return False
    return True


render.renderAndSave(f, "case_plug_bottom.stl", 0.3)


