---
title: Power Apps code readability
description: Learn about how to optimize code readability in Power Apps.
ms.date: 06/12/2024
ms.topic: concept-article
ms.subservice: guidance
ms.service: powerapps
author: robstand
ms.author: rachaudh
---

# Code readability

## Naming conventions

### General naming conventions

This section describes "camel case" and "Pascal case" naming conventions. If you're already familiar with those terms, you can skip ahead.

#### Camel case

You should use camel case for controls and variables. Camel case begins with a lowercase prefix, removes all spaces from object or variable names, and capitalizes the first letter of each word after the first. For example, a text input control might be named **txtUserEmailAddress**.

#### Pascal case

You should use Pascal case for data sources. Pascal case is sometimes referred to as "upper camel case." Like camel case, it removes all spaces and capitalizes the first letter of words. However, unlike camel case, Pascal case also capitalizes the first word. For example, a common data source in PowerApps is the Microsoft Office 365 Users connector, which is named Office365Users in your code.

### Screen names

Screen names should reflect the purpose of the screen, so that it's easier to navigate through complex apps in Power Apps Studio.

What's less obvious is that screen names are read aloud by screen readers, which are needed for users who have vision accessibility needs. Therefore, ***it's imperative that you use plain language to name your screens and that the names include spaces and no abbreviations***. Also, we recommend that you end the name with the word "Screen," so that the context is understood when the name is announced.

Here are some good examples:

- `Home_Screen` or `Home Screen`
- `Search_Screen` or `Search Screen`

![Screenshot that shows a list of screen names that follow the described pattern](media/image1.png)

These example screen names are less understandable:

- `Home`
- `LoaderScreen`
- `EmpProfDetails`
- `Thrive Help`

### Controls names

All control names on the canvas should use camel case. They should begin with a three-character type descriptor, followed by the purpose of control. This approach helps identify the type of control and makes it easier to build formulas and search. For example, `lblUserName` indicates that the control is a label.

The following table shows the abbreviations for common controls.

| **Control name**                      | **Abbreviation** |
|---------------------------------------|------------------|
| Badge                                 | bdg              |
| Button                                | btn              |
| Camera control                        | cam              |
| Canvas                                | can              |
| Card                                  | crd              |
| Charts                                | chr              |
| CheckBox                              | chk              |
| Collection                            | col              |
| Combo box                             | cmb              |
| Component                             | cmp              |
| Container                             | con              |
| Dates                                 | dte              |
| Drop down                             | drp              |
| Form                                  | frm              |
| Gallery                               | gal              |
| Group                                 | grp              |
| Header                                | hdr              |
| Html text                             | htm              |
| Icon                                  | ico              |
| Image                                 | img              |
| Info Button                           | info             |
| Label                                 | lbl              |
| Link                                  | lnk              |
| List box                              | lst              |
| Microphone                            | mic              |
| Microsoft Stream                      | str              |
| Page section shape                    | sec              |
| Pen Input                             | pen              |
| Power BI Tile                         | pbi              |
| Progress Bar                          | pbar             |
| Rating                                | rtg              |
| Rich text editor                      | rte              |
| Shapes (rectangle, circle, and so on) | shp              |
| Slider                                | sld              |
| Tab List                              | tbl              |
| Table                                 | tbl              |
| Text input                            | txt              |
| Timer                                 | tmr              |
| Toggle                                | tgl              |
| Video                                 | vid              |

Detailed list of controls and their properties are described in [Controls reference](/power-apps/maker/canvas-apps/reference-properties).

> [!NOTE]
> Control names must be unique across an application. If a control is reused on multiple screens, the short screen name should have a suffix. For example, `galBottomNavMenuHS`, where "HS" stands for "Home Screen." This approach makes it easier to reference the control in formulas across screens.

Here are some bad examples:

- `zipcode`
- `Next`

When you consistently name your controls, your app is cleaner in the navigation view, and your code is cleaner too.

![Screenshot of the navigation view showing control names following the pattern](media/image2.png)

### Data source names

When you add a data source to your application, the name can't be changed in the Power Apps app. The name is inherited from the source connector or data entities that are derived from the connection.

Here are some examples:

- **Name inherited from the source connector:** The Office 365 Users connector is namedOffice365Users in your code.
- **Data entities derived from the connection:** A Microsoft SharePoint list named `Employees` is returned from the SharePoint connector. Therefore, the name of the data source in your code is Employees. The same Power Apps app can also use ***the same SharePoint connector*** to access a SharePoint list named `Contractors`. In this case, the name of the data source in the code is `Contractors`.

For more information about connectors and connections, see [Overview of canvas app connectors for Power Apps](/powerapps/maker/canvas-apps/connections-list).

#### Standard action connectors

In Standard action connectors that expose functions, such as LinkedIn, the data source name and its operations use Pascal casing. For example, the LinkedIn data source is named LinkedIn and has an operation named `ListCompanies`.

```powerappsfl
ClearCollect(
    colCompanies,
    LinkedIn.ListCompanies()
)
```

#### Custom connectors

Custom connectors used to connect to custom application programming interfaces (APIs) such as  services or line-of-business APIs that your company has created. They can be created by any maker in your environment. We recommend Pascal casing for the data source name and its operations. Just be aware that the custom connector name and the way that it appears in PowerApps can differ.

Consider this example of a custom connector named `MS Auction Item Bid API`.

![Screenshot of a connector named MS Auction Item Bid API](media/image4.png)

But when you create a connection from this connector and add it to your PowerApps app as a data source, it appears as `AuctionItemBidAPI`.

![Screenshot of a connector showing that the name is AuctionItemBidAPI](media/image5.png)

To discover the reason, you can look inside the OpenAPI file for a title attribute that contains the text `Auction Item Bid API`.

```json
"info": {
    "version": "v1",
    "title": "Auction Item Bid API"
},
```

Power Apps removes all the spaces from this attribute value and uses it as the name of your data source.

> [!TIP]
> We recommend that you change the value of this attribute to a Pascal-cased name such as `AuctionItemBidAPI` and use it as the name of your custom connection. In that way, there will be no confusion. Change this value before you import the OpenAPI file to create the custom connector.
> [!NOTE]
> If you use the **Create from a blank** option instead of importing an existing OpenAPI file, PowerApps will prompt you for the custom connector name. This name will be used both as the name of the custom connector and as the value of the title attribute inside the OpenAPI file. Be sure to use a Pascal-cased name such as `AuctionItemBidAPI` to keep things consistent and simple.

#### Excel DataTables

PowerApps uses DataTables in Microsoft Excel to connect to data in Excel worksheets. Keep these points in mind when you create Excel documents as data sources:

- Give your DataTables descriptive names. The name is in the Power Apps app when you write the code to connect to it.
- Use one DataTable per worksheet.
- Give the same name to the DataTable and worksheet.
- Use descriptive column names in the DataTables.
- Use Pascal casing. Each word of the DataTable name should begin with a capital letter, such as `EmployeeLeaveRequests`.

### Variable names

Naming conventions for variables in canvas apps are important for maintaining readability, consistency, and clarity in your Power Apps projects. While no strict standard is enforced, adopting a consistent naming convention across your canvas app can make it easier for you and other collaborators to understand, use, and manage the variables.

- Use camel case, where the first letter of each word is capitalized except for the first word.
- Choose meaningful and descriptive names that clearly describe the purpose or content of the variable. Avoid overly generic names like temp or var1. Instead, use descriptive names like userEmail or totalAmount.
- Consider using prefixes or suffixes to indicate the type of variable. For instance:
  - `strUserName` for a text/string variable
  - `numTotalAmount` for a numeric variable
  - `boolIsEnabled` for a boolean variable
  - `locVarName` for local variables/context variables
  - `gblVarLoginUser` for global variables
- Decide whether your variables should be named in the singular or plural form and stick to that convention. For example, consistently use userCount or users.
- Avoid using reserved words or names that might conflict with Power Apps functions or keywords. Check the Power Apps documentation for a list of reserved words.
- Consider using prefixes that provide context about the variable's usage or scope. For example:
  - `frm` for form variables
  - `col` for collections
  - `var` for general-purpose variables
- Avoid special characters. Keep names alphanumeric and avoid special characters or spaces. Stick to letters and numbers.

Power Apps lets context variables and global variables share the same names. This can cause confusion because your formulas use context variables by default unless the [disambiguation operator](/powerapps/maker/canvas-apps/functions/operators#disambiguation-operator) is used.

Avoid this situation by following these conventions:

- Prefix context variables with `loc`.
- Prefix global variables with `gbl`.
- The name after the prefix should indicate the intent/purpose of the variable. Multiple words can be used and don't have to be separated by any special characters, such as spaces or underscores, if the first letter of each word is capitalized.
- Use Camel casing. Begin your variable names with a prefix in lowercase letters, and then capitalize the first letter of each word in the name.

These examples follow standards and conventions:

- **Global variable:** `gblFocusedBorderColor`

- **Context variable:** `locSuccessMessage`

- **Scope variable:** `scpRadius`

These examples don't follow the standards and are harder to understand:

- `dSub`
- `rstFlds`
- `hideNxtBtn`
- `ttlOppCt`
- `cFV`
- `cQId`

Avoid short and cryptic variable names such as EID. `Use EmployeeId` instead.

When there are many variables in an app, you can just type the prefix in the formula bar to see a list of the available variables. If you follow these guidelines to name your variables, you are able to find them easily in the formula bar as you develop your app. Ultimately, this approach leads to quicker app development.

### Collection names

- Be descriptive of the collection's contents. Think about what the collection contains and/or how it's used, and then name it accordingly.
- Collections should be prefixed with `col`.
- The name after the prefix should indicate the intent or purpose of the collection. Multiple words can be used and don't have to be separated by spaces or underscores, if the first letter of each word is capitalized.
- Use Camel casing. Begin your collection names with a lowercase col prefix, and then capitalize the first letter of each word in the name.

These examples follow the collection name conventions:

- `colMenuItems`
- `colThriveApps`

These examples don't follow the collection name conventions:

- `orderscoll`
- `tempCollection`

> [!TIP]
> When there are many collections in the app, you can just type the prefix in the formula bar to see a list of the available collections. As for variables, if you follow these guidelines to name your collections, you'll be able to find them very easily in the formula bar as you develop your app. Ultimately, this approach leads to quicker app development.

## Comments and documentation

As you write code for your application, emphasize the importance of comprehensive commenting. These comments not only serve as a helpful guide when you revisit the application months later but also extend a gesture of gratitude to the next developer who collaborates on the project.

There are two primary types of comments to enhance code clarity: Power Apps supports two comment styles: line comments, denoted by double forward slashes (`//`) for single-line remarks, and block comments enclosed within `/*` and `*/` for multi-line annotations.

### Line comments

Adding a double forward slash (`//`) to any line of code in PowerApps designates the rest of the line (including the `//`) as a comment.

Utilize line comments to elucidate the functionality of the subsequent code. They can also serve to temporarily disable a line of code, making them beneficial for testing purposes.

This example shows the use of line comments.

```powerappsfl
// ClearCollect function populates the Expenses2 collection with sample data
ClearCollect(
    Expenses2,
    // Entry 1: Client hosted meet and greet
    {
        Title: "Client hosted meet and greet:",
        ID: "4"
        // additional properties  
    }
)
```

### Block comments

Text enclosed within `/*` and `*/` is recognized as a block comment. Unlike line comments that apply to a single line, block comments can span multiple lines.

Block comments are useful for multiline explanations, such as documenting a code module header. They also facilitate temporarily disabling multiple lines of code during testing or debugging.

For optimal code organization, it's advisable to add comments after utilizing the Format Text feature. This is beneficial if your comments precede a code block.

```powerappsfl
/*
    Patch Operation to Insert Data:
    - Inserts a new employee record into the 'Employee' entity.
    - Adds corresponding department details to the 'Department' entity.
    Note: Ensure that foreign key relationships and dependencies are maintained for data integrity.
*/
Patch(
    Employee,
    Defaults(Employee),
    {
        FirstName: "John",
        LastName: "Doe",
        Position: "Software Developer"
    }
)
```

The Format Text feature follows these rules for existing comments:

1. If a property begins with a block comment, the next line of code will be appended to it.
1. If a property begins with a line comment, the next line of code won't be appended to it. Otherwise, the code is commented out.
1. Line and block comments elsewhere in the property will be appended to the previous line of code.

Don't worry about adding too many comments or comments that are too long. All comments are stripped out when PowerApps creates the client app package. Therefore, they won't affect the package size or slow down the app download or loading times.

### Modern app designer with comments

In Power Apps, it's considered the best practice for makers to effectively utilize commenting features within both Power Apps Studio and Modern app designer.

For optimal engagement in the Power Apps Studio, makers are advised to add comments using the following methods:

1. Right-click the ellipsis ("...") of any item in the Tree View.
2. Right-click a component in the canvas area.
3. Select the "Comments" button located on the command bar in the top right-hand corner of the screen.

When mentioning colleagues in comments, it's recommended to use the "@" symbol followed by their name. This prompts a notification email for the tagged colleague, ensuring swift access to the comment. In cases where a tagged user lacks access to the app, the maker is prompted to share the app with them.

![A screenshot of an expenses app showing a person @ mentioned in the comment](media/image9.png)

### Indentation and formatting

In Power Apps, indentation and formatting are crucial for maintaining a clear and organized structure in your app. Following best practices improve the readability of your formulas and controls.

#### Formula bar

##### Indentation

Although Power Apps doesn't enforce strict indentation, you can use spaces to visually separate different sections of your formulas. Press the space bar multiple times to create an indentation effect.

##### Line breaks

You can break long formulas into multiple lines to enhance readability. Press Enter to create a line break within the formula bar.

#### Use the Format text command

The "Format Text" command in the formula bar is designed to apply indentation, spacing, and line breaks to your Power Apps code. Utilize the "Format Text" command to establish a uniform coding style across your entire canvas app, ensuring a more efficient and error-resistant development process.

![Screenshot of Power Apps studio with the Format text command highlighted](media/image10.png)

## Next step

> [!div class="nextstepaction"]
> [Code optimization](code-optimization.md)
