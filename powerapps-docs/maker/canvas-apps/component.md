---
title: Components (Experimental feature)  | Microsoft Docs
description: Introduction to reusable canvas components
author: yifwang
ms.service: powerapps
ms.topic: article
ms.date: 12/12/2018
ms.author: emcoope
search.audienceType:
  - maker
search.app:
  - PowerApps
---

# Components (Experimental feature)

Components are reusable canvas app building blocks where app makers can create custom controls to use within the app or across apps. Advanced features like custom properties enable complex capabilities in components. In this article, we will introduce component concepts and some examples.

Components are useful in building larger apps that have similar control patterns. With components, updating a component definition reflects the changes in all instances within the app. It also helps improve performance as it reduces duplicate controls through copy/paste. Components also enable collaborative development and standardized look-and-feel within an organization.

Since this feature is in the experimental stage, it needs to be enabled from the App Settings screen.

## Prerequisite

Make sure you are in a preview region, turn on the feature in the app setting. Read here about the [Preview program](../../administrator/preview-environments.md). The feature is not supported in classic canvas.

## Component canvas

There are two gestures to making a new component: from the ‘Components’ list view or from the ‘Components’ ribbon button. The Components view lives next to the ‘Screens’ tree view and lists components that you have defined in the app, sorted by creation time. 

![Component list view](./media/component/list-view.png)

The ribbon button brings you to the same spare canvas where you can add controls as part of the component definition. The ribbon dropdown also shows the same list and selecting one from the ribbon inserts an instance of the component, just like inserting a control. 

Editing on the component canvas will update related component instances that you inserted in the app screens.

## Scope

Think of a component as an encapsulated black box with properties as the interface. Controls within the component are not accessible from outside of the component. Within the component, any reference to outside of the component is not valid and will result in an expression error. Scope restrictions keep the data contract of a component simple and cohesive, and it helps enable seamless component definition updates, especially across apps. You can update the data contract of the component by creating custom properties.

## Variables

You can use variables in component with the Set() function. UpdateContext() function is not supported. Please note that the scope of these variables is within the component. To access them from outside the component, you can leverage custom output properties.

## Import and export

The export gesture will create a local file which you can import to a different app. If the app contains the same component but modified, you will be prompted to decide whether to replace or skip the modified version. Saving components to the cloud and sharing them within an environment is a limitation that will be addressed in future updates. 

![Import and export](./media/component/import.png)

## Custom properties

A component can receive input values and emit data using custom properties. They are advanced scenarios which require understanding of formulas and binding contract.

An input property is how a component receives data to be used inside the component. Input properties show up in the properties pane of component instances and can be configured with expressions, just like standard properties in other controls. The ‘Default’ property on input controls like **TextInput** is an example of an input property. 

Output properties can emit data or component state. For example, the “Selected” property on the Gallery control is an output property. When you create an output property, you can determine what other controls can refer to from the component state.

The following walkthrough explains the concepts further. 

## Menu component example

Let’s create a menu component which takes a list of menu items text as input. It should have an **Items** property like in List box and Gallery controls. 

First, create a new component by selecting **New component** from the Components list view. Next, select the **New custom property** option (highlighted) to create a new custom property. The data type will be ‘table’ since the input will be a list of text. 

![New property](./media/component/new-property.png)

A default value is assigned based on the data type of the property. In this case, we want to change it to a list of text. You can click on the name from the right-hand pane and update it from the ribbon or you can find it from the advanced pane to update the formula. 

Let's define the default value of Items to: 

```
Table({Item:"SampleText"})
```

![Formula](./media/component/formula.png)

Next, insert a gallery with label and set the Items property of the gallery control to:

```
MenuComponent.Items
```

This way, the gallery Items property reads and depends on the component input property ‘Items’. Make sure Gallery field selection is correct. 

![Gallery](./media/component/gallery.png)

Now, go back to screens and insert a menu component from the ribbon. You will find the input property “Items” shows up on the right-hand pane. Make sure the input you give here matches the fields when you create this property. As shown in the screenshot, . You can have any number of entries.

![Insert](./media/component/insert.png)

![Table input](./media/component/table-input.png)

Next, let’s create a text output property which display what’s selected from the menu.

![Output](./media/component/output.png)

Go to advanced pane and change the formula to the following, so that the output property is bond to the **seleted** of the gallery.

![Advanced pane](./media/component/advance.png)

Go back to screens and test it out by adding a label to the app and bond it to **MenuComponent_2.Selected**. Note that here **MenuComponent_2** is the name of an instance, not the name of the defined component. You can rename any instance. Now the label shows the text of selected menu item.

![Demo](./media/component/demo.png)

## Known limitations

1. Data source is not saved with components. This capability is planned as the next step.
1. Variables used in components don't display with app variables. This is coming soon.
