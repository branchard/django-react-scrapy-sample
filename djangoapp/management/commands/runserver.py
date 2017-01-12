from django.contrib.staticfiles.management.commands.runserver import Command as StaticfilesRunserverCommand
from django.conf import settings
import os
import subprocess

class Command(StaticfilesRunserverCommand):
    help = "Starts a lightweight Web server for development, serves static files and does some custom fancy stuff."

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

    def get_handler(self, *args, **options):
        """
        My fancy stuff function.
        """
        handler = super(Command, self).get_handler(*args, **options)

        # Custom script
        print("Webpack initialization ...")
        self.project_path = settings.BASE_DIR
        self.stdout.write("Starting the Webpack watch command from {0}\n".format(self.project_path))
        self.command = "{0}/node_modules/.bin/webpack --config {0}/webpack.config.js --watch".format(self.project_path)
        self.stdout.write("Executed command: {0}".format(self.command))
        self.process_pid = subprocess.Popen([self.command],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=self.stdout,
            stderr=self.stderr)
        self.stdout.write("Webpack watch process: %r\n" % self.process_pid.pid)

        print("done.")

        return handler
