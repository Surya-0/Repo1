#include "mpi.h"
#include <stdio.h>

int main(int argc, char **argv)
{
    // Initialize the MPI environment
    MPI_Init(&argc, &argv);
  
    // Get the number of processes ssociated with the communicator
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size); //MPI_COMM_WORLD is the default communicating worldg

    // Get the rank of the calling process
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank); //Rank initialization

    // Get the name of the processor
    char processor_name[MPI_MAX_PROCESSOR_NAME]; //Here using MPI_MAX_PROCESSOR_NAME you will get the processor name
    int name_len;
    MPI_Get_processor_name(processor_name, &name_len);

    printf("Hello world from process %s with rank %d out of %d processors\n", processor_name, world_rank, world_size);

    // Finalize: Any resources allocated for MPI can be freed
    MPI_Finalize(); //For closing the mpi setup
		// Between rank and finalize we will be writing the logic
}