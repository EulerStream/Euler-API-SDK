from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.oxy_labs_proxy_region import OxyLabsProxyRegion
from ...models.retrieve_webcast_rankings_rank_type import RetrieveWebcastRankingsRankType
from ...models.webcast_region_rankings_response import WebcastRegionRankingsResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    region: OxyLabsProxyRegion,
    session_id: str,
    tt_target_idc: str,
    rank_type: RetrieveWebcastRankingsRankType,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_region = region.value
    params["region"] = json_region

    params["session_id"] = session_id

    params["tt_target_idc"] = tt_target_idc

    json_rank_type = rank_type.value
    params["rank_type"] = json_rank_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/rankings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WebcastRegionRankingsResponse | None:
    if response.status_code == 200:
        response_200 = WebcastRegionRankingsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WebcastRegionRankingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    region: OxyLabsProxyRegion,
    session_id: str,
    tt_target_idc: str,
    rank_type: RetrieveWebcastRankingsRankType,
) -> Response[WebcastRegionRankingsResponse]:
    """Premium Route - Retrieve TikTok LIVE rankings for a specific region.

    Args:
        region (OxyLabsProxyRegion):
        session_id (str):
        tt_target_idc (str):
        rank_type (RetrieveWebcastRankingsRankType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebcastRegionRankingsResponse]
    """

    kwargs = _get_kwargs(
        region=region,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        rank_type=rank_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    region: OxyLabsProxyRegion,
    session_id: str,
    tt_target_idc: str,
    rank_type: RetrieveWebcastRankingsRankType,
) -> WebcastRegionRankingsResponse | None:
    """Premium Route - Retrieve TikTok LIVE rankings for a specific region.

    Args:
        region (OxyLabsProxyRegion):
        session_id (str):
        tt_target_idc (str):
        rank_type (RetrieveWebcastRankingsRankType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebcastRegionRankingsResponse
    """

    return sync_detailed(
        client=client,
        region=region,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        rank_type=rank_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    region: OxyLabsProxyRegion,
    session_id: str,
    tt_target_idc: str,
    rank_type: RetrieveWebcastRankingsRankType,
) -> Response[WebcastRegionRankingsResponse]:
    """Premium Route - Retrieve TikTok LIVE rankings for a specific region.

    Args:
        region (OxyLabsProxyRegion):
        session_id (str):
        tt_target_idc (str):
        rank_type (RetrieveWebcastRankingsRankType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebcastRegionRankingsResponse]
    """

    kwargs = _get_kwargs(
        region=region,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        rank_type=rank_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    region: OxyLabsProxyRegion,
    session_id: str,
    tt_target_idc: str,
    rank_type: RetrieveWebcastRankingsRankType,
) -> WebcastRegionRankingsResponse | None:
    """Premium Route - Retrieve TikTok LIVE rankings for a specific region.

    Args:
        region (OxyLabsProxyRegion):
        session_id (str):
        tt_target_idc (str):
        rank_type (RetrieveWebcastRankingsRankType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebcastRegionRankingsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            region=region,
            session_id=session_id,
            tt_target_idc=tt_target_idc,
            rank_type=rank_type,
        )
    ).parsed
