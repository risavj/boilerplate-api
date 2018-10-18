from flask import Blueprint
from flask_restplus import Api


blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='My Title', version='1.0', description='A description')


def register_namespaces():
	"""
	Add all your namespaces here regarding different applications

	:return:
	"""
	from BoilerplateAPI.applications.endpoints.dummy import dummy_namespace

	api.add_namespace(dummy_namespace)


register_namespaces()
