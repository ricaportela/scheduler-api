from flask import Flask, request, jsonify
from flask import abort


appointments_app = Flask('appointments_app')


appointments = [
    {
        "id": 1,
        "data": "01/02/2017",
        "hora_inicio": "19:00",
        "hora_fim": "19:30",
        "paciente": "Herculoide Nascimento", 
        "procedimento": "X-ray do torax"
    },
    {
        "id": 2,
        "data": "01/02/2017",
        "hora_inicio": "20:00",
        "hora_fim": "20:30",
        "paciente": "Mutley Abravanel", 
        "procedimento": "pulsao coloidal intravenal"
    }
]


@appointments_app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify({'appointments': appointments})


@appointments_app.route('/appointments/appointment/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    print(appointment_id)
    #appointment = [appointment for appointment in appointments if appointments['id'] == appointment_id]
    #if len(appointment) == 0:
    #    abort(404)
    return jsonify({'appointment': appointment[0]})

