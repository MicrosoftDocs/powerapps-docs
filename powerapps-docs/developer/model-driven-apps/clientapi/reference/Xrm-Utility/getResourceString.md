---
title: "getResourceString (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: d5e51eac-ce0a-4f4a-b7b6-495433e3f8c1
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# getResourceString (Client API reference)



[!INCLUDE[./includes/getResourceString-description.md](./includes/getResourceString-description.md)] 

## Syntax

`Xrm.Utility.getResourceString(webResourceName,key)` 

## Parameters

|Name |Type |Required |Description |
|---|---|---|---|
|webResourceName|String|Yes|The name of the web resource.|
|key|String|Yes|The key for the localized string.|

## Return value

A localized string.

## Remarks

<!-- 
Content adapted from /developer/resx-web-resources 
If you change this, make sure that topic is in sync.
-->

When you create RESX web resources you must explicitly set the language value and include the locale identifier (LCID) for the appropriate language in the name of the web resource. For example, `new_/strings/MyAppResources.1033.resx` would contain resources for English language. See [Microsoft Locale ID Values](https://msdn.microsoft.com/library/ms912047(WinEmbedded.10).aspx) for a list of LCID values.

For example `Xrm.Utility.getResourceString("new_/strings/MyAppResources","hello")` will return the localized string value for the resource key `hello` within the `new_/strings/MyAppResources.1033.resx` web resource if the user’s preferred language is English. Notice that the function doesn’t refer to any specific language or full name of any RESX web resource. This functionality depends on the RESX web resource being associated to the calling JavaScript web resource as a dependency. More information: [Web resource dependencies](../../../web-resource-dependencies.md).

The appropriate string value will be determined by the individual user’s language preference and the languages available in the organization. If a localized string is not found that matches the user’s language preference, the localized string will automatically fallback to the base language for the organization. If no matching localized string is found for the organizations base language, a null value will be returned.

### Related topics

[Xrm.Utility](../xrm-utility.md)<br />
[String (RESX) web resources](../../../resx-web-resources.md)<br />
[Web resource dependencies](../../../web-resource-dependencies.md)



