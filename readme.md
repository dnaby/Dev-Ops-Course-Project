# DevOps Course Project

## Run APP

Clone the repository and move to the directory containing the `docker-compose.yaml` file inside your commande line and execute the following command to run the app.

```bash
docker-compose -f docker-compose.yml up -d
```

The compose.yml file is an old version of our docker-compose in which we can have access have to the PGAdmin interface.

But in the new version(`docker-compose.yml`), we removed the PGAdmin container.

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
minikube service django-service
```

- Deployed APP

![Deployed](./images/deployed.png)

- Services

![Services](./images/services.png)

- Pods

![Pods](./images/pods.png)

- StatefulSet

![StatefulSet](./images/statefulsets.png)

- ReplicaSets

![ReplicaSets](./images/replicasets.png)

- Config & Storage

![Config & Storage](./images/config_storage.png)

## Authors

Job done by `Mouhamadou Naby DIA`, `Abdoulkhadre DIALLO`, `Nassr Eddine El HIMEUR` & `Serigne Saliou WADE`.
