from os import getenv as getenv
from os import listdir as listdir
from shutil import copy as copy

def getComputerName():
    setores = ['COPEX', 'DAP', 'CMSTI', 'DOF', 'DGDP', 'DG', 'UA1', 'UA2', 'UA3', 'UA4', 'UA5']
    nomes = ['NTB', 'DSK', 'MINI', 'WORK', 'ULT']
    campus = ['-JP']
    for i in setores:    
        computer_name = getenv('COMPUTERNAME')
    for i in nomes:
        computer_name = computer_name.replace(i, '')
    for i in campus:
        computer_name = computer_name.replace(i, '')
    for i in range(0,9):
        computer_name = computer_name.replace(str(i), '')
    return getSharedFolder(computer_name, setores)

def getSharedFolder(setor, setores):
    pastas = {'COPEX':'copex', 'DAP': 'dap', 'DOF': 'dof', 'DGDP': 'dgdp', 'CMSTI': 'cmsi', 'UA3': 'ua3', 'UAG': 'ua3'}
    dir = listdir("C:/Users/")
    if setor in pastas:
        for i in dir:
            try:
                int(i)
                copy("//10.0.41.8/manutenção/2018/Atalhos das pastas compartilhadas/"+pastas[setor]+" (10.0.7.10).lnk", "C:/Users/"+i+"/Desktop/"+pastas[setor]+".lnk")
            except (ValueError, PermissionError) as ex:
                print(ex)
                print("Pasta: "+i+"\n")
    else:
        print('erro')

getComputerName()