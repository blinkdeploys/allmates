from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declared_attr



# Association table to connect court appearances and attendees
court__appearance_attendees = db.Table(
    'court__appearance_attendees',
    db.Column('court__appearance_id', db.Integer, db.ForeignKey('court__appearance.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)


"""
case_concurrences_dissents = db.Table(
    'case_concurrences_dissents',
    db.Column('case_id', db.Integer, db.ForeignKey('case.id'), primary_key=True),
    db.Column('concurrence_dissent_id', db.Integer, db.ForeignKey('concurrence_dissent.id'), primary_key=True)
)
concurrences_dissents = db.relationship('ConcurrenceDissent', secondary=case_concurrences_dissents, backref=db.backref('cases', lazy='dynamic'))
cases = db.relationship('Case', secondary=case_concurrences_dissents, backref=db.backref('concurrences_dissents', lazy='dynamic'))
"""



class BasePerson(db.Model):
    __abstract__ = True
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    other_name = db.Column(db.String(255), nullable=True)


class BaseAddress(db.Model):
    __abstract__ = True
    address = db.Column(db.Text, nullable=True)
    zip_code = db.Column(db.String(100), nullable=True)

    @declared_attr
    def city_id(cls):
        return db.Column(db.Integer, db.ForeignKey('city.id'), nullable=True)

    @declared_attr
    def county_id(cls):
        return db.Column(db.Integer, db.ForeignKey('county.id'), nullable=True)

    @declared_attr
    def state_id(cls):
        return db.Column(db.Integer, db.ForeignKey('state.id'), nullable=True)

    @declared_attr
    def country_id(cls):
        return db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)

    @declared_attr
    def city(cls):
        return db.relationship('City', backref=db.backref(f'{cls.__name__.lower()}_address_city', lazy=True))

    @declared_attr
    def county(cls):
        return db.relationship('County', backref=db.backref(f'{cls.__name__.lower()}_address_county', lazy=True))

    @declared_attr
    def state(cls):
        return db.relationship('State', backref=db.backref(f'{cls.__name__.lower()}_address_state', lazy=True))

    @declared_attr
    def country(cls):
        return db.relationship('Country', backref=db.backref(f'{cls.__name__.lower()}_address_country', lazy=True))

    def __repr__(self):
        return f"<Address street={self.address} city={self.city.title} county={self.county.title} state={self.state.title} zip_code={self.zip_code}>"




class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    detail = db.Column(db.Text, nullable=True)
    county_id = db.Column(db.Integer, db.ForeignKey('county.id'), nullable=True)
    county = db.relationship('County', backref=db.backref('county', lazy=True))

    def __repr__(self):
        return f"<City title={self.title}>"


class County(db.Model):
    __tablename__ = 'county'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    detail = db.Column(db.Text, nullable=True)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=True)
    state = db.relationship('State', backref=db.backref('state', lazy=True))

    def __repr__(self):
        return f"<County title={self.title}>"


class State(db.Model):
    __tablename__ = 'state'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    detail = db.Column(db.Text, nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)
    country = db.relationship('Country', backref=db.backref('country', lazy=True))

    def __repr__(self):
        return f"<State title={self.title}>"


class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    detail = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Country title={self.title}>"


class ProfileJudge(BasePerson):
    __tablename__ = 'profile__judge'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<Judge first_name={self.first_name} last_name={self.last_name}>"


class ProfileLegalRepresentative(BasePerson):
    __tablename__ = 'profile__legal_representative'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<LegalRepresentative first_name={self.first_name} last_name={self.last_name}>"


class ProfileCitizen(BasePerson):
    __tablename__ = 'profile__citizen'
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<Citizen first_name={self.first_name} last_name={self.last_name}>"


class User(UserMixin, BaseAddress):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    other_name = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # e.g., 'lawyer', 'judge', 'defendant', 'plaintiff', etc.
    # address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    # address = db.relationship('Address', backref=db.backref('users', lazy=True))
    # Backref to indicate which court appearances the user is attending
    court_apearances = db.relationship(
        'CourtAppearance',
        secondary=court__appearance_attendees,
        backref=db.backref('attendees_in_court', lazy='dynamic')
    )
    is_superuser = db.Column(db.Boolean, default=False)


    def set_password(self, password):
        # hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        self.password_hash = generate_password_hash(password)

    
    def check_password(self, password):
        result = check_password_hash(self.password_hash, password)
        return result


    def __repr__(self):
        return f"<User first_name={self.first_name} last_name={self.last_name}>"


class Court(BaseAddress):
    __tablename__ = 'court'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.Text, nullable=True)
    # address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    # address = db.relationship('Address', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f"<Court title={self.title} city={self.city}>"


class Case(db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True)
    case_number = db.Column(db.String(50), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    rule_of_law = db.Column(db.Text, nullable=True)
    facts = db.Column(db.Text, nullable=True)
    holding = db.Column(db.Text, nullable=True)
    citation = db.Column(db.Text, nullable=True)
    court_id = db.Column(db.Integer, db.ForeignKey('court.id'), nullable=False)
    court = db.relationship('Court', backref=db.backref('court', lazy=True))

    def __repr__(self):
        return f"<Case case_number={self.case_number} title={self.title}>"


class CaseJudge(db.Model):
    __tablename__ = 'case__judge'
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    case = db.relationship('Case', backref=db.backref('cases', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('cases', lazy=True))
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<CaseJudge case={self.case.title} answer={self.user.full_name}>"


class CaseLegalRepresentative(db.Model):
    __tablename__ = 'case__legal_representative'
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    case = db.relationship('Case', backref=db.backref('case_legal_representative__cases', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('users', lazy=True))
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<CaseLegalRepresentative case={self.case.title} answer={self.user.full_name}>"


class CasePlaintiff(db.Model):
    __tablename__ = 'case__plaintiff'
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    case = db.relationship('Case', backref=db.backref('plaintiff__cases', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('case_plaintiff__user_account', lazy=True))
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<CasePlaintiff case={self.case.title} answer={self.user.full_name}>"


class CaseDefendant(db.Model):
    __tablename__ = 'case__defendant'
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    case = db.relationship('Case', backref=db.backref('case_defendant__cases', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('case_defendant__user_account', lazy=True))
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<CaseDefendant case={self.case.title} answer={self.user.full_name}>"


class CaseIssue(db.Model):
    __tablename__ = 'case__issue'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=True)
    answer = db.Column(db.String(255), nullable=False)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    case = db.relationship('Case', backref=db.backref('issue__case', lazy=True))

    def __repr__(self):
        return f"<CaseIssue question={self.question} answer={self.answer}>"


class CaseConcurrenceDissent(db.Model):
    __tablename__ = 'case_concurrence_dissent'
    id = db.Column(db.Integer, primary_key=True)
    concurrence = db.Column(db.Text, nullable=True)
    dissent = db.Column(db.Text, nullable=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    case = db.relationship('Case', backref=db.backref('case_concurrent_dissent__cases', lazy=True))

    def __repr__(self):
        return f"<ConcurrenceDissent concurrence={self.concurrence[:30]}... dissent={self.dissent[:30]}...>"


class CourtAppearance(db.Model):
    __tablename__ = 'court__appearance'
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    case = db.relationship('Case', backref=db.backref('court__appearances_by_case', lazy=True))
    court_id = db.Column(db.Integer, db.ForeignKey('court.id'), nullable=False)
    court = db.relationship('Court', backref=db.backref('court__appearances_by_court', lazy=True))
    title = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    # Relationship to attendees through the association table
    attendees = db.relationship('User', secondary=court__appearance_attendees, backref=db.backref('court_appearances_as_attendee', lazy='dynamic'))  # Updated backref

    def __repr__(self):
        return f"<CourtAppearance case={self.case} date={self.date} time={self.time}>"

