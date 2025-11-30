# IAlertTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **string** |  | [default to undefined]
**metadata** | **{ [key: string]: any; }** | Construct a type with a set of properties K of type T | [optional] [default to undefined]
**alert_id** | **number** |  | [default to undefined]
**alert_creator_id** | **number** |  | [default to undefined]
**id** | **number** |  | [default to undefined]
**last_status** | [**IAlertTargetStatus**](IAlertTargetStatus.md) |  | [default to undefined]
**created_at** | **string** |  | [default to undefined]
**updated_at** | **string** |  | [default to undefined]
**format** | [**IAlertTargetFormat**](IAlertTargetFormat.md) |  | [default to undefined]
**account_id** | **number** |  | [default to undefined]

## Example

```typescript
import { IAlertTarget } from './api';

const instance: IAlertTarget = {
    url,
    metadata,
    alert_id,
    alert_creator_id,
    id,
    last_status,
    created_at,
    updated_at,
    format,
    account_id,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
