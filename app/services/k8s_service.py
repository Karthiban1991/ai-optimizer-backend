from kubernetes import client, config

class K8sService:

    def __init__(self):
        try:
            config.load_incluster_config()
        except:
            config.load_kube_config()

        self.v1 = client.CoreV1Api()

    def list_pods(self):
        pods = self.v1.list_pod_for_all_namespaces()
        return [
            {
                "name": p.metadata.name,
                "namespace": p.metadata.namespace
            }
            for p in pods.items
        ]
