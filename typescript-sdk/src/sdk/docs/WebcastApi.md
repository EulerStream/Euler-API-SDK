# WebcastApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**fetchWebcastURL**](#fetchwebcasturl) | **GET** /webcast/fetch | |
|[**getConnectedWebSockets**](#getconnectedwebsockets) | **GET** /webcast/websockets | |
|[**getRateLimits**](#getratelimits) | **GET** /webcast/rate_limits | |
|[**retrieveRoomCover**](#retrieveroomcover) | **GET** /webcast/room_cover | |
|[**retrieveRoomId**](#retrieveroomid) | **GET** /webcast/room_id | |
|[**retrieveRoomInfo**](#retrieveroominfo) | **GET** /webcast/room_info | |
|[**retrieveRoomVideo**](#retrieveroomvideo) | **GET** /webcast/room_video | |
|[**sendRoomChat**](#sendroomchat) | **POST** /webcast/chat | |
|[**signWebcastUrl**](#signwebcasturl) | **POST** /webcast/sign_url | |

# **fetchWebcastURL**
> object fetchWebcastURL()

Fetch the WebSocket URL & first payload for a TikTok LIVE Room given a Room Id.

### Example

```typescript
import {
    WebcastApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new WebcastApi(configuration);

let client: string; //The client ID (default to undefined)
let roomId: string; //The room ID to fetch the webcast URL for (optional) (default to undefined)
let uniqueId: string; //The unique ID of the TikTok user. Only available to Enterprise users. (optional) (default to undefined)
let cursor: string; //The cursor to fetch the webcast URL for (optional) (default to undefined)
let sessionId: string; //The session ID used to fetch a privileged WS connection (optional) (default to undefined)
let userAgent: string; //Override the user agent used in the signature (optional) (default to undefined)
let ttTargetIdc: string; //The target IDC to use for the request (optional) (default to undefined)
let clientEnter: boolean; //Whether the client is entering the room (optional) (default to undefined)

const { status, data } = await apiInstance.fetchWebcastURL(
    client,
    roomId,
    uniqueId,
    cursor,
    sessionId,
    userAgent,
    ttTargetIdc,
    clientEnter
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client** | [**string**] | The client ID | defaults to undefined|
| **roomId** | [**string**] | The room ID to fetch the webcast URL for | (optional) defaults to undefined|
| **uniqueId** | [**string**] | The unique ID of the TikTok user. Only available to Enterprise users. | (optional) defaults to undefined|
| **cursor** | [**string**] | The cursor to fetch the webcast URL for | (optional) defaults to undefined|
| **sessionId** | [**string**] | The session ID used to fetch a privileged WS connection | (optional) defaults to undefined|
| **userAgent** | [**string**] | Override the user agent used in the signature | (optional) defaults to undefined|
| **ttTargetIdc** | [**string**] | The target IDC to use for the request | (optional) defaults to undefined|
| **clientEnter** | [**boolean**] | Whether the client is entering the room | (optional) defaults to undefined|


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

# **getConnectedWebSockets**
> IRetrievedCloudWebSocketsRouteResponse getConnectedWebSockets()

Retrieve the currently connected WebSocket clients for your account. Only for paid plans.

### Example

```typescript
import {
    WebcastApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new WebcastApi(configuration);

const { status, data } = await apiInstance.getConnectedWebSockets();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**IRetrievedCloudWebSocketsRouteResponse**

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

# **getRateLimits**
> IGetRateLimits getRateLimits()

Retrieve the rate limits for the provided API key (or the unauthenticated limits if no key is provided)

### Example

```typescript
import {
    WebcastApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new WebcastApi(configuration);

const { status, data } = await apiInstance.getRateLimits();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**IGetRateLimits**

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
> IJSONResponse retrieveRoomCover()

Fetch TikTok LIVE Stream Cover URL given a uniqueId.

### Example

```typescript
import {
    WebcastApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new WebcastApi(configuration);

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

**IJSONResponse**

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
> IWebcastRoomIdRouteResponse retrieveRoomId()

Fetch Room Id for a given uniqueId & whether that user is live.

### Example

```typescript
import {
    WebcastApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new WebcastApi(configuration);

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

**IWebcastRoomIdRouteResponse**

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
> IWebcastRoomInfoRouteResponse retrieveRoomInfo()

Retrieve TikTok Live Room Information

### Example

```typescript
import {
    WebcastApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new WebcastApi(configuration);

let uniqueId: string; //The unique identifier for the TikTok user or room (default to undefined)
let giftInfo: boolean; //Optional flag to include gift information in the response (optional) (default to false)

const { status, data } = await apiInstance.retrieveRoomInfo(
    uniqueId,
    giftInfo
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uniqueId** | [**string**] | The unique identifier for the TikTok user or room | defaults to undefined|
| **giftInfo** | [**boolean**] | Optional flag to include gift information in the response | (optional) defaults to false|


### Return type

**IWebcastRoomInfoRouteResponse**

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
> IJSONResponse retrieveRoomVideo()

Fetch TikTok LIVE Stream video given a uniqueId.

### Example

```typescript
import {
    WebcastApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new WebcastApi(configuration);

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

**IJSONResponse**

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
> IWebcastRoomChatRouteResponse sendRoomChat(iWebcastRoomChatPayload)

Send a chat to a TikTok LIVE room.

### Example

```typescript
import {
    WebcastApi,
    Configuration,
    IWebcastRoomChatPayload
} from './api';

const configuration = new Configuration();
const apiInstance = new WebcastApi(configuration);

let iWebcastRoomChatPayload: IWebcastRoomChatPayload; //The payload configuration for sending a chat

const { status, data } = await apiInstance.sendRoomChat(
    iWebcastRoomChatPayload
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **iWebcastRoomChatPayload** | **IWebcastRoomChatPayload**| The payload configuration for sending a chat | |


### Return type

**IWebcastRoomChatRouteResponse**

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
> SignWebcastUrl200Response signWebcastUrl(iSignTikTokUrlBody)


### Example

```typescript
import {
    WebcastApi,
    Configuration,
    ISignTikTokUrlBody
} from './api';

const configuration = new Configuration();
const apiInstance = new WebcastApi(configuration);

let iSignTikTokUrlBody: ISignTikTokUrlBody; //

const { status, data } = await apiInstance.signWebcastUrl(
    iSignTikTokUrlBody
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **iSignTikTokUrlBody** | **ISignTikTokUrlBody**|  | |


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

