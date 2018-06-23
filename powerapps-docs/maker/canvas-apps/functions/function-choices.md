---
title: Choices function | Microsoft Docs
description: Reference information, including syntax, for the Choices function in PowerApps
author: gregli-msft

ms.service: powerapps
ms.topic: reference
ms.component: canvas
ms.date: 06/15/2018
ms.author: gregli

---
# Choices function in PowerApps
Returns a table of the possible values for a lookup column.

## Description
The **Choices** function returns a table of the possible values for a lookup column.  

Use the **Choices** function to provide a list of choices for your user to select from. This function is commonly used with the [**Combo box**](../controls/control-combo-box.md) control in edit forms.

For a lookup, the table that **Choices** returns matches the foreign table that's associated with the lookup. By using **Choices**, you eliminate the need to add the foreign table as an additional data source. **Choices** returns all columns of the foreign table.

Because **Choices** returns a table, you can use [**Filter**](function-filter-lookup.md), [**Sort**](function-sort.md), [**AddColumns**](function-table-shaping.md), and all the other table-manipulation functions to filter, sort, and shape the table before using it. 

At this time, you can't [delegate](../delegation-overview.md) **Choices**. If this limitation poses a problem in your app, add the foreign entity as a data source, and use it directly. 

**Choices** doesn't require column names to be strings and enclosed in double quotes, unlike the [**ShowColumns**](function-table-shaping.md), [**Search**](function-filter-lookup.md), and other table functions. Provide the formula as if you were referencing the column directly.

Column references must be direct to the data source. For example, if the data source is **Accounts** and the lookup is **SLA**, the column reference would be **Accounts.SLA**. The reference can't pass through a function, a variable, or a control. Furthering this example, if **Accounts** is fed to a **Gallery** control, the SLA for the selected account can be referenced by the formula **Gallery.Selected.SLA**. However, this reference has passed through a control, so it can't be passed to the **Columns** function - **Accounts.SLA** must still be used.

At this time, only SharePoint and Common Data Service for Apps support lookup columns.

## Syntax
**Choices**( *column-reference* )

* *column-reference* – Required.  A lookup column of a data source. Don't enclose the column name in double quotes. The reference must be directly to the column of the data source and not pass through a function or a control.

## Examples

#### Choices for a lookup

1. [Create a database](../../../administrator/create-database.md) in Common Data Service for Apps, and select the **Include sample apps and data** box.

    Many entities, such as **Accounts**, are created:

	![A partial list of the fields from the Account entity in Commmon Data Service for Apps, highlighting that "Primary Contact" is a lookup field](media/function-choices/entity-account.png)

	The **Accounts** entity has a **Primary Contact** column, which is a lookup to the **Contacts** entity.  

	![A partial list of the fields from the Contact entity in the Commmon Data Service](media/function-choices/entity-contact.png)

	For each account, a contact is designated as the primary contact, or the primary contact is *blank*.

1. [Generate an app](../data-platform-create-app.md) from the **Accounts** entity in Common Data Service for Apps.

1. In the list of screens and controls near the left edge, select the **EditForm1** control (under the **EditScreen1** screen).

1. If it hasn't already been added, show the **Primary Contact** field in the form.

    The field appears at the end of the list of fields in the form, and you can move each field up or down in the form.

1. Within the card for **Primary Contact**, select the **Combo box** control.

    The **Items** property of that control is set to this formula:

	**Choices( Accounts.'Primary Contact' )**

	![A canvas screen with a form control. The **Combo box** control within the **Primary Contact** card is selected, and the Items property with the formula Choices( Accounts.'Primary Contact' ) appears](media/function-choices/accounts-primary-contact.png)

	If, in the app's advanced settings, the **Use column display names** check box is cleared, this formula appears as **Choices( Acccounts.primarycontactid )**.

1. To show what **Choices** is returning, add a screen.

1. Add a **Data table** control, and set its **Items** property to this formula:

	**Choices( Accounts.'Primary Contact' )**

1. In the **Data** pane, select **First Name**, **Last Name**, or any other fields that you want to show.

	![A canvas screen with a data table control. The Items property is set to the formula Choices( Accounts.'Primary Contact' ), and the table shows the firstname and lastname columns for the first set of records from the Contacts entity](media/function-choices/full-accounts-pc.png)