from flask import Flask, request, jsonify

# Toy example to see how to change the color of agents inside an environment
class SimulationEnvironment:
    def __init__(self):
        self.current_time = 0
        self.agent_color = 'red' 

# Initialize the simulation environment and the server 
env = SimulationEnvironment()
server = Flask(__name__)

# Display a message when you connect to the server
@server.route('/status', methods=['GET'])
def connected():
    return "Connected to the simulation server"

# Change the color of agent inside the simulation environment 
@server.route('/change_agent_color', methods=['POST'])
def change_agent_color():
    global env

    old_color = env.agent_color
    new_color = request.json.get('color')
    env.agent_color = new_color

    return jsonify(f"Agent color was {old_color} and is now {new_color}")

# Run the server
if __name__ == '__main__':
    server.run(port=5000)
