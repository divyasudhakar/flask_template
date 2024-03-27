from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import logging
from node import Node
import dataclasses

app = Flask('NodeService')
api = Api(app)

# Configure logging output to log to a file.
handler = logging.FileHandler('app.log')
app.logger.addHandler(handler)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Keep track of the node objects the user is creating.
node_map = {}


@app.errorhandler(400)
def client_error(error):
  app.logger.error('An exception occurred during a request: %s', error)
  return f'Bad Input: {error}', 400


class NodeService(Resource):

  def get(self):
    """Query for a single node object or for all nodes."""
    id = request.args.get('id', None)
    if id and int(id) in node_map:
      return jsonify(node_map[int(id)])
    json_dict = {}
    for id, node_obj in node_map.items():
      json_obj = dataclasses.asdict(node_obj)
      json_dict[id] = json_obj
    return jsonify(json_dict)

  def post(self):
    """Create a new node object and store it in the map."""
    data = dict(request.get_json())
    title = data.get('title', None)
    content = data.get('content', None)
    # Nothing fancy. Simple counter to generate unique keys for the node map.
    # Use UUIDs if you're serious about unique ids.
    new_id = len(node_map) + 1
    new_node = Node(new_id, title, content)
    node_map[new_id] = new_node
    return 'Added Node'

  def delete(self, id):
    """Delete a node object from the map given the id"""
    if id in node_map:
      del node_map[id]
      return 'Deleted Node'
    else:
      return 'Node not found'


api.add_resource(NodeService, '/api/node', endpoint='api/node')
api.add_resource(NodeService, '/api/node/<int:id>', endpoint='api/node/id')

if __name__ == '__main__':
  # This runs on 0.0.0.0 since I typically run this on Replit.
  # Replace this with 127.0.0.1 if you're running locally.
  app.run('0.0.0.0', 3001, debug=True)

