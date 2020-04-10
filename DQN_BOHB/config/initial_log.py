import numpy as np
from config.parameter import *

STATE_ZERO = np.zeros(STATE_DIM)

STATE_ONE = np.zeros(STATE_DIM)

STATE_TWO = np.random.rand(STATE_DIM)

'''
STATE_ONE = np.array([-0.,0.,0.,-0.,-0.,-0.,-0.
,0.,1.60886598,-0.,-0.,-0.,0.,-0.
,-0.,-0.,-0.,-0.,-0.,-0.,])    # 피쳐 개수랑 맞춰야 함


STATE_TWO = np.array([-1.87984073,-0.86145484,-0.54868346,1.52073514,0.94928151,-1.03887677
,0.58782494,-0.21568462,-0.48047647,-0.5076974,-0.89917511,-0.23951845
,-0.87805331,3.84582424,-0.,-0.11206599,-0.08779752,-0.15081047, -0.10621548, -0.21568462
])


STATE_ONE = np.array([-0.,0.,0.,-0.,-0.,-0.,-0.
,0.,1.60886598,-0.,-0.,-0.,0.,-0.
,-0.,-0.,-0.,-0.,-0.,-0.,-0.,0.,0.,-0.,-0.,-0.,-0.
,0.,1.60886598,-0.,-0.,-0.,0.,-0.
,-0.,-0.,-0.,-0.,-0.,-0.,0.,-0.,-0.,-0.,-0.,-0.,-0.,-0.])

STATE_TWO = np.array([-1.87984073,-0.86145484,-0.54868346,1.52073514,0.94928151,-1.03887677
,0.58782494,-0.21568462,-0.48047647,-0.5076974,-0.89917511,-0.23951845
,-0.87805331,3.84582424,-0.,-0.11206599,-0.08779752,-0.15081047, -0.10621548, -0.21568462,
-1.87984073,-0.86145484,-0.54868346,1.52073514,0.94928151,-1.03887677
,0.58782494,-0.21568462,-0.48047647,-0.5076974,-0.89917511,-0.23951845
,-0.87805331,3.84582424,-0.,-0.11206599,-0.08779752,-0.15081047, -0.10621548, -0.21568462,
0.58782494,-0.21568462,-0.48047647,-0.5076974,-0.89917511,-0.23951845,0.94928151,-1.03887677
])
'''
TRACKED_STATES = [
	STATE_ZERO,
	STATE_ONE,
	STATE_TWO
]
