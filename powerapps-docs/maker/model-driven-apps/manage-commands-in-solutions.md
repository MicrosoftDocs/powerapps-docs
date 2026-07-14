---
title: "Manage commands in solutions | MicrosoftDocs"
description: "Modern commands can be managed in solutions."
Keywords: command bar, command designer
author: caburk
ms.author: caburk
ms.reviewer: matp
ms.date: 05/26/2022
ms.subservice: mda-maker
ms.topic: article
search.audienceType: 
  - maker
---

# Manage commands in solutions

Unlike classic commands, modern commands are treated the same as other solution objects and support core solution behaviors. You can also edit existing modern commands from within a solution.

To add commands to a solution, you add the solution objects that depend on your command actions:

- Modern commands are a table component. When you add a command to a solution, you must add the command component. In this screenshot there's one JavaScript and one Power Fx command for the custom Classroom table that can be added as a specific object to a solution for export.
   :::image type="content" source="media/commanddesigner-add-to-solution.png" alt-text="Add a command table component to a solution":::
- Power Fx commands use a Dataverse component library. Add the component library to your solution if you plan to export it.
- JavaScript commands use a web resource. Add the web resource that includes the underlying JavaScript to run your command to the solution if you plan to export it.

More information: [Add an existing component to a solution](../data-platform/create-solution.md#add-an-existing-object-to-a-solution)

Modern commanding provides these benefits when you work with solutions:

- Block commands from being customized by using managed properties. Open the table, select **Commands**, select the command, and then on the command bar select **Advanced** > **Managed properties** to disable **Allow customizations**.
- View dependencies related to your modern command components. More information: [View dependencies for a component in Power Apps](../data-platform/view-component-dependencies.md)
- Troubleshoot by viewing which solutions modified the component and when using solution layers. More information: [Solution layers](../data-platform/solution-layers.md)
- Remove any unmanaged customizations if in an unhealthy state. More information: [Remove an unmanaged layer](../data-platform/solution-layers.md#remove-an-unmanaged-layer)
- Segment solutions and build minor updates or patches that include your modern command components.
- Modern command components work with solution upgrade so you can delete components by importing a new version. [Upgrade or update a solution](../data-platform/update-solutions.md)
- Standardized localization via export/import translations. More information: [Translate label text](../data-platform/translate-entity-label-text.md)

## Related articles

[Modern commanding overview](command-designer-overview.md)

[Solutions overview](../data-platform/solutions-overview.md)
