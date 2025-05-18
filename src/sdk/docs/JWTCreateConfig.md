# JWTCreateConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**IAccountRequestLimits**](IAccountRequestLimits.md) |  | [optional] [default to undefined]
**websockets** | [**WebSocketJWTLimits**](WebSocketJWTLimits.md) |  | [optional] [default to undefined]
**expireAfter** | **number** |  | [default to undefined]
**name** | **string** |  | [optional] [default to undefined]

## Example

```typescript
import { JWTCreateConfig } from './api';

const instance: JWTCreateConfig = {
    limits,
    websockets,
    expireAfter,
    name,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
