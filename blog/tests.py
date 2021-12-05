from typing import Text
from django.test import TestCase, Client
from blog.models import Post, Comment
# Create your tests here.
from django.contrib.auth.models import User



class ModelsTestCase(TestCase):

    def __init__(self, *args, **kwargs):
        self.title = "My first post"
        super(ModelsTestCase, self).__init__(*args, **kwargs)
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'password')
        self.client.login(username='testuser', password='password')
        self.post = Post.objects.create(title='My first post', author=self.user)
        self.comment = Comment(post=self.post, author=self.user, text="My first comment")
        
    def test_post_is_created(self):
        """Post is created"""
        post = Post.objects.get(title=self.title)
        self.assertEqual(post.title, self.title)

    
    def test_string_representation(self):
        """Post string representation"""
        post = Post.objects.get(title=self.title)
        self.assertEqual(str(post),self.title)

    def test_post_is_published(self):
        """Post is Published"""
        self.post.publish()
        post = Post.objects.get(title=self.title)
        self.assertNotEqual(post.published_date, None)

    def test_comment_approve(self):
        """Comment is created"""     
        self.comment.approve()
        self.assertEqual(self.comment.approved_comment, True)
