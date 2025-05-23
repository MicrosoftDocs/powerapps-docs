---
title: "Create canvas app dataset component in Microsoft Dataverse | MicrosoftDocs"
description: "In this tutorial, learn how to create a canvas app dataset code component, and deploy, add to a screen, and test the component using Visual Studio Code."
author: anuitz
ms.author: anuitz
ms.date: 02/20/2023
ms.reviewer: jdaly
ms.topic: tutorial
ms.subservice: pcf
contributors:
 - JimDaly
 - v-scottdurow
---

# Tutorial: Creating a canvas app dataset component

In this tutorial, you'll create a canvas app dataset code component, deploy it, add it to a screen, and test the component using Visual Studio Code. The code component displays a paged, scrollable dataset grid that provides sortable and filterable columns. It also allows the highlighting of specific rows by configuring an indicator column. This is a common request from app makers and can be complex to implement using native canvas app components. Code components can be written to work on both canvas and model-driven apps. However, this component is written to specifically target use within canvas apps.

In addition to these requirements, you'll also ensure the code component follows best practice guidance:

1. Use of [Microsoft Fluent UI](code-components-best-practices.md#use-microsoft-fluent-ui-react)
1. Localization of the code component labels at both design and runtime
1. Assurance that the code component renders at the width and height provided by the parent canvas app screen
1. Consideration for the app maker to customize the user interface using input properties and external app elements as far as possible

:::image type="content" source="media/canvas-datagrid-demo.gif" alt-text="Canvas Grid Demo":::

> [!NOTE]
> Before you start, make sure you've installed all the [prerequisite components](implementing-controls-using-typescript.md#prerequisites).


## Code

You can download the complete sample from [PowerApps-Samples/component-framework/CanvasGridControl/](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/CanvasGridControl).

## Create a new `pcfproj` project

1. Create a new folder to use for your code component. For example, `C:\repos\CanvasGrid`.

1. Open **Visual Studio Code** and then **File** > **Open Folder** and select the `CanvasGrid` folder. If you've added the Windows Explorer extensions during installation of Visual Studio Code, you can use the **Open with Code** context menu option inside the folder. You can also load any folder into Visual Studio Code using `code .` at the command prompt when the current directory is set to that location.

1. Inside a new Visual Studio Code PowerShell terminal (**Terminal** > **New Terminal**), use the [pac pcf init](/power-platform/developer/cli/reference/pcf#pac-pcf-init) command to create a new code component project:

   ```powershell
   pac pcf init --namespace SampleNamespace --name CanvasGrid --template dataset
   ```

   or using the short form:

   ```powershell
   pac pcf init -ns SampleNamespace -n CanvasGrid -t dataset
   ```

1. This adds a new `pcfproj` and related files to the current folder, including a `packages.json` that defines the modules needed. To install the required modules, use [npm install](https://docs.npmjs.com/cli/v8/commands/npm-install):

   ```CLI
   npm install
   ```

   > [!NOTE]
   >
   > If you receive the message, `The term 'npm' is not recognized as the name of a cmdlet, function, script file, or operable program.`, make sure you've installed all the prerequisites, specifically [node.js](https://nodejs.org/en/download/) (LTS version is recommended).

   :::image type="content" source="media/canvas-datagrid-1.gif" alt-text="Canvas dataset grid":::

The template includes an `index.ts` file along with various configuration files. This is the starting point of your code component and contains the lifecycle methods described in [Component implementation](custom-controls-overview.md#component-implementation).

### Install Microsoft Fluent UI

You'll be using Microsoft Fluent UI and React for creating UI, so you must install these as dependencies. Use the following at the terminal:

```powershell
npm install react react-dom @fluentui/react
```

This adds the modules to the `packages.json` and installs them into the `node_modules` folder. You won't commit `node_modules` into source control since all the required modules can be restored using `npm install`.

One of the advantages of Microsoft Fluent UI is that it provides a consistent and highly [accessible](code-components-best-practices.md#check-accessibility) UI.

### Configuring `eslint`

The template used by [pac pcf init](/power-platform/developer/cli/reference/pcf#pac-pcf-init) installs the `eslint` module to your project and configures it by adding an `.eslintrc.json` file. `Eslint` now requires configuring for TypeScript and React coding styles. More information: [Linting - Best practices and guidance for code components](code-components-best-practices.md#linting).

## Define the dataset properties

The `CanvasGrid\ControlManifest.Input.xml` file defines the metadata describing the behavior of the code component. The [control](manifest-schema-reference/control.md) attribute will already contain the namespace and name of the component.

[!INCLUDE [cc_tip-format-xml](includes/cc_tip-format-xml.md)]

You must define the records that the code component can be bound to, by adding the following inside the `control` element, replacing the existing `data-set` element:

#### [Before](#tab/before)

```xml
<data-set name="sampleDataSet"
  display-name-key="Dataset_Display_Key">
</data-set>
```

#### [After](#tab/after)

```xml
<data-set name="records"
  display-name-key="Records_Dataset_Display">
  <property-set name="HighlightIndicator"
    display-name-key="HighlightIndicator_Disp"
    description-key="HighlightIndicator_Desc"
    of-type="SingleLine.Text"
    usage="bound"
    required="true" />
</data-set>
```

---

The records [data-set](manifest-schema-reference\data-set.md) will be bound to a data source when the code component is added to a canvas app. The [property-set](manifest-schema-reference\property-set.md) indicates that the user must configure one of the columns of that dataset to be used as the row highlight indicator.

> [!TIP]
> You can specify multiple dataset elements. This could be useful if you wanted to search one dataset but show a list of records using a second.

### Defining the input and output properties

In addition to the dataset, you can provide the following **input** properties:

- `HighlightValue` - Allows the app maker to provide a value to be compared against the column defined as the `HighlightIndicator` `property-set`. When the values are equal, the row should be highlighted.
- `HighlightColor` - Allows the app maker to select a color to use to highlight rows.

> [!TIP]
> When creating code components for use in canvas apps, it's recommended to provide input properties for the styling of common aspects of your code components.

In addition to the input properties, an **output** property named `FilteredRecordCount` will be updated (and triggers the `OnChange` event) when the rows count is changed because of a filter action applied inside the code component. This is helpful when you want to show a `No Rows Found` message inside the parent app.

> [!NOTE]
> In the future, code components will support custom events so that you can define a specific event rather than using the generic `OnChange` event.

To define these three properties, add the following to the `CanvasGrid\ControlManifest.Input.xml` file, *below* the `data-set` element:

```xml
<property name="FilteredRecordCount"
  display-name-key="FilteredRecordCount_Disp"
  description-key="FilteredRecordCount_Desc"
  of-type="Whole.None"
  usage="output" />
<property name="HighlightValue"
  display-name-key="HighlightValue_Disp"
  description-key="HighlightValue_Desc"
  of-type="SingleLine.Text"
  usage="input"
  required="true"/>
<property name="HighlightColor"
  display-name-key="HighlightColor_Disp"
  description-key="HighlightColor_Desc"
  of-type="SingleLine.Text"
  usage="input"
  required="true"/>
```

**Save** this file and then, at the command-line, use:

```powershell
npm run build
```

> [!NOTE]
> If you get an error like this while running `npm run build`:
> 
> ```powershell
> [2:48:57 PM] [build]  Running ESLint...
> [2:48:57 PM] [build]  Failed:
> [pcf-1065] [Error] ESLint validation error:
> C:\repos\CanvasGrid\CanvasGrid\index.ts
>   2:47  error  'PropertyHelper' is not defined  no-undef
> ```
> 
> Open index.ts file and add this: `// eslint-disable-next-line no-undef`, directly above the line:<br />
> `import DataSetInterfaces = ComponentFramework.PropertyHelper.DataSetApi;`
>
> The run `npm run build` again.


After the component is built, you'll see that:

- An automatically generated file `CanvasGrid\generated\ManifestTypes.d.ts` is added to your project. This is generated as part of the build process from the `ControlManifest.Input.xml` and provides the types for interacting with the input/output properties.
- The build output is added to the `out` folder. The `bundle.js` is the transpiled JavaScript that runs inside the browser, and the `ControlManifest.xml` is a reformatted version of the `ControlManifest.Input.xml` file that's used during deployment.

   > [!NOTE]
   > Do not modify the contents of the `generated` and `out` folders directly. They'll be overwritten as part of the build process.

## Add the Grid Fluent UI React component

When the code component uses React, there must be a single root component that's rendered within the [updateView method](reference/control/updateview.md). Inside the `CanvasGrid` folder, add a new TypeScript file named `Grid.tsx`, and add the following content:

```typescript
import {
    DetailsList,
    ConstrainMode,
    DetailsListLayoutMode,
    IColumn,
    IDetailsHeaderProps,
} from '@fluentui/react/lib/DetailsList';
import { Overlay } from '@fluentui/react/lib/Overlay';
import { 
   ScrollablePane, 
   ScrollbarVisibility 
} from '@fluentui/react/lib/ScrollablePane';
import { Stack } from '@fluentui/react/lib/Stack';
import { Sticky } from '@fluentui/react/lib/Sticky';
import { StickyPositionType } from '@fluentui/react/lib/Sticky';
import { IObjectWithKey } from '@fluentui/react/lib/Selection';
import { IRenderFunction } from '@fluentui/react/lib/Utilities';
import * as React from 'react';

type DataSet = ComponentFramework.PropertyHelper.DataSetApi.EntityRecord & IObjectWithKey;

export interface GridProps {
    width?: number;
    height?: number;
    columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
    records: Record<string, ComponentFramework.PropertyHelper.DataSetApi.EntityRecord>;
    sortedRecordIds: string[];
    hasNextPage: boolean;
    hasPreviousPage: boolean;
    totalResultCount: number;
    currentPage: number;
    sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
    filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
    resources: ComponentFramework.Resources;
    itemsLoading: boolean;
    highlightValue: string | null;
    highlightColor: string | null;
}

const onRenderDetailsHeader: IRenderFunction<IDetailsHeaderProps> = (props, defaultRender) => {
    if (props && defaultRender) {
        return (
            <Sticky stickyPosition={StickyPositionType.Header} isScrollSynced>
                {defaultRender({
                    ...props,
                })}
            </Sticky>
        );
    }
    return null;
};

const onRenderItemColumn = (
    item?: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord,
    index?: number,
    column?: IColumn,
) => {
    if (column && column.fieldName && item) {
        return <>{item?.getFormattedValue(column.fieldName)}</>;
    }
    return <></>;
};

export const Grid = React.memo((props: GridProps) => {
    const {
        records,
        sortedRecordIds,
        columns,
        width,
        height,
        hasNextPage,
        hasPreviousPage,
        sorting,
        filtering,
        currentPage,
        itemsLoading,
    } = props;

    const [isComponentLoading, setIsLoading] = React.useState<boolean>(false);

    const items: (DataSet | undefined)[] = React.useMemo(() => {
        setIsLoading(false);

        const sortedRecords: (DataSet | undefined)[] = sortedRecordIds.map((id) => {
            const record = records[id];
            return record;
        });

        return sortedRecords;
    }, [records, sortedRecordIds, hasNextPage, setIsLoading]);

    const gridColumns = React.useMemo(() => {
        return columns
            .filter((col) => !col.isHidden && col.order >= 0)
            .sort((a, b) => a.order - b.order)
            .map((col) => {
                const sortOn = sorting && sorting.find((s) => s.name === col.name);
                const filtered =
                    filtering && 
                    filtering.conditions && 
                    filtering.conditions.find((f) => f.attributeName == col.name);
                return {
                    key: col.name,
                    name: col.displayName,
                    fieldName: col.name,
                    isSorted: sortOn != null,
                    isSortedDescending: sortOn?.sortDirection === 1,
                    isResizable: true,
                    isFiltered: filtered != null,
                    data: col,
                } as IColumn;
            });
    }, [columns, sorting]);

    const rootContainerStyle: React.CSSProperties = React.useMemo(() => {
        return {
            height: height,
            width: width,
        };
    }, [width, height]);

    return (
        <Stack verticalFill grow style={rootContainerStyle}>
            <Stack.Item grow style={{ position: 'relative', backgroundColor: 'white' }}>
                <ScrollablePane scrollbarVisibility={ScrollbarVisibility.auto}>
                    <DetailsList
                        columns={gridColumns}
                        onRenderItemColumn={onRenderItemColumn}
                        onRenderDetailsHeader={onRenderDetailsHeader}
                        items={items}
                        setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
                        initialFocusedIndex={0}
                        checkButtonAriaLabel="select row"
                        layoutMode={DetailsListLayoutMode.fixedColumns}
                        constrainMode={ConstrainMode.unconstrained}
                    ></DetailsList>
                </ScrollablePane>
                {(itemsLoading || isComponentLoading) && <Overlay />}
            </Stack.Item>
        </Stack>
    );
});

Grid.displayName = 'Grid';
```

> [!NOTE]
> The file has the extension `tsx` which is a TypeScript file that supports XML style syntax used by React. It's compiled into standard JavaScript by the build process.

### Grid design notes

This section includes commons on the design of the `Grid.tsx` component.

#### It is a functional component

This is a React *functional component*, but equally, it could be a *class component*. This is based on your preferred coding style. Class components and functional components can also be mixed in the same project. Both function and class components use the `tsx` XML style syntax used by React. More information: [Function and Class Components](https://reactjs.org/docs/components-and-props.html#function-and-class-components)

#### Minimize bundle.js size

When importing the `ChoiceGroup` Fluent UI components using path-based imports, instead of:

```typescript
import { 
    DetailsList, 
    ConstrainMode, 
    DetailsListLayoutMode, 
    IColumn, 
    IDetailsHeaderProps, 
    Stack 
} from "@fluentui/react";
```

This code uses:

```typescript
import {
    DetailsList,
    ConstrainMode,
    DetailsListLayoutMode,
    IColumn,
    IDetailsHeaderProps,
} from '@fluentui/react/lib/DetailsList';
import { Stack } from '@fluentui/react/lib/Stack';
```

This way, your bundle size will be smaller, resulting in lower capacity requirements and better runtime performance.

An alternative would be to use [tree-shaking.](code-components-best-practices.md#use-path-based-imports-from-fluent-to-reduce-bundle-size)

#### Destructuring assignment

This code:

```typescript
export const Grid = React.memo((props: GridProps) => {
    const {
        records,
        sortedRecordIds,
        columns,
        width,
        height,
        hasNextPage,
        hasPreviousPage,
        sorting,
        filtering,
        currentPage,
        itemsLoading,
    } = props;
```

Uses [destructuring assignment](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment). In this way, you extract the attributes required to render from the props, rather than prefixing them with `props.` each time they're used.

The code also uses [React.memo](https://reactjs.org/docs/react-api.html#reactmemo) to wrap the functional component so that it won't render unless any of the input props have changed.

#### Use of React.useMemo

[React.useMemo](https://reactjs.org/docs/hooks-reference.html#usememo) is used in several places to ensure that the item array created is only mutated when the input props `options` or `configuration` change. This is a best practice of function components that reduces unnecessary renders of the child components.

#### Other items to note:

- The `DetailsList` in a `Stack` is wrapped because, later you'll add a footer element with the paging controls.
- The Fluent UI `Sticky` component is used to wrap the header columns (using `onRenderDetailsHeader`) so that they remain visible when scrolling the grid.
- `setKey` is passed to the `DetailsList` along with `initialFocusedIndex` so that when the current page changes, the scroll position and selection will be reset.
- The function `onRenderItemColumn` is used to render the cell contents. It accepts row item and uses [getFormattedValue](reference\entityrecord\getformattedvalue.md) to return the display value of the column. The [getValue](reference\entityrecord\getvalue.md) method returns a value that you could use to provide an alternative rendering. The advantage of `getFormattedValue` is that it contains a formatted string for columns of non-string types such as dates and lookups.
- The `gridColumns` block is mapping the object shape of the columns provided by the dataset context, onto the shape expected by the `DetailsList` columns prop. Since this is wrapped in the [React.useMemo](https://reactjs.org/docs/hooks-reference.html#usememo) hook, the output will only change when the `columns` or `sorting` props change. You can display the sort and filter icons on the columns where the sorting and filtering details provided by the code component context matches the column being mapped. The columns are sorted using the [`column.order`](reference\column.md#order) property to ensure that they're in the correct order on the grid as defined by the app maker.
- You're maintaining an internal state for `isComponentLoading` in our React component. This is because when the user selects sorting and filtering actions, you can grey out the grid as a visual cue until the `sortedRecordIds` are updated and the state is reset. There's an additional input prop called `itemsLoading` which is mapped to the [dataset.loading](reference\dataset.md#loading) property provided by the dataset context. Both flags are used to control the visual loading cue that's implemented using the Fluent UI `Overlay` component.

## Update index.ts

The next step is to make changes to the `index.ts` file to match properties defined in `Grid.tsx.`

### Add import statements and initialize icons

To the header of `index.ts`, replace the existing imports with the following:

#### [Before](#tab/before)

```typescript
import {IInputs, IOutputs} from './generated/ManifestTypes';
import DataSetInterfaces = ComponentFramework.PropertyHelper.DataSetApi;
type DataSet = ComponentFramework.PropertyTypes.DataSet;
```

#### [After](#tab/after)

```typescript
import { initializeIcons } from "@fluentui/react/lib/Icons";
import * as React from "react";
import * as ReactDOM from "react-dom";
import { IInputs, IOutputs } from "./generated/ManifestTypes";
import { Grid } from "./Grid";

initializeIcons(undefined, { disableWarnings: true });
```

---

> [!NOTE]
> The import of `initializeIcons` is required because this code uses the Fluent UI icon set. You call `initializeIcons` to load the icons inside the test harness. Inside canvas apps, they're already initialized.

### Add fields to the CanvasGrid class

Add the following fields to the `CanvasGrid` class:

#### [Before](#tab/before)

```typescript
export class CanvasGrid implements ComponentFramework.StandardControl<IInputs, IOutputs> {

    /**
     * Empty constructor.
     */
    constructor() {

    }
```

#### [After](#tab/after)

```typescript
export class CanvasGrid implements ComponentFramework.StandardControl<IInputs, IOutputs> {
    notifyOutputChanged: () => void;
    container: HTMLDivElement;
    context: ComponentFramework.Context<IInputs>;
    sortedRecordsIds: string[] = [];
    resources: ComponentFramework.Resources;
    isTestHarness: boolean;
    records: {
        [id: string]: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord;
    };
    currentPage = 1;
    filteredRecordCount?: number;

    /**
     * Empty constructor.
     */
    constructor() {

    }
```

---

### Update the init method

Add the following to `init`:

#### [Before](#tab/before)

```typescript
public init(
    context: ComponentFramework.Context<IInputs>, 
    notifyOutputChanged: () => void, 
    state: ComponentFramework.Dictionary, 
    container: HTMLDivElement): void {
    // Add control initialization code
}
```

#### [After](#tab/after)

```typescript
public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement): void {
    this.notifyOutputChanged = notifyOutputChanged;
    this.container = container;
    this.context = context;
    this.context.mode.trackContainerResize(true);
    this.resources = this.context.resources;
    this.isTestHarness = document.getElementById("control-dimensions") !== null;
}
```

---

The `init` function is called when the code component is first initialized on an app screen. You store a reference to the following:

- `notifyOutputChanged`: This is the callback provided that you call to notify the canvas app that one of the properties has changed.
- `container`:This is the DOM element to which you add your code component UI.
- `resources`:This is used to retrieve localized strings in the current user's language.

The [context.mode.trackContainerResize(true))](reference\mode\trackcontainerresize.md) is used so that `updateView` will be called when the code component changes size.

> [!NOTE]
> Currently, there's no way to determine if the code component is running inside the test harness. You need to detect if the `control-dimensions` `div` element is present as an indicator.

### Update the updateView method

Add the following to `updateView`:

#### [Before](#tab/before)

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): void {
    // Add code to update control view
}
```

#### [After](#tab/after)

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): void {
    const dataset = context.parameters.records;
    const paging = context.parameters.records.paging;
    const datasetChanged = context.updatedProperties.indexOf("dataset") > -1;
    const resetPaging =
        datasetChanged &&
        !dataset.loading &&
        !dataset.paging.hasPreviousPage &&
        this.currentPage !== 1;

    if (resetPaging) {
        this.currentPage = 1;
    }
    if (resetPaging || datasetChanged || this.isTestHarness) {
        this.records = dataset.records;
        this.sortedRecordsIds = dataset.sortedRecordIds;
    }

    // The test harness provides width/height as strings
    const allocatedWidth = parseInt(
        context.mode.allocatedWidth as unknown as string
    );
    const allocatedHeight = parseInt(
        context.mode.allocatedHeight as unknown as string
    );

    ReactDOM.render(
        React.createElement(Grid, {
            width: allocatedWidth,
            height: allocatedHeight,
            columns: dataset.columns,
            records: this.records,
            sortedRecordIds: this.sortedRecordsIds,
            hasNextPage: paging.hasNextPage,
            hasPreviousPage: paging.hasPreviousPage,
            currentPage: this.currentPage,
            totalResultCount: paging.totalResultCount,
            sorting: dataset.sorting,
            filtering: dataset.filtering && dataset.filtering.getFilter(),
            resources: this.resources,
            itemsLoading: dataset.loading,
            highlightValue: this.context.parameters.HighlightValue.raw,
            highlightColor: this.context.parameters.HighlightColor.raw,
        }),
        this.container
    );
}
```

---

You can see that:

- You call [React.createElement](https://reactjs.org/docs/react-api.html#createelement), passing the reference to the DOM container you received inside the `init` function.
- The `Grid` component is defined inside `Grid.tsx` and is imported at the top of the file.
- The `allocatedWidth` and `allocatedHeight` will be provided by the parent context whenever they change (for example, the app resizes the code component or you enter full screen mode), since you made a call to [trackContainerResize(true)](reference\mode\trackcontainerresize.md) inside the `init` function.
- You can detect when there are new rows to display when the [updatedProperties](reference\updatedproperties.md) array contains the `dataset` string.
- In the test harness, the `updatedProperties` array is not populated, so you can use the `isTestHarness` flag you set in the `init` function to short-circuit the logic that sets the `sortedRecordId` and `records`. You maintain a reference to the current values until they change, so that you don't mutate these when passed to the child component unless a re-render of the data is required.
- Since the code component maintains the state of which page displayed, the page number is reset when the parent context resets the records to the first page. You know when you're back on the first page when `hasPreviousPage` is false.


### Update the destroy method

Lastly, you need to tidy up when the code component is destroyed:

#### [Before](#tab/before)

```typescript
public destroy(): void {
    // Add code to cleanup control if necessary
}
```

#### [After](#tab/after)

```typescript
public destroy(): void {
    ReactDOM.unmountComponentAtNode(this.container);
}
```

More information: [ReactDOM.unmountComponentAtNode](https://reactjs.org/docs/react-dom.html#unmountcomponentatnode)

---

## Start the test harness

Ensure all the files are saved and at the terminal use:

```powershell
npm start watch
```

You need to set the width and height to see the code component grid that's populated using the sample three records. You can then export a set of records into a CSV file from Dataverse and then load it into the test harness using **Data Inputs** > **Records panel**:

:::image type="content" source="media/canvas-datagrid-2.gif" alt-text="Test Harness":::

Here is some comma separated sample data you can save to a .csv file and use:

```text
address1_city,address1_country,address1_stateorprovince,address1_line1,address1_postalcode,telephone1,emailaddress1,firstname,fullname,jobtitle,lastname
Seattle,U.S.,WA,7842 Ygnacio Valley Road,12150,555-0112,someone_m@example.com,Thomas,Thomas Andersen (sample),Purchasing Manager,Andersen (sample)
Renton,U.S.,WA,7165 Brock Lane,61795,555-0109,someone_j@example.com,Jim,Jim Glynn (sample),Owner,Glynn (sample)
Snohomish,U.S.,WA,7230 Berrellesa Street,78800,555-0106,someone_g@example.com,Robert,Robert Lyon (sample),Owner,Lyon (sample)
Seattle,U.S.,WA,931 Corte De Luna,79465,555-0111,someone_l@example.com,Susan,Susan Burk (sample),Owner,Burk (sample)
Seattle,U.S.,WA,7765 Sunsine Drive,11910,555-0110,someone_k@example.com,Patrick,Patrick Sands (sample),Owner,Sands (sample)
Seattle,U.S.,WA,4948 West Th St,73683,555-0108,someone_i@example.com,Rene,Rene Valdes (sample),Purchasing Assistant,Valdes (sample)
Redmond,U.S.,WA,7723 Firestone Drive,32147,555-0107,someone_h@example.com,Paul,Paul Cannon (sample),Purchasing Assistant,Cannon (sample)
Issaquah,U.S.,WA,989 Caravelle Ct,33597,555-0105,someone_f@example.com,Scott,Scott Konersmann (sample),Purchasing Manager,Konersmann (sample)
Issaquah,U.S.,WA,7691 Benedict Ct.,57065,555-0104,someone_e@example.com,Sidney,Sidney Higa (sample),Owner,Higa (sample)
Monroe,U.S.,WA,3747 Likins Avenue,37925,555-0103,someone_d@example.com,Maria,Maria Campbell (sample),Purchasing Manager,Campbell (sample)
Duvall,U.S.,WA,5086 Nottingham Place,16982,555-0102,someone_c@example.com,Nancy,Nancy Anderson (sample),Purchasing Assistant,Anderson (sample)
Issaquah,U.S.,WA,5979 El Pueblo,23382,555-0101,someone_b@example.com,Susanna,Susanna Stubberod (sample),Purchasing Manager,Stubberod (sample)
Redmond,U.S.,WA,249 Alexander Pl.,86372,555-0100,someone_a@example.com,Yvonne,Yvonne McKay (sample),Purchasing Manager,McKay (sample)
```

> [!NOTE]
> There's only a single column shown in the test harness regardless of the columns you provide in the loaded CSV file. This is because the test harness only shows `property-set` when there is one defined. If no `property-set` is defined, then all of the columns in the loaded CSV file will be populated.

## Add row selection

Although the Fluent UI `DetailsList` allows selecting records by default, the selected records are not linked to the output of the code component. You need the `Selected` and `SelectedItems` properties to reflect the chosen records inside a canvas app, so that related components can be updated. In this example, you allow selection of only a single item at a time so `SelectedItems` will only ever contain a single record.

### Update Grid.tsx imports

Add the following to the imports inside `Grid.tsx`:

#### [Before](#tab/before)

```typescript
import {
    DetailsList,
    ConstrainMode,
    DetailsListLayoutMode,
    IColumn,
    IDetailsHeaderProps,
} from '@fluentui/react/lib/DetailsList';
import { Overlay } from '@fluentui/react/lib/Overlay';
import { 
   ScrollablePane, 
   ScrollbarVisibility 
} from '@fluentui/react/lib/ScrollablePane';
import { Stack } from '@fluentui/react/lib/Stack';
import { Sticky } from '@fluentui/react/lib/Sticky';
import { StickyPositionType } from '@fluentui/react/lib/Sticky';
import { IObjectWithKey } from '@fluentui/react/lib/Selection';
import { IRenderFunction } from '@fluentui/react/lib/Utilities';
import * as React from 'react';
```

#### [After](#tab/after)

```typescript
import {
    DetailsList,
    ConstrainMode,
    DetailsListLayoutMode,
    IColumn,
    IDetailsHeaderProps,
} from '@fluentui/react/lib/DetailsList';
import { Overlay } from '@fluentui/react/lib/Overlay';
import { 
   ScrollablePane, 
   ScrollbarVisibility 
} from '@fluentui/react/lib/ScrollablePane';
import { Stack } from '@fluentui/react/lib/Stack';
import { Sticky } from '@fluentui/react/lib/Sticky';
import { StickyPositionType } from '@fluentui/react/lib/Sticky';
import { IObjectWithKey } from '@fluentui/react/lib/Selection';
import { IRenderFunction } from '@fluentui/react/lib/Utilities';
import * as React from 'react';
import { useConst, useForceUpdate } from "@fluentui/react-hooks";
import { Selection } from "@fluentui/react/lib/Selection";
import { SelectionMode } from "@fluentui/react/lib/Utilities";
```

---

### Add setSelectedRecords to GridProps

To the `GridProps` interface, inside `Grid.tsx`, add the following:

#### [Before](#tab/before)

```typescript
export interface GridProps {
    width?: number;
    height?: number;
    columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
    records: Record<string, ComponentFramework.PropertyHelper.DataSetApi.EntityRecord>;
    sortedRecordIds: string[];
    hasNextPage: boolean;
    hasPreviousPage: boolean;
    totalResultCount: number;
    currentPage: number;
    sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
    filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
    resources: ComponentFramework.Resources;
    itemsLoading: boolean;
    highlightValue: string | null;
    highlightColor: string | null;
}
```

#### [After](#tab/after)

```typescript
export interface GridProps {
    width?: number;
    height?: number;
    columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
    records: Record<string, ComponentFramework.PropertyHelper.DataSetApi.EntityRecord>;
    sortedRecordIds: string[];
    hasNextPage: boolean;
    hasPreviousPage: boolean;
    totalResultCount: number;
    currentPage: number;
    sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
    filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
    resources: ComponentFramework.Resources;
    itemsLoading: boolean;
    highlightValue: string | null;
    highlightColor: string | null;
    setSelectedRecords: (ids: string[]) => void;
}
```

---

### Add the setSelectedRecords property to Grid

Inside the `Grid.tsx` function component, update the destructuring of the `props` to add the new prop `setSelectedRecords`.

#### [Before](#tab/before)

```typescript
export const Grid = React.memo((props: GridProps) => {
    const {
        records,
        sortedRecordIds,
        columns,
        width,
        height,
        hasNextPage,
        hasPreviousPage,
        sorting,
        filtering,
        currentPage,
        itemsLoading,
    } = props;
```

#### [After](#tab/after)

```typescript
export const Grid = React.memo((props: GridProps) => {
    const {
        records,
        sortedRecordIds,
        columns,
        width,
        height,
        hasNextPage,
        hasPreviousPage,
        sorting,
        filtering,
        currentPage,
        itemsLoading,
        setSelectedRecords,
    } = props;
```

---

Directly below that, add:

```typescript
const forceUpdate = useForceUpdate();
const onSelectionChanged = React.useCallback(() => {
  const items = selection.getItems() as DataSet[];
  const selected = selection.getSelectedIndices().map((index: number) => {
    const item: DataSet | undefined = items[index];
    return item && items[index].getRecordId();
  });

  setSelectedRecords(selected);
  forceUpdate();
}, [forceUpdate]);

const selection: Selection = useConst(() => {
  return new Selection({
    selectionMode: SelectionMode.single,
    onSelectionChanged: onSelectionChanged,
  });
});
```

The [React.useCallback](https://reactjs.org/docs/hooks-reference.html#usecallback) and [useConst](https://www.npmjs.com/package/@fluentui/react-hooks#useconst) hooks ensure that these values do not mutate between renders and cause unnecessary child component rendering.

The [useForceUpdate](https://www.npmjs.com/package/@fluentui/react-hooks#useforceupdate) hook ensures that when selection is updated, the component is re-rendered to reflect the updated selection count.

### Add selection to DetailsList

The `selection` object created to maintain the state of the selection is then passed into the `DetailsList` component:

#### [Before](#tab/before)

```typescript
<DetailsList
   columns={gridColumns}
   onRenderItemColumn={onRenderItemColumn}
   onRenderDetailsHeader={onRenderDetailsHeader}
   items={items}
   setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
   initialFocusedIndex={0}
   checkButtonAriaLabel="select row"
   layoutMode={DetailsListLayoutMode.fixedColumns}
   constrainMode={ConstrainMode.unconstrained}
></DetailsList>
```

#### [After](#tab/after)

```typescript
<DetailsList
   columns={gridColumns}
   onRenderItemColumn={onRenderItemColumn}
   onRenderDetailsHeader={onRenderDetailsHeader}
   items={items}
   setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
   initialFocusedIndex={0}
   checkButtonAriaLabel="select row"
   layoutMode={DetailsListLayoutMode.fixedColumns}
   constrainMode={ConstrainMode.unconstrained}
   selection={selection}
></DetailsList>
```

---

### Define the setSelectedRecords callback

You need to define the new `setSelectedRecords` callback inside `index.ts` and pass it to the `Grid` component. Near the top of `CanvasGrid` class, add the following:

#### [Before](#tab/before)

```typescript
export class CanvasGrid
  implements ComponentFramework.StandardControl<IInputs, IOutputs>
{
  notifyOutputChanged: () => void;
  container: HTMLDivElement;
  context: ComponentFramework.Context<IInputs>;
  sortedRecordsIds: string[] = [];
  resources: ComponentFramework.Resources;
  isTestHarness: boolean;
  records: {
    [id: string]: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord;
  };
  currentPage = 1;
  filteredRecordCount?: number;
```

#### [After](#tab/after)

```typescript
export class CanvasGrid
  implements ComponentFramework.StandardControl<IInputs, IOutputs>
{
  notifyOutputChanged: () => void;
  container: HTMLDivElement;
  context: ComponentFramework.Context<IInputs>;
  sortedRecordsIds: string[] = [];
  resources: ComponentFramework.Resources;
  isTestHarness: boolean;
  records: {
    [id: string]: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord;
  };
  currentPage = 1;
  filteredRecordCount?: number;

  setSelectedRecords = (ids: string[]): void => {
    this.context.parameters.records.setSelectedRecordIds(ids);
  };

```

---

> [!NOTE]
> The method is defined as an [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) to bind it to the current `this` instance of the code component.

The call to [setSelectedRecordIds](reference\dataset\setselectedrecordids.md) informs the canvas app that the selection has changed so that other components referencing `SelectedItems` and `Selected` will be updated.

### Add new callback to the input props

Finally, add the new callback to the input props of the `Grid` component in the `updateView` method:

#### [Before](#tab/before)

```typescript
ReactDOM.render(
 React.createElement(Grid, {
   width: allocatedWidth,
   height: allocatedHeight,
   columns: dataset.columns,
   records: this.records,
   sortedRecordIds: this.sortedRecordsIds,
   hasNextPage: paging.hasNextPage,
   hasPreviousPage: paging.hasPreviousPage,
   currentPage: this.currentPage,
   totalResultCount: paging.totalResultCount,
   sorting: dataset.sorting,
   filtering: dataset.filtering && dataset.filtering.getFilter(),
   resources: this.resources,
   itemsLoading: dataset.loading,
   highlightValue: this.context.parameters.HighlightValue.raw,
   highlightColor: this.context.parameters.HighlightColor.raw,
 }),
this.container
);
```

#### [After](#tab/after)

```typescript
ReactDOM.render(
 React.createElement(Grid, {
   width: allocatedWidth,
   height: allocatedHeight,
   columns: dataset.columns,
   records: this.records,
   sortedRecordIds: this.sortedRecordsIds,
   hasNextPage: paging.hasNextPage,
   hasPreviousPage: paging.hasPreviousPage,
   currentPage: this.currentPage,
   totalResultCount: paging.totalResultCount,
   sorting: dataset.sorting,
   filtering: dataset.filtering && dataset.filtering.getFilter(),
   resources: this.resources,
   itemsLoading: dataset.loading,
   highlightValue: this.context.parameters.HighlightValue.raw,
   highlightColor: this.context.parameters.HighlightColor.raw,
   setSelectedRecords: this.setSelectedRecords,
 }),
this.container
);
```

---

### Invoking the `OnSelect` event

There's a pattern in canvas apps where if a gallery or grid has an item selection invoked (for example, selecting a chevron icon), it raises the `OnSelect` event. You can implement this pattern using the [openDatasetItem](reference\dataset\opendatasetitem.md) method of the dataset.

#### Add onNavigate to GridProps interface

As before, you add an additional callback prop on the `Grid` component by adding the following to the `GridProps` interface inside `Grid.tsx`:

##### [Before](#tab/before)

```typescript
export interface GridProps {
  width?: number;
  height?: number;
  columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
  records: Record<
    string,
    ComponentFramework.PropertyHelper.DataSetApi.EntityRecord
  >;
  sortedRecordIds: string[];
  hasNextPage: boolean;
  hasPreviousPage: boolean;
  totalResultCount: number;
  currentPage: number;
  sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
  filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
  resources: ComponentFramework.Resources;
  itemsLoading: boolean;
  highlightValue: string | null;
  highlightColor: string | null;
  setSelectedRecords: (ids: string[]) => void;
}
```

##### [After](#tab/after)

```typescript
export interface GridProps {
  width?: number;
  height?: number;
  columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
  records: Record<
    string,
    ComponentFramework.PropertyHelper.DataSetApi.EntityRecord
  >;
  sortedRecordIds: string[];
  hasNextPage: boolean;
  hasPreviousPage: boolean;
  totalResultCount: number;
  currentPage: number;
  sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
  filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
  resources: ComponentFramework.Resources;
  itemsLoading: boolean;
  highlightValue: string | null;
  highlightColor: string | null;
  setSelectedRecords: (ids: string[]) => void;
  onNavigate: (item?: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord) => void;
}
```

---

#### Add onNavigate to Grid props

Again, you must add the new prop to the destructuring of the props:

##### [Before](#tab/before)

```typescript
export const Grid = React.memo((props: GridProps) => {
  const {
    records,
    sortedRecordIds,
    columns,
    width,
    height,
    hasNextPage,
    hasPreviousPage,
    sorting,
    filtering,
    currentPage,
    itemsLoading,
    setSelectedRecords,
  } = props;
```

##### [After](#tab/after)

```typescript
export const Grid = React.memo((props: GridProps) => {
  const {
    records,
    sortedRecordIds,
    columns,
    width,
    height,
    hasNextPage,
    hasPreviousPage,
    sorting,
    filtering,
    currentPage,
    itemsLoading,
    setSelectedRecords,
    onNavigate,
  } = props;
```

---

#### Add onItemInvoked to DetailsList

The `DetailList` has a callback prop called `onItemInvoked` which, in turn, you pass your callback to:

##### [Before](#tab/before)

```typescript
<DetailsList
   columns={gridColumns}
   onRenderItemColumn={onRenderItemColumn}
   onRenderDetailsHeader={onRenderDetailsHeader}
   items={items}
   setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
   initialFocusedIndex={0}
   checkButtonAriaLabel="select row"
   layoutMode={DetailsListLayoutMode.fixedColumns}
   constrainMode={ConstrainMode.unconstrained}
   selection={selection}
></DetailsList>
```

##### [After](#tab/after)

```typescript
<DetailsList
   columns={gridColumns}
   onRenderItemColumn={onRenderItemColumn}
   onRenderDetailsHeader={onRenderDetailsHeader}
   items={items}
   setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
   initialFocusedIndex={0}
   checkButtonAriaLabel="select row"
   layoutMode={DetailsListLayoutMode.fixedColumns}
   constrainMode={ConstrainMode.unconstrained}
   selection={selection}
   onItemInvoked={onNavigate}
></DetailsList>
```

---

#### Add onNavigate method to index.ts

Add the `onNavigate` method to the `index.ts` just below the `setSelectedRecords` method:

```typescript
onNavigate = (
  item?: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord
): void => {
  if (item) {
    this.context.parameters.records.openDatasetItem(item.getNamedReference());
  }
};
```

This simply invokes the `openDatasetItem` method on the dataset record so that the code component will raise the `OnSelect` event. The method is defined as an [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) to bind it to the current `this` instance of the code component.

You need to pass this callback into the `Grid` component props inside the `updateView` method:

##### [Before](#tab/before)

```typescript
    ReactDOM.render(
      React.createElement(Grid, {
        width: allocatedWidth,
        height: allocatedHeight,
        columns: dataset.columns,
        records: this.records,
        sortedRecordIds: this.sortedRecordsIds,
        hasNextPage: paging.hasNextPage,
        hasPreviousPage: paging.hasPreviousPage,
        currentPage: this.currentPage,
        totalResultCount: paging.totalResultCount,
        sorting: dataset.sorting,
        filtering: dataset.filtering && dataset.filtering.getFilter(),
        resources: this.resources,
        itemsLoading: dataset.loading,
        highlightValue: this.context.parameters.HighlightValue.raw,
        highlightColor: this.context.parameters.HighlightColor.raw,
        setSelectedRecords: this.setSelectedRecords,
      }),
      this.container
    );
```

##### [After](#tab/after)

```typescript
    ReactDOM.render(
      React.createElement(Grid, {
        width: allocatedWidth,
        height: allocatedHeight,
        columns: dataset.columns,
        records: this.records,
        sortedRecordIds: this.sortedRecordsIds,
        hasNextPage: paging.hasNextPage,
        hasPreviousPage: paging.hasPreviousPage,
        currentPage: this.currentPage,
        totalResultCount: paging.totalResultCount,
        sorting: dataset.sorting,
        filtering: dataset.filtering && dataset.filtering.getFilter(),
        resources: this.resources,
        itemsLoading: dataset.loading,
        highlightValue: this.context.parameters.HighlightValue.raw,
        highlightColor: this.context.parameters.HighlightColor.raw,
        setSelectedRecords: this.setSelectedRecords,
        onNavigate: this.onNavigate,
      }),
      this.container
    );
```

---

When you save all files, the test harness will reload. Use `Ctrl` + `Shift` + `I` (or `F12`) and use **Open File** (`Ctrl` + `P`) searching for `index.ts` and you can place a breakpoint inside the `onNavigate` method. Double-click on a row (or highlight it with the cursor keys and pressing `Enter`) will hit the breakpoint because the `DetailsList` invokes the `onNavigate` callback.

:::image type="content" source="media/canvas-datagrid-3.png" alt-text="Canvas Data Grid debug OnNavigate in index.ts":::

There is a reference to `_this` because the function is defined as an [arrow function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) and has been transpiled into a JavaScript closure to capture the instance of `this`.

## Add Localization

Before you go any further, you need to add resource strings to the code component so that you can use localized strings for messages such as paging, sorting, and filtering. Add a new file `CanvasGrid\strings\CanvasGrid.1033.resx` and use the Visual Studio resource editor or Visual Studio Code with an extension to enter the following:


|Name|Value|
|---------|---------|
|`Records_Dataset_Display`|Records|
|`FilteredRecordCount_Disp`|Filtered Record Count|
|`FilteredRecordCount_Desc`|The number of records after filtering|
|`HighlightValue_Disp`|Highlight Value|
|`HighlightValue_Desc`|The value to indicate a row should be highlighted|
|`HighlightColor_Disp`|Highlight Color|
|`HighlightColor_Desc`|The color to highlight a row using|
|`HighlightIndicator_Disp`|Highlight Indicator Field|
|`HighlightIndicator_Desc`|Set to the name of the field to compare against the Highlight Value|
|`Label_Grid_Footer`|Page {0} ({1} Selected)|
|`Label_SortAZ`|A to Z|
|`Label_SortZA`|Z to A|
|`Label_DoesNotContainData`|Does not contain data|
|`Label_ShowFullScreen`|Show Full Screen|

> [!TIP]
> It's not recommended to edit `resx` files directly. Instead, use either Visual Studio's resource editor or an extension for Visual Studio Code. Find a Visual Studio Code extension: [Search Visual Studio Marketplace for a resx editor](https://marketplace.visualstudio.com/search?term=resx%20editor&target=VSCode&category=All%20categories&sortBy=Relevance)

The data for this file can also be set by opening the `CanvasGrid.1033.resx` file in Notepad and copying the XML content below:

```xml
<?xml version="1.0" encoding="utf-8"?>
<root>
  <xsd:schema id="root" xmlns="" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:import namespace="http://www.w3.org/XML/1998/namespace"/>
    <xsd:element name="root" msdata:IsDataSet="true">
      <xsd:complexType>
        <xsd:choice maxOccurs="unbounded">
          <xsd:element name="metadata">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0"/>
              </xsd:sequence>
              <xsd:attribute name="name" use="required" type="xsd:string"/>
              <xsd:attribute name="type" type="xsd:string"/>
              <xsd:attribute name="mimetype" type="xsd:string"/>
              <xsd:attribute ref="xml:space"/>
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="assembly">
            <xsd:complexType>
              <xsd:attribute name="alias" type="xsd:string"/>
              <xsd:attribute name="name" type="xsd:string"/>
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="data">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1"/>
                <xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2"/>
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1"/>
              <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3"/>
              <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4"/>
              <xsd:attribute ref="xml:space"/>
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="resheader">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1"/>
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required"/>
            </xsd:complexType>
          </xsd:element>
        </xsd:choice>
      </xsd:complexType>
    </xsd:element>
  </xsd:schema>
  <resheader name="resmimetype">
    <value>text/microsoft-resx</value>
  </resheader>
  <resheader name="version">
    <value>2.0</value>
  </resheader>
  <resheader name="reader">
    <value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <resheader name="writer">
    <value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <data name="Records_Dataset_Display" xml:space="preserve">
    <value>Records</value>
  </data>
  <data name="FilteredRecordCount_Disp" xml:space="preserve">
    <value>Filtered Record Count</value>
  </data>
  <data name="FilteredRecordCount_Desc" xml:space="preserve">
    <value>The number of records after filtering</value>
  </data>
  <data name="HighlightValue_Disp" xml:space="preserve">
    <value>Highlight Value</value>
  </data>
  <data name="HighlightValue_Desc" xml:space="preserve">
    <value>The value to indicate a row should be highlighted</value>
  </data>
  <data name="HighlightColor_Disp" xml:space="preserve">
    <value>Highlight Color</value>
  </data>
  <data name="HighlightColor_Desc" xml:space="preserve">
    <value>The color to highlight a row using</value>
  </data>
  <data name="HighlightIndicator_Disp" xml:space="preserve">
    <value>Highlight Indicator Field</value>
  </data>
  <data name="HighlightIndicator_Desc" xml:space="preserve">
    <value>Set to the name of the field to compare against the Highlight Value</value>
  </data>
   <data name="Label_Grid_Footer" xml:space="preserve">
    <value>Page {0} ({1} Selected)</value>
  </data>
  <data name="Label_SortAZ" xml:space="preserve">
    <value>A to Z</value>
  </data>
  <data name="Label_SortZA" xml:space="preserve">
    <value>Z to A</value>
  </data>
  <data name="Label_DoesNotContainData" xml:space="preserve">
    <value>Does not contain data</value>
  </data>
  <data name="Label_ShowFullScreen" xml:space="preserve">
    <value>Show Full Screen</value>
  </data>
</root>
```

You have resource strings for the `input`/`output` properties and the `dataset` and associated `property-set`. These will be used in Power Apps Studio at design time based on the maker's browser language. You can also add label strings that can be retrieved at runtime using [getString](reference\resources\getstring.md). More information: [Implementing localization API component](sample-controls\localization-api-control.md).

Add this new resource file to the `ControlManifest.Input.xml` file inside the `resources` element:

##### [Before](#tab/before)

```xml
<resources>
   <code path="index.ts"
      order="1" />
</resources>
```

##### [After](#tab/after)

```xml
<resources>
   <code path="index.ts"
      order="1" />
   <resx path="strings/CanvasGrid.1033.resx"
      version="1.0.0" />
</resources>
```

---

### Add column sorting and filtering

If you want to allow the user to sort and filter using grid column headers, the Fluent UI `DetailList` provides an easy way of adding context menus to the column headers.

#### Add onSort and onFilter to GridProps

First, add `onSort` and `onFilter` to the `GridProps` interface inside `Grid.tsx` to provide callback functions for sorting and filtering:

##### [Before](#tab/before)

```typescript
export interface GridProps {
  width?: number;
  height?: number;
  columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
  records: Record<
    string,
    ComponentFramework.PropertyHelper.DataSetApi.EntityRecord
  >;
  sortedRecordIds: string[];
  hasNextPage: boolean;
  hasPreviousPage: boolean;
  totalResultCount: number;
  currentPage: number;
  sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
  filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
  resources: ComponentFramework.Resources;
  itemsLoading: boolean;
  highlightValue: string | null;
  highlightColor: string | null;
  setSelectedRecords: (ids: string[]) => void;
  onNavigate: (
    item?: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord
  ) => void;
}
```

##### [After](#tab/after)

```typescript
export interface GridProps {
  width?: number;
  height?: number;
  columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
  records: Record<
    string,
    ComponentFramework.PropertyHelper.DataSetApi.EntityRecord
  >;
  sortedRecordIds: string[];
  hasNextPage: boolean;
  hasPreviousPage: boolean;
  totalResultCount: number;
  currentPage: number;
  sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
  filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
  resources: ComponentFramework.Resources;
  itemsLoading: boolean;
  highlightValue: string | null;
  highlightColor: string | null;
  setSelectedRecords: (ids: string[]) => void;
  onNavigate: (
    item?: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord
  ) => void;
  onSort: (name: string, desc: boolean) => void;
  onFilter: (name: string, filtered: boolean) => void;
}
```

---

#### Add onSort, onFilter, and resources to props

Then, add these new props along with the `resources` reference (so you can retrieve localized labels for sorting and filtering) to the props destructuring:
##### [Before](#tab/before)

```typescript
export const Grid = React.memo((props: GridProps) => {
  const {
    records,
    sortedRecordIds,
    columns,
    width,
    height,
    hasNextPage,
    hasPreviousPage,
    sorting,
    filtering,
    currentPage,
    itemsLoading,
    setSelectedRecords,
    onNavigate,
  } = props;
```

##### [After](#tab/after)

```typescript
export const Grid = React.memo((props: GridProps) => {
  const {
    records,
    sortedRecordIds,
    columns,
    width,
    height,
    hasNextPage,
    hasPreviousPage,
    sorting,
    filtering,
    currentPage,
    itemsLoading,
    setSelectedRecords,
    onNavigate,
    onSort, 
    onFilter, 
    resources,
  } = props;
```

---

#### Import ContextualMenu components

You need to add some imports to the top of `Grid.tsx` so that you can use the `ContextualMenu` component provided by Fluent UI. You can use path-based imports to reduce the size of the bundle.

```typescript
import { ContextualMenu, DirectionalHint, IContextualMenuProps } from '@fluentui/react/lib/ContextualMenu';
```

#### Add context menu rendering functionality

Now add the context menu rendering functionality to `Grid.tsx` just below the line<br /> `const [isComponentLoading, setIsLoading] = React.useState<boolean>(false);`:

##### [Before](#tab/before)

```typescript
const [isComponentLoading, setIsLoading] = React.useState<boolean>(false);
```

##### [After](#tab/after)

```typescript
const [isComponentLoading, setIsLoading] = React.useState<boolean>(false);

const [contextualMenuProps, setContextualMenuProps] =
    React.useState<IContextualMenuProps>();

const onContextualMenuDismissed = React.useCallback(() => {
    setContextualMenuProps(undefined);
  }, [setContextualMenuProps]);

const getContextualMenuProps = React.useCallback(
    (
      column: IColumn,
      ev: React.MouseEvent<HTMLElement>
    ): IContextualMenuProps => {
      const menuItems = [
        {
          key: "aToZ",
          name: resources.getString("Label_SortAZ"),
          iconProps: { iconName: "SortUp" },
          canCheck: true,
          checked: column.isSorted && !column.isSortedDescending,
          disable: (
            column.data as ComponentFramework.PropertyHelper.DataSetApi.Column
          ).disableSorting,
          onClick: () => {
            onSort(column.key, false);
            setContextualMenuProps(undefined);
            setIsLoading(true);
          },
        },
        {
          key: "zToA",
          name: resources.getString("Label_SortZA"),
          iconProps: { iconName: "SortDown" },
          canCheck: true,
          checked: column.isSorted && column.isSortedDescending,
          disable: (
            column.data as ComponentFramework.PropertyHelper.DataSetApi.Column
          ).disableSorting,
          onClick: () => {
            onSort(column.key, true);
            setContextualMenuProps(undefined);
            setIsLoading(true);
          },
        },
        {
          key: "filter",
          name: resources.getString("Label_DoesNotContainData"),
          iconProps: { iconName: "Filter" },
          canCheck: true,
          checked: column.isFiltered,
          onClick: () => {
            onFilter(column.key, column.isFiltered !== true);
            setContextualMenuProps(undefined);
            setIsLoading(true);
          },
        },
      ];
      return {
        items: menuItems,
        target: ev.currentTarget as HTMLElement,
        directionalHint: DirectionalHint.bottomLeftEdge,
        gapSpace: 10,
        isBeakVisible: true,
        onDismiss: onContextualMenuDismissed,
      };
    },
    [setIsLoading, onFilter, setContextualMenuProps]
  );

const onColumnContextMenu = React.useCallback(
    (column?: IColumn, ev?: React.MouseEvent<HTMLElement>) => {
      if (column && ev) {
        setContextualMenuProps(getContextualMenuProps(column, ev));
      }
    },
    [getContextualMenuProps, setContextualMenuProps]
  );

const onColumnClick = React.useCallback(
    (ev: React.MouseEvent<HTMLElement>, column: IColumn) => {
      if (column && ev) {
        setContextualMenuProps(getContextualMenuProps(column, ev));
      }
    },
    [getContextualMenuProps, setContextualMenuProps]
  );
```

---

You'll see that:

- The `contextualMenuProps` state controls the visibility of the context menu that's rendered using the Fluent UI `ContextualMenu` component.
- This code provides a simple filter to show only values where the field doesn't contain any data. You could extend this to provide additional filtering.
- This code uses `resources.getString` to show labels on the context menu that can be localized.
- The `React.useCallback` hook, similar to `React.useMemo`, ensures that the callbacks are only mutated when the dependent values change. This optimizes the rendering of child components.

#### Add new context menu functions to the column select and context menu events

Add these new context menu functions to the column select and context menu events. Update the `const gridColumns` to add the `onColumnContextMenu` and `onColumnClick` callbacks:

##### [Before](#tab/before)

```typescript
const gridColumns = React.useMemo(() => {
   return columns
     .filter((col) => !col.isHidden && col.order >= 0)
     .sort((a, b) => a.order - b.order)
     .map((col) => {
       const sortOn = sorting && sorting.find((s) => s.name === col.name);
       const filtered =
         filtering &&
         filtering.conditions &&
         filtering.conditions.find((f) => f.attributeName == col.name);
       return {
         key: col.name,
         name: col.displayName,
         fieldName: col.name,
         isSorted: sortOn != null,
         isSortedDescending: sortOn?.sortDirection === 1,
         isResizable: true,
         isFiltered: filtered != null,
         data: col,
       } as IColumn;
     });
 }, [columns, sorting]);
```

##### [After](#tab/after)

```typescript
const gridColumns = React.useMemo(() => {
   return columns
     .filter((col) => !col.isHidden && col.order >= 0)
     .sort((a, b) => a.order - b.order)
     .map((col) => {
       const sortOn = sorting && sorting.find((s) => s.name === col.name);
       const filtered =
         filtering &&
         filtering.conditions &&
         filtering.conditions.find((f) => f.attributeName == col.name);
       return {
         key: col.name,
         name: col.displayName,
         fieldName: col.name,
         isSorted: sortOn != null,
         isSortedDescending: sortOn?.sortDirection === 1,
         isResizable: true,
         isFiltered: filtered != null,
         data: col,
         onColumnContextMenu: onColumnContextMenu,
         onColumnClick: onColumnClick,
       } as IColumn;
     });
 }, [columns, sorting, onColumnContextMenu, onColumnClick]);
```

---

#### Add context menu to rendered output


For the context menu to be shown, you need to add it to the rendered output. Add the following directly underneath the `DetailsList` component in the returned output:


##### [Before](#tab/before)

```typescript
<ScrollablePane scrollbarVisibility={ScrollbarVisibility.auto}>
    <DetailsList
      columns={gridColumns}
      onRenderItemColumn={onRenderItemColumn}
      onRenderDetailsHeader={onRenderDetailsHeader}
      items={items}
      setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
      initialFocusedIndex={0}
      checkButtonAriaLabel="select row"
      layoutMode={DetailsListLayoutMode.fixedColumns}
      constrainMode={ConstrainMode.unconstrained}
      selection={selection}
      onItemInvoked={onNavigate}
    ></DetailsList>
</ScrollablePane>
```

##### [After](#tab/after)

```typescript
<ScrollablePane scrollbarVisibility={ScrollbarVisibility.auto}>
    <DetailsList
      columns={gridColumns}
      onRenderItemColumn={onRenderItemColumn}
      onRenderDetailsHeader={onRenderDetailsHeader}
      items={items}
      setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
      initialFocusedIndex={0}
      checkButtonAriaLabel="select row"
      layoutMode={DetailsListLayoutMode.fixedColumns}
      constrainMode={ConstrainMode.unconstrained}
      selection={selection}
      onItemInvoked={onNavigate}
    ></DetailsList>
    {contextualMenuProps && <ContextualMenu {...contextualMenuProps} />}
</ScrollablePane>
```

---

#### Add onSort and OnFilter functions

Now that you've added the sorting and filtering UI, you need to add the callbacks to `index.ts` to actually perform the sort and filter on the records bound to the code component. Add the following to `index.ts` just below the `onNavigate` function:

```typescript
onSort = (name: string, desc: boolean): void => {
  const sorting = this.context.parameters.records.sorting;
  while (sorting.length > 0) {
    sorting.pop();
  }
  this.context.parameters.records.sorting.push({
    name: name,
    sortDirection: desc ? 1 : 0,
  });
  this.context.parameters.records.refresh();
};

onFilter = (name: string, filter: boolean): void => {
  const filtering = this.context.parameters.records.filtering;
  if (filter) {
    filtering.setFilter({
      conditions: [
        {
          attributeName: name,
          conditionOperator: 12, // Does not contain Data
        },
      ],
    } as ComponentFramework.PropertyHelper.DataSetApi.FilterExpression);
  } else {
    filtering.clearFilter();
  }
  this.context.parameters.records.refresh();
};
```

You'll see that:

- The sort and filter are applied to the dataset using the [sorting](reference/dataset.md#sorting) and [filtering](reference/dataset.md#filtering) properties.
- When modifying the sort columns, the existing sort definitions must be removed using pop rather than the sorting array itself being replaced.
- [Refresh](reference\dataset\refresh.md) must be called after sorting and filtering is applied. If a filter and sort are applied at the same time, refresh only needs to be called once.

#### Add OnSort and OnFilter callbacks to Grid rendering

Lastly, you can pass these two callbacks into the `Grid` rendering call:

##### [Before](#tab/before)

```typescript
ReactDOM.render(
    React.createElement(Grid, {
        width: allocatedWidth,
        height: allocatedHeight,
        columns: dataset.columns,
        records: this.records,
        sortedRecordIds: this.sortedRecordsIds,
        hasNextPage: paging.hasNextPage,
        hasPreviousPage: paging.hasPreviousPage,
        currentPage: this.currentPage,
        totalResultCount: paging.totalResultCount,
        sorting: dataset.sorting,
        filtering: dataset.filtering && dataset.filtering.getFilter(),
        resources: this.resources,
        itemsLoading: dataset.loading,
        highlightValue: this.context.parameters.HighlightValue.raw,
        highlightColor: this.context.parameters.HighlightColor.raw,
        setSelectedRecords: this.setSelectedRecords,
        onNavigate: this.onNavigate,
    }),
    this.container
);
```

##### [After](#tab/after)

```typescript
ReactDOM.render(
    React.createElement(Grid, {
        width: allocatedWidth,
        height: allocatedHeight,
        columns: dataset.columns,
        records: this.records,
        sortedRecordIds: this.sortedRecordsIds,
        hasNextPage: paging.hasNextPage,
        hasPreviousPage: paging.hasPreviousPage,
        currentPage: this.currentPage,
        totalResultCount: paging.totalResultCount,
        sorting: dataset.sorting,
        filtering: dataset.filtering && dataset.filtering.getFilter(),
        resources: this.resources,
        itemsLoading: dataset.loading,
        highlightValue: this.context.parameters.HighlightValue.raw,
        highlightColor: this.context.parameters.HighlightColor.raw,
        setSelectedRecords: this.setSelectedRecords,
        onNavigate: this.onNavigate,
        onSort: this.onSort,
        onFilter: this.onFilter,
    }),
    this.container
);
```

---

> [!NOTE]
> At this point, you can no longer test using the test harness because it doesn't provide support for sorting and filtering. Later, you can deploy using [pac pcf push](/power-platform/developer/cli/reference/pcf#pac-pcf-push) and then add to a canvas app for testing. If you wish, you can skip to that step to see how the code component looks inside canvas apps.

### Update the FilteredRecordCount output property

Since the grid can now filter records internally, it's important to report back to the canvas app how many records are displayed. This is so that you can show a 'No Records' type message.

> [!TIP]
> You could implement this internally within the code component, however it's recommended that as much user interface is left up to the canvas app since it will give the app maker more flexibility.

You have already defined an output property called `FilteredRecordCount` in the `ControlManifest.Input.xml`. When the filtering takes place and the filtered records are loaded, the `updateView` function will be called with string `dataset` in the [updatedProperties](reference\updatedproperties.md) array. If the number of records has changed, you need to make a call to `notifyOutputChanged` so that the canvas app knows it must update any controls that use the `FilteredRecordCount` property. Inside the `updateView` method of `index.ts`, add the following just above the `ReactDOM.render` and below `allocatedHeight`:

##### [Before](#tab/before)

```typescript
const allocatedHeight = parseInt(
    context.mode.allocatedHeight as unknown as string
);
```

##### [After](#tab/after)

```typescript
const allocatedHeight = parseInt(
    context.mode.allocatedHeight as unknown as string
);

if (this.filteredRecordCount !== this.sortedRecordsIds.length) {
    this.filteredRecordCount = this.sortedRecordsIds.length;
    this.notifyOutputChanged();
}

```

---

#### Add FilteredRecordCount to getOutputs

This updates the `filteredRecordCount` on the code component class you defined earlier when it's different from the new data received. After `notifyOutputChanged` is called, you need to ensure the value is returned when `getOutputs` is called, so update the `getOutputs` method to be:

##### [Before](#tab/before)

```typescript
public getOutputs(): IOutputs {
    return {};
}
```

##### [After](#tab/after)

```typescript
public getOutputs(): IOutputs {
    return {
        FilteredRecordCount: this.filteredRecordCount,
    } as IOutputs;
}
```

---

## Add paging to the grid

For large datasets, canvas apps will split the records across multiple pages. You can add a footer that shows page navigation controls. Each button will be rendered using a Fluent UI `IconButton`, which you must import.

### Add IconButton to imports

Add this to the imports inside `Grid.tsx`:

```typescript
import { IconButton } from '@fluentui/react/lib/Button';
```

### Add stringFormat function

The following step will add capabilities to load the format for the page indicator label from the resource strings (`"Page {0} ({1} Selected)"`) and format using a simple `stringFormat` function. This function could equally be in a separate file and shared between your components for convenience:

In this tutorial, add it at the top of `Grid.tsx`, right below `type DataSet ...`.

```typescript
function stringFormat(template: string, ...args: string[]): string {
  for (const k in args) {
    template = template.replace("{" + k + "}", args[k]);
  }
  return template;
}
```

### Add Paging buttons

In `Grid.tsx`, add the following `Stack.Item` below the existing `Stack.Item` that contains the `ScrollablePane`:

##### [Before](#tab/before)

```typescript
return (
  <Stack verticalFill grow style={rootContainerStyle}>
      <Stack.Item grow style={{ position: 'relative', backgroundColor: 'white' }}>
        <ScrollablePane scrollbarVisibility={ScrollbarVisibility.auto}>
            <DetailsList
              columns={gridColumns}
              onRenderItemColumn={onRenderItemColumn}
              onRenderDetailsHeader={onRenderDetailsHeader}
              items={items}
              setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
              initialFocusedIndex={0}
              checkButtonAriaLabel="select row"
              layoutMode={DetailsListLayoutMode.fixedColumns}
              constrainMode={ConstrainMode.unconstrained}
              selection={selection}
              onItemInvoked={onNavigate}
            ></DetailsList>
            {contextualMenuProps && <ContextualMenu {...contextualMenuProps} />}
        </ScrollablePane>
        {(itemsLoading || isComponentLoading) && <Overlay />}
      </Stack.Item>    
  </Stack>
);
```

##### [After](#tab/after)

```typescript
return (
  <Stack verticalFill grow style={rootContainerStyle}>
      <Stack.Item grow style={{ position: 'relative', backgroundColor: 'white' }}>
        <ScrollablePane scrollbarVisibility={ScrollbarVisibility.auto}>
            <DetailsList
              columns={gridColumns}
              onRenderItemColumn={onRenderItemColumn}
              onRenderDetailsHeader={onRenderDetailsHeader}
              items={items}
              setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
              initialFocusedIndex={0}
              checkButtonAriaLabel="select row"
              layoutMode={DetailsListLayoutMode.fixedColumns}
              constrainMode={ConstrainMode.unconstrained}
              selection={selection}
              onItemInvoked={onNavigate}
            ></DetailsList>
            {contextualMenuProps && <ContextualMenu {...contextualMenuProps} />}
        </ScrollablePane>
        {(itemsLoading || isComponentLoading) && <Overlay />}
      </Stack.Item>
      <Stack.Item>
        <Stack horizontal style={{ width: '100%', paddingLeft: 8, paddingRight: 8 }}>
            <IconButton
              alt="First Page"
              iconProps={{ iconName: 'Rewind' }}
              disabled={!hasPreviousPage}
              onClick={loadFirstPage}
            />
            <IconButton
              alt="Previous Page"
              iconProps={{ iconName: 'Previous' }}
              disabled={!hasPreviousPage}
              onClick={loadPreviousPage}
            />
            <Stack.Item align="center">
              {stringFormat(
                  resources.getString('Label_Grid_Footer'),
                  currentPage.toString(),
                  selection.getSelectedCount().toString(),
              )}
            </Stack.Item>
            <IconButton
              alt="Next Page"
              iconProps={{ iconName: 'Next' }}
              disabled={!hasNextPage}
              onClick={loadNextPage}
            />
        </Stack>
      </Stack.Item>
  </Stack>
);
```

---

You'll see that:

- The `Stack` ensures that the footer will stack below the `DetailsList`. The `grow` attribute is used to make sure that the grid expands to fill the available space.
- You load the format for the page indicator label from the resource strings (`"Page {0} ({1} Selected)"`) and format using the `stringFormat` function you added in the previous step.
- You can provide `alt` text for accessibility on the paging `IconButtons`.
- The style on the footer could equally be applied using a CSS class name referencing a CSS file added to the code component.

### Add callback props to support paging

Next, you must add the missing `loadFirstPage`, `loadNextPage`, and `loadPreviousPage` callback props.

To the `GridProps` interface, add the following:

##### [Before](#tab/before)

```typescript
export interface GridProps {
   width?: number;
   height?: number;
   columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
   records: Record<string, ComponentFramework.PropertyHelper.DataSetApi.EntityRecord>;
   sortedRecordIds: string[];
   hasNextPage: boolean;
   hasPreviousPage: boolean;
   totalResultCount: number;
   currentPage: number;
   sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
   filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
   resources: ComponentFramework.Resources;
   itemsLoading: boolean;
   highlightValue: string | null;
   highlightColor: string | null;
   setSelectedRecords: (ids: string[]) => void;
   onNavigate: (item?: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord) => void;
   onSort: (name: string, desc: boolean) => void;
   onFilter: (name: string, filtered: boolean) => void;
}
```

##### [After](#tab/after)

```typescript
export interface GridProps {
   width?: number;
   height?: number;
   columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
   records: Record<string, ComponentFramework.PropertyHelper.DataSetApi.EntityRecord>;
   sortedRecordIds: string[];
   hasNextPage: boolean;
   hasPreviousPage: boolean;
   totalResultCount: number;
   currentPage: number;
   sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
   filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
   resources: ComponentFramework.Resources;
   itemsLoading: boolean;
   highlightValue: string | null;
   highlightColor: string | null;
   setSelectedRecords: (ids: string[]) => void;
   onNavigate: (item?: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord) => void;
   onSort: (name: string, desc: boolean) => void;
   onFilter: (name: string, filtered: boolean) => void;
   loadFirstPage: () => void;
   loadNextPage: () => void;
   loadPreviousPage: () => void;
}
```

---

### Add new paging props to the Grid

Add these new props to the props destructuring:

##### [Before](#tab/before)

```typescript
export const Grid = React.memo((props: GridProps) => {
   const {
      records,
      sortedRecordIds,
      columns,
      width,
      height,
      hasNextPage,
      hasPreviousPage,
      sorting,
      filtering,
      currentPage,
      itemsLoading,
      setSelectedRecords,
      onNavigate,
      onSort,
      onFilter,
      resources,
   } = props;
```

##### [After](#tab/after)

```typescript
export const Grid = React.memo((props: GridProps) => {
   const {
      records,
      sortedRecordIds,
      columns,
      width,
      height,
      hasNextPage,
      hasPreviousPage,
      sorting,
      filtering,
      currentPage,
      itemsLoading,
      setSelectedRecords,
      onNavigate,
      onSort,
      onFilter,
      resources,
      loadFirstPage, 
      loadNextPage, 
      loadPreviousPage,
   } = props;
```

---


### Add callbacks to index.ts

Add these callbacks to `index.ts` below the `onFilter` method:

```typescript
loadFirstPage = (): void => {
  this.currentPage = 1;
  this.context.parameters.records.paging.loadExactPage(1);
};
loadNextPage = (): void => {
  this.currentPage++;
  this.context.parameters.records.paging.loadExactPage(this.currentPage);
};
loadPreviousPage = (): void => {
  this.currentPage--;
  this.context.parameters.records.paging.loadExactPage(this.currentPage);
};
```

Then update the `Grid` rendering call to include these callbacks:

##### [Before](#tab/before)

```typescript
ReactDOM.render(
    React.createElement(Grid, {
        width: allocatedWidth,
        height: allocatedHeight,
        columns: dataset.columns,
        records: this.records,
        sortedRecordIds: this.sortedRecordsIds,
        hasNextPage: paging.hasNextPage,
        hasPreviousPage: paging.hasPreviousPage,
        currentPage: this.currentPage,
        totalResultCount: paging.totalResultCount,
        sorting: dataset.sorting,
        filtering: dataset.filtering && dataset.filtering.getFilter(),
        resources: this.resources,
        itemsLoading: dataset.loading,
        highlightValue: this.context.parameters.HighlightValue.raw,
        highlightColor: this.context.parameters.HighlightColor.raw,
        setSelectedRecords: this.setSelectedRecords,
        onNavigate: this.onNavigate,
        onSort: this.onSort,
        onFilter: this.onFilter,
    }),
    this.container
);
```

##### [After](#tab/after)

```typescript
ReactDOM.render(
    React.createElement(Grid, {
        width: allocatedWidth,
        height: allocatedHeight,
        columns: dataset.columns,
        records: this.records,
        sortedRecordIds: this.sortedRecordsIds,
        hasNextPage: paging.hasNextPage,
        hasPreviousPage: paging.hasPreviousPage,
        currentPage: this.currentPage,
        totalResultCount: paging.totalResultCount,
        sorting: dataset.sorting,
        filtering: dataset.filtering && dataset.filtering.getFilter(),
        resources: this.resources,
        itemsLoading: dataset.loading,
        highlightValue: this.context.parameters.HighlightValue.raw,
        highlightColor: this.context.parameters.HighlightColor.raw,
        setSelectedRecords: this.setSelectedRecords,
        onNavigate: this.onNavigate,
        onSort: this.onSort,
        onFilter: this.onFilter,
        loadFirstPage: this.loadFirstPage,
        loadNextPage: this.loadNextPage,
        loadPreviousPage: this.loadPreviousPage,
    }),
    this.container
);
```

---

## Add full screen support

Code components offer the ability to show in full screen mode. This is especially useful on small screen sizes or where there's limited space for the code component within a canvas app screen.

### Import Fluent UI Link component

To launch the full screen mode, you can use the Fluent UI `Link` component. Add it to the imports at the top of `Grid.tsx`:

```typescript
import { Link } from '@fluentui/react/lib/Link';
```

### Add the Link control

To add a full screen link, you add the following to the existing `Stack` that contains the paging controls. 

> [!NOTE]
> Be sure to add this to the nested `Stack`, and not the root `Stack`.

##### [Before](#tab/before)

```typescript
<Stack horizontal style={{ width: '100%', paddingLeft: 8, paddingRight: 8 }}>
    <IconButton
      alt="First Page"
      iconProps={{ iconName: 'Rewind' }}
      disabled={!hasPreviousPage}
      onClick={loadFirstPage}
    />
    <IconButton
      alt="Previous Page"
      iconProps={{ iconName: 'Previous' }}
      disabled={!hasPreviousPage}
      onClick={loadPreviousPage}
    />
    <Stack.Item align="center">
      {stringFormat(
          resources.getString('Label_Grid_Footer'),
          currentPage.toString(),
          selection.getSelectedCount().toString(),
      )}
    </Stack.Item>
    <IconButton
      alt="Next Page"
      iconProps={{ iconName: 'Next' }}
      disabled={!hasNextPage}
      onClick={loadNextPage}
    />
</Stack>
```

##### [After](#tab/after)

```typescript
<Stack horizontal style={{ width: '100%', paddingLeft: 8, paddingRight: 8 }}>
    <Stack.Item grow align="center">
        {!isFullScreen && (
            <Link onClick={onFullScreen}>{resources.getString('Label_ShowFullScreen')}</Link>
        )}
    </Stack.Item>
    <IconButton
      alt="First Page"
      iconProps={{ iconName: 'Rewind' }}
      disabled={!hasPreviousPage}
      onClick={loadFirstPage}
    />
    <IconButton
      alt="Previous Page"
      iconProps={{ iconName: 'Previous' }}
      disabled={!hasPreviousPage}
      onClick={loadPreviousPage}
    />
    <Stack.Item align="center">
      {stringFormat(
          resources.getString('Label_Grid_Footer'),
          currentPage.toString(),
          selection.getSelectedCount().toString(),
      )}
    </Stack.Item>
    <IconButton
      alt="Next Page"
      iconProps={{ iconName: 'Next' }}
      disabled={!hasNextPage}
      onClick={loadNextPage}
    />
</Stack>
```

---

You'll see that:

- This code uses resources to show the label to support localization.
- If full screen mode is open, then the link is not shown. Instead, the parent app context automatically renders a close icon.

### Add props to support full screen to GridProps

Add the `onFullScreen` and `isFullScreen` props to the `GridProps` interface inside `Grid.tsx` to provide callback functions for sorting and filtering:

##### [Before](#tab/before)

```typescript
export interface GridProps {
   width?: number;
   height?: number;
   columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
   records: Record<string, ComponentFramework.PropertyHelper.DataSetApi.EntityRecord>;
   sortedRecordIds: string[];
   hasNextPage: boolean;
   hasPreviousPage: boolean;
   totalResultCount: number;
   currentPage: number;
   sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
   filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
   resources: ComponentFramework.Resources;
   itemsLoading: boolean;
   highlightValue: string | null;
   highlightColor: string | null;
   setSelectedRecords: (ids: string[]) => void;
   onNavigate: (item?: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord) => void;
   onSort: (name: string, desc: boolean) => void;
   onFilter: (name: string, filtered: boolean) => void;
   loadFirstPage: () => void;
   loadNextPage: () => void;
   loadPreviousPage: () => void;
}
```

##### [After](#tab/after)

```typescript
export interface GridProps {
   width?: number;
   height?: number;
   columns: ComponentFramework.PropertyHelper.DataSetApi.Column[];
   records: Record<string, ComponentFramework.PropertyHelper.DataSetApi.EntityRecord>;
   sortedRecordIds: string[];
   hasNextPage: boolean;
   hasPreviousPage: boolean;
   totalResultCount: number;
   currentPage: number;
   sorting: ComponentFramework.PropertyHelper.DataSetApi.SortStatus[];
   filtering: ComponentFramework.PropertyHelper.DataSetApi.FilterExpression;
   resources: ComponentFramework.Resources;
   itemsLoading: boolean;
   highlightValue: string | null;
   highlightColor: string | null;
   setSelectedRecords: (ids: string[]) => void;
   onNavigate: (item?: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord) => void;
   onSort: (name: string, desc: boolean) => void;
   onFilter: (name: string, filtered: boolean) => void;
   loadFirstPage: () => void;
   loadNextPage: () => void;
   loadPreviousPage: () => void;
   onFullScreen: () => void;
   isFullScreen: boolean;
}
```

---

### Add props to support full screen to the Grid

Add these new props to the props destructuring:

##### [Before](#tab/before)

```typescript
export const Grid = React.memo((props: GridProps) => {
   const {
      records,
      sortedRecordIds,
      columns,
      width,
      height,
      hasNextPage,
      hasPreviousPage,
      sorting,
      filtering,
      currentPage,
      itemsLoading,
      setSelectedRecords,
      onNavigate,
      onSort,
      onFilter,
      resources,
      loadFirstPage,
      loadNextPage,
      loadPreviousPage,
   } = props;
```

##### [After](#tab/after)

```typescript
export const Grid = React.memo((props: GridProps) => {
   const {
      records,
      sortedRecordIds,
      columns,
      width,
      height,
      hasNextPage,
      hasPreviousPage,
      sorting,
      filtering,
      currentPage,
      itemsLoading,
      setSelectedRecords,
      onNavigate,
      onSort,
      onFilter,
      resources,
      loadFirstPage,
      loadNextPage,
      loadPreviousPage,
      onFullScreen, 
      isFullScreen,
   } = props;
```

---

### Update index.ts to support full screen to the Grid

To provide these new props, inside `index.ts`, add the following callback method below `loadPreviousPage`:

```typescript
onFullScreen = (): void => {
  this.context.mode.setFullScreen(true);
};
```

The call to [setFullScreen](reference\mode\setfullscreen.md) causes the code component to open the full screen mode and adjust the `allocatedHeight` and `allocatedWidth` accordingly because of the call to `trackContainerResize(true)` in the `init` method. Once the full screen mode is open, `updateView` will be called, updating the rendering of the component with the new size. The `updatedProperties` contains `fullscreen_open` or `fullscreen_close`, depending on the transition that is happening.

To store the state of the full screen mode, add a new `isFullScreen` field to the `CanvasGrid` class inside `index.ts`:

##### [Before](#tab/before)

```typescript
export class CanvasGrid implements ComponentFramework.StandardControl<IInputs, IOutputs> {
    notifyOutputChanged: () => void;
    container: HTMLDivElement;
    context: ComponentFramework.Context<IInputs>;
    sortedRecordsIds: string[] = [];
    resources: ComponentFramework.Resources;
    isTestHarness: boolean;
    records: {
        [id: string]: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord;
    };
    currentPage = 1;
    filteredRecordCount?: number;
```

##### [After](#tab/after)

```typescript
export class CanvasGrid implements ComponentFramework.StandardControl<IInputs, IOutputs> {
    notifyOutputChanged: () => void;
    container: HTMLDivElement;
    context: ComponentFramework.Context<IInputs>;
    sortedRecordsIds: string[] = [];
    resources: ComponentFramework.Resources;
    isTestHarness: boolean;
    records: {
        [id: string]: ComponentFramework.PropertyHelper.DataSetApi.EntityRecord;
    };
    currentPage = 1;
    filteredRecordCount?: number;
    isFullScreen = false;
```

---

### Edit updateView to track the state

Add the following to the `updateView` method to track the state:

##### [Before](#tab/before)

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): void {
    const dataset = context.parameters.records;
    const paging = context.parameters.records.paging;
    const datasetChanged = context.updatedProperties.indexOf("dataset") > -1;
    const resetPaging =
        datasetChanged &&
        !dataset.loading &&
        !dataset.paging.hasPreviousPage &&
        this.currentPage !== 1;

    if (resetPaging) {
        this.currentPage = 1;
    }
```

##### [After](#tab/after)

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): void {
    const dataset = context.parameters.records;
    const paging = context.parameters.records.paging;
    const datasetChanged = context.updatedProperties.indexOf("dataset") > -1;
    const resetPaging =
        datasetChanged &&
        !dataset.loading &&
        !dataset.paging.hasPreviousPage &&
        this.currentPage !== 1;

    if (context.updatedProperties.indexOf('fullscreen_close') > -1) {
        this.isFullScreen = false;
    }
    if (context.updatedProperties.indexOf('fullscreen_open') > -1) {
        this.isFullScreen = true;
    }

    if (resetPaging) {
        this.currentPage = 1;
    }
```

---

### Pass the callback and isFullScreen field to render in the Grid

Now you can pass the callback and `isFullScreen` field into the `Grid` rendering props:

##### [Before](#tab/before)

```typescript
ReactDOM.render(
    React.createElement(Grid, {
        width: allocatedWidth,
        height: allocatedHeight,
        columns: dataset.columns,
        records: this.records,
        sortedRecordIds: this.sortedRecordsIds,
        hasNextPage: paging.hasNextPage,
        hasPreviousPage: paging.hasPreviousPage,
        currentPage: this.currentPage,
        totalResultCount: paging.totalResultCount,
        sorting: dataset.sorting,
        filtering: dataset.filtering && dataset.filtering.getFilter(),
        resources: this.resources,
        itemsLoading: dataset.loading,
        highlightValue: this.context.parameters.HighlightValue.raw,
        highlightColor: this.context.parameters.HighlightColor.raw,
        setSelectedRecords: this.setSelectedRecords,
        onNavigate: this.onNavigate,
        onSort: this.onSort,
        onFilter: this.onFilter,
        loadFirstPage: this.loadFirstPage,
        loadNextPage: this.loadNextPage,
        loadPreviousPage: this.loadPreviousPage,
    }),
    this.container
);
```

##### [After](#tab/after)

```typescript
ReactDOM.render(
    React.createElement(Grid, {
        width: allocatedWidth,
        height: allocatedHeight,
        columns: dataset.columns,
        records: this.records,
        sortedRecordIds: this.sortedRecordsIds,
        hasNextPage: paging.hasNextPage,
        hasPreviousPage: paging.hasPreviousPage,
        currentPage: this.currentPage,
        totalResultCount: paging.totalResultCount,
        sorting: dataset.sorting,
        filtering: dataset.filtering && dataset.filtering.getFilter(),
        resources: this.resources,
        itemsLoading: dataset.loading,
        highlightValue: this.context.parameters.HighlightValue.raw,
        highlightColor: this.context.parameters.HighlightColor.raw,
        setSelectedRecords: this.setSelectedRecords,
        onNavigate: this.onNavigate,
        onSort: this.onSort,
        onFilter: this.onFilter,
        loadFirstPage: this.loadFirstPage,
        loadNextPage: this.loadNextPage,
        loadPreviousPage: this.loadPreviousPage,
        isFullScreen: this.isFullScreen,
        onFullScreen: this.onFullScreen,
    }),
    this.container
);
```

---

## Highlighting rows

Now you're ready to add the conditional row highlighting functionality. You've already defined the `HighlightValue` and `HighlightColor` input properties, and the `HighlightIndicator` `property-set`. The `property-set` allows the maker to choose a field to use to compare with the value they provide in `HighlightValue`.

### Import types to support highlighting

Custom row rendering in the `DetailsList` requires some additional imports. There are already some types from `@fluentui/react/lib/DetailsList`, so add `IDetailsListProps`, `IDetailsRowStyles` and `DetailsRow` to that import statement in  `Grid.tsx`:

##### [Before](#tab/before)

```typescript
import {
    DetailsList,
    ConstrainMode,
    DetailsListLayoutMode,
    IColumn,
    IDetailsHeaderProps
} from '@fluentui/react/lib/DetailsList';
```

##### [After](#tab/after)

```typescript
import {
    DetailsList,
    ConstrainMode,
    DetailsListLayoutMode,
    IColumn,
    IDetailsHeaderProps,
    IDetailsListProps,
    IDetailsRowStyles,
    DetailsRow
} from '@fluentui/react/lib/DetailsList';
```

---

Now, create the custom row renderer by adding the following just below the `const rootContainerStyle` block:


```typescript
const onRenderRow: IDetailsListProps['onRenderRow'] = (props) => {
    const customStyles: Partial<IDetailsRowStyles> = {};
    if (props && props.item) {
        const item = props.item as DataSet | undefined;
        if (highlightColor && highlightValue && item?.getValue('HighlightIndicator') == highlightValue) {
            customStyles.root = { backgroundColor: highlightColor };
        }
        return <DetailsRow {...props} styles={customStyles} />;
    }
    return null;
};
```

You'll see that:

- You can retrieve the value of the field chosen by the maker via the `HighlightIndicator` alias using:<br /> `item?.getValue('HighlightIndicator')`.
- When the value of the `HighlightIndicator` field matches the value of the `highlightValue` provided by the input property on the code component, you can add a background color to the row.
- The `DetailsRow` component is used by the `DetailsList` to render the columns you defined. You don't need to change the behavior other than the background color.

### Add additional props to support highlighting

Add some additional props for `highlightColor` and `highlightValue` that will be provided by the rendering inside `updateView`. You've already added to the `GridProps` interface, so you just need to add them to the props destructuring:

##### [Before](#tab/before)

```typescript
export const Grid = React.memo((props: GridProps) => {
   const {
      records,
      sortedRecordIds,
      columns,
      width,
      height,
      hasNextPage,
      hasPreviousPage,
      sorting,
      filtering,
      currentPage,
      itemsLoading,
      setSelectedRecords,
      onNavigate,
      onSort,
      onFilter,
      resources,
      loadFirstPage,
      loadNextPage,
      loadPreviousPage,
      onFullScreen, 
      isFullScreen,
   } = props;
```

##### [After](#tab/after)

```typescript
export const Grid = React.memo((props: GridProps) => {
   const {
      records,
      sortedRecordIds,
      columns,
      width,
      height,
      hasNextPage,
      hasPreviousPage,
      sorting,
      filtering,
      currentPage,
      itemsLoading,
      setSelectedRecords,
      onNavigate,
      onSort,
      onFilter,
      resources,
      loadFirstPage,
      loadNextPage,
      loadPreviousPage,
      onFullScreen, 
      isFullScreen,
      highlightValue, 
      highlightColor,
   } = props;
```

---

### Add the onRenderRow method to the DetailsList

Pass the `onRenderRow` method into the `DetailsList` props:

##### [Before](#tab/before)

```typescript
<DetailsList
  columns={gridColumns}
  onRenderItemColumn={onRenderItemColumn}
  onRenderDetailsHeader={onRenderDetailsHeader}
  items={items}
  setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
  initialFocusedIndex={0}
  checkButtonAriaLabel="select row"
  layoutMode={DetailsListLayoutMode.fixedColumns}
  constrainMode={ConstrainMode.unconstrained}
  selection={selection}
  onItemInvoked={onNavigate}
></DetailsList>
```

##### [After](#tab/after)

```typescript
<DetailsList
  columns={gridColumns}
  onRenderItemColumn={onRenderItemColumn}
  onRenderDetailsHeader={onRenderDetailsHeader}
  items={items}
  setKey={`set${currentPage}`} // Ensures that the selection is reset when paging
  initialFocusedIndex={0}
  checkButtonAriaLabel="select row"
  layoutMode={DetailsListLayoutMode.fixedColumns}
  constrainMode={ConstrainMode.unconstrained}
  selection={selection}
  onItemInvoked={onNavigate}
  onRenderRow={onRenderRow}
></DetailsList>
```

---

## Deploy and configure the component

Now that you've implemented all the features, you must deploy the code component to Microsoft Dataverse for testing.

1. Inside your Dataverse environment, ensure there's a publisher created with a prefix of `samples`:

   :::image type="content" source="media/field-component-4.png" alt-text="Add new publisher":::

   This could also be your own publisher, provided you update the publisher prefix parameter in the call to [pac pcf push](/power-platform/developer/cli/reference/pcf#pac-pcf-push) below.
   More information: [Create a solution publisher](/powerapps/maker/data-platform/create-solution#solution-publisher).

1. Once you've saved the publisher, you're ready to authorize the CLI against your environment so that we can push the compiled code component. At the command-line, use:

   ```powershell
   pac auth create --url https://myorg.crm.dynamics.com
   ```

   Replace `myorg.crm.dynamics.com` with the URL of your own Dataverse environment.
   Sign in with an administrator/customizer user when prompted. The privileges provided by these user roles are needed to deploy any code components to Dataverse.

1. To deploy your code component, use:

   ```powershell
   pac pcf push --publisher-prefix samples
   ```

   > [!NOTE]
   > If you receive the error, `Missing required tool: MSBuild.exe/dotnet.exe. Please add MSBuild.exe/dotnet.exe in Path environment variable or use 'Developer Command Prompt for VS`, you must install either [Visual Studio 2019 for Windows & Mac](https://visualstudio.microsoft.com/downloads/) or [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019), being sure to select the '.NET build tools' workload as described in the prerequisites.

1. Once completed, this process will have created a small temporary solution named **PowerAppTools_samples** in your environment, and the `CanvasGrid` code component will be added to this solution. You can move the code component into your own solution later if necessary. More information: [Code Component Application Lifecycle Management (ALM)](code-components-alm.md).

   :::image type="content" source="media/canvas-datagrid-4.png" alt-text="PowerAppsTools_samples solution":::

1. To use code components inside canvas apps, you must enable the **Power Apps component framework for canvas apps** on the environment you're using.
   
    a. Open the **Admin center** (admin.powerplatform.microsoft.com) and navigate to your environment.
    b. Navigate to **Settings** > **Product** > **Features** . Ensure **Power Apps component framework for canvas apps** is turned **On**:
   
   :::image type="content" source="media/canvas-datagrid-enable.png" alt-text="Enable code components":::
   
1. Create a new canvas app using the **Tablet** layout.
1. From the **Insert** panel, select **Get more components**.
1. Select the **Code** tab on the **Import components** pane.
1. Select the **`CanvasGrid`** component.
1. Select **Import**. The code component will now appear under **Code components** on the **Insert** panel.
1. Drag the `CanvasGrid` component onto the screen and bind to the `Contacts` table in Microsoft Dataverse.
1. Set the following properties on the `CanvasGrid` code component using the properties panel:

   - **Highlight Value** = `1` - This is the value that `statecode` has when the record is inactive.
   - **Highlight Color** = `#FDE7E9` - This is the color to use when the record is inactive.
   - **`HighlightIndicator`** = `"statecode"` - This is the field to compare against. This will be on the **Advanced** panel in the **DATA** section.

   :::image type="content" source="media/canvas-datagrid-5.png" alt-text="Properties Panel":::

1. Add a new `TextInput` component and name it `txtSearch`.
1. Update the `CanvasGrid.Items` property to be `Search(Contacts,txtSearch.Text,"fullname")`.
   
   As you type in the **Text Input**, you'll see that the contacts are filtered in the grid.

15. Add a new **Text label** and set the text to be "No records found". Position the label on top of the Canvas Grid.
16. Set the **Visible** property of the Text label to be `CanvasGrid1.FilteredRecordCount=0`.
   
   This means that when there are no records matching the `txtSearch` value, or if a column filter is applied using the context menu that returns no records (for example, **Full Name** does not contain data), the label will be displayed.
   
1. Add a **Display Form** (from the **Input** group in the **Insert** panel).
1. Set the form `DataSource` to the `Contacts` table and add some **form fields**.
1. Set the form `Item` property to `CanvasGrid1.Selected`.
   
   You should now see that when you select items on the grid, the form displays the item selected.
   
1. Add a new **Screen** to the canvas app called `scrDetails`.
1. Copy the form from the previous screen and paste it onto the new screen.
1. Set the `CanvasGrid1.OnSelect` property to be `Navigate(scrDetails)`.
   
   When you invoke the grid row select action, you should now see that the app navigates to the second screen with the item selected.
  

## Debugging after deploying

You can easily debug your code component while it's running inside the canvas app by opening Developer Tools using `Ctrl+Shift+I`.

Select `Ctrl+P` and type `Grid.tsx` or `Index.ts`. You can then set a break point and step through your code.

:::image type="content" source="media/canvas-datagrid-9.png" alt-text="Debug in canvas apps":::

If you need to make further changes to your component, you don't need to deploy each time. Instead, use the technique described in [Debug code components](debugging-custom-controls.md) to create a Fiddler **AutoResponder** to load the file from your local file system while `npm start watch` is running.

The **AutoResponder** would look similar to the following:

```
REGEX:(.*?)((?'folder'css|html)(%252f|\/))?SampleNamespace\.CanvasGrid[\.\/](?'fname'[^?]*\.*)(.*?)$
```

```
C:\repos\CanvasGrid\out\controls\CanvasGrid\${folder}\${fname}
```

:::image type="content" source="media/canvas-datagrid-8.png" alt-text="AutoResponder rule":::

You'll also need to enable the filters to add the `Access-Control-Allow-Origin` header. More information: [Debugging after deploying into Microsoft Dataverse](debugging-custom-controls.md#debugging-after-deploying-into-microsoft-dataverse).

You'll need to **Empty cache and hard refresh** on your browser session for the **AutoResponder** file to be picked up. Once loaded, you can simply refresh the browser since Fiddler will add a cache control header to the file to prevent it from being cached.

Once you're happy with your changes, you can increment the patch version in the manifest, and then redeploy using [pac pcf push](/power-platform/developer/cli/reference/pcf#pac-pcf-push).

So far, you've deployed a development build, which is not optimized and will run slower at runtime. You can choose to deploy an optimized build using [pac pcf push](/power-platform/developer/cli/reference/pcf#pac-pcf-push) by editing the `CanvasGrid.pcfproj`. Underneath the `OutputPath`, add the following: `<PcfBuildMode>production</PcfBuildMode>`

##### [Before](#tab/before)

```xml
  <PropertyGroup>
    <Name>CanvasGrid</Name>
    <ProjectGuid>a670bba8-e0ae-49ed-8cd2-73917bace346</ProjectGuid>
    <OutputPath>$(MSBuildThisFileDirectory)out\controls</OutputPath>
  </PropertyGroup>
```

##### [After](#tab/after)

```xml
  <PropertyGroup>
    <Name>CanvasGrid</Name>
    <ProjectGuid>a670bba8-e0ae-49ed-8cd2-73917bace346</ProjectGuid>
    <OutputPath>$(MSBuildThisFileDirectory)out\controls</OutputPath>
    <PcfBuildMode>production</PcfBuildMode>
  </PropertyGroup>
```

---

### Related articles

[Application lifecycle management (ALM) with Microsoft Power Platform](/power-platform/alm/overview-alm)<br/>
[Power Apps component framework API reference](reference/index.md)<br/>
[Create your first component](implementing-controls-using-typescript.md)<br/>
[Debug code components](debugging-custom-controls.md)<br/>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
