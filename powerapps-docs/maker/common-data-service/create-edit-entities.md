---
title: "Create and edit entities in Common Data Service | MicrosoftDocs"
description: "Learn how to create and edit entities"
ms.custom: ""
ms.date: 04/16/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
author: "Mattp123"
ms.assetid: fa04f99d-a5f9-48cb-8bfb-f0f50718ccee
caps.latest.revision: 41
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Create and edit entities in Common Data Service

Before you create a custom entity, evaluate whether using an existing entity will meet your requirements. More information: [Create new metadata or use existing metadata?](create-edit-metadata.md#create-new-metadata-or-use-existing-metadata)

There are two designers you can use to create an entity:

|Designer| Description|
|--|--|
|[Power Apps portal](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)|Provides an easy streamlined experience, but some special settings are not available.<br />More information: <br />[Tutorial: Create a custom entity that has components in Power Apps](/powerapps/maker/common-data-service/create-custom-entity)<br />[Create and edit entities using Power Apps portal](create-edit-entities-portal.md)|
|Solution explorer|Not as easy, but provides for more flexibility for less common requirements. <br />More information [Create and edit entities using solution explorer](create-edit-entities-solution-explorer.md)|

> [!NOTE]
> You can also create entities in your environment using the following:
> - Import a solution that contains the definition of the entity.
> - Use Power Query to create new entities and fill them with data. More information: [Add data to an entity in the Common Data Service by using Power Query](/powerapps/maker/common-data-service/data-platform-cds-newentity-pq).
> - A developer can use [Metadata services](/powerapps/developer/common-data-service/use-web-services#metadata-services) to write a program.

## Entity options not available in the Power Apps portal

Information in this topic will help you choose which designer you can use. You can use the Power Apps portal to create the entity unless you need to address any of the following requirements.

- Control the customization prefix

  Part of the name of any custom entity you create is the customization prefix. This is set based on the solution publisher for the solution you’re working in. If you care about the customization prefix, make sure that you are working in an unmanaged solution where the customization prefix is the one you want for this entity. More information [Change the solution publisher prefix](change-solution-publisher-prefix.md).

- Change the icons for a custom entity

  By default, all custom entities in the model-driven apps have the same icons. You can create image web resources for the icons you want for your custom entities. More information:  [Change icons for custom entities](../model-driven-apps/change-custom-entity-icons.md). 

- Change any of the following properties that can only be enabled:

  [!INCLUDE [cc_entity-set-once-options-table](../../includes/cc_entity-set-once-options-table.md)]

- Change any of the following properties:

  |Option   |Description  |
  |---------|---------|
  |**Areas that display this entity**|In the web application choose one of the available sitemap areas to display this entity. This does not apply to model-driven apps.|
  |**Auditing**|When auditing is enabled for your organization, this allows for changes to entity records to be captured over time. When you enable auditing for an entity, auditing is also enabled on all its fields. You can select or clear fields that you want to enable auditing on.|
  |**Color**|Set a color to be used for the entity in model-driven apps.|
  |**Document management**|After other tasks have been performed to enable document management for your organization, enabling this feature allows for this entity to participate in integration with SharePoint. |
  |**Enable for mobile**|Make this entity available to the Dynamics 365 for phones and tablets apps. You also have the option to make this entity **Read-only in mobile**.<br /><br /> If the forms for an entity require an extension not supported in Dynamics 365 for phones and tablets apps use this setting to ensure that mobile app users can’t edit the data for these entities.|
  |**Enable for phone express**|Make this entity available to the Dynamics 365 for phones app.|
  |**Reading pane in Dynamics 365 for Outlook**|Whether the entity will be visible in the reading pane for the Dynamics 365 for Outlook app.|
  |**Use custom Help**|When enabled, set a Help URL to control what page users will see when they click the help button in the application. Use this to provide guidance specific to your company processes for the entity.|


### See also

[Create and edit entities using solution explorer](create-edit-entities-solution-explorer.md)<br />
[Tutorial: Create a custom entity that has components in Power Apps](/powerapps/maker/common-data-service/create-custom-entity)<br />
[Edit an entity](edit-entities.md)<br />
[Developer Documentation: Create a custom entity](/dynamics365/customer-engagement/developer/org-service/create-custom-entity)
