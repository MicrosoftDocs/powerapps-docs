---
title: "getViewPortHeight (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the getViewPortHeight method.
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
# getViewPortHeight (Client API reference)



[!INCLUDE[./includes/getViewPortHeight-description.md](./includes/getViewPortHeight-description.md)]

The viewport is the area of the page containing form data. It corresponds to the body of the form and does not include the navigation, header, footer or form assistant areas of the page.

## Syntax

`formContext.ui.getViewPortHeight();`

## Return Value

**Type**: Number

**Description**: The viewport height in pixels. 


### Related topics

[getViewPortWidth](getViewPortWidth.md)

[formContext.ui](../formContext-ui.md)

[formContext](../../clientapi-form-context.md)



[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]