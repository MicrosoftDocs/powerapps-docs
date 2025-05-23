---
title: "Edit system table messages with Power Apps | MicrosoftDocs"
description: "Learn how to edit system table messages"
ms.custom: ""
ms.date: 11/02/2022
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 3ccbd8de-8d6f-4058-87f7-15463667cfc6
caps.latest.revision: 41
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Edit system table messages (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The default display name of some system tables, such as account and contact tables, is used in user interface text and error messages in Microsoft Dataverse. If you change the display name for a system table, you should also update any messages that use the default display name. For example, if you change the display name from *Account* to *Company*, you could still see an error message using the old name.

> [!IMPORTANT]
> This is a preview feature. More information: [Model-driven apps and app management](../powerapps-preview-program.md#model-driven-apps-and-app-management)

## Add a message to a system table

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) (make.powerapps.com).
1. Go to **Solutions**, open the solution that has the table you want, and then open the table. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. In the **Customizations** area, select **Messages**.
   :::image type="content" source="media/open-messages-area.png" alt-text="Table messages area":::
1. Select the message you want, and then select **Add**.

## Edit a system table message

1. Open the table that has the message you want to edit, and then in the **Customizations** area select **Messages**.
1. Select the message, and then select **Edit** on the command bar. Enter the changes you want:   
   :::image type="content" source="media/edit-table-message.png" alt-text="Edit a system table message":::

   |Field|Description|  
   |-----------|-----------------|  
   |**Default display text**|Shows the original text, which isn't editable.|  
   |**Custom display text**|Edit this text to change the message that is displayed.|  
   |**Comment**|Optional. Include a comment about what you changed and why.|  

1. Select **Done**.

## Programmatically update table display strings

For developers looking for a way to work with these in code, the display strings are stored in the [DisplayString](../../developer/data-platform/reference/entities/displaystring.md) table. 

The `DisplayString` table doesn’t contain the default display strings. The two attributes for this table that contain text are [CustomDisplayString](../../developer/data-platform/reference/entities/displaystring.md#BKMK_CustomDisplayString) and [PublishedDisplayString](../../developer/data-platform/reference/entities/displaystring.md#BKMK_PublishedDisplayString). By default, these attribute values are null unless the display string has been customized and published. The `PublishedDisplayString` value is read-only and reflects the currently published `CustomDisplayString`.

## Edit using the classic experience

For information about how to edit system table messages using the classic experience, see [Edit system entity messages and display names](/dynamics365/customerengagement/on-premises/customize/edit-system-entity-messages).

## See also

[Edit a table](edit-entities.md)<br />
[Translate localizable text for model-driven apps](../model-driven-apps/translate-localizable-text.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
