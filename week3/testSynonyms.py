
import fasttext
import pandas as pd
import utilities.functions as fn


# Hide Model Warning: https://stackoverflow.com/questions/66353366/cant-suppress-fasttext-warning-load-model-does-not-return
fasttext.FastText.eprint = lambda x: None
model = fasttext.load_model('/workspace/datasets/fasttext/title_model.bin')

test_queries = [
    "Phone",
    "Camera",
    "Laptop",
    "Refrigerator",
    "Guitar",
    "Dryer",
    "Tv",
    "Subwoofer",
    "Beats",
    "Mouse",
    "Blender",
    "Macbook",
    #brands
    "Apple",
    "Samsung",
    "Nintendo",
    "Sony",
    "Playstation",
    "Xbox",
    "Hp",
    "Whirpool",
    "Kitchenaid"
]


all_queries = [];
all_neighbors = [];
all_neighbors_score = []
items = 10;
threshold = .93

for w in test_queries:
    all_queries.append(w);
    neighbors = model.get_nearest_neighbors(fn.extract_title_transform(w), k=items)
    nl = ", ".join(map(lambda x: x[1] + "({:.2f})".format(x[0]), neighbors));
    all_neighbors.append(nl)

    # Track which recommendations are above threshold
    above_threshhold = 0;
    for n in neighbors:
        if n[0] >= threshold:
            above_threshhold += 1
    all_neighbors_score.append(above_threshhold / items)

df = pd.DataFrame({
    'queries': all_queries,
    'score': all_neighbors_score,
    'neighbors': all_neighbors,
})

print(df.to_string())