---
title: Canvas component properties (experimental)
description: Using properties in canvas components.
author: jorisdg
ms.subservice: canvas-developer
ms.topic: article
ms.date: 04/04/2023
ms.author: jorisde
ms.reviewer: mkaur
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - jorisdg
---
# Canvas component properties (experimental)

[Canvas components](./create-component.md) allow makers to create different types of properties to relay values or logic between the component and the app that is hosting the component. Properties are an essential part of creating interactive and reusable components.

> [!IMPORTANT]
> - This is an experimental feature.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. More information: [Experimental and preview features](working-with-experimental-preview.md)
> - The behavior that this article describes is available only when the _Enhanced component properties_ experimental feature in [Settings > Upcoming features > Experimental](./working-with-experimental-preview.md#controlling-which-features-are-enabled) is turned on (off by default).
> - Your feedback is very valuable to us - please let us know what you think in the [Power Apps experimental features community forum](https://powerusers.microsoft.com/t5/Power-Apps-Experimental-Features/bd-p/PA_ExperimentalFeatures).

## Types of properties

There are four types of properties available to makers:

1. [Data properties](component-properties.md#data-property): Data properties pertain to data, like a color or text value. A **Data** property can be set to be **Input** or **Output**, which indicates if the component provides data to the app (**Output**) or the app provides data to the component (**Input**). **Data** properties are the only properties that participate in app data flow.
2. [Function properties](component-properties.md#function-property): Function properties are related to logic, such as performing a calculation based on specific parameters or altering text. A **Function** property can be set to be **Input** or **Output**, which indicates if the component provides a function the app can call (**Output**), or the app provides a function the component can call (**Input**). **Function** properties do not participate in an app's data flow, and cannot use component or app variables.
3. [Action properties](component-properties.md#action-property): Action properties are a type of property that deals with logic and behaves like an **Output** **Function**. Thus, the component has the logic defined, and that logic can use chained expressions and manipulate collections or variables ("behavior"). For example, a `Clear()` **Action** property could provide functionality the app can call to clear out some values in the component, or a `Save()` **Action** property that updates a datasource.
4. [Event properties](component-properties.md#event-property): Event properties are a category of property that involves logic and functions as an **Input** **Function**. Thus, the app defines the logic, which the component can call and that logic can use chained expressions and manipulate collections or variables ("behavior"). Typically these properties' names reflect an event such as `OnSelect` or `OnChanged`.


### Data property

A data property's usage is easy to imagine. Standard controls in apps typically have several data properties, to set default values, text color, size, etc. Let's look at a simple example where we wish to make properties of a control within the component available to the hosting app. In this example, our component is named `Component1`. We will put a slider control in inside our component. We will have an **Input** property to specify the color from the consuming app, and an **Output** property where the component can tell the app what the current value of the slider is. The following example assumes your component contains a **Slider** control named `Slider`.

1. In the property pane of the component, select **New custom property**.
2. On the **New custom property** pane, enter display name `Slider Color`.
3. Select **Property type** of **Data** and select **Property definition** value **Input**.
4. Finally, from the **Data type** dropdown, select **Color**.
5. Click **Create**.

Next, select the `Slider1` **Slider** control. Find its **ValueFill** property and in the formula bar, enter `Component1.SliderColor`. `Component1` refers to the name of our component, and `SliderColor` is the name of the property we added previously.

Now our component has a `SliderColor` property which can be set in the consuming app, to pass a color into the component to set the slider's **ValueFill** property.

We also wish to provide the value of the slider to the consuming app. To accomplish this, we will add an **Output** property.

1. In the property pane of the component, select **New custom property**.
2. On the **New custom property** pane, enter display name `Slider Value`.
3. Select **Property type** of **Data** and select **Property definition** value **Output**.
4. Finally, from the **Data type** dropdown, select **Number**.
5. Click **Create**.

When a **Data** property is **Output**, the component provides the value to the consuming app. To set the formula for this, we need to set the new `SliderValue` property in the component to the **Value** property of the slider.

1. In the property pane of the component, click on the `Slider Value` property.
2. In the formula bar, replace the default value of `100` with the following formula: `Slider1.Value`.

Now our component's `SliderValue` property will reflect the value of the slider inside the component, which can then be read from the consuming app.

### Function property

A function property contains an expression that returns a value. Typically, the function takes some arguments which it uses to calculate or determine the value to return.

> [!NOTE]
> Function properties currently cannot access variables or component values and properties, and cannot trigger data flow. Any required values have to be passed in as arguments.

An **Output** function is a simple way to create a custom function for Power Apps. The component defines an **Output** function with an expression that takes some arguments and returns a value. This function can then be used in an app using the component's name (say `Component1`) by calling `Component1.MyFunction(arg1, arg2)`.

An **Input** function is a way for a consuming app to provide logic to a component, similar to a function pointer or callback function. For example, your component may be dealing with people's names and have an input function with arguments `firstname` and `lastname` and respects a string back. The app could define the function expression to return `$"{firstname} {lastname}"` or it could choose to define an expression for `$"{lastname}, {firstname}"`. The component can just call the function the app maker has provided, and use the returned string.

### Action property

Action properties are similar to function properties of type **Output**, but they allow side-effect formulas, and expression chaining. A component could have an action property named `AddRecord` that allows the app to add a record to a collection inside the component, or a `Reset` action that clears variables or collections inside the component.

In the example of the slider examples used for the **Data property** earlier, we can introduce an action property called `ResetValue` to set the slider back to its default value. We can use the formula `Reset( Slider1 )` for this. Now, instances of our component in the app can call `Component1.ResetValue()` to set the slider back to the default value.

### Event property

There are many common **Event**-type properties, effectively input behavior function properties, in standard controls. **OnSelect** on the button control is the most obvious example. A component could define any number of event properties, and call these events like a function. For example, a component that has a button control could have an event property named `OnButtonClicked`. In the button control's **OnSelect** the component can call its `Component1.OnButtonClicked()` property. A consuming app can then define its own logic for this property, to act when the button inside the component is pressed.

## Default values for properties or arguments

Default values can provide a default value for an argument or property in case none is set. This does not makes sense for some types of properties. However, in some cases they can be used to provide an expected schema for a record. By providing a default record, a record type is established as the expected schema.

For example, an **Action** property named `AddRecord` accepts a record to be added to a local collection. To provide the schema of the expected record, a maker has to add a default value for this `AddRecord` property's argument.
