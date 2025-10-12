#! /usr/bin/env bash     
# the previous statement indicates to interpret this program using bash

#set -x  #uncomment for execution logging - try it

TARPGM=./mytar.py

rm -rf dst # clean up from previous runs
mkdir dst # make destination directory for extraction of tar file
(cd src; $TARPGM c *) | (cd dst;  tar x) # pipe, first create tar file from src, then extract in dst 
if diff -r src dst # compare src and dst directories if identical then success else failure
then
    echo "success" >&2		# error msg to stdout
    rm -rf dst			# clean up
    exit 0			# return success
else
    echo "failure" >&2
    exit 1			# return failure
fi
     

