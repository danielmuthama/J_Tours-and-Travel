from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from . import main


# Views


@main.route('/')
def index():
    title = 'Welcome to Africa'
    return render_template('index.html', title=title)


@main.route('/carhire.html')
def carhire():
    return render_template('carhire.html')


@main.route('/contact.html')
def contact():
    return render_template('contact.html')


@main.route('/destinations.html')
def destinations():
    return render_template('destinations.html')


@main.route('/destinations/tsavo.html')
def tsavo():
    return render_template('destinations/tsavo.html')


@main.route('/destinations/tsavoeast.html')
def tsavoeast():
    return render_template('destinations/tsavoeast.html')


@main.route('/destinations/tanzania.html')
def tanzania():
    return render_template('destinations/tanzania.html')


@main.route('/destinations/samburu.html')
def samburu():
    return render_template('destinations/samburu.html')


@main.route('/destinations/nairobi.html')
def nairobi():
    return render_template('destinations/nairobi.html')


@main.route('/destinations/kilimanjaro.html')
def kilimanjaro():
    return render_template('destinations/kilimanjaro.html')


@main.route('/destinations/mtkenya.html')
def mtkenya():
    return render_template('destinations/mtkenya.html')


@main.route('/destinations/mara.html')
def mara():
    return render_template('destinations/mara.html')


@main.route('/destinations/nakuru.html')
def nakuru():
    return render_template('destinations/nakuru.html')


@main.route('/details/amboseli.html')
def amboseli():
    return render_template('details/amboseli.html')


@main.route('/details/tsavoamboseli.html')
def tsavoamboseli():
    return render_template('details/tsavoamboseli.html')


@main.route('/details/tsavoeast.html')
def tsaveast():
    return render_template('details/tsavoeast.html')


@main.route('/details/tsavomara.html')
def tsavomara():
    return render_template('details/tsavomara.html')


@main.route('/details/samburudetail.html')
def samburudetail():
    return render_template('details/samburudetail.html')


@main.route('/details/pejeta.html')
def pejeta():
    return render_template('details/pejeta.html')


@main.route('/details/giraffe.html')
def giraffe():
    return render_template('details/giraffe.html')


@main.route('/details/big5.html')
def big5():
    return render_template('details/big5.html')


@main.route('/details/bogoria.html')
def bogoria():
    return render_template('details/bogoria.html')


@main.route('/details/aberdares.html')
def aberdares():
    return render_template('details/aberdares.html')


@main.route('/details/nakurukenya.html')
def nakurukenya():
    return render_template('details/nakurukenya.html')


@main.route('/details/sirimon.html')
def sirimon():
    return render_template('details/sirimon.html')


@main.route('/details/hellsgate.html')
def hellsgate():
    return render_template('/details/hellsgate.html')


@main.route('/details/oldonyo.html')
def oldonyo():
    return render_template('/details/oldonyo.html')
