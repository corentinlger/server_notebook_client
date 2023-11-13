from flask import Flask, request, jsonify

# Toy example to see how to change the color of agents inside an environment
class SimulationEnvironment:
    def __init__(self):
        self.agent_color = 'red' 

# Initialize the simulation environment, the number of connections and the server 
env = SimulationEnvironment()
nb_connections = 0
server = Flask(__name__)

# Display a message when you connect to the server
@server.route('/status', methods=['GET'])
def connected():
    global nb_connections

    # Increment the number of connections and return it 
    nb_connections += 1
    return f"Client number {nb_connections} connected to the simulation server"

# Change the color of agent inside the simulation environment 
@server.route('/change_agent_color', methods=['POST'])
def change_agent_color():
    global env

    # Change the color of agents 
    old_color = env.agent_color
    new_color = request.json.get('color')
    env.agent_color = new_color

    return jsonify(f"Agent color was {old_color} and is now {new_color}")

# Run the server
if __name__ == '__main__':
    server.run(port=5000)
