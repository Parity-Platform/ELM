# ELM
Edge Load Management (ICOS)

![ELM-ICOS Architecture](elm-architecture.png "ELM-ICOS Architecture")


## Testing with multiple clusters

Create controller cluster
kind create cluster --config controller-cluster.yaml -n icos-cluster-1

Create agent cluster  
```bash
kind create cluster --config agent-cluster.yaml -n icos-cluster-2
```
Verify clusters
```bash
kind get clusters
```

use a cluster (e.g. to deploy helm charts)
```bash
kubectl cluster-info --context kind-icos-cluster-2
```