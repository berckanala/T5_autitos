import numpy as np

u=176/1000

#-------------------------------------T1
T1=8+u
sit1= np.array([[1,-2],[1,1]])
sit2= np.array([2,T1])
soluyon=np.linalg.solve(sit1,sit2)
print("P1",soluyon)
print("C1",soluyon[0]+10)
print("C2",2*soluyon[1]+12)
print("")
print("-------")
#--------------------------------------T1

#--------------------------------------T2
T1=8+u
sit1= np.array([[1,-2,0],[1,0,-1],[1,1,1]])
sit2= np.array([2,5,T1])
sol=np.linalg.solve(sit1,sit2)
print("P2",sol)
print("C1",sol[0]+10)
print("C2",2*sol[1]+12)
print("C3",sol[2]+15)
print("")
print("-------")
#--------------------------------------T2

#--------------------------------------T3
T1=4+u
sit1= np.array([[1,-2,0],[1,0,-1],[1,1,1]])
sit2= np.array([2,5,T1])
sol=np.linalg.solve(sit1,sit2)
print("P3",sol)
print("Por lo que la ruta h+15 no se ocupa")
T1=4+u
sit1= np.array([[1,-2],[1,1]])
sit2= np.array([2,T1])
sol=np.linalg.solve(sit1,sit2)
print("P3",sol)
print("C1",sol[0]+10)
print("C2",2*sol[1]+12)
print("")
print("")
print("-------")
#--------------------------------------T3

#--------------------------------------T4
TAB=20+u
TBA=10+u
#     a b c d e g
ec1=[-1,1,1,1,0,0] #Costo1=Costo2         
ec2=[ 1,1,1,1,0,0] #flujo AB                   
ec3=[ 0,0,1,0,1,1] #flujo BA                  
ec4=[ 0,-1,1,0,-1,0] #Balance en fc=b+e   
ec5=[ 0,1,0,-1,0,0] #balance fd=fb         
ec6=[ 0,0,0,0,1,-1] #balance fe=fg           
solve=np.array([1,TAB,TBA,0,0,0])
sist=np.array([ec1,ec2,ec3,ec4,ec5,ec6])
soluyon=np.linalg.solve(sist,solve)
print("P4",soluyon)
print("C1", soluyon[1]+5+soluyon[2]+soluyon[3]+8)
print("C2", soluyon[0]+14)
print("C3", soluyon[4]+5+soluyon[2]+soluyon[5]+8)
print("")
print("-------")
#--------------------------------------T4

#--------------------------------------T5


T01 = 200 + 10 * u
T02 = 200 + 10 * u

# Ajuste en las ecuaciones
# Variables: f_a, f_b, f_c, f_d, f_g, f_i, f_j
#     0, 1, 2, 3, 4, 5, 6
#     a, b, c, d, g, i, j
ec1 = [1, -1, 0, 0, 1, -1, 0]  # a + g = b + i
ec2 = [0, 0, 0, -1, 1, -1, 0]  # g = d + i
ec3 = [0, 1, -1, 0, 0, 0, 1]   # c = b + j
ec4 = [-1, 0, 1, -1, 0, 0, -1] # c = d + a + j
ec5 = [1, 1, 0, 1, 1, 1, 0]    # a + b + d + g + i = T01
ec6 = [1, 1, 1, 1, 0, 0, 1]    # c + j = T02
ec8 = [1, 0, 0, 1, -1, 0, 0]   # f_a + f_d = f_g

# Matriz del sistema y el vector solución actualizado
sist= np.array([ec1, ec2, ec3, ec4, ec5, ec6, ec8])
sol = np.array([0, 10, 0, 10, T01, T02, 0])

sol, _, _, _ = np.linalg.lstsq(sist, sol, rcond=None)
print("P5",sol)
print("C1",sol[0]/10+sol[4]/10+2 )
print("C2",sol[1]/10+sol[5]/10+2 )
print("C3",sol[0]/10+sol[5]/10+sol[3]/10+3)
print("C4",sol[2]/10+2)
print("C5",sol[1]/10+sol[6]/10+2)
print("C6",sol[0]/10+sol[3]/10+sol[6]/10+3)



