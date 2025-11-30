from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_bulk_live_check_payload import RetrieveBulkLiveCheckPayload
from ...models.retrieve_bulk_live_check_response import RetrieveBulkLiveCheckResponse
from ...types import Response


def _get_kwargs(
    *,
    body: RetrieveBulkLiveCheckPayload,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webcast/bulk_live_check",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrieveBulkLiveCheckResponse | None:
    if response.status_code == 200:
        response_200 = RetrieveBulkLiveCheckResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrieveBulkLiveCheckResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RetrieveBulkLiveCheckPayload,
) -> Response[RetrieveBulkLiveCheckResponse]:
    """Premium Route - A bulk-check endpoint to determine if a group of TikTok users (up to 50 at once) are
    live.
    It uses a highly optimized job-based system for checking large numbers of users quickly.

    Args:
        body (RetrieveBulkLiveCheckPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBulkLiveCheckResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RetrieveBulkLiveCheckPayload,
) -> RetrieveBulkLiveCheckResponse | None:
    """Premium Route - A bulk-check endpoint to determine if a group of TikTok users (up to 50 at once) are
    live.
    It uses a highly optimized job-based system for checking large numbers of users quickly.

    Args:
        body (RetrieveBulkLiveCheckPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBulkLiveCheckResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RetrieveBulkLiveCheckPayload,
) -> Response[RetrieveBulkLiveCheckResponse]:
    """Premium Route - A bulk-check endpoint to determine if a group of TikTok users (up to 50 at once) are
    live.
    It uses a highly optimized job-based system for checking large numbers of users quickly.

    Args:
        body (RetrieveBulkLiveCheckPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrieveBulkLiveCheckResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RetrieveBulkLiveCheckPayload,
) -> RetrieveBulkLiveCheckResponse | None:
    """Premium Route - A bulk-check endpoint to determine if a group of TikTok users (up to 50 at once) are
    live.
    It uses a highly optimized job-based system for checking large numbers of users quickly.

    Args:
        body (RetrieveBulkLiveCheckPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrieveBulkLiveCheckResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
