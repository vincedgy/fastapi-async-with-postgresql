import time
from locust import HttpUser, task


class QuickstartUser(HttpUser):

    @task()
    def get_items(self):
        for x in range(10):
            self.client.get(f"/notes/{x+1}")

    def on_start(self):
        self.client.post(f"/notes", json={"completed": "true", "text": "bar"})
