---
title: "getSelectedResults (Client API Reference)| MicrosoftDocs"
description: Includes description and supported parameters for the getSelectedResults method.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
ms.assetid: 4d025f92-db16-440c-9f82-e40d71e09862
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getSelectedResults (Client API Reference)


Use this method to get the currently selected result of the search control. The currently selected result also represents the result that is currently open. 

## Control types supported

knowledge base search control

## Syntax

```JavaScript
var kbSearchControl = formContext.getControl("<name>");
var kbSearchResult = kbSearchControl.getSelectedResults();
```

## Return Value 

**KBSearchResult**. The currently selected result.

## KBSearchResult properties

| **Property**        | **Type** | **Description**  |
|---------------------|----------|------------------|
| **answer**          | String   | The HTML markup containing the content of the article. You could pass this content to a custom action that could include it in an email to send to the customer. |
| **articleId**       | String   | The article ID that is used as an alternate key. You can use it to see if this article already exists in Microsoft Dataverse or not.|
| **articleUid**      | String   | The unique article ID. This value is used as an alternate key. This ID is needed to create a new KB record while associating an article if one doesn't exist already. |
| **attachmentCount** | Number   | Number of attachments in the article. |
| **createdOn**       | Date     | The date the article was created. This value will be in the current user’s time zone and format. You may want to use the age of the article in your business logic. |
| **expiredDate**     | Date     | The date the article was or will be expired. You can compare this date to the current data to determine whether the article has expired or not. The value uses the current user’s time zone and format.|
| **folderHref**      | String   | The link to the folder path of the article.|
| **href**            | String   | The direct link to the article.|
| **isAssociated**    | Boolean  | Indicates whether the article is associated with the parent record or not. You can check this value before associating the article with the current record using form scripts or in another process initiated by form scripts. |
| **lastModifiedOn**  | Date     | Date on which the article was last modified. This value will be in the current user’s time zone and format. |
| **publicUrl**       | String   | Support Portal URL of the article. If the Portal URL option is turned off, this will be blank. Use a custom action to include this in a link in the content of an email to send to a customer. |
| **published**       | Boolean  | Indicates whether the article is in published state. **True** if published; otherwise **False**. You should check whether the article is published before you send information about it to a customer. |
| **question**        | String   | The title of the article. If you’re going to reference the article in any business process, you can refer to it by name using this value.  |
| **rating**          | Number   | The rating of the article.  |
| **searchBlurb**     | String   | A short snippet of article content that contains the areas where the search query was hit. Use this to give a glimpse of article to the users in the search list and help them determine if this is the article they are looking for. |
| **serviceDeskUri**  | String   | Link to the article. Use this link to open the article.   |
| **timesViewed**     | Number   | The number of times an article is viewed on the portal by customers.  |


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]