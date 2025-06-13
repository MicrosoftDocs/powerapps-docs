---
title: "Add agent response using the form designer" 
description: Learn how to add the agent response component to model forms to call Copilot Studio topics.
ms.date: 06/16/2025
ms.reviewer: matp
ms.topic: how-to
author: adrianorth
ms.subservice: mda-maker
ms.author: aorth
search.audienceType: 
  - maker
---
# Add agents response use the form designer (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Agent Response component can be added to a model-driven app form which can directly call an Microsoft Copilot Studio (MCS) topic and display the response to the user. This builds on the Code Component Agent API executeEvent and simplifies usage by not requiring a new custom component.  The implicit context of the app, page, and record are available in MCS. 

<!-- TODO Replace the previous paragraph with the following after PR 11054 is merged. The link won't work.

Agent Response component can be added to a model-driven app form which can directly call an Microsoft Copilot Studio (MCS) topic and display the response to the user. This builds on the [Code Component Agent API executeEvent](developer/component-framework/bring-intelligence-using-agent-apis) and simplifies usage by not requiring a new custom component.  The implicit context of the app, page, and record are available in MCS. 

-->

This component supports the following responses from MCS:

* Markdown
* Adaptive card
* Image
* Video

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2216214), and are available before an official release so that customers can get early access and provide feedback.

## Add a agent response component using drag and drop

1. Open the form designer to create or edit a form. More information: [Create a form](create-and-edit-forms.md#create-a-form) or [Edit a form](create-and-edit-forms.md#edit-a-form)
1. In the form designer, select **Component** on the command bar.
1. In the Components pane, expand **Artificial Intelligence**
1. Drag the **Agent Response** onto the form preview.
   > [!div class="mx-imgBorder"]
   > ![Agent Response in components pane](media/form-designer-add-configure-agent-response/form-designer-components-agent-response.png "Agent Response in components pane")
1. In the **Add Agent Response** dialog, enter the Event Name from the MCS Topic.
   > [!div class="mx-imgBorder"]
   > ![Configure Agent Response Event Name](media/form-designer-add-configure-agent-response/form-designer-configure-agent-response.png "Configure Agent Response Event Name")
1. Select **Save and publish** on the command bar.
1. Open the form in a model-driven app to test the component. 

> [!NOTE]
> Form preview will display a warning message "Agent Response is only available when you play the app" since live preview is not yet supported. Save and publish the form and validate the component in a running app.

## Limitations

The following component properties are currently not supported:

- Label
- Hide label
- Hide on phone
- Lock
- Read-only
- Component width
- Component height
- Bind to table column

The component is not supported for mobile or tablets.

## See more

[Overview of the model-driven form designer](form-designer-overview.md)<br/>
[Add, configure, move, or delete components on a form](add-move-configure-or-delete-components-on-form.md)<br/>
[Using the tree view in the form designer](using-tree-view-on-form.md)
