from sympy import false, true

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "initial_id",
   "metadata": {
    "collapsed": true,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:27:16.333488Z",
     "start_time": "2023-10-29T06:27:16.317229Z"
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from joblib import load\n",
    "load_classifier = load('RandomForestClassifier1.joblib')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "outputs": [],
   "source": [
    "data = pd.read_csv('data_preview')\n",
    "data= data.drop(columns=['crop'])\n",
    "\n",
    "X = data.iloc[:,:-1].values\n",
    "y = data.iloc[:,-1].values\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)\n"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:27:16.354146Z",
     "start_time": "2023-10-29T06:27:16.337861Z"
    }
   },
   "id": "168802c9e66612c2"
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "outputs": [],
   "source": [
    "predictions = [tree.test(X_test,y_test) for tree in load_classifier]\n",
    "y_pred_joblib= np.round(np.mean(predictions, axis=0))"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:27:16.386518Z",
     "start_time": "2023-10-29T06:27:16.355722Z"
    }
   },
   "id": "b75a1223c0a04fe8"
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "outputs": [
    {
     "data": {
      "text/plain": "0.771"
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "acc = accuracy_score(y_test,y_pred_joblib)\n",
    "acc"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:27:16.393568Z",
     "start_time": "2023-10-29T06:27:16.389074Z"
    }
   },
   "id": "eeb7e4e0b57523a"
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "outputs": [],
   "source": [],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:27:16.396141Z",
     "start_time": "2023-10-29T06:27:16.394209Z"
    }
   },
   "id": "a6576abc3ef3d5ac"
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
