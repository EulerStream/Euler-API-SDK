# PartialSignedUrlStringUserAgentStringBrowserNameStringBrowserVersionStringTokensRecordStringStringRequestHeadersRecordStringStringCookiesRecordStringStringArray

Make all properties in T optional

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signedUrl** | **string** |  | [optional] [default to undefined]
**userAgent** | **string** |  | [optional] [default to undefined]
**browserName** | **string** |  | [optional] [default to undefined]
**browserVersion** | **string** |  | [optional] [default to undefined]
**tokens** | **{ [key: string]: string; }** | Construct a type with a set of properties K of type T | [optional] [default to undefined]
**requestHeaders** | **{ [key: string]: string; }** | Construct a type with a set of properties K of type T | [optional] [default to undefined]
**cookies** | **Array&lt;{ [key: string]: string; }&gt;** |  | [optional] [default to undefined]

## Example

```typescript
import { PartialSignedUrlStringUserAgentStringBrowserNameStringBrowserVersionStringTokensRecordStringStringRequestHeadersRecordStringStringCookiesRecordStringStringArray } from './api';

const instance: PartialSignedUrlStringUserAgentStringBrowserNameStringBrowserVersionStringTokensRecordStringStringRequestHeadersRecordStringStringCookiesRecordStringStringArray = {
    signedUrl,
    userAgent,
    browserName,
    browserVersion,
    tokens,
    requestHeaders,
    cookies,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
