#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '07/02/2016'.
"""

from haystack.query import SearchQuerySet


class GeoShapeSearchQuerySet(SearchQuerySet):
    """
    Extend SearchQuerySet with a geo_shape method to add geo shape query
    """

    def geo_shape(self, field, point, dist):
        """
        Spatial: Denotes results must have distance measurements from the
        provided point.
        """
        clone = self._clone()
        clone.query.add_geo_shape(field, point, dist)
        return clone
