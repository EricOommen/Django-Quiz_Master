from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Question(models.Model):
    TOPIC_CHOICES = [
        ("os", "Operating Systems"),
        ("dbms", "Database Management Systems"),
        ("dsa", "Data Structures & Algorithms"),
        ("networks", "Networks"),
        ("cloud", "Cloud Computing"),
    ]

    DIFFICULTY_LEVELS = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS)
    question_text = models.TextField()  # The question text
    correct_answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255, blank=True)
    option_2 = models.CharField(max_length=255, blank=True)
    option_3 = models.CharField(max_length=255, blank=True)
    option_4 = models.CharField(max_length=255, blank=True)

    def get_options(self):
        return [
            option
            for option in [self.option_1, self.option_2, self.option_3, self.option_4]
            if option
        ]

    def __str__(self):
        return self.question_text


class UserResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    level = models.CharField(max_length=50, default="beginner")
    score = models.IntegerField()
    total_questions = models.IntegerField(default=8)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return (
            f"{self.user.username} - {self.topic}: {self.score}/{self.total_questions}"
        )
