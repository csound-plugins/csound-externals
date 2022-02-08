# hdf5read

## Abstract

Read signals and arrays from an hdf5 file. 


## Description

Opcode in hdf5 plugin. hdf5read reads N signals and arrays from a specified hdf5 file. 

Datasets with a rank larger than 1 must be read as arrays, i-rate signals must also be read as i-rate 
signals. Other than these restrictions datasets may be read as any type of array or 
signal. When reading has reached the end of a dataset it no longer outputs any new values.

---------------------------

## Syntax


```csound
xout1[, xout2, xout3, ..., xoutN] hdf5read Sfilename, Svariablename1[, Svariablename2, Svariablename3, …]
```
    
## Arguments


* **Sfilename**: the hdf5 file's name (i-time).
* **Svariablename**: the names of the datasets (in double-quotes) to be read from the hdf5 file, 
	if the dataset name is suffixed with an asterisk, e.g. "mydataset*", the entire dataset is 
	copied to the array regardless of array type. 

## Output

* **xout1**, …, **xoutN**: The specified types of variables that the hdf5 datasets are to be read as. 
	Datasets with a rank larger than 1 must be read as arrays, i-rate signals must also be read as i-rate 
	signals. Other than these restrictions datasets may be read as any type of array or signal. 
	When reading has reached the end of a dataset it no longer outputs any new values. 


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

instr hdf5read
	; Open hdf5 file and read variables
    aArray[], aVar, kVar hdf5read "example.h5", "aArray", "aVar", "kVar"

    ; Add audio signals together for stereo out 
    aLeft = (aArray[0][0] + aArray[0][1] + aVar) / 3 
    aRight = (aArray[1][0] + aArray[1][1] + aVar) / 3

	; Multiply audio signals by k-rate signal
    outs aLeft * kVar, aRight * kVar 
endin

</CsInstruments>
<CsScore>

i "hdf5read" 0 1

</CsScore>
</CsoundSynthesizer>
```

## See also

* [hdf5write](hdf5write.md)


## Credits

* Author: Edward Costello, NUIM, 2014
