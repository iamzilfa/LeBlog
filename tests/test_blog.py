import unittest
from app.models import Blog
Blog = Blog

class BlogTest(unittest.TestCase):

    def setUp(self):

        self.new_blog = Blog()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))
