from doctors import app, db
from flask import  request, jsonify, json
from doctors.models import Doctor, Appointment
from flask_login import login_user, logout_user, current_user


@app.route('/login', methods = ['GET', 'POST'])
def loginPage():
    r = request.json
    app.logger.info(r)

    attempted_user = Doctor.query.filter_by(email_address=r['email_address']).first()
    if attempted_user and (attempted_user.password == r['password']):
        app.logger.info(attempted_user.appointments)

        apts = Appointment.query.filter_by(appointed_doctor=attempted_user.id)
        list_of_apts = []
        for apt in apts:
            list_of_apts.append(apt.as_apt_dict())


        response = attempted_user.as_dict() 
        response["appointments"] = list_of_apts
        login_user(attempted_user)
        return jsonify(response)
    else:
        return 'Login information incorrect'

@app.route('/logout')
def logoutPage():
    logout_user()