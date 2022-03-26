/* file : tsanalyser.i */

/* name of module to use*/
%module tsanalyser
%{ 
	/* Every thing in this file is being copied in 
	wrapper file. We include the C header file necessary 
	to compile the interface */
	#include "../include/tsanalyser/tsanalyser.h" 
%} 

%include "stdint.i"
%include "../include/tsanalyser/tsanalyser.h"  
