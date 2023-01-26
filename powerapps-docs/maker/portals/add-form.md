---
title: Add form
description: Learn how to add form component to a Power Apps portals page using portals Studio.
author: neerajnandwana-msft

ms.topic: conceptual
ms.custom: 
ms.date: 12/01/2022
ms.subservice: portals
ms.author: nenandw
ms.reviewer: kkendrick
contributors:
    - neerajnandwana-msft
    - nickdoelman
    - ProfessorKendrick
---

# Add form

[!INCLUDE [cc-portals-studio-ga-banner](../../includes/cc-portals-studio-ga-banner.md)]

Form is a data-driven configuration that collects data in the portal without the need for a developer to surface the form in the portal. 

Forms are [created in Microsoft Dataverse](../model-driven-apps/form-designer-overview.md). You can use them in webpages in the portal or in conjunction with lists to build out complete web applications.  

To add a form component:

1. [Edit the portal](manage-existing-portals.md#edit) to open it in Power Apps portals Studio.  

1. Select the page on which you want to add the component.

1. Select an editable element on the canvas.

1. Select **Components** ![components icon.](media/components-icon.png "Components icon") from the left side of the screen.  

1. Under **Portal components**, select **Form**.

1. In the properties pane on the right side of the screen, select one of the following options:

    - **Create new**: Create a new form.
    - **Use existing**: Use an existing form.

1. Enter information or make selection:

    - **Name**: Name of the form.

    - **Table**: The name of the table from which the form is loaded.

    - **Form layout**: The name of the form on the target table in Dataverse that is to be rendered.

    - **Mode**: Select one of the following options:

        - **Insert**: Indicates the form should insert a new record upon submission.

        - **Edit**: Indicates the form should edit an existing record.

        - **Read only**: Indicates the form should display an existing record's non-editable form.

        > [!NOTE]
        > The default option for **Edit** and **ReadOnly** modes is set as Query String Parameter Name passed as ID in URL. To change these values, you need to open Portal Management app and update the form properties.

    - **On success**: Select one of the following options:

        - **Show success message**: Requires a message to be displayed to the user on successful submission of the form. You can also select **Hide form on success** to hide the form upon successful submission.

        - **Redirect to webpage**: Redirects the user to the selected webpage in the portal. This field is required.

        - **Redirect to URL**: Redirects the user to the specified URL. This field is required.

    - **Show captcha for anonymous users**: Displays captcha to anonymous users.
    
    - **Show captcha for authenticated users**: Displays captcha to authenticated users.

    - **Permissions**: Table permissions to be considered for the form. [Configure table permissions](configure/entity-permissions-studio.md) to make the form available to anyone, or any specific roles.

        > [!div class=mx-imgBorder]
        > ![Form properties.](media/form-props.png "Form properties")

    > [!NOTE]
    > By default, permissions are applied to components containing data. Making it visible to anyone, or only to specific roles, is done by managing table permissions.

### See also

- [Power Apps portals Studio](portal-designer-anatomy.md)
- [Create and manage webpages](create-manage-webpages.md)
- [WYSIWYG editor](compose-page.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
