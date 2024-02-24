#include <stdio .h>
#include <string .h>  For strlen  #include <mpi.h> /**/ For MPI functions , etc ∗/
const int MAX_STRING = 100;
int
main ( void ) char
int int
{
greeting [MAX_STRING ];
comm_sz ; /∗ Number of processes ∗/ my_rank; /∗ My process rank ∗/
MPI_Init (NULL , NULL );
MPI_Comm_size (MPI_COMM_WORLD , &comm_sz ); MPI_Comm_rank (MPI_COMM_WORLD , &my_rank );
if (my_rank != 0) {
sprintf (greeting , "Greetings from process %d
%d!" ,
of MPI_Send ( greeting , strlen ( greeting )+1 , MPI_CHAR ,
my_rank , comm_sz );
MPI_COMM_WORLD );
}else{
printf ("Greetings from process %d of %d!\n" ,
my_rank , comm_sz );
for (int q = 1; q < comm_sz; q++) {
MPI_Recv ( greeting , MAX_STRING , MPI_CHAR , q , 0, MPI_COMM_WORLD , MPI_STATUS_IGNORE );
printf ("%s\n" ,
MPI_Finalize ();
greeting );
} }
return 0; } 