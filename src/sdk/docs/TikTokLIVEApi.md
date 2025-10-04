# TikTokLIVEApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**fetchWebcastURL**](#fetchwebcasturl) | **GET** /webcast/fetch | |
|[**getRateLimits**](#getratelimits) | **GET** /webcast/rate_limits | |
|[**retrieveRoomCover**](#retrieveroomcover) | **GET** /webcast/room_cover | |
|[**retrieveRoomId**](#retrieveroomid) | **GET** /webcast/room_id | |
|[**retrieveRoomInfo**](#retrieveroominfo) | **GET** /webcast/room_info | |
|[**retrieveRoomVideo**](#retrieveroomvideo) | **GET** /webcast/room_video | |
|[**sendRoomChat**](#sendroomchat) | **POST** /webcast/chat | |
|[**signWebcastUrl**](#signwebcasturl) | **POST** /webcast/sign_url | |

# **fetchWebcastURL**
> object fetchWebcastURL()

Fetch the WebSocket URL & first payload for a TikTok LIVE Room given a Room ID.

### Example

```typescript
import {
    TikTokLIVEApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TikTokLIVEApi(configuration);

let client: string; //The client library identifier. Used for metrics. (optional) (default to 'ttlive-other')
let roomId: string; //The room ID to fetch the Webcast URL for. (optional) (default to undefined)
let uniqueId: string; //The unique ID of the TikTok user. Send this instead of a Room ID, if you\'re an Enterprise user. (optional) (default to undefined)
let cursor: string; //Starting cursor for the webcast connection, if any (optional) (default to undefined)
let sessionId: string; //Cookie - The account session ID from TikTok web (optional) (default to undefined)
let userAgent: string; //Override the user agent used for signing and fetching (optional) (default to undefined)
let ttTargetIdc: string; //Cookie - TikTok \"Identity Data Center\" which links a session_id to a region (optional) (default to undefined)
let clientEnter: boolean; //Whether the client enters a room after connecting, or if it\'s done by query parameters (optional) (default to true)
let country: ProxyRegion; //Country code to make the request from. (optional) (default to undefined)
let platform: WebcastFetchPlatform; //Platform to connect with (optional) (default to undefined)

const { status, data } = await apiInstance.fetchWebcastURL(
    client,
    roomId,
    uniqueId,
    cursor,
    sessionId,
    userAgent,
    ttTargetIdc,
    clientEnter,
    country,
    platform
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client** | [**string**] | The client library identifier. Used for metrics. | (optional) defaults to 'ttlive-other'|
| **roomId** | [**string**] | The room ID to fetch the Webcast URL for. | (optional) defaults to undefined|
| **uniqueId** | [**string**] | The unique ID of the TikTok user. Send this instead of a Room ID, if you\&#39;re an Enterprise user. | (optional) defaults to undefined|
| **cursor** | [**string**] | Starting cursor for the webcast connection, if any | (optional) defaults to undefined|
| **sessionId** | [**string**] | Cookie - The account session ID from TikTok web | (optional) defaults to undefined|
| **userAgent** | [**string**] | Override the user agent used for signing and fetching | (optional) defaults to undefined|
| **ttTargetIdc** | [**string**] | Cookie - TikTok \&quot;Identity Data Center\&quot; which links a session_id to a region | (optional) defaults to undefined|
| **clientEnter** | [**boolean**] | Whether the client enters a room after connecting, or if it\&#39;s done by query parameters | (optional) defaults to true|
| **country** | **ProxyRegion** | Country code to make the request from. | (optional) defaults to undefined|
| **platform** | **WebcastFetchPlatform** | Platform to connect with | (optional) defaults to undefined|


### Return type

**object**

### Authorization

[api_key_query](../README.md#api_key_query), [jwt_key_header](../README.md#jwt_key_header), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getRateLimits**
> GetRateLimits getRateLimits()

Retrieve the rate limits for the provided API key (or the unauthenticated limits if no key is provided)

### Example

```typescript
import {
    TikTokLIVEApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TikTokLIVEApi(configuration);

const { status, data } = await apiInstance.getRateLimits();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**GetRateLimits**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieveRoomCover**
> JSONResponse retrieveRoomCover()

Fetch TikTok LIVE Stream Cover URL given a uniqueId.

### Example

```typescript
import {
    TikTokLIVEApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TikTokLIVEApi(configuration);

let uniqueId: string; //The unique ID of the TikTok to fetch the cover for. (default to undefined)

const { status, data } = await apiInstance.retrieveRoomCover(
    uniqueId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uniqueId** | [**string**] | The unique ID of the TikTok to fetch the cover for. | defaults to undefined|


### Return type

**JSONResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [jwt_key_header](../README.md#jwt_key_header), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieveRoomId**
> WebcastRoomIdRouteResponse retrieveRoomId()

Fetch Room ID for a given uniqueId & whether that user is live.

### Example

```typescript
import {
    TikTokLIVEApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TikTokLIVEApi(configuration);

let uniqueId: string; //The unique ID of the TikTok user to fetch the data for. (default to undefined)

const { status, data } = await apiInstance.retrieveRoomId(
    uniqueId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uniqueId** | [**string**] | The unique ID of the TikTok user to fetch the data for. | defaults to undefined|


### Return type

**WebcastRoomIdRouteResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [jwt_key_header](../README.md#jwt_key_header), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieveRoomInfo**
> WebcastRoomInfoRouteResponse retrieveRoomInfo()

Retrieve TikTok Live Room Information

### Example

```typescript
import {
    TikTokLIVEApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TikTokLIVEApi(configuration);

let uniqueId: string; //The unique identifier for the TikTok user or room (default to undefined)

const { status, data } = await apiInstance.retrieveRoomInfo(
    uniqueId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uniqueId** | [**string**] | The unique identifier for the TikTok user or room | defaults to undefined|


### Return type

**WebcastRoomInfoRouteResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieveRoomVideo**
> JSONResponse retrieveRoomVideo()

Fetch TikTok LIVE Stream video given a uniqueId.

### Example

```typescript
import {
    TikTokLIVEApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TikTokLIVEApi(configuration);

let uniqueId: string; //The unique ID of the TikTok to fetch the data for. (default to undefined)
let streamType: StreamType; //The type of video stream to fetch. Default is HLS_SD. (optional) (default to undefined)

const { status, data } = await apiInstance.retrieveRoomVideo(
    uniqueId,
    streamType
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uniqueId** | [**string**] | The unique ID of the TikTok to fetch the data for. | defaults to undefined|
| **streamType** | **StreamType** | The type of video stream to fetch. Default is HLS_SD. | (optional) defaults to undefined|


### Return type

**JSONResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [jwt_key_header](../README.md#jwt_key_header), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sendRoomChat**
> WebcastRoomChatRouteResponse sendRoomChat(webcastRoomChatPayload)

Send a chat to a TikTok LIVE room.

### Example

```typescript
import {
    TikTokLIVEApi,
    Configuration,
    WebcastRoomChatPayload
} from './api';

const configuration = new Configuration();
const apiInstance = new TikTokLIVEApi(configuration);

let webcastRoomChatPayload: WebcastRoomChatPayload; //The payload configuration for sending a chat

const { status, data } = await apiInstance.sendRoomChat(
    webcastRoomChatPayload
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **webcastRoomChatPayload** | **WebcastRoomChatPayload**| The payload configuration for sending a chat | |


### Return type

**WebcastRoomChatRouteResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signWebcastUrl**
> SignWebcastUrl200Response signWebcastUrl(signTikTokUrlBody)


### Example

```typescript
import {
    TikTokLIVEApi,
    Configuration,
    SignTikTokUrlBody
} from './api';

const configuration = new Configuration();
const apiInstance = new TikTokLIVEApi(configuration);

let signTikTokUrlBody: SignTikTokUrlBody; //
let client: string; // (optional) (default to 'ttlive-other')

const { status, data } = await apiInstance.signWebcastUrl(
    signTikTokUrlBody,
    client
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **signTikTokUrlBody** | **SignTikTokUrlBody**|  | |
| **client** | [**string**] |  | (optional) defaults to 'ttlive-other'|


### Return type

**SignWebcastUrl200Response**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

