def generate_questions(tech_stack):
    questions = {}

    for tech in tech_stack:
        tech_title = tech.capitalize()

        questions[tech_title] = [
            f"What is {tech_title} and where is it used?",
            f"Explain an advanced feature of {tech_title}.",
            f"Describe a real-world project using {tech_title}.",
            f"What are common issues faced in {tech_title}?"
        ]

    return questions
