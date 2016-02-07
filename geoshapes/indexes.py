#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '30/12/2015'.
"""

from haystack.indexes import LocationField
from haystack.utils.geo import ensure_point

class CircleField(LocationField):

    field_type = 'geo_circle'

    def prepare(self, obj):

        value = super(LocationField, self).prepare(obj)
        if value is None:
            return None

        point, distance = value
        pnt = ensure_point(point)
        pnt_lng, pnt_lat = pnt.get_coords()
        value = {
            "type" : "circle",
            "coordinates" : [pnt_lng, pnt_lat],
            "radius" : distance
        }
        return value
