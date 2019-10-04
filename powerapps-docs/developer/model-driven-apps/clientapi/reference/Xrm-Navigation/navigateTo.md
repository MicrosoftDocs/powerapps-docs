---
title: "navigateTo (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/4/2019
ms.service: powerapps
ms.topic: "reference"
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# navigateTo (Client API reference)



[!INCLUDE[./includes/navigateTo-description.md](./includes/navigateTo-description.md)]

## Syntax

`Xrm.Navigation.navigateTo(pageInput).then(successCallback,errorCallback);`

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|pageInput|Object|Yes|Input about the page to navigate to. The object contains the following attributes:<br/>- **pageType**: String. Specify "entitylist".<br/>- **entityName**: String. The logical name of the entity to load in the list control. <br/>- **viewId**: (Optional) String. The ID of the view to load.<br/>- **viewType**: (Optional) String. Specify "systemQuery" or "userQuery".|
|successCallback|function|No|A function to execute on successful navigation to page.|
|errorCallback|function|No|A function to execute when the operation fails.|


### Related topics

[Xrm.Navigation](../xrm-navigation.md)

