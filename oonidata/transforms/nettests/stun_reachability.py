from typing import List, Tuple

from oonidata.models.nettests import StunReachability
from oonidata.models.observations import WebObservation
from oonidata.transforms.nettests.measurement_transformer import MeasurementTransformer


class StunReachabilityTransformer(MeasurementTransformer):
    def make_observations(self, msmt: StunReachability) -> Tuple[List[WebObservation]]:
        dns_observations = self.make_dns_observations(msmt.test_keys.queries)
        http_observations = self.make_http_observations(msmt.test_keys.requests)

        return (
            self.consume_web_observations(
                dns_observations=dns_observations,
                http_observations=http_observations,
            ),
        )
