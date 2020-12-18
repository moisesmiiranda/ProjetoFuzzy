import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#variáveis apresentadas
#ENTRADAS
aventura_familia = ctrl.Antecedent(np.arange(0,6,1),'AventuraFamilia')
aventura_familia_romantico = ctrl.Antecedent(np.arange(0,6,1),'AventuraFamiliaRomantico')
aventura = ctrl.Antecedent(np.arange(0,6,1),'Aventura')
familia_historico_religioso = ctrl.Antecedent(np.arange(0,6,1), 'FamiliaHistoricoReligioso')
familia_conforto = ctrl.Antecedent(np.arange(0,6,1),'FamiliaConforto')
romantico = ctrl.Antecedent(np.arange(0,6,1),'Romantico')
familia = ctrl.Antecedent(np.arange(0,6,1),'Familia')
religioso = ctrl.Antecedent(np.arange(0,6,1),'Religioso')
conforto = ctrl.Antecedent(np.arange(0,6,1),'Conforto')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#SAÍDAS
perfil = ctrl.Consequent(np.arange(0,6,1),'perfil') #saida

#Variaveis textuais para melhor identificar o perfil atraves das questoes
aventura_familia.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])
aventura_familia_romantico.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])
aventura.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])
familia_historico_religioso.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])
familia_conforto.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])
romantico.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])
familia.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])
religioso.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])
conforto.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])

perfil.automf(names=['Aventura','Romantico','Familia','Religioso','Conforto'])
#visualizando
aventura.view()

#-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-
#REGRAS
#A partir das respostas vamos tentar mapear o perfil de cada usuário segundo as regras a seguir:

regra1 = ctrl.Rule(aventura['Sim, quero muito'],perfil['Aventura'])
regra2 = ctrl.Rule(romantico['Sim, quero muito'],perfil['Romantico'])
regra3 = ctrl.Rule(religioso['Sim, quero muito'],perfil['Religioso'])

#Sistema de controle

perfil_ctrl = ctrl.ControlSystem([regra1,regra2,regra3])
perfil_simulator = ctrl.ControlSystemSimulation(perfil_ctrl)

#valores de entrada
perfil_simulator.input['aventura'] = 'Sim, quero muito'
perfil_simulator.input['romantico'] = 'Sim, quero muito'
perfil_simulator.input['religioso'] = 'Sim, quero muito'

#Computando
perfil_simulator.compute()
print(perfil_simulator.output['perfil'])


aventura.view(sim=perfil_simulator)
romantico.view(sim=perfil_simulator)
religioso.view(sim=perfil_simulator)
perfil.view(sim=perfil_simulator)



''' 
nomes dos perfis pra facilitar minha vida

aventura_familia
aventura_familia_romantico
aventura
familia_historico_religioso
familia_conforto
romantico
familia
religioso
conforto

'''
