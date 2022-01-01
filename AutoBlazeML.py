from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import pandas as pd
import datetime as dt
from datetime import datetime
from time import sleep
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import ExtraTreesClassifier

Data = pd.read_excel('C:/Users/lfsou/Desktop/PROGRAMAÇÃO/Blaze/TOTAL.xlsx')
Data['Dia'] = pd.to_datetime(Data['Dia'])
Data['Hora'] = pd.to_timedelta(Data['Hora'])
Horas = pd.DataFrame(Data['Hora'].dt.total_seconds()).reset_index(drop=True)
Data['Hora'] = Horas['Hora']
Data['Multiplicador'] = (Data['Multiplicador']/0.6)+5
Data.loc[Data.Multiplicador>9.42,'Resultado']=1
Data.loc[Data.Multiplicador<=9.42,'Resultado']=0
Data['Resultado1'] = Data['Resultado'].shift(-2)
Data = Data.drop(['Dia', 'Multiplicador', 'ID', 'Resultado'], axis=1)
Data = Data.dropna()

y = Data['Resultado1']
x = Data.drop('Resultado1', axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)

scaleX = StandardScaler()
x_treino = scaleX.fit_transform(x_treino)
x_teste = scaleX.fit_transform(x_teste)

modelo = ExtraTreesClassifier(n_estimators=60,
                              criterion='gini',
                              max_depth=None,
                              min_samples_split=100,
                              min_samples_leaf=1,
                              min_weight_fraction_leaf=0.0,
                              max_features='auto',
                              max_leaf_nodes=None,
                              min_impurity_decrease=0.0, 
                              bootstrap=False, 
                              oob_score=False, 
                              n_jobs=None, 
                              random_state=None, 
                              verbose=0, 
                              warm_start=False, 
                              class_weight=None, 
                              ccp_alpha=0.0, 
                              max_samples=None)

modelo.fit(x_treino, y_treino)

resultado = modelo.score(x_teste, y_teste)
#print("Acurácia:", (resultado*100))

chromedrive_path = 'C:/Users/lfsou/Desktop/drive/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedrive_path)
webdriver.get('https://blaze.com/pt/games/crash')
options = Options()
options.add_argument('--headless')
cont = 0
Data = []
k = 'o'

x1 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[1]').text
x2 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[2]').text
x3 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[3]').text
x4 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[4]').text
x5 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[5]').text
x6 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[6]').text
x7 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[7]').text
dic1 = {'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'x5': x5, 'x6': x6, 'x7': x7}

while True:
    a = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[2]').text
    b = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[3]').text
    c = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[4]').text
    d = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[5]').text
    e = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[6]').text
    f = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[7]').text
    g = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[8]').text
    dic2 = {'x1': a, 'x2': b, 'x3': c, 'x4': d, 'x5': e, 'x6': f, 'x7': g}
    j = dic1['x1']
    tipo = (type(j) is str)

    if tipo==True and j[-1]=='X':
        try:
            if dic1 == dic2 and j!='' and j!='-' and k=='o':
                k='l'
                try:
                    #Coletando dados para multiplicador diferente de 1
                    jogadores = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[2]/div[1]/div[1]/span[1]').text
                    valor_aposta1 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[2]/div[1]/div[2]/span').text
                    valor_aposta2 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[11]/td[2]/div/span').text
                    if valor_aposta1[:2] != 'R$':
                        valor_aposta1 = 'R$0.0'
                    if valor_aposta2[:2] != 'R$':
                        valor_aposta2 = 'R$0.0'
                except:
                    continue

                cont+=1
                Hora = pd.to_timedelta(str(datetime.now().time())[:-7])
                Hora = pd.DataFrame(({'ID': 1, 'Hora': Hora}), index=[0])
                Horas = pd.DataFrame(Hora['Hora'].dt.total_seconds()).reset_index(drop=True)
                lista = [int(jogadores), float(valor_aposta1[2:]), float(valor_aposta2[2:]), float(Horas['Hora'])]
                Data.append(lista)
                df = pd.DataFrame(Data, columns=['Jogadores', 'Valor_total1', 'Valor_total2', 'Hora'])

                Previsão = df.values
                Previsão = scaleX.fit_transform(Previsão)
                previsões = modelo.predict(Previsão)
                Resultado = pd.DataFrame(previsões, columns=['Prev']).reset_index(drop=True)
                df['Prev'] = Resultado['Prev']
                Mean = df.iloc[-10:]
                Mean = Mean['Prev'].mean()

                if Mean>=0.8:
                    print(Mean,"--> Entrar após uma rodada (Buscar: 1,2)!")
                    sleep(3)
                if Mean>=0.8 and float(x1[2:])<2 and float(x2[2:])<2:
                    print(Mean,"--> Entrar após uma rodada(Buscar: 2)!")
                    sleep(3)
                pass

            if k=='l':
                k='o'
                #Reposição de valores
                x1 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[1]').text
                x2 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[2]').text
                x3 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[3]').text
                x4 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[4]').text
                x5 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[5]').text
                x6 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[6]').text
                x7 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[7]').text
                dic1 = {'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'x5': x5, 'x6': x6, 'x7': x7}
                j = dic1['x1']
            
        except:
            continue

    else:
        x1 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[1]').text
        tipo = (type(x1) is str)
        while tipo!=True and x1[-1]!='X':
            x1 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[1]').text
            tipo = (type(x1) is str)
            if tipo==True and x1[-1]=='X':
                x1 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[1]').text
                x2 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[2]').text
                x3 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[3]').text
                x4 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[4]').text
                x5 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[5]').text
                x6 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[6]').text
                x7 = webdriver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[4]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div/span[7]').text
                dic1 = {'x1': x1, 'x2': x2, 'x3': x3, 'x4': x4, 'x5': x5, 'x6': x6, 'x7': x7}
                break