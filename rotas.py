
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
aventura_familia['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,1,1])
aventura_familia['Acho que não'] = fuzz.trimf(aventura_familia.universe,[1,2,3])
aventura_familia['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[2,3,4])
aventura_familia['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[3,4,5])
aventura_familia['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[5,5,6])

aventura_familia_romantico['Definitivamente não'] = fuzz.trimf(aventura_familia_romantico.universe,[0,1,1])
aventura_familia_romantico['Acho que não'] = fuzz.trimf(aventura_familia_romantico.universe,[1,2,3])
aventura_familia_romantico['Mais ou menos'] = fuzz.trimf(aventura_familia_romantico.universe,[2,3,4])
aventura_familia_romantico['Gostaria de tentar'] = fuzz.trimf(aventura_familia_romantico.universe,[3,4,5])
aventura_familia_romantico['Sim, quero muito'] = fuzz.trimf(aventura_familia_romantico.universe,[5,5,6])

aventura['Definitivamente não'] = fuzz.trimf(aventura.universe,[0,1,1])
aventura['Acho que não'] = fuzz.trimf(aventura.universe,[1,2,3])
aventura['Mais ou menos'] = fuzz.trimf(aventura.universe,[2,3,4])
aventura['Gostaria de tentar'] = fuzz.trimf(aventura.universe,[3,4,5])
aventura['Sim, quero muito'] = fuzz.trimf(aventura.universe,[5,5,6])

familia_historico_religioso['Definitivamente não'] = fuzz.trimf(familia_historico_religioso.universe,[0,1,1])
familia_historico_religioso['Acho que não'] = fuzz.trimf(familia_historico_religioso.universe,[1,2,3])
familia_historico_religioso['Mais ou menos'] = fuzz.trimf(familia_historico_religioso.universe,[2,3,4])
familia_historico_religioso['Gostaria de tentar'] = fuzz.trimf(familia_historico_religioso.universe,[3,4,5])
familia_historico_religioso['Sim, quero muito'] = fuzz.trimf(familia_historico_religioso.universe,[5,5,6])

familia_conforto['Definitivamente não'] = fuzz.trimf(familia_conforto.universe,[0,1,1])
familia_conforto['Acho que não'] = fuzz.trimf(familia_conforto.universe,[1,2,3])
familia_conforto['Mais ou menos'] = fuzz.trimf(familia_conforto.universe,[2,3,4])
familia_conforto['Gostaria de tentar'] = fuzz.trimf(familia_conforto.universe,[3,4,5])
familia_conforto['Sim, quero muito'] = fuzz.trimf(familia_conforto.universe,[5,5,6])

romantico['Definitivamente não'] = fuzz.trimf(romantico.universe,[0,1,1])
romantico['Acho que não'] = fuzz.trimf(romantico.universe,[1,2,3])
romantico['Mais ou menos'] = fuzz.trimf(romantico.universe,[2,3,4])
romantico['Gostaria de tentar'] = fuzz.trimf(romantico.universe,[3,4,5])
romantico['Sim, quero muito'] = fuzz.trimf(romantico.universe,[5,5,6])

familia['Definitivamente não'] = fuzz.trimf(familia.universe,[0,1,1])
familia['Acho que não'] = fuzz.trimf(familia.universe,[1,2,3])
familia['Mais ou menos'] = fuzz.trimf(familia.universe,[2,3,4])
familia['Gostaria de tentar'] = fuzz.trimf(familia.universe,[3,4,5])
familia['Sim, quero muito'] = fuzz.trimf(familia.universe,[5,5,6])

religioso['Definitivamente não'] = fuzz.trimf(religioso.universe,[0,1,1])
religioso['Acho que não'] = fuzz.trimf(religioso.universe,[1,2,3])
religioso['Mais ou menos'] = fuzz.trimf(religioso.universe,[2,3,4])
religioso['Gostaria de tentar'] = fuzz.trimf(religioso.universe,[3,4,5])
religioso['Sim, quero muito'] = fuzz.trimf(religioso.universe,[5,5,6])

conforto['Definitivamente não'] = fuzz.trimf(conforto.universe,[0,1,1])
conforto['Acho que não'] = fuzz.trimf(conforto.universe,[1,2,3])
conforto['Mais ou menos'] = fuzz.trimf(conforto.universe,[2,3,4])
conforto['Gostaria de tentar'] = fuzz.trimf(conforto.universe,[3,4,5])
conforto['Sim, quero muito'] = fuzz.trimf(conforto.universe,[5,5,6])

#vizualizando
aventura_familia.view()

#-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-
#REGRAS
