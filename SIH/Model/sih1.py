from sympy import true, false

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "initial_id",
   "metadata": {
    "collapsed": true,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:18.888233Z",
     "start_time": "2023-10-29T06:58:18.023449Z"
    }
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "outputs": [
    {
     "data": {
      "text/plain": "        crop  moisture  temp  pump\n0     cotton       758    45     0\n1     cotton       996    20     1\n2     cotton       395    45     1\n3     cotton       798    45     1\n4     cotton       713    19     1\n...      ...       ...   ...   ...\n4995  cotton       846    45     1\n4996  cotton      1013    33     0\n4997  cotton       570    24     0\n4998  cotton      1008    13     1\n4999  cotton       971    26     1\n\n[5000 rows x 4 columns]",
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>crop</th>\n      <th>moisture</th>\n      <th>temp</th>\n      <th>pump</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>cotton</td>\n      <td>758</td>\n      <td>45</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>cotton</td>\n      <td>996</td>\n      <td>20</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>cotton</td>\n      <td>395</td>\n      <td>45</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>cotton</td>\n      <td>798</td>\n      <td>45</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>cotton</td>\n      <td>713</td>\n      <td>19</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>4995</th>\n      <td>cotton</td>\n      <td>846</td>\n      <td>45</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4996</th>\n      <td>cotton</td>\n      <td>1013</td>\n      <td>33</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>4997</th>\n      <td>cotton</td>\n      <td>570</td>\n      <td>24</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>4998</th>\n      <td>cotton</td>\n      <td>1008</td>\n      <td>13</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4999</th>\n      <td>cotton</td>\n      <td>971</td>\n      <td>26</td>\n      <td>1</td>\n    </tr>\n  </tbody>\n</table>\n<p>5000 rows × 4 columns</p>\n</div>"
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('data_preview')\n",
    "df"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:18.898639Z",
     "start_time": "2023-10-29T06:58:18.888586Z"
    }
   },
   "id": "5a15350d5315141a"
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "outputs": [
    {
     "data": {
      "text/plain": "1    3501\n0    1499\nName: pump, dtype: int64"
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['pump'].value_counts()"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:18.902802Z",
     "start_time": "2023-10-29T06:58:18.900362Z"
    }
   },
   "id": "191ca5388f6cf994"
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "outputs": [],
   "source": [
    "df = df.drop(columns=['crop'])"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:18.905533Z",
     "start_time": "2023-10-29T06:58:18.903809Z"
    }
   },
   "id": "70a0bb0004bb12f8"
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "outputs": [
    {
     "data": {
      "text/plain": "      moisture  temp  pump\n0          758    45     0\n1          996    20     1\n2          395    45     1\n3          798    45     1\n4          713    19     1\n...        ...   ...   ...\n4995       846    45     1\n4996      1013    33     0\n4997       570    24     0\n4998      1008    13     1\n4999       971    26     1\n\n[5000 rows x 3 columns]",
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>moisture</th>\n      <th>temp</th>\n      <th>pump</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>758</td>\n      <td>45</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>996</td>\n      <td>20</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>395</td>\n      <td>45</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>798</td>\n      <td>45</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>713</td>\n      <td>19</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>4995</th>\n      <td>846</td>\n      <td>45</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4996</th>\n      <td>1013</td>\n      <td>33</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>4997</th>\n      <td>570</td>\n      <td>24</td>\n      <td>0</td>\n    </tr>\n    <tr>\n      <th>4998</th>\n      <td>1008</td>\n      <td>13</td>\n      <td>1</td>\n    </tr>\n    <tr>\n      <th>4999</th>\n      <td>971</td>\n      <td>26</td>\n      <td>1</td>\n    </tr>\n  </tbody>\n</table>\n<p>5000 rows × 3 columns</p>\n</div>"
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:18.919710Z",
     "start_time": "2023-10-29T06:58:18.907625Z"
    }
   },
   "id": "a3e971f97cfd38f9"
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "outputs": [],
   "source": [
    "\n",
    "X = df.iloc[:,:-1].values\n",
    "y = df.iloc[:,-1].values"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:18.920007Z",
     "start_time": "2023-10-29T06:58:18.911843Z"
    }
   },
   "id": "aeb1f7955a3e903c"
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20,random_state=42)"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:19.556593Z",
     "start_time": "2023-10-29T06:58:18.914511Z"
    }
   },
   "id": "98b0d9262214703c"
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "outputs": [
    {
     "data": {
      "text/plain": "array([[1022,   23],\n       [   4,   26],\n       [ 909,   29],\n       ...,\n       [ 869,   16],\n       [   4,   44],\n       [1022,   35]])"
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:19.561146Z",
     "start_time": "2023-10-29T06:58:19.557223Z"
    }
   },
   "id": "90da21ce3bbcba1b"
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "outputs": [
    {
     "data": {
      "text/plain": "array([1, 0, 1, ..., 1, 1, 1])"
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_train"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:19.562739Z",
     "start_time": "2023-10-29T06:58:19.559877Z"
    }
   },
   "id": "7e772041dda36f33"
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "outputs": [],
   "source": [
    "class Perceptron_RMSProp_BCE:\n",
    "    def __init__(self, learning_rate=0.001, num_epochs=2000, decay_rate=0.9, epsilon=1e-7):\n",
    "        self.learning_rate = learning_rate\n",
    "        self.num_epochs = num_epochs\n",
    "        self.decay_rate = decay_rate\n",
    "        self.epsilon = epsilon\n",
    "        self.moving_avg_sq_b = 0\n",
    "        self.moving_avg_sq_w = 0\n",
    "\n",
    "    def sigmoid(self, z):\n",
    "        return 1 / (1 + np.exp(-z))\n",
    "\n",
    "    def predicted(self, X):\n",
    "        linear_model = np.dot(X, self.weights) + self.bias\n",
    "        pred = self.sigmoid(linear_model)\n",
    "        return pred\n",
    "\n",
    "    def fit(self, X, y):\n",
    "\n",
    "        num_samples, num_features = X.shape\n",
    "        self.weights = np.zeros(num_features)\n",
    "        self.bias = 0\n",
    "\n",
    "        for i in range(self.num_epochs):\n",
    "            y_pred = self.predicted(X)\n",
    "            term = y_pred - y\n",
    "            dw = (1 / num_samples) * np.dot(X.T, term)\n",
    "            db = (1 / num_samples) * np.sum(term)\n",
    "\n",
    "            # Update the moving average of squared gradients\n",
    "            self.moving_avg_sq_w = self.decay_rate * self.moving_avg_sq_w + (1 - self.decay_rate) * (dw ** 2)\n",
    "            self.moving_avg_sq_b = self.decay_rate * self.moving_avg_sq_b + (1 - self.decay_rate) * (db ** 2)\n",
    "\n",
    "            # Update weights and bias using RMS prop\n",
    "            self.weights -= (self.learning_rate / (np.sqrt(self.moving_avg_sq_w + self.epsilon))) * dw\n",
    "            self.bias -= (self.learning_rate / (np.sqrt(self.moving_avg_sq_b + self.epsilon))) * db\n",
    "\n",
    "    def test(self, X, y):\n",
    "        Y_predtest = self.predicted(X)\n",
    "        Y_values = Y_predtest\n",
    "        correct = 0\n",
    "        total = len(y)\n",
    "        for i in range(len(Y_predtest)):\n",
    "            if Y_predtest[i] > 0.5:\n",
    "                Y_predtest[i] = 1\n",
    "            else:\n",
    "                Y_predtest[i] = 0\n",
    "        for i in range(len(y)):\n",
    "            if y[i] == Y_predtest[i]:\n",
    "                correct += 1\n",
    "        return Y_predtest\n"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:19.568929Z",
     "start_time": "2023-10-29T06:58:19.565223Z"
    }
   },
   "id": "d7b47f7233846f7c"
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "outputs": [],
   "source": [
    "class Perceptron_RMSProp_RMSE:\n",
    "    def __init__(self, learning_rate=0.001, num_epochs=2000, decay_rate=0.9, epsilon=1e-7):\n",
    "        self.bias = None\n",
    "        self.weights = None\n",
    "        self.learning_rate = learning_rate\n",
    "        self.num_epochs = num_epochs\n",
    "        self.decay_rate = decay_rate\n",
    "        self.epsilon = epsilon \n",
    "        self.moving_avg_sq_b = 0\n",
    "        self.moving_avg_sq_w = 0\n",
    "\n",
    "\n",
    "    def sigmoid(self, z):\n",
    "        return 1 / (1 + np.exp(-z))\n",
    "\n",
    "    def sigmoid_prime(self, z):\n",
    "        return self.sigmoid(z) * (1 - self.sigmoid(z))\n",
    "\n",
    "    def predicted(self, X):\n",
    "        linear_model = np.dot(X, self.weights) + self.bias\n",
    "        pred = self.sigmoid(linear_model)\n",
    "        return pred\n",
    "\n",
    "    def sigmoid_prime_predictor(self, X):\n",
    "        linear_model = np.dot(X, self.weights) + self.bias\n",
    "        pred = self.sigmoid_prime(linear_model)\n",
    "        return pred\n",
    "\n",
    "    def fit(self, X, y):\n",
    "\n",
    "        num_samples, num_features = X.shape\n",
    "        self.weights = np.zeros(num_features)\n",
    "        self.bias = 0\n",
    "\n",
    "        for i in range(self.num_epochs):\n",
    "            y_pred = self.predicted(X)\n",
    "            sp = self.sigmoid_prime_predictor(X)\n",
    "            term = ((y_pred - y) * sp).astype('float')\n",
    "            dw = (1 / num_samples) * np.dot(X.T, term)\n",
    "            db = (1 / num_samples) * sum(term)\n",
    "\n",
    "            # Update the moving average of squared gradients\n",
    "            self.moving_avg_sq_w = self.decay_rate * self.moving_avg_sq_w + (1 - self.decay_rate) * (dw ** 2)\n",
    "            self.moving_avg_sq_b = self.decay_rate * self.moving_avg_sq_b + (1 - self.decay_rate) * (db ** 2)\n",
    "\n",
    "            # Update weights and bias using  RmsProp\n",
    "            self.weights -= (self.learning_rate / (np.sqrt(self.moving_avg_sq_w + self.epsilon))) * dw\n",
    "            self.bias -= (self.learning_rate / (np.sqrt(self.moving_avg_sq_b + self.epsilon))) * db\n",
    "\n",
    "    def test(self, X, y):\n",
    "        Y_predtest = self.predicted(X)\n",
    "        Y_values = Y_predtest\n",
    "        correct = 0\n",
    "        total = len(y)\n",
    "        for i in range(len(Y_predtest)):\n",
    "            if Y_predtest[i] > 0.5:\n",
    "                Y_predtest[i] = 1\n",
    "            else:\n",
    "                Y_predtest[i] = 0\n",
    "        for i in range(len(y)):\n",
    "            if y[i] == Y_predtest[i]:\n",
    "                correct += 1\n",
    "        return Y_predtest\n"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:19.575051Z",
     "start_time": "2023-10-29T06:58:19.570372Z"
    }
   },
   "id": "515213178a2a06f1"
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "outputs": [],
   "source": [
    "class Perceptron_adam_BCE:\n",
    "    def __init__(self, learning_rate=0.001, num_epochs=2000, decay_rate1=0.9,decay_rate2 = 0.999, epsilon=1e-7):\n",
    "        self.bias = None\n",
    "        self.weights = None\n",
    "        self.learning_rate = learning_rate\n",
    "        self.num_epochs = num_epochs\n",
    "        self.decay_rate1 = decay_rate1\n",
    "        self.decay_rate2 = decay_rate2\n",
    "        self.epsilon = epsilon\n",
    "        self.moving_avg_sq_b = 0\n",
    "        self.moving_avg_sq_w = 0\n",
    "        self.first_momentum_w = 0\n",
    "        self.first_momentum_b = 0\n",
    "\n",
    "\n",
    "    def sigmoid(self, z):\n",
    "        return 1 / (1 + np.exp(-z))\n",
    "\n",
    "\n",
    "    def predicted(self, X):\n",
    "        linear_model = np.dot(X, self.weights) + self.bias\n",
    "        pred = self.sigmoid(linear_model)\n",
    "        return pred\n",
    "\n",
    "\n",
    "    def fit(self, X, y):\n",
    "\n",
    "        num_samples, num_features = X.shape\n",
    "        self.weights = np.zeros(num_features)\n",
    "        self.bias = 0\n",
    "        prev_v_w,prev_v_b,gamma = 0,0,0.9\n",
    "        for i in range(self.num_epochs):\n",
    "            y_pred = self.predicted(X)\n",
    "            term = y_pred - y\n",
    "            dw = (1 / num_samples) * np.dot(X.T, term)\n",
    "            db = (1 / num_samples) * np.sum(term)\n",
    "\n",
    "\n",
    "            # Update the moving average of squared gradients\n",
    "            self.moving_avg_sq_w = self.decay_rate2 * self.moving_avg_sq_w + (1 - self.decay_rate2) * (dw ** 2)\n",
    "            self.moving_avg_sq_b = self.decay_rate2 * self.moving_avg_sq_b + (1 - self.decay_rate2) * (db ** 2)\n",
    "\n",
    "            self.first_momentum_w = self.decay_rate1 * self.first_momentum_w + (1 - self.decay_rate1)*dw\n",
    "            self.first_momentum_b = self.decay_rate1 * self.first_momentum_b + (1 - self.decay_rate1)*db\n",
    "\n",
    "\n",
    "            # Update weights and bias using  adam\n",
    "            self.weights -= (self.learning_rate / (np.sqrt(self.moving_avg_sq_w + self.epsilon))) * self.first_momentum_w\n",
    "            self.bias -= (self.learning_rate / (np.sqrt(self.moving_avg_sq_b + self.epsilon))) * self.first_momentum_b\n",
    "\n",
    "    def test(self, X, y):\n",
    "        Y_predtest = self.predicted(X)\n",
    "        Y_values = Y_predtest\n",
    "        correct = 0\n",
    "        total = len(y)\n",
    "        for i in range(len(Y_predtest)):\n",
    "            if Y_predtest[i] > 0.5:\n",
    "                Y_predtest[i] = 1\n",
    "            else:\n",
    "                Y_predtest[i] = 0\n",
    "        for i in range(len(y)):\n",
    "            if y[i] == Y_predtest[i]:\n",
    "                correct += 1\n",
    "        return Y_predtest\n"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:19.578704Z",
     "start_time": "2023-10-29T06:58:19.576269Z"
    }
   },
   "id": "6d2bfd8bf2efb5f1"
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "outputs": [],
   "source": [
    "class Perceptron_adam_RMSE:\n",
    "    def __init__(self, learning_rate=0.001, num_epochs=2000, decay_rate1=0.9,decay_rate2 = 0.999, epsilon=1e-7):\n",
    "        self.bias = None\n",
    "        self.weights = None\n",
    "        self.learning_rate = learning_rate\n",
    "        self.num_epochs = num_epochs\n",
    "        self.decay_rate1 = decay_rate1\n",
    "        self.decay_rate2 = decay_rate2\n",
    "        self.epsilon = epsilon\n",
    "        self.moving_avg_sq_b = 0\n",
    "        self.moving_avg_sq_w = 0\n",
    "        self.first_momentum_w = 0\n",
    "        self.first_momentum_b = 0 \n",
    "\n",
    "\n",
    "    def sigmoid(self, z):\n",
    "        return 1 / (1 + np.exp(-z))\n",
    "\n",
    "    def sigmoid_prime(self, z):\n",
    "        return self.sigmoid(z) * (1 - self.sigmoid(z))\n",
    "\n",
    "    def predicted(self, X):\n",
    "        linear_model = np.dot(X, self.weights) + self.bias\n",
    "        pred = self.sigmoid(linear_model)\n",
    "        return pred\n",
    "\n",
    "    def sigmoid_prime_predictor(self, X):\n",
    "        linear_model = np.dot(X, self.weights) + self.bias\n",
    "        pred = self.sigmoid_prime(linear_model)\n",
    "        return pred\n",
    "\n",
    "    def fit(self, X, y):\n",
    "\n",
    "        num_samples, num_features = X.shape\n",
    "        self.weights = np.zeros(num_features)\n",
    "        self.bias = 0\n",
    "        prev_v_w,prev_v_b,gamma = 0,0,0.9\n",
    "        for i in range(self.num_epochs):\n",
    "            y_pred = self.predicted(X)\n",
    "            sp = self.sigmoid_prime_predictor(X)\n",
    "            term = ((y_pred - y) * sp).astype('float')\n",
    "            dw = (1 / num_samples) * np.dot(X.T, term)\n",
    "            db = (1 / num_samples) * sum(term)\n",
    "            \n",
    "\n",
    "            # Update the moving average of squared gradients\n",
    "            self.moving_avg_sq_w = self.decay_rate2 * self.moving_avg_sq_w + (1 - self.decay_rate2) * (dw ** 2)\n",
    "            self.moving_avg_sq_b = self.decay_rate2 * self.moving_avg_sq_b + (1 - self.decay_rate2) * (db ** 2)\n",
    "            \n",
    "            self.first_momentum_w = self.decay_rate1 * self.first_momentum_w + (1 - self.decay_rate1)*dw\n",
    "            self.first_momentum_b = self.decay_rate1 * self.first_momentum_b + (1 - self.decay_rate1)*db\n",
    "            \n",
    "            \n",
    "            # Update weights and bias using  adam\n",
    "            self.weights -= (self.learning_rate / (np.sqrt(self.moving_avg_sq_w + self.epsilon))) * self.first_momentum_w\n",
    "            self.bias -= (self.learning_rate / (np.sqrt(self.moving_avg_sq_b + self.epsilon))) * self.first_momentum_b\n",
    "\n",
    "    def test(self, X, y):\n",
    "        Y_predtest = self.predicted(X)\n",
    "        Y_values = Y_predtest\n",
    "        correct = 0\n",
    "        total = len(y)\n",
    "        for i in range(len(Y_predtest)):\n",
    "            if Y_predtest[i] > 0.5:\n",
    "                Y_predtest[i] = 1\n",
    "            else:\n",
    "                Y_predtest[i] = 0\n",
    "        for i in range(len(y)):\n",
    "            if y[i] == Y_predtest[i]:\n",
    "                correct += 1\n",
    "        return Y_predtest\n"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:19.624972Z",
     "start_time": "2023-10-29T06:58:19.623321Z"
    }
   },
   "id": "78c6a4950f132c1e"
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "outputs": [],
   "source": [
    "n_trees = 100\n",
    "trees = []\n",
    "for i in range(n_trees):\n",
    "    indices = np.random.choice(X_train.shape[0],size=75,replace=True)\n",
    "    X_bootstrap = X_train[indices]\n",
    "    y_bootstrap = y_train[indices]\n",
    "    model1 = Perceptron_RMSProp_BCE()\n",
    "    model1.fit(X_bootstrap,y_bootstrap)\n",
    "    trees.append(model1)"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:21.894861Z",
     "start_time": "2023-10-29T06:58:19.628910Z"
    }
   },
   "id": "9005182f4425fbc3"
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 1. 1. 0. 0. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 1. 1.\n",
      " 1. 1. 1. 1. 0. 1. 1. 1. 0. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1.\n",
      " 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 0. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 0. 0. 1.\n",
      " 1. 1. 0. 0. 1. 1. 0. 1. 1. 1. 1. 0. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 0. 1. 1. 1. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 0.\n",
      " 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1.\n",
      " 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 0. 1. 1. 1. 0. 0. 1. 1. 1. 1. 1. 1. 0. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 1. 0. 1. 1. 0. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 0. 1.\n",
      " 1. 1. 1. 1. 1. 1. 0. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 0.\n",
      " 0. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 1. 0.\n",
      " 0. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 0. 1. 1. 1. 0. 1.\n",
      " 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 0. 0. 1. 1. 0. 1. 1. 1. 0. 0. 1. 1.\n",
      " 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1.\n",
      " 1. 1. 0. 1. 1. 1. 0. 1. 1. 1. 0. 1. 1. 1. 1. 1. 0. 0. 0. 1. 1. 0. 1. 1.\n",
      " 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 0. 1. 1. 1. 0. 1. 1.\n",
      " 0. 1. 1. 1. 1. 1. 1. 0. 1. 0. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 0. 1. 0. 0.\n",
      " 1. 1. 1. 0. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 0.\n",
      " 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 0. 1. 1. 0. 1.\n",
      " 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 1. 1. 1. 1. 1.\n",
      " 1. 0. 1. 0. 1. 1. 0. 1. 1. 1. 1. 1. 1. 0. 1. 0. 1. 0. 1. 1. 0. 1. 0. 1.\n",
      " 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 0. 1. 1. 1. 1. 0.\n",
      " 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 0. 1. 0. 1. 1. 0. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 0. 1. 1.\n",
      " 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 0. 1. 0. 1. 1. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 1. 1. 1. 1. 1. 1. 0. 1. 1. 0.\n",
      " 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1. 0.\n",
      " 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 0. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 0. 1.\n",
      " 0. 1. 0. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1.\n",
      " 1. 1. 1. 1. 1. 0. 1. 0. 1. 0. 0. 1. 1. 1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 0.\n",
      " 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 1. 1. 1. 1.]\n"
     ]
    }
   ],
   "source": [
    "predictions = [tree.test(X_test,y_test) for tree in trees]\n",
    "y_pred = np.round(np.mean(predictions, axis=0))\n",
    "print(y_pred)\n"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:21.925486Z",
     "start_time": "2023-10-29T06:58:21.894824Z"
    }
   },
   "id": "c6ec99d9469d32ef"
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 1 1 0 0 1 1 1 1 1 0 0 1 0 1 1 1 1 1 1 1 1 0 1 1 1 1 1 0 0 1 1 0 0 1 1 0\n",
      " 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 0 0 0 1 0 1 1 1 1 0 1 1 1 1 1 1 1 1 0 1 1 1\n",
      " 0 1 0 1 1 1 1 1 0 1 0 1 0 1 0 1 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 1 1\n",
      " 1 1 1 1 1 1 1 1 0 1 0 0 0 1 1 0 1 1 1 1 1 0 1 0 1 0 1 1 1 0 1 1 1 1 1 1 1\n",
      " 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 0 1 1 0 1 1 0 1 1 1 1 1 1 0 1 1 1 1 0 1 1 1\n",
      " 1 1 1 1 1 1 1 1 1 0 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 0 0\n",
      " 0 1 0 1 1 1 1 0 0 1 0 1 1 1 0 0 1 1 1 1 1 1 1 1 0 1 1 1 1 0 1 1 1 0 1 1 1\n",
      " 1 0 1 1 1 1 0 1 1 0 0 1 1 1 1 0 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 0 1 0 1\n",
      " 1 0 0 0 0 1 1 1 1 0 1 0 1 0 1 0 1 1 1 1 1 1 1 0 0 0 1 0 1 1 1 0 1 1 1 1 0\n",
      " 0 1 0 0 1 1 1 0 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0 0 1 1 0 0 1 1 0 0 1 1\n",
      " 1 1 1 1 1 1 0 1 1 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 1 1 1 1 0 1 0 0 1 1 1 1\n",
      " 1 0 0 1 1 1 1 1 0 1 1 0 1 0 0 1 1 1 0 1 1 0 1 0 0 1 0 0 1 0 1 0 1 1 0 1 1\n",
      " 0 0 1 0 0 1 1 0 0 1 1 1 1 0 1 1 1 1 1 1 0 0 0 1 0 0 1 1 1 1 1 1 1 1 0 1 1\n",
      " 1 0 0 1 1 0 0 0 1 0 0 0 1 0 0 0 0 0 1 1 0 0 1 1 0 1 1 0 0 1 1 1 1 1 1 1 0\n",
      " 1 1 1 1 1 1 1 0 1 0 0 1 1 1 1 0 1 0 1 1 1 0 0 1 1 0 1 1 1 1 0 1 0 0 1 1 1\n",
      " 0 0 1 0 1 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 1 1 0 1 1 1 1 1 1 1 1 1\n",
      " 1 1 1 1 1 1 1 0 1 1 1 1 0 1 1 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1 1\n",
      " 0 1 1 1 1 1 0 0 1 1 1 1 0 0 1 1 1 1 1 0 0 1 0 1 1 0 1 1 1 1 1 0 1 1 0 0 1\n",
      " 1 1 1 1 1 1 1 0 0 0 1 1 0 0 1 0 1 1 0 1 0 1 0 0 1 1 1 1 1 0 1 1 1 0 1 1 1\n",
      " 0 1 1 1 0 1 1 0 1 1 1 1 1 0 1 0 1 1 1 0 1 0 0 0 0 1 1 1 1 1 0 1 0 1 0 1 1\n",
      " 0 0 1 1 1 0 1 0 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 0 1 1 1 1 1 0 1 0 1 1 1\n",
      " 1 1 1 1 1 1 1 1 1 1 0 1 1 1 0 0 1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 1 0 1 0 1 1\n",
      " 1 1 1 1 0 1 1 1 1 1 0 1 1 1 0 0 1 0 1 1 1 1 0 1 1 0 0 0 0 0 1 1 1 1 1 1 1\n",
      " 1 0 1 0 0 1 1 1 0 1 1 1 0 0 1 1 1 0 1 1 1 1 1 0 1 1 1 0 1 0 1 0 1 0 1 1 1\n",
      " 1 1 1 1 1 1 1 1 0 1 1 0 1 1 1 0 0 1 1 0 1 1 1 1 1 1 0 1 0 1 1 1 1 1 1 1 1\n",
      " 1 0 1 0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 0 0 1 0 1 1 0 1\n",
      " 1 1 0 1 1 0 1 0 0 0 0 1 0 0 1 1 1 1 1 1 1 0 1 0 0 1 0 1 0 0 1 0 1 0 1 1 1\n",
      " 0]\n"
     ]
    }
   ],
   "source": [
    "print(y_test)"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:21.926648Z",
     "start_time": "2023-10-29T06:58:21.924403Z"
    }
   },
   "id": "f876db9e1331f5f"
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[107 187]\n",
      " [ 48 658]]\n",
      "0.765\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix,accuracy_score\n",
    "cm = confusion_matrix(y_test,y_pred)\n",
    "ac = accuracy_score(y_test,y_pred)\n",
    "print(cm)\n",
    "print(ac)\n"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:21.930443Z",
     "start_time": "2023-10-29T06:58:21.927028Z"
    }
   },
   "id": "9605e80c0aa04eeb"
  },
  {
   "cell_type": "markdown",
   "source": [
    "### Pickling"
   ],
   "metadata": {
    "collapsed": false
   },
   "id": "91c289f67202b3ad"
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "outputs": [
    {
     "data": {
      "text/plain": "['RandomForestClassifier1.joblib']"
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from joblib import dump,load\n",
    "dump(trees,'RandomForestClassifier1.joblib')"
   ],
   "metadata": {
    "collapsed": false,
    "ExecuteTime": {
     "end_time": "2023-10-29T06:58:21.940117Z",
     "start_time": "2023-10-29T06:58:21.930545Z"
    }
   },
   "id": "a7c69a6a28e8dcb8"
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
