---
title: Power Apps application design guidelines
description: Discover best practices for designing user-friendly Power Apps. Learn about modern controls, form design, gallery optimization, and reusable components to create impactful business solutions.
#customer intent: As a Power Apps user, I want to learn best practices for designing modern controls so that I can create visually appealing and accessible applications.
ms.date: 02/18/2026
ms.topic: best-practice
ms.subservice: guidance
ms.service: powerapps
author: robstand
ms.author: rachaudh
---

# App design guidelines

Designing effective and user-friendly Power Apps is essential for creating impactful business solutions. This guide provides best practices and recommendations for designing Power Apps, focusing on modern controls, form design, container usage, gallery optimization, and building reusable components.

## Modern controls

Modern controls in canvas apps represent a significant advancement in the development and design of user interfaces within the Microsoft ecosystem. Based on Microsoft's Fluent Design System, these controls are designed to deliver a fast, performance-oriented, and accessible user experience, all while ensuring seamless integration with theming capabilities. The introduction of these controls, including tab lists, progress bars, info buttons, spinners, and more, underscores a strategic shift towards creating more intuitive, responsive, and visually appealing applications. By using these modern controls, developers can easily implement sophisticated user interface (UI) elements that are both aesthetically pleasing and functionally rich, enhancing the overall user engagement and satisfaction.

The inherent design of these controls, keeping theming in mind, allows for a unified and consistent look and feel across applications, significantly reducing the effort required in customizing and branding apps. The ability to automatically update the styles of all controls based on the set theme simplifies the design process and ensures that applications remain visually coherent throughout. This approach aligns with the needs of modern businesses seeking to maintain brand consistency while offering high-quality digital experiences. The modern controls also emphasize accessibility and performance, ensuring that applications are usable by a wide range of audiences, including those with disabilities, aligning with inclusive design principles. As such, the modern controls in canvas apps aren't just a set of UI components but a transformative toolset that empowers developers to build more efficient, maintainable, accessible, and cohesive applications that meet the evolving needs of businesses and users alike.

> [!IMPORTANT]
> While a subset of the modern controls in canvas apps is generally available (GA), the broader feature set remains in preview. Explore and provide feedback on these preview controls. However, keep in mind that features and functionalities might change based on feedback and testing before they reach general availability.

## Forms design and guidelines

This section provides best practices for designing forms in Power Apps, including organizing your form, reusing forms, form modes, and control placement.

### Organize your form

- Divide your form into logical sections and group related fields together.
- Aim to keep your form on a single screen. If it's lengthy, consider dividing it into multiple screens, steps, or tabs.
- Use clear and simple language for field labels and avoid unfamiliar terms or jargon.
- Implement validation rules to ensure data accuracy. For mandatory fields, clearly indicate that they're required. Validate email addresses, phone numbers, and other formats as needed.

### Reuse forms

- Use a single form for creating new records, editing existing records, and displaying records in view-only mode.
- Reuse the same form to reduce development and maintenance time while ensuring consistency.

### Form modes

Set the form mode dynamically based on user actions. For example:

- When creating a new record, set the form to "New" mode.
- When editing an existing record, set the form to "Edit" mode.
- When displaying a record, set the form to "View" mode.

### Control placement

- Place different controls (such as gallery, display form, and edit form) on separate screens to make them distinguishable.
- Combine these controls with formulas to create a cohesive user experience.

## Containers

As the canvas app grows to address more business scenarios, the number of controls increases, and you need to organize the controls based on their function. One way to do this is to group the controls. However, grouping controls isn't always recommended. The canvas app `Container` control holds a set of controls and has its own properties.

Containers function as empty spaces where you can insert and organize controls in relation to the top-left corner of the container. You can nest containers, allowing you to create more complex layouts and manage related controls together.

Containers are actual controls with their own properties like `Width` and `BorderColor`. Containers affect app layout and help screen reader users understand the structure of the app.

While you can add any controls in a group, you should only add logically related controls in a container.

Organizing elements in Power Apps using groups allows users to apply shared properties to multiple elements. However, making individual property changes within a group might require manual adjustments. Groups aren't part of the logical structure of an app for accessibility reasons because screen readers can't recognize them. The inability to nest groups also makes creating intricate layouts challenging.

## Gallery design and guidelines

The Gallery control in Power Apps allows you to display and interact with data. Keep the following best practices in mind when designing galleries to ensure optimal performance and user experience.

- **Avoid changing gallery items from within**: Don't modify the `Items` property of a gallery within child controls' events like `OnChange` or `OnSelect`. This action can cause unexpected behavior, especially when dealing with controls that trigger events when their values change.

- **Be cautious with OnChange triggered controls**: Be cautious when using controls like Combo box, Date picker, Slider, or Toggle in galleries. These controls might trigger the `OnChange` event unexpectedly, which can lead to potential issues like infinite loops.

- **Assess performance impact on patching**: Consider the performance impact when patching or updating items in a gallery, especially when dealing with many items. Patching can be slow, and the gallery might reload all items, which affects performance.

- **Handle infinite loops with care**: If modifying gallery data triggers events that lead to infinite loops, use modern controls or controls that don't trigger `OnChange` when their data changes to break the loop.

- **Avoid nested galleries**: Nested galleries can lead to performance issues and complex data binding. Whenever possible, avoid nesting galleries. Instead, try to design your data structure and use functions in an optimized way.

- **Use flexible height galleries**: Fixed-height galleries might limit content visibility, especially when dealing with dynamic data. Use flexible height galleries by setting the `Height` property to `Parent.Height` or a dynamic value based on your data. This setting ensures that the gallery adjusts its height to accommodate varying amounts of data.

    :::image type="content" source="media/image11.png" alt-text="Screenshot of Power Apps Studio with Blank flexible height gallery highlighted.":::

- **Optimize data loading**: When you optimize data loading in Power Apps, fetch and display only the necessary columns in a gallery instead of retrieving the entire dataset.

    Here's an example of how you can achieve this optimization. Suppose you have a collection named `ProductSales` with multiple columns, but you want to display only the "ProductName" and "QuantitySold" columns in a gallery.

    ```powerappsfl
    // Collection named ProductSales with sample sales data
    
    ClearCollect(ProductSales, 
        Table(
            { ProductName: "Phone", UnitPrice: 499.99, QuantitySold: 100 },
            { ProductName: "Laptop", UnitPrice: 999.99, QuantitySold: 50 },
            { ProductName: "Tablet", UnitPrice: 299.99, QuantitySold: 75 }
        )
    )
    
    // Bind the gallery to display only the "ProductName" and "QuantitySold" columns
    
    Gallery1.Items = ShowColumns(ProductSales, ProductName, QuantitySold)
    ```

Learn more about [Gallery best practices](/power-apps/maker/canvas-apps/gallery-best-practice).

## Build reusable components with Power Apps Component Framework (PCF)

Power Platform enables you to create reusable components through the Power Apps Component Framework (PCF). Learn more in [Power Apps Component Framework overview](/power-apps/developer/component-framework/overview).

Consider creating PCF components in Power Apps for the following scenarios:

- **Complex UI elements**: You need to create complex user interface elements or controls that aren't readily available in the standard Power Apps controls.

- **Custom controls for specific requirements**: Your app has specific requirements that aren't met by the out-of-the-box controls, and you need to create custom controls tailored to your needs.

- **Consistent user experience across apps**: You want to maintain a consistent user experience across multiple Power Apps or environments by encapsulating specific functionalities within a PCF component.

- **Reusability across apps**: You anticipate the need to reuse a specific piece of functionality or user interface element in multiple apps. Creating a PCF component allows you to build once and reuse.

- **Implementing advanced logic**: You need to implement advanced business logic or calculations that are beyond the capabilities of standard formulas or functions in Power Apps.

- **Improved user experience**: You aim to enhance the overall user experience by creating visually appealing and interactive components that aren't achievable with the default controls.

## Next step

> [!div class="nextstepaction"]
> [Responsive design guidelines](responsive-design-guidelines.md)
