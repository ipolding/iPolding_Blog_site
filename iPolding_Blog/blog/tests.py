from datetime import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.

def create_entry(title):
    """ Creates a blog entry with a given title.
    The other fields are generated below
    """
    pub_date = datetime.now()


