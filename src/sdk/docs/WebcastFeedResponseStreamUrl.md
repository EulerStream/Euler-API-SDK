# WebcastFeedResponseStreamUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rtmp_pull_url** | **string** |  | [default to undefined]
**flv_pull_url** | [**WebcastFeedResponseStreamUrlFlvPullUrl**](WebcastFeedResponseStreamUrlFlvPullUrl.md) |  | [default to undefined]
**flv_pull_url_params** | **{ [key: string]: string; }** | Construct a type with a set of properties K of type T | [optional] [default to undefined]
**live_core_sdk_data** | [**WebcastFeedResponseStreamUrlLiveCoreSdkData**](WebcastFeedResponseStreamUrlLiveCoreSdkData.md) |  | [optional] [default to undefined]
**stream_size_width** | **number** |  | [default to undefined]
**stream_size_height** | **number** |  | [default to undefined]

## Example

```typescript
import { WebcastFeedResponseStreamUrl } from './api';

const instance: WebcastFeedResponseStreamUrl = {
    rtmp_pull_url,
    flv_pull_url,
    flv_pull_url_params,
    live_core_sdk_data,
    stream_size_width,
    stream_size_height,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
