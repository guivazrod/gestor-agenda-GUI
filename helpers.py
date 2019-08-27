#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:08:40 2019

@author: gvr
"""

""" Funciones de ayuda """

import os
import platform
import re


def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def input_text(min_length, max_length):
    while True:
        text = input("> ")
        if len(text) >= min_length and len(text) <= max_length:
            return text

def valida_dni(dni=None):
    return re.match('[0-9]{2}[A-Z]', dni)
