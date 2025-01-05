# MindTrek: Interactive Quiz Application

MindTrek is an interactive quiz application that allows users to test their knowledge on various topics or topics. This project demonstrates the use of Django for backend development and a responsive frontend built with HTML and CSS. It incorporates user authentication, dynamic scoring, and filtering quizzes by topics.

## Features

1. **User Authentication**:
   - Registration and Login.
   - Logout functionality.

2. **Quizzes by Topics**:
   - Quizzes are categorized by topics (e.g., Mathematics, Seerah, IT).
   - Users can filter quizzes by topic.

3. **Interactive Quiz**:
   - Multiple-choice questions.
   - Scoring system based on points per question.
   - Feedback for correct and incorrect answers with explanations.

4. **User Progress Tracking**:
   - Users can view their quiz attempts.
   - Scores and performance percentages are calculated and displayed.
   - Average score percentage across all quizzes attempted.

5. **Responsive Design**:
   - Fully responsive layout for both desktop and mobile devices.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default for Django)
- **Others**: Django Templates

## Installation and Setup

### Prerequisites
- Python 3.x installed
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Steps

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd MindTrek
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Database Schema

### Tables
1. **User**:
   - `id`: Primary key
   - `username`: Unique username
   - `email`: User email
   - `password`: Hashed password

2. **Topic**:
   - `id`: Primary key
   - `name`: Name of the topic
   - `description`: Description of the topic

3. **Quiz**:
   - `id`: Primary key
   - `title`: Quiz title
   - `description`: Quiz description
   - `topic`: Foreign key referencing `Topic`
   - `points_per_question`: Points awarded per question

4. **Question**:
   - `id`: Primary key
   - `quiz`: Foreign key referencing `Quiz`
   - `text`: Question text
   - `explanation`: Explanation for the correct answer

5. **Answer**:
   - `id`: Primary key
   - `question`: Foreign key referencing `Question`
   - `text`: Answer text
   - `is_correct`: Boolean indicating whether the answer is correct

6. **UserQuizAttempt**:
   - `id`: Primary key
   - `user`: Foreign key referencing `User`
   - `quiz`: Foreign key referencing `Quiz`
   - `score`: User's score for the quiz

7. **UserAnswer**:
   - `id`: Primary key
   - `attempt`: Foreign key referencing `UserQuizAttempt`
   - `question`: Foreign key referencing `Question`
   - `selected_answer`: Foreign key referencing `Answer`

## Usage

### Register and Login
1. Create an account or log in to access quizzes.
2. Navigate to the dashboard to view available quizzes.

### Take a Quiz
1. Select a quiz by topic.
2. Answer questions and submit the quiz.
3. View your score, feedback, and explanations for each question.

### View Progress
1. Access your quiz history to view all attempted quizzes.
2. See scores, percentages, and average performance.

## Future Enhancements
1. Add support for time-limited quizzes.
2. Include leaderboards for competitive scoring.
3. Implement additional question types (e.g., true/false, short answer).
4. Add functionality to upload quizzes via CSV files.

## Authors

- **Mohammed Khalilu Rahman**  
  Final-year Computer Engineering student and aspiring Software Engineer. Passionate about web development and creating impactful digital solutions.  
  [Follo on Github](https://github.com/krmohammed)

- **Contributors**  
  A special thanks to all contributors who have helped improve this project through feedback, testing, and feature additions.
<!-- ## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Submit a pull request. -->

<!-- ## License
This project is licensed under the MIT License. See the LICENSE file for details. -->

