---
title: "View dependencies for a component in Power Apps | MicrosoftDocs"
description: "Understand how to view dependencies for a component in Power Apps and take action."
ms.custom: ""
ms.date: 03/25/2024
ms.reviewer: ""
ms.topic: "article"
author: "swatimadhukargit"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "swatim"
search.audienceType: 
  - maker
---
# View dependencies for a component in Power Apps

Solution components in Microsoft Dataverse often depend on other solution components. You can’t delete any solution component that has dependencies from another solution component. For example, you can't delete a model-driven app site map component without first deleting the model-driven app component, or removing the dependency, because the site map depends on the model-driven app.

You can view the dependent components from the **Solutions** area of Power Apps.

## Show dependencies

The show dependencies page for a component helps identify the dependencies so you can take appropriate action.

This section describes the actions you can take while viewing the dependencies in the **Show dependencies** menu under **Advanced**.

### Dependencies page contents

The **Dependencies** page displays details about all the components that have a dependency on the solution component. They're grouped by the solution's name.

The **Dependencies** page has tabs covering reports for **Delete blocked by**, **Used by**, and **Uses**:

- **Delete blocked by**: The report lists all the dependencies that block the delete of the solution component. Unless these dependencies are removed or the component is deleted, the solution component delete remains blocked.
- **Used by**: The report lists all the dependencies of other components that are using this solution component.
- **Uses**: This report lists all the dependencies that the given solution component uses.

#### Dependencies page actions

The **Dependencies** page has multiple actions you can take for each dependency. The actions can be used to inspect, delete the component, or remove a dependency with the listed dependencies.

To choose an action, select the vertical ellipsis next to any component and then select one of the following actions:

- **Open**: This action takes you to the particular component using the default solution. The open action helps you navigate to the component where you can inspect or edit it.
- **Delete**: This action allows you to delete the component. Ensure to use this action only if the component is no longer required and can be deleted. This action is available only for unmanaged components.
- **Remove dependency**: This action allows you to remove the dependency of the component on the solution component. The system attempts to edit the component to remove the dependency. In the event, when the system is unsuccessful in removing the dependency you might have to do a manual edit. This feature is currently available for the following components:
  - Entity's dependency on WebResource
  - SystemForm's dependency on Attribute and Role
  - AppModule's dependency on SavedQuery, SavedQueryVisualization, Entity, and SystemForm
- **Open documentation**: This action allows you to open documentation where you can learn about the dependencies for that component type.

You can also select a grouped solution and perform delete solution action:

**Delete Solution**: If you need to delete (uninstall) a solution that has dependencies on the solution component, use **Delete**. This action deletes the solution.

:::image type="content" source="media/solution-component-dependencies.png" alt-text="Solution component dependencies actions":::

### See also

[For developers: Detect solution dependencies](/power-platform/alm/solution-api#detect-solution-dependencies)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
