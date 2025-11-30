from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_aggregate_usage_period import RetrieveAggregateUsagePeriod
from ...models.retrieve_aggregate_usage_response import RetrieveAggregateUsageResponse
from ...types import UNSET, Response


def _get_kwargs(
    account_id: float,
    *,
    period: RetrieveAggregateUsagePeriod,
    value: float,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_period = period.value
    params["period"] = json_period

    params["value"] = value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/usage/sign_usage/aggregate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrieveAggregateUsageResponse | None:
    if response.status_code == 200:
        response_200 = RetrieveAggregateUsageResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrieveAggregateUsageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
    period: RetrieveAggregateUsagePeriod,
    value: float,
) -> Response[RetrieveAggregateUsageResponse]:
    """Retrieve the usage logs for a specific account

    Args:
        account_id (float):
        period (RetrieveAggregateUsagePeriod):
        value (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveAggregateUsageResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        period=period,
        value=value,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    *,
    client: AuthenticatedClient,
    period: RetrieveAggregateUsagePeriod,
    value: float,
) -> RetrieveAggregateUsageResponse | None:
    """Retrieve the usage logs for a specific account

    Args:
        account_id (float):
        period (RetrieveAggregateUsagePeriod):
        value (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveAggregateUsageResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        period=period,
        value=value,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
    period: RetrieveAggregateUsagePeriod,
    value: float,
) -> Response[RetrieveAggregateUsageResponse]:
    """Retrieve the usage logs for a specific account

    Args:
        account_id (float):
        period (RetrieveAggregateUsagePeriod):
        value (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveAggregateUsageResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        period=period,
        value=value,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    *,
    client: AuthenticatedClient,
    period: RetrieveAggregateUsagePeriod,
    value: float,
) -> RetrieveAggregateUsageResponse | None:
    """Retrieve the usage logs for a specific account

    Args:
        account_id (float):
        period (RetrieveAggregateUsagePeriod):
        value (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveAggregateUsageResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            period=period,
            value=value,
        )
    ).parsed
