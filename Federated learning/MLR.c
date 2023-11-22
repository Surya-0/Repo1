// #include <nuttx/config.h>
// #include <sdk/config.h>

// #include <sys/types.h>
// #include <sys/ioctl.h>
// #include <sys/boardctl.h>

#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#include "MLR.h"

// #include <arch/chip/scu.h>
// #include <nuttx/sensors/sht21.h>
// #include <nuttx/board.h>
// #include <sys/ioctl.h>
// #include <sys/fcntl.h>

/*
Load the dataset
Perform train and test split
Perform X_train, X_test, y_train, y_test
Instantiate the Linear Regression model
Under fit operation: 
    Normalize the dataset
    Compute cost
    Optimize
*/

void getSD(float [], float , int , float*);
void getMean(float [], int , float*);

int normalizeXTrain(float X_train[][n_features]);
int normalizeXTest(float X_test[][n_features]);

int populateXTrain(char*);
int populateYTrain(char*);
int populateXTest(char*);
int populateYTest(char*);

void executeMain();
int evaluate(float X_test[n_test][n_features], float y_test[n_test]);
int fit(float X_train[][n_features], float y_train[]);
void updateParameters(float X_train[][n_features], float y_train[], float y_pred[], int arrayLen);
void getCost(float y_train[], float y_pred[], float *cost, int arrayLen);
void getPredictions(float X_train[][n_features], float y_pred[], int arrayLen);


float weights[n_features] = {};
float bias = 0.0;

// print buffer
char printB[1000];

int main()
{
    executeMain();
    return 0;
}

void executeMain(){
    
    // Populate X_train, X_test, y_train and y_test datasets into 2D arrays
    char X_train_path[50], y_train_path[50], X_test_path[50], y_test_path[50];
    sprintf(X_train_path, "new/X_train.txt");
    sprintf(y_train_path, "new/y_train.txt");
    sprintf(X_test_path, "new/X_test.txt");
    sprintf(y_test_path, "new/y_test.txt");

    int ret = -1;
    ret = populateXTrain(X_train_path);
    if(ret != 0){
        printf("File reading error\n");
        return 0;
    }

    ret = populateYTrain(y_train_path);
    if(ret != 0){
        printf("File reading error\n");
        return 0;
    }

    ret = populateXTest(X_test_path);
    if(ret != 0){
        printf("File reading error\n");
        return 0;
    }

    ret = populateYTest(y_test_path);
    if(ret != 0){
        printf("File reading error\n");
        return 0;
    }

    // Normalize X_train and X_test
    // Normalize all columns
    normalizeXTrain(X_train);
    normalizeXTest(X_test);

    printf("Normalization Done!\n\n");
    
    // print normalized dataset
    sprintf(printB, "printing first 5 records of Normalised X_train\n");
    printf("%s", printB);

    // delay(100);

    for(int i=0;i<5;i++){
        sprintf(printB, "%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n", 
                       X_train[i][0],
                       X_train[i][1], 
                       X_train[i][2],
                       X_train[i][3],
                       X_train[i][4],
                       X_train[i][5],
                       X_train[i][6],                        
                       X_train[i][7],
                       X_train[i][8],
                       X_train[i][9],
                       X_train[i][10],
                       X_train[i][11],
                       X_train[i][12], 
                       X_train[i][13],
                       X_train[i][14],
                       X_train[i][15],
                       X_train[i][16],
                       X_train[i][17],                        
                       X_train[i][18],
                       X_train[i][19],
                       X_train[i][20],
                       X_train[i][21],
                       X_train[i][22],
                       X_train[i][23], 
                       X_train[i][24],
                       X_train[i][25],
                       X_train[i][26],
                       X_train[i][27],
                       X_train[i][28],                        
                       X_train[i][29],
                       X_train[i][30],
                       X_train[i][31]);

       printf("%s", printB);
       // delay(100);

    }

    // delay(100);

    sprintf(printB, "printing first 5 records of Normalised X_test\n");
    printf("%s", printB);

    // delay(100);

    for(int i=0;i<5;i++){
        sprintf(printB, "%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n", 
                       X_test[i][0],
                       X_test[i][1], 
                       X_test[i][2],
                       X_test[i][3],
                       X_test[i][4],
                       X_test[i][5],
                       X_test[i][6],                        
                       X_test[i][7],
                       X_test[i][8],
                       X_test[i][9],
                       X_test[i][10],
                       X_test[i][11],
                       X_test[i][12], 
                       X_test[i][13],
                       X_test[i][14],
                       X_test[i][15],
                       X_test[i][16],
                       X_test[i][17],                        
                       X_test[i][18],
                       X_test[i][19],
                       X_test[i][20],
                       X_test[i][21],
                       X_test[i][22],
                       X_test[i][23], 
                       X_test[i][24],
                       X_test[i][25],
                       X_test[i][26],
                       X_test[i][27],
                       X_test[i][28],                        
                       X_test[i][29],
                       X_test[i][30],
                       X_test[i][31]);
        
        printf("%s", printB);
        // delay(100);
    }
    
    // Initialize weights and bias - Declared at the beginning
    sprintf(printB, "initializing weights and biases\n");
    printf("%s", printB);
    for(int i=0;i<n_features;i++){
        weights[i] = (float)(rand() % 10);
    }

    // make predictions n_epochs times on the train data, compute cost and update parameters
    ret = -1;
    ret = fit(X_train, y_train);
    if(ret == 0){
        sprintf(printB, "Training complete\n");
        printf("%s", printB);
    }

    ret = -1;
    ret = evaluate(X_test, y_test);
    if(ret == 0){
        sprintf(printB, "Testing complete\n");
        printf("%s", printB);
    }
    // return;
}

int evaluate(float X_test[n_test][n_features], float y_test[n_test]){
    
    sprintf(printB, "TEST PHASE\n");
    printf("%s", printB);

    // calculate cost on test dataset
    float y_pred[n_test];
    float cost = 0.0;
    for(int i=0;i<n_test;i++){
        y_pred[i] = 0.0;
    }
    sprintf(printB, "array initialization done\n");
    printf("%s", printB);

    getPredictions(X_test, y_pred, n_test);

    // printf("printing first 5 predictions\n");
    // for(int i=0;i<5;i++){
    //     sprintf(printB, "%f ",y_pred[i]);
    //     printf("%s", printB);
    // }
    // sprintf(printB, "\n\n");
    // printf("%s", printB);

    getCost(y_test, y_pred, &cost, n_test);
    // delay(1 * 1000);

    sprintf(printB, "X_test cost: %f\n", cost);
    printf("%s", printB);

    return 0;
}

int fit(float X_train[][n_features], float y_train[]){
    
    sprintf(printB, "TRAINING PHASE\n");
    printf("%s", printB);

    float y_pred[n_train];
    for(int i=0;i<n_train;i++){
        y_pred[i] = 0.0;
    }

    for(int epoch = 1; epoch <= n_epochs; epoch++){

        getPredictions(X_train, y_pred, n_train);
        
        // sprintf(printB, "printing first 5 predictions\n");
        // printf("%s", printB);

        // for(int i=0;i<5;i++){
        //     sprintf(printB, "%f ",y_pred[i]);
        //     printf("%s", printB);
        // }
        // sprintf(printB, "\n\n");
        // printf("%s", printB);

        // get accuracy as well
        float cost = 0.0;
        // float trainAccuracy = 0.0;
        getCost(y_train, y_pred, &cost, n_train);
        // getAccuracy(y_train, y_pred, n_train, &trainAccuracy);

        sprintf(printB, "iteration: %d, cost: %f\n", epoch, cost);
        // sprintf(printB, "iteration: %d, cost: %f, TrainingAccuracy: %f\n", epoch, cost, trainAccuracy * 100.0);
        printf("%s", printB);

        // optimise weights and bias
        updateParameters(X_train, y_train, y_pred, n_train);
        
        // sprintf(printB, "printing weights\n");
        // printf("%s", printB);

        // for(int i=0;i<n_features;i++){
        //     sprintf(printB, "%f, ",weights[i]);
        //     printf("%s", printB);
        // }
        // sprintf(printB, "bias: %f\n",bias);
        // printf("%s", printB);

        // delay(1 * 1000);

    }
    // getPredictions(X_train, y_pred, n_train);
    // sprintf(printB, "printing first 5 predictions\n");
    // printf("%s", printB);

    // for(int i=0;i<5;i++){
    //     sprintf(printB, "%f ",y_pred[i]);
    //     printf("%s", printB);
    // }

    // sprintf(printB, "\n\n");
    // printf("%s", printB);

    return 0;
}

// mapping each prediction to nerest interger and finding accuracy
// void getAccuracy(float y_train[], float y_pred[], int arrayLen, float* trainAccuracy){
    
//     float tot = 0.0;
//     float actual = 0.0;
//     for(int i=0;i<arrayLen;i++){
//         float diff = y_pred[i] - (int)y_pred[i];
//         if(diff >= 0.50){
//             actual = ceil(y_pred[i]);
//         }
//         else{
//             actual = floor(y_pred[i]);
//         }

//         if(y_train[i] == actual){
//             tot += 1.0;
//         }
//     }
//     *trainAccuracy = (float) (tot / arrayLen);
// }

void updateParameters(float X_train[][n_features], float y_train[], float y_pred[], int arrayLen){
    // for each feature, dot product it with the (predicted-actual) array and divide by n_train

    // update weights
    // sprintf(printB, "Updating weights\n");
    // printf("%s", printB);

    float errorArr[n_train];
    float db = 0.0;
    for(int i=0;i<arrayLen;i++){
        errorArr[i] = 0.0;
    }

    for(int i=0;i<arrayLen;i++){
        errorArr[i] = y_pred[i] - y_train[i];
        db += (errorArr[i]);
    }
    db = (float) (db / arrayLen) * (-2);


    // sprintf(printB, "printing first 5 error array values\n");
    // printf("%s", printB);

    // for(int i=0;i<5;i++){
    //     sprintf(printB, "%f, ", errorArr[i]);
    //     printf("%s", printB);
    // }

    // sprintf(printB, "\n");
    // printf("%s", printB);

    for(int feature = 0; feature < n_features; feature++){
        float singleColumn[n_train];

        for(int i=0;i<arrayLen;i++){
            singleColumn[i] = X_train[i][feature];
        }
        float dw = 0.0;
        for(int i=0;i<arrayLen;i++){
            dw += (singleColumn[i]*errorArr[i]);
        }
        dw = (float) (dw / arrayLen) * (-2);

        // for(int i=0;i<n_features;i++){
        //     weights[i] = weights[i] - LR*dw;
        // }
        weights[feature] = weights[feature] - LR * dw;

        // delay(100);
    }
    
    // // delay(2000);
    // sprintf(printB, "Updating Bias\n");
    // printf("%s", printB);

    bias = bias - db * LR;

    // delay(1000);

    // sprintf(printB, "Weight and Bias updation completed\n");
    // printf("%s", printB);

}

void getCost(float y_train[], float y_pred[], float *cost, int arrayLen){
    
    float result = 0.0;
    for(int i=0;i<arrayLen;i++){
        result += pow(y_train[i] - y_pred[i], 2);
    }
    result = result / (arrayLen);
    *cost = result;
    // delay(1 * 1000);

    // sprintf(printB, "Value of cost inside getCost(): %f\n", *cost);
    // printf("%s", printB);

}

void getPredictions(float X_train[][n_features], float y_pred[], int arrayLen){
    // For each record (of length n_features) in the train dataset
    // Multiply with correspinding weight values and add bias
    // Store the prediction in y_pred

    for(int i=0;i<arrayLen;i++){
        y_pred[i] = (X_train[i][0] * weights[0] + 
                    X_train[i][1] * weights[1] +
                    X_train[i][2] * weights[2] +
                    X_train[i][3] * weights[3] +
                    X_train[i][4] * weights[4] +
                    X_train[i][5] * weights[5] +
                    X_train[i][6] * weights[6] +
                    X_train[i][7] * weights[7] +
                    X_train[i][8] * weights[8] +
                    X_train[i][9] * weights[9] +
                    X_train[i][10] * weights[10] +
                    X_train[i][11] * weights[11] + 
                    X_train[i][12] * weights[12] +
                    X_train[i][13] * weights[13] +
                    X_train[i][14] * weights[14] +
                    X_train[i][15] * weights[15] +
                    X_train[i][16] * weights[16] +
                    X_train[i][17] * weights[17] +
                    X_train[i][18] * weights[18] +
                    X_train[i][19] * weights[19] +
                    X_train[i][20] * weights[20] +
                    X_train[i][21] * weights[21] +
                    X_train[i][22] * weights[22] + 
                    X_train[i][23] * weights[23] +
                    X_train[i][24] * weights[24] +
                    X_train[i][25] * weights[25] +
                    X_train[i][26] * weights[26] +
                    X_train[i][27] * weights[27] +
                    X_train[i][28] * weights[28] +
                    X_train[i][29] * weights[29] +
                    X_train[i][30] * weights[30] +
                    X_train[i][31] * weights[31] +
                    bias);
    }
    // printf("printing first 5 predictions inside getPredictions()\n");
    // for(int i=0;i<5;i++){
    //     sprintf(printB, "%f ",y_pred[i]);
    //     printf("%s", printB);
    // }
    // delay(1 * 1000);
}

// Normalization code
int normalizeXTrain(float X_train[][n_features]){

    printf("Normalizing X_train dataset\n");
    int arrayLen = n_train;

    for(int feature = 0; feature < n_features; ++feature){

        float singleColumn[n_train];
        for(int i=0;i<arrayLen;i++){
            singleColumn[i] = 0.0;
        }

        for(int i=0;i<arrayLen;i++){
            singleColumn[i] = X_train[i][feature];
        }
        // sprintf(printB, "printing singleColumn array values\n");
        // printf("%s", printB);

        // for(int i=0;i<5;i++){
        //     sprintf(printB, "feature-%d singleColumn[%d]=%f\n", feature, i, singleColumn[i]);
        //     printf("%s", printB);
        // }

        float mean = 0.0;
        getMean(singleColumn, arrayLen, &mean);
        // sprintf(printB, "mean-%d: %f\n", feature+1, mean);
        // printf("%s", printB);

        float std;
        getSD(singleColumn, mean, arrayLen, &std);
        // sprintf(printB, "std-%d: %f\n", feature+1, std);
        // printf("%s", printB);

        // Only if the standard deviation is not equal to 0.0, standarize the column
        // else, skip standardization of that column
        if(std != 0.0){
            for(int i=0;i<arrayLen;i++){
                X_train[i][feature] = (X_train[i][feature] - mean) / std;
            }
        }

        // delay(1000);

    }

    return 0;
}

int normalizeXTest(float X_test[][n_features]){

    printf("Normalizing X_test dataset\n");
    int arrayLen = n_test;

    for(int feature = 0; feature < n_features; feature++){

        float singleColumn[n_test];
        for(int i=0;i<arrayLen;i++){
            singleColumn[i] = 0.0;
        }

        for(int i=0;i<arrayLen;i++){
            singleColumn[i] = X_test[i][feature];
        }
        // sprintf(printB, "printing singleColumn array values\n");
        // printf("%s", printB);
        // for(int i=0;i<5;i++){
        //     sprintf(printB, "feature-%d singleColumn[%d]=%f\n", feature, i, singleColumn[i]);
        //     printf("%s", printB);
        // }
        
        float mean = 0.0;
        getMean(singleColumn, arrayLen, &mean);
        // sprintf(printB, "mean-%d: %f\n", feature+1, mean);
        // printf("%s", printB);

        float std = 0.0;
        getSD(singleColumn, mean, arrayLen, &std);
        // sprintf(printB, "std-%d: %f\n", feature+1, std);
        // printf("%s", printB);

        // Only if the standard deviation is not equal to 0.0, standarize the column
        // else, skip standardization of that column
        if(std != 0.0){
            for(int i=0;i<arrayLen;i++){
                X_test[i][feature] = (X_test[i][feature] - mean) / std;
            }
        }
        // delay(1000);

    }
    return 0;
    
}

void getSD(float array[], float mean, int arrayLen, float* std){
    // size_t arrayLen = sizeof(array)/sizeof(array[0]);
    // printf("array len: %d\n", arrayLen);
    float x = 0.0;
    float result = 0.0;
    for (int i = 0; i < arrayLen; ++i) {
        x += (float) pow(array[i] - mean, 2);
    }

    result = sqrt(x / arrayLen);
    *std = result;
    // delay(500);

    // sprintf(printB, "value of sd in function: %f\n", *std);
    // printf("%s", printB);
}

void getMean(float array[], int arrayLen, float* mean){
    float sum = 0.0;
    float result = 0.0;
    // size_t arrayLen = sizeof(array)/sizeof(array[0]);
    // printf("array len: %d\n", arrayLen);
    for(int i=0;i<arrayLen;i++){
        sum += array[i];
    }
    result = (float)(sum / arrayLen);
    *mean = result;
    // delay(500);

    // sprintf(printB, "value of mean in function: %f\n", *mean);
    // printf("%s", printB);
}

// Pupulating the structure code
int populateXTrain(char* X_train_path){
    
    // Populating X_train
    int i = 0;
    FILE* inputfile;
    printf("Reading X_train data\n");
    inputfile = fopen(X_train_path,"r");
    if(inputfile == NULL)
    {   
        printf("Error in opening file\n");
        return -1;
    }
    while(fscanf(inputfile, "%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n",
                &X_train[i][0],
                &X_train[i][1], 
                &X_train[i][2],
                &X_train[i][3],
                &X_train[i][4],
                &X_train[i][5],
                &X_train[i][6],                        
                &X_train[i][7],
                &X_train[i][8],
                &X_train[i][9],
                &X_train[i][10],
                &X_train[i][11],
                &X_train[i][12], 
                &X_train[i][13],
                &X_train[i][14],
                &X_train[i][15],
                &X_train[i][16],
                &X_train[i][17],                        
                &X_train[i][18],
                &X_train[i][19],
                &X_train[i][20],
                &X_train[i][21],
                &X_train[i][22],
                &X_train[i][23], 
                &X_train[i][24],
                &X_train[i][25],
                &X_train[i][26],
                &X_train[i][27],
                &X_train[i][28],                        
                &X_train[i][29],
                &X_train[i][30],
                &X_train[i][31]) != EOF)
                {
                    i += 1;
                }
    
    printf("X_train head\n");
    for(int i=0;i<5;i++){
        printf("%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n",
                X_train[i][0],
                X_train[i][1], 
                X_train[i][2],
                X_train[i][3],
                X_train[i][4],
                X_train[i][5],
                X_train[i][6],                        
                X_train[i][7],
                X_train[i][8],
                X_train[i][9],
                X_train[i][10],
                X_train[i][11],
                X_train[i][12], 
                X_train[i][13],
                X_train[i][14],
                X_train[i][15],
                X_train[i][16],
                X_train[i][17],                        
                X_train[i][18],
                X_train[i][19],
                X_train[i][20],
                X_train[i][21],
                X_train[i][22],
                X_train[i][23], 
                X_train[i][24],
                X_train[i][25],
                X_train[i][26],
                X_train[i][27],
                X_train[i][28],                        
                X_train[i][29],
                X_train[i][30],
                X_train[i][31]);
    }
    fclose(inputfile);
    return 0;
}

int populateYTrain(char* y_train_path){
    
    // Populating y_train
    int i = 0;
    FILE* inputfile;
    printf("Reading y_train data\n");
    inputfile = fopen(y_train_path, "r");
    if(inputfile == NULL)
    {   
        printf("Error in opening file\n");
        return -1;
    }
    while(fscanf(inputfile, "%f\n", &y_train[i]) != EOF){
        // printf("%f\n", y_train[i]);
        i += 1;
    }
    fclose(inputfile);
    return 0;
}

int populateXTest(char* X_test_path){
    // Populating X_test
    int i = 0;
    FILE* inputfile;
    printf("Reading X_test data\n");    
    inputfile = fopen(X_test_path,"r");
    if(inputfile == NULL)
    {   
        printf("Error in opening file\n");
        return -1;
    }
    while(fscanf(inputfile, "%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n",
                &X_test[i][0],
                &X_test[i][1], 
                &X_test[i][2],
                &X_test[i][3],
                &X_test[i][4],
                &X_test[i][5],
                &X_test[i][6],                        
                &X_test[i][7],
                &X_test[i][8],
                &X_test[i][9],
                &X_test[i][10],
                &X_test[i][11],
                &X_test[i][12], 
                &X_test[i][13],
                &X_test[i][14],
                &X_test[i][15],
                &X_test[i][16],
                &X_test[i][17],                        
                &X_test[i][18],
                &X_test[i][19],
                &X_test[i][20],
                &X_test[i][21],
                &X_test[i][22],
                &X_test[i][23], 
                &X_test[i][24],
                &X_test[i][25],
                &X_test[i][26],
                &X_test[i][27],
                &X_test[i][28],                        
                &X_test[i][29],
                &X_test[i][30],
                &X_test[i][31]) != EOF)
                {
                    i += 1;
                }

    printf("X_test head\n");
    for(int i=0;i<5;i++){
        printf("%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n",
                X_test[i][0],
                X_test[i][1], 
                X_test[i][2],
                X_test[i][3],
                X_test[i][4],
                X_test[i][5],
                X_test[i][6],                        
                X_test[i][7],
                X_test[i][8],
                X_test[i][9],
                X_test[i][10],
                X_test[i][11],
                X_test[i][12], 
                X_test[i][13],
                X_test[i][14],
                X_test[i][15],
                X_test[i][16],
                X_test[i][17],                        
                X_test[i][18],
                X_test[i][19],
                X_test[i][20],
                X_test[i][21],
                X_test[i][22],
                X_test[i][23], 
                X_test[i][24],
                X_test[i][25],
                X_test[i][26],
                X_test[i][27],
                X_test[i][28],                        
                X_test[i][29],
                X_test[i][30],
                X_test[i][31]);
    }
    
    fclose(inputfile);
    return 0;
}

int populateYTest(char* y_test_path){
    // Populating y_test
    int i = 0;
    FILE* inputfile;
    printf("Reading y_test data\n");
    inputfile = fopen(y_test_path, "r");
    if(inputfile == NULL)
    {   
        printf("Error in opening file\n");
        return -1;
    }
    while(fscanf(inputfile, "%f\n", &y_test[i]) != EOF){
        // printf("%f\n", y_test[i]);
        i += 1;
    }
    fclose(inputfile);
    return 0;
}

// void getR2Score(struct Y_record* y_test, float y_pred_test[], int arrayLen, float* R2){
    
//     float num = 0.0, deno = 0.0, y_mean = 0.0, actualSum = 0.0;
//     // sum(actual - predicted)^2
//     for(int i=0;i<arrayLen;i++){
//         num += (pow((y_test[i].result - y_pred_test[i]), 2));
//         actualSum += (y_test[i].result);
//     }    
//     // sum(actual - avg(actual))^2
//     y_mean = (float)(actualSum / arrayLen);
//     for(int i=0;i<arrayLen;i++){
//         deno += (pow((y_test[i].result - y_mean), 2));
//     }
//     printf("num = %f, deno = %f\n", num, deno);
//     *R2 =  1 - (num/deno);
// }
