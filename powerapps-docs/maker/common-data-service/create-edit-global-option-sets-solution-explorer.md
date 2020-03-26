---
title: "Create and edit global option sets for Common Data Service using solution explorer | MicrosoftDocs"
ms.custom: ""
ms.date: 05/26/2018
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
ms.author: "matp"
manager: "kvivek"
author: "Mattp123"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Create and edit global option sets for Common Data Service using solution explorer

Solution explorer provides one way to Create and edit global option sets for Common Data Service.

The [Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) enables configuring the most common options, but certain options can only be set using solution explorer. <br />More information: 
- [Create and edit global option sets for Common Data Service](create-edit-global-option-sets.md)
- [Create an option set](custom-picklists.md)

## Open solution explorer

Part of the name of any global option set you create is the customization prefix. This is set based on the solution publisher for the solution you’re working in. If you care about the customization prefix, make sure that you are working in an unmanaged solution where the customization prefix is the one you want for this global option set. More information: [Change the solution publisher prefix](change-solution-publisher-prefix.md) 

[!INCLUDE [cc_navigate-solution-from-powerapps-portal](../../includes/cc_navigate-solution-from-powerapps-portal.md)]

## View global option sets

With solution explorer open, under **Components** select **Option Sets**.

![View global option sets](media/view-global-option-sets-solution-explorer.png)

> [!NOTE]
> Some system global option sets are not customizable. These options may change with updates or new versions so we recommend you don’t use them unless you are certain that your requirements align with the way that Common Data Service uses these values.

## Create a global option set

> [!NOTE]
> You do not need to create a global option set before you use it within a custom field. When you create a new option set field you have the option to create a new global option set or use an existing one. See [Option set field options](create-edit-field-solution-explorer.md#option-set-field-options)

While viewing global option sets, click **New** to open a form to define the global option set.

![Create global option set](media/create-global-option-set-solution-explorer.png)

Type a **Display name** that will be visible to people with the system administrator or customizer role who will choose this global option set when defining new fields that use it. This name will not be visible to people using your apps.

A **Name** field value will be generated for you based on the **Display name** you enter. It will include the customization prefix for the Solution publisher in the context of the solution you are working in. You can change the generated portion of the **Name** field value before you save.

Type a **Description** for the global option set. 

> [!TIP]
> Use the **Description** to explain the purpose of this global option set. This value is not visible to users of the application, it is for other people with the system administrator or customizer role who may want to know why this particular global option set was created.

### Configure options

[!INCLUDE [cc_configure-option-set-options-solution-explorer](../../includes/cc_configure-option-set-options-solution-explorer.md)]

## Edit a global option set

While viewing global option sets, select the option set you want to edit to open the panel to edit it.

Except for changing the **Name** field value or the number **Value** assigned to an option, you can make any of the changes you can when creating the global option set.

> [!NOTE]
> You cannot edit an option set if it is part of a managed solution. To edit managed solution option sets, you will have to contact the solution owner.

[!INCLUDE [cc_remove-option-warning](../../includes/cc_remove-option-warning.md)]

## Delete a global option set

To delete a global option set, while viewing the list select the ![Delete command](media/delete.gif) command in the command bar.

> [!IMPORTANT]
> If the global option set has been used by a field, you will not be able to delete it until that field is deleted.
  
### See also
 
[Create and edit global option sets for Common Data Service](create-edit-global-option-sets.md)<br />
[Create an option set](custom-picklists.md)<br />
[Create and edit fields](create-edit-fields.md)<br />
[Developer documentation: Customize global option sets](/dynamics365/customer-engagement/developer/org-service/customize-global-option-sets)
