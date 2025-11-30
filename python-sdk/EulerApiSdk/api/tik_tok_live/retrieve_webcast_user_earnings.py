from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webcast_user_earnings_output_period import WebcastUserEarningsOutputPeriod
from ...models.webcast_user_earnings_response import WebcastUserEarningsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    unique_id: str,
    session_id: str,
    tt_target_idc: str,
    period: WebcastUserEarningsOutputPeriod | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["unique_id"] = unique_id

    params["session_id"] = session_id

    params["tt_target_idc"] = tt_target_idc

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webcast/user_earnings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WebcastUserEarningsResponse | None:
    if response.status_code == 200:
        response_200 = WebcastUserEarningsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WebcastUserEarningsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    unique_id: str,
    session_id: str,
    tt_target_idc: str,
    period: WebcastUserEarningsOutputPeriod | Unset = UNSET,
) -> Response[WebcastUserEarningsResponse]:
    """Premium Route - Retrieve TikTok LIVE earnings for a specific user.

    Args:
        unique_id (str):
        session_id (str):
        tt_target_idc (str):
        period (WebcastUserEarningsOutputPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebcastUserEarningsResponse]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    unique_id: str,
    session_id: str,
    tt_target_idc: str,
    period: WebcastUserEarningsOutputPeriod | Unset = UNSET,
) -> WebcastUserEarningsResponse | None:
    """Premium Route - Retrieve TikTok LIVE earnings for a specific user.

    Args:
        unique_id (str):
        session_id (str):
        tt_target_idc (str):
        period (WebcastUserEarningsOutputPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebcastUserEarningsResponse
    """

    return sync_detailed(
        client=client,
        unique_id=unique_id,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        period=period,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    unique_id: str,
    session_id: str,
    tt_target_idc: str,
    period: WebcastUserEarningsOutputPeriod | Unset = UNSET,
) -> Response[WebcastUserEarningsResponse]:
    """Premium Route - Retrieve TikTok LIVE earnings for a specific user.

    Args:
        unique_id (str):
        session_id (str):
        tt_target_idc (str):
        period (WebcastUserEarningsOutputPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebcastUserEarningsResponse]
    """

    kwargs = _get_kwargs(
        unique_id=unique_id,
        session_id=session_id,
        tt_target_idc=tt_target_idc,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    unique_id: str,
    session_id: str,
    tt_target_idc: str,
    period: WebcastUserEarningsOutputPeriod | Unset = UNSET,
) -> WebcastUserEarningsResponse | None:
    """Premium Route - Retrieve TikTok LIVE earnings for a specific user.

    Args:
        unique_id (str):
        session_id (str):
        tt_target_idc (str):
        period (WebcastUserEarningsOutputPeriod | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebcastUserEarningsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            unique_id=unique_id,
            session_id=session_id,
            tt_target_idc=tt_target_idc,
            period=period,
        )
    ).parsed
