import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

ticker='AAPL'
trset=pd.read_csv(f'{ticker}_D1.csv')
trset=trset[['Close']]
trset=trset.iloc[2:]
print(trset.head())

sc= MinMaxScaler(feature_range=(0,1))
trainset=sc.fit_transform(trset)

ep=50
b=32
Stat=[]
testset = pd.read_csv(f'{ticker}_D2.csv')
testset = testset[['Close']]
testset = testset.iloc[2:]
testset = testset.tail(100).values
testset = testset.reshape(-1, 1)
sc = MinMaxScaler(feature_range=(0, 1))
trai = sc.fit_transform(testset)

for w in (50,60):
    X_te = []
    XI = []
    YI = []
    for i in range(70, 99):
        X_te.append(trai[i - w:i, 0])
        XI.append(trai[i, 0])
        YI.append(trai[i + 1, 0])

    X_te = np.array(X_te)
    XI = np.array(XI)
    XI = XI.reshape(-1, 1)
    YI = np.array(YI)
    YI = YI.reshape(-1, 1)

    for un in (40,50):
        X_train=[]
        Y_train=[]
        for i in range (w,1258):
            X_train.append(trainset[i-w:i,0])
            Y_train.append(trainset[i,0])

        X_train=np.array(X_train)
        Y_train=np.array(Y_train)
        X_train=np.reshape(X_train, (X_train.shape[0],X_train.shape[1],1))

        # edw 8a mpoun oi entoles {if} kai mia akomh {for} [[ {for mod in models} {if mod =='modi' }]]
        # gia ta models sth periptwsh poy 8eloume peraiterv parametropoihsh ths diadikasias
        # oso anafora thn arxitektonikh twn layers ((grammes 61 -70)).

        regressor = Sequential()
        regressor.add(LSTM(units=un,return_sequences=True ,input_shape=(X_train.shape[1],1)))
        regressor.add(Dropout(0.2))
        regressor.add(LSTM(units=un,return_sequences=True))
        regressor.add(Dropout(0.2))
        regressor.add(LSTM(units=un))
        regressor.add(Dropout(0.2))
        regressor.add(Dense(units =1))
        regressor.compile(optimizer='adam',loss='mean_squared_error' )
        regressor.fit(X_train,Y_train,epochs=ep,batch_size=b)
        modelname=f'model1.{un}.{w}.h5'

        regressor.save(modelname)

        #apo edw kai katw 8a einai gia ka8e montelo idio

        PR =regressor.predict(X_te)
        PR = sc.inverse_transform(PR)
        XI = sc.inverse_transform(XI)
        YI = sc.inverse_transform(YI)
        PO = (np.abs(YI - PR)) / XI
        DIA = np.abs(YI - PR)
        apmop=np.abs(PO)
        apmop=np.mean(apmop)
        mop=np.mean(PO)
        apmodiaf=np.abs(DIA)
        apmodiaf = np.mean(apmodiaf)
        modiaf=np.mean(DIA)
        Stat.append((modelname, mop,apmop,modiaf,apmodiaf))
        TEST = np.concatenate((XI, YI, PR, PO, DIA), axis=1)
        print(TEST)


df=pd.DataFrame(Stat,columns=['Modelname','Meso_pososto','Apolyto.mop','Mesh_diafora','Mesh_diafora'] )
df.to_csv('statistik.csv')