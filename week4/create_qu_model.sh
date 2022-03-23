DATA="/workspace/datasets/labeled_query_data.txt"
TRAINING="/workspace/datasets/qu_model/data.train"
TEST="/workspace/datasets/qu_model/data.test"
MODEL_PATH="/workspace/datasets/qu_model/"
MODEL="/workspace/datasets/qu_model/model_qu.bin"

# Make Directory if it dosen't exist
mkdir -p $MODEL_PATH
rm -rf $MODEL

head -n 10000 $DATA > $TRAINING
tail -10000 $DATA > $TEST

echo "Training data"
head -n 10 $TRAINING
echo "Test data"
head -n 10 $TEST

# Train model
~/fastText-0.9.2/fasttext supervised -input $TRAINING -output model_qu -lr .5 -epoch 25 -wordNgrams 2 -minCountLabel 10 -loss hs
mv model_qu.bin model_qu.vec $MODEL_PATH

# Test Model
echo "p@1 test"
~/fastText-0.9.2/fasttext test $MODEL $TEST

echo "p@5 test"
~/fastText-0.9.2/fasttext test $MODEL $TEST 5