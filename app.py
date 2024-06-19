from flask import Flask, jsonify
import random

app = Flask(__name__)

facts = [
    "The muon is an elementary particle similar to the electron.",
    "Muons have a negative electric charge and a spin of 1/2.",
    "Muons are classified as leptons in the Standard Model of particle physics.",
    "The muon is about 207 times more massive than the electron.",
    "The symbol for a muon is μ.",
    "Muons have an average lifetime of 2.2 microseconds.",
    "When muons decay, they typically produce an electron, a neutrino, and an antineutrino.",
    "Muons were first discovered by Carl D. Anderson and Seth Neddermeyer in 1936.",
    "Muons can penetrate materials more deeply than electrons.",
    "Muons are produced in large numbers in the upper atmosphere by cosmic rays.",
    "Muons are used in particle physics experiments to probe the internal structure of matter.",
    "The muon's charge is -1 elementary charge.",
    "Muons can travel through several meters of lead, unlike electrons.",
    "The existence of muons was unexpected and initially called a 'puzzle' in physics.",
    "Muons play a crucial role in muon-catalyzed fusion research.",
    "Muon g-2 is an experiment that studies the anomalous magnetic dipole moment of the muon.",
    "The decay rate of muons is an important factor in determining the weak interaction coupling constant.",
    "Muons are used in muography, a technique for imaging the interiors of large objects like pyramids and volcanoes.",
    "In particle accelerators, muons are studied to understand their properties and interactions.",
    "Muons are part of the second generation of fundamental particles in the Standard Model."
]


@app.route('/random_fact', methods=['GET'])
def random_fact():
    return jsonify({"fact": random.choice(facts)})

if __name__ == '__main__':
    app.run(debug=True)
