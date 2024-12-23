from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Question, UserResult


def home(request):
    context = {
        "background_image": "quiz/images/background.jpg",
    }
    return render(request, "quiz/home.html", context)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print("Form errors:", form.errors)
    else:
        form = UserCreationForm()
    context = {
        "form": form,
        "background_image": "quiz/images/background.jpg",
    }
    return render(request, "quiz/signup.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    context = {
        "background_image": "quiz/images/background.jpg",
    }
    return render(request, "quiz/login.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def topic_selection(request):
    context = {
        "background_image": "quiz/images/background.jpg",
    }
    return render(request, "quiz/topic_selection.html", context)


@login_required
def experience_level(request, topic):
    if request.method == "POST":
        level = request.POST.get("level")
        return redirect("quiz_page", topic=topic, level=level)
    context = {"topic": topic, "background_image": "quiz/images/background.jpg"}
    return render(request, "quiz/experience_level.html", context)


def quiz_page(request, topic, level):
    questions = Question.objects.filter(topic=topic, difficulty=level)

    # Store topic and level in the session
    request.session["topic"] = topic
    request.session["level"] = level

    context = {
        "background_image": "quiz/images/background.jpg",
        "questions": questions,
        "topic": topic,
        "level": level,
    }
    return render(request, "quiz/quiz_page.html", context)


@login_required
def result_page(request):
    if request.method == "POST":
        # Retrieve topic and level from session
        topic = request.session.get("topic")
        level = request.session.get("level")

        if not topic or not level:
            return redirect("home")  # Redirect to home if session data is missing

        questions = Question.objects.filter(topic=topic, difficulty=level)
        score = 0
        total_questions = questions.count()

        for question in questions:
            user_answer = request.POST.get(f"q{question.id}")
            if user_answer == question.correct_answer:
                score += 1

        # Save the result for the user with total_questions
        UserResult.objects.create(
            user=request.user,
            topic=topic,
            level=level,
            score=score,
            total_questions=total_questions,
        )

        context = {
            "background_image": "quiz/images/background.jpg",
            "score": score,
            "total_questions": total_questions,
        }
        return render(request, "quiz/result_page.html", context)
    return redirect("home")


@login_required
def history_page(request):
    # Get results for the logged-in user
    user_results = UserResult.objects.filter(user=request.user)

    context = {
        "background_image": "quiz/images/background.jpg",
        "user_results": user_results,
    }
    return render(request, "quiz/history.html", context)
