#!/bin/sh

for file in *.dot
do
  dot -Tpng $file -o $file.png
done
