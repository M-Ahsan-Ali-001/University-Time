# -*- coding: utf-8 -*-
"""DS&A ASSIGMENT _TASK_1 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CwB5SS3DWJu3dkCa-JbjTp00EX36hxd1
"""

from collections import deque

class stack:
    def __init__(self):
        self.prefix=deque()
        self.input=deque()
        self.stk=deque()
   
    def push(self,element):
        self.stk.append(element)
    def pop(self):
        return self.stk.pop()
    def top(self):
        return self.stk[-1]
    def is_empty(self):
        return len(self.stk)==0
    def conversion(self,strg):
        for x in strg:
            self.input.append(x)
        for x in range(0, len(self.input)):
            z=self.input.pop()
            if z in ")]}":
                self.push(z)
            elif z in "asdfghjklqwertyuiopzxcvbnmASDFGHJKLZXCVBNMQWERTYUIOP":
                self.prefix.append(z)
            elif z in "+-/*":
                t=self.top()
                if t in"+-":
                    if z in "+-*/":
                        self.push(z)
                elif t in")}]":
                    self.push(z)
                elif t in "*/":
                    if z in "*/":
                        self.push(z)
                    elif z in "+-":
                        self.prefix.append(self.pop())
                        self.push(z)
                        tp=self.top()
                       
            elif z in "{[(":
                  ln=len(self.stk)
                  for p in range(0,ln):
                    topp=self.top()

                    if topp  in "+-/*":
                      self.prefix.append(self.pop())
                    elif topp in "}])":
                      exit()
                  self.pop()
                        
               
    def pref(self):
            d=len(self.prefix)
            x=d-1
            pprefix=[]
            str=""
            w=len(str)
            if w > 0:
              str=""
              
            for z in range(0,d):
                str=self.prefix.pop()+str
            return(str[::-1])

node=stack()

node.conversion("((AX+B*CY)/(D-E))")
print("Prefix :",node.pref())

node.conversion("((H*((((A+((B+C)*D))*F)*G)*E))+J)")
print("Prefix :",node.pref())

node.conversion("(AX*(BX*(((CY+AY)BY)*CX)))")
print("Prefix :",node.pref())

