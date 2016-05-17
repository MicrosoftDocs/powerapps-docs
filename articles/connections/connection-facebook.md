<properties
	pageTitle="Overview of the Facebook connection | Microsoft PowerApps"
	description="See the available Facebook functions, responses, and examples"
	services=""	
	suite="powerapps"
	documentationCenter="" 	
	authors="MandiOhlinger"	
	manager="erikre"	
	editor="" 
	tags="" />

<tags
ms.service="powerapps"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="na"
ms.date="05/05/2016"
ms.author="mandia"/>

#  Facebook

![Facebook](./media/connection-facebook/facebookicon.png)

Facebook API allows you to access and publish posts on your Facebook user account

You can display this information in a text box on your app. For example, you can create an app that uses an input text box. Users enter text, and then post their text to Facebook. 

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[TriggerNewPost](connection-facebook.md#triggernewpost) | Triggers a new flow when there is a new post on the logged in user's timeline |
|[MyTimeline](connection-facebook.md#mytimeline) | Gets the feeds from the logged in user's timeline |
|[PostToMyTimeline](connection-facebook.md#posttomytimeline) | Post a status message to the logged in user's timeline |
|[UserTimeline](connection-facebook.md#usertimeline) | Get posts from a user's timeline |
|[PageFeed](connection-facebook.md#pagefeed) | Get posts from the feed of a specified page |
|[PostToPage](connection-facebook.md#posttopage) | Post a message to a Facebook Page as the logged in user |



## TriggerNewPost
When there is a new post on my timeline: Triggers a new flow when there is a new post on the logged in user's timeline 

#### Input properties
None.

#### Output properties

| Property Name | Type | Required | Description |
| --- | --- | --- |--- |
|data|array|No | An individual entry in a profile's feed. The profile could be a user, page, app, or group. Properties include: <ul><li>id (optional): The post ID</li><li>created_time (optional): The time the post was initially published. For a post about a life event, this will be the date and time of the life event.</li><li>from (optional): Information about the profile that posted the message.</li><li>message (optional): The status message in the post.</li><li>type (optional): A string indicating the object type of this post.</li></ul> |


## MyTimeline
Get feed from my timeline: Gets the feeds from the logged in user's timeline 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|fields|string|no|Specify the fields you want returned. Example (id,name,picture).|
|limit|integer|no|Maximum number of posts to be retrieved|
|with|string|no|Restrict the list of posts to only those with location attached.|
|filter|string|no|Retrieve only posts that match a particular stream filter.|

#### Output properties

| Property Name | Type | Required | Description |
| --- | --- | --- |--- |
|data|array|No | *PostItem*: An individual entry in a profile's feed. The profile could be a user, page, app, or group. Properties include: <ul><li>id (optional): Unique ID of the post</li><li>admin_creator (optional): Unique ID of admin who created the post. Applies to pages only.</li><li>caption (optional): The caption of a link in the post (appears beneath the name).</li><li>created_time (optional): The time the post was initially published. For a post about a life event, this will be the date and time of the life event.</li><li>description (optional): A description of a link in the post (appears beneath the caption).</li><li>feed_targeting (optional): Object that controls news feed targeting for this post. Anyone in these groups will be more likely to see this post, others will be less likely. Applies to Pages only. Properties include targeted country, targeted region, excluded cities, minimum age, maximum age, targeted genders, targeted relationship status, targeted interests, targeted college graduation year, targeted education statuses, and targeted locales.</li><li>from (optional): Information about the profile that posted the message. Properties include user ID, first name, last name, user full name, gender, and user bio.</li><li>icon (optional): A link to an icon representing the type of this post.</li><li>is_hidden (optional): If this post is marked as hidden (applies to Pages only).</li><li>is_published (optional): Indicates whether a scheduled post was published (applies to scheduled Page Post only, for users post and instanlty published posts this value is always true).</li><li>link (optional): The link attached to this post.</li><li>message (optional): The status message in the post.</li><li>name (optional): The name of the link.</li><li>object_id (optional): The ID of any uploaded photo or video attached to the post.</li><li>picture (optional): The picture scraped from any link included with the post.</li><li>place (optional): Any location information attached to the post. </li><li>privacy (optional): Determines the privacy settings of the post. Value options include: Everyone, All Friends, Friends of friends, Self, and Custom. <br/> When Value is set to Custom, the Allow, Deny, and Friends properties are also available. When using Allow or Deny, create a comma-separated list of User IDs and friend list IDs that can/cannot see the post. When using Friends, select the group of friends that can see the post.</li><li>properties (optional): A list of properties for any attached video, for example, the length of the video. Properties include the property name, the value of the property, and any link associated with the property.</li><li>source (optional): A URL to any Flash movie or video file attached to the post.</li><li>status_type (optional): Description of the type of a status update. Options include mobile_status_update, created_note, added_photos, added_video, shared_story, created_group, created_event, wall_post, app_created_story, published_story, tagged_in_photo, and approved_friend.</li><li>story (optional): Text from stories not intentionally generated by users, such as those generated when two people become friends, or when someone else posts on the person's wall.</li><li>targeting (optional): Object that limits the audience for this content. Properties include targeted countries, targeted locales, targeted region, and excluded cities.</li><li>to (optional): Profiles mentioned or targeted in this post. UserItem properties include user ID, first name, last name, user full name, gender, and user bio.</li><li>type (optional): A string indicating the object type of this post. Options include link, status, photo, video, and offer.</li><li>updated_time (optional): The time of the last change to this post, or the comments on it.</li><li>with_tags (optional): Profiles tagged as being 'with' the publisher of the post. UserItem properties include user ID, first name, last name, user full name, gender, and user bio.</li></ul> | 


## PostToMyTimeline
Post to my timeline: Post a status message to the logged in user's timeline 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|post| |yes|New message to be posted. Properties include: <ul><li>message: The main body of the post, otherwise called the status message.</li><li>link: The URL of a link to attach to the post.</li><li>picture: Determines the preview image associated with the link.</li><li>name: Overwrites the title of the link preview.</li><li>caption: Overwrites the caption under the title in the link preview.</li><li>description: Overwrites the description in the link preview.</li><li>place: Page ID of a location associated with this post</li><li>tags: Comma-separated list of user IDs of people tagged in this post.</li><li>privacy: Determines the privacy settings of the post.</li><li>object_attachment: Facebook ID for an existing picture in the person's photo </li>albums to use as the thumbnail image.</li></ul> |

#### Output properties

| Property Name | Type | Required | Description |
| --- | --- | --- |--- |
|id | string | no | Post ID |


## UserTimeline
Get user timeline: Get posts from a user's timeline 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|userId|string|yes|Unique ID of the user whose timeline have to be retrieved.|
|limit|integer|no|Maximum number of posts to be retrieved|
|with|string|no|Restrict the list of posts to only those with location attached.|
|filter|string|no|Retrieve only posts that match a particular stream filter.|
|fields|string|no|Specify the fields you want returned. Example (id,name,picture).|

#### Output properties

| Property Name | Type | Required | Description |
| --- | --- | --- |--- |
|data|array|No | *PostItem*: An individual entry in a profile's feed. The profile could be a user, page, app, or group. Properties include: <ul><li>id (optional): Unique ID of the post</li><li>admin_creator (optional): Unique ID of admin who created the post. Applies to pages only.</li><li>caption (optional): The caption of a link in the post (appears beneath the name).</li><li>created_time (optional): The time the post was initially published. For a post about a life event, this will be the date and time of the life event.</li><li>description (optional): A description of a link in the post (appears beneath the caption).</li><li>feed_targeting (optional): Object that controls news feed targeting for this post. Anyone in these groups will be more likely to see this post, others will be less likely. Applies to Pages only. Properties include targeted country, targeted region, excluded cities, minimum age, maximum age, targeted genders, targeted relationship status, targeted interests, targeted college graduation year, targeted education statuses, and targeted locales.</li><li>from (optional): Information about the profile that posted the message. Properties include user ID, first name, last name, user full name, gender, and user bio.</li><li>icon (optional): A link to an icon representing the type of this post.</li><li>is_hidden (optional): If this post is marked as hidden (applies to Pages only).</li><li>is_published (optional): Indicates whether a scheduled post was published (applies to scheduled Page Post only, for users post and instanlty published posts this value is always true).</li><li>link (optional): The link attached to this post.</li><li>message (optional): The status message in the post.</li><li>name (optional): The name of the link.</li><li>object_id (optional): The ID of any uploaded photo or video attached to the post.</li><li>picture (optional): The picture scraped from any link included with the post.</li><li>place (optional): Any location information attached to the post. </li><li>privacy (optional): Determines the privacy settings of the post. Value options include: Everyone, All Friends, Friends of friends, Self, and Custom. <br/> When Value is set to Custom, the Allow, Deny, and Friends properties are also available. When using Allow or Deny, create a comma-separated list of User IDs and friend list IDs that can/cannot see the post. When using Friends, select the group of friends that can see the post.</li><li>properties (optional): A list of properties for any attached video, for example, the length of the video. Properties include the property name, the value of the property, and any link associated with the property.</li><li>source (optional): A URL to any Flash movie or video file attached to the post.</li><li>status_type (optional): Description of the type of a status update. Options include mobile_status_update, created_note, added_photos, added_video, shared_story, created_group, created_event, wall_post, app_created_story, published_story, tagged_in_photo, and approved_friend.</li><li>story (optional): Text from stories not intentionally generated by users, such as those generated when two people become friends, or when someone else posts on the person's wall.</li><li>targeting (optional): Object that limits the audience for this content. Properties include targeted countries, targeted locales, targeted region, and excluded cities.</li><li>to (optional): Profiles mentioned or targeted in this post. UserItem properties include user ID, first name, last name, user full name, gender, and user bio.</li><li>type (optional): A string indicating the object type of this post. Options include link, status, photo, video, and offer.</li><li>updated_time (optional): The time of the last change to this post, or the comments on it.</li><li>with_tags (optional): Profiles tagged as being 'with' the publisher of the post. UserItem properties include user ID, first name, last name, user full name, gender, and user bio.</li></ul> | 


## PageFeed
Get page feed: Get posts from the feed of a specified page 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|pageId|string|yes|Unique ID of the page from which posts have to be retrieved.|
|limit|integer|no|Maximum number of posts to be retrieved|
|include_hidden|boolean|no|Whether or not to include any posts that were hidden by the Page|
|fields|string|no|Specify the fields you want returned. Example (id,name,picture).|

#### Output properties

| Property Name | Type | Required | Description |
| --- | --- | --- |--- |
|data|array|No | *PostItem*: An individual entry in a profile's feed. The profile could be a user, page, app, or group. Properties include: <ul><li>id (optional): Unique ID of the post</li><li>admin_creator (optional): Unique ID of admin who created the post. Applies to pages only.</li><li>caption (optional): The caption of a link in the post (appears beneath the name).</li><li>created_time (optional): The time the post was initially published. For a post about a life event, this will be the date and time of the life event.</li><li>description (optional): A description of a link in the post (appears beneath the caption).</li><li>feed_targeting (optional): Object that controls news feed targeting for this post. Anyone in these groups will be more likely to see this post, others will be less likely. Applies to Pages only. Properties include targeted country, targeted region, excluded cities, minimum age, maximum age, targeted genders, targeted relationship status, targeted interests, targeted college graduation year, targeted education statuses, and targeted locales.</li><li>from (optional): Information about the profile that posted the message. Properties include user ID, first name, last name, user full name, gender, and user bio.</li><li>icon (optional): A link to an icon representing the type of this post.</li><li>is_hidden (optional): If this post is marked as hidden (applies to Pages only).</li><li>is_published (optional): Indicates whether a scheduled post was published (applies to scheduled Page Post only, for users post and instanlty published posts this value is always true).</li><li>link (optional): The link attached to this post.</li><li>message (optional): The status message in the post.</li><li>name (optional): The name of the link.</li><li>object_id (optional): The ID of any uploaded photo or video attached to the post.</li><li>picture (optional): The picture scraped from any link included with the post.</li><li>place (optional): Any location information attached to the post. </li><li>privacy (optional): Determines the privacy settings of the post. Value options include: Everyone, All Friends, Friends of friends, Self, and Custom. <br/> When Value is set to Custom, the Allow, Deny, and Friends properties are also available. When using Allow or Deny, create a comma-separated list of User IDs and friend list IDs that can/cannot see the post. When using Friends, select the group of friends that can see the post.</li><li>properties (optional): A list of properties for any attached video, for example, the length of the video. Properties include the property name, the value of the property, and any link associated with the property.</li><li>source (optional): A URL to any Flash movie or video file attached to the post.</li><li>status_type (optional): Description of the type of a status update. Options include mobile_status_update, created_note, added_photos, added_video, shared_story, created_group, created_event, wall_post, app_created_story, published_story, tagged_in_photo, and approved_friend.</li><li>story (optional): Text from stories not intentionally generated by users, such as those generated when two people become friends, or when someone else posts on the person's wall.</li><li>targeting (optional): Object that limits the audience for this content. Properties include targeted countries, targeted locales, targeted region, and excluded cities.</li><li>to (optional): Profiles mentioned or targeted in this post. UserItem properties include user ID, first name, last name, user full name, gender, and user bio.</li><li>type (optional): A string indicating the object type of this post. Options include link, status, photo, video, and offer.</li><li>updated_time (optional): The time of the last change to this post, or the comments on it.</li><li>with_tags (optional): Profiles tagged as being 'with' the publisher of the post. UserItem properties include user ID, first name, last name, user full name, gender, and user bio.</li></ul> | 


## PostToPage
Post to page: Post a message to a Facebook Page as the logged in user 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|pageId|string|yes|Unique ID of the page to post to.|
|post| |yes|New message to be posted. Properties include: <ul><li>message (required): The main body of the post, otherwise called the status message.</li><li>link (optional): The URL of a link to attach to the post.</li><li>picture (optional): Determines the preview image associated with the link.</li><li>name (optional): Overwrites the title of the link preview.</li><li>caption (optional): Overwrites the caption under the title in the link preview.</li><li>description (optional): Overwrites the description in the link preview.</li><li>actions (optional): The action links attached to the post. Options include the name or label of the action link, and The URL of the action link itself. </li><li>place (optional): Page ID of a location associated with this post</li><li>tags (optional): Comma-separated list of user IDs of people tagged in this post.</li><li>object_attachment (optional): Facebook ID for an existing picture in the person's photo albums to use as the thumbnail image.</li><li>targeting (optional): Object that limits the audience for this content. Properties include targeted countries, targeted locales, targeted regions, and excluded cities.</li><li>feed_targeting (optional): Object that controls news feed targeting for this content. Properties include targeted countries, targeted locales, targeted regions, and excluded cities.</li><li>published (optional): Whether a story is shown about this newly published object.</li><li>scheduled_publish_time (optional): Time when this post should go live, this can be any date between ten minutes and six months from the time of the API call.</li><li>backdated_time (optional): Specifies a time in the past to back-date this post to.</li><li>backdated_time_granularity (optional): Controls the display of how a backdated post appears.</li><li>child_attachments (optional): Use to specify multiple links in the post. Properties include the link URL to attach to the post, picture associated with the link, image hash associated with the link, link name, and link description. </li><li>multi_share_end_card (optional): If set to false, does not display the end card of a carousel link post when child_attachments is used.</li></ul> |

#### Output properties - PostFeedResponse

| Property Name | Type | Required | Description |
| --- | --- | --- |--- |
|id|string|No | Post ID |


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.