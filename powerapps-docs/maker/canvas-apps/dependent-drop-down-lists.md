---
title: Create a dependent drop-down list in a canvas app | Microsoft Docs
description: In PowerApps, create a drop-down list that filters another drop-down list in a canvas app.
author: emcoope-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 02/28/2019
ms.author: emcoope
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Create dependent drop-down lists in a canvas app

When you create dependent (or cascading) drop-down lists, users select an option in a list to filter options in a different list. Many organizations create such lists to help users fill out forms more efficiently. For example, users might select a country or region to filter a list of cities, or users might select a category to show only the codes in that category.

As a best practice, create a data source for the values in the "parent" (the list that filters the other list), and create another data source for the "child" (which users update by using the app). If you take this approach, you can use the same parent list in more than one app, and you can update the parent list without republishing the app. You can accomplish the same outcome by using a collection or static data, but it isn't recommended for enterprise scenarios.

For this topic, store employees submit issues to an **Incidents** list through a form. Employees specify not only the location at which the incident occurred but also the department within that location. Not all locations have the same departments, so a **Departments** list ensures that employees can't specify a department for a location that doesn't have that department.

This topic uses SharePoint lists as data sources, but all tabular data sources work the same way.

## Create data sources

The **Departments** list shows the departments at each location.

| Location | Department |
|----------------|------------------|
| Eganville      | Bakery           |
| Eganville      | Deli             |
| Eganville      | Produce          |
| Renfrew        | Bakery           |
| Renfrew        | Deli             |
| Renfrew        | Produce          |
| Renfrew        | Pharmacy         |
| Renfrew        | Floral           |
| Pembroke       | Bakery           |
| Pembroke       | Deli             |
| Pembroke       | Produce          |
| Pembroke       | Floral           |

The **Incidents** list shows contact information and information about each incident.

| First Name | Last Name | Phone Number     | Location | Department | Description       | Date      |
|------------|-----------|------------------|----------------|------------|-------------------------|-----------|
| Tonya       | Cortez   | (206) 555 - 1022 | Eganville      | Produce    | I had a problem with…   | 2/12/2019 |
| Moses     | Laflamme     | (425) 555 - 1044 | Renfrew        | Floral     | I experienced an issue… | 2/13/2019 |

1. In the **Incidents** list, select **PowerApps** > **Customize forms**.

    ![SharePoint list](./media/dependent-drop-down-lists/store_incidents_createform.png)

    A tab will open with the default form in PowerApps Studio:

    ![Default form in PowerApps](./media/dependent-drop-down-lists/default-form.png)

    > [!NOTE]
    > If your parent and child fields aren't **Drop down**, **Combo box**, or **List box** controls, you'll have to change the control type. This usually occurs when the type of column is of type Text or Choice. On the **Fields** pane, select the field to expand its information, and then set the control type to **Allowed Values**, which will change the input mechanism to a **Drop down** control.

    ![Allowed values](./media/dependent-drop-down-lists/field-type-allowed-values.png)

1. Add the **Departments** list as a data source.

    1. Select **View** > **Data Sources**.

    1. Select your existing SharePoint connection or create another one, select the **Departments** list, and then select **Connect**.

        ![Data pane](./media/dependent-drop-down-lists/sp-datapane.png)

        The form or app shows two SharePoint connections in the form or app. The form is connected to one, and you'll create the dependent drop-down list with the other.

        ![SharePoint data sources](./media/dependent-drop-down-lists/datasources.png)

1. By default, all the cards are locked. To create the dependent drop-down list, unlock the **Location** and **Department** data cards.

    To unlock a card, select it or a control within it, select the **Advanced** tab in the right-hand pane, and then select **Unlock**.

1. Rename the Location control to **ddLocation** and the Department control to **ddDepartment**.

    To rename a control, select it (not the data card), and edit the name at the top of the **Properties** tab of the right-hand pane.

    ![rename controls](./media/dependent-drop-down-lists/rename-control.png)

    If you rename your controls, you can identify them more easily, and the examples are easier to follow. To discover other best practices, review the Coding Standards and Guidelines whitepaper.

1. Test the app by pressing F5, selecting an option in  **ddLocation**, and confirming that **ddDepartment** shows the appropriate options. If the column in the SharePoint list is a choice field, Eganville, Renfrew, and Pembroke would correctly appear. If this column is a LookUp field to another list or table, the data may contain duplicate options. In that case, wrap a **Distinct** function around the **Items** property of this control, and ensure that the second part of the formula where I select which column to ensure there is only one option for, in this case, Store Location.

1. Select **ddDepartment** and then, on the **Properties** tab of the right-hand pane, select **Depends on.**

    ![depends on flyout](./media/dependent-drop-down-lists/dependson.png)

1. In the list just under **Parent control**, select **ddStoreLocation**, and then select **Value** in the list under that.

    The column name may change depending on the function that you used.

    - Select **Result** if you're evaluating expressions in the parent using **LookUp** or **Distinct**.
    - Select **ID** if you don’t want to match on string but on the actual ID of the row of data.

1. Under **Matching field**, select **Departments**.

    Now the field in this data source that will match the one in the parent control is **Location. Select Store Location in the following drop down.

1. Select **Apply**.

The **Items** property of **ddDepartment** is set to a formula with the **Filter** function.

![dependent dropdown](./media/dependent-drop-down-lists/dddropdowns.gif)

## FAQ

**I can’t see any data: the sources are all blank or have the wrong data.**
Check that you are displaying the correct field for your control. This can be done selecting the Value property in the property pane for drop downs or by editing the field for combo boxes and ensuring that the primary text is the field you want to display.

![Change combo box](./media/dependent-drop-down-lists/combo-box-display-field.png)

![Change drop down](./media/dependent-drop-down-lists/drop-down-display-field.png)

**I am seeing multiple, repeated items in my child dropdown.**
This is likely due to using a LookUp column or a Choices function. This is easily solved by wrapping a Distinct function around the properly returning Data. See more on the Distinct function.

## Known limitations

This configuration is only available on **Drop down**, **Combo box**, and **List box** controls that are single select. Multi-select isn't supported at this time. We plan to extend the same type of functionality to galleries. This isn't the recommended experience for working with option sets in CDS. There is more documentation on the way on using option sets in canvas apps.

The Depends On configuration doesn't support static data or collections. To configure with these sources, use the formula bar to edit the expression directly. Additionally, using two choice fields in SharePoint without any matching table of data isn't supported, and defining the Matching within this UI isn't possible.