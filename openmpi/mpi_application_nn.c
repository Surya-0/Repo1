#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Define the perceptron model
typedef struct {
    float weight;
    float bias;
} Perceptron;

// Define the training data
typedef struct {
    float input;
    float expected_output;
} TrainingData;

// Activation function
float activation_function(float x) {
    // Use the step function as the activation function
    return x >= 0 ? 1 : 0;
}

// Get the parameters of a perceptron model
void get_parameters(Perceptron* perceptron, float* parameters) {
    parameters[0] = perceptron->weight;
    parameters[1] = perceptron->bias;
}

// Train the perceptron model on the given dataset
Perceptron train_perceptron(TrainingData* data, int data_size) {
    Perceptron perceptron = {0.0, 0.0}; // Initialize the perceptron with weight 0 and bias 0
    float learning_rate = 0.1;
    int i, j;

    // Train the perceptron for a number of epochs
    for (i = 0; i < 100; i++) {
        // Loop over each data point
        for (j = 0; j < data_size; j++) {
            // Calculate the perceptron's output
            float output = activation_function(perceptron.weight * data[j].input + perceptron.bias);

            // Update the perceptron's weight and bias
            float error = data[j].expected_output - output;
            perceptron.weight += learning_rate * error * data[j].input;
            perceptron.bias += learning_rate * error;
        }
    }

    // Print the trained perceptron's weight and bias
    printf("Trained perceptron: weight = %f, bias = %f\n", perceptron.weight, perceptron.bias);

    return perceptron;
}

// Fill the data array with the training data
void fill_data(TrainingData* data, int data_size) {
    srand(time(NULL)); // Seed the random number generator
    int i;

    for (i = 0; i < data_size; i++) {
        // Generate a random input between 0 and 1
        data[i].input = (float)rand() / RAND_MAX;

        // The expected output is 1 if the input is greater than or equal to 0.5, and 0 otherwise
        data[i].expected_output = data[i].input >= 0.5 ? 1 : 0;
    }
}

int main(int argc, char* argv[]) {
    int rank, size, i;
    TrainingData* data;
    int data_size = 1000000; // Assume we have 1,000,000 data points

    // Initialize MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Root process initializes the data
    if (rank == 0) {
        data = (TrainingData*)malloc(sizeof(TrainingData) * data_size);
        fill_data(data, data_size);
    }

    // Calculate the size of the subarray that each process will work on
    int subarray_size = data_size / size;
    TrainingData* subarray = (TrainingData*)malloc(sizeof(TrainingData) * subarray_size);

    // Distribute the data across processes
    MPI_Scatter(data, subarray_size, MPI_FLOAT, subarray, subarray_size, MPI_FLOAT, 0, MPI_COMM_WORLD);

    // Each process trains the perceptron model on its subarray
    Perceptron perceptron = train_perceptron(subarray, subarray_size);

    // Each process gets the parameters of its trained perceptron model
    float parameters[2];
    get_parameters(&perceptron, parameters);

    // Gather the parameters from each process
    float* all_parameters = NULL;
    if (rank == 0) {
        all_parameters = (float*)malloc(sizeof(float) * 2 * size);
    }
    MPI_Gather(parameters, 2, MPI_FLOAT, all_parameters, 2, MPI_FLOAT, 0, MPI_COMM_WORLD);

    // Root process averages the parameters
if (rank == 0) {
    float average_parameters[2] = {0.0, 0.0};
    for (i = 0; i < size; i++) {
        average_parameters[0] += all_parameters[i * 2] / size;
        average_parameters[1] += all_parameters[i * 2 + 1] / size;
    }

    // Set the averaged parameters as the parameters of the combined model
    perceptron.weight = average_parameters[0];
    perceptron.bias = average_parameters[1];

    // Calculate and print the combined accuracy
    float combined_accuracy = calculate_accuracy(&perceptron, data, data_size);
    printf("Combined accuracy: %f\n", combined_accuracy);

    // Print the combined perceptron's weight and bias
    printf("Combined perceptron: weight = %f, bias = %f\n", perceptron.weight, perceptron.bias);
}

    // Finalize MPI
    MPI_Finalize();

    return 0;
}