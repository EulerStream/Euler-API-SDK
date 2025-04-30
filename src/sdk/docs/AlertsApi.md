# AlertsApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createAlert**](#createalert) | **PUT** /accounts/{account_id}/alerts/create | |
|[**listAlerts**](#listalerts) | **GET** /accounts/{account_id}/alerts/list | |
|[**retrieveAlert**](#retrievealert) | **GET** /accounts/{account_id}/alerts/{alert_id}/retrieve | |

# **createAlert**
> ICreateAlertResponse createAlert(iAlertConfigBase)

Create a creator alert. These alerts are used to notify users of a new livestream.

### Example

```typescript
import {
    AlertsApi,
    Configuration,
    IAlertConfigBase
} from './api';

const configuration = new Configuration();
const apiInstance = new AlertsApi(configuration);

let accountId: number; //The ID of the account to create the alert for (default to undefined)
let iAlertConfigBase: IAlertConfigBase; //Configuration for the alert

const { status, data } = await apiInstance.createAlert(
    accountId,
    iAlertConfigBase
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **iAlertConfigBase** | **IAlertConfigBase**| Configuration for the alert | |
| **accountId** | [**number**] | The ID of the account to create the alert for | defaults to undefined|


### Return type

**ICreateAlertResponse**

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

# **listAlerts**
> IListAlertsResponse listAlerts()


### Example

```typescript
import {
    AlertsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AlertsApi(configuration);

let accountId: number; // (default to undefined)

const { status, data } = await apiInstance.listAlerts(
    accountId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] |  | defaults to undefined|


### Return type

**IListAlertsResponse**

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
> IRetrieveAlertResponse retrieveAlert()

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

**IRetrieveAlertResponse**

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

