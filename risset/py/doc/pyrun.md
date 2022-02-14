# pyrun

## Abstract

Run a Python statement or block of statements

## Description

Execute the specified Python statement at k-time (*pyrun* and *pylrun*) or i-time (*pyruni* and *pylruni*).

The statement is executed in the global environment for pyrun and pyruni or the local environment for pylrun and pylruni.

These opcodes perform no message passing. However, since the statement have access to the main namespace and the private namespace, it can interact with objects previously created in that environment.

The "local" version of the pyrun opcodes are useful when the code ran by different instances of an instrument should not interact.

The python opcodes target python 3.

---------------------------

## Syntax


```csound
pyrun Sstatement
pyruni Sstatement
pylrun Sstatement
pylruni Sstatement
pyrunt ktrigger, Sstatement
pylrunt ktrigger, Sstatement
```
    
## Arguments

* **Sstatement**: the python statement to run

## Output

## Execution Time

* Init
* Performance

## Examples


```csound
sr = 44100
ksmps = 10
nchnls = 1

pyinit

pyruni "import random"

instr 1
    ; This message is stored in the main namespace
    ; and is the same for every instance
    pyruni "message = 'a global random number: %f' % random.random()"
    pyrun  "print(message)"

    ; This message is stored in the private namespace
    ; and is different for different instances
    pylruni "message = 'a private random number: %f' % random.random()"
    pylrun  "print(message)"
endin

; Running this score you should get intermixed pairs of messages from the two
; instances of instrument 1.

; The first message of each pair is stored into the main namespace and so the
; second instance overwrites the message of the first instance. The result is
; that first message will be the same for both instances.

; The second message is different for the two instances, being stored in the
; private namespace.
schedule 1, 0, 0.1

```

## See also

* [pyeval](https://csound.com/docs/manual/pyeval.html)
* [pycall](https://csound.com/docs/manual/pycall.html)
* [pyinit](https://csound.com/docs/manual/pyinit.html)


## Credits

Copyright 2002 by Maurizio Umberto Puxeddu. All rights reserved. Portions
copyright 2004 and 2005 by Michael Gogins. This document has been updated
Sunday 25 July 2004 and 1 February 2005 by Michael Gogins.
