---
title: "Add form navigation for related entities in PowerApps | MicrosoftDocs"
descriptoin: Learn how to add form navigation for related entities
ms.custom: ""
ms.date: 03/30/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Mattp123"
ms.assetid: b4098c96-bce1-4f57-804f-8694e6254e81
caps.latest.revision: 15
ms.author: "matp"
manager: "kvivek"
---
# Add form navigation for related entities

[!INCLUDE [cc-applies-to-powerapps-and-update-9-0-0]../../includes/cc-applies-to-powerapps-and-update-9-0-0.md)]

In the form Navigation Pane, you can add links to related entities. When a user clicks one of these links in a record, the associated view for the entity is displayed.  
  
  
1.  Open solution explorer.  
  
2.  Under **Components**, expand **Entities**, expand the entity you want to work with, and then choose **Forms**.  
  
3.  In the list, locate an entry with the form type of Main, and then double-click or tap to edit it.  
  
4.  To add a link to a related entity, on **Home** tab, in the **Select** group, choose **Navigation**.  
  
     The **Relationship Explorer** pane displays on the right side of the form editor.  
  
5.  In the **Relationship Explorer** pane, in the **Filter** list, select one of the following options:  
  
    - **Available Relationships**. Lists all the entities that can be related to the entity the form is associated with.  
  
    - **1:N Relationships**. Lists entities that can be related in a 1:N relationship to the entity the form is associated with.  
  
    - **N:N Relationships**. Lists entities that can be related in a N:N relationship to the entity the form is associated with.  
  
    > [!NOTE]
    >  If no related entities show up in the **Relationship Explorer** pane, you cannot create a link on this form to a related entity.  
  
6.  Select the related entity you want to link to, drag it to the Navigation Pane, and then drop it where you want it to be displayed.  
  
    > [!TIP]
    >  You can also create a new relationship by choosing **New 1:N** or **New N:N** in the **Relationship Explorer** pane. For more information, see [Create and edit entity relationships for Common Data Service for Apps](../customize/create-edit-entity-relationships.md)  
  
7. To edit the properties for this or any other related entity link, in the Navigation Pane, select the link, and then on the **Home** tab, choose **Change Properties**.  
  
8. In the **Relationship Properties** dialog box, on the **Display** tab, type a new display label.  
  
9. On the **Name** tab, choose **Edit** to view or edit the details associated with the relationship record.  
  
10. Choose **OK**.  
  
11. Preview how the main form will appear and how events will function:  
  
    1.  On the **Home** tab, choose **Preview**, and then select **Create Form**, **Update Form**, or **Read-Only Form**.  
  
    2.  To close the **Preview** form, on the **File** menu, choose **Close**.  
  
12. When you finish editing the form, choose **Save and Close** to close the form.  
  
13. When your customizations are complete, publish them:  
  
    -   To publish customizations for only the component that you are currently editing, in the Navigation Pane, choose the entity you have been working on, and then choose **Publish**.  
  
    -   To publish customizations for all unpublished components at one time, in the Navigation Pane, choose **Entities**, and then on the command bar, choose **Publish All Customizations**.  
  
> [!NOTE]
> [!INCLUDE[cc_solution_recommendation]../../includes/cc-solution-recommendation.md)]  
  
### See also  
 [Create and edit entity relationships for Common Data Service for Apps](../customize/create-edit-entity-relationships.md)
