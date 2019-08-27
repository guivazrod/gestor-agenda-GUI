#!/usr16/331bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:10:33 2019

@author: gvr
"""

""" Fichero principal del programa """

import menu_wx2 as menu

def main(*args):
    print(len(args))
    if len(args) == 0:
        menu.loop('agenda_base.csv')
    else:
        menu.loop(args(0))

if __name__ == "__main__":
    main()
    
