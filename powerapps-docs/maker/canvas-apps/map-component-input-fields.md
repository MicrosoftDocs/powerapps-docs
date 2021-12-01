---
title: Map input fields of a component
description: Learn about how to map input fields of a component to the table or record.
author: hemantgaur
ms.service: powerapps
ms.subservice: canvas-developer
ms.topic: article
ms.date: 11/29/2021
ms.author: hemantg
ms.reviewer: tapanm
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - hemantgaur
  - tapanm-msft
  - gregli-msft
---

# Map input fields of a component

[This article is pre-release documentation and is subject to change.]

A component can receive input values to emit or process data using custom input properties. In this article, you'll learn about working with such components expecting one or more input properties with a specific schema for the given table or record, and how to map the component input fields to the columns of the data source.

> [!TIP]
> To learn about what the custom input and output properties in components are, see [Custom properties in components](create-component.md#custom-properties).

## Map columns

Use the [RenameColumns()](functions/function-table-shaping.md) function to rename one or more columns of a table
to match the input property schema for input column selection.

For example, consider a component that expects a table input with the following format:

| **Flavor** | **UnitPrice** | **QuantitySold** |
|------------|---------------|------------------|
| Strawberry | 1.99          | 20               |
| Chocolate      | 2.99          | 45               |

The input property expects table data type:

:::image type="content" source="media/map-component-input-fields/custom-input-property.png" alt-text="Custom input property expecting Table data type.":::

The schema of the input property looks like the following formula:

```powerapps-dot
Table({Flavor: "Strawberry",UnitPrice: 1.99, QuantitySold:20})
```

:::image type="content" source="media/map-component-input-fields/custom-property-formula.png" alt-text="Custom input property formula defined as table and sample values.":::

The app consuming this component has the following **IceCreams** table that doesn’t match with the component schema:

| **FlavorName** | **Price** | **SaleNumber** |
|----------------|-----------|----------------|
| Strawberry     | 1.99      | 20             |
| Chocolate      | 2.99      | 45             |

:::image type="content" source="media/map-component-input-fields/icecreams-table.png" alt-text="Schema of IceCreams table.":::

To map the correct fields, use **RenameColumn()** function to rename expected columns.

```powerapps-dot
RenameColumns(IceCreams,"cra56_flavorname","Flavor","cra56_price","UnitPrice","cra56_salenumber","QuantitySold")
```

:::image type="content" source="media/map-component-input-fields/app-custom-input-property.png" alt-text="App using component that uses custom input property mapping with the correct columns using RenameColumns function.":::

The input fields that the component expects are now mapped with the matching columns from the data source.

## Map records

Use [With()](functions/function-with.md) function to map a single record.

For example, continuing from the [earlier example](#map-columns) for mapping columns, the custom input property of a component inside an app expects a record type with the following schema:

```powerapps-dot
{Flavor: "Strawberry",UnitPrice: 1.99, QuantitySold: 20}
```

:::image type="content" source="media/map-component-input-fields/custom-record-property.png" alt-text="Custom input property formula defined as record and sample values.":::

Since the **IceCreams** data source expects column names as **FlavorName**, **Price**, and **SaleNumber**, we'll need to change the mapping for the record once the component is added to the app.

Use **With()** function to select the columns of the **IceCreams** table, and map them to the input fields of the component:

```powerapps-dot
With(Gallery3.Selected,{Flavor:FlavorName,UnitPrice:Price,QuantitySold:SaleNumber})
```

:::image type="content" source="media/map-component-input-fields/app-component-record.png" alt-text="Component record in app mapped to the data source schema.":::

The following animation shows the example of a component added to the app that shows the selected record from the gallery (above the component):

:::image type="content" source="media/map-component-input-fields/component-selected-record.gif" alt-text="Animation that shows selection of a record from gallery above changing the component instance text below.":::

## Map tables

Use [ForAll()](functions/function-forall.md) function to map a table of records with the records expected by the component added to the app.

For example, at the end of the [map columns](#map-columns) example, you can use the **ForAll()** function to map the entire table with the specific columns to point to the fields from the component for each row:

```powerapps-dot
ForAll(IceCreams,{Flavor:FlavorName,UnitPrice:Price,QuantitySold:SaleNumber})
```

:::image type="content" source="media/map-component-input-fields/map-table-forall.png" alt-text="Map table using ForAll() function for all records.":::

## Map using dropdown (deprecated)

You can use the **Advanced** tab for a component added to an app that expects input property of table or record type, and select the field mappings using the dropdown option. This mapping is assigned by default, and unless you manually select the appropriate mapping fields, the mapping might not yield expected results.

For example, the following animation shows the formula being updated to rename columns. The component on screen doesn't change the field mapping since the default field selection using this dropdown needs to be updated manually.

:::image type="content" source="media/map-component-input-fields/deprecated-dropdown.gif" alt-text="Deprecated method to select field mapping using dropdown in advanced property section of a component added to an app.":::

This method of selecting the mapping using the dropdown has been deprecated. Instead, use the [column](#map-columns), [record](#map-records), or [table](#map-tables) mapping methods as described earlier in this article.

You can still use the dropdown option to choose mapping for existing apps, though not recommended. For new apps, this option will be unavailable by default. To turn this deprecated capability on or off, go to **Settings** > **Upcoming features** > **Retired**, and choose **Name**.

### See also

[Behavior formulas for components](component-behavior.md)
