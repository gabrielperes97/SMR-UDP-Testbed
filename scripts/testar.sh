#!/bin/bash

SAMPLES=10000
#mn --custom topologia.py --topo sddltopo --link=tc
function testa(){ 
if [[ $SECURE ]]; then
	SEC="-sec"
fi
./topologia.py 10 $LENGTH $SAMPLES tx10-l$LENGTH$SEC.csv $SECURE
./topologia.py 50 $LENGTH $SAMPLES tx50-l$LENGTH$SEC.csv $SECURE
./topologia.py 100 $LENGTH $SAMPLES tx100-l$LENGTH$SEC.csv $SECURE
#./topologia.py 200 $LENGTH $SAMPLES tx200-l$LENGTH$SEC.csv $SECURE
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

SECURE=true
LENGTH=1024
testa

LENGTH=512
testa

LENGTH=256
testa

LENGTH=128
testa