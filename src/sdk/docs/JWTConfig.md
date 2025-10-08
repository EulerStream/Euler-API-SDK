# JWTConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  | [default to undefined]
**expiresAt** | **number** |  | [default to undefined]
**ttl** | **number** |  | [default to undefined]
**accountId** | **number** |  | [default to undefined]
**apiKeyId** | **number** |  | [default to undefined]
**limits** | [**AccountsTableRequestLimits**](AccountsTableRequestLimits.md) |  | [default to undefined]
**webSocketData** | [**JWTConfigWebSocketData**](JWTConfigWebSocketData.md) |  | [default to undefined]
**name** | **string** |  | [default to undefined]

## Example

```typescript
import { JWTConfig } from './api';

const instance: JWTConfig = {
    id,
    expiresAt,
    ttl,
    accountId,
    apiKeyId,
    limits,
    webSocketData,
    name,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
