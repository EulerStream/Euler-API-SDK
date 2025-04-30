# AuthenticationApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createJWT**](#createjwt) | **POST** /accounts/{account_id}/jwt/create | |
|[**createKey**](#createkey) | **PUT** /accounts/{account_id}/api_keys/create | |
|[**deleteKey**](#deletekey) | **DELETE** /accounts/{account_id}/api_keys/delete | |
|[**getKey**](#getkey) | **GET** /accounts/{account_id}/api_keys/retrieve | |
|[**listKeys**](#listkeys) | **GET** /accounts/{account_id}/api_keys/list | |
|[**updateKey**](#updatekey) | **PATCH** /accounts/{account_id}/api_keys/update | |

# **createJWT**
> ICreateJWTResponse createJWT(jWTCreateConfig)

Create a JWT for a given API key. Note that these JWT keys are only valid for the non-authenticated Webcast endpoints. They function to attach the rate limits of the API key to the request for client-sided applications.

### Example

```typescript
import {
    AuthenticationApi,
    Configuration,
    JWTCreateConfig
} from './api';

const configuration = new Configuration();
const apiInstance = new AuthenticationApi(configuration);

let accountId: number; //The ID of the account to create the JWT for (default to undefined)
let jWTCreateConfig: JWTCreateConfig; //The configuration for the JWT

const { status, data } = await apiInstance.createJWT(
    accountId,
    jWTCreateConfig
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **jWTCreateConfig** | **JWTCreateConfig**| The configuration for the JWT | |
| **accountId** | [**number**] | The ID of the account to create the JWT for | defaults to undefined|


### Return type

**ICreateJWTResponse**

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

# **createKey**
> ICreateKeyResponse createKey(iApiKeyConfigBase)

Create a new API key

### Example

```typescript
import {
    AuthenticationApi,
    Configuration,
    IApiKeyConfigBase
} from './api';

const configuration = new Configuration();
const apiInstance = new AuthenticationApi(configuration);

let accountId: number; //The ID of the account to create the key for (default to undefined)
let iApiKeyConfigBase: IApiKeyConfigBase; //The configuration for the new key

const { status, data } = await apiInstance.createKey(
    accountId,
    iApiKeyConfigBase
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **iApiKeyConfigBase** | **IApiKeyConfigBase**| The configuration for the new key | |
| **accountId** | [**number**] | The ID of the account to create the key for | defaults to undefined|


### Return type

**ICreateKeyResponse**

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

# **deleteKey**
> IDeleteKeyResponse deleteKey()

Delete an API key by its key value, name, or ID

### Example

```typescript
import {
    AuthenticationApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AuthenticationApi(configuration);

let accountId: number; //The ID of the account to delete the key for (default to undefined)
let deleteBy: 'value' | 'name' | 'id'; //The API key field to delete by (default to undefined)
let deleteParam: string; //The API key field value to delete by (default to undefined)

const { status, data } = await apiInstance.deleteKey(
    accountId,
    deleteBy,
    deleteParam
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The ID of the account to delete the key for | defaults to undefined|
| **deleteBy** | [**&#39;value&#39; | &#39;name&#39; | &#39;id&#39;**]**Array<&#39;value&#39; &#124; &#39;name&#39; &#124; &#39;id&#39;>** | The API key field to delete by | defaults to undefined|
| **deleteParam** | [**string**] | The API key field value to delete by | defaults to undefined|


### Return type

**IDeleteKeyResponse**

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

# **getKey**
> IRetrieveKeyResponse getKey()

Retrieve an API key by its key value, name, or ID

### Example

```typescript
import {
    AuthenticationApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AuthenticationApi(configuration);

let accountId: number; //The ID of the account to retrieve the key for (default to undefined)
let retrieveParam: string; //The API key field value to retrieve by (default to undefined)
let retrieveBy: 'value' | 'name' | 'id'; //The API key field to retrieve by (optional) (default to 'value')

const { status, data } = await apiInstance.getKey(
    accountId,
    retrieveParam,
    retrieveBy
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The ID of the account to retrieve the key for | defaults to undefined|
| **retrieveParam** | [**string**] | The API key field value to retrieve by | defaults to undefined|
| **retrieveBy** | [**&#39;value&#39; | &#39;name&#39; | &#39;id&#39;**]**Array<&#39;value&#39; &#124; &#39;name&#39; &#124; &#39;id&#39;>** | The API key field to retrieve by | (optional) defaults to 'value'|


### Return type

**IRetrieveKeyResponse**

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

# **listKeys**
> IListKeysResponse listKeys()

Retrieve an API key by its key value, name, or ID

### Example

```typescript
import {
    AuthenticationApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AuthenticationApi(configuration);

let accountId: number; //The ID of the account to retrieve the key for (default to undefined)

const { status, data } = await apiInstance.listKeys(
    accountId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountId** | [**number**] | The ID of the account to retrieve the key for | defaults to undefined|


### Return type

**IListKeysResponse**

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

# **updateKey**
> IUpdateKeyResponse updateKey(iApiKeyConfigBase)

Update an existing API key

### Example

```typescript
import {
    AuthenticationApi,
    Configuration,
    IApiKeyConfigBase
} from './api';

const configuration = new Configuration();
const apiInstance = new AuthenticationApi(configuration);

let accountId: number; //The account to update the key for (default to undefined)
let updateBy: 'value' | 'name' | 'id'; //The API key field to update by (default to undefined)
let updateParam: string; //The API key field value to update by (default to undefined)
let iApiKeyConfigBase: IApiKeyConfigBase; //The new configuration for the key

const { status, data } = await apiInstance.updateKey(
    accountId,
    updateBy,
    updateParam,
    iApiKeyConfigBase
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **iApiKeyConfigBase** | **IApiKeyConfigBase**| The new configuration for the key | |
| **accountId** | [**number**] | The account to update the key for | defaults to undefined|
| **updateBy** | [**&#39;value&#39; | &#39;name&#39; | &#39;id&#39;**]**Array<&#39;value&#39; &#124; &#39;name&#39; &#124; &#39;id&#39;>** | The API key field to update by | defaults to undefined|
| **updateParam** | [**string**] | The API key field value to update by | defaults to undefined|


### Return type

**IUpdateKeyResponse**

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

