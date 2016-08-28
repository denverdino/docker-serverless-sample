import docker

class Client(docker.Client):
    def __init__(self, *args, **kwargs):
        super(AliyunContainerServiceClient, self).__init__(*args, **kwargs)

    def projects(self, q=None, services=True, containers=True):
        u = self._url('/projects/')
        params = {
            'q': q,
            'services': services,
            'containers': containers
        }
        res = self._result(self._get(u, params=params), True)
        return res

    def inspect_project(self, project):
        return self._result(
            self._get(self._url("/projects/{0}", project)), True
        )

    def create_project(self, name, description='', version='1.0', template='', environment=None):
        data = {
            'name': name,
            'description': description,
            'version': version,
            'template': template,
            'environment': environment
        }
        u = self._url('/projects/')
        res = self._post_json(u, data=data)
        return res

