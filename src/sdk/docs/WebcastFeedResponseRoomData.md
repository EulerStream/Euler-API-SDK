# WebcastFeedResponseRoomData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [default to undefined]
**id_str** | **string** |  | [default to undefined]
**status** | **number** |  | [default to undefined]
**owner_user_id** | **number** |  | [default to undefined]
**title** | **string** |  | [default to undefined]
**user_count** | **number** |  | [default to undefined]
**client_version** | **number** |  | [default to undefined]
**cover** | [**WebcastFeedResponseImage**](WebcastFeedResponseImage.md) |  | [default to undefined]
**stream_url** | [**WebcastFeedResponseStreamUrl**](WebcastFeedResponseStreamUrl.md) |  | [default to undefined]
**stats** | [**WebcastFeedResponseRoomDataStats**](WebcastFeedResponseRoomDataStats.md) |  | [default to undefined]
**feed_room_label** | [**WebcastFeedResponseRoomDataFeedRoomLabel**](WebcastFeedResponseRoomDataFeedRoomLabel.md) |  | [default to undefined]
**owner** | [**WebcastFeedResponseUser**](WebcastFeedResponseUser.md) |  | [default to undefined]
**live_type_third_party** | **boolean** |  | [default to undefined]
**room_auth** | [**{ [key: string]: RecordStringBooleanOrNumberValue; }**](RecordStringBooleanOrNumberValue.md) | Construct a type with a set of properties K of type T | [default to undefined]
**like_count** | **number** |  | [default to undefined]
**anchor_tab_type** | **number** |  | [default to undefined]
**commerce_info** | **{ [key: string]: any; }** | Construct a type with a set of properties K of type T | [default to undefined]
**hashtag** | [**WebcastFeedResponseHashtag**](WebcastFeedResponseHashtag.md) |  | [optional] [default to undefined]
**live_room_mode** | **number** |  | [default to undefined]
**stream_url_filtered_info** | **{ [key: string]: any; }** | Construct a type with a set of properties K of type T | [default to undefined]
**square_cover_img** | [**WebcastFeedResponseRoomDataSquareCoverImg**](WebcastFeedResponseRoomDataSquareCoverImg.md) |  | [default to undefined]
**rectangle_cover_img** | [**WebcastFeedResponseRoomDataFeedRoomLabel**](WebcastFeedResponseRoomDataFeedRoomLabel.md) |  | [default to undefined]
**blurred_cover** | [**WebcastFeedResponseRoomDataSquareCoverImg**](WebcastFeedResponseRoomDataSquareCoverImg.md) |  | [default to undefined]
**multi_stream_url** | **{ [key: string]: any; }** | Construct a type with a set of properties K of type T | [default to undefined]
**game_tag_detail** | [**WebcastFeedResponseRoomDataGameTagDetail**](WebcastFeedResponseRoomDataGameTagDetail.md) |  | [default to undefined]
**taxonomy_tag_info** | [**WebcastFeedResponseRoomDataTaxonomyTagInfo**](WebcastFeedResponseRoomDataTaxonomyTagInfo.md) |  | [default to undefined]

## Example

```typescript
import { WebcastFeedResponseRoomData } from './api';

const instance: WebcastFeedResponseRoomData = {
    id,
    id_str,
    status,
    owner_user_id,
    title,
    user_count,
    client_version,
    cover,
    stream_url,
    stats,
    feed_room_label,
    owner,
    live_type_third_party,
    room_auth,
    like_count,
    anchor_tab_type,
    commerce_info,
    hashtag,
    live_room_mode,
    stream_url_filtered_info,
    square_cover_img,
    rectangle_cover_img,
    blurred_cover,
    multi_stream_url,
    game_tag_detail,
    taxonomy_tag_info,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
