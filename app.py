import os
from flask import Flask, jsonify, send_from_directory
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
    "Muons are part of the second generation of fundamental particles in the Standard Model.",
    "Muons were initially mistaken for mesons before their properties were fully understood.",
    "Muons are a key tool in the study of electroweak interactions.",
    "Muons are created when cosmic rays interact with particles in the Earth's atmosphere.",
    "Muons are more massive than electrons, but still much lighter than protons or neutrons.",
    "Muons lose energy primarily through ionization when traveling through matter.",
    "The discovery of muons helped in the development of quantum field theory.",
    "Muons have a rest mass of about 105.7 MeV/c².",
    "The muon neutrino, associated with the muon, is an electrically neutral lepton.",
    "Muons are used in non-destructive testing methods for inspecting large-scale structures.",
    "High-energy muons can be produced in particle accelerators.",
    "Muons can help study the properties of other fundamental particles through their interactions.",
    "The interaction of muons with magnetic fields is a subject of ongoing research.",
    "Muons contribute to the background radiation that is constantly present at the Earth's surface.",
    "The study of muon decay processes provides insights into particle lifetimes and decay mechanisms.",
    "Muon beams are used in advanced imaging techniques for medical and industrial applications.",
    "The anomalous magnetic moment of the muon is slightly different from theoretical predictions, leading to new physics investigations.",
    "Muon detectors are essential components of modern particle physics experiments.",
    "Muons are used in experiments to test the validity of the Standard Model.",
    "Muons can be captured by atomic nuclei, leading to muonic atoms with unique properties.",
    "The decay products of muons are used to trace cosmic ray interactions and their origins.",
    "Muons play a role in the search for dark matter and other unknown particles."
]


@app.route('/random_fact', methods=['GET'])
def random_fact():
    return jsonify({"fact": random.choice(facts)})

@app.route('/docs')
def docs():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'api.html')

if __name__ == '__main__':
    app.run()
