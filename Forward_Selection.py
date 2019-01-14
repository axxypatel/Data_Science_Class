import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.tools import add_constant


def forward_selection(data, target):
    print("Start of Forward selection")
    target_data = data[target]
    data.drop([target], axis=1, inplace=True)
    features = data.columns
    numeric_features = []
    non_numeric_features = []
    min_aic_feature = []
    aic_value = {}

    for col in features:
        if data[col].dtype in [np.int8, np.int16, np.int64, np.int32, np.float64, np.float16, np.float32]:
            numeric_features.append(col)
        else:
            non_numeric_features.append(col)
    print("---------------------------------------------------------")
    print("Numeric Variable: \n", numeric_features, '\n\n', "Non Numeric Variable: \n", non_numeric_features)
    print("---------------------------------------------------------")

    i = 0
    length = len(numeric_features)
    while i < length:
        aic_value = {}
        for temp_col in numeric_features:
            temp_features = []
            if i != 0:
                temp_features = min_aic_feature
            temp_features.append(temp_col)
            cstep_ols_model = sm.OLS(target, data[temp_features])
            aic_value.update({temp_col: cstep_ols_model.aic})

        current_aic = 0.0
        next_aic = min(aic_value.items(), key=lambda x: x[1])[1]
        if current_aic > next_aic and i != 0:
            numeric_features.remove(min_aic_feature)
            min_aic_feature.append(min(aic_value.items(), key=lambda x: x[1])[0])
        else:
            current_aic = next_aic

        i += 1


sample_data = pd.read_csv(r'''C:\Users\Akshay\Desktop\MIS\First_Sem\Data_Sci_Eng_Mthd\Assignment3\googleplaystore.csv''',encoding="ISO-8859-1")
sample_data.drop(sample_data.loc[sample_data['Type'] == "0"].index, inplace=True, axis=0)
sample_data.drop(sample_data.loc[sample_data['Installs'] == "0"].index, axis=0, inplace=True)
sample_data.drop(sample_data.loc[sample_data['Rating'].isna()].index, axis=0, inplace=True)
sample_data.drop(sample_data.loc[sample_data['Size'] == "Varies with device"].index, axis=0, inplace=True)

sample_data['Size'] = sample_data['Size'].apply(lambda x : float(x.replace("M", ""))*1024 if "M" in x else float(x.replace("k","")))
sample_data['Reviews'] = sample_data['Reviews'].astype(float)
sample_data.reset_index(drop=True, inplace=True)

values = {'Rating': 0.0, 'Type': 'Free', 'Content Rating': 'Unrated','Price':'0.0'}
sample_data.fillna(value=values, inplace=True)


def price_quality(temp):
    if temp == "0":
        return 0
    else:
        temp = temp[1:]
        temp = float(temp)
        return temp


sample_data['Price'] = sample_data['Price'].map(price_quality).astype(float)
sample_data.drop_duplicates(subset='App', keep='first', inplace=True)
sample_data.drop(columns=['App', 'Last Updated', 'Current Ver', 'Android Ver','Installs'], axis=1, inplace=True)
sample_data.info()
forward_selection(sample_data, 'Rating')
