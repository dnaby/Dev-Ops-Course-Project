# DevOps Course Project

## Run APP

Clone the repository and move to the directory containing the `docker-compose.yaml` file inside your commande line and execute the following command to run the app.

```bash
docker-compose up -d
```

## Images

- [PGAdmin 4 web interface for postgresql database management](http://localhost:8888/browser/)

![pgAdmin 4](./images/pgadmin.png)

- [First Endpoint - Get infomation about all users in the database](http://127.0.0.1:8000/get_users/)

![pgAdmin 4](./images/get_users.png)

- [Second Endpoint - Count the numbers of visits on the endpoint](http://127.0.0.1:8000/count_visits//)

![pgAdmin 4](./images/count_visits.png)

## Kubernetes

To deploy the app locally, here are the steps.

```bash
cd kubernetes/
kubectl apply -f secret.yml
kubectl apply -f postgres.yml
kubectl apply -f django.yml
minikube service @service_name-here
```

- Services

![Services](./images/services.png)

- Pods

![Pods](./images/pods.png)

- Deployed APP

![Deployed](./images/deployed.png)

Note: We try to change the app url to a domain name using ingress but unfornately it was not succeful.
