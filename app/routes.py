import re
import datetime
import random
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Case, CourtAppearance
from .forms import LoginForm
from . import login_manager
from .constants import *



main = Blueprint('main', __name__)




# Function to calculate the day of the week
def find_day_of_week(date_string):
    date_format = "%Y-%m-%d"
    if "," in date_string:
        # Remove the ordinal suffix (e.g., "15th" -> "15")
        date_format = "%B %d, %Y"
        date_string = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_string)

    # Parse the date string into a datetime object
    date_object = datetime.datetime.strptime(date_string, date_format)
    
    # Get the name of the day of the week
    return date_object.strftime("%A")



# Example: Login function (for testing)
@main.route('/do_login')
def do_login():
    user = User(id=1)  # Replace with actual user loading logic
    login_user(user)
    return redirect(url_for('dashboard'))


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200


@main.route('/')
@login_required
def index():
    context = dict(
                   app_name = APP_NAME,
                   title = APP_NAME,
                   detail=f"{APP_NAME} is a case data platform that helps citizens locate and stay up-to-date in cases and court communications regarding on-going cases.",
                   navigation_menu=NAVIGATION_MENU,
                   links=[
                        dict(title="Find Case", detail="Search cases by case number and citizen detail", code="find-case", id=1),
                        dict(title="Court Appearance Schedule", detail="Get notified on your court schedule", code="court-schedule", id=2),
                        dict(title="Locate Inmate", detail="Find an inmates current location", code="locate-inmate", id=3),
                        dict(title="Visitation", detail="Check up on visitation hours", code="visitation", id=4),
                        dict(title="Fund Transfers", detail="Transfer funds to an inmate", code="funds", id=5),
                        dict(title="Fees & Deadlines", detail="Deadlines of fees to be made", code="fees", id=5),
                   ],
                   user=MOCK_USER_PROFILE,
                   )

    return render_template('index.html', context=context)



@main.route('/case')
@login_required
def case():

    cases = MOCK_CASE_LIST[:7]
    for this_case in cases:
        team_count = random.randint(0, 3)
        rnd = random.randint(0, 2)
        this_case["alert"] = MOCK_ALERT_STATUS[rnd]
        this_case["team"] = []
        for t in range(0, team_count):
            rnd = random.randint(0, 9)
            this_case["team"].append(MOCK_CASE_TEAM[rnd])

    context = dict(
                   app_name = APP_NAME,
        title = f"{APP_NAME} / Cases",
        page_title = "Cases",
        page_code = "case",
        cases=cases,
        navigation_menu=NAVIGATION_MENU,
        detail="Below are the associated legal cases in the system.",
        user=MOCK_USER_PROFILE,
    )
    return render_template('case.html', context=context)



@main.route('/schedule')
@login_required
def schedule():
    rnd = random.randint(0, 10)
    event = MOCK_SCHEDULE_LIST[rnd]
    event["guests"] = []
    rnd = random.randint(0, 4)
    for r in range(0, rnd):
        rnd_team = random.randint(0, 12)
        event["guests"].append(MOCK_CASE_TEAM[rnd_team])


    schedules = MOCK_SCHEDULE_LIST
    random.shuffle(schedules)
    for schedule in schedules:
        schedule["day_of_week"] = find_day_of_week(schedule["date"])[:3]
        schedule["day"] = schedule["date"].split()[1].replace(',', '')
        schedule["month"] = schedule["date"].split()[0][:3]
        rnd = random.randint(0, 3)
        schedule["status"] = MOCK_EVENT_STATUS[rnd]
    context = dict(
                   app_name = APP_NAME,
        title = f"{APP_NAME} / Court Schedule",
        page_code = "schedule",
        page_title = "Court Schedule",
        navigation_menu=NAVIGATION_MENU,
        schedule=schedules,
        event=event,
        detail="Your court appearance schedule.",
        user=MOCK_USER_PROFILE,
    )
    return render_template('schedule.html', context=context)



@main.route('/locate')
@main.route('/locate/<int:pk>')
@login_required
def locate(pk=None):
    current_court = None
    if pk:
      if pk > 0 and pk - 1 < len(COURT_LIST):
        current_court = COURT_LIST[pk - 1]
    context = dict(
                   app_name = APP_NAME,
        title = f"{APP_NAME} / Locate Inmate",
        page_code = "locate",
        page_title = "Locate Inmate",
        detail="Locate inmate by case number, bio data, station or prison. Inmate information will be added to your records.",
        courts=COURT_LIST,
        current_court = current_court,
        services=COURT_SERVICE_LIST,
        navigation_menu=NAVIGATION_MENU,
        user=MOCK_USER_PROFILE,
    )
    return render_template('locate.html', context=context)



@main.route('/team')
@login_required
def team():

    rnd = random.randint(0, 10)
    chat = MOCK_TEAM_CHAT[rnd]
    rnd = random.randint(0, 10)
    chat["team"] = MOCK_CASE_TEAM[rnd]
    # stop = len(this_team["chat"]["conversation"]) - 1
    # stop = random.randint(0, stop) + 1
    # this_team["chat"]["conversation"] = this_team["chat"]["conversation"][:stop]

    team = MOCK_CASE_TEAM[:7]
    for this_team in team:
        rnd = random.randint(0, 10)
        this_team["chat"] = MOCK_TEAM_CHAT[rnd]

    context = dict(
                   app_name = APP_NAME,
        page_code = "team",
        title = f"{APP_NAME} / Your Legal Team",
        page_title = "Your Legal Team",
        detail="Find legal help, build a team that will support you.",
        team=team,
        chat=chat,
        navigation_menu=NAVIGATION_MENU,
        user=MOCK_USER_PROFILE,
    )
    return render_template('team.html', context=context)



@main.route('/transfer')
@login_required
def transfer():
    context = dict(
                   app_name = APP_NAME,
        page_code = "transfer",
        title = f"{APP_NAME} / Funds Trander History",
        page_title = "Funds Transfer History",
        detail="A history of your fund transfers.",
        navigation_menu=NAVIGATION_MENU,
        user=MOCK_USER_PROFILE,
    )
    return render_template('transfer.html', context=context)



@main.route('/fee')
@login_required
def fee():
    context = dict(
                   app_name = APP_NAME,
        page_code = "fee",
        title = f"{APP_NAME} / Fees & Deadlines",
        page_title = "Fees & Deadlines",
        detail="A schedule of mandatory fees and penalties and timelines.",
        navigation_menu=NAVIGATION_MENU,
        user=MOCK_USER_PROFILE,
    )
    return render_template('fee.html', context=context)



@main.route('/about')
def about():
    context = dict(
                   app_name = APP_NAME,
        page_code = "about",
        title = f"About {APP_NAME}",
        page_title = f"About {APP_NAME}",
        detail = f"{APP_NAME} is a case data platform that helps citizens locate and stay up-to-date in cases and court communications regarding on-going cases.",
        navigation_menu=NAVIGATION_MENU,
        user=MOCK_USER_PROFILE,
    )
    return render_template('about.html', context=context)



@login_required
@main.route('/search_case', methods=['GET', 'POST'])
def search_case():
    if request.method == 'POST':
        case_number = request.form.get('case_number')
        case = Case.query.filter_by(case_number=case_number).first()
        if case:
            return render_template('case_detail.html', case=case)
        flash('Case not found')
    return render_template('search_case.html')



@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    context = dict(
                   app_name = APP_NAME,
                   page_title = f"{APP_NAME} Login",
                   )

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            print("User not found.")
        else:
            print(f"User found: {user.username}")

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Invalid username or password')
    return render_template('login.html', form=form, context=context)



@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/disclaimer', methods=['GET', 'POST'])
def terms_and_conditions():
    context = dict(
        app_name = APP_NAME,
        page_title = f"{APP_NAME} Legal Disclaimer",
        detail = """
"""
    )
    return render_template('disclaimer.html', context=context)

