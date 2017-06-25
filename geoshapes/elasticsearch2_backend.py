#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '07/02/2016'.

Custom elastic search backend https://wellfire.co/learn/custom-haystack-elasticsearch-backend/

"""

from haystack.backends.elasticsearch2_backend import (
    Elasticsearch2SearchBackend,
    Elasticsearch2SearchQuery,
    Elasticsearch2SearchEngine
)

from .mixins import (
    GeoShapeElasticSearchBackendMixin,
    GeoShapeElasticsearchSearchQueryMixin
)


class GeoShapeElasticsearch2SearchBackend(GeoShapeElasticSearchBackendMixin, Elasticsearch2SearchBackend):
    """
    Elasticsearch 2.* backend with support for querying overlapping shape
    """


class GeoShapeElasticsearch2SearchQuery(GeoShapeElasticsearchSearchQueryMixin, Elasticsearch2SearchQuery):
    """
    Add geoshape filter to Elasticsearch 2.* query
    """


class GeoShapeElasticsearch2SearchEngine(Elasticsearch2SearchEngine):
    backend = GeoShapeElasticsearch2SearchBackend
    query = GeoShapeElasticsearch2SearchQuery
