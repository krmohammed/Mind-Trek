from quiz.models import Quiz, Question, Answer

def create_questions(quiz_id, questions_data):
    """
    Adds questions and answers to a specific quiz.

    :param quiz_title: Title of the quiz to which the questions belong
    :param questions_data: A list of dictionaries containing question text and answer choices
    """
    try:
        quiz = Quiz.objects.get(id=quiz_id)
    except Quiz.DoesNotExist:
        print(f"Quiz with id '{quiz_id}' does not exist.")
        return

    for question_data in questions_data:
        # Create the question
        question = Question.objects.create(
            quiz=quiz,
            text=question_data['text']
        )
        print(f"Added question: {question.text}")

        # Add answers for the question
        for answer_data in question_data['answers']:
            Answer.objects.create(
                question=question,
                text=answer_data['text'],
                is_correct=answer_data['is_correct']
            )
            print(f"  - Added answer: {answer_data['text']} (Correct: {answer_data['is_correct']})")

    print(f"All questions and answers added to quiz: {quiz.title}")

