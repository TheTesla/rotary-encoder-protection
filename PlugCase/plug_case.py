#!/usr/bin/env python3

from numba import njit
from fuzzyometry import bodies as bd
from fuzzyometry import combinations as cmb
from xyzcad import render


@njit
def fz_top(x, y, z):
    ya = abs(y)
    mp = bd.fz_circle((abs(x+8)-6,ya-12.0),1.2)
    hole = bd.fz_circle((z-1,ya-12.5),1.6)
    cblhole = bd.fz_circle((min(x,9)-9,y),2.3)
    mc = bd.fz_cuboid((x,ya,z-4), (60.,20.,14.8),0.5)
    pc = bd.fz_cuboid((x+25,ya,z-7.4), (14.,31.,6.5),0.5)
    sc = bd.fz_cuboid((x-5,ya,z-6.4), (8.,29.,6.5),0.5)
    body = bd.fz_cuboid((x+8.0,ya,z-1), (38.,31.,12.8),1.5)
    solid = cmb.fz_or_chamfer(0.5, body, cmb.fz_and_chamfer(0.5, mp, z-13, -z))
    return cmb.fz_and_chamfer(0.5, solid, -hole, -mc, -sc, -cblhole, -pc)

@njit
def case_top(x, y, z):
    if  fz_top(x, y, z) > 0:
        return False
    return True



@njit
def case_bottom(x, y, z):
    if abs(z) > 25:
        return False
    ya = abs(y)

    hole = bd.fz_circle((z-1,ya-12.5),1.6)
    top = fz_top(x, y, z)

    mcbtm = bd.fz_cuboid((x+8.0,ya,z-6), (33.,20.,14.8),0.5)
    ccbtm = bd.fz_cuboid((x+10.0,ya,z+3), (42.,40.,24.8),0.5)
    bodybtm = bd.fz_cuboid((x+9.5,ya,z-6), (48., 31.,23.), 1.5)
    pcbtm = bd.fz_cuboid((x+22,ya,z-7.4), (8.,30.,16.5),0.5)
    scbtm = bd.fz_cuboid((x-5,ya,z-6.4), (8.,29.,16.5),0.5)
    conholeinf = bd.fz_circle((min(z,-2)+2+max(z,4)-4,max(ya,7-z/5)-7+z/5),1.5)
    conhole = cmb.fz_and_chamfer(0.5, conholeinf, x)

    bottom = cmb.fz_and_chamfer(0.5, bodybtm, 0.1-top, -mcbtm, -ccbtm, -pcbtm, -scbtm, -conhole, -hole)

    if bottom > 0:
        return False
    return True

res = 0.2
render.renderAndSave(case_top, "case_plug_top.stl", res)
render.renderAndSave(case_bottom, "case_plug_bottom.stl", res)


