import json
from app import server, db
from app.models import (City, County, State, Country,
                        Court, Case,
                        CaseIssue, CaseConcurrenceDissent,
                        CourtAppearance,
                        )

def save_records(model, data, db):
    records = []
    for row in data:
        # mold the row
        props = dict()
        # row_keys = row.keys()
        model_keys = dir(model)
        if len(model_keys) > 0:
            for prop in model_keys:
                if prop[0] != '_':
                    props[prop] = row[prop]
            # mold the model instance and add to the list
            records.append(model(**props))
    # save to db
    if len(records) > 0:
        db.session.add_all(records)


with server.app_context():
    db.create_all()

    data = []
    with open("../data.json", "r") as f:
        data = json.load(f)

    cities = data['city']
    counties = data['county']
    states = data['state']
    countries = data['country']
    courts = data['court']
    cases = data['case']
    appearances = data['appearance']
    case__issues = data['case__issue']
    case__concurrences_dissents = data['case__concurrency_dissent']
    court__appearances = data['court__appearance']

    save_records(City, cities, db)
    save_records(County, counties, db)
    save_records(State, states, db)
    save_records(Country, countries, db)
    save_records(Court, courts, db)
    save_records(Case, cases, db)
    save_records(CaseIssue, case__issues, db)
    save_records(CaseConcurrenceDissent, case__concurrences_dissents, db)
    save_records(CourtAppearance, court__appearances, db)

    db.session.commit()


