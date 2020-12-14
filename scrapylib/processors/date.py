import logging
from dateutil.parser import parse
from itemloaders.processors import Compose
from scrapylib.processors import default_output_processor

logger = logging.getLogger(__name__)


def parse_datetime(value):
    try:
        d = parse(value)
    except ValueError:
        logger.warning('Unable to parse %s' % value)
        return value
    else:
        return d.isoformat()

def parse_date(value):
    try:
        d = parse(value)
    except ValueError:
        logger.warning('Unable to parse %s' % value)
        return value
    else:
        return d.strftime("%Y-%m-%d")

default_out_parse_datetime = Compose(default_output_processor, parse_datetime)
default_out_parse_date = Compose(default_output_processor, parse_date)
