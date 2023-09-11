	area Program, code, readonly
	ENTRY
Main
	MOV r1, #0x25		; hexadecimal
	MOV r2, #30 		; decimal
	ADD r3, r1,r2		; Does not set the FLAGS	
	ADDS  r4,r1,r2		; SETS the flags 
	SUBS  r5,r2,r1		; set the negative flag 
	MOV r6, #0XF0000000 ;  flag is not set 
	MOVS r7, #0XF0000000	;   flags are set Negative 
	ADDS r8,r6,r7			;  sets the carry and negative flag 

stop B stop
END 

