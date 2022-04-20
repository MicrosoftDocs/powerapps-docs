---
title: "Tutorial: How to add a rich text component to a basic form"
description: Walk-through example steps for adding a rich text component to a basic form in Power Apps portals.
author: GitanjaliSingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/06/2022
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
  - nickdoelman
  - GitanjaliSingh33msft

---

# Tutorial: Configure the rich text editor control on portals 

In this tutorial, you'll configure Power Apps portals to add the [rich text editor control](../model-driven-apps/rich-text-editor-control.md) to a basic form and then add the basic form to a webpage. Portal users will be able interact with the rich text editor control to format text on the form.

## Prerequisites

Your portal version must be [9.4.3.x](/power-platform/released-versions/portals) or later.<!--note from editor: "Or later" is via Writing Style Guide.-->

## Step 1. Add the rich text editor control to a field in a model-driven app
<!--note from editor: I'm not sure why it's "field" above and "table" below. Will the reader know the difference?-->
Follow the steps in the tutorial [Add or replace a text column for rich text editing](../model-driven-apps/rich-text-editor-control.md#add-or-replace-a-text-column-for-rich-text-editing) to add the component to a table on a model-driven form.

> [!NOTE]
> To display the data as rich text, you might have to increase the character size of the text fields to accommodate the extra information.

## Step 2. Verify that the model-driven app uses the new control
<!--note from editor: Edit okay? "With" is a bit ambiguous here.-->
You can [update an existing model-driven app](../model-driven-apps/design-custom-business-apps-using-app-designer.md) or [create a new app](../model-driven-apps/build-first-model-driven-app.md) with the form to which you added the component. For example, the following image shows the feedback table **simple contact us form** using the rich text editor control in a model-driven app.

:::image type="content" source="media/component-rte-tutorial/rich-text-editor-mda.png" alt-text="Rich text editor for a feedback table.":::

## Step 3. Add a rich text editor control to a basic form in portals

In this step, you'll create a new basic form in portals and then add the control to the basic form. You can also use an existing basic form.

### Step 3.1. Create a new basic form

1. Open the [Portal Management app](/configure/configure-portal.md).

1. On the left pane under **Content**, select **Basic Forms**.

1. Select **New**.

1. Enter a **Name** for the form. In this example, we use **Feedback basic form with RTE**<!--note from editor: Bold is the primary way to indicate user input or anything you select in a UI. Italics are actually kind of rare (new terms, variable names, book titles, game names, song titles, and "sparingly for emphasis"), I think because they're seen as being hard to read online.-->.

1. For **Table Name**, select **Feedback (feedback)**.

1. Select the name of the model-driven app form to which you added the rich text control. In this example, **simple contact us form**.

1. Select your portal website.

    :::image type="content" source="media/component-rte-tutorial/basic-form.png" alt-text="Basic form configuration.":::

1. Select **Save & Close**.

### Step 3.2. Add the rich text editor control to the basic form

1. Open the [Portal Management app](/configure/configure-portal.md).

1. On the left pane under **Content**, select **Basic Forms**.

1. Select the basic form you created in step 3.1.

1. Select the **Basic Form Metadata** tab.

1. Select **New Basic Form Metadata**.

1. For **Type**, select **Attribute**.

1. For the **Attribute Logical Name**, select the name of the column for which the rich text control is enabled. In this example, **Comments (comments)**.

    :::image type="content" source="media/component-rte-tutorial/basic-form-metadata.png" alt-text="Basic form metadata configuration.":::

1. Enter a value for **Label**. In this example, **Comments**.

1. For **Control Style**, select **Code component**.

    :::image type="content" source="media/component-rte-tutorial/basic-form-metadata-controlstyle.png" alt-text="Basic form metadata configuration setting the control style to 'code component'.":::

1. Select **Save & Close**.

### Step 3.3. Add table permissions for the rich text attachment table

For using and storing images in the rich text editor on the portal, you'll need to add [table permissions](configure/entity-permissions-studio.md) to the rich text attachment table (msdyn_richtextfile).

1. Open your portal in [Power Apps portals Studio](portal-designer-anatomy.md).

1. On the left pane, choose **Settings** (gear icon) and select **Table Permissions**

    :::image type="content" source="media/component-rte-tutorial/table-permissions.png" alt-text="Selecting table permissions.":::

1. Create a new table permission for the rich text attachment table. The name can be anything you choose; in this example, we use **RTE Attachment**.

1. For **Access type**, select **Global access**.

    > [!NOTE]
    > The **Global access** type is chosen because no relationship exists<!--note from editor: Suggested, to avoid "there is." (Which is via Writing Style Guide.)--> between the table configured to use the rich text editor control and the rich text attachment table.

1. Under **Permission to**, select the **Read**, **Write**, **Create**, and **Delete** checkboxes.
 
1. Assign an appropriate [web role](configure/create-web-roles.md) to the table permission.

    :::image type="content" source="media/component-rte-tutorial/rich-text-table-permission.png" alt-text="Configuration of the rich text table permissions.":::

> [!IMPORTANT]
> If you want to store images as base 64 strings directly in the column that you've configured to use the rich text editor control, you need to configure the control by using a [JSON configuration file](../model-driven-apps/rich-text-editor-control.md#configure-the-rich-text-editor-control). Set **disableImages** and **disableDefaultImageProcessing** to **true** to allow images to be rendered consistently across all clients. Using this method doesn't require the global table permission on the rich text attachment (msdyn_richtextfile) table.

### Step 3.4. Add web API site setting

1. Open the [Portal Management app](configure/configure-portal.md). 

1. Go to **Site Settings**.

1. Create the following site settings: enter the name, your website,<!--note from editor: Will it be obvious to the reader where the name and website are to be entered? The table below doesn't seem to correspond to these steps.--> and the value of **true**, and then select **Save & Close**.

    | Site setting name | Value |
    | - | - | 
    | Webapi/msdyn_richtextfile/enabled | true |
    | Webapi/msdyn_richtextfile/fields | * |

## Step 4. Create a webpage in portals that uses the basic form
<!--note from editor: Edit okay? "Create a webage in portals with the basic form" implies that you use the form to create the webpage.-->
1. Open your portal in the [Power Apps portals Studio](portal-designer-anatomy.md).

1. In the upper-left corner, select **New page**.

1. Select the **Blank** layout.

1. On the right-side property pane, update the webpage name. For example, **Feedback**.

1. Update the **Partial URL**. For example, **feedback**.

1. Inside the page editor, below the **Header** section, select the **Column** section.

1. On the left pane, select Components (**+**).

1. Under **Portal components**, select **Form**.

1. On the right-side property pane, select **Use existing**.

1. Under **Name**, select the basic form that you created earlier in this tutorial. In this example, **Feedback basic form with RTE**.

    > [!TIP]
    > If you don't see the form, select **Sync Configuration** to synchronize changes from Dataverse.

1. Under **Permissions**, select **Manage table permissions** and make sure that you have the appropriate [table permissions](/configure/assign-entity-permissions.md) and [web roles](/configure/create-web-roles.md) configured for the Dataverse table associated to the form.
    
    > [!NOTE]
    > By default, the **feedback** table has **create** permissions configured for the default web roles. For more information, go to [Contact us sample](contact-us-sample.md).

1. In the upper-right corner, select **Browse website**.

    The webpage will now show the basic form for the feedback table with the rich text editor control, similar to how the form appears while the model-driven app is being used.<!--note from editor: Passive voice is necessary here, to fix the misplaced modifier.-->

    :::image type="content" source="media/component-rte-tutorial/basic-form-portal.png" alt-text="Basic form showing rich text component on a webpage.":::

## Rich text editor on a read-only form

On a read-only form, the rich text editor displays the content with formatting and images. The content can be read, but not edited or updated.<!--note from editor: Suggested.-->

### See also

[Power Apps component framework overview](../../developer/component-framework/overview.md) <br>
[Create your first component](../../developer/component-framework/implementing-controls-using-typescript.md) <br>
[Add code components to a field or table in model-driven apps](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md)

