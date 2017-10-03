#!/bin/bash
INPUT=$1

for (( c=40; c<=61; c++ ))
do
	echo $c
	./prepare.sh $1 ${1}_${c} $c
done    
