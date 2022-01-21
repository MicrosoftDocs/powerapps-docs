---
title: "Tutorial: How to add a rich text component to a basic form"
description: Walk through example steps for adding a rich text component to basic form in Power Apps portals.
author: GitanjaliSingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 01/20/2022
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
  - nickdoelman
  - GitanjaliSingh33msft

---

# Tutorial: Configure rich text editor control on portals (preview)

[This article is pre-release documentation and is subject to change.]

In this tutorial, you'll configure Power Apps portals to add the [rich text editor control](../model-driven-apps/rich-text-editor-control.md) to a basic form and then add the basic form to a web page. Portal users will be able interact with the rich text editor control on a web page.

## Prerequisites

Your portal version must be [9.4.1.x](/power-platform/released-versions/portals/portalupdate941x) or higher.

## Step 1. Add the rich text editor control to a field in a model-driven app

Follow the steps in the tutorial [Add or replace a text column for rich text editing](../model-driven-apps/rich-text-editor-control.md#add-or-replace-a-text-column-for-rich-text-editing) to add the component to a table on a model-driven form.

## Step 2. Verify the model-driven app with the new control

You can [update an existing model-driven app](../model-driven-apps/design-custom-business-apps-using-app-designer.md) or [create a new app](../model-driven-apps/build-first-model-driven-app.md) with the form to which you added the component. For example, the following image shows the feedback table main form using the rich text editor control.

:::image type="content" source="media/component-rte-tutorial/rich-text-editor-mda.png" alt-text="Rich text editor for feedback table.":::

## Step 3. Add a rich text editor control to a basic form in portals

In this step, you'll create a new basic form in portals and then add the control to the basic form. You can also use an existing basic form.

### Step 3.1. Create a new basic form

1. Open the [Portal Management app](/configure/configure-portal.md).

1. On the left pane, under **Content**, select **Basic Forms**.

1. Select **New**.

1. Enter a **Name** for the form. For example, *Feedback basic form with RTE*.

1. Select *Feedback (feedback)* as the **Table Name**.

1. Select the name of the model-driven app form that you added the rich text control. For example *Feedback*.

1. Select your portal website.

    :::image type="content" source="media/component-rte-tutorial/basic-form.png" alt-text="Basic form configuration.":::

1. Select Save & Close.

### Step 3.2. Add the rich text editor control to the basic form

1. Open Portal Management app.

1. On the left pane, under **Content**, select **Basic Forms**.

1. Select the basic form you created in the previous step.

1. Select the **Basic Form Metadata** tab.

1. Select **New Basic Form Metadata**.

1. Select *Attribute* as the **Type**.

1. Select the name of the column for which the rich text control is enabled as the Attribute Logical Name. For example, Comments (comments).

    :::image type="content" source="media/component-rte-tutorial/basic-form-metadata.png" alt-text="Basic form metadata configuration.":::

1. Enter a value for **Label**. For example, *Comments*.

1. For **Control Style**, select *Code component*.

    :::image type="content" source="media/component-rte-tutorial/basic-form-metadata-controlstyle.png" alt-text="Basic form metadata configuration setting the control style to 'code component'.":::

## Step 4. Create a webpage in portals with the basic form

1. Open your portal in the [Power Apps portals Studio](portal-designer-anatomy.md).

1. On the top-left corner, select **New page**.

1. Select the **Blank** layout.

1. On the right-side property pane, update the webpage name. For example, *Feedback*.

1. Update the **Partial URL**. For example, *feedback*.

1. Expand Permissions.

1. Disable Page available to everyone.

1. Select the web roles that should be allowed access to this page.

1. Inside the page editor, below the **Header** section, select the **Column** section.

1. On the left pane (toolbelt), select Components (**+**).

1. Under **Portal components**, select **Form**.

1. On the right-side property pane, select **Use existing**.

1. Under **Name**, select the basic form that you created earlier in this tutorial. For example, *Feedback basic form with RTE*.

    > [!TIP]
    > If you don't see the form, try **Sync Configuration** to synchronize changes from Dataverse.

1. On the top-right corner, select **Browse website**.

The web page will now show the basic form for the feedback table with the rich text editor control, similar to how it appears while using the model-driven app.

## Limitations

Image is added in the Dataverse table form where image upload is available, loading the same table form in portals using the rich text editor will not show the image.

### See also

[Power Apps component framework overview](../../developer/component-framework/overview.md) <br>
[Create your first component](../../developer/component-framework/implementing-controls-using-typescript.md) <br>
[Add code components to a field or table in model-driven apps](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md)

