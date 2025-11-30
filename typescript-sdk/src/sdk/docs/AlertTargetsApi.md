# AlertTargetsApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createAlertTarget**](#createalerttarget) | **PUT** /accounts/{account_id}/alerts/{alert_id}/targets/create | |
|[**deleteAlertTarget**](#deletealerttarget) | **DELETE** /accounts/{account_id}/alerts/{alert_id}/targets/{target_id}/delete | |
|[**listAlertTargets**](#listalerttargets) | **GET** /accounts/{account_id}/alerts/{alert_id}/targets/list | |
|[**testAlertTarget**](#testalerttarget) | **POST** /accounts/{account_id}/alerts/{alert_id}/targets/{target_id}/test | |

# **createAlertTarget**
> CreateAlertTargetResponse createAlertTarget(createAlertTargetPayload)

Create a target for an alert. This is the HTTP endpoint that will be called when an alert is triggered.

### Example

```typescript
import {
    AlertTargetsApi,
    Configuration,
    CreateAlertTargetPayload
} from './api';

const configuration = new Configuration();
const apiInstance = new AlertTargetsApi(configuration);

let accountId: number; //The ID of the account to create the alert target for (default to undefined)
let alertId: number; //The ID of the alert to create the target for (default to undefined)
let createAlertTargetPayload: CreateAlertTargetPayload; //Configuration for the alert target

const { status, data } = await apiInstance.createAlertTarget(
    accountId,
    alertId,
    createAlertTargetPayload
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **createAlertTargetPayload** | **CreateAlertTargetPayload**| Configuration for the alert target | |
| **accountId** | [**number**] | The ID of the account to create the alert target for | defaults to undefined|
| **alertId** | [**number**] | The ID of the alert to create the target for | defaults to undefined|


### Return type

**CreateAlertTargetResponse**

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

# **deleteAlertTarget**
> DeleteAlertTargetResponse deleteAlertTarget()

Delete an alert target from the Sign API

### Example

```typescript
import {
    AlertTargetsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AlertTargetsApi(configuration);

let accountId: number; //The ID of the account to delete the alert target from (default to undefined)
let alertId: number; //The ID of the alert to delete the target from (default to undefined)
let targetId: number; //The ID of the target to delete (default to undefined)

const { status, data } = await apiInstance.deleteAlertTarget(
    accountId,
    alertId,
    targetId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The ID of the account to delete the alert target from | defaults to undefined|
| **alertId** | [**number**] | The ID of the alert to delete the target from | defaults to undefined|
| **targetId** | [**number**] | The ID of the target to delete | defaults to undefined|


### Return type

**DeleteAlertTargetResponse**

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

# **listAlertTargets**
> ListAlertTargetsResponse listAlertTargets()

List all alert targets for a specific alert

### Example

```typescript
import {
    AlertTargetsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AlertTargetsApi(configuration);

let accountId: number; //The account that the alert belongs to (default to undefined)
let alertId: number; //The alert to list targets for (default to undefined)

const { status, data } = await apiInstance.listAlertTargets(
    accountId,
    alertId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The account that the alert belongs to | defaults to undefined|
| **alertId** | [**number**] | The alert to list targets for | defaults to undefined|


### Return type

**ListAlertTargetsResponse**

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

# **testAlertTarget**
> TestAlertTargetResponse testAlertTarget()

Test an alert target

### Example

```typescript
import {
    AlertTargetsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AlertTargetsApi(configuration);

let accountId: number; //The account that the alert belongs to (default to undefined)
let alertId: number; //The alert that the target belongs to (default to undefined)
let targetId: number; //The target to test (default to undefined)

const { status, data } = await apiInstance.testAlertTarget(
    accountId,
    alertId,
    targetId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The account that the alert belongs to | defaults to undefined|
| **alertId** | [**number**] | The alert that the target belongs to | defaults to undefined|
| **targetId** | [**number**] | The target to test | defaults to undefined|


### Return type

**TestAlertTargetResponse**

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

