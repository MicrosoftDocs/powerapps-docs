---
title: "Best practices for code components | Microsoft Docs"
description: "Learn best practices and get guidance on how to use code components created using Power Apps component framework."
author: anuitz
ms.author: anuitz
ms.date: 03/25/2024
ms.reviewer: jdaly
ms.topic: best-practice
ms.subservice: pcf
contributors:
 - JimDaly
 - v-scottdurow
---


# Best practices and guidance for code components created using Power Apps component framework

Developing, deploying, and maintaining code components needs a combination of knowledge that includes the following areas:

- Power Apps component framework
- Microsoft Power Apps
- TypeScript and JavaScript
- HTML Browser User Interface Development
- Azure DevOps/GitHub

This article outlines established best practices and guidance for professionals developing code components. This article aims to describe the benefits behind each so that your code components can take advantage of the usability, supportability, and performance improvements these tools and tips provide.

## Power Apps component framework

This section contains best practices and guidance related to Power Apps component framework itself.

### Avoid deploying development builds to Dataverse

Code components can be built in [production or development mode](code-components-alm.md#building-pcfproj-code-component-projects). Avoid deploying development builds to Dataverse since they adversely affect the performance and can even get blocked from deployment due to their size. Even if you plan to deploy a release build later, it can be easy to forget to redeploy if you don't have an automated release pipeline. More information: [Debugging custom controls](debugging-custom-controls.md).

### Avoid using unsupported framework methods

These include using undocumented internal methods that exist on the `ComponentFramework.Context`. These methods might work but, because they're not supported, they might stop working in future versions. Use of control script that accesses host application HTML Document Object Model (DOM) isn't supported. Any parts of the host application DOM that are outside the code component boundary, are subject to change without notice. 

### Use `init` method to request network required resources

When the hosting context loads a code component, the [init](reference\control\init.md) method is first called. Use this method to request any network resources such as metadata instead of waiting for the `updateView` method. If the `updateView` method is called before the requests return, your code component must handle this state and provide a visual loading indicator.

### Clean up resources inside the `destroy` method

The hosting context calls the [destroy](reference\control\destroy.md) method when a code component is removed from the browser DOM. Use the `destroy` method to close any `WebSockets` and remove  event handlers that are added outside of the container element. If you're using React, use `ReactDOM.unmountComponentAtNode` inside the `destroy` method. Cleaning up resources in this way prevents any performance issues caused by code components being loaded and unloaded within a given browser session.

### Avoid unnecessary calls to refresh on a dataset property

If your code component is of type dataset, the bound dataset properties expose a [`refresh`](reference\dataset\refresh.md) method that causes the hosting context to reload the data. Calling this method unnecessarily impacts the performance of your code component.

### Minimize calls to `notifyOutputChanged`

In some circumstances, it's undesirable for updates to a UI control (such as keypresses or mouse move events) to each call `notifyOutputChanged`, as more calls to `notifyOutputChanged` would result in many more events propagating to the parent context than needed. Instead, consider using an event when a control loses focus, or when the user's touch or mouse event completes.

### Check API availability

When developing code components for different hosts (model-driven apps, canvas apps, portals), always check the availability of the APIs you're using for support on those platforms. For example, `context.webAPI` isn't available in canvas apps. For individual API availability, see [Power Apps component framework API reference](reference/index.md).

### Manage temporarily null property values passed to `updateView`

Null values are passed to the `updateView` method when data isn't ready. Your components should account for this situation and expect that the data could be null, and that a subsequent `updateView` cycle can include updated values. `updateView` is available for both [standard](reference/control/updateview.md) and [React](reference/react-control/updateview.md) components.

## Model-driven apps

This section contains best practices and guidance relating to code components within model-driven apps.

### Don't interact directly with `formContext`

If you have experience working with client API, you might be used to interacting with `formContext` to access attributes, controls, and call API methods such as `save`, `refresh`, and `setNotification`. Code components are expected to work across various products like model-driven apps, canvas apps, and dashboards, therefore they can't have a dependency on `formContext`.

A workaround is to make the code component bound to a column and add an `OnChange` event handler to that column. The code component can update the column value, and the `OnChange` event handler can access the `formContext`. Support for the custom events will be added in the future, which will enable communicating changes outside of a control without adding a column configuration.

### Limit size and frequency of calls to the `WebApi`

When using the `context.WebApi` methods, limit both the number of calls and the amount of data. Each time you call the `WebApi`, it counts towards the user's API entitlement and service protection limits. When performing CRUD operations on records, consider the size of the payload. In general, the larger the request payload, the slower your code component is.

## Canvas apps

This section contains best practices and guidance relating to code components within canvas apps.

### Minimize the number of components on a screen

Each time you add a component to your canvas app, it takes a finite amount of time to render. Render time increases with each component you add. Carefully measure the performance of your code components as you add more to a screen using the Developer Performance tools.

Currently, each code component bundles their own library of shared libraries such as Fluent UI and React. Loading multiple instances of the same library won't load these libraries multiple times. However, loading multiple different code components results in the browser loading multiple bundled versions of these libraries. In the future, these libraries will be able to be loaded and shared with code components.

### Allow makers to style your code component

When app makers consume code components from inside a canvas app, they want to use a style that matches the rest of their app. Use input properties to provide customization options for theme elements such as color and size. When using Microsoft Fluent UI, map these properties to the theme elements provided by the library. In the future, theming support will be added to code components to make this process easier.

### Follow canvas apps performance best practices

Canvas apps provide a wide set of best practices from inside the app and solution checker. Ensure your apps follow these recommendations before you add code components. For more information, see:

- [Tips to improve canvas app performance](/powerapps/maker/canvas-apps/performance-tips)
- [Considerations for optimized performance in Power Apps](https://powerapps.microsoft.com/blog/considerations-for-optimized-performance-in-power-apps/)

## TypeScript and JavaScript

This section contains best practices and guidance relating to TypeScript and JavaScript within code components.

### ES5 vs ES6

By default, code components target ES5 to support older browsers. If you don't want to support these older browsers, you can change the target to ES6 inside your `pcfproj` folder's `tsconfig.json`. More information: [ES5 vs ES6](debugging-custom-controls.md#es5-vs-es6).

### Module imports

Always bundle the modules that are required as part of your code component instead of using scripts that are required to be loading using the `SCRIPT` tag. For example, if you wanted to use a non-Microsoft charting API where the sample shows adding  `<script type="text/javascript" src="somechartlibrary.js></script>` to the page, this isn't supported inside a code component. Bundling all of the required modules isolates the code component from other libraries and also supports running in offline mode.

> [!NOTE]
> Support for shared libraries across components using library nodes in the component manifest is not yet supported.

### Linting

Linting is where a tool can scan the code for potential issues. The template used by [pac pcf init](/power-platform/developer/cli/reference/pcf#pac-pcf-init) installs the `eslint` module to your project and configures it by adding an `.eslintrc.json` file. `Eslint` requires configuring for TypeScript and React coding styles. It can also be used to fix some of these issues automatically where possible. To configure, at the command-line use:

```shell
npx eslint --init
```

Then answer the following questions when prompted:

- How would you like to use `ESLint`?
  Answer: **To check syntax, find problems, and enforce code style**

- What type of modules does your project use?
  Answer: **JavaScript modules (import/export)**

- Which framework does your project use?
  Answer: **React**

- Does your project use TypeScript? 
  Answer: **Yes**

- Where does your code run?
  Answer: **Browser**

- How would you like to define a style for your project?
  Answer: **Answer questions about your style**

- What format do you want your config file to be in?
  Answer: **JSON** (This answer updates the existing `.eslintrc.json`)

- What style of indentation do you use?
  Answer: **Spaces** (This indentation style is the Visual Studio Code default)

- What quotes do you use for strings?
  Answer: **Single**

- What line endings do you use?
  Answer: **Windows** (This line ending is the Visual Studio Code default [CRLF](https://developer.mozilla.org/docs/Glossary/CRLF) line endings style.)

- Do you require semicolons?
  Answer: **Yes**

> [!NOTE]
> You can customize this configuration to suit your particular needs (for example, if you are not using React). More information: [Getting started with ESLint](https://eslint.org/docs/user-guide/getting-started).

Before you can use `eslint`, you need to add some scripts to the `package.json`:

```json
 "scripts": {
    ...
    "lint": "eslint MY_CONTROL_NAME --ext .ts,.tsx",
    "lint:fix": "npm run lint -- --fix"
  }
```


The `eslint` script accepts the folder that contains your code. Replace **MY_CONTROL_NAME** to be the same name as the code component used when calling [pac pcf init](/power-platform/developer/cli/reference/pcf#pac-pcf-init).

Now at the command-line, you can use:

```shell
npm run lint:fix
```

This command changes the code in the project to match your chosen style, and it also reports some issues that are resolved later.

> [!NOTE]
> ESLint will point out problems with the template code initially (e.g. empty constructor). You can add inline comments to instruct ESLint to exclude the rules such as:
> `// eslint-disable-next-line @typescript-eslint/no-empty-function`
>
> Additionally, you can add files to ignore (for example, the automatically generated interfaces) by adding the following to the `.eslintrc.json`:
> ```
> "ignorePatterns": ["**/generated/*.ts"]
> ```
> More information: [ignorePatterns in config files](https://eslint.org/docs/user-guide/configuring/ignoring-code#ignorepatterns-in-config-files).

> [!TIP]
> You can install Visual Studio Code extension that uses the project's `.eslintrc.json` file to provide code highlighting for any issues detected, with the option to fix them directly inside the IDE. More information: [Managing Extensions in Visual Studio Code](https://code.visualstudio.com/docs/editor/extension-marketplace).


## HTML browser user interface development

This section contains best practices and guidance relating to HTML browser UI development.

### Use Microsoft Fluent UI React

[Fluent UI React](https://developer.microsoft.com/fluentui#/get-started/web) is the official [open source](https://github.com/microsoft/fluentui) React front-end framework designed to build experiences that fit seamlessly into a broad range of Microsoft products. Power Apps itself uses Fluent UI, meaning you are able to create UI that's consistent with the rest of your apps.

#### Use path-based imports from Fluent to reduce bundle size

Currently, the code component templates used with [pac pcf init](/power-platform/developer/cli/reference/pcf#pac-pcf-init) won't use tree-shaking, which is the process where `webpack` detects modules imported that aren't used and removes them. If you import from Fluent UI using the following command, it imports and bundles the entire library:

```typescript
import { Button } from '@fluentui/react'
```

To avoid importing and bundling the entire library, you can use path-based imports where the specific library component is imported using the explicit path:

```typescript
import { Button } from '@fluentui/react/lib/Button';
```

Using the specific path reduces your bundle size both in development and release builds.

You can take advantage of tree-shaking (which only affects release/production builds) by updating your `tsconfig.json` to use the following module configuration inside the `compilerOptions` section:

```json
"module": "es2015",
"moduleResolution": "node"
```

More information: [Fluent UI - Advanced usage](https://github.com/microsoft/fluentui/wiki/Advanced-Usage).

#### Optimize React rendering

When using React, it's important to follow React specific best practices regarding minimizing rendering of components, resulting in a more responsive UI. Following are some of the best practices:

- Only make a call to `ReactDOM.render` inside the `updateView` method when a bound property or framework aspect change requires the UI to reflect the change. You can use [updatedProperties](reference\updatedproperties.md) to determine what has changed.
- Use [PureComponent](https://reactjs.org/docs/react-api.html#reactpurecomponent) (with class components) or [React.memo](https://reactjs.org/docs/react-api.html#reactmemo) (with function components) where possible to avoid unnecessary re-renders of components when its input props haven't mutated.
- For large React components, deconstruct your UI into smaller components to improve performance.
- Avoid use of arrow functions and function binding inside the render function as these practices create a new callback closure with each render and cause the child component to always re-render when the parent component is rendered. Instead, use function binding in the constructor or use class field arrow functions. See [Handling Events - React](https://reactjs.org/docs/handling-events.html).

### Check accessibility

Ensure that code components are accessible so that keyboard only and screen-reader users can use them:

- Provide keyboard navigation alternatives to mouse/touch events. For example, if your component provides a drop-down list, ensure that a user can use tab to set focus and then navigate the options using the arrow keys.
- Ensure that `alt` and [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) (Accessible Rich Internet Applications) attributes are set so that screen readers announce an accurate representation of the code components interface. The Microsoft Fluent UI library makes using these attributes easy since many of the components are already accessible and screen reader-compatible.
- Modern browser developer tools offer helpful ways to inspect accessibility. Use these tools to look for common accessibility issues with your code component.

More information: [Create accessible canvas apps in Power Apps](/powerapps/maker/canvas-apps/accessible-apps).

### Always use asynchronous network calls

When making network calls, never use a synchronous blocking request since this causes the app to stop responding and result in slow performance. More information: [Interact with HTTP and HTTPS resources asynchronously](/powerapps/developer/model-driven-apps/best-practices/business-logic/interact-http-https-resources-asynchronously).

### Write code for multiple browsers

Model-driven apps, canvas apps, and portals all support multiple browsers. Be sure to only use techniques that are supported on all modern browsers, and test with a representative set of browsers for your intended audience.

- [Limits and configurations](/powerapps/maker/canvas-apps/limits-and-config)
- [Supported web browsers](/power-platform/admin/supported-web-browsers-and-mobile-devices)
- [Browsers used by office](/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins)

### Code components should plan for supporting multiple clients and screen formats

Code components can be rendered in multiple clients (model-driven apps, canvas apps, portals) and screen formats (mobile, tablet, web). When used in model-driven apps, dataset code components can be placed on main form grids, related record grids, subgrids, or dashboards. When used in canvas apps, code components can be placed inside responsive containers that resize\ dynamically using the configuration provided by the app maker.

- Using [`trackContainerResize`](reference\mode\trackcontainerresize.md) allows code components to respond to changes in the available width and height. In some cases, setting this renders a different UI that fits the space available. Using `allocatedHeight` and `allocatedWidth` can be combined with [`getFormFactor`](reference\client\getformfactor.md) to determine if the code component is running on a mobile, tablet, or web client. More information: See this [Choices picker tutorial](tutorial-create-model-driven-field-component.md). 
- Implementing [`setFullScreen`](reference\mode\setfullscreen.md) allows users to expand to use the entire available screen available where space is limited. More information: [Canvas app grid component](tutorial-create-canvas-dataset-component.md).
- If the code component can't provide a meaningful experience in the given container size, it should disable functionality appropriately and provide feedback to the user.

### Always use scoped CSS rules

When you implement styling to your code components using CSS, ensure that the CSS is scoped to your component using the automatically generated CSS classes applied to the container `DIV` element for your component. If your CSS is scoped globally, it might break the existing styling of the form or screen where the code component is rendered. If using a third party CSS framework, use a namespaced version of that framework or otherwise wrap that framework in a namespace either by hand or using a CSS preprocessor.

For example, if your namespace is `SampleNamespace` and your code component name is `LinearInputComponent`, you would add a custom CSS rule using:

```css
.SampleNamespace\.LinearInputComponent rule-name
```

### Avoid use of web storage objects

Code components shouldn't use the HTML web storage objects, like `window.localStorage` and `window.sessionStorage`, to store data. Data stored locally on the user's browser or mobile client isn't secure and not guaranteed to be available reliably.

## ALM/Azure DevOps/GitHub

See the article on [Code component application lifecycle management (ALM)](code-components-alm.md) for best practices on code components with ALM/Azure DevOps/GitHub.

## Related articles

- [What are code components](custom-controls-overview.md)
- [Code components for canvas apps](component-framework-for-canvas-apps.md)
- [Create and build a code component](create-custom-controls-using-pcf.md)
- [Learn Power Apps component framework](/training/paths/use-power-apps-component-framework)
- [Use code components in Power Pages](../../maker/portals/component-framework.md)
