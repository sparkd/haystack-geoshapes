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


class GeoShapeElasticSearchBackend(ElasticsearchSearchBackend):
    """
    Elastic search backend with support for querying overlapping shape
    """

    # Additional geo field mappings
    FIELD_MAPPINGS = {
        'geo_circle':    {'type': 'geo_shape'}
    }

    def build_schema(self, fields):
        content_field_name, mapping = super().build_schema(fields)
        # Over write the field mappings for any gep shape fields (currently just circle)
        for field_name, field_class in fields.items():
            if field_class.field_type in self.FIELD_MAPPINGS:
                mapping[field_class.index_fieldname] = self.FIELD_MAPPINGS[field_class.field_type]
        return (content_field_name, mapping)

    def build_search_kwargs(self, query_string, **kwargs):
        # Remove the geoshape kwarg before handing back to parent

        try:
            geo_shape = kwargs.pop('geo_shape')
        except KeyError:
            geo_shape = None

        search_kwargs = super().build_search_kwargs(query_string, **kwargs)

        if geo_shape:

            lng, lat = geo_shape['point'].get_coords()

            distance = "%(dist).6f%(unit)s" % {
                    'dist': geo_shape['distance'].km,
                    'unit': "km"
                }

            filter = {
                "geo_shape": {
                    geo_shape['field']: {
                        "shape": {
                        "type": "circle",
                        "radius": distance,
                        "coordinates": [
                            lng,
                            lat
                        ]
                        }
                    }

                }
            }

            search_kwargs['query']['filtered']["filter"] = filter

        return search_kwargs

class GeoShapeElasticsearchSearchQuery(ElasticsearchSearchQuery):

    geo_shape = None

    def build_params(self, spelling_query=None, **kwargs):

        search_kwargs = super().build_params(spelling_query, **kwargs)
        if self.geo_shape:
            search_kwargs['geo_shape'] = self.geo_shape
        return search_kwargs


    def add_geo_shape(self, field, point, distance):
        """Adds radius-based parameters to search query."""
        from haystack.utils.geo import ensure_point, ensure_distance
        self.geo_shape = {
            'field': field,
            'point': ensure_point(point),
            'distance': ensure_distance(distance),
        }


class GeoShapeElasticSearchEngine(ElasticsearchSearchEngine):
    backend = GeoShapeElasticSearchBackend
    query = GeoShapeElasticsearchSearchQuery
