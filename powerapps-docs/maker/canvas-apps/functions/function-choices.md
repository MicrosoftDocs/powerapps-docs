---
title: Choices function | Microsoft Docs
description: Reference information, including syntax, for the Choices function in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 06/15/2018
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Choices function in PowerApps
Returns a table of the possible values for a lookup column.

## Description
The **Choices** function returns a table of the possible values for a lookup column.  

Use the **Choices** function to provide a list of choices for your user to select from. This function is commonly used with the [**Combo box**](../controls/control-combo-box.md) control in edit forms.

For a lookup, the table that **Choices** returns matches the foreign table that's associated with the lookup. By using **Choices**, you eliminate the need to add the foreign table as an additional data source. **Choices** returns all columns of the foreign table.

Because **Choices** returns a table, you can use [**Filter**](function-filter-lookup.md), [**Sort**](function-sort.md), [**AddColumns**](function-table-shaping.md), and all the other table-manipulation functions to filter, sort, and shape the table. 

At this time, you can't [delegate](../delegation-overview.md) **Choices**. If this limitation poses a problem in your app, add the foreign entity as a data source, and use it directly. 

**Choices** doesn't require column names to be strings and enclosed in double quotes, unlike the [**ShowColumns**](function-table-shaping.md), [**Search**](function-filter-lookup.md), and other table functions. Provide the formula as if you were referencing the column directly.

Column references must be direct to the data source. For example, if the data source is **Accounts** and the lookup is **SLA**, the column reference would be **Accounts.SLA**. The reference can't pass through a function, a variable, or a control. Furthering this example, if **Accounts** is fed to a **Gallery** control, use the formula **Gallery.Selected.SLA** to reference the SLA for the selected account. However, this reference has passed through a control, so it can't be passed to the **Columns** function - you must still use **Accounts.SLA**.

At this time, you can use lookup columns only with SharePoint and Common Data Service for Apps.

## Syntax
**Choices**( *column-reference* )

* *column-reference* – Required.  A lookup column of a data source. Don't enclose the column name in double quotes. The reference must be directly to the column of the data source and not pass through a function or a control.

## Examples

#### Choices for a lookup

1. [Create a database](../../../administrator/create-database.md) in Common Data Service for Apps, and select the **Include sample apps and data** box.

    Many entities, such as **Accounts**, are created.

    **Note**: Entity names are singular on web.powerapps.com and plural in PowerApps Studio.

	![A partial list of the fields from the Account entity in Commmon Data Service for Apps, highlighting that "Primary Contact" is a lookup field](media/function-choices/entity-account.png)

	The **Accounts** entity has a **Primary Contact** column, which is a lookup to the **Contacts** entity.  

	![A partial list of the fields from the Contact entity in the Commmon Data Service](media/function-choices/entity-contact.png)

	For each account, a contact is designated as the primary contact, or the primary contact is *blank*.

2. [Generate an app](../data-platform-create-app.md) from the **Accounts** entity.

3. In the list of screens and controls near the left edge, scroll down until **EditScreen1** appears, and then select **EditForm1** just under it.

	![In the left navigation bar, select EditForm1 on EditScreen1](media/function-choices/select-editform.png)

4. On the **Properties** tab of the right pane, select **Accounts**.

	![Select Accounts to open the Data pane](media/function-choices/open-data-pane.png)

5. In the **Data** pane, scroll down to the list of fields.

	![Select Accounts to open the Data pane](media/function-choices/field-list.png)

6. Find the **Primary Contact** check box, and then select it if it's cleared.

7. (optional) Drag the **Primary Contact** field from the bottom to the top of the list of fields.

8. In the card for **Primary Contact**, select the **Combo box** control.

    The **Items** property of that control is set to one of two formulas based on the state of the **Use column display names** check box in advanced settings.

   - If the check box is selected, the property is set to this formula:<br>**Choices( Accounts.'Primary Contact' )**
   - If the check box is cleared, the property is set to this formula:<br>**Choices( Accounts.primarycontactid )**

     ![A canvas screen with a form control. The **Combo box** control within the **Primary Contact** card is selected, and the Items property with the formula Choices( Accounts.'Primary Contact' ) appears](media/function-choices/accounts-primary-contact.png)

9. On the **Home** tab, select **New screen**, and then select **Blank**.

10. On the **Insert** tab, select **Data table**.

11. Set the **Items** property of the **Data table** control to one of these formulas:

     - If the **Use column display names** check box in advanced settings is selected, use this formula:<br>**Choices( Accounts.'Primary Contact' )**
     - Otherwise, use this formula:<br>**Choices( Accounts.primarycontactid )**

12. Open the **Data** pane, and then select the check boxes for **firstname**, **lastname**, or any other field that you want to show.

     ![A canvas screen with a data table control. The Items property is set to the formula Choices( Accounts.'Primary Contact' ), and the table shows the firstname and lastname columns for the first set of records from the Contacts entity](media/function-choices/full-accounts-pc.png)
