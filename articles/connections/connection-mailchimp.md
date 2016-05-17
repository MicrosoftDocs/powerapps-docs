<properties
	pageTitle="Overview of the MailChimp connection | Microsoft PowerApps"
	description="See the available MailChimp functions, responses, and examples"
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
ms.date="04/26/2016"
ms.author="mandia"/>

#  MailChimp

![MailChimp](./media/connection-mailchimp/mailchimpicon.png)

MailChimp is a SaaS service that allows businesses to manage and automate email marketing activities, including sending marketing emails, automated messages and targeted campaigns.

You can manage campaigns, lists, and more using controls within your app. For example, you can add input text boxes that asks users for campaign details. Then, you can add a button that creates a new campaign based on the text the users entered.

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[newcampaign](connection-mailchimp.md#newcampaign) | Create a new campaign based on a Campaign Type, Recipients list and Campaign Settings (subject line, title, from_name and reply_to) |
|[newlist](connection-mailchimp.md#newlist) | Create a new list in your MailChimp account |
|[addmember](connection-mailchimp.md#addmember) | Add or update a list member |
|[removemember](connection-mailchimp.md#removemember) | Delete a member from a list.  |
|[updatemember](connection-mailchimp.md#updatemember) | Update information for a specific list member |
|[OnMemberSubscribed](connection-mailchimp.md#onmembersubscribed) | Triggers a workflow when a new member has been added to a list |
|[OnCreateList](connection-mailchimp.md#oncreatelist) | Triggers a workflow when a new list is created |


## newcampaign
New Campaign: Create a new campaign based on a Campaign Type, Recipients list and Campaign Settings (subject line, title, from_name and reply_to) 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|newCampaignRequest| |yes|Json object to send in the body with the new campaign request parameters|

#### Output properties - CampaignResponseModel

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|id|string|No |A string that uniquely identifies this campaign |
|type|string|No | There are four types of campaigns you can create in MailChimp: <ul><li>"regular"</li><li>"plaintext"</li><li>"absplit"</li><li>"rss"</li><li>"variate"</li></ul><br/>**Note** *A/B Split* campaigns have been deprecated and *variate* campaigns should be used instead. |
|create_time|string|No | The date and time the campaign was created|
|archive_url|string|No | The link to the campaign’s archive version|
|status|string|No | The link to the campaign’s archive version|
|emails_sent|integer|No | The total number of emails sent for this campaign|
|send_time|string|No | The time and date a campaign was sent|
|content_type|string|No | How the campaign’s content is put together: <ul><li>‘template’</li><li>‘drag_and_drop’</li><li>‘html’</li><li>‘url’</li></ul> |
|recipient|array|No | List settings for the campaign|
|settings|not defined|No | The settings for your campaign, including subject, from name, reply-to address, and more|
|variate_settings|not defined|No | The settings specific to A/B test campaigns|
|tracking|not defined|No | The tracking options for a campaign|
|rss_opts|not defined|No | RSS options for a campaign|
|ab_split_opts|not defined|No | A/B Testing options for a campaign|
|social_card|not defined|No | A/B Testing options for a campaign|
|report_summary|not defined|No | For sent campaigns, a summary of opens, clicks, and unsubscribes|
|delivery_status|not defined|No | Updates on campaigns in the process of sending|
|_links|array|No | A list of link types and descriptions for the API schema documents|


## newlist
New List: Create a new list in your MailChimp account 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|newListRequest| |yes|Json object to send in the body with the new campaign request parameters|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|id|string|Yes | A string that uniquely identifies this list|
|name|string|Yes | The name of the list|
|contact|not defined|Yes | Contact information displayed in campaign footers to comply with international spam laws|
|permission_reminder|string|Yes | The permission reminder for the list|
|use_archive_bar|boolean|No | Whether campaigns for this list use the Archive Bar in archives by default|
|campaign_defaults|not defined|Yes | Default values for campaigns created for this list|
|notify_on_subscribe|string|No | The email address to send subscribe notifications to|
|notify_on_unsubscribe|string|No | The email address to send unsubscribe notifications to|
|date_created|string|No | The date and time that this list was created|
|list_rating|integer|No | An auto-generated activity score for the list (0-5)|
|email_type_option|boolean|Yes | Whether the list supports multiple formats for emails. When set to true, subscribers can choose whether they want to receive HTML or plain-text emails. When set to false, subscribers will receive HTML emails, with a plain-text alternative backup|
|subscribe_url_short|string|No | Our EepURL shortened version of this list’s subscribe form|
|subscribe_url_long|string|No | The full version of this list’s subscribe form (host will vary)|
|beamer_address|string|No | The list’s Email Beamer address|
|visibility|string|No | Whether this list is public or private|
|modules|array|No | Any list-specific modules installed for this list|
|stats|not defined|No | Stats for the list.Many of these are cached for at least five minutes|
|_links|array|No | A list of link types and descriptions for the API schema documents|


## addmember
Add member to list: Add or update a list member 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|list_id|string|yes|The unique id for the list|
|newMemberInList| |yes|Json object to send in the body with the new member information|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|id|string|No | The MD5 hash of the lowercase version of the list member’s email address|
|email_address|string|No | Email address for a subscriber|
|unique_email_id|string|No | An identifier for the address across all of MailChimp|
|email_type|string|No | Type of email this member asked to get (‘html’ or ‘text’).|
|status|string|No | Subscriber’s current status. Possible Values: subscribed, unsubscribed, cleaned, pending|
|merge_fields|not defined|No |An individual merge var and value for a member |
|interests|string|No | The key of this object’s properties is the ID of the interest in question|
|stats|not defined|No | Open and click rates for this subscriber|
|ip_signup|string|No |IP address the subscriber signed up from |
|timestamp_signup|string|No |Date and time the subscriber signed up for the list |
|ip_opt|string|No | The IP address the subscriber used to confirm their opt-in status|
|timestamp_opt|string|No | Date and time the subscribe confirmed their opt-in status|
|member_rating|integer|No | Star rating for this member, between 1 and 5|
|last_changed|string|No |Date and time the member’s info was last changed |
|language|string|No |If set/detected, the subscriber’s language |
|vip|boolean|No | VIP status for subscriber|
|email_client|string|No |The list member’s email client |
|location|not defined|No | Subscriber location information|
|last_note|not defined|No | The most recent Note added about this member|
|list_id|string|No | List ID|
|_links|array|No |A list of link types and descriptions for the API schema documents|


## removemember
Remove Member from list: Delete a member from a list. 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|list_id|string|yes|The unique id for the list|
|member_email|string|yes|The email address of the member to delete|

#### Output properties
None. 


## updatemember
Update member information: Update information for a specific list member 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|list_id|string|yes|The unique id for the list|
|member_email|string|yes|The unique email address of the member to update|
|updateMemberInListRequest| |yes|Json object to send in the body with the updated member information|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|id|string|No | The MD5 hash of the lowercase version of the list member’s email address|
|email_address|string|No | Email address for a subscriber|
|unique_email_id|string|No | An identifier for the address across all of MailChimp|
|email_type|string|No | Type of email this member asked to get (‘html’ or ‘text’).|
|status|string|No | Subscriber’s current status. Possible Values: subscribed, unsubscribed, cleaned, pending|
|merge_fields|not defined|No |An individual merge var and value for a member |
|interests|string|No | The key of this object’s properties is the ID of the interest in question|
|stats|not defined|No | Open and click rates for this subscriber|
|ip_signup|string|No |IP address the subscriber signed up from |
|timestamp_signup|string|No |Date and time the subscriber signed up for the list |
|ip_opt|string|No | The IP address the subscriber used to confirm their opt-in status|
|timestamp_opt|string|No | Date and time the subscribe confirmed their opt-in status|
|member_rating|integer|No | Star rating for this member, between 1 and 5|
|last_changed|string|No |Date and time the member’s info was last changed |
|language|string|No |If set/detected, the subscriber’s language |
|vip|boolean|No | VIP status for subscriber|
|email_client|string|No |The list member’s email client |
|location|not defined|No | Subscriber location information|
|last_note|not defined|No | The most recent Note added about this member|
|list_id|string|No | List ID|
|_links|array|No |A list of link types and descriptions for the API schema documents|


## OnMemberSubscribed
When a Member has been added to a list: Triggers a workflow when a new member has been added to a list 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|list_id|string|yes|The unique id for the list|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|members|array|No | An array of objects, each representing a specific list member|
|list_id|string|No | The list id|
|total_items|integer|No |The total number of items matching the query regardless of pagination |


## OnCreateList
When a new list is created: Triggers a workflow when a new list is created 

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|lists|array|No |An array of objects, each representing a list |
|total_items|integer|No |The total number of items matching the query regardless of pagination |


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
