# JWTCreateConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**AccountsTableRequestLimits**](AccountsTableRequestLimits.md) |  | [optional] [default to undefined]
**websockets** | [**JWTCreateConfigWebSocketData**](JWTCreateConfigWebSocketData.md) |  | [optional] [default to undefined]
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
