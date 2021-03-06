# Kubernetes + Django + Nginx + uWSGI
An overly engineered website to demonstrate a basic usage of a Django app deployed on DigitalOceans Kubernetes cluster, which was provisioned by Terraform as IaC. You can read more on my (again, very basic) Terraform [design here](https://github.com/benji011/digitalocean-terraform-k8s-cluster).

<img src="https://github.com/benji011/An-overly-engineered-website/blob/main/app/static/img/infra.png" alt="My tiny infrastructure">

# Preview
https://benji011.github.io/k8s-django-nginx-uWSGI-preview/

# Usage

### 1. Create .env file from template

```bash
cp -p .env.template .env
```

### 2. Create your own secrets in .env file

```bash
DEBUG=<your_value_here>
SECRET_KEY=<your_secret_key_here>
ALLOWED_HOSTS=<your_allowed_hosts_value_here>
```

### 2. Generate secrets.yml from .env file

```bash
kubectl create secret generic prod-secrets --from-env-file=.env
```

### 3. Apply development.yml

```bash
kubectl apply -f kubernetes/deployments/deployment.yml
```

### 4. Apply service.yml

```bash
kubectl apply -f kubernetes/services/service.yml
```

### 5. Access the app (locally)
Open app on [http://localhost](http://localhost)

## TODO:
1. Create Ingress service to map external IP to DNS
2. Provision IaC using Terraform
