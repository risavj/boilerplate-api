from flask_restplus import Resource, reqparse

from BoilerplateAPI.applications import api

dummy_namespace = api.namespace('dummy', description='Dummy')

search_arguments = reqparse.RequestParser()
search_arguments.add_argument('name', type=str, location='args', required=False)


@dummy_namespace.route("/")
class Dummy(Resource):

	@dummy_namespace.expect(search_arguments, validate=True)
	def get(self):
		"""

		:return: dict
		"""
		return {"statue": True}
