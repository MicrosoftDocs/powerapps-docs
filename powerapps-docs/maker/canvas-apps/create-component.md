---
title: Create a component for canvas apps | Microsoft Docs
description: Introduction to reusable components for canvas apps
author: yifwang
ms.service: powerapps
ms.topic: article
ms.date: 02/15/2020
ms.author: yifwang
ms.reviewer: tapanm
search.audienceType:
  - maker
search.app:
  - PowerApps
---

# Create a component for canvas apps

Components are reusable building blocks for canvas apps so that app makers can create custom controls to use in an app or across apps. Advanced features, such as custom properties, enable complex capabilities in components. This article introduces component concepts and some examples.

Components are useful in building larger apps that have similar control patterns. If you update a component definition, all instances in the app reflect your changes. You can also improve performance by using one or more components because you don't copy and paste controls, which duplicates overhead. Components also facilitates collaborative development and standardizes look-and-feel in an organization.

## Components in canvas app

You can create a component from within an app, or by creating a new component inside a component library. 

To create a component within an app, go to **Insert** menu, select **Custom** drop down menu and then select **New Component**:

![Insert new custom component](./media/create-component/insert-new-component.png)

Alternatively, you can go to **Tree View**, select **Components** tab and then select **New Component**:

![Insert new custom component using tree view](./media/create-component/insert-new-component-treeview.png)

Regardless of which approach you take, an empty canvas appears, where you can add controls as part of the component definition. If you edit a component in the canvas, you'll update instances of the same component in other app screens and other apps.

If you select a screen, you can select a component from the list of existing components in the left navigation bar or the **Custom** menu on the **Insert** tab. When you select a component, you insert an instance of that component onto the screen, just as you insert a control.

Components available inside the app are listed under **Custom** category in list of components inside tree view; whereas components available from imported component libraries are listed under **Library components** category:

![Insert components to the app](./media/create-component/insert-components.png)

## Scope

Think of a component as an encapsulated black box with properties as the interface. You can't access controls in the component from outside of the component, and you can't refer to anything outside of the component from inside the component. If you try, an error appears. Scope restrictions keep the data contract of a component simple and cohesive, and it helps enable seamless component-definition updates, especially across apps. You can update the data contract of the component by creating one or more custom properties.

> [!NOTE]
> You cannot **preview** components from components section or the component library like the way you can preview an app using the play button on top right side of the Power Apps Studio. In order to experience the components, you must use components inside an app. Component library does not display when using Power Apps mobile.

## Variables

Components don't support the **UpdateContext** function, but you can create and update variables in a component by using the **Set** function. The scope of these variables is limited to the component, but you can access them from outside the component by leveraging custom output properties.

## Import and export

To import one or more components from one app into another, select **Import components** in the drop-down list of components. 

![Import export component](./media/create-component/import-export-components-option.png)

A dialog box lists all apps that contain components that you have permission to edit. Select an app, and then select **Import** to import the most recent published version of all of the components in that app. After you import at least one component, you can edit your copy and delete any that you don’t need.

![Import components dialog box](./media/create-component/import-component-screen.png)

You can save an app with existing components to a file locally and then reuse this file by importing it. This allows you export all components of an app and then import to another app. 

If the app contains a modified version of the same component, you're prompted to decide whether to replace the modified version or cancel the import. 

## Custom properties

A component can receive input values and emit data if you create one or more custom properties. These scenarios are advanced and require you to understand formulas and binding contracts.

An input property is how a component receives data to be used in the component. Input properties appear in the **Properties** tab of the right-hand pane if an instance of the component is selected. You can configure input properties with expressions or formulas, just as you configure standard properties in other controls. Other controls have input properties, such as the **Default** property of a **Text input** control.

Output properties can emit data or component state. For example, the **Selected** property on a **Gallery** control is an output property. When you create an output property, you can determine what other controls can refer to the component state.

This walkthrough further explains these concepts.

## Create an example component

In this example, you'll create a menu component that resembles this graphic and in which you can change the text and use in multiple screens, apps, or both:

![Final gallery](./media/create-component/menu-instance-new.png)

1. Go to make.powerapps.com and create a blank app.

1. In the **Tree View**, select **Components** and then select **New Component** to create a new component.

    ![Insert new custom component using tree view](./media/create-component/insert-new-component-treeview.png)

1. Select the new component in left navigation, then select ellipsis (...) and select **Rename**. Type or paste the name as **MenuComponent**.

1. Optional - in the right-hand pane, set the component's width to **150** and its height to **250**, and then select **New custom property**. You can also set the height & width to any other value as appropriate.

    ![New property](./media/create-component/new-property.png)

1. In the **Display name**, **Property name**, and **Description** boxes, type or paste **Items**.

    ![Display name, property name, description boxes](./media/create-component/property-names.png)

    When you specify a property name, don't include spaces because you'll refer to the component by this name when you write a formula (for example, **ComponentName.PropertyName**).

    The display name appears on the **Properties** tab of the right-hand pane if you select the component. A descriptive display name helps you and other makers understand the purpose of this property. The **Description** appears in a tooltip if you hover over the display name of this property in the **Properties** tab.

1. In the **Data type** list, select **Table**, and then select **Create**.

    ![Data type of the property](./media/create-component/property-data-type.png)

    The **Items** property is set to a default value based on the data type that you specified, but you can set it to a value that suits your needs. If you specified a data type of **Table** or **Record**, you may want to change the value of the **Items** property to match the data schema that you want to input to the component. In this case, you'll change it to a list of strings.

    You can set the property's value in the formula bar if you select the name of the property on the **Properties** tab of the right-hand pane.

    ![Custom input property on the Properties tab](./media/create-component/properties-tab.png)

    As the next graphic shows, you can also edit the property's value on the **Advanced** tab of the right-hand pane.

1. Set the component's **Items** property to this formula:

    ```powerapps-dot
    Table({Item:"SampleText"})
    ```

    ![Formula](./media/create-component/set-component-items.png)

1. In the component, insert a blank vertical **Gallery** control and select **Layout** on the property pane as **Title**.

1. Make sure that the property list shows the **Items** property (as it does by default), and then set the value of that property to this expression:

    ```powerapps-dot
    MenuComponent.Items
    ```

    This way, the **Items** property of the **Gallery** control reads and depends on the **Items** input property of the component.

1. Optional - set the **Gallery** control's **BorderThickness** property to **1**  and its **TemplateSize** property to **50**. You can also update values for border thickness and template size to any other value as appropriate.

Next, you'll add the component to a screen and specify a table of strings for the component to show.

1. In the left navigation bar, select the list of screens, and then select the default screen.

    ![Default screen](./media/create-component/default-screen.png)

1. On the **Insert** tab, open the **Components** menu, and then select **MenuComponent**.

    ![Insert](./media/create-component/insert.png)

    The new component is named **MenuComponent_1** by default.

1. Set the **Items** property of **MenuComponent_1** to this formula:

    ```powerapps-dot
    Table({Item:"Home"}, {Item:"Admin"}, {Item:"About"}, {Item:"Help"})
    ```

    This instance resembles this graphic, but you can customize the text and other properties of each instance.

    ![Final gallery](./media/create-component/menu-instance-new.png)

So far, you've created a component and added it to an app. Next, you'll create an output property that reflects the item that the user selects in the menu.

1. Open the list of components, and then select **MenuComponent**.

1. In the right-hand pane, select the **Properties** tab, and then select **New custom property**.

1. In the **Display name**, **Property name**, and **Description** boxes, type or paste **Selected**.

1. Under **Property type**, select **Output**, and then select **Create**.

    ![Property type as output](./media/create-component/output-property-type.png)

1. On the **Advanced** tab, set the value of the **Selected** property to this expression, adjusting the numeral in the gallery name if necessary:

    ```powerapps-dot
    Gallery1.Selected.Item
    ```

    ![Advanced pane](./media/create-component/advance.png)

1. On the default screen of the app, add a label, and set its **Text** property to this expression, adjusting the numeral in the component name if necessary:

    ```powerapps-dot
    MenuComponent_1.Selected
    ```

    Note that **MenuComponent_1** is the default name of an instance, not the name of the component definition. You can rename any instance.

1. While holding down the Alt key, select each item in the menu.

    The **Label** control reflects the menu item that you selected most recently.

## Known limitations

- As of this writing, data sources aren't saved with components, so forms and data tables are disabled.
- Power Apps doesn't support collections in components.
- You can't insert a component into a gallery, a form, or a data card.
- A master instance of a component is a local master and scoped to the app. If you change a master instance, only copies of the component within the app will reflect the change. Copies in other apps will remain the same unless you import the component library again. All master instances in those apps will be automatically detected and updated.
- You can't package media files when you import a component.
