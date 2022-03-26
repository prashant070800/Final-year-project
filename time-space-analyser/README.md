# Time Space Analyser Library

Library is made to analyse time and memory taken by a program.

## Example Program

```c
#include <tsanalyser/tsanalyser.h>

int main(int argc, char *argv[])
{
        setDebugOption(argc,argv);

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


```


## Installation
1. Clone this repository
```sh
git clone https://gitlab.iotiot.in/shunya/time-space-analyser.git
```
2. Build and Install library
**If you code is in C then run these commands** 
```sh
cd time-space-analyser
./scripts/build-c.sh
```
**If you code is in python then run these commands** 
```sh
cd time-space-analyser
./scripts/build-py.sh
```

## How to Compile the Example

To compile the example, run command
```
gcc -o example example.c -ltsanalyser
```

## API's 

| **API** | **Description** | **Details** |
| ------ | ------ | ------ |
| `getTSAnalysis()` | Prints, Peak RAM used in KB and Total CPU time taken in secs by the program | [Read More](#gettsanalysis) |
| `startKeepingTime()` | Starts keeping time | [Read More](#startkeepingtime) |
| `getTimeTaken()` | Gets the Total time Taken from start time | [Read More](#gettimetaken) |
| `setDebugOption()` | Adds the debug option to the program, i.e library will print only if -d option is added while running the program | [Read More](#setdebugoption) |

---

### `getTSAnalysis()`

**Description** : Prints, Peak RAM used in KB and Total CPU time taken in secs by the program

**Parameter** :
- mode(int8_t) - Flag when set to DEBUG_MODE will print the information and when set to 0 will not print the information.

**Return-type** : void

**Usage** : getTSAnalysis();

---

### `startKeepingTime()`

**Description** : Starts keeping time

**Return-type** : void

**Usage** : startKeepingTime();

---

### `getTimeTaken()`

**Description** : Gets the Total time Taken from start time

**Parameter** :
- mode(int8_t) - Flag when set to DEBUG_MODE will print the Time Taken and when set to 0 will not print the time.


**Return-type** : float

**Returns** : (float) Time taken from start till now in seconds.

**Usage** : getTimeTaken();


## Features Coming Soon

1. Ability to write to Log file
