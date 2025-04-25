import json
from django.core.management.base import BaseCommand
import logging
from ...helpers import create_pdf_helper as helper

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'This is a utility management command for generating latex template for questions and solutions'

    def handle(self, *args, **options):
        with open("temp/mcq_output.json", "r") as file:
            questions = file.read()
        mcq_json = json.loads(questions)
        latex_template_for_questions = helper.create_latex_template_for_questions(mcq_json)
        latex_template_for_solutions = helper.create_latex_template_for_solutions(mcq_json)
        with open("temp/latex_question.txt", "w") as file:
            file.write(latex_template_for_questions)
        with open("temp/latex_solution.txt", "w") as file:
            file.write(latex_template_for_solutions)
