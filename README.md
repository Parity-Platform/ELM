# ELM
Edge Load Management (ICOS)

![ELM-ICOS Architecture](elm-architecture.png "ELM-ICOS Architecture")


## Testing with multiple clusters

Create controller cluster
kind create cluster --config controller-cluster.yaml -n icos-cluster-1

Create agent cluster  
kind create cluster --config agent-cluster.yaml -n icos-cluster-2

Verify clusters
kind get clusters