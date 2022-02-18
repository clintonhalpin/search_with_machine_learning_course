POST bbuy_products/_search
{
  "size": 5,
  "query": {
    "function_score": {
      "query": {
        "bool": {
          "must": [
            {
              "multi_match": {
                "query": "ipad",
                "fields": ["name^100", "shortDescription^50", "longDescription^10", "department"]
              }
            }
          ],
          "filter": [
            {
              "term": {
                "department.keyword": "COMPUTERS"
              }
            }
          ]
        }
      },
      "field_value_factor": {
        "field": "price",
        "missing": 1
      }
    }
  }
}



POST bbuy_products/_search
{
  "size": 0,
  "aggs": {
    "department": {
      "terms": {
        "field": "department.keyword",
        "size": 10,
        "min_doc_count": 0
      }
    }
  }
}


# Filter by price

POST bbuy_products/_search
{
  "size": 5,
  "query": {
    "function_score": {
      "query": {
        "bool": {
          "must": [
            {
              "multi_match": {
                "query": "ipad",
                "fields": ["name^100", "shortDescription^50", "longDescription^10", "department"]
              }
            }
          ],
          "filter": [
            {
              "range": {
                "regularPrice": {
                  "gte": 0,
                  "lte": 10
                }
              }
            }
          ]
        }
      },
      "field_value_factor": {
        "field": "price",
        "missing": 1
      }
    }
  }
}


## Experiment with index settings
```
DELETE /bespokeindex

PUT /bespokeindex
{
  "settings": {
    "analysis": {
      "analyzer": {
        "smarter_hyphens": {
          "tokenizer": "smarter_hyphens_tokenizer",
          "filter": [
            "smarter_hyphens_filter",
            "lowercase"
          ]
        }
      },
      "tokenizer": {
        "smarter_hyphens_tokenizer": {
          "type": "char_group",
          "tokenize_on_chars": [
            "whitespace",
            "\n"
          ]
        }
      },
      "filter": {
        "smarter_hyphens_filter": {
          "type": "word_delimiter_graph",
          "catenate_words": true,
          "catenate_all": true
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "name": {
        "type": "text",
        "analyzer": "english",
        "fields": {
          "keyword": {
            "type": "keyword",
            "ignore_above": 2048
          },
          "hyphens": {
            "type": "text",
            "analyzer": "smarter_hyphens"
          },
          "suggest": {
            "type": "completion"
          }
        }
      }
    }
  }
}

PUT /bespokeindex/_doc/doc_a
{
  "name": "Targus - Versavu Case with Keyboard for Apple® iPad® 2 - White"
}

GET /bespokeindex/_search?q=ipad&format=yaml

POST bespokeindex/_analyze
{
  "text": ["Targus - Versavu Case with Keyboard for Apple® iPad® 2 - White"],
  "analyzer": "smarter_hyphens"
}
```