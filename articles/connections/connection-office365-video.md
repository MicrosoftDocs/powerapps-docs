<properties
	pageTitle="Overview of the Office 365 Video connection | Microsoft PowerApps"
	description="See the available Office 365 Video functions, responses, and examples"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="archnair"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/26/2016"
   ms.author="archanan"/>

#  Office 365 Video

![Office 365 Video](./media/connection-office365-video/office365icon.png)

The Office 365 Video provides access to work with Office 365 channels and videos.

You can display video information on your app. For example, you can display all the available videos from a specific Office 365 video channel in your app. You can also display a specific video from a channel, and then play it on your app.

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[IsVideoPortalEnabled](connection-office365-video.md#isvideoportalenabled) | Checks the video portal status to see if video services are enabled  |
|[ListViewableChannels](connection-office365-video.md#listviewablechannels) | Gets all the channels the user has viewing access to  |
|[ListVideos](connection-office365-video.md#listvideos) | Lists all the Office 365 videos present in a channel  |
|[GetVideo](connection-office365-video.md#getvideo) | Gets information about a particular Office 365 video  |
|[GetPlaybackUrl](connection-office365-video.md#getplaybackurl) | Get playback url of the Azure Media Services manifest for a video  |
|[GetStreamingKeyAccessToken](connection-office365-video.md#getstreamingkeyaccesstoken) | Get playback url of the Azure Media Services manifest for a video  |


## IsVideoPortalEnabled
Checks video portal status: Checks the video portal status to see if video services are enabled

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|tenant|string|yes|The tenant name for the directory the user is part of|

#### Output properties
None.


## ListViewableChannels
Get all viewable Channels: Gets all the channels the user has viewing access to

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|tenant|string|yes|The tenant name for the directory the user is part of|

#### Output properties

| Property Name | Data Type | Required | Description|
| ---|---|---|---|
|Id|string|No | |
|Title|string|No | |
|Description|string|No | |


## ListVideos
Lists all the Office 365 videos present in a channel: Lists all the Office 365 videos present in a channel

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|tenant|string|yes|The tenant name for the directory the user is part of|
|channelId|string|yes|The channel id from which videos need to be fetched|

#### Output properties - Video

| Property Name | Data Type | Required | Description|
| ---|---|---|---|
|Id|string|No | |
|Title|string|No | |
|Description|string|No | |
|CreationDate|string|No | |
|Owner|string|No | |
|ThumbnailUrl|string|No | |
|VideoUrl|string|No | |
|VideoDuration|integer|No | |
|VideoProcessingStatus|integer|No | |
|ViewCount|integer|No | |


## GetVideo
Gets information about a particular office 365 video: Gets information about a particular Office 365 video

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|tenant|string|yes|The tenant name for the directory the user is part of|
|channelId|string|yes|The channel id|
|videoId|string|yes|The video id|

#### Output properties - Video

| Property Name | Data Type | Required | Description|
| ---|---|---|---|
|Id|string|No | |
|Title|string|No | |
|Description|string|No | |
|CreationDate|string|No | |
|Owner|string|No | |
|ThumbnailUrl|string|No | |
|VideoUrl|string|No | |
|VideoDuration|integer|No | |
|VideoProcessingStatus|integer|No | |
|ViewCount|integer|No | |


## GetPlaybackUrl
Get playback url of the Azure Media Services manifest for a video: Get playback url of the Azure Media Services manifest for a video

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|tenant|string|yes|The tenant name for the directory the user is part of|
|channelId|string|yes|The channel id|
|videoId|string|yes|The video id|
|streamingFormatType|string|yes|Streaming format type: <ul><li>1 - Smooth Streaming or MPEG-DASH</li><li> 0 - HLS Streaming</li></ul>|

#### Output properties
None.


## GetStreamingKeyAccessToken
Get the bearer token to get access to decrypt the video: Get the bearer token to get access to decrypt the video

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|tenant|string|yes|The tenant name for the directory the user is part of|
|channelId|string|yes|The channel id|
|videoId|string|yes|The video id|

#### Output properties
None.


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
