---
title: Create a component for canvas apps | Microsoft Docs
description: Introduction to reusable components for canvas apps
author: yifwang
ms.service: powerapps
ms.topic: article
ms.date: 02/20/2020
ms.author: yifwang
ms.reviewer: tapanm
search.audienceType:
  - maker
search.app:
  - PowerApps
---

# Create a component for canvas apps

> [!IMPORTANT]
> This feature is still in public preview. For more information, see [Experimental and preview features](working-with-experimental.md).

Components are reusable building blocks for canvas apps so that app makers can create custom controls to use in an app. Components can be reused across apps using [component library](component-library.md). Components can utilize advanced features, such as custom properties and enable complex capabilities. This article introduces component concepts and some examples.

Components are useful in building larger apps that have similar control patterns. If you update a component definition inside the app, all instances in the app reflect your changes. You can also improve performance by using one or more components because you don't copy and paste controls, which duplicates overhead. Components also facilitates collaborative development and standardizes look-and-feel in an organization when you use a [component library](component-library.md).

## Components in canvas app

You can create a component from within an app as explained in this article, or by creating a new component inside a [component library](component-library.md). A component library should be used for requirements to use components across multiple app screens. You can also copy the existing components into an existing or a new component library.

To create a component within an app, go to **Tree View**, select **Components** tab and then select **New Component**:

![Create new custom component using tree view](./media/create-component/insert-new-component-treeview.png)

Regardless of which approach you take, an empty canvas appears, where you can add controls as part of the component definition. If you edit a component in the canvas, you'll update instances of the same component in other app screens and other apps.

If you select a screen, you can select a component from the list of existing components in the left navigation. When you select a component, you insert an instance of that component onto the screen, just as you insert a control.

Components available inside the app are listed under **Custom** category in list of components inside tree view; whereas components available from imported component libraries are listed under **Library components** category:

![Insert components to the app](./media/create-component/insert-components.png)

> [!NOTE]
> Components discussed in this article are different from the Power Apps Component Framework that enables developers and makers to create code components for model-driven and canvas apps. For more information, read [Power Apps Component Framework overview](https://docs.microsoft.com/powerapps/developer/component-framework/overview).

## Scope

Think of a component as an encapsulated black box with properties as the interface. You can't access controls in the component from outside of the component, and you can't refer to anything outside of the component from inside the component. Data sources are an exception as they are shared between app and its components. Scope restrictions keep the data contract of a component simple and cohesive, and it helps enable seamless component-definition updates, especially across apps with component libraries. You can update the data contract of the component by creating one or more custom properties.

> [!NOTE]
> You can insert instances of components into a screen within a component library, and preview that screen for testing purposes. Also, note that the component library does not display when using [Power Apps mobile](https://powerapps.microsoft.com/downloads/).

## Variables

Components don't support the [**UpdateContext**](./functions/function-updatecontext.md) function, but you can create and update variables in a component by using the [**Set**](functions/function-set.md) function. The scope of these variables is limited to the component, but you can access them from outside the component by leveraging custom output properties.

## Custom properties

A component can receive input values and emit data if you create one or more custom properties. These scenarios are advanced and require you to understand formulas and binding contracts.

An input property is how a component receives data to be used in the component. Input properties appear in the **Properties** tab of the right-hand pane if an instance of the component is selected. You can configure input properties with expressions or formulas, just as you configure standard properties in other controls. Other controls have input properties, such as the **Default** property of a **Text input** control.

Output properties can emit data or component state. For example, the **Selected** property on a **Gallery** control is an output property. When you create an output property, you can determine what other controls can refer to the component state.

This walk-through further explains these concepts.

## Create an example component

In this example, you'll create a menu component that resembles this graphic and in which you can change the text and use in multiple screens, apps, or both:

![Final gallery](./media/create-component/menu-instance-new.png)

> [!NOTE]
> We recommend that you use [component library](component-library.md) when creating components for reuse. Updating components inside an app only makes the component updates available only inside the app. When you import components from one app to another, new updates to components in original app do not propagate to the app that imported those components earlier. When using component library, you get prompted to update components if components inside a library are updated and published.

1. Go to make.powerapps.com and create a blank app.

1. In the **Tree View**, select **Components** and then select **New Component** to create a new component.

    ![Create new custom component using tree view](./media/create-component/insert-new-component-treeview.png)

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

## Import and export components

> [!NOTE]
> This feature will be deprecated. [Component libraries](component-library.md) are the recommended way to reuse the components across the apps. When using content library, an app maintains dependencies on the components it uses. The app maker will be alerted when the updates to dependent components become available. Hence, all new reusable components should be created within the component libraries instead.

### Import components from another app

To import one or more components from one app into another, select **Import components** from either **Insert** menu and then using **Custom** drop down, or by using **Components** in tree view on the left navigation.

A dialog box lists all apps that contain components that you have permission to edit. Select an app, and then select **Import** to import the most recent published version of all of the components in that app. After you import at least one component, you can edit your copy and delete any that you don’t need.

![Import components dialog box](./media/create-component/import-component-screen.png)

You can save an app with existing components to a file locally and then reuse this file by importing it. This allows you export all components of an app and then import to another app. 

If the app contains a modified version of the same component, you're prompted to decide whether to replace the modified version or cancel the import. 

After you create components in an app, other apps can consume the components from this app by importing them.

### Export components from your app

You can export components to file and download them for import to another app. To do this, select **Export components** option from **Components** section in left navigation tree view:

![Export components treeview](./media/create-component/export-components-treeview.png)

Alternatively, you can also use **Insert** menu and then select **Custom** drop down. 

![Export components insert menu](./media/create-component/export-components-insert-menu.png)

Once you select to export a component, you are presented with the option to download the exported component file:

![Download component](./media/create-component/download-component.png)

Downloaded component file has extension of *.msapp*. 

### Import components from exported components file

To import components from an exported components file, select **Import components** from either **Insert** menu and then using **Custom** drop down, or by using **Components** in tree view on the left navigation. From the components dialog box, select **Import file** instead of selecting any other components or apps:

![Import component file](./media/create-component/import-component-file.png)

From the **Open** dialog box, browse to the location of the component file and select **Open**. This imports the component inside the app for reuse.

### Import components from exported app

You can save an app locally using **File** -> **Save As** option:

![Save app](./media/create-component/save-app-locally.png)

Once you save the app, you can reuse the components of this app using the same method of importing components from file. To do this, follow the steps explained in importing components from exported components file section above.

## Known limitations

- You cannot save data sources, forms and data tables with components.
- Use of collections in components is not supported.
- You cannot insert a component into a gallery or a form.
- A master instance of a component is a local master and scoped to the app. If you change a master instance, only copies of the component within the app will reflect the change. Copies in other apps will remain the same unless you import the component library again. All master instances in those apps will be automatically detected and updated.
- You cannot package media files when you import a component.

## Next steps

Learn [component library](component-library.md) to create a repository of reusable components.