# Best value: 0.806649

cat_ordered_symtree_par = {'iterations': 142,
                             'learning_rate': 0.09683665466695757,
                             'depth': 5,
                             'l2_leaf_reg': 6.1062838459906335,
                             'random_strength': 0.0012767207201878252,
                             'bagging_temperature': 0.03101414737416228,
                             'border_count': 236
                          }

# Best value: 0.801392

cat_plain_symtree_par = {'iterations': 116,
                         'learning_rate': 0.03145492350963575,
                         'depth': 8,
                         'l2_leaf_reg': 2.6190281798977058,
                         'random_strength': 0.8366568219717394,
                         'bagging_temperature': 0.014683975260008454,
                         'border_count': 68
                        }

# Best value: 0.796825

cat_plain_depthwise_par = {'iterations': 277,
                             'learning_rate': 0.029259087047518634,
                             'depth': 6,
                             'l2_leaf_reg': 0.6029981707854901,
                             'random_strength': 0.47134867978618455,
                             'bagging_temperature': 0.6863865105803352,
                             'border_count': 84
                          }

# Best value: 0.800247

cat_plain_lossguide_par = {'iterations': 85,
                             'learning_rate': 0.006887714325073432,
                             'depth': 7,
                             'l2_leaf_reg': 0.03290262695126801,
                             'random_strength': 0.49755322617522946,
                             'bagging_temperature': 0.09432047676854367,
                             'border_count': 61
                          }

# Best value: 0.813178

cat_reg_ordered_symtree_par = {'iterations': 135,
                                 'learning_rate': 0.037920131339924744,
                                 'depth': 5,
                                 'l2_leaf_reg': 0.00014126451042398354,
                                 'random_strength': 0.030937460295748592,
                                 'bagging_temperature': 0.5954487006531055,
                                 'border_count': 214
                              }

# Best value: 0.803841

cat_reg_plain_symtree_par = {'iterations': 156,
                             'learning_rate': 0.02194842898341571,
                             'depth': 9,
                             'l2_leaf_reg': 6.620397079613212,
                             'random_strength': 0.00046230439250571887,
                             'bagging_temperature': 0.35669526696582043,
                             'border_count': 40
                            }

# Best value: 0.796244

cat_reg_plain_depthwise_par = {'iterations': 235,
                                 'learning_rate': 0.0012912686592075355,
                                 'depth': 8,
                                 'l2_leaf_reg': 0.7493760716808211,
                                 'random_strength': 0.13887141050657445,
                                 'bagging_temperature': 1.4185121453318825,
                                 'border_count': 34
                              }

# Best value: 0.806754

cat_reg_plain_lossguide_par = {'iterations': 135,
                                 'learning_rate': 0.07220871943416828,
                                 'depth': 7,
                                 'l2_leaf_reg': 2.9532816667844127e-05,
                                 'random_strength': 0.0013670287146795317,
                                 'bagging_temperature': 0.0847344970788103,
                                 'border_count': 47
                              }

hist_par = {'learning_rate': 0.045162433853079643,
             'max_depth': 14,
             'min_samples_leaf': 63,
             'l2_regularization': 0.00026804501664776185,
             'max_bins': 192,
             'max_iter': 213
           }

for_par = {'n_estimators': 1356,
             'max_depth': 12,
             'min_samples_split': 93,
             'min_samples_leaf': 34,
             'bootstrap': False,
             'criterion': 'entropy'
          }

# Best value: 0.811279

xgb_params = {'booster': 'dart', 
              'num_boost_round': 68, 
              'eta': 0.044015849416905915, 
              'max_depth': 9, 
              'subsample': 0.7478335707576562, 
              'colsample_bytree': 0.6094558324111821, 
              'min_child_weight': 6, 
              'lambda': 0.0012004732202989827, 
              'alpha': 0.013571510170559338, 
              'gamma': 0.0016844941439451105
}

lgbm_gdbt_par = {'boosting_type': 'gbdt',
                 'num_leaves': 44,
                 'learning_rate': 0.005889963051289158,
                 'feature_fraction': 0.5494228875759491,
                 'bagging_fraction': 0.9157733624508494,
                 'bagging_freq': 5,
                 'min_child_samples': 68,
                 'n_estimators': 485
                }

lgbm_dart_par = {'boosting_type': 'dart', 
                 'num_leaves': 57, 
                 'learning_rate': 0.04056214999415536, 
                 'feature_fraction': 0.4108313894086571, 
                 'bagging_fraction': 0.8413038711426254, 
                 'bagging_freq': 6, 
                 'min_child_samples': 98, 
                 'n_estimators': 490
                }

