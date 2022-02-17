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