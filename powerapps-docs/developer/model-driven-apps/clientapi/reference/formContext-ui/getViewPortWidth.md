---
title: "getViewPortWidth (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getViewPortWidth method.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# getViewPortWidth (Client API reference)



[!INCLUDE[./includes/getViewPortWidth-description.md](./includes/getViewPortWidth-description.md)]

The viewport is the area of the page containing form data. It corresponds to the body of the form and does not include the navigation, header, footer or form assistant areas of the page.

## Syntax

`formContext.ui.getViewPortWidth();`

## Return Value

**Type**: Number

**Description**: The viewport width in pixels. 


### Related topics

[getViewPortHeight](getViewPortHeight.md)

[formContext.ui](../formContext-ui.md)

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]