---
title: "OnLookupTagClick Event (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 02/11/2020
ms.service: powerapps
ms.topic: "reference"
ms.assetid: e291973b-9634-4442-995c-37fd49a10571
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# OnLookupTagClick Event (Client API reference)

This event occurs when the user clicks the tag in a lookup control. 

An execution context object is passed to event handlers for this event. You can use the [getEventArgs](../executioncontext/getEventArgs.md) method to retrieve an object that has the **getTagValue** method. 

The **getTagValue** method returns an object with the following properties:

- **name**. String. Name of the tag.
- **id**: String. ID of the tag.
- **entityType**. String. Entity type of the tag.
- **fieldName**. String. The originating lookup field that raised the event.

## Methods supported for this event
- [addOnLookupTagClick](../controls/addOnLookupTagClick.md) method to add event handlers for this event.
- [removeOnLookupTagClick](../controls/removeOnLookupTagClick.md) method to remove event handlers for this event. 



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]