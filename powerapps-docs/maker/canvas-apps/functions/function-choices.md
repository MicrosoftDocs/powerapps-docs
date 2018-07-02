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

Use the **Choices** function to provide a list of choices for your user to select from.  It is commonly used with the [**Combo box**](../controls/control-combo-box.md) control in edit forms.

For a lookup, the table returned by **Choices** is the same as the foreign table associated with the lookup.  Using **Choices** eliminates the need to add the foreign table as an additional data source.  All columns of the foreign table are returned by **Choices**.

Since **Choices** returns a table, you can use [**Filter**](function-filter-lookup.md), [**Sort**](function-sort.md), [**AddColumns**](function-table-shaping.md), and all the other table manipulation functions to filter, sort, and shape the table before using it. 

At this time, **Choicess** cannot be [delegated](../delegation-overview.md). If this poses a problem in your situation, add the foreign entity as a data source and use it directly.  

Unlike the [**ShowColumns**](function-table-shaping.md), [**Search**](function-filter-lookup.md), and other table functions that require column names to a string and enclosed in double quotes, this is not the case for **Choices**.  Provide the formula as if you were referencing the column directly.

Column references must be direct to the data source.  For example, if the data source is **Accounts** and the lookup is **SLA** then the column reference would be **Accounts.SLA**. The reference cannot pass through a function, variable, of control.  Furthering this example, if **Accounts** is fed to a **Gallery** control, then the SLA for the selected account can be referenced by the formula **Gallery.Selected.SLA**.  However, as this reference has passed through a control, it cannot be passed to the **Columns** function - **Accounts.SLA** must still be used.  

At this time, only SharePoint and the Common Data Service support lookup columns.

## Syntax
**Choices**( *column-reference* )

* *column-reference* – Required.  A lookup column of a data source.  Do not enclose the column name in double quotes.  The reference must be directly to the column of the data source and not pass through a function or control.

## Examples

#### Choices for a lookup

1. Create a [Common Data Service database](../../../administrator/create-database.md) and check the box to "Include sample apps and data".  Many entities will be created including the **Accounts** entity:

	![A partial list of the fields from the Account entity in the Commmon Data Service, highlighting that "Primay Contact" is a lookup field](media/function-choices/entity-account.png)

	The **Accounts** entity has a **Primary Contact** column which is a lookup to the **Contacts** entity.  

	![A partial list of the fields from the Contact entity in the Commmon Data Service](media/function-choices/entity-contact.png)

	For each each Account, there is a Contact designated as the Primary Contact.  It is also possible that the Primary Contact is *blank*.
 
2. [Generate an app from the Common Data Service](../data-platform-create-app.md) using the **Accouns** entity.

3. Select the **EditForm1** control in the **EditScreen1** screen from the left hand Screens pane.

8. If it has not already been added, add the **Primary Contact** field to the form.  It will appear at the end of the list of fields in the form, which you can move up or down in the form.

9. Select the **Combo box** control within the card for **Primary Contact**.  View the **Items** property which will contain the formula:

	**Choices( Accounts.'Primary Contact' )**

	![A canvas screen with a form control.  The combo box control within the Primary Contact data card is selected showing the Items property with the formula Choices( Accounts.'Primary Contact' )](media/function-choices/accounts-primary-contact.png)

	Note that if the "Use column display names" is turned off in the app's advanced settings that this formula will appear as **Choices( Acccounts.primarycontactid )**.

10. To see what **Choices** is returning, inert a new screen.

11. Add a **Data table** control and set its **Items** property to the formula:

	**Choices( Accounts.'Primary Contact' )**

11. In the Data pane, select "First Name", "Last Name", or any other fields that you would like to view.

	![A canvas screen with a data table control.  The items property is set to the formula Choices( Accounts.'Primary Contact' ) and the table is displaying the firstname and lastname columns for the first set of records from the Contacts entity](media/function-choices/full-accounts-pc.png) 



  

