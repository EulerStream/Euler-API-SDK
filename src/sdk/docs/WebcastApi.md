# WebcastApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**fetchWebcastURL**](#fetchwebcasturl) | **GET** /webcast/fetch | |
|[**getRateLimits**](#getratelimits) | **GET** /webcast/rate_limits | |
|[**retrieveRoomId**](#retrieveroomid) | **GET** /webcast/room_id | |
|[**retrieveRoomInfo**](#retrieveroominfo) | **GET** /webcast/room_info | |
|[**sendRoomChat**](#sendroomchat) | **POST** /webcast/chat | |
|[**signWebcastUrl**](#signwebcasturl) | **POST** /webcast/sign_url | |

# **fetchWebcastURL**
> fetchWebcastURL()

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
let preferredAgentIds: string; //The preferred agent ID (optional) (default to undefined)

const { status, data } = await apiInstance.fetchWebcastURL(
    client,
    roomId,
    uniqueId,
    cursor,
    sessionId,
    userAgent,
    preferredAgentIds
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
| **preferredAgentIds** | [**string**] | The preferred agent ID | (optional) defaults to undefined|


### Return type

void (empty response body)

### Authorization

[api_key_query](../README.md#api_key_query), [jwt_key_header](../README.md#jwt_key_header), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No content |  -  |

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

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

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

Fetch Room Info for a given uniqueId. This is a premium endpoint that bypasses TikTok captchas. It is counted towards your request quota.

### Example

```typescript
import {
    WebcastApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new WebcastApi(configuration);

let uniqueId: string; //The unique ID of the TikTok user to fetch data for (default to undefined)

const { status, data } = await apiInstance.retrieveRoomInfo(
    uniqueId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **uniqueId** | [**string**] | The unique ID of the TikTok user to fetch data for | defaults to undefined|


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

# **sendRoomChat**
> IWebcastRoomChatRouteResponse sendRoomChat(iWebcastRoomChatPayload)

Fetch Room Info for a given uniqueId. This is a premium endpoint that bypasses TikTok captchas. It is counted towards your request quota.

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
let preferredAgentId: string; // (optional) (default to undefined)

const { status, data } = await apiInstance.signWebcastUrl(
    iSignTikTokUrlBody,
    preferredAgentId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **iSignTikTokUrlBody** | **ISignTikTokUrlBody**|  | |
| **preferredAgentId** | [**string**] |  | (optional) defaults to undefined|


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

