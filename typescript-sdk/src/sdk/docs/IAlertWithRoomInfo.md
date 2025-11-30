# IAlertWithRoomInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **string** |  | [default to undefined]
**account_id** | **number** |  | [default to undefined]
**alert_creator_id** | **number** |  | [default to undefined]
**id** | **number** |  | [default to undefined]
**created_at** | **string** |  | [default to undefined]
**alert_creator_username** | **string** |  | [default to undefined]
**read_only** | **boolean** |  | [default to undefined]
**room_info** | [**TikTokLiveRoomInfo**](TikTokLiveRoomInfo.md) |  | [optional] [default to undefined]

## Example

```typescript
import { IAlertWithRoomInfo } from './api';

const instance: IAlertWithRoomInfo = {
    unique_id,
    account_id,
    alert_creator_id,
    id,
    created_at,
    alert_creator_username,
    read_only,
    room_info,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
