# AlertTargetConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **string** |  | [default to undefined]
**metadata** | **{ [key: string]: any; }** | Construct a type with a set of properties K of type T | [default to undefined]
**alert_id** | **number** |  | [default to undefined]
**alert_creator_id** | **number** |  | [default to undefined]
**last_status** | [**AlertTargetStatus**](AlertTargetStatus.md) |  | [default to undefined]
**format** | [**AlertTargetFormat**](AlertTargetFormat.md) |  | [default to undefined]

## Example

```typescript
import { AlertTargetConfig } from './api';

const instance: AlertTargetConfig = {
    url,
    metadata,
    alert_id,
    alert_creator_id,
    last_status,
    format,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
