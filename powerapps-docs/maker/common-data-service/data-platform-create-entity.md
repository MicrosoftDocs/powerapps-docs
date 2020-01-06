---
title: Create a custom entity | Microsoft Docs
description: Learn how to create a custom entity in Power Apps.
author: Mattp123
ms.service: powerapps
ms.component: cds
ms.topic: quickstart
ms.date: 12/23/2019
ms.author: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Create a custom entity
In Power Apps, an *entity* defines information that you want to track in the form of records, which typically include properties such as company name, location, products, email, and phone. You can then surface that data by developing an app that refers to the entity. Power Apps offers standard "out-of-the-box" entities to cover typical scenarios within an organization (such as tracking appointments), but there may be times when you need to create custom entities to store data that's specific to your organization.

In this topic, you'll learn how to create a custom entity called Product Review that you can use to create an app that displays ratings and comments for products that your company sells.

## Prerequisites
To follow this procedure, you must have either a System Administrator or System Customizer security role within Common Data Service.

## Sign in to Power Apps
Sign in to Power Apps at [https://make.powerapps.com](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).

## Create an entity
1. In the navigation pane, click or tap **Data** to expand it, and then click or tap **Entities**.

    ![List of entities and their details](./media/data-platform-cds-create-entity/entitylist.png "Entity List")

2. in the command bar, click or tap **New entity**.

    Before you create an entity, check out the [entity reference](../../developer/common-data-service/reference/about-entity-reference.md) for a description of available standard entities. These entities cover typical scenarios. If one of these entities meets your requirements as is or after minor changes, you can save time by starting with that entity. 

3. In the **New entity** panel, do the following:

    a. In the **Display name** box, enter **Product review**.

    Observe that the following boxes are autopopulated as you enter a display name:

    * **Plural display name** - This box is autopopulated when you enter a display name, but you can change it if needed. The plural display name is the name of the entity in the Common Data Service WebAPI and is used when interacting with this entity from Power Apps or Flow.
    * **Name** - This box is also autopopulated when you enter a display name. The prefix was set up when the environment was created and ensures that the entities you create can be exported and imported into other environments without conflicting with other entity names. You can change this prefix by updating the prefix on your Publisher for the Common Data Service Default Solution. To keep existing apps from breaking, you cannot change the name after saving the entity.

       > [!NOTE]
       > In order for the entity name to work with [Dynamics 365 for Customer Service embedded knowledge search](/dynamics365/customer-engagement/customer-service/set-up-knowledge-management-embedded-knowledge-search), the maximum entity name length including the publisher prefix can’t exceed 24 characters.

    b. In the **Primary Field** section, in the **Display name** box, replace **Name** with **Product Review**. 

    By default, every entity contains a **Primary Field**, which is used by lookup fields when establishing relationships with other entities. Typically the primary field stores the name or primary description of the data stored in the entity. You may update the name and display name of the primary field before saving the entity for the first time.

    Also, observe that the primary field also has its own **Name** box, which functions similarly to the entity name described above. The primary field name is autopopulated when a display name is entered, uses the same prefix as the entity, and cannot be changed after the entity is created.

    c. Open the **More settings** section and expand the **Description** accordion. You may enter a description for your entity if you wish (descriptions are helpful if other people will use this entity). 

    d. Select **Activity** entity option from the **Choose entity type** drop-down list to enable an entity as an activity.

    e. Ensure **Display in Activity menus** check box is selected. This option ensures the activity is made available in the activity menu.

      > [!Note]
      > Ensure to the **Display in Activity menus** option before you create the entity.

    f. Expand **Create and update settings** and select the **Enable quick create forms** check box. This option ensures, you can use the quick create form to crete a record.
    
    g. When you're done, click **Create**.
     
    ![New Entity](./media/data-platform-cds-create-entity/newentitypanel.png "New Entity Panel")

4. On the entity details page, observe that the entity is now being provisioned in the background. Once provisioning is completed, your entity will be saved and available for use in apps. Fields, relationships, and keys can be added to your entity at any time (even while provisioning is still in progress), but views, forms, charts, dashboards, and business rules can only be added to the entity after provisioning is completed.

    ![Entity Details](./media/data-platform-cds-create-entity/newentitydetails.png "New Entity Details")

5. Under the **Fields** tab, observe the **Primary Field** that you named in the previous step. Click or tap the **Primary Field** field to open the **Primary Field** panel if you would like to make any additional customizations to the field. Notice that the **Name** can no longer be changed, since the entity has already been saved.

5. To add a field to the entity, do the following:
 
    a. In the command bar, click or tap **Add field** to open the **Field properties** panel.

    b. In the **Display name** box, enter **Review Date**.

    c. From the **Data type** drop-down list, select **Date Only**.

    d. Click or tap the **Required** check box.
    
    e. Click or tap **Done**.
     
    For more information, see [Manage fields in an entity](data-platform-manage-fields.md).

    > [!div class="mx-imgBorder"] 
    > ![New Field](./media/data-platform-cds-create-entity/newfieldpanel-2.png "New Field Panel")

6. Repeat the previous step to add three more fields with the following configurations:
    * **Display name** = Product Rating; **Data type** = Whole Number; click or tap **Required** check box
    * **Display name** = Reviewer Name; **Data type** = Text
    * **Display name** = Reviewer Comment; **Data type** = Text

    When you're done, you should have five fields listed on your entity details page.

    ![Field list](./media/data-platform-cds-create-entity/addedfields.png "List of fields")

    Note that all entities have read-only system fields. By default, system fields are not shown in the list of fields even though they exist in the entity. To see all fields, change the filter on the command bar from **Default** to **All**. For more information on the metadata related to an entity, see [Entity metadata](../../developer/common-data-service/entity-metadata.md).

7. Click **Save Entity** to save the latest changes to your entity.

    The Product Review entity should appear in the list of entities in your database. If you don't see it, change the filter in the command bar from **Default** to **Custom**.

    > [!div class="mx-imgBorder"] 
    > ![Filter](./media/data-platform-cds-create-entity/filter.png "Filter selection")

## Next steps
In this topic, you learned how to create a custom entity called Product Review that can be used to create an app that displays ratings and comments for each product sold by a particular company. Next, learn how to define relationships between entities (in this case between the standard Product entity and your custom Product Review entity) so you can associate each product with the reviews and comments it receives.

> [!div class="nextstepaction"]
> [Create a relationship](data-platform-entity-lookup.md)

## Privacy notice
With the Microsoft Power Apps common data model, Microsoft collects and stores custom entity and field names in our diagnostic systems. We use this knowledge to improve the common data model for our customers. The entity and field names that app Creators create help us understand scenarios that are common across the Microsoft Power Apps community and ascertain gaps in the service’s standard entity coverage, such as schemas related to organizations. The data in the database tables associated with these entities is not accessed or used by Microsoft or replicated outside of the region in which the database is provisioned. Note, however, that the custom entity and field names may be replicated across regions and are deleted in accordance with our data retention policies. Microsoft is committed to your privacy as described further in our [Trust Center](https://www.microsoft.com/trustcenter/Privacy/default.aspx).
