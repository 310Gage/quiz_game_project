class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input("\nQ.{}: {} (True/False): \n".format(self.question_number, current_question.text))
        self.check_answer(user_answer, current_question.answer)
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.upper() == correct_answer.upper():
            self.score += 1
            print('yup yup, that seems right.')
        else:
            print('uhhhh... not sure about that one.')
            print(f'The answer was {correct_answer}')
            if self.score < 3:
                print(f'your score isnt looking too hot: {self.score}')
            else:
                print(f'your score is: {self.score}')
                
            