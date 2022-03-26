#include <stdio.h>
#include <tsanalyser/tsanalyser.h>

int main(int argc, char *argv[])
{
	/* Example array*/
        double tp[2048];
        
        /* Start Keeping time before the loop 
         * Since we want to measure the time taken by the loop.
         */
        startKeepingTime();
        
        /* --------------------------------------------- */

        /* In a typical program this is where you will run the
         * Time Intensive code or the code which you may want to measure 
         * time.
         */
        
        for(int i=0; i<2048; i++) {
                tp[i] = i + 100000;
        }

        /* --------------------------------------------- */

        /* End Keeping time after the loop 
         * Since we want to measure the time taken by the loop.
         */
	getTimeTaken(DEBUG_MODE);

        /*Print total time taken and total RAM usage*/
        getTSAnlaysis(DEBUG_MODE);

	return 0;
}

