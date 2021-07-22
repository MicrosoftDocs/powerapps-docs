---
title: "Controls collection (Client API reference)| MicrosoftDocs"
description: "Learn about how to access controls associated with columns."
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: d5f3c0c5-b267-42a8-82e8-8c4a1cda3752
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Controls collection (Client API reference)


Use the Controls collection to access controls associated with columns. 

Because each column may be represented more than one time on the page, the controls collection provides access to all controls representing that column. If the column is represented by only one control in the page, the length of this collection will be 1. When you use the control getName method, the name of the first control will be the same as the name of the column. The second instance of a control for that column will be **\<columnName>1**. The pattern **\<columnName>+N** will continue for each additional control added to the form for a specific column.

When a form displays a business process flow control in the header, additional controls will be added for each column that is displayed in the business process flow. These controls have a unique name like the following: **header\_process\_\<column name>**.

When performing actions on controls that are tied to a column, you should always consider that the control may be included on the page more than once and you should generally perform the same actions for each control for the column. You can do this by looping through the column controls collection and perform the actions on each control.

### Related topics

[Columns (Client API reference)](../attributes.md)




[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]