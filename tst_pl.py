import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model

w=60
un=40
ticker='AAPL'

modelname=f'model1.{un}.{w}.h5'

trset=pd.read_csv(f'{ticker}_D2.csv')
trset=trset[['Close']]
trset=trset.iloc[2:]
trset=trset.tail(100).values

print(trset.shape)

trset=trset.reshape(-1,1)
print(trset.shape[0])
print(trset.shape[1])


sc= MinMaxScaler(feature_range=(0,1))
trai = sc.fit_transform(trset)

X_te=[]
XI=[]
YI=[]
for i in range(70,99):
    X_te.append(trai[i-w:i,0])
    XI.append(trai[i,0])
    YI.append(trai[i+1, 0])

X_te = np.array(X_te)
XI = np.array(XI)
XI=XI.reshape(-1,1)
YI = np.array(YI)
YI=YI.reshape(-1,1)
X_te = np.reshape(X_te, (X_te.shape[0], X_te.shape[1], 1))

model = load_model(f'{modelname}')
PR=model.predict(X_te)

PR = sc.inverse_transform(PR)
XI = sc.inverse_transform(XI)
YI = sc.inverse_transform(YI)
PO = (YI-PR)/XI
DIA= YI-PR
print(f"Διαστάσεις PR: {PR.shape}")
TEST = np.concatenate((XI,YI,PR,PO,DIA), axis=1)
print(XI.shape, YI.shape, PR.shape, PO.shape, DIA.shape)

PO=np.abs(PO)
mop=np.mean(PO)
print(mop)
DIA= np.abs(DIA)
MDIA=np.mean(DIA)
print(MDIA)

df=pd.DataFrame(TEST,columns=['Today_Price','Goal','Predicrion','Ratio','Total_Diffrence'])
print(df.shape)
print(df.head())
df.to_csv(f'{modelname}.csv',index=False)

plt.plot(YI, label='pragmatikh timh', marker='o', color='blue')
plt.plot(PR, label='Problech', marker='x', color='red')
plt.title(f'{modelname} sthn {ticker}')
plt.xlabel("Δείκτες")
plt.ylabel("Τιμές")
plt.show()
plt.savefig(f'{modelname}.png', dpi=300, bbox_inches='tight')

