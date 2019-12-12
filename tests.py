import unittest
from datetime import datetime, timedelta

from app import app, db
from app.models import User, Post


class UserModelTestCase(unittest.TestCase):

    def setUp(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite://'  # use an in-memory SQLite db during the tests
        db.create_all()  # creates all the database tables

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        susan = User(username='Susan')
        susan.set_password('cat')
        self.assertTrue(susan.check_password('cat'))
        self.assertFalse(susan.check_password('dog'))

    def test_avatar(self):
        john = User(username='John', email='john@example.com')
        self.assertEqual(
            'https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?d=identicon&s=128', john.avatar(128)
        )

    def test_follow(self):
        john = User(username='john', email='john@example.com')
        susan = User(username='susan', email='susan@example.com')
        db.session.add(john)
        db.session.add(susan)
        db.session.commit()
        self.assertEqual([], john.followed.all())
        self.assertEqual([], john.followers.all())

        john.follow(susan)
        db.session.commit()
        self.assertTrue(john.is_following(susan))
        self.assertEqual(1, john.followed.count())
        self.assertEqual('susan', john.followed.first().username)
        self.assertEqual(1, susan.followers.count())
        self.assertEqual('john', susan.followers.first().username)

        john.unfollow(susan)
        db.session.commit()
        self.assertFalse(john.is_following(susan))
        self.assertEqual(0, john.followed.count())
        self.assertEqual(0, susan.followers.count())

    def test_follow_posts(self):
        # create users
        john = User(username='john', email='john@example.com')
        susan = User(username='susan', email='susan@example.com')
        mary = User(username='mary', email='mary@example.com')
        david = User(username='david', email='david@example.com')
        db.session.add_all([john, susan, mary, david])

        # create posts
        now = datetime.utcnow()
        p1 = Post(body='post from John', author=john, timestamp=now + timedelta(seconds=1))
        p2 = Post(body='post from Susan', author=susan, timestamp=now + timedelta(seconds=4))
        p3 = Post(body='post from Mary', author=mary, timestamp=now + timedelta(seconds=3))
        p4 = Post(body='post from David', author=david, timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])

        # setup the followers
        john.follow(susan)
        john.follow(david)
        susan.follow(mary)
        mary.follow(david)
        db.session.commit()

        # check the followed posts of each user
        self.assertEqual([p2, p4, p1], john.followed_posts().all())
        self.assertEqual([p2, p3], susan.followed_posts().all())
        self.assertEqual([p3, p4], mary.followed_posts().all())
        self.assertEqual([p4], david.followed_posts().all())


if __name__ == '__main__':
    unittest.main(verbosity=2)
