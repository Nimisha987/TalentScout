from chatbot.memory import Memory
from chatbot.question_generator import generate_questions
from chatbot.storage import save_candidate

class ChatFlow:
    def __init__(self):
        self.memory = Memory()
        self.step = -1
        self.completed = False

        self.questions = [
            "Hello! I'm TalentScout 🤖. What's your full name?",
            "Please provide your email address.",
            "Your phone number?",
            "How many years of experience do you have?",
            "What position are you applying for?",
            "Where are you currently located?",
            "List your tech stack (comma separated):"
        ]

        self.tech_questions = []
        self.tech_q_index = 0
        self.in_tech_round = False

    def process(self, user_input):

        if self.completed:
            return "The interview is already completed. Thank you!"

        # ========== Technical round ==========
        if self.in_tech_round:

            current_question = self.tech_questions[self.tech_q_index]
            self.memory.data["tech_answers"][current_question] = user_input

            self.tech_q_index += 1

            if self.tech_q_index < len(self.tech_questions):
                return self.tech_questions[self.tech_q_index]
            else:
                save_candidate(self.memory.data)
                self.completed = True
                return "✅ Thank you for answering the technical questions.\n\n🎯 Our team will contact you soon. Have a great day!"

        # ========== Normal info collection ==========
        if self.step == 0:
            self.memory.data["name"] = user_input
        elif self.step == 1:
            self.memory.data["email"] = user_input
        elif self.step == 2:
            self.memory.data["phone"] = user_input
        elif self.step == 3:
            self.memory.data["experience"] = user_input
        elif self.step == 4:
            self.memory.data["position"] = user_input
        elif self.step == 5:
            self.memory.data["location"] = user_input
        elif self.step == 6:
            techs = [t.strip().lower() for t in user_input.split(",") if t.strip()]
            self.memory.data["tech_stack"] = techs

            tech_q_dict = generate_questions(techs)

            for tech, qs in tech_q_dict.items():
                for q in qs:
                    self.tech_questions.append(f"{tech}: {q}")

            self.in_tech_round = True
            self.tech_q_index = 0

            return self.tech_questions[0]

        self.step += 1
        return self.questions[self.step]
