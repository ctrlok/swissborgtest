# What is it
`web.py` - simple python web service

Features:

- /will​ returning “Hello World” in a JSON format
- /ready​ returning “It works!” in a JSON format

# How to build
You need [docker](https://docs.docker.com/docker-for-mac/) installed

```shell script
docker build . -t ctrlok/swissapp:0.0.1
```

# How to deploy

You need to [install helm](https://helm.sh/docs/intro/install/)

Then run

```shell script
helm install ./web-helm/  --generate-name
```

While we didn't have any ingress, you can access your service by port-forwarding:

```shell script
  # Find your pod
  kubectl get pods
  # Replace $POD_NAME with your POD Name
  kubectl --namespace default port-forward $POD_NAME 8080:8080
  # Create request
  curl localhost:8080/ready
```
  
  
  
