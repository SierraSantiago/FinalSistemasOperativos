#!/bin/bash


data_folder="./Request"


bucket_name="ssr-so-ueia-2024" 


for file in $data_folder/*.json; do
    if [ -f "$file" ]; then
        aws s3 cp "$file" s3://$bucket_name/$(basename "$file")
    fi
done

rm -f $data_folder/*.json
