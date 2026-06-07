# save as create_chunks.py
# run: python create_chunks.py
# Output: chunk.pkl

import pickle

chunks = [
    {
        "topic": "Government_college and Counselling Code",
        "content": """
ANNA UNIVERSITY REGIONAL CAMPUS MADURAI (AURCM)

Official Name: Anna University Regional Campus Madurai
Affiliation: Constituent campus of Anna University, Chennai
Location: NH-7 Kanyakumari National Highway, Keelakuilkudi Road, Madurai-625019, Tamil Nadu
Nearby City: Madurai
Counselling Code: 5010
Type: Government Engineering Campus
Admission Mode: Primarily through TNEA counselling for undergraduate programmes
Controlling University: Anna University Chennai
"""
    },
{
        "topic": "Support Mail , Student Section and other mails",
        "content": """ 
Support and Contact:
Student Section: 0452-2555 544
Email: helpdesk@autmdu.in
Dean Email: dean@autmdu.ac.in
Placements: tpo_aurcm@autmdu.in
POSH Cell: aurcmposhcell@autmdu.in
Grievance Cell: aurcmgrievancecell@autmdu.in
"""
    },

    {
        "topic": "location_accessibility",
        "content": """
LOCATION AND ACCESSIBILITY

Location: NH-7 Kanyakumari National Highway, Keelakuilkudi Road, Madurai-625019, Tamil Nadu
Campus Name: Anna University Regional Campus Madurai
Location and Address: NH-7 Kanyakumari National Highway, Keelakuilkudi Road, Madurai-625019, Tamil Nadu

Nearest Railway Station: Madurai Junction
Nearest Airport: Madurai Airport

Campus Area: Spacious campus outside central city area
Environment: Calm academic atmosphere with greenery and open space
"""
    },

    {
        "topic": "transport_bus_facility",
        "content": """

TRANSPORT / BUS FACILITY

College Transport:
Bus facility may be available for students and staff from:
- Mattuthavani Bus Stand
- Periyar Bus Stand
- Arapalayam Bus Stand

Private Bus Access:
Public buses and town buses available from Madurai city.

Travel Recommendation:
Students can take direct buses to AURCM.
Students can also take any 48 series bus from Mattuthavani Bus Stand or Periyar Bus Stand stop at Thirunagar Third Stop.
From Thirunangar, autos can be used to reach the college.

Bus Timing:
Direct Bus : Morning 7.45 AM in Mattuthavani Bus Stand
Direct Bus : Morning 8:00 AM in Periyar
Direct Bus :5:00 PM from college to Mattuthavani and Periyar Bus Stop
Indirect: 48 Series bus are available at any Time.


Travel Time:
- Periyar Bus Stand: 45 to 60 minutes
- Mattuthavani: 60 to 80 minutes
- Arapalayam: 45 to 60 minutes


Transport Charges:
- Bus fare/Cost: Rs.25 to Rs.40
- Auto fare/Cost from Thirunagar: Rs.20


"""
    },

    {
        "topic": "hostel_facility",
        "content": """
HOSTEL FACILITY

Hostel Availability:
Separate hostels available for boys and girls.

Hostel Count:
- 2 hostels for boys
- 2 hostels for girls

Room Type:
Shared rooms depending on allotment.

Room Facilities:
- Electrical facilities
- Two fans
- Cots for students
- Cupboards
- Plug points

Other Facilities:
- Water supply
- Electricity
- Study environment
- Security
- Basic maintenance

Hostel Admission:
Done after college starting dates.

Mess Facility:
Neat and clean mess with varieties of foods.


Students should confirm latest vacancy and fee details with hostel office.
"""
    },

{
    "topic": "Anna_University_Lateral_Entry_Admission",
    "content": """
LATERAL ENTRY ADMISSION – ANNA UNIVERSITY

Lateral Entry admission allows eligible Diploma or B.Sc. students to join directly into the second year of B.E./B.Tech programs in Anna University colleges such as MIT and CEG.

ELIGIBILITY

Candidates are eligible if they have completed:
1. Diploma in Engineering / Technology
OR
2. B.Sc. Degree

APPLICATION PROCESS

1. Apply through the Tamil Nadu Lateral Entry Admission (TNLEA) portal.
2. Fill the online application form.
3. Upload required documents.
4. Pay the admission fee online.
5. Attend online counseling.
6. Seat allotment is based on merit and seat availability.

Official Admission Portal:
https://www.auegov.ac.in/Admissions/

REPORTING TO COLLEGE

After seat allotment, candidates must report to the allotted campus on the specified date and time with original documents.

Example Reporting Locations:
- MIT Campus, Chromepet, Chennai
- CEG Campus, Guindy, Chennai

The exact reporting schedule will be mentioned in the allotment details.

FEE PAYMENT

- Fees must be paid online only through the Anna University admission portal.
- Fee payment should be completed before reporting to the campus.

HOSTEL FACILITY

Students requiring hostel accommodation can contact the respective campus hostel office after admission confirmation.

REQUIRED DOCUMENTS

Candidates generally need:
- Transfer Certificate (TC)
- Conduct Certificate
- Diploma / B.Sc. Mark Sheets
- Community Certificate (if applicable)
- Passport-size Photographs
- Other documents mentioned in the allotment order

IMPORTANT INSTRUCTIONS

- Report on the correct date and time.
- Submit all required documents properly.
- Late submission of TC may result in additional fees.
- Regularly check the official admission portal for updates and notifications.

By following these procedures, eligible students can secure lateral entry admission into Anna University B.E./B.Tech programs.
"""
},

{
    "topic": "Anna_University_Transfer_Application_Process",
    "content": """
TRANSFER APPLICATION PROCESS – ANNA UNIVERSITY

Students seeking transfer between engineering colleges affiliated with Anna University must follow the official transfer procedure.

CONTACT AUTHORITY

Candidates seeking transfer between self-financing and government engineering colleges should contact the Directorate of Technical Education (DOTE), Chennai.

ELIGIBILITY CRITERIA

Students must satisfy the following condition:
- Completion of the first year of the course.

APPLICATION PROCESS

1. Transfer applications must be submitted online.
2. The application should include:
   - Consent from the Principal of the current college (Transferor College)
   - Consent from the Principal of the new college (Transferee College)

GRIEVANCE REDRESSAL

If students face issues during the transfer process, they can approach the Grievance Redressal Cell constituted by Anna University for support and clarification.

IMPORTANT NOTES

- Transfer approval depends on eligibility, seat availability, and university regulations.
- Students should regularly check official Anna University or DOTE notifications for updates.
"""
},
{
    "topic": "TamilNadu_7_5_Percent_Reservation",
    "content": """
7.5% RESERVATION – TAMIL NADU GOVERNMENT SCHOOLS

The Government of Tamil Nadu provides a 7.5% special reservation for students who studied in Government Schools from Classes 6 to 12.

PURPOSE

The reservation helps Government School students get admission in professional courses such as:
- Engineering
- Medical
- Agriculture
- Veterinary
- Fisheries
- Law and other professional courses

ELIGIBILITY

Students are eligible if they:
1. Studied from 6th Standard to 12th Standard completely in Tamil Nadu Government Schools.
2. Qualified in the respective entrance or counseling process.
3. Apply through the regular counseling process.

APPLICABLE INSTITUTIONS

The 7.5% reservation is applicable in:
- Government Colleges
- Government Quota seats in Self-Financing Colleges
- Universities under Tamil Nadu admissions

BENEFITS

Eligible students may receive:
- Special reservation seats
- Tuition fee concessions provided by the Tamil Nadu Government in certain courses and colleges

REQUIRED DOCUMENTS

Candidates generally need:
- Government School Study Certificate
- Community Certificate (if applicable)
- Transfer Certificate
- Mark Sheets
- Counseling documents

IMPORTANT NOTES

- The reservation is applicable only for eligible Government School students.
- Students must produce valid certificates during counseling and admission.
- False information or invalid certificates may lead to cancellation of admission.
- Admission is based on merit and reservation rules of Tamil Nadu Government.

Students should regularly check official Tamil Nadu counseling and admission portals for latest updates and instructions.
"""
},

    {
        "topic": "hostel_mess",
        "content": """
HOSTEL MESS FACILITY

Mess Foods are only for Hostel Students and College Staffs not for dayscholars.

Mess Type:
Student mess / common dining

Meals Usually Provided:
- Breakfast
- Lunch
- Dinner
- Tea / Snacks depending on schedule
"""
    },

    {
        "topic": "college_infrastructure",
        "content": """
COLLEGE INFRASTRUCTURE

Infrastructure Highlights:
- Academic blocks
- Department buildings
- Laboratories
- Library
- Seminar halls
- Auditorium / event halls
- Computer Labs
- Hostel buildings
- Playground
- Canteen
- Internal roads
- Parking area
- Green campus atmosphere
"""
    },

    {
        "topic": "canteen",
        "content": """
COLLEGE CANTEEN

Availability:
Campus canteen available

Day Scholar Students, Hostel Student and all Visitors to the college can take foods in Canteen.

Food Options:
- Tea / Coffee
- Snacks
- Lunch meals
- Juice / Beverages depending on vendor
"""
    },

    {
        "topic": "sports_ground",
        "content": """
PLAYGROUND / SPORTS GROUND / SPORTS /SPORTS ACTIVITIES

Ground Availability:
Open playground for sports and student activities.

Sports:
- Cricket
- Football
- Volleyball
- Kabaddi
- Athletics
- Badminton

Practice Time:
- Morning: 5:00 AM to 7:00 AM
- Evening: 5:00 PM to 7:00 PM
"""
    },

    {
        "topic": "faculty",
        "content": """
FACULTY DETAILS

Faculty Nature:
- Qualified professors
- Assistant professors
- Associate professors
- Technical staff

Strengths:
- Experienced teaching staff
- Subject expertise
- Guidance for projects
- Exam preparation support
"""
    },

    {
        "topic": "academic_system",
        "content": """
ACADEMIC SYSTEM

University Regulation: Anna University regulations
Semester Pattern: Semester based academic system
Typical UG Duration: 4 years
Total Semesters: 8 semesters

Assessment:
- Internal assessment
- Assignments
- Lab records
- Semester examinations
"""
    },

    {
        "topic": "departments_courses",
        "content": """
DEPARTMENTS / COURSES

Undergraduate Departments :
1. Computer Science and Engineering (CSE)
2. Electronics and Communication Engineering (ECE)
3. Electrical and Electronics Engineering (EEE)
4. Mechanical Engineering
5. Civil Engineering
6. Computer Science and Engineering with Artificial Intelligence and Machine Learning (CSE & AIML)

Postgraduate Department:
1. Master of Business Administration (MBA)
"""
    },

    {
        "topic": "seats_intake",
        "content": """
NUMBER OF SEATS

UG:
- CSE: 60
- ECE: 60
- EEE: 60
- Mechanical: 60
- Civil: 60
- AIML: 30

PG:
- MBA: 60

Exact sanctioned intake may change yearly.
"""
    },

    {
        "topic": "admission_details",
        "content": """
ADMISSION DETAILS

Admission Method:

Undergraduate:
- Through TNEA Counselling

Postgraduate:
- Through TANCET

Eligibility:

UG:
- HSC / 12th standard with Physics, Chemistry, Maths

PG:
- TANCET Score

Selection Basis:

UG:
- TNEA rank / merit list
- 7.5 reservation for government school students

PG:
- TANCET scores
"""
    },


{
        "topic": "admission_process",
        "content": """
  
ADMISSION PROCESS

1.Step-by-Step Abstract Process:Online Registration & Profile Creation: Register on the official TNEA portal by creating a user ID and password.
2.Application Form Filling & Document Upload: Complete the application form, entering academic details (marks) and personal information.Upload necessary documents (10th/12th mark sheets, community certificate, etc.).
3.Application Fee Payment: Pay the application fee online (varies for general/reserved categories).
4.Rank List Publication: Anna University generates a rank list based on the calculated cut-off marks Mathematics + (Physics / 2) + (Chemistry / 2).
5.Counseling & Choice Filling: Eligible candidates select their preferred colleges (e.g., Anna University Departments, affiliated colleges) and branches (CSE, ECE, etc.) in order of preference during the specified window.
6.Seat Allotment: Based on the rank, reservation rules, and preferences, seats are allotted through a digital system.
7.Provisional Admission & Joining: Confirm the seat by paying fees. Successful candidates receive provisional allotment letters to report to the college.
8.College Admission:After receiving provisional allotment letters to report to the college with necessary Documents.

For PG courses (MBA), admission is based on the TANCET exam

"""
    },

    {
        "topic": "admission_documents",
        "content": """
ADMISSION DOCUMENTS REQUIRED

- 10th Marksheet
- 12th Marksheet
- Transfer Certificate
- Community Certificate
- Nativity Certificate if required
- Income Certificate if required
- Passport size photos
- Aadhaar copy
- TNEA allotment order
- First Graduate certificate if applicable
- Medical fitness / declaration if required
"""
    },

    {
        "topic": "lab_facilities",
        "content": """
LAB FACILITIES

Available Labs:

Computer Science And Engineering Labs :-
- Database Management Lab
- CCC Lab
- Python Lab
- Artificial Intelligence and Machine Learning Lab

Electrical and Communication Labs:-
- Electronics Lab
- Electrical Machines Lab
-Digital Signal Processing Lab

Electrical And Electronic Engineering Labs:-
- Electronics Lab
- Electrical Machines Lab

Science and Humanities Lab:-
- Physics Lab
- Chemistry Lab
- Language Lab
- Internet-enabled computer lab

Additional:
Free WiFi and separate passwords allotted to students.
"""
    },

    {
        "topic": "library",
        "content": """
LIBRARY FACILITY

Library Availability:
Central library

Resources:
- Textbooks
- Reference books
- Journals
- Digital materials
- Newspapers
"""
    },
{
    "topic": "Career_Counselling_For_College_Students",
    "content": """
CAREER COUNSELLING FOR COLLEGE STUDENTS

Career counselling helps college students identify their interests, skills, strengths, and career opportunities to make better decisions for their future.

PURPOSE OF CAREER COUNSELLING

Career counselling helps students:
- Choose suitable career paths
- Understand job opportunities
- Improve career planning
- Prepare for higher studies or placements
- Build confidence and communication skills

AREAS COVERED

Career counselling may include guidance in:
- Engineering careers
- IT and Software jobs
- Government jobs
- Core industry jobs
- Higher education in India or abroad
- Entrepreneurship and startups
- Competitive exam preparation

CAREER COUNSELLING PROCESS

1. Understanding student interests and strengths
2. Identifying career goals
3. Exploring available career opportunities
4. Providing guidance for skill development
5. Planning internships, projects, and certifications
6. Preparing students for placements and interviews

IMPORTANT SKILLS FOR STUDENTS

Students are encouraged to improve:
- Communication skills
- Technical knowledge
- Aptitude and reasoning
- Problem-solving ability
- Resume building
- Interview skills
- Teamwork and leadership

BENEFITS

Career counselling helps students:
- Reduce confusion about careers
- Select the right specialization or job field
- Increase placement opportunities
- Improve self-confidence
- Make informed career decisions

COMMON CAREER OPTIONS AFTER COLLEGE

Students may choose:
- Private sector jobs
- Government sector jobs
- Higher studies (M.E., M.Tech., MBA, MS, etc.)
- Research careers
- Entrepreneurship
- Freelancing and remote work opportunities

IMPORTANT NOTE

Students should regularly update their skills, participate in internships, attend workshops, and stay informed about industry trends to improve career opportunities.
"""
},

    {
        "topic": "events",
        "content": """
EVENTS / CULTURAL / TECHNICAL

Possible Events:
- Symposium
- Technical workshops
- Hackathons
- Cultural fest
- Department seminars
- Sports day
- Freshers day
- Farewell events
"""
    },

    {
        "topic": "scholarships",
        "content": """
SCHOLARSHIPS

Available Scholarships:
- First Graduate Scholarship
- BC / MBC / SC / ST Scholarships
- HP Scholarships
- Government Scholarship Schemes


First Graduate Scholarship:
Provided to students who are first in family to pursue a degree.
Requires First Graduate Certificate from Tahsildar.

HP Scholarships:

HP Scholarship/Hindustan Petroleum Corporation Limited (HPCL) offers the Unnati Post Metric Scholarship for SC/ST/OBC/PwD students in graduation and post-graduation with family incomes below ₹2.5 lakhs per annum. 

BC / MBC / SC / ST Scholarships:
Tamil Nadu government scholarships for BC/MBC/DNC and SC/ST students, typically for those with a family income under ₹2.5 Lakh per annum, offer tuition fee waivers, boarding grants, and hostel fee exemptions. Applications for the 2025-2026 cycle are available through college websites or district welfare.

Government Scholarship Schemes:
Tamil Nadu government scholarship schemes (2026) focus on supporting BC/MBC/DNC/SC/ST students, rural girl students, and individuals with disabilities. Key programs include the Pudhumai Penn Scheme (₹1,000/month for girls), Tamil Pudhalvan Scheme (₹1,000/month for boys), and various fee reimbursements for technical/professional courses managed via ssp.tn.gov.in.

Students should verify latest scholarship details and deadlines.
"""
    },
{
        "topic": "scholarship_Procedure",
        "content": """
SCHOLARSHIP Procedure

Step 1: Research & Inquiry: You visit the college's Student Section (office) to find out which specific scholarships (private, state, or institutional) you qualify for.
Step 2: Procurement: You physically collect the hard-copy application form from the office.
Step 3: Validation: You fill it out and visit various departments to get official seals and signatures from professors or heads of departments to prove your attendance and conduct.
Step 4: Documentation: You gather physical photocopies of your records (marks, income, caste, etc.).Step 5: Submission: You hand in the completed bundle back to the office before the official deadline.

Important:Make sure your Bank Account is seeded with your Aadhaar Number.
"""
    },

    {
        "topic": "scholarship_documents",
        "content": """
SCHOLARSHIP DOCUMENTS

- Income certificate
- Community certificate
- Aadhaar
- Bank passbook
- Mark statements
- Bonafide certificate
- First graduate certificate
- Fee receipt
- Passport photos
"""
    },


 {
        "topic": "revaluation Procedure",
        "content": """

REVALUATION PROCEDURE

Anna University allows students to apply for revaluation of their exam answer scripts after obtaining a photocopy, with specific fees and a structured review process.

Step-by-Step Revaluation Process:

1.Obtain Photocopy of Answer Script:
   * Students must first apply for a photocopy of their answer script by paying  ₹300 per script before the last date for photocopy applications (). 
   *After receiving the photocopy, students should carefully check for discrepancies such as totaling errors or omissions in valuation. Any issues can be reported to the Additional Controller of Examinations for remedial action (). 

2.Apply for Revaluation
*If the student identifies potential errors or believes the marks are lower than   deserved, they can apply for revaluation.
*The revaluation fee is ₹400 per subject (). 
*The application must be submitted through the respective college or study center, along with the fee, before the deadline (). 


3.Expert Valuation
*The answer script is re-evaluated by a subject expert appointed by the Head of the Department (). 
*If the expert recommends a higher grade, the revaluation is processed, and the updated result is published on the COE portal (). 

4.Review (Challenge Revaluation)
*If the student is still not satisfied after revaluation, they can request a  review of the answer script by paying ₹3,000 per subject (). 
*The review is conducted by another expert, and if the grade increases, the fee is refunded (). 

Important Notes:
* Eligibility: Only students who have obtained the photocopy of their answer script are eligible for revaluation (). 
* Deadlines: All applications must be submitted within the prescribed dates; late or incomplete applications are rejected, and fees are non-refundable (). 
* Result Checking: Updated revaluation results can be checked on the Anna University COE portal by logging in with your register number and date of birth (). 
* Recommendation: It is advisable to consult faculty after obtaining the photocopy before applying for revaluation to assess the likelihood of a grade change ().

This structured process ensures transparency and gives students a fair opportunity to verify and improve their academic performance.
"""
    },


    {
        "topic": "placements",
        "content": """
PLACEMENTS

AURCM has an active placement cell.

The Training and Placement Cell of Anna University Regional Campus Madurai, in coordination with the Centre for University-Industry Collaboration (CUIC), facilitates the final year students to appear for placement interviews with the industries visiting Anna University. The prefinal year students are offered Summer Internships in various industries with very good stipends. The students are provided with required training and supports to obtain internships and placements.

Activities:
- Campus interviews
- Recruitment drives
- Aptitude training
- Technical training
- Communication skill training
- Interview preparation
- Internship support

Recruiter Types:
- IT companies
- Core engineering companies
- Service companies

Top Recruiters:
- Zoho
- TCS
- Aptean
- Vtiger
- Foxconn
- Vaken
- Chella Software

Placement depends on student skills and performance.
"""
    },

    {
        "topic": "student_support_safety",
        "content": """
STUDENT SUPPORT / SAFETY

No ragging and Students maintains friendly relationship.

Facilities:
- Anti-ragging support
- Student grievance support
- Faculty advisors
- Security personnel
- CCTV in important areas
- Medical support nearby
- First aid
"""
    }
]

# Save chunk.pkl
with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("chunk.pkl created successfully with", len(chunks), "topic chunks.")