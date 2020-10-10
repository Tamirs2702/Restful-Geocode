import geojson
from micro import db
from geoalchemy2 import Geometry
from geoalchemy2.functions import GenericFunction


class ST_GeomFromGeoJSON(GenericFunction):
    """ Exposes PostGIS ST_GeomFromGeoJSON function """
    name = 'ST_GeomFromGeoJSON'
    type = Geometry


class ST_SetSRID(GenericFunction):
    """ Exposes PostGIS ST_SetSRID function """
    name = 'ST_SetSRID'
    type = Geometry


class Mapping(db.Model):
    """ Describes an individual mapping feature """
    __tablename__ = "mapping"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    geometry = db.Column(Geometry('LINESTRING', srid=4326))  # Equivalent WGS 84

    def __init__(self, name, feature):
        """ Construct mapping object from a GeoJson feature"""
        self.name = name
        geojson_str = geojson.dumps(feature['geometry'])
        self.geometry = ST_SetSRID(ST_GeomFromGeoJSON(geojson_str), 4326)

    @staticmethod
    def get_features_by_name(name):
        """ Generate Feature Collection for name"""
        lines = db.session.query(Mapping.geometry.ST_AsGeoJSON().label('geojson')).filter_by(name=name).all()

        features = []
        for line in lines:
            line_geometry = geojson.loads(line.geojson)
            feature = geojson.Feature(geometry=line_geometry)
            features.append(feature)

        return geojson.FeatureCollection(features)

    def save(self):
        """ Save object to DB"""
        db.session.add(self)
        db.session.commit()
