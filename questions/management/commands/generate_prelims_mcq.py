from django.core.management.base import BaseCommand
from ...helpers import generate_prelims_mcq_helper as helper
import logging
from ...helpers import common_utils as cu

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Generate mcqs for upsc prelims mock test'


    def handle(self, *args, **options):
        content = helper.generate_mock_mcq(cu.PatternType.THREE_STATEMENTS,"Article 262, Article 263, Supreme court")
        print(content)
