# -*- coding: utf-8 -*-
import sys
import logging
import time
import json

from pytaskmanager.node.FlaskIO import ClientBaseProtocol

class Client(ClientBaseProtocol):
    """A client for the Vantage6 infrastructure."""

    def __init__(self, host: str, port: int, path: str='/api'):
        """Create a new instance."""
        super().__init__(host, port, path)
        self.__image = None
        self.__task_name = ''
        self.__collaboration_id = None

    def set_collaboration_id(self, collaboration_id):
        """Set the collaboration_id for future calls to `call()`."""
        self.__collaboration_id = collaboration_id

    def set_task_image(self, image, name=''):
        """Set the active task image for subsequent calls to call()."""
        self.__image = image
        self.__task_name = name

    def call(self, method, *args, **kwargs):
        """Call a method on a docker image."""
        if self.__collaboration_id is None:
            print('Please call set_collaboration_id() first!')

        input_ = {
            'method': method,
            'args': args,
            'kwargs': kwargs,
        }

        task = self.post_task(
            name=self.__task_name,
            image=self.__image,
            input_=input_,
            collaboration_id=self.__collaboration_id
        )

        result = self.wait_for_results(task)
        return result

    def wait_for_results(self, task):
        print("Waiting for results ...")

        while True:
            # Refresh the task ...
            task = self.request(f"/task/{task['id']}")

            if task['complete']:
                break

            # Wait a second ...
            print(" ... waiting")
            time.sleep(1)

        # If we're here, the task has completed
        task = self.request(f"/task/{task['id']}?include=results")
        return task


