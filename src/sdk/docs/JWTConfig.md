# JWTConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  | [default to undefined]
**expiresAt** | **number** |  | [default to undefined]
**ttl** | **number** |  | [default to undefined]
**accountData** | [**JWTConfigAccountData**](JWTConfigAccountData.md) |  | [default to undefined]
**apiKeyData** | [**JWTConfigApiKeyData**](JWTConfigApiKeyData.md) |  | [default to undefined]
**webSocketData** | [**WebSocketJWTLimits**](WebSocketJWTLimits.md) |  | [default to undefined]
**name** | **string** |  | [default to undefined]

## Example

```typescript
import { JWTConfig } from './api';

const instance: JWTConfig = {
    id,
    expiresAt,
    ttl,
    accountData,
    apiKeyData,
    webSocketData,
    name,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
