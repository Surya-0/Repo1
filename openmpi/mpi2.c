#include "mpi.h"
#include <stdio.h>

int main(int argc, char **argv) {
    int numtasks;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numtasks);

    printf("Total number of processes: %d\n", numtasks);

    MPI_Finalize();
    return 0;
}

