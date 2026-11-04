---
title: Understand SharePoint forms integration
description: Understand the responsive SharePoint form template in Power Apps, its flexible canvas, and how to customize its layout and list-item actions.
author: NickWaggoner
ms.topic: concept-article
ms.custom: canvas
ms.reviewer: joshuapa
ms.date: 11/03/2026
ai-usage: ai-assisted
ms.subservice: canvas-maker
ms.author: joshuapa
search.audienceType: 
  - maker
contributors:
  - joshuapartlow
  - amchern
  - lancedMicrosoft
reviewer: joshuapartlow
---

# Understand SharePoint forms integration

You can [customize a form for a SharePoint list](/sharepoint/dev/business-apps/power-apps/get-started/create-your-first-custom-form) with Power Apps to create, view, and edit list items without leaving the list. The responsive template provides a title, description, and a form inside layout containers. Generated formulas and the **SharePointIntegration** control connect the form to list actions.

> [!NOTE]
> The previous template used a mobile-sized canvas with a single-column form. The new template uses the **Flexible** canvas type and a responsive layout that adapts to the available space. This article describes the responsive template where it's enabled for new form creation. Existing customized forms keep their current layout and aren't automatically converted.

## Create and customize the form

Open your list in SharePoint or Microsoft Lists to customize its form. When you create or view a list in SharePoint, you're automatically redirected to Microsoft Lists. The list is available in both places. For more information, see [What is a list in Microsoft 365?](https://support.microsoft.com/office/what-is-a-list-in-microsoft-365-93262a88-20ad-4edc-8410-b6909b2f59a5)

1. Open your list in SharePoint or Microsoft Lists.
1. Select **Integrate** > **Power Apps** > **Customize forms**.
1. In Power Apps Studio, expand the screen's containers in the tree view and select the nested form control, **SharePointForm1**.
1. Use **Edit fields** to choose and order the fields. Keep the form's **DataSource** bound to your list.
1. Select the title and description controls to customize their text. Preserve the containers' responsive sizing and the generated **SharePointIntegration** actions.
1. Save the form and publish it to SharePoint. Test creating, viewing, editing, saving, and canceling an item from the list.

## Understand the default generated form

The form is nested inside layout containers rather than placed directly on the screen. Expand the containers in the tree view to find the form and its data cards.

| Control | Purpose |
| --- | --- |
| **FormScreen1** | The [screen](controls/control-screen.md) that contains the responsive layout. |
| **FormScroll1** | The outer container that provides vertical scrolling. |
| **TitleBand1** | The container for the title and description. |
| **FormCardWrap1** | The card-style container around the form. |
| **SharePointForm1** | The [form](working-with-forms.md) that creates, shows, or edits a list item. Its data cards represent the list fields. |
| **SharePointIntegration** | The control that connects SharePoint list actions to the form. |

These are example generated names. If a name differs in your app or you rename a control, use its actual name in formulas. The following examples use **SharePointForm1** for the nested form.

### Keep the form connected to the list

The form's **DataSource** is the list you customize. Its **Item** formula uses the record selected in SharePoint, with the first list item as a fallback when no item is selected:

```power-fx
If(
    IsBlank(SharePointIntegration.Selected),
    First('YourListName'),
    SharePointIntegration.Selected
)
```

Replace `'YourListName'` with your list's data source name. The fallback lets you work with sample data in Studio. The **SharePointIntegration** actions set the form's mode when it runs in SharePoint.

### Column layout

The flexible canvas uses responsive sizing instead of scaling a fixed mobile layout. The form's **NumberOfColumns** formula uses the app's width:

```power-fx
If(App.Width < 640, 1, If(App.Width < 900, 2, 3))
```

| App width | Columns |
| --- | --- |
| Less than 640. | One. |
| 640 to less than 900. | Two. |
| 900 or more. | Three. |

These app-width breakpoints don't guarantee how many columns fit inside every SharePoint panel. Check the form in its actual host, not only in Studio.

Generated data cards use formulas based on **Parent.NumberOfColumns** for their position and width. Replacing those formulas with fixed values can stop fields from reflowing. Check long labels, multiline fields, required-field messages, and scrolling at each layout size. A responsive screen doesn't imply that every field uses a new modern input control.

Keep the generated responsive display settings and container formulas when you customize the layout. For more information about sizing formulas, see [Create responsive layouts in canvas apps](create-responsive-layout.md).

> [!NOTE]
> While you can manually copy a form from one environment to another, there's currently no automated method in Power Apps to copy a form from one environment to another.

## Understand the SharePointIntegration control

The **SharePointIntegration** control communicates user actions between SharePoint and Power Apps. The form's position inside containers doesn't change this integration.

:::image type="content" source="./media/sharepoint-form-integration/sharepointintegration-object.png" alt-text="Screenshot of a SharePoint integration object as seen in Power Apps.":::

> [!NOTE]
> You can access properties for the **SharePointIntegration** control only when the form runs in SharePoint, not when you're customizing the form in Power Apps Studio. These properties might not be available in **OnStart** or **OnVisible**.

### Default form actions

Preserve the generated actions so the nested form responds to the list's **New**, **View**, **Edit**, **Save**, and **Cancel** operations:

| Property | Action in SharePoint | Form formula |
| --- | --- | --- |
| **OnNew** | Open the **New** or **Create item** form. | `NewForm(SharePointForm1)` |
| **OnView** | Select an item or open its detail form. | `ViewForm(SharePointForm1)` |
| **OnEdit** | Select **Edit all** or open the **Edit item** form. | `EditForm(SharePointForm1)` |
| **OnSave** | Select **Save** to submit the changes. | `SubmitForm(SharePointForm1)` |
| **OnCancel** | Select **Cancel** to reset the changes. SharePoint hides the form automatically. | `ResetForm(SharePointForm1)` |

### Handle save results

The form's **OnSuccess** runs only after a successful submission. The responsive template resets the form and asks SharePoint to hide it:

```power-fx
ResetForm(Self); RequestHide()
```

`Self` refers to the form whose **OnSuccess** formula runs. Keep `RequestHide()` in **OnSuccess**, not before a save succeeds. Use **OnFailure** and the form's **Error** output to communicate failed saves. Don't hide the form as though the record was saved.

### Selected item properties

Use these properties to work with the list item that SharePoint opens:

| Property | Description |
| --- | --- |
| **Selected** | The selected record from the list. |
| **SelectedListItemID** | The ID of the selected list item. |
| **Data Source** | The list that contains the record. Changing this property can prevent **Selected** and **SelectedListItemID** from working. |

To copy the current record to a variable, see [Common issues with the SharePointIntegration object](#common-issues-with-the-sharepointintegration-object).

## Customize the default form

Customize the layout and formulas without breaking the connection between the nested form and SharePoint.

- Keep the form inside its layout containers. Change the title, description, and fields without replacing responsive sizing formulas with fixed values.
- Use the **OnSave** formula of **SharePointIntegration** to submit only the form in use. If you add multiple forms, set a variable in **OnNew**, **OnView**, and **OnEdit** to identify which form to submit.
- Include `RequestHide()` in each form's **OnSuccess** formula. Run important logic before `RequestHide()`, while the form is still visible and can run that logic.
- Reset your forms in **SharePointIntegration.OnCancel**. SharePoint controls hiding when the user selects **Cancel**.
- Use **OnNew**, **OnView**, or **OnEdit** for logic that must run before SharePoint shows the form. Don't rely on **OnStart** or **OnVisible** for list-item changes.

## Common issues with the SharePointIntegration object

The following guidance applies when the responsive form runs inside SharePoint.

### Read the current record

If a variable based on **SharePointIntegration.Selected** doesn't show the latest values, use **SelectedListItemID** to look up the record. For example, add this formula to **SharePointIntegration.OnView** along with the generated `ViewForm(SharePointForm1)` action:

```power-fx
ViewForm(SharePointForm1);
Set(
    selectedLookupItem,
    LookUp('YourListName', ID = SharePointIntegration.SelectedListItemID)
)
```

Replace `'YourListName'` with your list's data source name.

### Reset session state

Collection variables aren't reset when you close the form. The state persists for the entire session. If you need to reset a collection, clear it in **SharePointIntegration.OnView**.

### Avoid unexpected background actions

Don't use imperative functions such as `Launch()` in **SharePointIntegration** properties such as **OnNew** and **OnView**. These events can run in the background even when the form isn't visible.

## Understand user access to customized forms

You can't manually share a SharePoint form customized with Power Apps. Instead, any user who has at least **Read** or **Restricted View** access to the linked SharePoint list inherits access to the form. Users who have only been given permissions to specific items in the list don't have access to the customized form.

## Related information

- [Move SharePoint Custom Forms with Power Apps (white paper)](https://go.microsoft.com/fwlink/?linkid=2263521)
- [EditForm, NewForm, SubmitForm, ResetForm, and ViewForm functions](/power-platform/power-fx/reference/function-form)
- [RequestHide function](/power-platform/power-fx/reference/function-requesthide)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
