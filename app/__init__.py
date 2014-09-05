# coding: utf-8
#
# Copyright (c) 2014 Tirith
#
# Licensed under the Apache License, Version 2.0 (the "License")
#
# Author: Thiago Ribeiro
# Email ribeiro dot it at gmail dot com
# Created: Sep 04, 2014, 2:34 PM
import os
import re
import pexpect

from subprocess import check_call

from flask import Flask, render_template, request, url_for, flash
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators

# tpl dir
tpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tpl')

# init
app = Flask(__name__, template_folder=tpl_dir)
app.config.from_pyfile('config.py')
app.debug = True

# main form
class ChangePass(Form):
    user = TextField('Username', [validators.Required()])
    oldpass = PasswordField('Current password', [validators.Required()])
    newpass = PasswordField('New password', [validators.Required()])

# routing
@app.route('/')
def form():
    form=ChangePass()
    return render_template('form.html', form=form)

@app.route('/change-pass', methods=['POST'])
def changepass():
    form = ChangePass()
    _msg = ('Was not possible to change your password', 'warning')

    if form.validate_on_submit():
        user = str(form.user.data)
        opw = str(form.oldpass.data)
        npw = str(form.newpass.data)
    
        _cmd = '/usr/bin/smbpasswd -r ' + app.config['AD_SERVER'] + ' -U ' + user
        child = pexpect.spawn(_cmd)
        #child.logfile = open("chpass.log", "w")
        child.expect('Old SMB password:')
        child.sendline(opw)
        child.expect('New SMB password:')
        child.sendline(npw)
        child.expect('Retype new SMB password:')
        child.sendline(npw)
        child.expect(pexpect.EOF)
        _return = child.before

        # NT_STATUS_LOGON_FAILURE
        if 'NT_STATUS_LOGON_FAILURE' in _return:
            _msg = ('Invalid current password', 'warning')
        elif 'Password restriction' in _return:
            _msg = ('Password restriction, define new one with numbers, wildchars and upper letters.', 'warning')
        elif 'Password changed' in _return: 
            _msg = ('Password changed', 'success')

    flash(*_msg)
    return render_template('form.html', form=form)

# Run the app :)
if __name__ == '__main__':
    app.run(host=app.config['SERVER_HOST'], port=int(app.config['SERVER_PORT']))
