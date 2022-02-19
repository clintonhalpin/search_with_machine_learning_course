#
# The main search hooks for the Search Flask application.
#
from flask import Blueprint, redirect, render_template, request, url_for
import json

from week1.opensearch import get_opensearch

bp = Blueprint("search", __name__, url_prefix="/search")


# Process the filters requested by the user and return a tuple that is appropriate for use in: the query, URLs displaying the filter and the display of the applied filters
# filters -- convert the URL GET structure into an OpenSearch filter query
# display_filters -- return an array of filters that are applied that is appropriate for display
# applied_filters -- return a String that is appropriate for inclusion in a URL as part of a query string.  This is basically the same as the input query string
def process_filters(filters_input):
    # Filters look like: &filter.name=regularPrice&regularPrice.key={{ agg.key }}&regularPrice.from={{ agg.from }}&regularPrice.to={{ agg.to }}
    filters = []
    display_filters = (
        []
    )  # Also create the text we will use to display the filters that are applied
    applied_filters = ""
    for filter in filters_input:
        type = request.args.get(filter + ".type")
        display_name = request.args.get(filter + ".displayName", filter)
        #
        # We need to capture and return what filters are already applied so they can be automatically added to any existing links we display in aggregations.jinja2
        applied_filters += "&filter.name={}&{}.type={}&{}.displayName={}".format(
            filter, filter, type, filter, display_name
        )
        # TODO: IMPLEMENT AND SET filters, display_filters and applied_filters.
        # filters get used in create_query below.  display_filters gets used by display_filters.jinja2 and applied_filters gets used by aggregations.jinja2 (and any other links that would execute a search.)
        if type == "range":
            range_from = request.args.get(filter + ".from")
            range_to = request.args.get(filter + ".to")
            applied_filters += "&{}.key={}&{}.from={}&{}.to={}".format(
                filter, key, filter, range_from, filter, range_to
            )
            range_filter = {"range": {"regularPrice": {"gte": range_from}}}
            if range_to:
                range_filter["range"]["regularPrice"]["lt"] = range_to
            filters += [range_filter]
        elif type == "terms":
            applied_filters += "&{}.key={}".format(filter, key)
            filters += [{"term": {"department.keyword": key}}]
    print("Filters: {}".format(filters))

    return filters, display_filters, applied_filters


# Our main query route.  Accepts POST (via the Search box) and GETs via the clicks on aggregations/facets
@bp.route("/query", methods=["GET", "POST"])
def query():
    opensearch = (
        get_opensearch()
    )  # Load up our OpenSearch client from the opensearch.py file.
    index_name = "bbuy_products"
    error = None
    user_query = None
    query_obj = None
    display_filters = None
    applied_filters = ""
    filters = None
    sort = "_score"
    sortDir = "desc"
    if request.method == "POST":  # a query has been submitted
        user_query = request.form["query"]
        if not user_query:
            user_query = "*"
        sort = request.form["sort"]
        if not sort:
            sort = "_score"
        sortDir = request.form["sortDir"]
        if not sortDir:
            sortDir = "desc"
        query_obj = create_query(user_query, [], sort, sortDir)
    elif (
        request.method == "GET"
    ):  # Handle the case where there is no query or just loading the page
        user_query = request.args.get("query", "*")
        filters_input = request.args.getlist("filter.name")
        sort = request.args.get("sort", sort)
        sortDir = request.args.get("sortDir", sortDir)
        if filters_input:
            (filters, display_filters, applied_filters) = process_filters(filters_input)

        query_obj = create_query(user_query, filters, sort, sortDir)
    else:
        query_obj = create_query("*", [], sort, sortDir)

    print("query")
    print(json.dumps(query_obj["query"], indent=4))
    response = opensearch.search(body=query_obj, index=index_name)
    if error is None:
        return render_template(
            "search_results.jinja2",
            query=user_query,
            search_response=response,
            display_filters=display_filters,
            applied_filters=applied_filters,
            sort=sort,
            sortDir=sortDir,
        )
    else:
        redirect(url_for("index"))


def create_query(user_query, filters, sort="_score", sortDir="desc"):
    print("Query: {} Filters: {} Sort: {}".format(user_query, filters, sort))
    price_range_agg = create_price_range_agg()
    department_agg = create_department_agg()
    query_obj = {
        "size": 10,
        "sort": {sort: sortDir},
        "query": {
            "function_score": {
                "query": {
                    "bool": {
                        "must": {
                            "multi_match": {
                                "query": user_query,
                                "fields": [
                                    "name^100",
                                    "shortDescription^50",
                                    "longDescription^10",
                                ],
                            }
                        }
                    }
                }
            }
        },
        "aggs": {
            "regularPrice": {
                "range": {"field": "regularPrice", "ranges": price_range_agg}
            },
            "department": department_agg,
        },
    }
    return query_obj


def create_department_agg():
    return {"terms": {"field": "department.keyword", "size": 5, "min_doc_count": 0}}


def create_price_range_agg():
    ranges = [
        [0, 25, "Less than $25"],
        [25, 49],
        [50, 74],
        [75, 99],
        [100, 149],
        [150, 199],
        [200, 249],
        [250, 499],
        [500, 749],
        [750, 999],
        [1000, 1249],
        [1250, 1499],
        [1500, 1999],
        [2000, 2499],
        [2500, 2999],
    ]

    rangesDeclaration = []
    for x in ranges:
        FilterRange = {}
        FilterRange["from"] = x[0]
        FilterRange["to"] = x[1]
        if 2 < len(x):
            FilterRange["key"] = x[2]
        else:
            FilterRange["key"] = "$" + str(x[0]) + "-" + str(x[1])
        rangesDeclaration.append(FilterRange)

    return rangesDeclaration
