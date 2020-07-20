---
title: Create a custom entity | Microsoft Docs
description: Learn how to create a custom entity in Power Apps.
author: Mattp123
ms.service: powerapps
ms.component: cds
ms.topic: quickstart
ms.date: 07/20/2020
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create a custom entity
In Power Apps, an *entity* defines information that you want to track in the form of records, which typically include properties such as company name, location, products, email, and phone. You can then surface that data by developing an app that refers to the entity. Power Apps offers standard "out-of-the-box" entities to cover typical scenarios within an organization (such as tracking appointments), but there may be times when you need to create custom entities to store data that's specific to your organization.

## Prerequisites
To create an entity, you must have either a System Administrator or System Customizer security role within Common Data Service.

## Sign in to Power Apps
Sign in to Power Apps at [https://make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

## Create an entity
1. In the navigation pane, expand **Data**, and then select **Entities**.

2. On the command bar, select **New entity**.

    Before you create an entity, check out the [entity reference](../../developer/common-data-service/reference/about-entity-reference.md) for a description of available standard entities. These entities cover typical scenarios. If one of these entities meets your requirements as is or after minor changes, you can save time by starting with that entity. 

3. In the **New entity** panel, enter the following information fields. Required fields are designated with an asterisk (*) next to the field label. 
    > [!div class="mx-imgBorder"] 
    > ![Create new entity](media/data-platform-cds-create-entity/newentitypanel.png)
    
    |Section  |Field  |Description  |
    |---------|---------|---------|
    |Required fields   | **Display name &#42;**      | This is the singular name for the entity that will be shown in the app. This can be changed later.     |
    |Required fields      |  **Plural display name &#42;**        | This is the plural name for the entity that will be shown in the app. This can be changed later.      |
    |Required fields     |  **Display Name &#42;** (Primary field)     | By default, every entity contains a Primary Field, which is used by lookup fields when establishing relationships with other entities. Typically the primary field stores the name or primary description of the data stored in the entity. You may update the name and display name of the primary field before saving the entity for the first time. Also, observe that the primary field also has its own **Name** box, which functions similarly to the entity name described above. The primary field name is autopopulated when a display name is entered, uses the same prefix as the entity, and cannot be changed after the entity is created.      |
    |Required fields      | **Name &#42;**    |  This field is pre-populated based on the **Primary Field Display name** you enter. It includes the customization prefix for the Common Data Service solution publisher. You cannot change this after the entity is saved. <br /> <br /> In order for the entity name to work with [Dynamics 365 for Customer Service embedded knowledge search](/dynamics365/customer-engagement/customer-service/set-up-knowledge-management-embedded-knowledge-search), the maximum entity name length including the publisher prefix can’t exceed 24 characters.         |
    | Required fields  | **Enable attachments**  | Adds the attachments control to the entity. The control is used to add or remove files and notes to records. Enabling this option lets users add files, such as document files from their computer or existing photos from a mobile device. Attached files can be up to 10 MB in size. Once this option is set, it can’t be changed after the entity is created.   |
    |**Description**     | **Description**      | Expand **More settings** > **Description**.  You can enter a description for your entity if you wish. Descriptions are helpful if other people will use this entity.     |
    |**Entity type and ownership**   |  **Choose entity type**    | Switch the entity type to **Activity Entity** to create entities that can manage tasks.      |
    |**Entity type and ownership**   |  **Ownership**     | The type of ownership defines who can perform operations on a record. **User or team** ownership allows the entity records to contain data that relates to customers, such as accounts or contacts. Security can be defined according to the business unit for the user or team.  **Organization** ownership entity records contain data involving something that belongs to or that can be viewed by the whole organization. *Organization-owned entity records can't be assigned or shared.*      |
    |**Collaboration**     |  **Allow feedback**     |  Let customers write feedback for any entity record, or rate entity records within a defined rating range. Once enabled this setting can't be disabled. More information: [Configure an entity for feedback/ratings](configure-entity-feedback.md)    |
    |**Collaboration**     | **Enable for activities**    | Associate activities to records for this entity.  Once enabled this setting can't be disabled.      |
    |**Collaboration**     | **Enable connections**    | Use the connections feature to show how records for this entity have connections to records of other entities that also have connections enabled. Once enabled this setting can't be disabled.    |
    |**Collaboration**     |  **Send email to entity**     | Send emails using an email address stored in one of the fields for this entity. If a **Single Line** of **Text field** with format set to email doesn’t already exist for this entity, a new one will be created when you enable sending email. Once enabled this setting can't be disabled.   |
    |**Collaboration**     | **Support mail merge**   | Allows people to use this entity with mail merge.     |
    |**Collaboration**     | **Enable SharePoint document management**  |  After other tasks have been performed to enable document management for your organization, enabling this feature allows for this entity to participate in integration with SharePoint.       |
    |**Collaboration**     | **Auto create access teams**     |  Create team templates for this entity.      |
    |**Collaboration**     |  **Enable queues**       | Use the entity with queues. Queues improve routing and sharing of work by making records for this entity available in a central place that everyone can access. Once enabled this setting can't be disabled.      |
    |**Create and update settings**     | **Enable quick create forms**     | After you have created and published a quick create form for this entity, people will have the option to create a new record using the **Create** button in the navigation pane. <br /> <br />When this is enabled for a custom activity entity, the custom activity will be visible in the group of activity entities when people use the **Create** button. However, because activities don’t support quick create forms, the main form will be used when the custom entity icon is selected.      |
    |**Create and update settings**     | **Duplicate detection**     | Enabling this allows you to create duplicate detection rules for this entity.     |
    |**Create and update settings**     |  **Enable change tracking**     | Enables data synchronization in a performant way by detecting what data has changed since the data was initially extracted or last synchronized.     |  
    | **Dynamics 365 for Outlook**  | **Enable offline capabilities**  | Enables record data for this entity to be available while the Dynamics 365 for Outlook application is not connected to the network.  |

4. Select  **Create**.
     
On the entity details page, observe that the entity is now being provisioned in the background. Once provisioning is completed, your entity will be saved and available for use in apps. Fields, relationships, and keys can be added to your entity at any time (even while provisioning is still in progress), but views, forms, charts, dashboards, and business rules can only be added to the entity after provisioning is completed.

## Next steps
In this article, you learned how to create a custom entity. Next, learn how to define relationships between entities.

> [!div class="nextstepaction"]
> [Create a relationship](data-platform-entity-lookup.md)

## Privacy notice
With the Microsoft Power Apps common data model, Microsoft collects and stores custom entity and field names in our diagnostic systems. We use this knowledge to improve the common data model for our customers. The entity and field names that app Creators create help us understand scenarios that are common across the Microsoft Power Apps community and ascertain gaps in the service’s standard entity coverage, such as schemas related to organizations. The data in the database tables associated with these entities is not accessed or used by Microsoft or replicated outside of the region in which the database is provisioned. Note, however, that the custom entity and field names may be replicated across regions and are deleted in accordance with our data retention policies. Microsoft is committed to your privacy as described further in our [Trust Center](https://www.microsoft.com/trustcenter/Privacy/default.aspx).
