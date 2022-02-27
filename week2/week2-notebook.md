# Week 2 Notebook
## Baseline Results
Just working on the PR tonight. I copied my code from feature/project2... Running baseine to see metrics... MRR should be lower

Run LTR-End-To-End ⬇️


```python
# Run Training
%cd /workspace/search_with_machine_learning_course
!./ltr-end-to-end.sh -y -d
```


```python
# Original Output / Once things are hooked up
%cd /workspace/search_with_machine_learning_course
!python week2/utilities/build_ltr.py --analyze --output_dir /workspace/ltr_output
```

    /workspace/search_with_machine_learning_course
    /home/gitpod/.pyenv/versions/search_with_ml_week2/lib/python3.9/site-packages/xgboost/compat.py:36: FutureWarning: pandas.Int64Index is deprecated and will be removed from pandas in a future version. Use pandas.Index with the appropriate dtype instead.
      from pandas import MultiIndex, Int64Index
    Analyzing results from /workspace/ltr_output/xgb_test_output.csv
    Queries not seen during training: [169]
                  query
    0        Ear phones
    1        apple ipod
    2         VGA cable
    3        camera bag
    4      taylor swift
    ..              ...
    164       entourage
    165            Sony
    166  power inverter
    167             Pvr
    168              hp
    
    [169 rows x 1 columns]
    
    
    Simple MRR is 0.291
    LTR Simple MRR is 0.279
    Hand tuned MRR is 0.390
    LTR Hand Tuned MRR is 0.376
    
    Simple p@10 is 0.111
    LTR simple p@10 is 0.105
    Hand tuned p@10 is 0.166
    LTR hand tuned p@10 is 0.155
    Simple better: 834	LTR_Simple Better: 362	Equal: 759
    HT better: 1038	LTR_HT Better: 646	Equal: 599
    Saving Better/Equal analysis to /workspace/ltr_output/analysis


# Updated ltr_featureset.json
Added a bunch of features
- sku
- clicks
- rank
- num_impressions
- doc_id
- product_name
- query_id
- name_match
- manufacturer_match
- name_hyphens_match
- name_hyphens_and_match
- name_phrase_match
- shortDescription_match
- longDescription_match
- salesRankShortTerm
- salesRankMediumTerm
- salesRankLongTerm
- salePrice
- regularPrice
- click_prior
- grade


```python
# Results with features
%cd /workspace/search_with_machine_learning_course
!python week2/utilities/build_ltr.py --analyze --output_dir /workspace/ltr_output
```

    /workspace/search_with_machine_learning_course
    /home/gitpod/.pyenv/versions/search_with_ml_week2/lib/python3.9/site-packages/xgboost/compat.py:36: FutureWarning: pandas.Int64Index is deprecated and will be removed from pandas in a future version. Use pandas.Index with the appropriate dtype instead.
      from pandas import MultiIndex, Int64Index
    Analyzing results from /workspace/ltr_output/xgb_test_output.csv
    Queries not seen during training: [173]
                         query
    0                     t.i.
    1            HP power cord
    2               Htc stylus
    3                    epson
    4                panasonic
    ..                     ...
    168                tablets
    169                 tomtom
    170                   tool
    171       nintendo ds lite
    172  Nikon digital cameras
    
    [173 rows x 1 columns]
    
    
    Simple MRR is 0.281
    LTR Simple MRR is 0.285
    Hand tuned MRR is 0.401
    LTR Hand Tuned MRR is 0.519
    
    Simple p@10 is 0.098
    LTR simple p@10 is 0.100
    Hand tuned p@10 is 0.163
    LTR hand tuned p@10 is 0.267
    Simple better: 103	LTR_Simple Better: 140	Equal: 2336
    HT better: 839	LTR_HT Better: 768	Equal: 1204
    Saving Better/Equal analysis to /workspace/ltr_output/analysis


# Adding Department
- departmentId


```python
# Final Results
%cd /workspace/search_with_machine_learning_course
!python week2/utilities/build_ltr.py --analyze --output_dir /workspace/ltr_output
```

    /workspace/search_with_machine_learning_course
    /home/gitpod/.pyenv/versions/search_with_ml_week2/lib/python3.9/site-packages/xgboost/compat.py:36: FutureWarning: pandas.Int64Index is deprecated and will be removed from pandas in a future version. Use pandas.Index with the appropriate dtype instead.
      from pandas import MultiIndex, Int64Index
    Analyzing results from /workspace/ltr_output/xgb_test_output.csv
    Queries not seen during training: [172]
                query
    0            Ipod
    1       Dsl modem
    2           iPods
    3       dane cook
    4            Xbox
    ..            ...
    167  Harry potter
    168        pc3200
    169       speaker
    170         beats
    171          treo
    
    [172 rows x 1 columns]
    
    
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



```python

```
