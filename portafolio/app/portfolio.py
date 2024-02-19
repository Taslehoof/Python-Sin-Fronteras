from flask import (
    Blueprint, render_template, request, redirect, url_for
)

import sendgrid
from sendgrid.helpers.mail import *


bp = Blueprint('portfolio', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')


@bp.route('/mail', methods=['GET', 'POST'])
def mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if request.method == 'POST':
        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html')

    return redirect(url_for('portfolio.index'))


def send_email(name, email, message):
    mi_email = 'sergio@mailinator.com'
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])

    from_email = Email(mi_email)
    #Aca estoy haciendo que identifique los datos para poder despues cambiarlos en el mail que me llegaria
    to_email = To(mi_email, substitutions={
        "-name-": name,
        "-email-": email,
        "-message-": message,
    })

    #Con estas etiquetas lo que le estoy diciendo de que lo remplaze funcionalmente para que los pueda ver en el correo
    html_content =="""
        <p>Hola Sergio, tienes un nuevo contacto desde la web:</p>
        <p>Nombre: -name-</p>
        <p>Correo: -email-</p>
        <p>Mensaje: -message-</p>
    """

    #Esto es para que me arme el mail con los datos esterotipados y lo pueda enviar
    mail = Mail(mi_email, to_email, 'Nuevo contacto desde la web', html_content=html_content)
    response = sg.client.mail.send.post(request_body=mail.get())
