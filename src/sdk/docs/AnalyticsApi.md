# AnalyticsApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**fetchAgents**](#fetchagents) | **GET** /analytics/agents | |
|[**getHosts**](#gethosts) | **GET** /analytics/hosts | |
|[**pips**](#pips) | **GET** /analytics/pips/{statName} | |

# **fetchAgents**
> IRetrieveAgentHostsResponse fetchAgents()

Retrieve the currently connected agents

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

const { status, data } = await apiInstance.fetchAgents();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**IRetrieveAgentHostsResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | All registered agents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getHosts**
> IHostsResponse getHosts()

Retrieve the list of API hosts (used for horizontal scaling)

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

const { status, data } = await apiInstance.getHosts();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**IHostsResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pips**
> Pips200Response pips()

Retrieve stats as an SVG

### Example

```typescript
import {
    AnalyticsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AnalyticsApi(configuration);

let statName: LogRequestMethod; //Name of the stat to retrieve (default to undefined)
let labelColour: string; //Specify label colour in SVG (optional) (default to '#555')
let valueColour: string; //Specify value colour in SVG (optional) (default to '#007ec6')
let hours: number; //The number of hours to retrieve the stat for (optional) (default to 1)
let client: LiveClient; //The client to filter for (optional) (default to undefined)
let json: boolean; //Add the ability to retrieve the pip as JSON (optional) (default to false)

const { status, data } = await apiInstance.pips(
    statName,
    labelColour,
    valueColour,
    hours,
    client,
    json
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **statName** | **LogRequestMethod** | Name of the stat to retrieve | defaults to undefined|
| **labelColour** | [**string**] | Specify label colour in SVG | (optional) defaults to '#555'|
| **valueColour** | [**string**] | Specify value colour in SVG | (optional) defaults to '#007ec6'|
| **hours** | [**number**] | The number of hours to retrieve the stat for | (optional) defaults to 1|
| **client** | **LiveClient** | The client to filter for | (optional) defaults to undefined|
| **json** | [**boolean**] | Add the ability to retrieve the pip as JSON | (optional) defaults to false|


### Return type

**Pips200Response**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

