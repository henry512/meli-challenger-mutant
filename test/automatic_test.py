from locust import HttpUser, task


class WebsiteUser(HttpUser):
    @task
    def mutant(self):
        self.client.post("/mutant", json={
            "dna": ["CCCCTA", "ACAGGC", "CAAGCA", "CAAAAA", "CCTCTT", "AACTTG"]
        })
        
    @task
    def stats(self):
        self.client.get("/stats")
