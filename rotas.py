
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#variáveis apresentadas
#ENTRADA
aventura_familia = ctrl.Antecedent(np.arange(0,7,1),'AventuraFamilia')
aventura_familia_romantico = ctrl.Antecedent(np.arange(0,7,1),'AventuraFamiliaRomantico')
aventura = ctrl.Antecedent(np.arange(0,7,1),'Aventura')
familia_historico_religioso = ctrl.Antecedent(np.arange(0,7,1), 'FamiliaHistoricoReligioso')
familia_conforto = ctrl.Antecedent(np.arange(0,7,1),'FamiliaConforto')
romantico = ctrl.Antecedent(np.arange(0,7,1),'Romantico')
familia = ctrl.Antecedent(np.arange(0,7,1),'Familia')
religioso = ctrl.Antecedent(np.arange(0,7,1),'Religioso')
conforto = ctrl.Antecedent(np.arange(0,7,1),'Conforto')

#perfil.automf(names=['Aventureiro','Conforto','Família','Religioso','Romântico','AventuraFamilia','AventuraFamiliaRomantico','FamiliaHistoricoReligioso','FamiliaConforto'])
#SAÍDAS
perfil = ctrl.Consequent(np.arange(0,7,1),'Aventureiro')
perfil = ctrl.Consequent(np.arange(0,7,1),'Conforto')
perfil = ctrl.Consequent(np.arange(0,7,1),'Família')
perfil = ctrl.Consequent(np.arange(0,7,1),'Religioso')
perfil = ctrl.Consequent(np.arange(0,7,1),'Romântico')
perfil = ctrl.Consequent(np.arange(0,7,1),'AventuraFamilia')
perfil = ctrl.Consequent(np.arange(0,7,1),'AventuraFamiliaRomantico')
perfil = ctrl.Consequent(np.arange(0,7,1),'FamiliaHistoricoReligioso')
perfil = ctrl.Consequent(np.arange(0,7,1),'FamiliaConforto')

#mapeando os valores difusos
perfil.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])

#Variaveis assumindo valores 
aventura_familia['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,0,2])
aventura_familia['Acho que não'] = fuzz.trimf(aventura_familia.universe,[0,1,3])
aventura_familia['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[1,2,4])
aventura_familia['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[2,3,5])
aventura_familia['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[3,4,6])

#vizualizando
aventura_familia.view()

#-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-
#REGRAS
