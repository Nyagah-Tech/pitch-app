from flask import render_template,abort,request,redirect,url_for
from . import main
from flask_login import login_required, current_user
from ..models import User,Pitch,Comment
from .forms import UpdateProfile,NewPitch,CommentForm
from .. import db,photos


@main.route('/')
def index():

    title= "home"

    pitches = Pitch.get_all_pitch()
    business = Pitch.get_pitch_category("Business")
    sport = Pitch.get_pitch_category("Sport")
    education = Pitch.get_pitch_category("Educational")
    religious = Pitch.get_pitch_category("Religious")

    return render_template("index.html",business = business,sport = sport,education = education,religious = religious ,title=title,pitches = pitches)


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

@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    pitch = Pitch.query.filter_by(id = id ).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(pitch_id = pitch.id, comment = comment, user = current_user.username)

        new_comment.save_comment()
        return redirect(url_for('.pitch',id = pitch.id))

    title = f'{pitch.pitch_title} comment'
    return render_template('comment.html',title = title, comment_form = form,pitch = pitch)

@main.route('/pitch/<id>')
@login_required
def pitch(id):
    pitch = Pitch.query.filter_by(id = id).first()

    comment = Comment.get_pitch_comment(pitch.id)
    return render_template('pitch.html',pitch = pitch, comment = comment)


@main.route('/user/<uname>/update/pic', methods = ['Post'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photo/{filename}'
        user.profile_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))