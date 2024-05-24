# models.py

from django.db import models
from django.db import connection

class City_model(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    @staticmethod
    def calculate_distance(city1_name, city2_name):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    ST_Distance(
                        ST_SetSRID(ST_MakePoint(t1.longitude, t1.latitude), 4326)::geography,
                        ST_SetSRID(ST_MakePoint(t2.longitude, t2.latitude), 4326)::geography
                    )/1000 AS distance
                FROM
                    City t1,
                    City t2
                WHERE
                    t1.cityname = %s AND
                    t2.cityname = %s;
            """, [city1_name, city2_name])

            row = cursor.fetchone()
            if row:
                return row[0]
            else:
                return None
