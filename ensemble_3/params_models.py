catboost_params = {
                    'iterations': 272,
                    'learning_rate': 0.017889418922277713,
                    'depth': 4,
                    'l2_leaf_reg': 0.1614020668856417,
                    'random_strength': 0.05514685630550458,
                    'bagging_temperature': 5.680830696738555,
                    'border_count': 43,
                    'thread_count': 32,
                    'verbose':0
}

catboost_params_2 = {
                    'iterations': 226,
                    'learning_rate': 0.03116525768097934,
                    'depth': 7,
                    'l2_leaf_reg': 1.4548629938258995,
                    'random_strength': 1.4086022109715814,
                    'bagging_temperature': 6.16286433464338,
                    'border_count': 70,
                    'thread_count': 32,
                    'verbose':0
}

catboost_params_3 = {
                    'learning_rate': 0.04923956131025385,
                    'depth': 8,
                    'l2_leaf_reg': 1.8902827697067257,
                    'random_strength': 0.8279666871647587,
                    'bagging_temperature': 0.0868937857409322,
                    'border_count': 62,
                    'thread_count': 32,
                    'verbose':0,
                    'iterations': 10000,
}

catboost_params_4 = {
                    'iterations': 441,
                    'learning_rate': 0.052267683132673874,
                    'depth': 4,
                    'l2_leaf_reg': 1.0743014408015688,
                    'random_strength': 1.0451266129957824,
                    'bagging_temperature': 6.403646294013038,
                    'border_count': 128,
                    'verbose':0
}

lgb_params = {
                'objective': 'binary',
                'metric': 'auc',
                'boosting_type': 'gbdt',
                'num_leaves': 30,
                'learning_rate': 0.011294244945959157,
                'feature_fraction': 0.7947058191389014,
                'bagging_fraction': 0.8445067742385154,
                'bagging_freq': 2,
                'min_child_samples': 34,
                'verbose': -1,
                'n_jobs' :32,
}

lgb_params_2 = {
                'objective': 'binary',
                'metric': 'auc',
                'boosting_type': 'gbdt',
                'num_leaves': 59,
                'learning_rate': 0.02407647949512364,
                'feature_fraction': 0.540015216008755,
                'bagging_fraction': 0.9177319228569271,
                'bagging_freq': 5,
                'min_child_samples': 60,
                'verbose': -1,
                'n_jobs' :32,
}


lgb_params_3 = {
                'objective': 'binary',
                'metric': 'auc',
                'boosting_type': 'gbdt',
                'num_leaves': 241,
                'learning_rate': 0.0013162227757522857,
                'feature_fraction': 0.5135194759501411,
                'bagging_fraction': 0.8192846381734347,
                'bagging_freq': 3,
                'min_child_samples': 58,
                'n_estimators': 10000,
                'verbose': -1,
                'n_jobs' :32
}

lgb_params_4 = {
                'objective': 'binary',
                'metric': 'auc',
                'boosting_type': 'gbdt',
                'num_leaves': 45,
                'learning_rate': 0.012491790771589944,
                'feature_fraction': 0.8770168107127723,
                'bagging_fraction': 0.6351268514524593,
                'bagging_freq': 1,
                'min_child_samples': 89,
                'n_estimators': 419,
                'verbose': -1,
                'n_jobs' :32
}


hist_boosting_params = {
                'learning_rate': 0.09803780770002858,
                'max_iter': 228,
                'max_depth': 3,
                'min_samples_leaf': 57,
                'l2_regularization': 0.0004425445759081672,
                'max_bins': 150
}

hist_boosting_params_2 = {
                'learning_rate': 0.023304640380408175,
                'max_iter': 263,
                'max_depth': 4,
                'min_samples_leaf': 69,
                'l2_regularization': 0.29014520399147076,
                'max_bins': 247
 }

hist_boosting_params_3 = {
                'learning_rate': 0.0013445401965037187,
                'max_depth': 15,
                'min_samples_leaf': 53,
                'l2_regularization': 0.02453933863767846,
                'max_bins': 163,
                'verbose': 0,
                'early_stopping': True
}

hist_boosting_params_4 = {
                'learning_rate': 0.01642656324213851,
                'max_depth': 15,
                'min_samples_leaf': 74,
                'l2_regularization': 8.65019213323698,
                'max_bins': 251,
                'max_iter': 131
}

forest_params = {
                'n_estimators': 315,
                'max_depth': 12,
                'min_samples_split': 11,
                'min_samples_leaf': 7,
                'bootstrap': False,
                'criterion': 'entropy'
}

xgb_params = {
            'booster': 'dart', 
            'num_boost_round': 326,
            'eta': 0.003200139820105765, 
            'max_depth': 9, 
            'subsample': 0.8582133872101535, 
            'colsample_bytree': 0.8687909303828145, 
            'min_child_weight': 7, 
            'lambda': 0.0039016974676786844, 
            'alpha': 0.09906613783802186, 
            'gamma': 0.017541645920993963
}
