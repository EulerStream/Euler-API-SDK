# WebcastFeedResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [default to undefined]
**nickname** | **string** |  | [default to undefined]
**bio_description** | **string** |  | [default to undefined]
**avatar_thumb** | [**WebcastFeedResponseImage**](WebcastFeedResponseImage.md) |  | [default to undefined]
**avatar_medium** | [**WebcastFeedResponseImage**](WebcastFeedResponseImage.md) |  | [default to undefined]
**avatar_large** | [**WebcastFeedResponseImage**](WebcastFeedResponseImage.md) |  | [default to undefined]
**status** | **number** |  | [default to undefined]
**modify_time** | **number** |  | [default to undefined]
**follow_info** | [**WebcastFeedResponseUserFollowInfo**](WebcastFeedResponseUserFollowInfo.md) |  | [default to undefined]
**pay_grade** | **{ [key: string]: any; }** | Construct a type with a set of properties K of type T | [default to undefined]
**user_attr** | **{ [key: string]: any; }** | Construct a type with a set of properties K of type T | [default to undefined]
**own_room** | [**WebcastFeedResponseUserOwnRoom**](WebcastFeedResponseUserOwnRoom.md) |  | [default to undefined]
**display_id** | **string** |  | [default to undefined]
**sec_uid** | **string** |  | [default to undefined]
**id_str** | **string** |  | [default to undefined]

## Example

```typescript
import { WebcastFeedResponseUser } from './api';

const instance: WebcastFeedResponseUser = {
    id,
    nickname,
    bio_description,
    avatar_thumb,
    avatar_medium,
    avatar_large,
    status,
    modify_time,
    follow_info,
    pay_grade,
    user_attr,
    own_room,
    display_id,
    sec_uid,
    id_str,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
