---
title: "Define alternate keys using Power Apps portal | MicrosoftDocs"
description: "Learn how to define alternate keys using Power Apps portal"
ms.custom: ""
ms.date: 05/31/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Define alternate keys using Power Apps portal

The [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) provides an easy way to view and create entity alternate keys with the Common Data Service.

The portal enables configuring the most common options, but certain options can only be set using solution explorer. <br />More information: 
- [Define alternate keys to reference records](define-alternate-keys-reference-records.md)
- [Define alternate keys using solution explorer](define-alternate-keys-solution-explorer.md)

## View alternate keys

1. From the [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Data** > **Entities** and select the entity that you want to view.
2. Select **Keys** to view a list of any alternate keys that are defined.

  > [!div class="mx-imgBorder"] 
	> ![View alternate keys](media/view-alternate-keys-portal.png)

## Create an alternate key

1. While [viewing alternate keys](#view-alternate-keys), select **Add key**.
2. Use the panel to set a **Display name** and choose the fields to use to create the alternate key.

    The **Name** field will be populated based on the display name.

    ![Example Alternate Key Definition](media/alternate-key-account-number-sic-code.png)

1. Select **Done** to close the panel.
2. Click **Save Entity** to create the alternate key.

> [!NOTE]
> The alternate key will not be immediately available. A system job is initiated when you save the entity to create database indexes to support the alternate key.

## Delete an alternate key

While [viewing alternate keys](#view-alternate-keys), select the key you want to delete and choose **Delete Key** from the command bar.

### See also

[Define alternate keys to reference records](define-alternate-keys-reference-records.md)<br />
[Define alternate keys using solution explorer](define-alternate-keys-solution-explorer.md)<br />
[Developer Documentation: Define alternate keys for an entity](/dynamics365/customer-engagement/developer/define-alternate-keys-entity)
