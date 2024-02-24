#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>

int main(int argc, char* argv[]) {
    int rank, size, i, count, total_count;
    double x, y, z, pi;

    // Initialize MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    srand(time(NULL) + rank); // Ensure different seeds for each process

    count = 0;
    for (i = 0; i < 1000000; i++) {
        x = (double)rand() / RAND_MAX;
        y = (double)rand() / RAND_MAX;
        z = x * x + y * y;
        if (z <= 1) count++;
    }

    // Reduce all counts to the root process
    MPI_Reduce(&count, &total_count, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    // Root process calculates and prints the estimated value of Pi
    if (rank == 0) {
        pi = (double)total_count / size / 1000000 * 4;
        printf("Estimated value of Pi = %f\n", pi);
    }

    // Finalize MPI
    MPI_Finalize();

    return 0;
}