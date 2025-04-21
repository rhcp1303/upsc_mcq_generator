from django.core.management.base import BaseCommand
import logging
from ...helpers import create_pdf_helper as helper

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'This is a utility management command for testing purpose'

    def handle(self, *args, **options):
        latex_code = helper.create_pdf()
        with open("latex.txt","w") as file:
            file.write(latex_code)
        print("here")
