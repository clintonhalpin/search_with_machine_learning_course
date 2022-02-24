# A simple loop that can be run to check on counts for our two indices as you are indexing.  Ctrl-c to get out.
while [ true ];
do
  echo "Queries:"
  curl -k -XGET -u admin:admin  "https://localhost:9200/_cat/count/bbuy_queries" | sed ':a;s/\B[0-9]\{3\}\>/,&/;ta';
  echo "Products:"
  curl -k -XGET -u admin:admin  "https://localhost:9200/_cat/count/bbuy_products" | sed ':a;s/\B[0-9]\{3\}\>/,&/;ta';
  sleep 5;
done