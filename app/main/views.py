from flask import render_template,abort,redirect,url_for
from . import main
from flask_login import login_required, current_user
from ..models import User,Pitch
from .forms import UpdateProfile,NewPitch
from .. import db


@main.route('/')
def index():

    title= "home"

    pitches = Pitch.get_all_pitch()

    return render_template("index.html", title=title,pitches = pitches)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    pitch = Pitch.get_user_pitch(user.username)
    return render_template("profile/profile.html",user = user,pitch = pitch)

@main.route('/user/<uname>/update', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname = user.username))
    
    return render_template('profile/update.html',form = form)

@main.route('/pitch/new/<uname>', methods = ['GET','POST'])
@login_required
def new_pitch(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = NewPitch()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.body.data
        category = form.category.data

        new_pitch = Pitch(pitch_title = title,pitch_body = pitch,category = category,user = current_user.username )

        new_pitch.save_pitch()
        return redirect(url_for('.profile',uname = current_user.username))
    title="create new pitch"
    return render_template('new_pitch.html',title = title,pitch_form = form,user = user)
