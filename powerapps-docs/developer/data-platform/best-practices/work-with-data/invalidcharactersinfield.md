---
title: "Manage invalid characters | Microsoft Docs"
description: Describes how to manage invalid characters.

ms.date: 08/09/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly"
ms.subservice: dataverse-developer
ms.author: "pehecke"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Manage invalid characters

There are a set of characters that cannot be saved in string or memo columns. When an application saves data containing these characters to Dataverse, the following error will occur:

Name: `InvalidCharactersInField`<br />
Hexadecimal error code : `80040278`<br />
Error Number: `-2147220872`<br />
Description: `The field '{0}' contains one or more invalid characters.`<br />

These characters are sometimes found in email content that includes replies or when text is copied from an another source which may have characters to control presentation.

Applications that work with data that can contain these characters should always HTML Encode the content before saving. 

### See Also

[Work with data using code in Dataverse (Power Apps)](../../work-with-data.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]

