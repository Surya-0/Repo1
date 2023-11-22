#ifndef MLR_h
#define MLR_h

#define n_train 856
#define n_test 215
#define n_epochs 10
#define LR 0.1
#define n_features 32

float X_train[n_train][n_features];

float X_test[n_test][n_features];

float y_train[n_train];

float y_test[n_test];

#endif // !MLR_h