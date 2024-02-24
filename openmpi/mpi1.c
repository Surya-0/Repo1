#include "mpi.h"
#include <stdio.h>

int main(int argc, char **argv) {
    int rank, size, received_data;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) {
        int data = 42;
        MPI_Send(&data, 1, MPI_INT, 1, 123, MPI_COMM_WORLD);
    } else if (rank == 1) {
        MPI_Status status;
        MPI_Recv(&received_data, 1, MPI_INT, 0, 123, MPI_COMM_WORLD, &status);

        // Print information from MPI_Status
        printf("Process 1 received data: %d from process %d with tag %d\n",
               received_data, status.MPI_SOURCE, status.MPI_TAG);
    }

    MPI_Finalize();
    return 0;
}

