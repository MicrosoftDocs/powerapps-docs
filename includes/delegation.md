## Delegation ##

When possible, PowerApps will delegate filter and sort operations to the data source and page through the results on demand.  For example, when starting an app that shows a **[Gallery](../controls/control-gallery.md)** control filled with data, only the first set of records will be initially brought to the device.  As the user scrolls, additional data will be brought down from the data source.  The result is a faster start time for the app and access to very large data sets.

However, delegation may not always be possible.  Data sources vary on what functions and operators they support while the PowerApps formula language is relatively rich.  If complete delegation of a formula is not possible, the authoring environment will flag the portion that cannot be delegated with a warning.  When possible, consider changing the formula to avoid functions and operators that cannot be delegated.   

PowerApps will delegate what it can, but will only pull down a small set of records to complete the work locally, at most 500 records.  Filter and sort functions will continue to operate, but with a reduced set of records.  What is available in the **[Gallery](../controls/control-gallery.md)** may not be the complete story which could be confusing to users.  Aggregate operations, such as **Sum** and **Average**, will operate on only a portion of the data source and therefore may not give the result that is expected.

Additional limitations on delegation (which we are working to remove):

- At this time, **LookUp** does not support delegation, but it will be coming soon.
- For **Sort**, the *Formula* argument can only be the name of a single column and cannot include other operators or functions.  The *SortOrder* argument has no limitations.
- For **Filter**, the formula can include =, <>, <, >, >=, <=, &&, ||, and **In** operators.  Only names of columns and values that do not depend on the data source can be used.  

