# -*- coding: utf-8 -*-
#   Copyright 2014 Sameer Suhas Marathe
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
.. module:: eulerlib.pythagoras
    :synopsis: Functions related to Pythagorean triplets

.. moduleauthor:: Sameer Marathe

"""
def _xform(t,n):
    """Matrix transform triplet *t* using *n*th matrix (n = 1,2 or 3)"""
    a = 0
    b = 0
    c = 0
    if n == 1:
        a = 1*t[0] -2*t[1] + 2*t[2]
        b = 2*t[0] -1*t[1] + 2*t[2]
        c = 2*t[0] -2*t[1] + 3*t[2]
    elif n==2:
        a = t[0] +2*t[1] + 2*t[2]
        b = 2*t[0] +1*t[1] + 2*t[2]
        c = 2*t[0] +2*t[1] + 3*t[2]
    elif n==3:
        a = -1*t[0] +2*t[1] + 2*t[2]
        b = -2*t[0] +1*t[1] + 2*t[2]
        c = -2*t[0] +2*t[1] + 3*t[2]
    if (b > a):
        return (a,b,c)
    else:
        return (b,a,c)

def _triplet():
    oldstack = [(3,4,5)]
    newstack = []
    while True:
        t0 = oldstack.pop()
        for xcount in range(1,4):
            newstack.append(_xform(t0,xcount))
        if oldstack == []:
            oldstack = newstack
            newstack = []
        yield t0

def first_n_triples(n):
    tgen = _triplet()
    result = [tgen.next() for i in range(n)]
    return result
        
            
        
        
        
        

