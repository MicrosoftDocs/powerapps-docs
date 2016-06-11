<properties
	pageTitle="Overview of the Slack connection | Microsoft PowerApps"
	description="See the available Slack functions, responses, and examples"
	services=""
	suite="powerapps"
	documentationCenter="" 	
	authors="AFTOwen"
	manager="erikre"
	editor=""
	tags="" />

<tags
ms.service="powerapps"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="na"
ms.date="04/26/2016"
ms.author="anneta"/>

#  Slack

![Slack](./media/connection-slack/slackicon.png)

Slack is a team communication tool, that brings together all of your team communications in one place, instantly searchable and available wherever you go.

In your app, you can add an input text box that asks the user to enter in some text. Then add a button that "posts" the message to a Slack channel.

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[PostMessage](connection-slack.md#postmessage) | Post a Message to a specified channel |

## PostMessage
Post Message: Post a Message to a specified channel.

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|channel|string|yes|Channel, private group, or IM channel to send message to. Can be a name(ex: #general) or an encoded ID.|
|text|string|yes|Text of the message to send. For formatting options, see https://api.slack.com/docs/formatting.|
|username|string|no|Name of the bot|
|as_user|boolean|no|Pass true to post the message as the authenticated user, instead of as a bot|
|parse|string|no|Change how messages are treated. For details, see https://api.slack.com/docs/formatting.|
|link_names|integer|no|Find and link channel names and usernames.|
|unfurl_links|boolean|no|Pass true to enable unfurling of primarily text-based content.|
|unfurl_media|boolean|no|Pass false to disable unfurling of media content.|
|icon_url|string|no|URL to an image to use as an icon for this message|
|icon_emoji|string|no|Emoji to use as an icon for this message|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|ok|boolean|No | Indicates if the operation was successful|
|channel|string|No | The channel which the message was posted to|
|ts|string|No |The time stamp for when the message is posted |
|message|not defined|No |The message that was posted |
|error|string|No | Error messages (if any)|


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
