---
title: Canvas component properties
description: Using properties in canvas components.
author: jorisdg
ms.subservice: canvas-developer
ms.topic: how-to
ms.date: 06/6/2025
ms.author: mamali
ms.reviewer: mkaur
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - jorisdg
  - mamali
---
# Canvas component properties

[Canvas components](./create-component.md) let makers create different types of properties to pass values or logic between the component and the app that hosts the component. Properties are essential for building interactive, reusable components.


## Prerequisites

This feature is on by default for new apps. For existing apps, you need to turn it on in your app settings.

1. Open your [canvas app for editing](edit-app.md) in Power Apps Studio. On the command bar, select **Settings** > **Updates**.

1. On the **New** tab, find and turn on the **Enhanced component properties** setting.

## Types of properties

There are four types of properties available to makers.

1. [Data properties](component-properties.md#data-property): Data properties pertain to data, like a color or text value. A **Data** property can be set to be **Input** or **Output**, which indicates if the component provides data to the app (**Output**) or the app provides data to the component (**Input**). **Data** properties are the only properties that participate in app data flow.
2. [Function properties](component-properties.md#function-property): Function properties are related to logic, such as performing a calculation based on specific parameters or altering text. A **Function** property can be set to be **Input** or **Output**, which indicates if the component provides a function the app can call (**Output**), or the app provides a function the component can call (**Input**). **Function** properties do not participate in an app's data flow, and cannot use component or app variables.
3. [Action properties](component-properties.md#action-property): Action properties are a type of property that deals with logic and behaves like an **Output** **Function**. Thus, the component has the logic defined, and that logic can use chained expressions and manipulate collections or variables ("behavior"). For example, a `Clear()` **Action** property could provide functionality the app can call to clear out some values in the component, or a `Save()` **Action** property that updates a datasource.
4. [Event properties](component-properties.md#event-property): Event properties are a category of property that involves logic and functions as an **Input** **Function**. Thus, the app defines the logic, which the component can call and that logic can use chained expressions and manipulate collections or variables ("behavior"). Typically these properties' names reflect an event such as `OnSelect` or `OnChanged`.


### Data property

A data property's usage is easy to imagine. Standard controls in apps typically have several data properties, to set default values, text color, size, etc. Let's look at a simple example where you want to make properties of a control within the component available to the hosting app. In this example, the component is named `Component1`. Put a slider control inside the component. Add an **Input** property to specify the color from the consuming app, and an **Output** property so the component can tell the app the current value of the slider. This example assumes the component has a **Slider** control named `Slider`.

1. In the property pane of the component, select **New custom property**.
2. On the **New custom property** pane, enter display name `Slider Color`.
3. Select **Property type** of **Data** and select **Property definition** value **Input**.
4. Finally, from the **Data type** dropdown, select **Color**.
5. Click **Create**.

Next, select the `Slider1` **Slider** control. Find its **ValueFill** property and in the formula bar, enter `Component1.SliderColor`. `Component1` is the name of the component, and `SliderColor` is the name of the property you added.

Now the component has a `SliderColor` property that can be set in the consuming app to pass a color into the component and set the slider's **ValueFill** property.

You might also want to provide the value of the slider to the consuming app. To do this, add an **Output** property.

1. In the property pane of the component, select **New custom property**.
2. On the **New custom property** pane, enter display name `Slider Value`.
3. Select **Property type** of **Data** and select **Property definition** value **Output**.
4. Finally, from the **Data type** dropdown, select **Number**.
5. Click **Create**.

When a **Data** property is **Output**, the component provides the value to the consuming app. To set the formula, set the new `SliderValue` property in the component to the **Value** property of the slider.

1. In the property pane of the component, click on the `Slider Value` property.
2. In the formula bar, replace the default value of `100` with the following formula: `Slider1.Value`.

Now the component's `SliderValue` property reflects the value of the slider inside the component, which the consuming app can read.

### Function property

A function property contains an expression that returns a value. Typically, the function takes arguments that it uses to calculate the value to return.

> [!NOTE]
> Function properties currently cannot access variables or component values and properties, and cannot trigger data flow. Any required values have to be passed in as arguments.

An **Output** function is a simple way to create a custom function for Power Apps. The component defines an **Output** function with an expression that takes some arguments and returns a value. This function can then be used in an app using the component's name (say `Component1`) by calling `Component1.MyFunction(arg1, arg2)`.

An **Input** function lets a consuming app provide logic to a component, similar to a function pointer or callback function. For example, if the component works with people's names, it can have an input function with arguments `firstname` and `lastname` and expects a string back. The app can define the function expression to return `$"{firstname} {lastname}"` or `$"{lastname}, {firstname}"`. The component calls the function the app maker provides and uses the returned string.

### Action property

Action properties are similar to function properties of type **Output**, but they allow side-effect formulas and expression chaining. A component can have an action property named `AddRecord` that lets the app add a record to a collection inside the component, or a `Reset` action that clears variables or collections inside the component.

In the earlier slider example for the **Data property**, you can add an action property called `ResetValue` to set the slider back to its default value. Use the formula `Reset( Slider1 )` for this. Now, instances of the component in the app can call `Component1.ResetValue()` to set the slider back to the default value.

### Event property

Many standard controls have common **Event**-type properties, which are input behavior function properties. **OnSelect** on the button control is a common example. A component can define event properties and call these events like a function. For example, a component with a button control can have an event property named `OnButtonClicked`. In the button control's **OnSelect**, the component can call its `Component1.OnButtonClicked()` property. A consuming app can define its own logic for this property to act when the button inside the component is pressed.

## Default values for properties or arguments

Default values give an argument or property a value if none is set. This doesn't make sense for some types of properties. In some cases, you can use default values to show the expected schema for a record. By providing a default record, you set the record type as the expected schema.

For example, an **Action** property named `AddRecord` takes a record to add to a local collection. To show the schema of the expected record, add a default value for the `AddRecord` property's argument.
