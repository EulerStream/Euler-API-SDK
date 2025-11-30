# CaptchasApi

All URIs are relative to *https://tiktok.eulerstream.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**completeIconCaptcha**](#completeiconcaptcha) | **POST** /tiktok/captchas/icons | |
|[**completePuzzleCaptcha**](#completepuzzlecaptcha) | **POST** /tiktok/captchas/puzzle | |
|[**completeShapesCaptcha**](#completeshapescaptcha) | **POST** /tiktok/captchas/shapes | |
|[**completeWhirlCaptcha**](#completewhirlcaptcha) | **POST** /tiktok/captchas/whirl | |
|[**retrieveCaptchaCredits**](#retrievecaptchacredits) | **GET** /tiktok/captchas/credits | |

# **completeIconCaptcha**
> IconCaptchaResponse completeIconCaptcha()

## ⚠️ Warning: Requires Business plan or higher  The icons captcha requires just one image & a prompt string.  ## Example Image <img src=\"https://www.eulerstream.com/_static/captchas/icon.png\" alt=\"Icons Captcha Example\" width=\"480\" />  ## Usage  The `prompt` is the text prompt provided by TikTok. The Icon captcha solution is provided as a list of points, where each point marks a location on the image that needs to be clicked. These points are expressed as ratios relative to the image\'s width and height. A point of (0.0, 0.0) corresponds to the image’s upper-left corner, while (1.0, 1.0) represents the lower-right corner. For reference, (0.5, 0.5) sits at the exact center.  The captcha image selector is `.captcha-verify-image`

### Example

```typescript
import {
    CaptchasApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CaptchasApi(configuration);

let prompt: string; //The prompt string provided by TikTok (default to undefined)
let captchaImage: File; //The uploaded image file (default to undefined)

const { status, data } = await apiInstance.completeIconCaptcha(
    prompt,
    captchaImage
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **prompt** | [**string**] | The prompt string provided by TikTok | defaults to undefined|
| **captchaImage** | [**File**] | The uploaded image file | defaults to undefined|


### Return type

**IconCaptchaResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **completePuzzleCaptcha**
> PuzzleCaptchaResponse completePuzzleCaptcha()

The puzzle captcha requires two images  ## Example Image <img src=\"https://www.eulerstream.com/_static/captchas/puzzle.png\" alt=\"Puzzle Piece Example\" width=\"480\" />  ## Usage  The solution to the puzzle captcha is the distance to move the slider to fit the puzzle piece into the background.  The `backgroundImage` is the full background image with the missing piece. The `pieceImage` is the small puzzle piece that needs to be fit into the background.  The captcha image selectors are: - Background: `.captcha-verify-image` - Piece: `#captcha-verify-image ~ div.cap-absolute > img`  The solution is the `x` proportion (0-1) of the width of the background image where the piece fits. It is 1:1 with the slider distance proportion.

### Example

```typescript
import {
    CaptchasApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CaptchasApi(configuration);

let backgroundImage: File; //The uploaded background image file (default to undefined)
let pieceImage: File; //The uploaded puzzle piece image file (default to undefined)

const { status, data } = await apiInstance.completePuzzleCaptcha(
    backgroundImage,
    pieceImage
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **backgroundImage** | [**File**] | The uploaded background image file | defaults to undefined|
| **pieceImage** | [**File**] | The uploaded puzzle piece image file | defaults to undefined|


### Return type

**PuzzleCaptchaResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **completeShapesCaptcha**
> ShapesCaptchaResponse completeShapesCaptcha()

The shapes captcha requires just one image.  ## Example Image <img src=\"https://www.eulerstream.com/_static/captchas/threed.png\" alt=\"Shapes Captcha Example\" width=\"480\" />  ## Usage  The solution to the shapes captcha are two points that need to be clicked. To use it in the GUI, convert the proportions to pixel values based on the image size.  The `points` are returned as `x` and `y` proportions (0-1) of the width and height of the source image. The captcha image selector is `.captcha-verify-image`

### Example

```typescript
import {
    CaptchasApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CaptchasApi(configuration);

let shapesCaptchaImage: File; //The uploaded image file (default to undefined)

const { status, data } = await apiInstance.completeShapesCaptcha(
    shapesCaptchaImage
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **shapesCaptchaImage** | [**File**] | The uploaded image file | defaults to undefined|


### Return type

**ShapesCaptchaResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **completeWhirlCaptcha**
> WhirlCaptchaResponse completeWhirlCaptcha()

The whirl captcha requires two images: the outer image and the inner image.  ## Example Image <img src=\"https://www.eulerstream.com/_static/captchas/rotate.png\" alt=\"Whirl Captcha Example\" width=\"480\" />  ## Usage  The solution to the whirl captcha is an angle from 0-360. To use it in the GUI, it must be converted to a slider distance:  `px = ((sidebar_length - icon_length) * angle) / 360`  - `sidebar_length` is the width of `.captcha_verify_slide--slidebar` - `icon_length` is the width of `.secsdk-captcha-drag-icon`

### Example

```typescript
import {
    CaptchasApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CaptchasApi(configuration);

let outerImage: File; //The outer image file (default to undefined)
let innerImage: File; //The inner image file (default to undefined)

const { status, data } = await apiInstance.completeWhirlCaptcha(
    outerImage,
    innerImage
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **outerImage** | [**File**] | The outer image file | defaults to undefined|
| **innerImage** | [**File**] | The inner image file | defaults to undefined|


### Return type

**WhirlCaptchaResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieveCaptchaCredits**
> CaptchaCreditsResponse retrieveCaptchaCredits()

Retrieve the rate limits for the provided API key

### Example

```typescript
import {
    CaptchasApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CaptchasApi(configuration);

const { status, data } = await apiInstance.retrieveCaptchaCredits();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**CaptchaCreditsResponse**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

