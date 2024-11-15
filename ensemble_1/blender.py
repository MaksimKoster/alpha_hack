import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score



def calculate_prediction(preds, ws):
    prediction = np.zeros(preds[0].shape)
    for i in range(len(ws)):
        prediction += ws[i] * preds[i]
    return prediction

def get_composition(it, weights_cnt, y_train, preds):
    
    print(f'Started iteration {it}')
    np.random.seed(13+it)
    
    preds = preds.copy()
    y_true = y_train.copy()
    
    preds = [preds[:, i] for i in range(preds.shape[1])]

    best_sc = -1
    es_rounds = 2
    
    # Initial weights are equal
    ws = np.array([1] * weights_cnt) / weights_cnt

    while True:
        flags = [False] * len(ws)
        # Work with coordinates-weights in random order
        for idx in np.random.permutation(len(ws)):
            best_w = None
            for w in np.arange(0, 1, 0.01):
                # Update weights
                new_ws = ws.copy()
                new_ws[idx] = 0
                new_ws = new_ws / new_ws.sum() * (1 - w)
                new_ws[idx] = w

                # Calculate predictions
                prediction = calculate_prediction(preds, new_ws)
                
                
                sc = roc_auc_score(y_true, prediction)
                
    
                if sc > best_sc:
                    best_sc = sc
                    best_w = w
            
            if best_w is not None:
                # Update weights
                flags[idx] = True
                print(f'Update weight idx = {idx} from {ws[idx]} to {best_w}. Best score updates to {best_sc}')
                ws[idx] = 0
                ws = ws / ws.sum() * (1 - best_w)
                ws[idx] = best_w
                print(f'New weights = {ws}, their sum = {ws.sum()}')
                assert np.abs(ws.sum() - 1) < 1e-6
            else:
                print(f'No update for {idx}')
                pass

        # Early stopping
        if sum(flags) == 0:
            es_rounds -= 1
        else:
            es_rounds = 2

        # Exit if no improvement for 2 full rounds
        if es_rounds == 0:
            break

    # Final blend and scoring
    prediction = calculate_prediction(preds, ws)
    sc = roc_auc_score(y_true, prediction)
    print('Iteration {}, best weights score: {:.5f}'.format(it, sc))

    return (it, sc, ws)