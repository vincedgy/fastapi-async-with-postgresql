import time
from locust import HttpUser, task


class QuickstartUser(HttpUser):

    @task()
    def get_items(self):
        for x in range(100):
            self.client.get(f"/notes")

    def on_start(self):
        self.client.post(f"/notes", json={"completed": "true", "text": "bar"})
