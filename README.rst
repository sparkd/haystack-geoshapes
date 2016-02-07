curl -XGET 'http://172.28.128.3:9200/sciencelive/_search' -d '{
    "query" : {
        "geo_shape": {
          "location_radius": {
            "shape": {
              "type": "circle",
              "radius": "200mi",
              "coordinates": [
                51.53717,
                -0.09652
              ]
            }
          }
        }
    }
}'
