---
title: " Multi Select OptionSet component| Microsoft Docs" 
description: "This sample demonstrates how to leverage the multi select option set type on properties of field components." 
ms.custom: ""
manager: kvivek
ms.date: 06/08/2021
ms.service: "powerapps"
ms.topic: "article"
ms.author: "nabuthuk" 
author: Nkrb
---
# Implementing  choices (multi select option set) component

This sample component demonstrates how to leverage the multi select option set type on properties of `field` components. By binding the code component's primary property to this type, users can create all new types of controls with choices column.

> [!NOTE]
> Control must be bound to a column of type `MultiSelectOptionSet`, then the OptionSet associated with that column is populated in the component. 


[!INCLUDE[cc-terminology](../../data-platform/includes/cc-terminology.md)]

> [!div class="mx-imgBorder"]
> ![Multi select option set component](../media/multi-select-option-set-control.png "Multi select option set component")

## Available for

Model-driven apps

## Code 

You can download the complete sample component from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/MultiSelectOptionSetControl)

In the manifest, a single property of type MultiSelectOptionSet is defined. This property is automatically bound to the OptionSet associated with whatever column the component is placed in the model-driven app.

This component renders a standard `select` element, with options for each value in the OptionSet, and a text column to display all the currently selected options. Each value's `onClick` call back is set to the `updateIndividualSelected` method defined in this component. This method will either add or remove the selected option and then calls the `notifyOutputChanged` to let the framework know there has been a change in the data.

For MultiSelectOptionSets, each option has a display name for the value as well as a numerical value associated with it. To track the currently selected options, the control maintains an array of the value's of all the currently selected options. This method is to align with what PCF expects back from the control for MultiSelectOptionSet in `getOutputs`.

The `getOutputs` method simply returns the currently selected set of values back to the framework for it to update. In `updateView` method, the component simply updates the content of the `selected options` text label to align with the newest value received from the framework through the MultiSelectOptionSet properyt’s formatted value.



### Related topics

[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework)<br/>
[How to use the sample components](../use-sample-components.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework manifest schema reference](../manifest-schema-reference/index.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]