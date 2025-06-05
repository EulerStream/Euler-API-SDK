# AccountsApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**countSignUsage**](#countsignusage) | **GET** /accounts/{account_id}/usage/sign_usage/page_count | |
|[**getSignUsage**](#getsignusage) | **GET** /accounts/{account_id}/usage/sign_usage | |
|[**retrieveAggregateUsage**](#retrieveaggregateusage) | **GET** /accounts/{account_id}/usage/sign_usage/aggregate | |

# **countSignUsage**
> ICountSignUsage countSignUsage()

Retrieve the usage logs for a specific account

### Example

```typescript
import {
    AccountsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AccountsApi(configuration);

let accountId: number; //Account ID to retrieve usage logs for (default to undefined)
let from: string; //Start date for the logs (default to undefined)
let to: string; //End date for the logs (default to undefined)
let apiKeyId: number; //Optional API key ID to filter logs by (optional) (default to undefined)

const { status, data } = await apiInstance.countSignUsage(
    accountId,
    from,
    to,
    apiKeyId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | Account ID to retrieve usage logs for | defaults to undefined|
| **from** | [**string**] | Start date for the logs | defaults to undefined|
| **to** | [**string**] | End date for the logs | defaults to undefined|
| **apiKeyId** | [**number**] | Optional API key ID to filter logs by | (optional) defaults to undefined|


### Return type

**ICountSignUsage**

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

# **getSignUsage**
> IGetSignUsageResponse getSignUsage()

Retrieve the usage logs for a specific account

### Example

```typescript
import {
    AccountsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AccountsApi(configuration);

let accountId: number; //Account ID to retrieve usage logs for (default to undefined)
let from: string; //Start date for the logs (default to undefined)
let to: string; //End date for the logs (default to undefined)
let apiKeyId: number; //Optional API key ID to filter logs by (optional) (default to undefined)
let page: number; //Page number to retrieve (optional) (default to 0)

const { status, data } = await apiInstance.getSignUsage(
    accountId,
    from,
    to,
    apiKeyId,
    page
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | Account ID to retrieve usage logs for | defaults to undefined|
| **from** | [**string**] | Start date for the logs | defaults to undefined|
| **to** | [**string**] | End date for the logs | defaults to undefined|
| **apiKeyId** | [**number**] | Optional API key ID to filter logs by | (optional) defaults to undefined|
| **page** | [**number**] | Page number to retrieve | (optional) defaults to 0|


### Return type

**IGetSignUsageResponse**

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

# **retrieveAggregateUsage**
> IRetrieveAggregateUsageResponse retrieveAggregateUsage()

Retrieve the usage logs for a specific account

### Example

```typescript
import {
    AccountsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AccountsApi(configuration);

let accountId: number; //Account ID to retrieve usage logs for (default to undefined)
let period: 'hour' | 'day'; //The period for aggregate statistics to check (default to undefined)
let value: number; //The value for the period (either hours or numbers) (default to undefined)

const { status, data } = await apiInstance.retrieveAggregateUsage(
    accountId,
    period,
    value
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | Account ID to retrieve usage logs for | defaults to undefined|
| **period** | [**&#39;hour&#39; | &#39;day&#39;**]**Array<&#39;hour&#39; &#124; &#39;day&#39;>** | The period for aggregate statistics to check | defaults to undefined|
| **value** | [**number**] | The value for the period (either hours or numbers) | defaults to undefined|


### Return type

**IRetrieveAggregateUsageResponse**

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

