from django.shortcuts import render

def profile(request):
    context = {
        "name": "Basavaraj",
        "tagline": "A Creative Developer passionate about building scalable and beautiful applications.",
        "email": "basava84310@gmail.com",
        "phone": "+91 8431057368",
        "linkedin": "https://www.linkedin.com/in/basavaraj-471427258/",
        "github": "https://github.com/basavagithubin",
        "profile_image": "https://avatars.githubusercontent.com/u/107114521?v=4",

        "education": [
            {
                "degree": "B.E Computer Science and Engineering",
                "institution": "MVJ College of Engineering, Bangalore",
                "date": "Jun 2023",
                "grade": "CGPA: 8.79"
            },
            {
                "degree": "PUC (PCMB)",
                "institution": "Vaishanavi Chethana PU College, Davangere, Karnataka",
                "date": "Jun 2019",
                "grade": "78.33%"
            },
            {
                "degree": "CBSE",
                "institution": "Gnyana Sudha Vidyalaya, Bidar, Karnataka",
                "date": "Jun 2017",
                "grade": "CGPA: 9.4"
            }
        ],

        "experience": [
            {
                "company": "Solar Secure Solutions",
                "role": "Full Stack Developer",
                "date": "Feb 2020 - May 2020",
                "details": [
                    "Developed production-ready code using modern front-end and back-end frameworks.",
                    "Built responsive applications with cross-platform UI web components.",
                    "Worked with HTML, CSS, JavaScript, React.js, and MongoDB."
                ]
            },
            {
                "company": "Talbotiq Private Limited, Malaysia",
                "role": "Software Developer",
                "date": "May 2020 - May 2024",
                "details": [
                    "Developed and maintained scalable web applications using Django and Python.",
                    "Performed software testing and provided customer support for issue resolution.",
                    "Gathered client requirements and delivered tailored solutions."
                ]
            }
        ],

        "projects": [
            {
                "title": "Gesture Recognition and Mouse Control Using Deep Learning",
                "tech": "Python, MySQL",
                "link": "https://github.com/basavagithubin",
                "desc": "Applied landmark detection techniques to identify hand points and trained a machine learning model."
            },
            {
                "title": "E-Commerce Website",
                "tech": "MERN Stack (React, Node.js, Express, MongoDB)",
                "link": "https://github.com/basavagithubin",
                "desc": "Designed and developed a full-stack e-commerce platform."
            },
            {
                "title": "Quiz-Grid App",
                "tech": "React.js",
                "link": "https://github.com/basavagithubin",
                "desc": "Built a dynamic quiz application with an interactive UI."
            },
            {
                "title": "Restaurant Management Website",
                "tech": "HTML, CSS, JavaScript, Bootstrap",
                "link": "https://github.com/basavagithubin",
                "desc": "Developed an engaging front-end UI for a restaurant management system."
            },
            {
                "title": "Twitter Website",
                "tech": "Python, Django, PostgreSQL",
                "link": "https://github.com/basavagithubin",
                "desc": "Built a Twitter clone with authentication, CRUD, REST APIs, and responsive UI."
            }
        ],

        "skills": [
            "Java", "Python", "PHP", "MySQL", "RDBMS", 
            "React", "JavaScript", "TypeScript", "HTML/CSS", "REST API", 
            "MongoDB", "Django", "Spring Boot", "Git", "PHPMyAdmin"
        ]
    }
    return render(request, "profile.html", context)
