import numpy as np
from scipy.spatial import distance


def product_similarity(m1,m2):     
  if not isinstance(m1, np.ndarray):
    m1 = np.array(m1)
  m1=m1.astype(int)
  if not isinstance(m2, np.ndarray):
    m2 = np.array(m2)
  m2=m2.astype(int)
  
  return m1@m2

def cosine_similarity(m1):
    if not isinstance(m1, np.ndarray):
      m1 = np.array(m1).astype(int)
    m1=m1.astype(int)
    print(m1.shape)
    m2=m1.T
    print(m2.shape)
    sim=np.zeros((m1.shape[0],m1.shape[0]))
    print(sim.shape)
    for i in range(m1.shape[0]):
      for j in range(m2.shape[0]):
        
        sim[i,j]= 1 - distance.cosine(m1[i,:],m2[:,j])

    return sim
