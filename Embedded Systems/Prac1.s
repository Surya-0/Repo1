	area Program, code, readonly
	ENTRY
Main
	MOV r1,#7
	mov r2,#10
	ADDS r3,r1,r2	 ;  // NZCV  -  0 1 1 0 
halt B halt 
	END