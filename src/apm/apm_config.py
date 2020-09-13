from typing import Dict

import elasticapm
from elasticapm.contrib.flask import ElasticAPM


from singleton_decorator import singleton


@singleton
class ApmClient:

    client = None
    apm = None

    def initialize(self, elastic_apm_settings: Dict):
        self.client = elasticapm.Client(elastic_apm_settings)
        self.apm = ElasticAPM(client=self.client)







