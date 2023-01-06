from locust import HttpUser, task,constant

url='/api/matrix'

class HelloWorldUser(HttpUser):
    #wait_time = constant(1)
    @task
    def ilk_task(self):
        #self.client.get(url="/mul")
        self.client.post(url=url, files={'matrix_file':open('1matrix.txt','rb'),'n':'{"n":3}'})