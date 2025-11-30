import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_sign_usage_response import GetSignUsageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: float,
    *,
    from_: datetime.datetime,
    to: datetime.datetime,
    api_key_id: float | Unset = UNSET,
    page: float | Unset = 0.0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params["api_key_id"] = api_key_id

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/usage/sign_usage",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetSignUsageResponse | None:
    if response.status_code == 200:
        response_200 = GetSignUsageResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSignUsageResponse]:
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
    from_: datetime.datetime,
    to: datetime.datetime,
    api_key_id: float | Unset = UNSET,
    page: float | Unset = 0.0,
) -> Response[GetSignUsageResponse]:
    """Retrieve the usage logs for a specific account

    Args:
        account_id (float):
        from_ (datetime.datetime):
        to (datetime.datetime):
        api_key_id (float | Unset):
        page (float | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSignUsageResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        from_=from_,
        to=to,
        api_key_id=api_key_id,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: float,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime,
    to: datetime.datetime,
    api_key_id: float | Unset = UNSET,
    page: float | Unset = 0.0,
) -> GetSignUsageResponse | None:
    """Retrieve the usage logs for a specific account

    Args:
        account_id (float):
        from_ (datetime.datetime):
        to (datetime.datetime):
        api_key_id (float | Unset):
        page (float | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSignUsageResponse
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        from_=from_,
        to=to,
        api_key_id=api_key_id,
        page=page,
    ).parsed


async def asyncio_detailed(
    account_id: float,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime,
    to: datetime.datetime,
    api_key_id: float | Unset = UNSET,
    page: float | Unset = 0.0,
) -> Response[GetSignUsageResponse]:
    """Retrieve the usage logs for a specific account

    Args:
        account_id (float):
        from_ (datetime.datetime):
        to (datetime.datetime):
        api_key_id (float | Unset):
        page (float | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSignUsageResponse]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        from_=from_,
        to=to,
        api_key_id=api_key_id,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: float,
    *,
    client: AuthenticatedClient,
    from_: datetime.datetime,
    to: datetime.datetime,
    api_key_id: float | Unset = UNSET,
    page: float | Unset = 0.0,
) -> GetSignUsageResponse | None:
    """Retrieve the usage logs for a specific account

    Args:
        account_id (float):
        from_ (datetime.datetime):
        to (datetime.datetime):
        api_key_id (float | Unset):
        page (float | Unset):  Default: 0.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSignUsageResponse
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            from_=from_,
            to=to,
            api_key_id=api_key_id,
            page=page,
        )
    ).parsed
