---
title: Power Apps code optimization
description: Learn about how to optimize code in Power Apps.
ms.date: 06/19/2025
ms.topic: concept-article
ms.subservice: guidance
ms.service: powerapps
author: robstand
ms.author: rachaudh
---

# Code optimization

As canvas apps evolve to meet different business needs, keeping performance optimal is critical. Data handling, user interface design, and app functionality all require a careful approach to code optimization.

When canvas apps get more complex, you can run into issues with data retrieval, formula complexity, and rendering speed. Balancing strong functionality and a responsive user interface means you need a systematic approach to code optimization.

## Power Fx formulas optimization

### With function

The `With` function evaluates a formula for a single record. The formula can calculate a value or perform actions, like modifying data or working with a connection. Use `With` to make complex formulas easier to read by dividing them into smaller named subformulas. These named values act like simple local variables limited to the scope of `With`. Using `With` is better than context or global variables because it's self-contained, easy to understand, and works in any declarative formula context. [Learn more](/power-platform/power-fx/reference/function-with) about the `With` function.

![Screenshot of a Power Fx formula that uses the With function.](media/image13.png)

### Concurrent function


The `Concurrent` function lets multiple formulas in the same property to be evaluated at the same time if they have connector or Dataverse calls. Normally, multiple formulas are evaluated at the same time when you chain them with the `;` (semicolon) operator. With `Concurrent`, the app evaluates all formulas in a property at the same time, even after using the `;` operator. This concurrency means users wait less for results. When data calls don't start until the previous calls finish, the app waits for the sum of all request times. If data calls start at the same time, the app waits only for the longest request time. [Learn more](/power-platform/power-fx/reference/function-concurrent) about the `Concurrent` function.


```powerappsfl
Concurrent(
    ClearCollect(colAccounts1, Accounts),
    ClearCollect(colUsers1, Users),
    ClearCollect(colEnvDef1, 'Environment Variable Definitions'),
    ClearCollect(colEnvVal1, 'Environment Variable Values')
);
```

### Coalesce Function

The `Coalesce` function evaluates its arguments in order and returns the first value that's not blank or an empty string. Use this function to replace a blank value or empty string with a different value, but leave nonblank and nonempty string values unchanged. If all arguments are blank or empty strings, the function returns blank. `Coalesce` is a good way to convert empty strings to blank values.


For example:

```powerappsfl
If(Not IsBlank(value1), value1, Not IsBlank(value2), value2)
```

Requires value 1 and value 2 to be evaluated twice. This function can be reduced to:

```powerappsfl
Coalesce(value1, value2)
```

### IsMatch function

The `IsMatch` function tests if a text string matches a pattern made up of ordinary characters, predefined patterns, or a regular expression. [Learn more](/power-platform/power-fx/reference/function-ismatch) about the `IsMatch` function. 

For example, this formula matches a United States Social Security number:


```powerappsfl
IsMatch(TextInput1.Text, "\d{3}-\d{2}-\d{4}")
```

Explanation of the regular expression:

`\\d` Matches any digit (0-9).

`{3}` Specifies that the preceding digit pattern (\\d) should occur exactly three times.

`-` Matches the hyphen character.

`{2}` Specifies that the preceding digit pattern (\\d) should occur exactly two times.

`{4}` Specifies that the preceding digit pattern (\\d) should occur exactly four times.

More examples of `IsMatch`:

```powerappsfl
IsMatch(TextInput1.Text, "Hello World")
IsMatch(TextInput1\_2.Text, "(?!^\[0-9\]\\\*$)(?!^\[a-zA-Z\]\\\*$)(\[a-zA-Z0-9\]{8,10})")
```

## Optimize app OnStart

The `OnStart` property for cavas apps plays a crucial role in defining actions that occur when the app is launched. This property allows app developers to execute global initialization tasks, set up variables, and perform actions that should happen only once during the app's startup process. Understanding and effectively utilizing the `OnStart` property is essential for creating responsive and efficient canvas apps.

A recommended approach is to streamline the `App.OnStart` function by migrating variable setups to named formulas. Named formulas, especially those configured early in the app lifecycle, prove to be advantageous. These formulas handle the initialization of variables based on data calls, providing a cleaner and more organized structure for your code. More details [Build large and complex canvas apps - Power Apps | Microsoft Learn](/power-apps/maker/canvas-apps/working-with-large-apps#split-up-long-formulas).

> [!NOTE]
> The `OnStart` property is **Imperative.** It's an ordered list of work that needs to be done before the first screen is shown. Because it's so specific about not only *what* needs to be done, but also *when* that work must be done based on order, it limits the reordering and deferring optimizations that could otherwise be done.

### Start screen

If `App.OnStart` contains a `Navigate` function call, even if it is in an `If` function and rarely called, we must complete execution of the App.`OnStart` before we show the first screen of the app. `App.StartScreen` is the new declarative way to indicate which screen should be shown first, that doesn't block optimizations.

Setting the `StartScreen` property shows the first screen before `App.OnStart` is complete. `App.StartScreen declares` which screen object to show first without requiring any preprocessing.

Instead of writing code like:

```powerappsfl
App.OnStart = Collect(OrdersCache, Orders);
If(Param("AdminMode") = "1", Navigate(AdminScreen), Navigate(HomeScreen))
```

Change the code to:

```powerappsfl
App.OnStart = Collect(OrdersCache, Orders);
App.StartScreen = If(Param("AdminMode") = "1", AdminScreen, HomeScreen)
```

Refer to <https://Power Apps.microsoft.com/en-us/blog/app-startscreen-a-new-declarative-alternative-to-navigate-in-app-onstart/> for more details.

> [!WARNING]
> Avoid dependencies between `StartScreen` and `OnStart`. Referencing a named formula that in turn references a global variable may cause a race condition in which `StartScreen` isn't applied correctly. 
**Note**: we shouldn't have dependencies between StartScreen and OnStart. We block referencing global variables in StartScreen, but we can reference a named formula, that in turn references a global variable, and that may cause a race condition in which the StartScreen isn't applied correctly.

### Named formulas

Named formulas are static or constants that can be defined on App.Formulas section. Once declared in App.Formulas, they can be used anywhere in the app and their value always remain up to date. Named Formulas in Power Apps enable the definition of values or sets of values that are automatically managed and updated by the platform. This functionality transfers the responsibility of value calculation and upkeep from the developer to Power Apps, streamlining the development process. Named Formulas in Power Apps are a powerful functionality that can significantly enhance app performance and maintainability.

Named formulas can also address is declaring app themes. In many cases where enterprise apps are build, we want the app to have common themes to give consistent look and user experience. To create a theme, there are 10s and 100s of variables that need to be declared on App OnStart. This increased code length and initialization time of the app.

Modern controls can also help significantly with theming and help reduce customer written logic to handle theming. Modern controls are currently in preview.

For example, the following code on `App.OnStart` can be moved to `App.Formulas`, thus reducing the startup time on global variable declarations.

```powerappsfl
Set(BoardDark, RGBA(181,136,99, 1));
Set(BoardSelect, RGBA(34,177,76,1));
Set(BoardRowWidth, 10);                      // expected 8 plus two guard characters for regular expressions.
Set(BoardMetadata, 8 \* BoardRowWidth + 1);   // which player is next, have pieces moved for castling rules, etc.
Set(BoardBlank, "----------------------------------------------------------------\_00000000000000");
Set(BoardClassic, "RNBQKBNR\_\_PPPPPPPP------------------------\_--------\_\_pppppppp\_\_rnbqkbnr\_\_0000000000");
```

The code can be moved to App.Formulas as follows:

```powerappsfl
BoardSize = 70;
BoardLight = RGBA(240,217,181, 1);
BoardDark = RGBA(181,136,99, 1);
BoardSelect = RGBA(34,177,76,1);
BoardRowWidth = 10;                      // expected 8 plus two guard characters for regular expressions
BoardMetadata = 8 \* BoardRowWidth + 1;   // which player is next, have pieces moved for castling rules, etc.
BoardBlank = "----------------------------------------------------------------\_00000000000000";
BoardClassic = "RNBQKBNR\_\_PPPPPPPP------------------------\_--------\_\_pppppppp\_\_rnbqkbnr\_\_0000000000";
```

Another example is inn setting `Lookups`. Here, a change is required in a Lookup formula to get the user information from Office 365, instead of Dataverse. There's only one place the change is required without changing the code everywhere.

```powerappsfl
UserEmail = User().Email;
UserInfo = LookUp(Users, 'Primary Email' = User().Email);
UserTitle = UserInfo.Title;
UserPhone = Switch(UserInfo.'Preferred Phone', 'Preferred Phone (Users)'.'Mobile Phone', UserInfo.'Mobile Phone',
UserInfo.'Main Phone');
```

These formulas embody the essence of calculation. They articulate the process for determining `UserEmail`, `UserInfo`, `UserTitle`, and `UserPhone` based on other values. This logic is encapsulated, enabling widespread utilization throughout the app, and can be modified in a singular location. The adaptability extends to switching from the Dataverse Users table to the Office 365 connector without necessitating alterations to formulas scattered across the app.

Another approach is to optimize `countRows`.

```powerappsfl
varListItems = CountRows(SampleList)
```

With `Set` Function, variable `varListItems` will have to be initialized with the initial count of rows in sample list and set again after the list items were added or removed. With Named formulas, as the data changes, the varListitems variables get updated automatically.

Named Formulas in the `App.Formulas` property provide a more flexible and declarative approach for managing values and calculations throughout the app, offering advantages in terms of timing independence, automatic updates, maintainability, and immutable definitions compared to relying solely on `App.OnStart`.

| Aspect                | Named Formulas (App.Formulas)                                     | App.OnStart                                                              |
|-----------------------|-------------------------------------------------------------------|--------------------------------------------------------------------------|
| Timing Independence   | Formulas are available instantly, can be calculated in any order. | Variables may introduce timing dependencies, impacting availability.     |
| Automatic Updates     | Formulas automatically update when dependencies change.           | Variables are set once during startup; manual updates may be needed.     |
| Maintainability       | Centralized formulas in one location improve maintainability.     | Scattered variables may require finding and updating in multiple places. |
| Immutable Definitions | Formula definitions in App.Formulas are immutable.                | Variable values may be susceptible to accidental changes.                |

### User defined functions

User Defined Functions in Power Apps Authoring Studio enables users to create their own custom function.

To use this feature, under preview settings, turn on User-defined function (UDFs). Preview functionality should not be used in production, which is why it is disabled by default, but will become generally available soon.

Define a formula under `App.Formulas` as follows:

`FunctionName(Parameter1:DataType1, Parameter2:DataType2):OutputDataType = Formula`

The code works as so:

- `FunctionName` is used to invoke the function

- `Parameter` is the name of the input. One or more inputs are allowed

- `DataType` is an argument passed into the function must match this data type. Available data types include Boolean, Color, Date, Datetime, Dynamic, GUID, Hyperlink, Text, and Time

- `OutputDataType` is the data type the output of the function will be in

- `Formula` is the output of the function

```powerappsfl
// Function to calculate the area of a circle based on the radius
calcAreaOfCircle(radius: Number): Number = 
    IfError(Pi() * radius * radius, 0);
```

Use `IfError` to implement error handling within the defined function.

Call the defined function from text/label control.

`calcAreaOfCircle(Int(*TextInput1*.Text))`

> [!NOTE]
> This is an experimental feature and subject to change. Some data types, such as records and filters, aren't yet supported.

## Optimize variables

Variables define and set local and global values you use throughout your app. While they're convenient, using too many variables can make your app less efficient. 

The following example demonstrates how to set a variable for each attribute of an object, which requires using `Set` for every property.

```powerappsfl
Set(varEmpName, Office365Users.MyProfile().DisplayName);
Set(varEmpCity, Office365Users.MyProfile().City);
Set(varEmpPhone, Office365Users.MyProfile().BusinessPhones);
Set(varEmpUPN, Office365Users.MyProfile().UserPrincipalName);
Set(varEmpMgrName, Office365Users.ManagerV2(varEmpUPN).DisplayName);
```

A more efficient approach is to use the property only when you need it:

```powerappsfl
Set(varEmployee, Office365Users.MyProfile())
"Welcome " & varEmployee.DisplayName
```

Use context variables and global variables wisely. If a variable's scope goes beyond a single screen, use global variables instead of context variables.


Too many unused variables increase memory usage and can slow app initialization. Resources are allocated for these variables even if you don't use them. Unused variables also add complexity to your app's logic. While the impact might not be severe, it's a good practice to keep your Power App clean and organized for better performance and easier development.

## Optimize collections

Collections are temporary data storage structures you use to store and manipulate data in a Power Apps app. But collections can cause performance overhead if you use them too much. Limit your use of collections and use them only when necessary.

```powerappsfl
// Use this pattern
ClearCollect(colErrors, {Text: gblErrorText, Code: gblErrorCode});

// Do not use this pattern
Clear(colErrors);
Collect(colErrors, {Text: gblErrorText, Code: gblErrorCode});
```

To count records in a local collection, use `CountIf` instead of `Count(Filter())`.

Consider this guidance when working with collections:

**Limit the size and number of collections**. Because collections are local to the app, they're stored in the mobile device memory. The more data collections hold, or the more collections you use, the worse the performance. Use the `ShowColumns` function to get only specific columns. Add the `Filter` function to get only relevant data.

The following example function returns the entire dataset.

```powerappsfl
ClearCollect(colDemoAccount, Accounts);
```

Compare this to the following code, which returns only specific records and columns:

```powerappsfl
ClearCollect(colAcc,
              ShowColumns(
                Filter(Accounts, !IsBlank('Address 1: City')),
                "name","address1_city"))
```

This example returns the following dataset:

![Screenshot of a dataset with a table named colAcc and two columns, address1_city and name.](media/image21.png)

**Set a data source refresh frequency**. If you add new records to the collection, refresh it or collect to it to get the new or changed records. If multiple users update your data source, refresh the collection to get the new or changed records. More refresh calls mean more interaction with the server.

### Cache data in collections and variables

A collection is a table variable that stores rows and columns of data, not just a single data item. Collections are useful for two main reasons: aggregating data before sending it to the data source, and caching information to avoid frequent queries. Because collections match the tabular structure of the data source and Power Apps, they let you interact with data efficiently, even when you're offline.

```powerappsfl
// Clear the contents of EmployeeCollection, it already contains data
ClearCollect(
    colEmployee,
    {
        Id: "1",
        Name: "John",
        Department: "IT"
    },
    {
        Id: "2",
        Name: "Nestor",
        Department: "IT"
    }
)
```

### Remove unused variables and media

While unused media and variables might not have a significant impact on app performance, it's important to clean up your app by removing any unused media or variables.

- Unused media files increase app size, which can slow down app load times.

- Unused variables increase memory usage and can slightly slow down app initialization. Resources are allocated for these variables even if they aren't used. Too many unused variables can also make the app's logic more complex.

- Use App Checker to review unused media and variables.

## Optimize screens and controls

### Avoid cross referencing controls

Controls that reference controls on other screens can slow down app loading and navigation. Doing this can force the app to load the other screens immediately, rather than waiting until the user goes to that screen. To fix this issue, use variables, collections, and navigation context to share state across screens instead.

The App checker in Power Apps Studio shows controls that are cross-referenced. Review App checker regularly to fix this issue.

Here's an example of cross-referenced controls. In the image below, the Gallery 1 control is cross-referenced in Screen 2, Label 2 control.

![Screenshot of Power Apps Studio showing a cross-referenced control.](media/image23.png)

If you reference a control from the first screen in the app in the second screen, there isn't a performance hit because the first screen is already loaded. This can actually be a good thing because the app is declarative instead of using variables.

If you reference controls that aren't loaded yet, such as the first screen referencing a control named `Label 3` from screen 3, the app loads that screen into memory.

### Enable DelayOutput for text controls

The DelayOutput setting, when set to true, registers user input after a half-second delay. This is useful for delaying expensive operations until the user finishes entering text, like filtering when input is used in other formulas.

For example, for a Gallery whose Items are Filtered depending on what the user enters in the TextInput control:

- With DelayOutput set to false, which is the default, the gallery is filtered as soon as any text is typed. If you have a gallery with lots of items, reloading the gallery with changes right away slows down performance. It's better to wait a little. This is practical when you're using the TextInput for a search string (see [Search](https://PowerApps.microsoft.com/en-us/tutorials/function-filter-lookup/) or the new StartsWith functions).

- With DelayOutput set to true, there's a short delay before the changes are detected. This gives you time to finish typing. The delay works well with the TextInput.OnChange property. If you have actions tied to changes, you don't want them triggered until you've finished typing in the field.

## Delegation and server side processing

### Delegation

Delegation in Power Apps is a concept that refers to the ability of the app to offload certain operations to the underlying data source rather than processing the operations within Power Apps itself. By using delegation in Power Apps, developers can create more efficient and scalable applications that perform well even in scenarios involving large datasets. It's important to be aware of delegation limitations for specific data sources and operations, and to design apps accordingly to achieve optimal performance.

> ![NOTE] Not all functions are delegable. Please refer to [Understanding Delegation](/power-apps/maker/canvas-apps/delegation-overview) to learn more about delegation.

Delegation has several advantages such as Query optimization and adds supports for large datasets. Additionally, if the source data changes frequently, delegation helps keep data up to date.

### Reduce API calls to data source

Sometimes, it can seem convenient to create collections by performing joins within your canvas app. Here's an example:

In this example, there are two tables: Drivers and Trucks. The code creates a collection of drivers and truck details, and for each truck, it calls the driver who owns the truck.

```powerappsfl
// Bad code
ClearCollect(vartruckdata, AddColumns('Truck Details',
    "CITY",LookUp(Drivers, 'Truck Details'\[@'Dummy ID'\] = Drivers\[@'Truck Details'\],City),
        "FIRSTNAME",LookUp(Drivers, 'Truck Details'\[@'Dummy ID'\] = Drivers\[@'Truck Details'\],'Driver First Name'),
    "LASTNAME",LookUp(Drivers, 'Truck Details'\[@'Dummy ID'\] = Drivers\[@'Truck Details'\],'Driver Last Name'),
        "STATE",LookUp(Drivers, 'Truck Details'\[@'Dummy ID'\] = Drivers\[@'Truck Details'\],State)));
```

Performing such join in the canvas app can generate many calls to the data source, which leads to slow loading times.


A better approach is:

```powerappsfl
// Good code
Set(
    varTruckData,
    LookUp(
        Drivers,
        'Dummy ID' = ThisRecord.'Dummy ID',
        'Driver First Name'
    ) & LookUp(
        Drivers,
        'Dummy ID' = ThisRecord.'Dummy ID',
        'Driver Last Name'
        )
);

Set(
    varTruckData,
    With(
        {
            vDriver: LookUp(
                Drivers,
                'Dummy ID' = ThisRecord.'Dummy ID'
            )
        },
        vDriver.'Driver First Name' & vDriver.'Driver Last Name'
    )
)
```

In the real time scenario, you can reduce loading times from five minutes to under 10 seconds by fixing the data at the source.

### Server side processing

Different data sources, like SQL and Dataverse, let you delegate data processing, such as filters and lookups, to the data source. In SQL Server, you can create views defined by a query. In Dataverse, you can create low-code plugins to process data on the server and return only the final results to your canvas app.

Delegating data processing to the server can improve performance, reduce client-side code, and make your app easier to maintain.

Learn more about [plugins in Dataverse](/power-apps/maker/data-platform/low-code-plug-ins).

## Optimize query data patterns

### Use explicit column selection

The Explicit Column Selection (ECS) feature is on by default for all new apps. If it isn't on for your app, turn it on. ECS automatically reduces the number of columns retrieved to only those used in the app. If ECS isn't on, you might get more data than you need, which can affect performance. Sometimes, when an app gets data through collections, the original source of a column can be lost. ECS drops columns if it can't tell they're used. To force ECS to keep a missing column, use the PowerFx expression `ShowColumns` after a collection reference or in a control.

### Avoid calling Power Automate to populate a collection

A common practice is to use Power Automate to fetch and populate collections in Power Apps. While this approach is valid, there are situations where it might not be the most efficient choice. Calling Power Automate comes with an overhead of network latency and adds a 0.6-second performance cost to instantiate the Power Automate flow.

Overuse of Power Automate flows can also lead to execution limits and throttling. Therefore always evaluate the trade-offs between network latency and performance cost.

### Eliminate N+1 problem

The N+1 problem is a common issue in database queries where, instead of fetching all the required data in a single query, multiple extra queries are made to retrieve related data. This can lead to performance issues, as each extra query incurs overhead.

A simple call like this to load a collection can generate N+1 calls to data source.

```powerappsfl
ClearCollect(MyCollection, OrdersList,
    {
        LookUp(CustomersList,CustomerID = OrdersList[@CustomerID])
    }
)
```

In the context of canvas apps and galleries, the N+1 problem may arise when working with data sources and galleries that display related records. The issue typically occurs when more queries are made for each item displayed in the gallery, leading to a performance bottleneck.

Use View objects in SQL Server to avoid N+1 query problem, or change the user interface to avoid triggering the N+1 scenario.

Dataverse automatically fetches the required data of related tables and you can select the columns from related tables.

`ThisItem.Account.'Account Name'`

If `RelatedDataSourc`e` size is small (<500 records), you can cache it in a collection and use the collection to drive the Lookup (N+1) query scenario.

### Limiting the package size

Although Power Apps does a lot to optimize app loading, you can take steps to reduce the footprint of your apps. A reduced footprint is especially important for users of older devices, or users in locales where there's higher latency or reduced bandwidth.

- Evaluate the media that are embedded in your app. If something isn't used, delete it.

- Embedded images might be too large. Instead of PNG files, see whether you can use SVG images. However, be careful about using text in SVG images, because the font that's used will have to be installed on the client. A great workaround when you need to show text is to superimpose a text label over an image.

- Evaluate whether the resolution is appropriate for the form factor. The resolution for a mobile app doesn't need to be as high as the resolution for a desktop app. Experiment to get the right balance of image quality and size.

- If you have unused screens, delete them. Be careful not to delete any hidden screens that only app makers or administrators use.

- Evaluate whether you're trying to fit too many workflows into one app. For example, do you have both admin screens and client screens in the same app? If so, consider breaking them into individual apps. This approach will also make it easier for multiple people to work on the apps at the same time, and it limits the "blast radius" (amount of testing) when app changes require a full test pass.

## Optimize ForAll

The `ForAll` function in Power Apps is used to iterate through a table of records and apply a formula or set of formulas to each record. While the function itself is versatile, improper use of ForAll function can quickly make your app less performant.

ForAll function is singular sequential function instead of concurrent function. Therefore it looks at only one record at a time, gets the result, then continues to the next until it has gone through all records in its scope.

**Avoid Nesting ForAll at all cost.** This can lead to exponential iterations and significantly impact performance.

```powerappsfl
ClearCollect(FollowUpMeetingAttendees.ForAll(ForAll(Distinct(AttendeesList.EmailAddress.Address).Lookup(Attendees))))
```

### Batch updates to Database

ForAll + Patch can be one approach to Batch update the database. However, be careful in using the order of For All and Patch.

Following function:

```powerappsfl
Patch(SampleFoodSalesData, ForAll(colSampleFoodSales,
    {
        demoName:"fromCanvas2"
    })
);
```

Performs better than:

```powerappsfl
ForAll(colSampleFoodSales, Patch(SampleFoodSalesData,
    {
        demoName:"test"
    })
);
```

## Next step

> [!div class="nextstepaction"]
> [Error handling guidelines](error-handling.md)
