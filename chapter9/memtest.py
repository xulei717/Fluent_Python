# -*- coding:utf-8 -*-
# @time   : 2019-12-20 13:27
# @author : xulei
# @project: Fluent_Python

import importlib
import sys
import resource

NUM_VECTORS = 10**7

if len(sys.argv) == 2:
    module_name = sys.argv[1].replace('.py', '')
    # module_name = "Vector2d"
    module = importlib.import_module(module_name)
else:
    print('Usage: {} <vector-module-to-test>'.format())
    sys.exit(1)

fmt = 'Selected Vector2d type: {.__name__}.{.__name__}'
print(fmt.format(module, module.Vector2d))

mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('Creating {:,} Vector2d instances'.format(NUM_VECTORS))

vectors = [module.Vector2d(3.0, 4.0) for i in range(NUM_VECTORS)]

mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('Initial RAM usages: {:14,}'.format(mem_init))
print('  Final RAM usages: {:14,}'.format(mem_final))

'''
$python3 memtest.py c9_7-8-9-10_vector2d_v3.py 
Selected Vector2d type: c9_7-8-9-10_vector2d_v3.Vector2d
Creating 10,000,000 Vector2d instances
Initial RAM usages:          9,448
  Final RAM usages:      1,753,700

$python3 memtest.py c9_11_vector2d_v3.py
Selected Vector2d type: c9_11_vector2d_v3.Vector2d
Creating 10,000,000 Vector2d instances
Initial RAM usages:          9,456
  Final RAM usages:        643,240
'''
