# hdf5read

## Abstract

 Write signals and arrays to an hdf5 file. 


## Description

Opcode in hdf5 plugin. `hdf5write` writes N signals and arrays to a specified hdf5 file. 

This opcode accepts i-rate, k-rate, a-rate signals or i-rate, k-rate, a-rate arrays of any dimension 
as input. These signals or arrays are written to a dataset within the hdf5 file using the same variable
 name as in Csound. For example, if the Csound variable is called 'ksignal', then the name of the hdf5 
 dataset is 'ksignal'. Any number and multiple types of datasets may be written at a time. 


---------------------------

## Syntax


```csound

hdf5write Sfilename, xout1[, xout2, xout3, ..., xoutN]

```
    
## Arguments


* **Sfilename**: the hdf5 file's name (i-time).
* **xout1**, **xout_n**: signals or arrays to be written to the hdf5 file. 

## Output

## Execution Time

* Performance

## Examples


```csound
<CsoundSynthesizer>
<CsOptions>
-odac
</CsOptions>
<CsInstruments>
nchnls = 2
0dbfs = 1
ksmps = 8
sr = 44100

instr hdf5write

    aArray[] init 2,2 ; Initialise a 2 X 2 a-rate array

    aArray[0][0] vco2 0.2, 100 ; Fill array with vco2 signals
    aArray[0][1] vco2 0.4, 200
    aArray[1][0] vco2 0.8, 300
    aArray[1][1] vco2 1, 400

    aVar vco2 0.2, 100 ; Initialise an a-rate variable with a vco2 signal

    kVar phasor 1 ; Initalise a k-rate variable with a phasor signal

    hdf5write "example.h5", aArray, aVar, kVar ; Write variables to an hdf5 file

endin

</CsInstruments>
<CsScore>

i "hdf5write" 0 1

</CsScore>
</CsoundSynthesizer>
```

## Dependencies

* **hdf5**
	* Linux: `apt install libhdf5-dev`
	* MacOS: `brew install hdf5`
	* Windows: install from https://www.hdfgroup.org/downloads/hdf5/

## See also

* [hdf5write](hdf5write.md)


## Credits

* Author: Edward Costello, NUIM, 2014
