# TikTokApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**signTikTokUrl**](#signtiktokurl) | **POST** /tiktok/sign_url | |

# **signTikTokUrl**
> ISignTikTokUrlResponse signTikTokUrl(iSignTikTokUrlBody)

Sign a non-LIVE TikTok URL. This is NOT available to customers in any public package, and access is approved on a case-by-case basis.

### Example

```typescript
import {
    TikTokApi,
    Configuration,
    ISignTikTokUrlBody
} from './api';

const configuration = new Configuration();
const apiInstance = new TikTokApi(configuration);

let iSignTikTokUrlBody: ISignTikTokUrlBody; //Config for the signature generation
let preferredAgentIds: string; //The preferred agent ID to use when signing (optional) (default to undefined)

const { status, data } = await apiInstance.signTikTokUrl(
    iSignTikTokUrlBody,
    preferredAgentIds
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **iSignTikTokUrlBody** | **ISignTikTokUrlBody**| Config for the signature generation | |
| **preferredAgentIds** | [**string**] | The preferred agent ID to use when signing | (optional) defaults to undefined|


### Return type

**ISignTikTokUrlResponse**

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

