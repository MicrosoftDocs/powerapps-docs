---
title: Implement portals Web API code components (preview)
description: This page walks you through example steps for creating a code component that uses the portal Web API.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 11/03/2021
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
  - nickdoelman
  - sandhangitmsft
 
---

# Implement a portal Web API component (preview)

[This article is pre-release documentation and is subject to change.]

The following is an example of implementing a code component that uses the portal Web API to perform create, retrieve, update, and delete actions. The component renders four buttons, which can be clicked to invoke different Web API actions. The result of the Web API call is injected into an HTML `div` element at the bottom of the code component. 

:::image type="content" source="media/implement-webpi-component/webapi-component.png" alt-text="Example component using the portal Web API.":::

## Prerequisites

- Your portal version must be [9.3.10.x](/power-platform/released-versions/portals/portalupdate9310x) or higher.
- Your starter portal package must be [9.2.2103.x](versions/package-version-9.2.2103.md) or higher.

1. You need to enable the site setting to enable the portals Web API for your portal. [Site settings for the Web API](web-api-overview.md#site-settings-for-the-web-api)

    For example, to expose the Web API for the account table where authenticated users are allowed to perform create, update, and delete operations, the site settings are shown in the following table will need to be configured.

    | Site setting name                 | Site setting value |
    |-|-|
    | `Webapi/account/enabled`            | `true`              |
    | `Webapi/account/fields`             | `attr1,attr2,attr3`  |
    | `Webapi/enableReadOperationPreview` | `true`               |

1. Portals requires Read permission to be set on the Web Resource table before users can see the code component on the webpage. [Allow read access to a web-resource table](component-framework.md#allow-read-access-to-a-web-resource-table)

1. Configure table security using table permission. [Table permissions using studio](configure/entity-permissions-studio.md)

## Code

You can download the complete sample component from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/portals/PortalWebAPIControl).

By default, in the sample, the component is configured to perform the create, retrieve, set the name and revenue fields in the Web API examples.

To change the default configuration to any table or column, update the below configuration values as shown

`private static \_entityName = "account";`

`private static \_requiredAttributeName = "name";`

`private static \_requiredAttributeValue = "Web API Custom Control (Sample)";`

`private static \_currencyAttributeName = "revenue";`

`private static \_currencyAttributeNameFriendlyName = "annual revenue";`

The createRecord method renders three buttons, which allows you to create an account record with the revenue field set to different values (100, 200, 300).

When you select one of the create buttons, the button's `onClick` event handler checks the value of the button selected and uses the Web API action to create an account record with the revenue field set to the button's value. The name field of the account record will be set to *Web API code component (Sample)* with a random `int` appended to the end of the string. The callback method from the Web API call injects the result of the call (success or failure) into the custom control's result `div`.

The `deleteRecord` method renders a button which deletes the selected record in the dropdown. The dropdown control allows you to select the account record you want to delete. Once an account record is selected from the dropdown and the **Delete Record** button is selected, the record is deleted. The callback method from the Web API call injects the result of the call (success or failure) into the custom control's result `div`.

The [FetchXML](/powerapps/developer/data-platform/use-fetchxml-construct-query.md) `retrieveMultiple` method renders a button in the code component. When the `onClick` method of this button is called, FetchXML is generated and passed to the `retrieveMultiple` function to calculate the average value of the revenue field for all the accounts records. The callback method from the Web API call injects the result of the call (success or failure) into the custom control's result `div`.

The OData `retrieveMultiple` method renders a button in the code component. When the `onClick` method of this button is called, an OData string is generated and passed to the `retrieveMultiple` function to retrieve all account records with a name field that is like *code component Web API (Sample)*, which is true for all account records created by this code component.

On successful retrieve of the records, the code component has logic to count how many account records have the revenue field set to 100, 200 or 300, and display this count into an OData status container div on the code component. The callback method from the Web API call injects the result of the call (success or failure) into the custom control's result `div`.

### See also

[Power Apps component framework overview](../../developer/component-framework/overview.md) <br>
[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework) <br>
[How to use the sample components](../../developer/component-framework/use-sample-components.md) <br>
[Create your first component](../../developer/component-framework/implementing-controls-using-typescript.md) <br>
[Add code components to a field or table in model-driven apps](../../developer/component-framework/add-custom-controls-to-a-field-or-entity.md)<br>
[Liquid template tag for code components](component-framework-liquid.md) <br>
[Portals Web API](web-api-overview.md)
