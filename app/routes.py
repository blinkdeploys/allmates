import re
import datetime
import random
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Case, CourtAppearance
from .forms import LoginForm
from . import login_manager



APP_NAME = "AllMates"

NAVIGATION_MENU = [
                    dict(code="case", title="Cases"),
                    dict(code="schedule", title="Schedule"),
                    dict(code="fee", title="Fees"),
                    dict(code="team", title="Legal Team"),
                    dict(code="locate", title="Locate"),
                    dict(code="transfer", title="Tranfers"),
                    # dict(code="about", title="About"),
                    ]

MOCK_USER_PROFILE = {
    "first_name": "Abdul",
    "first_name": "Mickelson",
    "avatar": "static/images/user.jpg",
    "username": "@amickelson",
}

MOCK_ALERT_STATUS = [
    None,
    {
        "code": "warning",
        "title": "URGENT",
    },
    {
        "code": "info",
        "title": "INFO",
    },
]
MOCK_EVENT_STATUS = [
    None,
    {
        "code": "danger",
        "title": "MISSED",
    },
    {
        "code": "grey",
        "title": "CANCELLED",
    },
    {
        "code": "warning",
        "title": "RESCHEDULED",
    },
]

MOCK_CASE_TEAM = [
    {
        "title": "1",
        "first_name": "Amanda",
        "last_name": "Chen",
        "achievement": "Attorney",
        "profile": "JD, Harvard Law School",
        "avatar": "static/images/01.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 4,
            "Advocacy": 5,
            "Negotiation and Settlement": 4,
        },
    },
    {
        "title": "2",
        "first_name": "David",
        "last_name": "Martinez",
        "achievement": "Public Defender",
        "profile": "JD, NYU School of Law",
        "avatar": "static/images/02.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 3,
            "Familiarity with Legal Processes": 5,
            "Advocacy": 5,
            "Negotiation and Settlement": 4,
        },
    },
    {
        "title": "3",
        "first_name": "Zara",
        "last_name": "Patel",
        "achievement": "Legal Aid Organization Rep",
        "profile": "JD, UCLA School of Law",
        "avatar": "static/images/03.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 4,
            "Advocacy": 5,
            "Negotiation and Settlement": 3,
        },
    },
    {
        "title": "4",
        "first_name": "James",
        "last_name": "O’Neill",
        "title": "Case Worker",
        "achievement": "BA, Social Work, University of Texas",
        "profile": "James works closely with clients involved in family court, helping them navigate the legal system during child custody disputes. With a background in social work, he ensures that the best interests of children are considered in legal proceedings. James is skilled in mediation and conflict resolution.",
        "avatar": "static/images/04.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 3,
            "Advocacy": 4,
            "Negotiation and Settlement": 5,
        },
    },
    {
        "title": "5",
        "first_name": "Rachel",
        "last_name": "Levine",
        "achievement": "Legal Researcher",
        "profile": "MA, Legal Studies, Georgetown University",
        "avatar": "static/images/05.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 3,
            "Advocacy": 3,
            "Negotiation and Settlement": 2,
        },
    },
    {
        "title": "6",
        "first_name": "Michael",
        "last_name": "Johnson",
        "achievement": "Attorney",
        "profile": "JD, Stanford Law School",
        "avatar": "static/images/06.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 5,
            "Advocacy": 4,
            "Negotiation and Settlement": 4,
        },
    },
    {
        "title": "7",
        "first_name": "Sophia",
        "last_name": "Garcia",
        "achievement": "Public Defender",
        "profile": "JD, University of Miami",
        "avatar": "static/images/07.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 5,
            "Advocacy": 5,
            "Negotiation and Settlement": 3,
        },
    },
    {
        "title": "8",
        "first_name": "Liam",
        "last_name": "Fisher",
        "achievement": "Legal Aid Organization Rep",
        "profile": "JD, Columbia Law School",
        "avatar": "static/images/08.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 5,
            "Advocacy": 4,
            "Negotiation and Settlement": 3,
        },
    },
    {
        "title": "9",
        "first_name": "Mina",
        "last_name": "Watanabe",
        "achievement": "Case Worker",
        "profile": "BA, Social Policy, University of Michigan",
        "avatar": "static/images/09.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 3,
            "Familiarity with Legal Processes": 4,
            "Advocacy": 4,
            "Negotiation and Settlement": 4,
        },
    },
    {
        "title": "10",
        "first_name": "Carlos",
        "last_name": "Hernandez",
        "achievement": "Legal Researcher",
        "profile": "MA, Jurisprudence, University of Pennsylvania",
        "avatar": "static/images/10.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 3,
            "Advocacy": 3,
            "Negotiation and Settlement": 2,
        },
    },
    {
        "title": "11",
        "first_name": "Olivia",
        "last_name": "Thompson",
        "achievement": "Attorney",
        "profile": "JD, Duke University",
        "avatar": "static/images/11.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 4,
            "Advocacy": 5,
            "Negotiation and Settlement": 4,
        },
    },
    {
        "title": "12",
        "first_name": "Elijah",
        "last_name": "Brooks",
        "achievement": "Public Defender",
        "profile": "JD, University of Chicago Law School",
        "avatar": "static/images/11.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 5,
            "Advocacy": 5,
            "Negotiation and Settlement": 3,
        },
    },
    {
        "title": "13",
        "first_name": "Nina",
        "last_name": "Gupta",
        "achievement": "Legal Aid Organization Rep",
        "profile": "JD, Yale Law School",
        "avatar": "static/images/12.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 4,
            "Advocacy": 5,
            "Negotiation and Settlement": 4,
        },
    },
    {
        "title": "14",
        "first_name": "Tyler",
        "last_name": "Mitchell",
        "achievement": "Case Worker",
        "profile": "BA, Public Administration, University of Southern California",
        "avatar": "static/images/13.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 3,
            "Familiarity with Legal Processes": 4,
            "Advocacy": 4,
            "Negotiation and Settlement": 4,
        },
    },
    {
        "title": "15",
        "first_name": "Maria",
        "last_name": "Lopez",
        "achievement": "Legal Researcher",
        "profile": "MA, Law and Policy, Stanford University",
        "avatar": "static/images/14.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 4,
            "Advocacy": 3,
            "Negotiation and Settlement": 2,

        },
    },
    {
        "title": "16",
        "first_name": "Ethan",
        "last_name": "Parker",
        "achievement": "Attorney",
        "profile": "JD, Northwestern University School of Law",
        "avatar": "static/images/15.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 4,
            "Advocacy": 4,
            "Negotiation and Settlement": 5,
        },
    },
    {
        "title": "17",
        "first_name": "Aisha",
        "last_name": "Mohammed",
        "achievement": "Public Defender",
        "profile": "JD, Georgetown University Law Center",
        "avatar": "static/images/16.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 5,
            "Advocacy": 5,
            "Negotiation and Settlement": 3,
        },
    },
    {
        "id": "18",
        "first_name": "Luca",
        "last_name": "De Rossi",
        "title": "Legal Aid Organization Rep",
        "achievement": "JD, University of California, Berkeley",
        "avatar": "static/images/17.jpg",
        "profile": "Luca provides legal aid in immigration law, specializing in asylum and deportation defense. He works with vulnerable populations seeking refuge in the United States, offering legal support and representation during the asylum process. Luca's empathetic approach and legal expertise make him a vital advocate for immigrant communities.",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 4,
            "Advocacy": 5,
            "Negotiation and Settlement": 4,
        },
    },
    {
        "title": "19",
        "first_name": "Hannah",
        "last_name": "Nguyen",
        "achievement": "Case Worker",
        "profile": "BA, Social Work, University of Washington",
        "avatar": "static/images/18.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 3,
            "Familiarity with Legal Processes": 4,
            "Advocacy": 4,
            "Negotiation and Settlement": 5,
        },
    },
    {
        "title": "20",
        "first_name": "Samuel",
        "last_name": "King",
        "achievement": "Legal Researcher",
        "profile": "MA, Jurisprudence, University of Virginia",
        "avatar": "static/images/19.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 3,
            "Advocacy": 3,
            "Negotiation and Settlement": 2,
        },
    },
    {
        "title": "21",
        "first_name": "Isabella",
        "last_name": "Rodriguez",
        "achievement": "Attorney",
        "profile": "JD, University of Texas School of Law",
        "avatar": "static/images/20.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 5,
            "Advocacy": 4,
            "Negotiation and Settlement": 5,
        },
    },
    {
        "title": "22",
        "first_name": "John",
        "last_name": "Kim",
        "achievement": "Public Defender",
        "profile": "JD, Fordham University School of Law",
        "avatar": "static/images/21.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 5,
            "Advocacy": 5,
            "Negotiation and Settlement": 3,
        },
    },
    {
        "title": "23",
        "first_name": "Priya",
        "last_name": "Sharma",
        "achievement": "Legal Aid Organization Rep",
        "profile": "JD, University of Michigan Law School",
        "avatar": "static/images/22.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 5,
            "Advocacy": 5,
            "Negotiation and Settlement": 4,
        },
    },
    {
        "title": "24",
        "first_name": "David",
        "last_name": "Williams",
        "achievement": "Case Worker",
        "profile": "BA, Criminal Justice, Arizona State University",
        "avatar": "static/images/23.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 3,
            "Familiarity with Legal Processes": 4,
            "Advocacy": 4,
            "Negotiation and Settlement": 5,
        },
    },
    {
        "title": "25",
        "first_name": "Emily",
        "last_name": "Adams",
        "achievement": "Legal Researcher",
        "profile": "MA, Legal Studies, University of Southern California",
        "avatar": "static/images/24.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 3,
            "Advocacy": 3,
            "Negotiation and Settlement": 2,
        },
    },
    {
        "title": "26",
        "first_name": "Carlos",
        "last_name": "Mendez",
        "achievement": "Attorney",
        "profile": "JD, Boston University School of Law",
        "avatar": "static/images/25.jpg",
        "top_rated": True,
        "ranking": {
            "Expert Knowledge and Experience": 5,
            
            "Familiarity with Legal Processes": 5,
            "Advocacy": 5,
            "Negotiation and Settlement": 3,
        },
    },
    {
        "title": "27",
        "first_name": "Anna",
        "last_name": "Murphy",
        "achievement": "Public Defender",
        "profile": "JD, University of North Carolina School of Law",
        "avatar": "static/images/26.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 5,
            "Advocacy": 5,
            "Negotiation and Settlement": 3,
        },
    },
    {
        "title": "28",
        "first_name": "Jamal",
        "last_name": "Wright",
        "achievement": "Legal Aid Organization Rep",
        "profile": "JD, Howard University School of Law",
        "avatar": "static/images/27.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 4,
            "Familiarity with Legal Processes": 5,
            "Advocacy": 5,
            "Negotiation and Settlement": 4,
        },
    },
    {
        "title": "29",
        "first_name": "Samantha",
        "last_name": "Lee",
        "achievement": "Case Worker",
        "profile": "BA, Sociology, University of California, Berkeley",
        "avatar": "static/images/28.jpg",
        "ranking": {
            "Expert Knowledge and Experience": 3,
            "Familiarity with Legal Processes": 4,
            "Advocacy": 4,
            "Negotiation and Settlement": 5,
        },
    },
    {
        "title": "30",
        "first_name": "Rebecca",
        "last_name": "Cohen",
        "achievement": "Legal Researcher",
        "profile": "MA, Law and Public Policy, University of Chicago",
        "avatar": "static/images/29.jpg",
        "top_rated": True,
        "ranking": {
                    "Expert Knowledge and Experience": 5,
            
                    "Familiarity with Legal Processes": 4,
                    "Advocacy": 3,
                    "Negotiation and Settlement": 2,
        },
    },
]

MOCK_CASE_LIST = [
    {"id": 1, "title": "Smith v. Johnson", "case_number": "2024-CV-1001", "summary": "Breach of contract regarding real estate transaction.", "date": "2024-01-05", "plaintiffs": "John Smith", "defendants": "Sarah Johnson", "judge": "Judge William Davis", "court": "Superior Court of California", "state": "California"},
    {"id": 2, "title": "Brown v. Taylor", "case_number": "2024-CV-1002", "summary": "Personal injury claim arising from a car accident.", "date": "2024-01-10", "plaintiffs": "Mary Brown", "defendants": "Robert Taylor", "judge": "Judge Linda Collins", "court": "Circuit Court of Illinois", "state": "Illinois"},
    {"id": 3, "title": "Johnson v. City of New York", "case_number": "2024-CV-1003", "summary": "Civil rights violation due to wrongful arrest.", "date": "2024-01-15", "plaintiffs": "James Johnson", "defendants": "City of New York", "judge": "Judge Karen Phillips", "court": "New York Supreme Court", "state": "New York"},
    {"id": 4, "title": "Martinez v. Rodriguez", "case_number": "2024-CV-1004", "summary": "Dispute over property boundary lines.", "date": "2024-01-20", "plaintiffs": "Carlos Martinez", "defendants": "Diego Rodriguez", "judge": "Judge Michael Bennett", "court": "District Court of Texas", "state": "Texas"},
    {"id": 5, "title": "Wilson v. Davis", "case_number": "2024-CV-1005", "summary": "Medical malpractice involving surgery complications.", "date": "2024-01-25", "plaintiffs": "Emily Wilson", "defendants": "Dr. Susan Davis", "judge": "Judge John Peterson", "court": "Superior Court of Georgia", "state": "Georgia"},
    {"id": 6, "title": "Garcia v. Hernandez", "case_number": "2024-CV-1006", "summary": "Defamation claim over social media posts.", "date": "2024-02-01", "plaintiffs": "Maria Garcia", "defendants": "Julio Hernandez", "judge": "Judge Elizabeth Carter", "court": "Circuit Court of Florida", "state": "Florida"},
    {"id": 7, "title": "Clark v. Martinez", "case_number": "2024-CV-1007", "summary": "Breach of partnership agreement in a business venture.", "date": "2024-02-08", "plaintiffs": "David Clark", "defendants": "Laura Martinez", "judge": "Judge Daniel Simmons", "court": "Superior Court of Arizona", "state": "Arizona"},
    {"id": 8, "title": "Harris v. Evans", "case_number": "2024-CV-1008", "summary": "Discrimination claim under employment law.", "date": "2024-02-10", "plaintiffs": "Ashley Harris", "defendants": "Global Corp (CEO Peter Evans)", "judge": "Judge Martha Johnson", "court": "Circuit Court of Virginia", "state": "Virginia"},
    {"id": 9, "title": "Lewis v. Scott", "case_number": "2024-CV-1009", "summary": "Patent infringement dispute involving tech products.", "date": "2024-02-14", "plaintiffs": "Michael Lewis", "defendants": "David Scott", "judge": "Judge Paul Robinson", "court": "District Court of Washington", "state": "Washington"},
    {"id": 10, "title": "Turner v. Hall", "case_number": "2024-CV-1010", "summary": "Divorce proceedings involving custody dispute.", "date": "2024-02-18", "plaintiffs": "Jennifer Turner", "defendants": "Andrew Hall", "judge": "Judge Susan Mitchell", "court": "Family Court of Nevada", "state": "Nevada"},
    {"id": 11, "title": "Young v. Carter", "case_number": "2024-CV-1011", "summary": "Landlord-tenant dispute over eviction and unpaid rent.", "date": "2024-02-25", "plaintiffs": "Jessica Young", "defendants": "Samuel Carter", "judge": "Judge Victor Thompson", "court": "Superior Court of Oregon", "state": "Oregon"},
    {"id": 11, "title": "Walker v. King", "case_number": "2024-CV-1012", "summary": "Trademark infringement involving a clothing brand.", "date": "2024-03-01", "plaintiffs": "Sarah Walker", "defendants": "Matthew King", "judge": "Judge Henry Adams", "court": "Circuit Court of Ohio", "state": "Ohio"},
    {"id": 12, "title": "Perez v. Adams", "case_number": "2024-CV-1013", "summary": "Contract dispute over home construction project.", "date": "2024-03-05", "plaintiffs": "Antonio Perez", "defendants": "Builder’s Inc. (CEO Mark Adams)", "judge": "Judge Lisa Harris", "court": "Superior Court of Colorado", "state": "Colorado"},
    {"id": 13, "title": "Scott v. Reed", "case_number": "2024-CV-1014", "summary": "Negligence claim from a slip-and-fall injury in a store.", "date": "2024-03-10", "plaintiffs": "Emily Scott", "defendants": "John Reed (Store Owner)", "judge": "Judge Richard Clarke", "court": "Circuit Court of Michigan", "state": "Michigan"},
    {"id": 14, "title": "Brooks v. Watson", "case_number": "2024-CV-1015", "summary": "Breach of non-disclosure agreement in a business deal.", "date": "2024-03-15", "plaintiffs": "Kevin Brooks", "defendants": "Amanda Watson", "judge": "Judge Peter Green", "court": "District Court of Oklahoma", "state": "Oklahoma"},
    {"id": 15, "title": "Sanders v. Cooper", "case_number": "2024-CV-1016", "summary": "Wrongful termination lawsuit under labor law.", "date": "2024-03-20", "plaintiffs": "Robert Sanders", "defendants": "Allied Industries (CEO Helen Cooper)", "judge": "Judge Gloria White", "court": "Circuit Court of Tennessee", "state": "Tennessee"},
    {"id": 16, "title": "Bennett v. Hill", "case_number": "2024-CV-1017", "summary": "Fraudulent investment scheme involving cryptocurrency.", "date": "2024-03-25", "plaintiffs": "Jennifer Bennett", "defendants": "Thomas Hill", "judge": "Judge Mark Taylor", "court": "District Court of New Jersey", "state": "New Jersey"},
    {"id": 17, "title": "Rivera v. Parker", "case_number": "2024-CV-1018", "summary": "Civil suit for breach of privacy involving unauthorized data sharing.", "date": "2024-04-01", "plaintiffs": "Maria Rivera", "defendants": "Richard Parker", "judge": "Judge Nancy Harris", "court": "Circuit Court of Maryland", "state": "Maryland"},
    {"id": 18, "title": "Cook v. White", "case_number": "2024-CV-1019", "summary": "Product liability lawsuit over defective kitchen appliances.", "date": "2024-04-05", "plaintiffs": "John Cook", "defendants": "HomeGoods Inc. (CEO Sarah White)", "judge": "Judge Alice Brown", "court": "Superior Court of Nevada", "state": "Nevada"},
    {"id": 19, "title": "Fisher v. Brooks", "case_number": "2024-CV-1020", "summary": "Negligence claim involving a boating accident.", "date": "2024-04-10", "plaintiffs": "Laura Fisher", "defendants": "Ryan Brooks", "judge": "Judge Charles Foster", "court": "District Court of Louisiana", "state": "Louisiana"},
    {"id": 20, "title": "Griffin v. Stewart", "case_number": "2024-CV-1021", "summary": "Custody dispute following a paternity case.", "date": "2024-04-15", "plaintiffs": "Olivia Griffin", "defendants": "Jason Stewart", "judge": "Judge Emily Roberts", "court": "Family Court of Kentucky", "state": "Kentucky"},
    {"id": 21, "title": "Morgan v. Allen", "case_number": "2024-CV-1022", "summary": "Environmental damage lawsuit due to illegal waste dumping.", "date": "2024-04-20", "plaintiffs": "Susan Morgan", "defendants": "Evergreen Inc. (CEO James Allen)", "judge": "Judge William Evan", "court": "Superior Court of California", "state": "California"},
    {"id": 22, "title": "Baker v. Russell", "case_number": "2024-CV-1023", "summary": "Wrongful death lawsuit following a workplace accident.", "date": "2024-04-25", "plaintiffs": "Henry Baker", "defendants": "Robert Russell (Factory Owner)", "judge": "Judge Patricia Martin", "court": "Circuit Court of Indiana", "state": "Indiana"},
    {"id": 22, "title": "Mitchell v. Coleman", "case_number": "2024-CV-1024", "summary": "Intellectual property dispute involving software code.", "date": "2024-04-30", "plaintiffs": "Alex Mitchell", "defendants": "James Coleman", "judge": "Judge David Lee", "court": "District Court of Minnesota", "state": "Minnesota"},
    {"id": 23, "title": "Ward v. Perry", "case_number": "2024-CV-1025", "summary": "Class action lawsuit over misleading advertising in financial services.", "date": "2024-05-05", "plaintiffs": "Jennifer Ward (on behalf of the class)", "defendants": "Perry Financial Services (CEO Henry Perry)", "judge": "Judge Robert Bell", "court": "Circuit Court of Missouri", "state": "Missouri"},
    {"id": 24, "title": "Foster v. Howard", "case_number": "2024-CV-1026", "summary": "Breach of contract involving commercial real estate development.", "date": "2024-05-10", "plaintiffs": "Thomas Foster", "defendants": "Karen Howard", "judge": "Judge Richard Young", "court": "Superior Court of Texas", "state": "Texas"},
    {"id": 25, "title": "Parker v. Griffin", "case_number": "2024-CV-1027", "summary": "Civil suit over intellectual property theft in a startup.", "date": "2024-05-15", "plaintiffs": "Lisa Parker", "defendants": "Christopher Griffin", "judge": "Judge Sharon Williams", "court": "District Court of Colorado", "state": "Colorado"},
    {"id": 26, "title": "Barnes v. Scott", "case_number": "2024-CV-1028", "summary": "Dispute over a failed merger between two companies.", "date": "2024-05-20", "plaintiffs": "Elizabeth Barnes", "defendants": "Michael Scott", "judge": "Judge Anthony Clark", "court": "Circuit Court of Pennsylvania", "state": "Pennsylvania"},
    {"id": 27, "title": "Reed v. Sanders", "case_number": "2024-CV-1029", "summary": "Employment discrimination case involving a whistleblower.", "date": "2024-05-25", "plaintiffs": "Samantha Reed", "defendants": "Global Tech (CEO Robert Sanders)", "judge": "Judge Linda Mitchell", "court": "Superior Court of Florida", "state": "Florida"},
    {"id": 29, "title": "Green v. Hall", "case_number": "2024-CV-1030", "summary": "Fraud case involving a Ponzi scheme investment scandal.", "date": "2024-05-30", "plaintiffs": "John Green", "defendants": "Benjamin Hall", "judge": "Judge Daniel Harris", "court": "District Court of New York", "state": "New York"},
]

MOCK_SCHEDULE_LIST = [
    {
        "id": 1,
        "type": "court",
        "title": "Smith v. Doe",
        "role": "Defendant",
        "case_number": "2024-CV-1021",
        "date": "September 15, 2024",
        "court": "Superior Court of California",
        "venue": "123 Main St., Los Angeles, CA",
        "reminder": "Bring case files, dress formally. Arrive 30 minutes early.",
    },
    {
        "id": 2,
        "type": "court",
        "title": "State v. Doe",
        "role": "Defendant",
        "case_number": "2024-CR-3045",
        "date": "September 20, 2024",
        "court": "Criminal Court of California",
        "venue": "450 Justice Rd., San Francisco, CA",
        "reminder": "Bring all evidence related to your defense. Meet with lawyer an hour before the hearing.",
    },
    {
        "id": 3,
        "type": "court",
        "title": "Doe v. Green Corp.",
        "role": "Plaintiff",
        "case_number": "2024-CV-1015",
        "date": "September 22, 2024",
        "court": "Superior Court of California",
        "venue": "900 Law Plaza, San Diego, CA",
        "reminder": "Prepare final argument drafts and review settlement offers.",
    },
    {
        "id": 4,
        "type": "court",
        "title": "State v. Doe",
        "role": "Defendant",
        "case_number": "2024-CR-3071",
        "date": "September 30, 2024",
        "court": "Criminal Court of California",
        "venue": "789 Law St., San Francisco, CA",
        "reminder": "Complete character reference letters. Submit additional documentation to lawyer beforehand.",
    },
    {
        "id": 5,
        "type": "court",
        "title": "Doe v. Acme Industries",
        "role": "Plaintiff",
        "case_number": "2024-CV-1109",
        "date": "October 2, 2024",
        "court": "Superior Court of California",
        "venue": "333 Court St., Oakland, CA",
        "reminder": "Review deposition transcripts. Confirm witness attendance.",
    },
    {
        "id": 6,
        "type": "court",
        "title": "State v. Doe",
        "role": "Defendant",
        "case_number": "2024-CR-3500",
        "date": "October 10, 2024",
        "court": "Criminal Court of California",
        "venue": "567 Justice Rd., Sacramento, CA",
        "reminder": "Bring all communication records. Review plea deal options with lawyer.",
    },
    {
        "id": 7,
        "type": "court",
        "title": "State v. Doe",
        "role": "Defendant",
        "case_number": "2024-CR-3689",
        "date": "October 14, 2024",
        "court": "Criminal Court of California",
        "venue": "123 Law St., San Francisco, CA",
        "reminder": "Prepare defense witness testimonies. Check transportation arrangements.",
    },
    {
        "id": 8,
        "type": "court",
        "title": "Williams v. Doe",
        "role": "Defendant",
        "case_number": "2024-CV-1050",
        "date": "October 21, 2024",
        "court": "Superior Court of California",
        "venue": "456 Main St., San Francisco, CA",
        "reminder": "Review case files. Ensure copies of legal documents are printed.",
    },
    {
        "id": 9,
        "type": "court",
        "title": "Doe v. Global Tech",
        "role": "Plaintiff",
        "case_number": "2024-CV-1085",
        "date": "October 25, 2024",
        "court": "Superior Court of California",
        "venue": "789 Court Plaza, San Diego, CA",
        "reminder": "Finalize settlement demands. Discuss court strategy with lawyer.",
    },
    {
        "id": 10,
        "type": "court",
        "title": "State v. Doe",
        "role": "Defendant",
        "case_number": "2024-CR-3701",
        "date": "November 1, 2024",
        "court": "Criminal Court of California",
        "venue": "890 Justice Ave., Oakland, CA",
        "reminder": "Print out court exhibits. Schedule post-hearing follow-up meeting with lawyer.",
    },
    {
        "id": 11,
        "type": "court",
        "title": "Doe v. West Corp.",
        "role": "Plaintiff",
        "case_number": "2024-CV-1120",
        "date": "November 3, 2024",
        "court": "Superior Court of California",
        "venue": "555 Law St., Los Angeles, CA",
        "reminder": "Confirm documents have been served to opposing counsel.",
    },
    {
        "id": 12,
        "type": "court",
        "title": "State v. Doe",
        "role": "Defendant",
        "case_number": "2024-CR-4009",
        "date": "November 5, 2024",
        "court": "Criminal Court of California",
        "venue": "456 Justice Rd., San Francisco, CA",
        "reminder": "Review testimony with defense lawyer.",
    },
    {
        "id": 13,
        "type": "court",
        "title": "Doe v. Parker Corp.",
        "role": "Plaintiff",
        "case_number": "2024-CV-1135",
        "date": "November 7, 2024",
        "court": "Superior Court of California",
        "venue": "123 Court Blvd., San Diego, CA",
        "reminder": "Review damages report. Coordinate expert witness testimony.",
    },
    {
        "id": 14,
        "type": "court",
        "title": "State v. Doe",
        "role": "Defendant",
        "case_number": "2024-CR-4125",
        "date": "November 9, 2024",
        "court": "Criminal Court of California",
        "venue": "678 Law St., Sacramento, CA",
        "reminder": "Ensure availability of key witnesses. Check court procedure timeline with legal team.",
    },
    {
        "id": 15,
        "type": "court",
        "title": "Doe v. Easton Corp.",
        "role": "Plaintiff",
        "case_number": "2024-CV-1189",
        "date": "November 12, 2024",
        "court": "Superior Court of California",
        "venue": "789 Justice Blvd., San Francisco, CA",
        "reminder": "Draft final court filings. Organize documents for presentation.",
    },
    {
        "id": 16,
        "type": "event",
        "title": "Meeting with Lawyer",
        "date": "September 10, 2024",
        "venue": "456 Justice Ave., San Francisco, CA",
        "reminder": "Bring case documents. Confirm meeting agenda. GPS: 37.7749° N, 122.4194° W.",
    },
    {
        "id": 17,
        "type": "event",
        "title": "Visit to Police Station",
        "date": "September 12, 2024",
        "venue": "789 Law Blvd., Oakland, CA",
        "reminder": "Bring ID and incident report. Complete and submit forms beforehand.",
    },
    {
        "id": 18,
        "type": "event",
        "title": "Meeting with Probation Officer",
        "date": "October 1, 2024",
        "venue": "123 Justice Rd., San Diego, CA",
        "reminder": "Bring probation report, pay outstanding fees. GPS: 32.7157° N, 117.1611° W.",
    },
    {
        "id": 19,
        "type": "event",
        "title": "Deposition Review",
        "date": "October 5, 2024",
        "venue": "678 Law St., Sacramento, CA",
        "reminder": "Review witness depositions and case strategy with legal team.",
    },
    {
        "id": 20,
        "type": "event",
        "title": "Pre-Trial Conference",
        "date": "October 18, 2024",
        "venue": "789 Justice Blvd., Los Angeles, CA",
        "reminder": "Bring updated legal briefs. Discuss strategy with lawyer.",
    },
]

MOCK_TEAM_CHAT = [
  {
    "conversation": [
      {
        "from": "client",
        "message": "Hello, is this Aisha Mohammed? I have some questions regarding my upcoming trial.",
        "timestamp": "2024-09-08 10:15:00"
      },
      {
        "from": "Aisha Mohammed",
        "message": "Good morning. Yes, this is Aisha Mohammed. How can I assist you today with your trial preparation?",
        "timestamp": "2024-09-08 10:16:30"
      },
      {
        "from": "client",
        "message": "I was wondering if we need any additional witnesses for my defense.",
        "timestamp": "2024-09-08 10:17:00"
      },
      {
        "from": "Aisha Mohammed",
        "message": "At this point, we have enough evidence and testimonies. However, if any new information arises, I will let you know. Rest assured, we're well-prepared.",
        "timestamp": "2024-09-08 10:18:45"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "Carlos Mendez",
        "message": "Good afternoon, this is Carlos Mendez, your defense attorney. I wanted to update you on the trial date next month and discuss some final preparations.",
        "timestamp": "2024-09-07 14:30:00"
      },
      {
        "from": "client",
        "message": "Thanks for reaching out, Carlos. What do I need to prepare before the trial?",
        "timestamp": "2024-09-07 14:31:20"
      },
      {
        "from": "Carlos Mendez",
        "message": "I will need you to gather all relevant documents related to the incident. Also, please be ready for a mock trial session next week so we can fine-tune your testimony.",
        "timestamp": "2024-09-07 14:32:50"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "client",
        "message": "Hi Priya, I have a question about my eviction case. Can we talk?",
        "timestamp": "2024-09-06 11:10:00"
      },
      {
        "from": "Priya Sharma",
        "message": "Good morning. Of course, how can I assist you with your housing situation today?",
        "timestamp": "2024-09-06 11:11:30"
      },
      {
        "from": "client",
        "message": "I want to know if there’s any way we can delay the eviction until I find a new place.",
        "timestamp": "2024-09-06 11:12:10"
      },
      {
        "from": "Priya Sharma",
        "message": "There are legal options available, including filing a motion to stay the eviction. I will draft a request for the court and keep you updated on the process.",
        "timestamp": "2024-09-06 11:13:50"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "Hannah Nguyen",
        "message": "Good morning, this is Hannah Nguyen, your caseworker. I just wanted to remind you about your child custody hearing scheduled for next week.",
        "timestamp": "2024-09-05 09:30:00"
      },
      {
        "from": "client",
        "message": "Hi Hannah, thank you for the reminder. Do I need to bring any specific documents to the hearing?",
        "timestamp": "2024-09-05 09:31:45"
      },
      {
        "from": "Hannah Nguyen",
        "message": "Yes, please bring any documentation related to your child’s living arrangements, as well as financial statements. I will also have our evidence prepared for submission.",
        "timestamp": "2024-09-05 09:33:10"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "client",
        "message": "Hello Luca, I need some help regarding my asylum case. Can we schedule a time to meet?",
        "timestamp": "2024-09-04 16:00:00"
      },
      {
        "from": "Luca De Rossi",
        "message": "Good afternoon. Absolutely, we can schedule a meeting. I’ll be available tomorrow afternoon at 2:00 PM. Does that work for you?",
        "timestamp": "2024-09-04 16:01:30"
      },
      {
        "from": "client",
        "message": "Yes, that time works for me. Thank you!",
        "timestamp": "2024-09-04 16:02:00"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "David Williams",
        "message": "Good evening. I’m David Williams, your caseworker. I’m reaching out to confirm our scheduled meeting with your probation officer next Wednesday.",
        "timestamp": "2024-09-03 18:45:00"
      },
      {
        "from": "client",
        "message": "Hi David, I got the notice. Do I need to bring anything specific to the meeting?",
        "timestamp": "2024-09-03 18:46:30"
      },
      {
        "from": "David Williams",
        "message": "Please bring any recent employment records and your completed probation report. This will help us in demonstrating your compliance.",
        "timestamp": "2024-09-03 18:48:00"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "client",
        "message": "Hi Isabella, do we have any updates on my personal injury case?",
        "timestamp": "2024-09-02 14:20:00"
      },
      {
        "from": "Isabella Rodriguez",
        "message": "Good afternoon. Yes, I just received confirmation from the opposing counsel that they're willing to enter settlement negotiations. I’ll schedule a meeting to discuss our strategy.",
        "timestamp": "2024-09-02 14:21:45"
      },
      {
        "from": "client",
        "message": "That sounds great. Let me know when you have the details.",
        "timestamp": "2024-09-02 14:23:00"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "John Kim",
        "message": "Good morning, this is John Kim, your public defender. I wanted to remind you of your arraignment hearing scheduled for next Tuesday. Please arrive at the courthouse by 9:00 AM.",
        "timestamp": "2024-09-01 10:00:00"
      },
      {
        "from": "client",
        "message": "Thanks for the reminder. Is there anything I should prepare before the hearing?",
        "timestamp": "2024-09-01 10:01:30"
      },
      {
        "from": "John Kim",
        "message": "Just make sure to review the charges and bring any documents we’ve discussed. We’ll go over your plea options before the hearing.",
        "timestamp": "2024-09-01 10:03:00"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "Emily Adams",
        "message": "Good afternoon, I’m Emily Adams, your legal researcher. I’ve completed the research on your corporate law case. Would you like to review the findings in detail?",
        "timestamp": "2024-08-31 15:20:00"
      },
      {
        "from": "client",
        "message": "Yes, I’d appreciate that. When can we schedule a time to go over the details?",
        "timestamp": "2024-08-31 15:21:30"
      },
      {
        "from": "Emily Adams",
        "message": "How about tomorrow morning at 10:00 AM? I’ll have all the documents ready for review.",
        "timestamp": "2024-08-31 15:22:45"
      },
      {
        "from": "client",
        "message": "That works for me. Thank you!",
        "timestamp": "2024-08-31 15:23:30"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "client",
        "message": "Hi Jamal, I need some advice about my civil rights case. Can you assist?",
        "timestamp": "2024-08-30 12:10:00"
      },
      {
        "from": "Jamal Wright",
        "message": "Good afternoon. Of course, I’d be happy to help. Let’s discuss your concerns. What specifically would you like advice on?",
        "timestamp": "2024-08-30 12:11:45"
      },
      {
        "from": "client",
        "message": "I want to know what legal steps we can take against police misconduct.",
        "timestamp": "2024-08-30 12:12:30"
      },
      {
        "from": "Jamal Wright",
        "message": "We can file a complaint with the police department, and if necessary, proceed with a civil lawsuit. Let’s gather all the facts first and plan accordingly.",
        "timestamp": "2024-08-30 12:14:15"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "Sofia Torres",
        "message": "Good evening, this is Sofia Torres, your legal representative. I wanted to check in and update you on your immigration case status.",
        "timestamp": "2024-08-29 19:00:00"
      },
      {
        "from": "client",
        "message": "Thank you for the update. Has there been any progress?",
        "timestamp": "2024-08-29 19:01:30"
      },
      {
        "from": "Sofia Torres",
        "message": "Yes, we’ve received a notice from immigration services and will need to respond by next week. I’ll draft a response and share it with you for review.",
        "timestamp": "2024-08-29 19:03:00"
      }
    ]
  },
  {
    "conversation": [
      {
        "from": "client",
        "message": "Hi Amir, I’d like to know the next steps for my divorce case.",
        "timestamp": "2024-08-28 17:00:00"
      },
      {
        "from": "Amir Khan",
        "message": "Good afternoon. We’re currently waiting for the court to schedule a mediation session. In the meantime, please review the proposed settlement agreement so we can discuss revisions.",
        "timestamp": "2024-08-28 17:01:45"
      }
    ]
  },
  {
    "conversation": [
      { "legal_rep": "Aisha Mohammed", "message": "Hello, this is Aisha Mohammed, your public defender. I'm reaching out to discuss your upcoming court appearance next week." },
      { "client": "Thank you for reaching out. What should I expect during the appearance?" },
      { "legal_rep": "Aisha Mohammed", "message": "The hearing will primarily focus on setting a timeline for your case. I'll be there to represent you, and we’ll ensure all procedural rights are maintained." },
      { "client": "Do I need to bring anything?" },
      { "legal_rep": "Aisha Mohammed", "message": "Just bring a form of identification. I’ll take care of all the legal documents. Please arrive at least 15 minutes early." },
      { "client": "Got it. Thank you!" },
      { "legal_rep": "Aisha Mohammed", "message": "You’re welcome. See you next week." }
    ]
  },
  {
    "conversation": [
      { "client": "Hi Ethan, I wanted to check on the status of my corporate acquisition case. Any updates?" },
      { "legal_rep": "Ethan Parker", "message": "Hello. Yes, we’ve made significant progress. We’ve reviewed all the contracts and are finalizing the negotiation terms. I’ll send you the updated documents later today." },
      { "client": "Great! Do I need to review anything before signing?" },
      { "legal_rep": "Ethan Parker", "message": "Please review the final clause regarding employee transitions. I’ll guide you through the rest." },
      { "client": "Okay, I’ll do that." }
    ]
  },
  {
    "conversation": [
      { "legal_rep": "Priya Sharma", "message": "Good afternoon, this is Priya Sharma from the housing legal aid team. I wanted to inform you that the landlord has responded to our eviction defense." },
      { "client": "Thanks for letting me know. What’s the next step?" },
      { "legal_rep": "Priya Sharma", "message": "The court has scheduled a hearing for next Tuesday. We’ll present our defense, which focuses on the landlord’s failure to maintain the property." },
      { "client": "Do I need to prepare anything for the hearing?" },
      { "legal_rep": "Priya Sharma", "message": "Please gather any evidence of poor maintenance, such as photos or documentation of complaints. I’ll handle the legal aspects." }
    ]
  },
  {
    "conversation": [
      { "client": "Hi, I had a question for John. Are we ready for my upcoming trial?" },
      { "legal_rep": "John Kim", "message": "Hello, yes we are fully prepared. We have all the necessary evidence and witnesses ready to go. I’ll go over the final defense strategy with you before court." },
      { "client": "That’s reassuring. Do I need to meet with you beforehand?" },
      { "legal_rep": "John Kim", "message": "Yes, let’s meet on Friday to review your testimony and ensure everything is clear. I’ll send you the details." },
      { "client": "Sounds good. See you Friday." }
    ]
  },
  {
    "conversation": [
      { "legal_rep": "Carlos Mendez", "message": "Good afternoon, Carlos Mendez here. I’m your defense attorney for the violent crime case. I wanted to go over some final points before the trial next week." },
      { "client": "Good afternoon. What should we focus on?" },
      { "legal_rep": "Carlos Mendez", "message": "We’ll focus on discrediting the prosecution’s key witness. Also, make sure your alibi is solid and consistent with the evidence." },
      { "client": "Got it. I’ll review everything again before the trial." },
      { "legal_rep": "Carlos Mendez", "message": "Perfect. I’ll be in touch with more details soon." }
    ]
  },
  {
    "conversation": [
      { "client": "Hi, is there any update on my immigration case?" },
      { "legal_rep": "Luca De Rossi", "message": "Hello, yes, we’ve just received confirmation that your hearing is scheduled for next month. I’ll send you the exact date and time via email." },
      { "client": "Thanks, do I need to prepare anything?" },
      { "legal_rep": "Luca De Rossi", "message": "Yes, please bring any documents that show your work history and community involvement. I’ll prepare the legal brief for your defense." }
    ]
  },
  {
    "conversation": [
      { "legal_rep": "Anna Murphy", "message": "Hi, this is Anna Murphy, your public defender. I wanted to check in before your juvenile hearing next Monday." },
      { "client": "Thanks for calling. What’s the focus of the hearing?" },
      { "legal_rep": "Anna Murphy", "message": "The court will be assessing the rehabilitation options we’ve proposed. I’ll argue for leniency based on your recent progress." },
      { "client": "Okay, I’ll make sure to be there on time." },
      { "legal_rep": "Anna Murphy", "message": "Great. Be prepared to speak briefly about your participation in the programs. I’ll handle the rest." }
    ]
  },
  {
    "conversation": [
      { "client": "Hi Carlos, I’m a bit nervous about my upcoming trial. Can we go over the details again?" },
      { "legal_rep": "Carlos Mendez", "message": "Of course. We’ll focus on challenging the evidence and ensuring that your rights are upheld. I’ve prepared our witnesses and will walk you through your testimony tomorrow." },
      { "client": "That would help. Thanks." }
    ]
  },
  {
    "conversation": [
      { "legal_rep": "Rebecca Cohen", "message": "Good afternoon, this is Rebecca Cohen. I’ve completed the research for your public policy case and wanted to schedule a time to discuss the findings." },
      { "client": "Thanks, Rebecca. Can we meet this Thursday?" },
      { "legal_rep": "Rebecca Cohen", "message": "Thursday works for me. I’ll send you the summary report in advance so we can go over it in detail." }
    ]
  },
  {
    "conversation": [
      { "legal_rep": "Isabella Rodriguez", "message": "Hello, Isabella Rodriguez here. I wanted to update you on your personal injury case. We’ve received the insurance company’s initial settlement offer." },
      { "client": "Thanks, is it a fair offer?" },
      { "legal_rep": "Isabella Rodriguez", "message": "It’s a bit lower than expected, but I’m confident we can negotiate for a better settlement. I recommend we counter with a revised figure." },
      { "client": "Okay, let’s do that." }
    ]
  },
  {
    "conversation": [
      { "legal_rep": "Jamal Wright", "message": "Good afternoon, this is Jamal Wright, your civil rights attorney. I wanted to inform you that we’ve filed the complaint regarding the police misconduct case." },
      { "client": "Thanks, Jamal. What’s the next step?" },
      { "legal_rep": "Jamal Wright", "message": "The court will now schedule a preliminary hearing. I’ll keep you updated on the date. In the meantime, please gather any additional evidence you might have." }
    ]
  },
  {
    "conversation": [
      { "client": "Hi John, I wanted to ask about the plea deal we discussed." },
      { "legal_rep": "John Kim", "message": "Hello, we’ve reviewed the terms and it seems like the best option at this point. It’ll reduce your sentence significantly. I’ll go over the details with you during our next meeting." },
      { "client": "Thanks, I’ll be there." }
    ]
  }
]

MOCK_UPCOMING_FEE_SHCEDULE = []

MOCK_FUND_TRANSFER_HISTORY = []


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




main = Blueprint('main', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200


@main.route('/')
def index():
    context = dict(
                   title = APP_NAME,
                   detail="AllMates is a case data platform that helps citizens locate and stay up-to-date in cases and court communications regarding on-going cases.",
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
def locate():
    context = dict(
        title = f"{APP_NAME} / Locate Inmate",
        page_code = "locate",
        page_title = "Locate Inmate",
        detail="Locate inmate by case number, bio data, station or prison. Inmate information will be added to your records.",
        navigation_menu=NAVIGATION_MENU,
        user=MOCK_USER_PROFILE,
    )
    return render_template('locate.html', context=context)


@main.route('/team')
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
def transfer():
    context = dict(
        page_code = "transfer",
        title = f"{APP_NAME} / Funds Trander History",
        page_title = "Funds Transfer History",
        detail="A history of your fund transfers.",
        navigation_menu=NAVIGATION_MENU,
        user=MOCK_USER_PROFILE,
    )
    return render_template('transfer.html', context=context)


@main.route('/fee')
def fee():
    context = dict(
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
        page_code = "about",
        title = "About AllMates",
        page_title = "About AllMates",
        detail="AllMates is a case data platform that helps citizens locate and stay up-to-date in cases and court communications regarding on-going cases.",
        navigation_menu=NAVIGATION_MENU,
        user=MOCK_USER_PROFILE,
    )
    return render_template('about.html', context=context)



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
