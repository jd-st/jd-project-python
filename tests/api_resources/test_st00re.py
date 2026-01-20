# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from jd_project import JdProject, AsyncJdProject
from tests.utils import assert_matches_type
from jd_project.types import St00reListInventoryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSt00re:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_inventory(self, client: JdProject) -> None:
        st00re = client.st00re.list_inventory()
        assert_matches_type(St00reListInventoryResponse, st00re, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_inventory(self, client: JdProject) -> None:
        response = client.st00re.with_raw_response.list_inventory()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        st00re = response.parse()
        assert_matches_type(St00reListInventoryResponse, st00re, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_inventory(self, client: JdProject) -> None:
        with client.st00re.with_streaming_response.list_inventory() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            st00re = response.parse()
            assert_matches_type(St00reListInventoryResponse, st00re, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSt00re:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_inventory(self, async_client: AsyncJdProject) -> None:
        st00re = await async_client.st00re.list_inventory()
        assert_matches_type(St00reListInventoryResponse, st00re, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_inventory(self, async_client: AsyncJdProject) -> None:
        response = await async_client.st00re.with_raw_response.list_inventory()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        st00re = await response.parse()
        assert_matches_type(St00reListInventoryResponse, st00re, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_inventory(self, async_client: AsyncJdProject) -> None:
        async with async_client.st00re.with_streaming_response.list_inventory() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            st00re = await response.parse()
            assert_matches_type(St00reListInventoryResponse, st00re, path=["response"])

        assert cast(Any, response.is_closed) is True
