<properties
	pageTitle="Overview of the Twilio connection | Microsoft PowerApps"
	description="See the available Twilio functions, responses, and examples"
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
ms.date="04/25/2016"
ms.author="mandia"/>


#  Twilio

![Twilio](./media/connection-twilio/twilioicon.png)

Twilio enables apps to send and receive global SMS, MMS and IP messages.

You can display and send messages from your app. For example, you can add a gallery on your app that returns all the messages from a Twilio account. You can also add some input text boxes that asks the user for message information, including the To recipient and the from number. Then add a button that sends the message. You can do all this from your app. 

This topic shows the available functions.

##  What you need to get started

- Access to the [PowerApps portal][1] or install [PowerApps][2]
- Add the [connection](../add-manage-connections.md)
- Create an app from a [template](../get-started-test-drive.md), from [data](../get-started-create-from-data.md), or from [scratch](../get-started-create-from-blank.md)

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[ListMessages](connection-twilio.md#listmessages) | Returns a list of messages associated with your account |
|[SendMessage](connection-twilio.md#sendmessage) | Send a new message to a mobile number |
|[GetMessage](connection-twilio.md#getmessage) | Returns a single message specified by the provided Message ID |


## ListMessages
List Messages: Returns a list of messages associated with your account 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|To|string|no|Only show messages to this phone number.|
|From|string|no|Only show messages from this phone number.|
|DateSent|string|no|Only show messages sent on this date (in GMT format), given as YYYY-MM-DD. <br/><br/>Example: DateSent=2009-07-06. <br/><br/>You can also specify inequality, such as DateSent<=YYYY-MM-DD for messages that were sent on or before midnight on a date, and DateSent>=YYYY-MM-DD for messages sent on or after midnight on a date.|
|PageSize|integer|no|How many resources to return in each list page. Default is 50.|
|Page|integer|no|Page number. Default is 0.|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|messages|array|No |Message |
|page|integer|No | Page number|
|page_size|integer|No |Page Size |
|num_pages|integer|No |Number of Pages |
|uri|string|No |relative URI for this list |
|first_page_uri|string|No |relative URI for the first page |
|next_page_uri|string|No | relative URI for the next page|
|total|integer|No | Total number of messages|
|previous_page_uri|string|No |relative URI for the previous page |


## SendMessage
Send Message: Send a new message to a mobile number. 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|sendMessageRequest| |yes|Message To Send that includes the following: <ul><li>from (required)</li><li>to (required)</li><li>body (required)</li><li>media_url (optional)</li><li>status_callback (optional)</li><li>messaging_service_sid (optional)</li><li>application_sid (optional)</li><li>max_price (optional)</li></ul> |




#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|body|string|No |Body |
|from|string|No | From Phone Number|
|to|string|No |To Phone Number |
|status|string|No |To Phone Number |
|sid|string|No |Message SID |
|account_sid|string|No |Account Sid |
|api_version|string|No | API version|
|num_segments|string|No |Number of Segments |
|num_media|string|No | Number of associated media files|
|date_created|string|No |Date Created |
|date_sent|string|No |Sent Date |
|date_updated|string|No |Updated Date |
|direction|string|No | Direction|
|error_code|string|No | Error Codes|
|error_message|string|No |Error Messages |
|price|string|No | Price|
|price_unit|string|No |Price Unit |
|uri|string|No |relative URI for this resource" |
|subresource_uris|array|No |relative The URIs for any subresources |
|messaging_service_sid|string|No | Unique id of the Messaging Service|


## GetMessage
Get Message: Returns a single message specified by the provided Message ID. 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|MessageId|string|yes|Message SID|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|body|string|No |Body |
|from|string|No | From Phone Number|
|to|string|No |To Phone Number |
|status|string|No |To Phone Number |
|sid|string|No |Message SID |
|account_sid|string|No |Account Sid |
|api_version|string|No | API version|
|num_segments|string|No |Number of Segments |
|num_media|string|No | Number of associated media files|
|date_created|string|No |Date Created |
|date_sent|string|No |Sent Date |
|date_updated|string|No |Updated Date |
|direction|string|No | Direction|
|error_code|string|No | Error Codes|
|error_message|string|No |Error Messages |
|price|string|No | Price|
|price_unit|string|No |Price Unit |
|uri|string|No |relative URI for this resource" |
|subresource_uris|array|No |relative The URIs for any subresources |
|messaging_service_sid|string|No | Unique id of the Messaging Service|


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.

[1]: https://web.powerapps.com
[2]: http://aka.ms/powerappsinstall