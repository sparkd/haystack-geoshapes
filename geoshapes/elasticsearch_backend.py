#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '07/02/2016'.

Custom elastic search backend https://wellfire.co/learn/custom-haystack-elasticsearch-backend/

"""

from haystack.backends.elasticsearch_backend import (
    ElasticsearchSearchBackend,
    ElasticsearchSearchQuery,
    ElasticsearchSearchEngine
)

from .mixins import (
    GeoShapeElasticSearchBackendMixin,
    GeoShapeElasticsearchSearchQueryMixin
)


class GeoShapeElasticsearchSearchBackend(GeoShapeElasticSearchBackendMixin, ElasticsearchSearchBackend):
    """
    Elasticsearch 2.* backend with support for querying overlapping shape
    """


class GeoShapeElasticsearchSearchQuery(GeoShapeElasticsearchSearchQueryMixin, ElasticsearchSearchQuery):
    """
    Add geoshape filter to Elasticsearch 2.* query
    """


class GeoShapeElasticSearchEngine(ElasticsearchSearchEngine):
    backend = GeoShapeElasticsearchSearchBackend
    query = GeoShapeElasticsearchSearchQuery
