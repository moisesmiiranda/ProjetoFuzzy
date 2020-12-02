import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Abreviação das variáveis 
# aventura = ave
# familia = fam
# historico = his
# romantico = rom
# religioso = rel
# conforto = con

#variáveis apresentadas
#ENTRADA
aventura_familia = ctrl.Antecedent(np.arange(0,6,1),'AventuraFamilia')
aventura_familia_romantico = ctrl.Antecedent(np.arange(0,6,1),'AventuraFamiliaRomantico')
aventura = ctrl.Antecedent(np.arange(0,6,1),'Aventura')
familia_historico_religioso = ctrl.Antecedent(np.arange(0,6,1), 'FamiliaHistoricoReligioso')
familia_conforto = ctrl.Antecedent(np.arange(0,6,1),'FamiliaConforto')
romantico = ctrl.Antecedent(np.arange(0,6,1),'Romantico')
familia = ctrl.Antecedent(np.arange(0,6,1),'Familia')
religioso = ctrl.Antecedent(np.arange(0,6,1),'Religioso')
conforto = ctrl.Antecedent(np.arange(0,6,1),'Conforto')

#perfil.automf(names=['Aventureiro','Conforto','Família','Religioso','Romântico','AventuraFamilia','AventuraFamiliaRomantico','FamiliaHistoricoReligioso','FamiliaConforto'])
#SAÍDAS
perfil = ctrl.Consequent(np.arange(0,6,1),'Aventureiro')
perfil = ctrl.Consequent(np.arange(0,6,1),'Conforto')
perfil = ctrl.Consequent(np.arange(0,6,1),'Família')
perfil = ctrl.Consequent(np.arange(0,6,1),'Religioso')
perfil = ctrl.Consequent(np.arange(0,6,1),'Romântico')
perfil = ctrl.Consequent(np.arange(0,6,1),'AventuraFamilia')
perfil = ctrl.Consequent(np.arange(0,6,1),'AventuraFamiliaRomantico')
perfil = ctrl.Consequent(np.arange(0,6,1),'FamiliaHistoricoReligioso')
perfil = ctrl.Consequent(np.arange(0,6,1),'FamiliaConforto')

#mapeando os valores difusos
perfil.automf(names=['Definitivamente não','Acho que não','Mais ou menos', 'Gostaria de tentar','Sim, quero muito'])

#Variaveis assumindo valores 
aventura_familia['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,0,1])
aventura_familia['Acho que não'] = fuzz.trimf(aventura_familia.universe,[0,1,2])
aventura_familia['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[0,2,3])
aventura_familia['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[0,3,4])
aventura_familia['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[0,4,5])

aventura_familia_romantico['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,0,1])
aventura_familia_romantico['Acho que não'] = fuzz.trimf(aventura_familia.universe,[0,1,2])
aventura_familia_romantico['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[0,2,3])
aventura_familia_romantico['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[0,3,4])
aventura_familia_romantico['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[0,4,5])

aventura['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,0,1])
aventura['Acho que não'] = fuzz.trimf(aventura_familia.universe,[0,1,2])
aventura['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[0,2,3])
aventura['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[0,3,4])
aventura['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[0,4,5])

familia_historico_religioso['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,0,1])
familia_historico_religioso['Acho que não'] = fuzz.trimf(aventura_familia.universe,[0,1,2])
familia_historico_religioso['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[0,2,3])
familia_historico_religioso['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[0,3,4])
familia_historico_religioso['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[0,4,5])

familia_conforto['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,0,1])
familia_conforto['Acho que não'] = fuzz.trimf(aventura_familia.universe,[0,1,2])
familia_conforto['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[0,2,3])
familia_conforto['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[0,3,4])
familia_conforto['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[0,4,5])

romantico['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,0,1])
romantico['Acho que não'] = fuzz.trimf(aventura_familia.universe,[0,1,2])
romantico['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[0,2,3])
romantico['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[0,3,4])
romantico['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[0,4,5])

familia['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,0,1])
familia['Acho que não'] = fuzz.trimf(aventura_familia.universe,[0,1,2])
familia['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[0,2,3])
familia['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[0,3,4])
familia['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[0,4,5])

religioso['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,0,1])
religioso['Acho que não'] = fuzz.trimf(aventura_familia.universe,[0,1,2])
religioso['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[0,2,3])
religioso['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[0,3,4])
religioso['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[0,4,5])

conforto['Definitivamente não'] = fuzz.trimf(aventura_familia.universe,[0,0,1])
conforto['Acho que não'] = fuzz.trimf(aventura_familia.universe,[0,1,2])
conforto['Mais ou menos'] = fuzz.trimf(aventura_familia.universe,[0,2,3])
conforto['Gostaria de tentar'] = fuzz.trimf(aventura_familia.universe,[0,3,4])
conforto['Sim, quero muito'] = fuzz.trimf(aventura_familia.universe,[0,4,5])
#vizualizando
aventura_familia.view()
#aventura_familia_romantico.view()
#aventura.view()
#familia_historico_religioso.view()
#familia_conforto.view()
#romantico.view()
#familia.view()
#religioso.view()
#conforto.view()
#-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-
#REGRAS


