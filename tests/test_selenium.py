import unittest
import threading

from flask import create_app, db
from selenium import webdriver

from app.models import Role, User, Post


class SeleniumTestCase(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        # Start FireFox
        try:
            cls.client = webdriver.FireFox()
        except:
            pass

        # Skip these tests if the browser could not be started
        if cls.client:
            # Create the application
            cls.app = create_app("testing")
            cls.app_context = cls.app.app_context()
            cls.app_context.push()

            # Suppress logging to keep unittest output clean
            import logging
            logger = logging.getLogger("werkzeug")
            logger.setLevel("ERROR")

            # Create the database and populate with some fake data
            db.create_all()
            Role.insert_roles()
            User.generate_fake(10)
            Post.generate_fake(10)

            # Add an administrator user
            admin_role = Role.query.filter_by(permissions=0xff).first()
            admin = User(email="john@example.com",
                         username="john", password="cat",
                         role=admin_role, confirmed=True)
            db.session.add(admin)
            db.session.commit()

            # Start the flask server in a thread
            threading.Thread(target=cls.app_run).start()

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            # Stop the flask server and the browser
            cls.client.get("http://localhost:5000/shutdown")
            cls.client.close()

            # Destroy the database
            db.drop_all()
            db.session.remove()

            # Remove application context
            cls.app_context.pop()

    def setUp(self):
        if not self.client:
            self.skipTest("Web browser not available")

    def teardown(self):
        pass
