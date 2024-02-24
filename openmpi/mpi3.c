#include "mpi.h"
#include <stdio.h>

int main(int argc, char **argv) {
    int rank, size;
    
    // Initialize MPI environment
    MPI_Init(&argc, &argv);
    
    // Get the rank of the calling process in MPI_COMM_WORLD
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // Get the total number of processes in MPI_COMM_WORLD
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Print the rank and size
    printf("Hello from process %d out of %d processes.\n", rank, size);

    // Finalize MPI environment
    MPI_Finalize();

    return 0;
}

