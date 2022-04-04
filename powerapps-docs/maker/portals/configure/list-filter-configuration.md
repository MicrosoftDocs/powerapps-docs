---
title: List filter configuration
description: Learn how to configure list filters on a portal.
author: sandhangitmsft

ms.topic: conceptual
ms.custom: 
ms.date: 04/04/2022
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
    - ProfessorKendrick
---
# List filter configuration

Adding the ability to filter records on a list is easy: enable the filtering option and then choose one or more filter types to display to users. It's possible to filter by an attribute that matches text provided by the user, or to select from a series of options. You can even design virtually any type of filter you can imagine by using Advanced Find.

**Enable the list filter**

In the **Metadata Filter** section, select the **Enabled** check box. This will add the Filter area to the list when it's displayed. Until you've defined at least one filter type, the box will appear empty.

You can define how the Filter area on the list will be rendered by using the Orientation setting. The default, Horizontal, renders the Filter area above the list. Vertical orientation renders the Filter area as a box to the left of the list.

![Metadata filter settings.](../media/metadata-filter-settings.png "Metadata filter settings")  

**Filter types**

|**Filter Type**      |**Description**                                                                                                                                                                                                                               |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Text Filter          | Filter the list by using a text box to search for matching text in a selected attribute of the given table.                                                                                                                               |
| Attribute Filter Set | Filter the list by using a series of check boxes, each of which tries to match its condition against a particular attribute of the given table.                                                                                           |
| Lookup Set           | Filter the list by using a series of check boxes, each of which represents a relationship between a record for the given table and a record for a related table.                                                                         |
| Range Filter Set     | Similar to the Attribute Filter Set, except that each check box can represent two conditions rather than one (for example, greater than or equal to 0 AND less than 100).                                                                    |
| Dynamic Picklist Set | Similar to choosing a picklist value on an Attribute Filter Set. The Dynamic Picklist Set doesn't require that you specify the picklist options to filter by; instead, it generates the full list of options when the list is loaded. |
| Dynamic Lookup Set   | Similar to the Lookup Set. The Dynamic Lookup Set doesn't require that you specify the lookup options to filter by; instead, it generates the full list of options when the list is loaded.                                           |
| FetchXML Filter      | Filter the list by using a FetchXML filter condition.                                                                                                                                                                                     |

**Text filter**

The Text filter adds a text box to the list Filter area that is tied to an attribute of the table type of the list. When a user applies the filter, the list only displays those records whose selected attribute contains the value.

To add a Text filter, select **+Text Filter**.

![Add a text filter.](../media/add-text-filter.png "Add a Text filter")  

The Text filter uses the following attributes:

|**Name**     |**Description**                                                                                                                                        |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attribute    | The name of the attribute on the list's selected table type to filter by. *Only attributes with the type String are valid for a Text filter.*                                                                                   |
| Display Name | Override the label for the filter when the list is displayed. By default, this will be automatically set to the name of the selected attribute. |

**Attribute Filter Set**

The Attribute Filter Set adds a series of options to filter the list by, tied to a single attribute of the list's selected table type. When a user applies the filter, the list only displays those records that exactly match at least one of the selected options.

![Attribute filter settings.](../media/set-attribute-filter.png "Attribute filter settings")

The Attribute Filter Set uses the following attributes:

|**Name**     |**Description**                                                                                                                                        |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attribute    | The name of the attribute on the list's selected table type to filter by. Only attributes with the following types are valid for a Text filter: String, BigInt, Decimal, Double, Integer, Money, Picklist, DateTime, and Boolean.
|Display Name | Override the label for the filter when the list is displayed. By default, this will be automatically set to the name of the selected attribute.
| Options |      A collection of possible values to filter by. See below for more details.                                                                              |

**Attribute Filter Set options**

An Attribute Filter Set can usually have any number of options, with the exceptions of picklist and Boolean attributes. A Boolean Attribute Filter Set can have only one or two options&mdash;one true option and one false option. A Picklist Attribute Filter Set can have at most one option for each possible value in the picklist.

Options have the following attributes:

|**Name**     |**Description**                                                                                                                                                                                  |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operator     | The comparison operator used to filter results, for example Equals, Less Than, and so on. The list of operators for the option will depend on the type of the attribute selected for the filter. For example, numeric (Decimal) types will have operators such as Less Than or Greater Than, whereas String attributes will use operators such as Begins With or Contains. Picklist and Boolean operators are always Equals.                                                                                                                                               |
| Value        | The actual value used for this filter condition.                                                                                                                                                 |
| Display Name | Overrides the display name for this option in the Filter box. By default, this will be set to the same value as the Value attribute.                                                             |

**Lookup Set**

The Lookup Set adds a series of options to filter the list by, tied to a related table to the list's selected table type. When a user applies the filter, the list only displays those records that exactly match at least one of the selected related records.

![Lookup set.](../media/lookup-set.png "Lookup Set")  

The Lookup Set uses the following attributes:

|**Name**     |**Description**                                                                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Relationship | The name of the related table to the list's selected table type to filter by. Only tables with a one-to-many or many-to-many relationship with the list's selected table type appear as options for this filter type.          |
| Display Name | Override the label for the filter when the list is displayed. By default, this will be automatically set to the name of the selected relationship. |
| Options      | A collection of possible values to filter by. See below for more details.                                                                                 |

**Lookup Set options**

A Lookup Set can typically have any number of options, with the only limit being the number of related records of the selected related type.

Options have the following attributes:

|**Name**     |**Description**                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Value        | The record of the selected related type to filter by.                                                                                |
| Display Name | Overrides the display name for this option in the Filter box. By default, this will be set to the same value as the Value attribute. |

**Range Filter Set**

The Range Filter Set adds a series of options, each with one or two conditions, to the Filter area. When a user applies the filter, the list only displays those records that exactly match all conditions on at least one of the selected options.

![Range filter settings.](../media/set-range-filter.png "Range filter settings")  

The Range Filter Set uses the following attributes:

|**Name**     |**Description**                                                                                                                                        |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attribute    | The name of the attribute on the list's selected table type to filter by. Only attributes with the following types are valid for a Text filter: String, BigInt, Decimal, Double, Integer, Money, DateTime.                       |
| Display Name | Override the label for the filter when the list is displayed. By default, this will be automatically set to the name of the selected attribute. |
| Options      | A collection of possible values to filter by. See below for more details.                                                                              |

**Range Filter Set options**

A Range Filter Set can have any number of options. Each option will produce a filter condition with either one or two subconditions, both of which must be met for the condition to be true.

Options have the following attributes:

|**Name**              |**Description**                                                                                                                                                                                |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operator 1            | The first comparison operator used to filter results, for example Equals and Less Than. The list of operators for the option will depend on the type of the attribute selected for the filter. For example, numeric (Decimal) types will have operators such as Less Than or Greater Than, whereas String attributes will use operators such as Begins With or Contains. Picklist and Boolean operators are always Equals.                                                                                                                                             |
| Value 1               | The first value used for this filter condition.                                                                                                                                                |
| Operator 2 (optional) | The second comparison operator used to filter results, for example Equals and Less Than. The list of operators for the option will depend on the type of the attribute selected for the filter. For example, numeric (Decimal) types will have operators such as Less Than or Greater Than, whereas String attributes will use operators such as Begins With or Contains. Picklist and Boolean operators are always Equals.                                                                                                                                             |
| Value 2 (optional)    | The second value used for this filter condition.                                                                                                                                               |
| Display Name          | Overrides the display name for this option in the Filter box. By default this will be set dynamically, based on the operators and values selected.                                         |

**Dynamic Picklist Set**

The Dynamic Picklist Set adds a series of options to filter by that represent all the values of a specified Picklist field. This is different from selecting a Picklist in the Attribute Filter Set. In the Attribute Filter Set, you must specify a set of options that will be made available to the user to filter by; in the Dynamic Picklist Set, you need only specify the Picklist field and the entire set of options will be provided automatically. If you need greater control, we recommend that you use the Attribute Filter Set.

![Dynamic picklist settings.](../media/set-dynamic-picklist.png "Dynamic picklist settings")  

The Dynamic Picklist Set uses the following options:

|**Name**     |**Description**                                                                                                                                        |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attribute    | The name of the Picklist attribute on the list's selected table type to filter by.                                                             |
| Display Name | Override the label for the filter when the list is displayed. By default, this will be automatically set to the name of the selected attribute. |

**Dynamic Lookup Set**

The Dynamic Lookup Set adds a dynamic series of options to filter the list by, tied to a related table to the list's selected table type. When a user applies the filter, the list only displays those records that exactly match at least one of the selected related records.

This is different from a Lookup Set. In the Lookup Set, you must manually specify the related tables to filter by. In the Dynamic Lookup Set, you need only specify the relationship on which to filter, and a list of options will be generated based on the specified view of related tables.

![Dynamic lookup settings.](../media/set-dynamic-lookup.png "Dynamic lookup settings")  

The Dynamic Lookup Set uses the following options:

|**Name**                      |**Description**                                                                                                                                                                      |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Relationship                  | The name of the related table to the list's selected table type to filter by. Only tables with a one-to-many or many-to-many relationship with the list's selected table type appear as options for this filter type.                                     |
| View                          | The view (Saved Query) to use as a source for the dynamic list of tables to filter by.                                                                                              |
| Label Column                  | The field from the view that provides each table's Name value.                                                                                                                    |
| Filter Lookup On Relationship | Specifies a relationship between the table specified by the Relationship field and the signed-in user. If the table specified by the Relationship field also has a relationship to a contact, you can narrow the list of filter options to those related to the signed-in user.  |
| Display Name                  | Override the label for the filter when the list is displayed. By default, this will be automatically set to the name of the selected relationship.                            |

**FetchXML filter**

The range filter can create either a simple text box filter like the Text filter or a set of options like the other filter types. It allows you to manually create virtually any type of filter for the list by using FetchXML.

![FetchXML filter settings.](../media/set-fetchxml-filter.png "FetchXML filter settings")

The FetchXML filter uses only one attribute:

|**Name** |**Description**                            |
|----------|--------------------------------------------|
| FetchXML | The XML statement representing the filter. |

### See also

- [Microsoft Learn: Display multiple Dataverse records using lists](/learn/modules/portals-access-data-platform/2-entity-lists)
- [Configure a portal](configure-portal.md)  
- [Redirect to a new URL on a portal](add-redirect-url.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
