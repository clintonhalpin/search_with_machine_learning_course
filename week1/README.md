# search_with_ml_week1 notes

## Getting Started
Running Flask
```
pyenv activate search_with_ml_week1
export FLASK_ENV=development
export FLASK_APP=week1
flask run --port 3000
```

## Helpful Queries

### Experimenting with indexing
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

### Get Top Queries
```
GET /bbuy_queries/_search
{
  "size": 0,
  "aggs": {
    "query": {
      "terms": {
        "field": "query.keyword",
        "size": 20,
        "min_doc_count": 1000
      }
    }
  }
}
```

### View explain for doc
```
# View the parsed Lucene query for a given OpenSearch query
POST /bbuy_products/_validate/query?explain
{
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query": "\"ipad 2\"",
            "fields": [
              "name^100",
              "shortDescription^50",
              "longDescription^10",
              "department"
            ]
          }
        }
      ]
    }
  }
}

# Explain the score for a particular document
POST /bbuy_products/_explain/2339322
{
  "query": {
    "multi_match": {
      "fields": [
        "name^100",
        "shortDescription^50",
        "longDescription^10",
        "department"
      ],
      "query": "apple ipad 2"
    }
  }
}
```