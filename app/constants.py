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

COURT_SERVICE_LIST = [
  dict(
    id=1,
    title="Access Court Records",
    detail="Information on accessing court records, online services for case search and purchase of select document downloads from the Register of Actions",
  ),
  dict(
    id=2,
    title="Appearing for Hearings",
    detail="Instructions on how to appear for hearings, including links to virtual hearings",
  ),
  dict(
    id=3,
    title="Jury Duty",
    detail="Check jury duty status, find information on reporting instructions, online services for postponements, payment status and work certification",
  ),
  dict(
    id=4,
    title="Traffic",
    detail="Traffic or Minor Offense ticket/citation information, online services to pay a fine, request traffic school, request an extension, or schedule an appointment",
  ),
  dict(
    id=5,
    title="Self Help",
    detail="Resources to learn about court procedures, forms and assistance that may be available through a self-help service provider",
  ),
  dict(
    id=6,
    title="Make a Payment",
    detail="Pay a Traffic ticket/ citation or other court-ordered fine or fee, including Criminal and Civil fines or fees",
  ),
  dict(
    id=7,
    title="Court Calendar",
    detail="View the five-day court calendar",
  ),
  dict(
    id=8,
    title="Judges and Departments",
    detail="View the department assignments for each of the San Diego Superior Court’s current judicial officers",
  ),
  dict(
    id=9,
    title="Bail Schedule",
    detail="",
  ),
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

COURT_LIST = [
    dict(
        id=1,
        link="http://www.alameda.courts.ca.gov/",
        title="Alameda",
        locations="https://www.courts.ca.gov/find-my-court.htm??query=Alameda",
        contact="http://www.alameda.courts.ca.gov/pages.aspx/phone-fax-numbers",              
        jury_info="http://www.alameda.courts.ca.gov/pages.aspx/jury-duty-overview",
        traffic="http://www.alameda.courts.ca.gov/Pages.aspx/Traffic",
        self_help="http://www.alameda.courts.ca.gov/Pages.aspx/Representing-Yourself",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=2,
        link="http://www.alpine.courts.ca.gov/",
        title="Alpine",
        locations="https://www.courts.ca.gov/find-my-court.htm??query=Alpine",
        contact="https://www.alpine.courts.ca.gov/generalinfo/index.htm",              
        jury_info="https://www.alpine.courts.ca.gov/generalinfo/jury.htm",
        traffic="https://www.alpine.courts.ca.gov/",
        self_help="https://www.alpine.courts.ca.gov/selfhelp/index.htm",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=3,
        link="http://www.amadorcourt.org/",
        title="Amador",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm??query=Amador",
        contact="http://www.amadorcourt.org/gi-contactUs.aspx",
        jury_info="http://www.amadorcourt.org/gi-juryServices.aspx",
        traffic="http://www.amadorcourt.org/dv-traffic.aspx",
        self_help="http://www.amadorcourt.org/sh-localResources.aspx",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=4,
        link="http://www.buttecourt.ca.gov/default.cfm",
        title="Butte",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm??query=Butte",
        contact="http://www.buttecourt.ca.gov/Information/Courthouses/",
        jury_info="http://www.buttecourt.ca.gov/Departments/Jury/",
        traffic="http://www.buttecourt.ca.gov/Departments/Traffic/",
        self_help="http://sharpcourts.org/",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=5,
        link="http://www.calaveras.courts.ca.gov/",
        title="Calaveras",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Calaveras",
        contact="http://www.calaveras.courts.ca.gov/info/contact",              
        jury_info="http://www.calaveras.courts.ca.gov/online-services/jury-service",
        traffic="http://www.calaveras.courts.ca.gov/divisions/traffic",
        self_help="http://www.calaveras.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=6,
        link="http://www.colusa.courts.ca.gov/",
        title="Colusa",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Colusa",
        contact="http://www.colusa.courts.ca.gov/contact_info.asp",              
        jury_info="http://www.colusa.courts.ca.gov/jury_service.asp",
        traffic="http://www.colusa.courts.ca.gov/traffic.asp",
        self_help="http://www.colusa.courts.ca.gov/self_help.asp",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=7,
        link="http://www.cc-courts.org/",
        title="Contra Costa",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Contra Costa",
        contact="http://www.cc-courts.org/general/court-phone.aspx",
        jury_info="http://www.cc-courts.org/jury/jury.aspx",
        traffic="http://www.cc-courts.org/traffic/traffic.aspx",
        self_help="http://www.cc-courts.org/family/self-help-center.aspx",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=8,
        link="http://www.delnorte.courts.ca.gov/",
        title="Del Norte",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Del Norte",
        contact="http://www.delnorte.courts.ca.gov/general-info",              
        jury_info="http://www.delnorte.courts.ca.gov/general-info/jury-service",
        traffic="http://www.delnorte.courts.ca.gov/divisions/traffic",
        self_help="http://www.delnorte.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=9,
        link="https://eldorado.courts.ca.gov",
        title="El Dorado",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=El Dorado",
        contact="https://eldorado.courts.ca.gov/general-information/locations-contact-info",              
        jury_info="https://eldorado.courts.ca.gov/divisions/jury",
        traffic="https://eldorado.courts.ca.gov/divisions/traffic",
        self_help="https://eldorado.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=10,
        link="http://www.fresno.courts.ca.gov/",
        title="Fresno",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Fresno",
        contact="https://www.fresno.courts.ca.gov/general-information/locations-contact-info",              
        jury_info="https://www.fresno.courts.ca.gov/divisions/jury-service",
        traffic="https://www.fresno.courts.ca.gov/divisions/traffic",
        self_help="https://www.fresno.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//5dca.htm",
        district="District 5",
    ),
    dict(
        id=11,
        link="http://www.glenncourt.ca.gov/",
        title="Glenn",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Glenn",
        contact="http://www.glenncourt.ca.gov/general-info/location-contact/telephone-directory.shtml",
        jury_info="http://www.glenncourt.ca.gov/divisions/trial-jury.shtml",
        traffic="http://www.glenncourt.ca.gov/divisions/traffic.shtml",
        self_help="http://www.glenncourt.ca.gov/self-help/index.shtml",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=12,
        link="http://www.humboldt.courts.ca.gov",
        title="Humboldt",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Humboldt",
        contact="http://www.humboldt.courts.ca.gov/gi/contact.htm",              
        jury_info="http://www.humboldt.courts.ca.gov/gi/jury.htm",
        traffic="http://www.humboldt.courts.ca.gov/dv/trafficdivision.htm",
        self_help="https://www.humboldt.courts.ca.gov/sh/index.htm",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=13,
        link="http://www.imperial.courts.ca.gov/",
        title="Imperial",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Imperial",
        contact="http://www.imperial.courts.ca.gov/",              
        jury_info="http://www.imperial.courts.ca.gov/juror.htm",
        traffic="http://www.imperial.courts.ca.gov/traffic.htm",
        self_help="http://www.imperial.courts.ca.gov/AccessCenter.htm",
        district_link="https://www.courts.ca.gov//4dca.htm",
        district="District 4",
    ),
    dict(
        id=14,
        link="https://www.inyo.courts.ca.gov/",
        title="Inyo",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Inyo",
        contact="https://www.inyo.courts.ca.gov/locations",              
        jury_info="https://www.inyo.courts.ca.gov/general-information/jury-service",
        traffic="https://www.inyo.courts.ca.gov/divisions/traffic",
        self_help="https://www.inyo.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//4dca.htm",
        district="District 4",
    ),
    dict(
        id=15,
        link="http://www.kern.courts.ca.gov/",
        title="Kern",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Kern",
        contact="http://www.kern.courts.ca.gov/home.aspx",              
        jury_info="http://www.kern.courts.ca.gov/home.aspx",
        traffic="http://www.kern.courts.ca.gov/",
        self_help="https://www.kern.courts.ca.gov/self_help/help_resources",
        district_link="https://www.courts.ca.gov//5dca.htm",
        district="District 5",
    ),
    dict(
        id=16,
        link="http://www.kings.courts.ca.gov/",
        title="Kings",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Kings",
        contact="http://www.kings.courts.ca.gov/generalinfo/contact-location.htm",              
        jury_info="http://www.kings.courts.ca.gov/generalinfo/jury.htm",
        traffic="http://www.kings.courts.ca.gov/divisions/traffic.htm",
        self_help="https://www.kings.courts.ca.gov/selfhelp/index.htm",
        district_link="https://www.courts.ca.gov//5dca.htm",
        district="District 5",
    ),
    dict(
        id=17,
        link="http://www.lake.courts.ca.gov/",
        title="Lake",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Lake",
        contact="http://www.lake.courts.ca.gov/gi/courtrooms_holidays.htm",              
        jury_info="http://www.lake.courts.ca.gov/dv/jury.htm",
        traffic="http://www.lake.courts.ca.gov/dv/traffic.htm",
        self_help="https://www.lake.courts.ca.gov/sh/index.htm",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=18,
        link="http://www.lassencourt.ca.gov/",
        title="Lassen",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Lassen",
        contact="http://www.lassencourt.ca.gov/general_info/location.shtml",
        jury_info="http://www.lassencourt.ca.gov/general_info/jury-services.shtml",
        traffic="http://www.lassencourt.ca.gov/court_divisions/traffic.shtml",
        self_help="http://www.lassencourt.ca.gov/self_help/index.shtml",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=19,
        link="http://www.lacourt.org/",
        title="Los Angeles",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Los Angeles",
        contact="http://www.lacourt.org/courthouse",
        jury_info="http://www.lacourt.org/division/jury/Jury.aspx",
        traffic="http://www.lacourt.org/division/traffic/traffic.aspx",
        self_help="http://www.lacourt.org/selfhelp/selfhelp.aspx",
        district_link="https://www.courts.ca.gov//2dca.htm",
        district="District 2",
    ),
    dict(
        id=20,
        link="http://madera.courts.ca.gov/",
        title="Madera",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Madera",
        contact="https://www.madera.courts.ca.gov/",              
        jury_info="http://madera.courts.ca.gov/MaderaJury.htm",
        traffic="http://madera.courts.ca.gov/MaderaProceduresTrafficLaw.htm",
        self_help="https://www.madera.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//5dca.htm",
        district="District 5",
    ),
    dict(
        id=21,
        link="http://www.marincourt.org/",
        title="Marin",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Marin",
        contact="http://www.marincourt.org/contact.htm",
        jury_info="https://www.marincourt.org/marinjury/JurorMain.aspx",
        traffic="http://www.marincourt.org/traffic.htm",
        self_help="http://www.marincourt.org/legal_self_help_services.htm",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=22,
        link="http://www.mariposacourt.org/",
        title="Mariposa",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Mariposa",
        contact="http://www.mariposacourt.org/",
        jury_info="http://www.mariposacourt.org/generalinfo/jury.shtml",
        traffic="https://www.mariposa.courts.ca.gov/divisions/traffic",
        self_help="https://www.mariposa.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//5dca.htm",
        district="District 5",
    ),
    dict(
        id=23,
        link="http://www.mendocino.courts.ca.gov/",
        title="Mendocino",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Mendocino",
        contact="https://www.mendocino.courts.ca.gov/general_info/locations.html",              
        jury_info="https://www.mendocino.courts.ca.gov/general_info/jury_service/jury-services.html",
        traffic="https://www.mendocino.courts.ca.gov/divisions/traffic/traffic.html",
        self_help="https://www.mendocino.courts.ca.gov/self_help/SHLA.html",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=24,
        link="http://www.mercedcourt.org",
        title="Merced",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Merced",
        contact="http://www.mercedcourt.org/contact_info.shtml",
        jury_info="http://www.mercedcourt.org/jury_services.shtml",
        traffic="http://www.mercedcourt.org/traffic.shtml",
        self_help="http://www.mercedcourt.org/self_help.shtml",
        district_link="https://www.courts.ca.gov//5dca.htm",
        district="District 5",
    ),
    dict(
        id=25,
        link="https://www.modoc.courts.ca.gov",
        title="Modoc",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Modoc",
        contact="https://www.modoc.courts.ca.gov/generalinfo/contact-location.htm",              
        jury_info="https://www.modoc.courts.ca.gov/generalinfo/jury-service.htm",
        traffic="https://www.modoc.courts.ca.gov/divisions/traffic-court.htm",
        self_help="https://www.modoc.courts.ca.gov/selfhelp/index.htm",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=26,
        link="http://www.mono.courts.ca.gov",
        title="Mono",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Mono",
        contact="https://www.mono.courts.ca.gov/generalinfo/contact-location.htm",              
        jury_info="http://www.mono.courts.ca.gov/generalinfo/jury.htm",
        traffic="http://www.mono.courts.ca.gov/divisions/traffic.htm",
        self_help="https://www.mono.courts.ca.gov/selfhelp",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=27,
        link="http://www.monterey.courts.ca.gov/",
        title="Monterey",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Monterey",
        contact="http://www.monterey.courts.ca.gov/General_Information/Locations.aspx",              
        jury_info="http://www.monterey.courts.ca.gov/JuryDuty/ReportingInstructions.aspx",
        traffic="http://www.monterey.courts.ca.gov/Traffic/",
        self_help="http://www.monterey.courts.ca.gov/SelfHelp/",
        district_link="https://www.courts.ca.gov//6dca.htm",
        district="District 6",
    ),
    dict(
        id=28,
        link="http://www.napa.courts.ca.gov/",
        title="Napa",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Napa",
        contact="https://www.napa.courts.ca.gov/general-information/holidays-hours-operation",              
        jury_info="http://www.napa.courts.ca.gov/divisions/jury",
        traffic="http://www.napa.courts.ca.gov/divisions/traffic",
        self_help="http://www.napa.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=29,
        link="http://nccourt.net/index.shtml",
        title="Nevada",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Nevada",
        contact="http://nccourt.net/geninfo/location-hours.shtml",
        jury_info="http://nccourt.net/divisions/jury.shtml",
        traffic="http://nccourt.net/divisions/traffic.shtml",
        self_help="http://nccourt.net/selfhelp/sh-center.shtml",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=30,
        link="http://www.occourts.org/",
        title="Orange",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Orange",
        contact="http://www.occourts.org/locations/general-phone.html",
        jury_info="http://www.occourts.org/directory/jury-services/",
        traffic="http://www.occourts.org/directory/traffic/",
        self_help="https://www.occourts.org/self-help/SelfHelpMain.html",
        district_link="https://www.courts.ca.gov//4dca.htm",
        district="District 4",
    ),
    dict(
        id=31,
        link="http://www.placer.courts.ca.gov",
        title="Placer",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Placer",
        contact="http://www.placer.courts.ca.gov/general-contact-us.shtml",              
        jury_info="http://www.placer.courts.ca.gov/general-jury-service.shtml",
        traffic="http://www.placer.courts.ca.gov/division-traffic-main.shtml",
        self_help="http://www.placer.courts.ca.gov/self-help-info.shtml",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=32,
        link="http://www.plumascourt.ca.gov/index.htm",
        title="Plumas",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Plumas",
        contact="http://www.plumascourt.ca.gov/Contact.htm",
        jury_info="http://www.plumascourt.ca.gov/Jury.htm",
        traffic="http://www.plumascourt.ca.gov/Traffic.htm",
        self_help="http://www.plumascourt.ca.gov/Self%20Help.htm",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=33,
        link="http://www.riverside.courts.ca.gov/",
        title="Riverside",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Riverside",
        contact="https://www.riverside.courts.ca.gov/GeneralInfo/PhoneNumbers/phone-numbers.php",              
        jury_info="https://www.riverside.courts.ca.gov/GeneralInfo/JuryInfo/jury-info.php",
        traffic="https://www.riverside.courts.ca.gov/Divisions/Traffic/traffic.php",
        self_help="https://www.riverside.courts.ca.gov/SelfHelp/self-help.php",
        district_link="https://www.courts.ca.gov//4dca.htm",
        district="District 4",
    ),
    dict(
        id=34,
        link="http://www.saccourt.ca.gov/",
        title="Sacramento",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Sacramento",
        contact="http://www.saccourt.ca.gov/general/court-phone.aspx",
        jury_info="http://www.saccourt.ca.gov/jury/jury.aspx",
        traffic="http://www.saccourt.ca.gov/traffic/traffic.aspx",
        self_help="https://www.saccourt.ca.gov/indexes/self-help.aspx",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=35,
        link="http://www.sanbenito.courts.ca.gov/",
        title="San Benito",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=San Benito",
        contact="https://www.sanbenito.courts.ca.gov/general-information/locations-contact-info",              
        jury_info="https://www.sanbenito.courts.ca.gov/general-information/jury-service",
        traffic="http://www.sanbenito.courts.ca.gov/court_divisions/traffic.shtml",
        self_help="https://www.sanbenito.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//6dca.htm",
        district="District 6",
    ),
    dict(
        id=36,
        title="San Bernardino",
        link="http://www.sb-court.org/",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=San Bernardino",
        contact="http://www.sb-court.org/Locations.aspx",
        jury_info="http://www.sb-court.org/JuryInformation.aspx",
        traffic="http://www.sb-court.org/Divisions/Traffic.aspx",
        self_help="https://www.sb-court.org/SelfHelp.aspx",
        district_link="https://www.courts.ca.gov//4dca.htm",
        district="District 4",
    ),
    dict(
        id=37,
        link="http://www.sdcourt.ca.gov/portal/page?_pageid=55,1&amp;_dad=portal&amp;_schema=PORTAL",
        title="San Diego",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=San Diego",
        contact="http://www.sdcourt.ca.gov/portal/page?_pageid=55,1056982&amp;_dad=portal&amp;_schema=PORTAL",
        jury_info="http://www.sdcourt.ca.gov/portal/page?_pageid=55,1406353&amp;_dad=portal&amp;_schema=PORTAL",
        traffic="http://www.sdcourt.ca.gov/portal/page?_pageid=55,1272147&amp;_dad=portal&amp;_schema=PORTAL",
        self_help="http://www.sdcourt.ca.gov/portal/page?_pageid=55,1665742&amp;_dad=portal&amp;_schema=PORTAL",
        district_link="https://www.courts.ca.gov//4dca.htm",
        district="District 4",
    ),
    dict(
        id=38,
        link="http://www.sfsuperiorcourt.org/",
        title="San Francisco",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=San Francisco",
        contact="http://www.sfsuperiorcourt.org/index.aspx?page=18",
        jury_info="http://www.sfsuperiorcourt.org/index.aspx?page=97",
        traffic="http://www.sfsuperiorcourt.org/divisions/traffic",
        self_help="https://sfsuperiorcourt.org/self-help",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=39,
        link="http://www.sjcourts.org/",
        title="San Joaquin",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=San Joaquin",
        contact="https://www.sjcourts.org/general-info/court-locations-contact/",
        jury_info="http://www.sjcourts.org/divisions/jury-service",
        traffic="http://www.sjcourts.org/divisions/traffic",
        self_help="https://www.sjcourts.org/self-help",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=40,
        link="http://www.slo.courts.ca.gov/",
        title="San Luis Obispo",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=San Luis Obispo",
        contact="http://www.slo.courts.ca.gov/gi/contact-location.htm",              
        jury_info="http://www.slo.courts.ca.gov/gi/jury.htm",
        traffic="http://www.slo.courts.ca.gov/dv/traffic.htm",
        self_help="https://www.slo.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//2dca.htm",
        district="District 2",
    ),
    dict(
        id=41,
        link="http://www.sanmateocourt.org/",
        title="San Mateo",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=San Mateo",
        contact="http://www.sanmateocourt.org/general_info/locations_and_contact_info/phone_numbers.php",
        jury_info="http://www.sanmateocourt.org/court_divisions/juror_services/",
        traffic="http://www.sanmateocourt.org/court_divisions/traffic/",
        self_help="https://www.sanmateocourt.org/self_help",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=42,
        link="http://www.sbcourts.org/",
        title="Santa Barbara",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Santa Barbara",
        contact="http://www.sbcourts.org/gi/loc/",
        jury_info="http://www.sbcourts.org/dv/jury-service.shtm",
        traffic="http://www.sbcourts.org/dv/traffic-minor-offenses.shtm",
        self_help="http://www.sbcourts.org/sh/index.shtm",
        district_link="https://www.courts.ca.gov//2dca.htm",
        district="District 2",
    ),
    dict(
        id=43,
        link="http://www.scscourt.org/",
        title="Santa Clara",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Santa Clara",
        contact="http://www.scscourt.org/general_info/contact/contact.shtml",
        jury_info="https://www.scscourt.org/online_services/jury/jury_duty.shtml",
        traffic="http://www.scscourt.org/online_services/traffic_epayments.shtml",
        self_help="http://www.scscourt.org/self_help.shtml",
        district_link="https://www.courts.ca.gov//6dca.htm",
        district="District 6",
    ),
    dict(
        id=44,
        link="https://www.santacruz.courts.ca.gov/",
        title="Santa Cruz",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Santa Cruz",
        contact="https://www.santacruz.courts.ca.gov/general-information/locations-contact-info",              
        jury_info="https://www.santacruz.courts.ca.gov/divisions/jury-division",
        traffic="https://www.santacruz.courts.ca.gov/divisions/traffic-division",
        self_help="https://www.santacruz.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//6dca.htm",
        district="District 6",
    ),
    dict(
        id=45,
        link="http://www.shasta.courts.ca.gov/",
        title="Shasta",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Shasta",
        contact="http://www.shasta.courts.ca.gov/General-Info/ContactInfo.shtml",              
        jury_info="http://www.shasta.courts.ca.gov/General-Info/JuryServices.shtml",
        traffic="http://www.shasta.courts.ca.gov/Divisions/Traffic.shtml",
        self_help="http://www.shasta.courts.ca.gov/Self-Help/self-help.shtml",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=46,
        link="http://sierra.courts.ca.gov",
        title="Sierra",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Sierra",
        contact="https://sierra.courts.ca.gov/",              
        jury_info="http://sierra.courts.ca.gov/generalinfo/jury_service.htm",
        traffic="http://sierra.courts.ca.gov/divisions/traffic.htm",
        self_help="https://www.sierra.courts.ca.gov/selfhelp/index.htm",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=47,
        link="http://www.siskiyou.courts.ca.gov/",
        title="Siskiyou",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Siskiyou",
        contact="http://www.siskiyou.courts.ca.gov/generalinfo/contact_locations.htm",              
        jury_info="http://www.siskiyou.courts.ca.gov/divisions/jury.htm",
        traffic="http://www.siskiyou.courts.ca.gov/divisions/traffic.htm",
        self_help="http://www.siskiyou.courts.ca.gov/selfhelp/index.htm",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=48,
        link="http://www.solano.courts.ca.gov/",
        title="Solano",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Solano",
        contact="https://solano.courts.ca.gov/",              
        jury_info="http://www.solano.courts.ca.gov/JuryInformation/default.html",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=49,
        link="http://sonoma.courts.ca.gov/",
        title="Sonoma",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Sonoma",
        contact="http://sonoma.courts.ca.gov/info",              
        jury_info="http://sonoma.courts.ca.gov/info/jury-service",
        traffic="http://sonoma.courts.ca.gov/divisions/traffic",
        self_help="http://sonoma.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//1dca.htm",
        district="District 1",
    ),
    dict(
        id=50,
        link="http://www.stanct.org/",
        title="Stanislaus",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Stanislaus",
        contact="https://www.stanct.org/court-locations-hours-holidays",
        jury_info="http://www.stanct.org/jury-services",
        traffic="http://www.stanct.org/traffic-division",
        district_link="https://www.courts.ca.gov//5dca.htm",
        district="District 5",
    ),
    dict(
        id=51,
        link="http://www.suttercourts.com/",
        title="Sutter",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Sutter",
        contact="https://www.suttercourts.com/general-info/locations-phone-numbers",
        jury_info="https://www.suttercourts.com/general-info/jury-service",
        traffic="http://www.suttercourts.com/divisions/traffic",
        self_help="http://www.suttercourts.com/self-help",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=52,
        link="http://www.tehama.courts.ca.gov",
        title="Tehama",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Tehama",
        contact="http://www.tehama.courts.ca.gov/generalinfo/contact-location.htm",              
        jury_info="http://www.tehama.courts.ca.gov/generalinfo/jury.htm",
        traffic="http://www.tehama.courts.ca.gov/divisions/traffic.htm",
        self_help="http://www.tehama.courts.ca.gov/selfhelp/index.htm",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=53,
        link="http://www.trinity.courts.ca.gov/",
        title="Trinity",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Trinity",
        contact="http://www.trinity.courts.ca.gov/#!contact-us/cyt2",              
        jury_info="http://www.trinity.courts.ca.gov/#!jury-services/c1b3w",
        traffic="http://www.trinity.courts.ca.gov/#!traffic/c106s",
        self_help="https://www.trinity.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=54,
        link="https://www.tulare.courts.ca.gov/",
        title="Tulare",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Tulare",
        contact="https://www.tulare.courts.ca.gov/general-information/locations-contact-info",              
        jury_info="https://www.tulare.courts.ca.gov/general-information/jury-services",
        traffic="https://www.tulare.courts.ca.gov/divisions/traffic",
        self_help="https://www.tulare.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//5dca.htm",
        district="District 5",
    ),
    dict(
        id=55,
        link="https://www.tuolumne.courts.ca.gov/",
        title="Tuolumne",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Tuolumne",
        contact="https://www.tuolumne.courts.ca.gov/index.shtml",              
        self_help="/selfhelp.htm",
        district_link="https://www.courts.ca.gov//5dca.htm",
        district="District 5",
    ),
    dict(
        id=56,
        link="http://www.ventura.courts.ca.gov/",
        title="Ventura",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Ventura",
        contact="http://www.ventura.courts.ca.gov/phone-directory.html",              
        jury_info="http://www.ventura.courts.ca.gov/JuryService",
        traffic="http://www.ventura.courts.ca.gov/traffic.html",
        self_help="http://www.ventura.courts.ca.gov/self-help.html",
        district_link="https://www.courts.ca.gov//2dca.htm",
        district="District 2",
    ),
    dict(
        id=57,
        link="http://www.yolo.courts.ca.gov/",
        title="Yolo",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Yolo",
        contact="http://www.yolo.courts.ca.gov/",              
        jury_info="http://www.yolo.courts.ca.gov/general-info/jury-services",
        traffic="http://www.yolo.courts.ca.gov/divisions/traffic",
        self_help="https://www.yolo.courts.ca.gov/self-help",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
    dict(
        id=58,
        link="http://www.yubacourts.org/",
        title="Yuba",
        terms="/11529.htm#Linking_and_Third",
        locations="https://www.courts.ca.gov/find-my-court.htm?query=Yuba",
        contact="http://www.yubacourts.org/Contact/contact.asp",
        jury_info="http://www.yubacourts.org/jury.html",
        traffic="http://www.yubacourts.org/divisions/traffic",
        self_help="http://www.yubacourts.org/self-help",
        district_link="https://www.courts.ca.gov//3dca.htm",
        district="District 3",
    ),
]

