# week2 notes

## Exercise 1: Manual relevance judgements
https://corise.com/course/search-with-machine-learning/week/contentweek_ckxe53vz900261gcj0zgggl6v/module/module_ckzf5p7la0010149c41wwe9xo

Queries
#### lcd tv
> For this query I imagine the user is looking for a new tv in a specific size. I can really remember but I feel like an LCD TV is state of the art for the time? They could also be looking for items on sale

```
"idx:1, sku:7622664, name:HANNspree - HANNSgolf 15\" LCD TV, relevant:Relevant, in_top:False",
"idx:2, sku:7863939, name:HANNspree - HANNSbugsy 12\" LCD TV, relevant:Relevant, in_top:False",
"idx:3, sku:7863948, name:HANNspree - HANNSwood 10\" LCD TV, relevant:Relevant, in_top:False",
"idx:4, sku:7623217, name:Curtis - 2.5\" Portable LCD TV, relevant:Relevant, in_top:False",
"idx:5, sku:1068277, name:Viore - 7\" Widescreen Portable LCD TV, relevant:Relevant, in_top:False",
"idx:6, sku:1344538, name:Philips - 9\" Class / Portable LCD TV, relevant:Relevant, in_top:False",
"idx:7, sku:5518889, name:Polaroid - 20\" Flat-Panel LCD TV, relevant:Relevant, in_top:False",
"idx:8, sku:1157049, name:Axion - Axion 7\" Widescreen Portable LCD TV, relevant:Relevant, in_top:False",
"idx:9, sku:1551014, name:Philips - Refurbished 9\" Class / Portable LCD TV, relevant:Relevant, in_top:False",
"idx:10, sku:4502363, name:Panasonic - 15\" LCD TV/DVD Player Combo, relevant:Relevant, in_top:False"
```

#### ipad
> I imagine the user is looking to purchase the latest ipad. The could also be looking for accesories. Or an earlier version.
```
"idx:1, sku:5879736, name:iphome - iPad Stand for Apple® iPad®, relevant:Relevant, in_top:False",
"idx:2, sku:2678269, name:Logitech - Tablet Keyboard for Apple® iPad®, iPad 2 and iPad (3rd Generation), relevant:Relevant, in_top:False",
"idx:3, sku:3640066, name:Rocketfish™ - Bluetooth Speaker for Apple® iPad®, iPad 2 and iPad (3rd Generation), relevant:Relevant, in_top:False",
"idx:4, sku:3725243, name:iPad® - Refurbished Dock, relevant:Relevant, in_top:False",
"idx:5, sku:3725313, name:iPad® - Refurbished Dock, relevant:Relevant, in_top:False",
"idx:6, sku:1271742, name:Apple® - iPad™ Case, relevant:Relevant, in_top:False",
"idx:7, sku:9889733, name:Apple® - iPad™ Case, relevant:Relevant, in_top:False",
"idx:8, sku:4382243, name:HADAKI - Wrap for Apple® iPad® and iPad 2 - Teal, relevant:Relevant, in_top:False",
"idx:9, sku:4207114, name:Hard Candy Cases - Sleek Skin SK-IPAD-CLR For IPAD - Clear, relevant:Relevant, in_top:False",
"idx:10, sku:4207123, name:Hard Candy Cases - Sleek Skin SK-IPAD-GRN For IPAD - Green, relevant:Relevant, in_top:False"
```
#### Touchpad
> User is looking for a new mouse specifically a touch pad
```
"idx:1, sku:3438568, name:Logitech - Wireless Touchpad - Black, relevant:Relevant, in_top:False",
"idx:2, sku:4744842, name:Maytag - Touchpad Dishwasher - White, relevant:Not Relevant, in_top:False",
"idx:3, sku:4747251, name:Maytag - Touchpad Dishwasher - Black, relevant:Not Relevant, in_top:False",
"idx:4, sku:2884137, name:HP - USB Charger for HP TouchPad, relevant:Not Relevant, in_top:False",
"idx:5, sku:4744405, name:Maytag - 24\" Touchpad Built-In Dishwasher - Black, relevant:Not Relevant, in_top:False",
"idx:6, sku:4747055, name:Maytag - 24\" Touchpad Built-In Dishwasher - Bisque, relevant:Not Relevant, in_top:False",
"idx:7, sku:3459958, name:Prestige - Perrix Ergonomic USB Touchpad Keyboard - Black, relevant:Relevant, in_top:False",
"idx:8, sku:2947041, name:ZAGG - InvisibleSHIELD for HP TouchPad Tablets, relevant:Relevant, in_top:True",
"idx:9, sku:2883101, name:HP - Wireless Keyboard for HP TouchPad Tablets, relevant:Relevant, in_top:False",
"idx:10, sku:2252095, name:Adesso - SlimTouch Ergo Mini Wireless Touchpad Keyboard, relevant:Relevant, in_top:False"
```

#### beats
> User is looking for a pair of headphones by DR DRE

```
"idx:1, sku:1232474, name:Beats By Dr. Dre - Beats iBeats Earbud Headphones, relevant:Relevant, in_top:False",
"idx:2, sku:19960767, name:Angel Beats: Op My Soul - Your Beats - CD, relevant:Not Relevant, in_top:False",
"idx:3, sku:2018569, name:Jeep Beats - CASSETTE, relevant:Not Relevant, in_top:False",
"idx:4, sku:3342449, name:Explorimenting Beats - CD, relevant:Not Relevant, in_top:False",
"idx:5, sku:3682410, name:Explicit Beats - CD, relevant:Not Relevant, in_top:False",
"idx:6, sku:2799314, name:Heart Beats - CD, relevant:Not Relevant, in_top:False",
"idx:7, sku:3016088, name:Back Beats - CD, relevant:Not Relevant, in_top:False",
"idx:8, sku:10275463, name:Beats Workin' - CD, relevant:Not Relevant, in_top:False",
"idx:9, sku:10291668, name:68 Beats - CD, relevant:Not Relevant, in_top:False",
"idx:10, sku:10438733, name:Nerve Beats - CD, relevant:Not Relevant, in_top:False"
```

- Where did you agree and disagree on your relevance judgements? Why?
- What fraction of the results did you each return as relevant for each of the four queries?
- What were the ranks of the first relevant results?
- How does the search engine’s performance compare to your expectations?
- What kinds of mistakes did the search engine make? Do you know why?
- How do your results compare to the top results from the aggregated query logs?


## Self Assessment

Do you understand the steps involved in creating and deploying an LTR model? Name them and describe what each step does in your own words.

Steps for LTR
1. Create the LTR store, LTR is a plugin for opensearch/elastic search
2. Create LTR features / upload them.
3. Create a test set. In our case we are taking roughly half of the clicks one to train with another to test with. From the training set we pull metrics from LTR / Elastic Search to store in our model as well as impressions
4. Train model with XGBBoost and upload to LTR store in Elastic search
5. With the trained model we can use a "rescore" to improve our baseline query

- What is a feature and featureset?
    - A feature comes from search information about a document
    - A featureset is a group of features combined together to improve relevance with LTR

- What is the difference between precision and recall?
    - Recall: The measure of relevant documents out of the entire corpus
    - Precision: The measure of relevant results in the retrieved results

- What are some of the traps associated with using click data in your model?
    - Clicks don't describe discrete value for the user. For instance we would be better off if we had purchases or some signal that had a bit more weight to it. Clicks could be accidental or influenced by position / display etc...

- What are some of the ways we are faking our data and how would you prevent that in your application?
    - We are using fake impressions in our training, we are training on a subset of data. In future applications we could incorporate the position/order of results to have more accurate models
    - You could pay testers to rank results manually human judgements

- What is target leakage and why is it a bad thing?
    - When you train a model on information that will not be seen with new data. Leakage can cause a model to select suboptimal results and think it's performing better than it actually is.

- When can using prior history cause problems in search and LTR?
    - New products are likely to be penalized because the model hasn't ever seen them before. 

Submit your project along with your best MRR scores

```
Simple MRR is 0.301
LTR Simple MRR is 0.302
Hand tuned MRR is 0.392
LTR Hand Tuned MRR is 0.522

Simple p@10 is 0.101
LTR simple p@10 is 0.101
Hand tuned p@10 is 0.172
LTR hand tuned p@10 is 0.263
Simple better: 67	LTR_Simple Better: 144	Equal: 2416
HT better: 837	LTR_HT Better: 765	Equal: 1377
Saving Better/Equal analysis to /workspace/ltr_output/analysis
```