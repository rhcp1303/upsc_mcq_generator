from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import json


@api_view(['GET'])
def test1(request):
    with open('questions/data/flt/test1.json', 'r') as f:
        data = json.load(f)
    return Response(data, status=200)

@api_view(['POST'])
def evaluate_test(request):
    data = request.data
    questions = data.get('questions')
    answers = data.get('answers')
    score = 0
    explanations = []
    for i, question in enumerate(questions):
        correct_answer_index = question['correct_option']
        user_answer_index = answers.get(str(i))
        is_correct = user_answer_index is not None and user_answer_index == correct_answer_index
        if is_correct:
            score += 1
        explanations.append(question['explanation'])
    return Response({'score': score, 'explanations': explanations})

def test1_view(request):
    return render(request, 'test1_view.html')
