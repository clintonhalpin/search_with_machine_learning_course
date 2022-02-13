./index-data.sh \
    -p /workspace/search_with_machine_learning_course/week1/conf/bbuy_products.json \ #-p /path/to/bbuy/products/field/mappings
    -q /workspace/search_with_machine_learning_course/week1/bbuy_queries.json  \ #-q /path/to/bbuy/queries/field/mappings
    -b /workspace/search_with_machine_learning_course/week1/index-bbuy-products.logstash  \ #-b /path/to/bbuy/products/logstash/conf
    -e /workspace/search_with_machine_learning_course/week1/index-bbuy-queries.logstash  \ #-e /path/to/bbuy/queries/logstash/conf