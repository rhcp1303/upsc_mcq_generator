from django.core.management.base import BaseCommand
import logging
from ...helpers import create_pdf_helper as helper

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'This is a utility management command for testing purpose'

    def handle(self, *args, **options):
        latex_code_questions = helper.create_question_pdf()
        latex_code_solutions = helper.create_solution_pdf()
        with open("latex_question.txt","w") as file:
            file.write(latex_code_questions)
        with open("latex_solution.txt","w") as file:
            file.write(latex_code_solutions)
        print("here")
