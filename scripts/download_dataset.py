#!/bin/bash

set -e

echo "Downloading Olist dataset..."

kaggle datasets download -d olistbr/brazilian-ecommerce

unzip -o brazilian-ecommerce.zip -d data/raw

rm brazilian-ecommerce.zip

echo "Dataset downloaded successfully."