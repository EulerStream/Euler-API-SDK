# AlertsApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createAlert**](#createalert) | **PUT** /accounts/{account_id}/alerts/create | |
|[**deleteAlert**](#deletealert) | **DELETE** /accounts/{account_id}/alerts/{alert_id}/delete | |
|[**listAlerts**](#listalerts) | **GET** /accounts/{account_id}/alerts/list | |
|[**retrieveAlert**](#retrievealert) | **GET** /accounts/{account_id}/alerts/{alert_id}/retrieve | |

# **createAlert**
> CreateAlertResponse createAlert(createAlertRequest)

Create a creator alert. These Alerts are used to notify users of a new livestream.

### Example

```typescript
import {
    AlertsApi,
    Configuration,
    CreateAlertRequest
} from './api';

const configuration = new Configuration();
const apiInstance = new AlertsApi(configuration);

let accountId: number; //The ID of the account to create the alert for (default to undefined)
let createAlertRequest: CreateAlertRequest; //Configuration for the alert

const { status, data } = await apiInstance.createAlert(
    accountId,
    createAlertRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **createAlertRequest** | **CreateAlertRequest**| Configuration for the alert | |
| **accountId** | [**number**] | The ID of the account to create the alert for | defaults to undefined|


### Return type

**CreateAlertResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [jwt_key_header](../README.md#jwt_key_header), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteAlert**
> DeleteAlertResponse deleteAlert()

Delete an alert from the Sign API

### Example

```typescript
import {
    AlertsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AlertsApi(configuration);

let accountId: number; //The ID of the account to delete the alert from (default to undefined)
let alertId: number; //The ID of the alert to delete (default to undefined)

const { status, data } = await apiInstance.deleteAlert(
    accountId,
    alertId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The ID of the account to delete the alert from | defaults to undefined|
| **alertId** | [**number**] | The ID of the alert to delete | defaults to undefined|


### Return type

**DeleteAlertResponse**

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

# **listAlerts**
> ListAlertsResponse listAlerts()


### Example

```typescript
import {
    AlertsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AlertsApi(configuration);

let accountId: number; // (default to undefined)
let page: number; // (optional) (default to 0)

const { status, data } = await apiInstance.listAlerts(
    accountId,
    page
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] |  | defaults to undefined|
| **page** | [**number**] |  | (optional) defaults to 0|


### Return type

**ListAlertsResponse**

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

# **retrieveAlert**
> RetrieveAlertResponse retrieveAlert()

Retrieve a specific alert by its ID

### Example

```typescript
import {
    AlertsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AlertsApi(configuration);

let accountId: number; //The account that the alert belongs to (default to undefined)
let alertId: number; //The ID of the alert to retrieve (default to undefined)

const { status, data } = await apiInstance.retrieveAlert(
    accountId,
    alertId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The account that the alert belongs to | defaults to undefined|
| **alertId** | [**number**] | The ID of the alert to retrieve | defaults to undefined|


### Return type

**RetrieveAlertResponse**

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

