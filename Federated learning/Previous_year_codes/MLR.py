import numpy as np

def get_mean(data):
    return np.mean(data, axis=0)

def get_sd(data):
    return np.std(data, axis=0)

def normalize_data(data, mean, sd):
    return (data - mean) / sd

def populate_data(file_path_x, file_path_y):
    x_data = np.loadtxt(file_path_x, delimiter=',')
    y_data = np.loadtxt(file_path_y, delimiter=',')
    return x_data, y_data

def get_predictions(x, weights, bias):
    return np.dot(x, weights) + bias

def get_cost(predictions, actual):
    return np.mean((predictions - actual)**2)

def update_parameters(x, predictions, actual, weights, bias, learning_rate):
    m = len(actual)
    gradient_weights = (1/m) * np.dot(x.T, (predictions - actual))
    gradient_bias = (1/m) * np.sum(predictions - actual)
    weights -= learning_rate * gradient_weights
    bias -= learning_rate * gradient_bias
    return weights, bias

def fit(x_train, y_train, x_test, y_test, epochs, learning_rate):
    mean_train = get_mean(x_train)
    sd_train = get_sd(x_train)

    x_train = normalize_data(x_train, mean_train, sd_train)
    x_test = normalize_data(x_test, mean_train, sd_train)

    weights = np.zeros(x_train.shape[1])
    bias = 0

    for epoch in range(epochs):
        predictions_train = get_predictions(x_train, weights, bias)
        cost_train = get_cost(predictions_train, y_train)

        weights, bias = update_parameters(x_train, predictions_train, y_train, weights, bias, learning_rate)

        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Training Cost: {cost_train}')

    predictions_test = get_predictions(x_test, weights, bias)
    cost_test = get_cost(predictions_test, y_test)
    print(f'Final Testing Cost: {cost_test}')

if __name__ == "__main__":
    file_path_x_train = "path/to/x_train.csv"
    file_path_y_train = "path/to/y_train.csv"
    file_path_x_test = "path/to/x_test.csv"
    file_path_y_test = "path/to/y_test.csv"

    x_train, y_train = populate_data(file_path_x_train, file_path_y_train)
    x_test, y_test = populate_data(file_path_x_test, file_path_y_test)

    epochs = 1000
    learning_rate = 0.01

    fit(x_train, y_train, x_test, y_test, epochs, learning_rate)
