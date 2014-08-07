#! /usr/bin/env bash

# Script for processing LARC data

unpack() {
  unzip FRF_2012_ProfileSurvey_Data.zip
  mkdir data
  mv FRF_FRF_2012_* data
  rmdir FRF_2012_ProfileSurvey_Data
  cd data
}

rename() {
  for file in *
  do  
    strip1=${file/FRF_FRF_/}; 
    strip2=${strip1/LARC_GPS_/}; 
    echo "Original: $file"; 
    echo "New: $strip2"; 
    mv "$file" "$strip2"
  done
}

unpack
rename
