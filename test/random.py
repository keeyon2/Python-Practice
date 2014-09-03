import os
import sys
import subprocess


# def system(*args, **kwargs):
#     kwargs.setdefault('stdout', subprocess.PIPE)
#     proc = subprocess.Popen(args, **kwargs)
#     out, err = proc.communicate()
#     return out

# output = sys('nosetests')
# print output
try:
    subprocess.check_call(["nosetests", "-q"])

except subprocess.CalledProcessError:
    sys.exit(1)

