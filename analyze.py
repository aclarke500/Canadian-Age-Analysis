import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from make_population import tally, x_values


# make dataframe
xdic ={'ages': x_values}
ydic ={'frequency': tally}

X=pd.DataFrame.from_dict(xdic)
y=pd.DataFrame.from_dict(ydic)

# set up domain and range for display
X_seq = np.linspace(X.min(),X.max(),300).reshape(-1,1)

degree=9
polyreg=make_pipeline(PolynomialFeatures(degree),LinearRegression())
polyreg.fit(X,y)

plt.figure()
plt.scatter(X,y, color='red')
plt.plot(X_seq,polyreg.predict(X_seq),color="purple")
plt.title("Polynomial regression with degree "+str(degree))
plt.xlabel("Age of Canadians")
plt.ylabel("Frequency of occurence in simulation")
plt.show()