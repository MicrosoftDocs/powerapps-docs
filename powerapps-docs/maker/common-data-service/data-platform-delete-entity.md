---
title: Delete an entity | Microsoft Docs
description: Step-by-step instructions for how to delete a custom entity and clear all data in Power Apps
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.component: cds
ms.topic: conceptual
ms.date: 06/29/2020
ms.author: lanced
ms.reviewer: matp
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Delete an entity
You can delete custom entities, but you can't delete standard entities. Notice that you can't delete a custom entity while it has one or more dependent components. More information: [Delete an entity that has dependencies](#delete-an-entity-that-has-dependencies)

> [!WARNING]
> When you delete an entity, you delete both the entity definition and all data that the entity contains. Entities and the data within them can't be recovered if deleted.

## Delete a custom entity
1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), select **Solutions** in the left navigation pane, open the solution that contains the custom entity you want to delete, and then select it.

    ![Entity Details](./media/data-platform-cds-create-entity/entitylist.png "Entity List")

2. On the command bar select **Remove**, and then select from the following choices:  
   - **Remove from this solution**. Removes the entity from the solution. You can still access the entity from the Default Solution. 
   - **Delete from this environment**. Deletes the entity and associated data. 

3. In the dialog box that appears, select **Delete** to delete the entity. If you receive a message that the *component cannot be deleted because it is referenced by other components*, see the next section in this article. 

## Delete an entity that has dependencies
You can’t delete an entity while it has a dependency on another component, such as a business process flow or a model-driven app. 

There are two ways that you can remove a dependency: 
- Reconfigure the component to remove the dependency. 
- Delete the component. 

### Remove a dependency
To find the dependencies for a component, see [View dependencies for a component](view-component-dependencies.md). 

Next, remove the component. For example, if you have a business process flow that references an entity you want to delete, edit the business process flow to remove that entity. Once the business process flow no longer references that entity, the entity will no longer appear in the show dependencies list and can be deleted. More information: [Delete a custom entity](#delete-a-custom-entity)   

> [!IMPORTANT]
> Removing the dependency, can cause the component to no longer work. For example, removing an entity from a model-driven app may cause the model-driven app to no longer work. 

For more information, see these articles: 
- [Edit or remove artifacts](../model-driven-apps/add-edit-app-components.md#edit-or-remove-artifacts)
- [Edit a business process flow](/power-automate/create-business-process-flow#edit-a-business-process-flow)
- [Delete relationships](create-edit-1n-relationships-portal.md#delete-relationships)
