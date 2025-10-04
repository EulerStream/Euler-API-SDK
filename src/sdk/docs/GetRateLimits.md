# GetRateLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **number** |  | [default to undefined]
**message** | **string** |  | [optional] [default to undefined]
**day** | [**RateLimitInfo**](RateLimitInfo.md) |  | [optional] [default to undefined]
**hour** | [**RateLimitInfo**](RateLimitInfo.md) |  | [optional] [default to undefined]
**minute** | [**RateLimitInfo**](RateLimitInfo.md) |  | [optional] [default to undefined]
**load_shedding** | [**LoadShedInfo**](LoadShedInfo.md) |  | [default to undefined]

## Example

```typescript
import { GetRateLimits } from './api';

const instance: GetRateLimits = {
    code,
    message,
    day,
    hour,
    minute,
    load_shedding,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
