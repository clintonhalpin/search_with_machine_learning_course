#!/bin/sh


DATA="/workspace/datasets/categories/output.fasttext"
TRAINING="/workspace/datasets/categories/contentCategories.train"
TEST="/workspace/datasets/categories/contentCategories.test"
MODEL_PATH="/workspace/datasets/categories/"
MODEL="/workspace/datasets/categories/model_categories.bin"

rm -rf $MODEL

head -n 10000 $DATA > $TRAINING | shuf
tail -10000 $DATA > $TEST | shuf

~/fastText-0.9.2/fasttext supervised -input $TRAINING -output model_categories -lr 1.0 -epoch 25 -wordNgrams 2
mv model_categories.bin model_categories.vec $MODEL_PATH

# ~/fastText-0.9.2/fasttext test /workspace/datasets/categories/model_categories.bin /workspace/datasets/categories/contentCategories.test
echo "\n p@1"    
~/fastText-0.9.2/fasttext test $MODEL $TEST

# ~/fastText-0.9.2/fasttext test /workspace/datasets/categories/model_categories.bin /workspace/datasets/categories/contentCategories.test 5
echo "\n p@5"    
~/fastText-0.9.2/fasttext test $MODEL $TEST 5




