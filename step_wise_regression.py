# Date: 14-01-2019 - First Task: Design generic function for forward selection method
# Date:  - Task: Use correlation metric to decide the most important features from the dataset.
# Date:  - Task: Plot the graph and check the how much percentage AIC got changes and decide the threshold based on that
# Date:  - Task: Implement the dummy variable conversion code
# Date:  - Task: Decide threshold criteria to stop forward selection function
# Date:  - Task: Add few more criteria like comparing AIC in current code to support forward selection method in effective way
# Date:  - Task: Test forward selection method with different dataset and compare with the existing automated function available in R
# Date:  - Task: Implement code to support backward selection method

"""
This module implements Step wise selection methods like:
Forward selection method
Backward selection method
"""

import pandas as pd
import numpy as np
# need import statsmodels library to use OLS to get model metrics
import statsmodels.api as sm


def forward_selection(data, target):
    print("Start of Forward selection")
    target_data = data[target]
    data.drop([target], axis=1, inplace=True)
    features = data.columns
    numeric_features = []
    min_aic_feature = []

    # Take only features with datatype as float or int
    for col in features:
        if data[col].dtype in [np.int8, np.int16, np.int64, np.int32, np.float64, np.float16, np.float32]:
            numeric_features.append(col)

    index = 0
    prev_aic = 0.0
    # we will not consider the last element of the dataset during the step wise selection
    temp_length = len(numeric_features) - 1

    # Below loop help to compare AIC of all features one by one
    while index < temp_length:
        aic_value = {}
        for imp_col in numeric_features:
            temp_features = []
            if index != 0:
                temp_features = min_aic_feature.copy()
            temp_features.append(imp_col)
            ols_model = sm.OLS(target_data, data[temp_features]).fit()
            aic_value.update({imp_col: ols_model.aic})

        current_aic = min(aic_value.items(), key=lambda x: x[1])[1]
        feature_with_min_aic = min(aic_value.items(), key=lambda x: x[1])[0]
        min_aic_feature.append(feature_with_min_aic)
        numeric_features.remove(feature_with_min_aic)

        # Condition to compare AIC value between current OLS model and previous OLS model
        if index != 0:
            if current_aic > prev_aic:
                print("No features left to be selected from the dataset")
                break
        else:
            prev_aic = current_aic
        index += 1
    # return list of import features based on forward selection method
    return min_aic_feature


prop_df = pd.read_csv("../properties_2016_10k.csv")
train_df_temp = pd.read_csv("../train_2016_v2.csv", parse_dates=["transactiondate"])
for clm, dtype in zip(prop_df.columns, prop_df.dtypes):
    if dtype == np.float64:
        prop_df[clm] = prop_df[clm].astype(np.float32)
train_df = prop_df.merge(train_df_temp, how='left', on='parcelid')

del train_df_temp, prop_df
train_df.drop(['transactiondate'], axis=1, inplace=True)
mean_values = train_df.mean(axis=0)
sample_data = train_df.fillna(mean_values)

sample_data.info()
print(forward_selection(sample_data, 'logerror'))
