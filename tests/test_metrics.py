# Copyright (c) 2021-present, Ethan Henderson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import pytest

from analytix import errors
from analytix.features import Metrics


@pytest.fixture()
def metrics() -> Metrics:
    return Metrics("views", "likes", "comments")


def test_metrics_repr_output(metrics):
    outputs = (
        r"Metrics(values={'views', 'likes', 'comments'})",
        r"Metrics(values={'views', 'comments', 'likes'})",
        r"Metrics(values={'likes', 'views', 'comments'})",
        r"Metrics(values={'likes', 'comments', 'views'})",
        r"Metrics(values={'comments', 'views', 'likes'})",
        r"Metrics(values={'comments', 'likes', 'views'})",
    )

    assert repr(metrics) in outputs
    assert f"{metrics!r}" in outputs


def test_metrics_hash(metrics):
    assert isinstance(hash(metrics), int)


def test_metrics_equal(metrics):
    assert metrics == Metrics("views", "likes", "comments")


def test_metrics_not_equal(metrics):
    assert metrics != Metrics("estimatedRevenue", "estimatedAdRevenue", "grossRevenue")


def test_metrics(metrics):
    metrics.validate(["views", "likes", "comments"])


def test_metrics_invalid(metrics):
    with pytest.raises(errors.InvalidMetrics) as exc:
        metrics.validate(["views", "likes", "henlo", "testing"])
    assert str(exc.value) in (
        "invalid metric(s) provided: henlo, testing",
        "invalid metric(s) provided: testing, henlo",
    )


def test_metrics_unsupported(metrics):
    with pytest.raises(errors.UnsupportedMetrics) as exc:
        metrics.validate(["views", "likes", "dislikes", "shares"])
    assert str(exc.value) in (
        "unsupported metric(s) for selected report type: dislikes, shares",
        "unsupported metric(s) for selected report type: shares, dislikes",
    )


def test_missing_metrics(metrics):
    with pytest.raises(errors.MissingMetrics) as exc:
        metrics.validate([])
    assert str(exc.value) == "expected at least 1 metric, got 0"
