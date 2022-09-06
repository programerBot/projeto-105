import os
import cv2

path = "C:/Users/USUARIO/Downloads/PRO_1-1_C105_AtividadeDoAluno1-main/PRO_1-1_C105_AtividadeDoAluno1-main/Images/"

image=[]

for elem in os.listdir(path):
    name,extecion=os.path.splitext(elem)
    if extecion in [".gif",".png",".jpg",".jpeg",".jfif"]:
        file_name=path+elem
        image.append(file_name)
print(len(image))
count=len(image)
frame=cv2.imread(image[0])
height,width,channels=frame.shape
size=(width,height)

out=cv2.VideoWriter("kiwi.mp4",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(count-1,0,-1):
    frame=cv2.imread(image[i])
    out.write(frame)

out.release()
print("concluido")




















