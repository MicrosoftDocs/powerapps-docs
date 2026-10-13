---
title: Reveal a masked Dataverse column value
description: Add reveal and hide controls to a canvas app so authorized users can view a masked Dataverse column value for a selected record.
author: yogeshgupta698
ms.author: yogupt
ms.topic: how-to
ms.custom: canvas
ms.date: 10/09/2026
ms.subservice: canvas-maker
search.audienceType:
  - maker
ms.reviewer: joshuapa
ai-usage: ai-generated
contributors: joshuapartlow
---

# Reveal a masked Dataverse column value

Use [Dataverse.Unmask](/power-platform/power-fx/reference/function-dataverse-unmask) in a canvas app to let authorized users reveal a masked Microsoft Dataverse column value for a selected record. This walkthrough adds reveal and hide buttons to a gallery-based app. For example, a support agent can reveal a masked customer reference when their Dataverse permissions allow it.

Dataverse evaluates the current user's permissions. The buttons don't grant access or bypass column-level security, and revealing a value doesn't change the stored data or masking rule.

For syntax, argument requirements, return values, and error behavior, see the [Dataverse.Unmask function reference](/power-platform/power-fx/reference/function-dataverse-unmask).

## Prerequisites

- [Add the Dataverse table as a data source](connections/connection-common-data-service.md) in your canvas app.
- Enable column-level security on the column. To add a masking rule, use a managed environment and a column type that supports masking.
- Give the app user the required table and record access, column **Read** permission, and appropriate **Read unmasked** permission through a column security profile.

Have your administrator choose the appropriate permission for the scenario. Don't grant **Read unmasked: All records** solely to enable a single-record example. Test restrictions with a non-administrator account: column-level security doesn't hide data from system administrators.

For configuration and supported masking-rule types, see [Column-level security](/power-platform/admin/field-level-security) and [Create and manage masking rules](/power-platform/admin/create-manage-masking-rules). A column being secured doesn't, by itself, mean that it has a masking rule.

## Set up the gallery

This walkthrough uses an illustrative `Customers` Dataverse table with a secured text column named `'Sensitive reference'`. Replace these names with your app's table and column. Use synthetic data rather than actual sensitive values.

1. Open your canvas app for editing in Power Apps Studio.
2. [Add a gallery](add-gallery.md) named `Gallery1`, and set its **Items** property to `Customers`.
3. Configure the gallery to show a nonsensitive column that helps users identify a record.
4. Add a text label outside the gallery to show the selected record's reference.
5. Add two buttons outside the gallery, labeled **Reveal** and **Hide**.

Keep the gallery connected directly to the Dataverse table for this example. The selected record must retain its Dataverse identity; don't replace it with a manually constructed record.

## Configure reveal and hide

Set the text label's **Text** property to the following formula. It shows the ordinary value until the user selects **Reveal**, then requests the unmasked value and displays a message if the read fails.

```power-fx
If(
    locReveal,
    IfError(
        Dataverse.Unmask(Gallery1.Selected, 'Sensitive reference'),
        "Unable to show this value."
    ),
    Gallery1.Selected.'Sensitive reference'
)
```

The single quotes in `'Sensitive reference'` identify a column whose name contains a space. Don't replace them with double quotes, which create a text literal.

Configure the controls and screen as follows:

| Property | Formula |
| --- | --- |
| Reveal button **OnSelect** | `UpdateContext({locReveal: true})` |
| Hide button **OnSelect** | `UpdateContext({locReveal: false})` |
| Reveal button **DisplayMode** | `If(IsBlank(Gallery1.Selected), DisplayMode.Disabled, DisplayMode.Edit)` |
| Screen **OnVisible** and **OnHidden** | `UpdateContext({locReveal: false})` |
| Gallery **OnSelect** | `UpdateContext({locReveal: false})` |

Ensure gallery child controls select their parent item, for example by setting their **OnSelect** property to `Select(Parent)`. Reset `locReveal` in any other formula that changes the selection or gallery data. Add an appropriate loading indication for the asynchronous read.

> [!IMPORTANT]
> Hiding a control isn't an authorization boundary and doesn't purge cached values. Dataverse permissions remain the access control.

## Check the experience with test accounts

Use non-administrator accounts and synthetic records to check the app before sharing it.

1. Select a saved record in the gallery. Check that the label initially shows its ordinary masked reference.
2. With an account authorized to unmask the value, select **Reveal**. Check that the label shows the original reference for the selected record.
3. Select **Hide**. Check that the label returns to the ordinary value.
4. Reveal a value, then select another gallery item or leave and return to the screen. Check that the reveal state resets and that a previous record's original value isn't displayed for another record.
5. Test an account without permission to unmask the value. Check that the original value isn't disclosed. Don't assume every denied read produces the same error response.

The example uses [IfError](/power-platform/power-fx/reference/function-iferror) to display a message when a read fails. If the label is blank, check the selected record, its value, and the user's access. A blank result alone doesn't identify a permission problem. For details, see the [function reference](/power-platform/power-fx/reference/function-dataverse-unmask).

## Handle sensitive data safely

Repeated reads might reuse cached results rather than make new network requests. Don't rely on hiding a label to clear cached data or on a repeated formula evaluation to recheck recently changed permissions.

Don't persist unmasked values with `SaveData`, write them to logs, or copy them to a less-protected data source. Avoid using unmasked data in screenshots or diagnostic attachments.

## Related information

- [Connect to Microsoft Dataverse](connections/connection-common-data-service.md)
- [Dataverse.Unmask function](/power-platform/power-fx/reference/function-dataverse-unmask)
- [Column-level security](/power-platform/admin/field-level-security)
- [Create and manage masking rules](/power-platform/admin/create-manage-masking-rules)
- [Power Fx formula reference](/power-platform/power-fx/formula-reference)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
