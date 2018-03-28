#!/bin/bash

SAMPLES=100
#mn --custom topologia.py --topo sddltopo --link=tc
function testa(){ 
./topologia.py 10 $LENGTH $SAMPLES tx1-l$LENGTH.csv $SECURE
./topologia.py 50 $LENGTH $SAMPLES tx100-l$LENGTH.csv $SECURE
./topologia.py 100 $LENGTH $SAMPLES tx100-l$LENGTH.csv $SECURE
./topologia.py 200 $LENGTH $SAMPLES tx10-l$LENGTH.csv $SECURE
}

SECURE=false
LENGTH=1024
testa

LENGTH=512
testa

LENGTH=256
testa

LENGTH=128
testa

LENGTH=64
testa

SECURE=true
LENGTH=1024
testa

LENGTH=512
testa

LENGTH=256
testa

LENGTH=128
testa

LENGTH=64
testa