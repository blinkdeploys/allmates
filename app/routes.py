from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Case, CourtAppearance
from .forms import LoginForm
from . import login_manager


main = Blueprint('main', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200


@main.route('/')
def index():
    context = dict(title = "AllMates",
    detail="AllMates is a case data platform that helps citizens locate and stay up-to-date in cases and court communications regarding on-going cases.",
    navigation_menu=[
        dict(code="case", title="Cases"),
        dict(code="schedule", title="Schedule"),
        dict(code="locate", title="Locate"),
        dict(code="transfer", title="Tranfers"),
        dict(code="about", title="About"),
    ],
    links=[
            dict(title="Find Case", detail="Search cases by case number and citizen detail", code="find-case", id=1),
            dict(title="Court Appearance Schedule", detail="Get notified on your court schedule", code="court-schedule", id=2),
            dict(title="Locate Inmate", detail="Find an inmates current location", code="locate-inmate", id=3),
            dict(title="Visitation", detail="Check up on visitation hours", code="visitation", id=4),
            dict(title="Transfer Funds", detail="Transfer funds to an inmate", code="funds", id=5),
           ])

    return render_template('index.html', context=context)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/search_case', methods=['GET', 'POST'])
def search_case():
    if request.method == 'POST':
        case_number = request.form.get('case_number')
        case = Case.query.filter_by(case_number=case_number).first()
        if case:
            return render_template('case_detail.html', case=case)
        flash('Case not found')
    return render_template('search_case.html')
