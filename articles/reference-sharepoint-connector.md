<properties
	pageTitle="Reference for SharePoint"
	description=""
	services="kratosapps"
	authors="aftowen"
 />
##SharePoint Connector

####This documentation is for version: v1
<div>Supported schemes:  http </div><h3> Description </h3> <div>Get Lists from SharePoint <br/> <br/><b>GET: /datasets('{dataset}')/tables </b> </div>


| Name| Type|Required|In|Default Value|Description|
| ---|---|---|---|---|---|
|dataSet|string|true|path| |SharePoint Site URL. The URL should be encoded (twice).|
<br/><div> <b> <h3> Response </h3> </b> </div>

|Name|Description|
|---|---|
|200|OK|
|default|Operation Failed.|
<br/><h3> Description </h3> <div>Get Items in a SharePoint List <br/> <br/><b>GET: /datasets('{dataset}')/tables('{table}')/items </b> </div>


| Name| Type|Required|In|Default Value|Description|
| ---|---|---|---|---|---|
|dataSet|string|true|path| |SharePoint Site URL. The URL should be encoded (twice).|
|table|string|true|path| |SharePoint List name from which items has to be fetched|
<br/><div> <b> <h3> Response </h3> </b> </div>

|Name|Description|
|---|---|
|200|OK|
|default|Operation Failed.|
<br/><h3> Description </h3> <div>Create an Item in SharePoint List <br/> <br/><b>POST: /datasets('{dataset}')/tables('{table}')/items </b> </div>


| Name| Type|Required|In|Default Value|Description|
| ---|---|---|---|---|---|
|dataSet|string|true|path| |SharePoint Site URL. The URL should be encoded (twice).|
|table|string|true|path| |SharePoint List name on which items has to be created|
|item| |true|body| |Item to Create|
<br/><div> <b> <h3> Response </h3> </b> </div>

|Name|Description|
|---|---|
|200|OK|
|default|Operation Failed.|
<br/><h3> Description </h3> <div>Get an Item from SharePoint List <br/> <br/><b>GET: /datasets('{dataset}')/tables('{table}')/items('{id}') </b> </div>


| Name| Type|Required|In|Default Value|Description|
| ---|---|---|---|---|---|
|dataSet|string|true|path| |SharePoint Site URL. The URL should be encoded (twice).|
|table|string|true|path| |SharePoint List name from which the item has to be fetched|
|id|string|true|path| |ID of Item to be fetched|
<br/><div> <b> <h3> Response </h3> </b> </div>

|Name|Description|
|---|---|
|200|OK|
|default|Operation Failed.|
<br/><h3> Description </h3> <div>Update an Item in SharePoint List <br/> <br/><b>PUT: /datasets('{dataset}')/tables('{table}')/items('{id}') </b> </div>


| Name| Type|Required|In|Default Value|Description|
| ---|---|---|---|---|---|
|dataSet|string|true|path| |SharePoint Site URL. The URL should be encoded (twice).|
|table|string|true|path| |SharePoint List name from which the item has to be updated|
|id|string|true|path| |ID of Item to be updated|
|item| |true|body| |Item to update|
<br/><div> <b> <h3> Response </h3> </b> </div>

|Name|Description|
|---|---|
|200|OK|
|default|Operation Failed.|
<br/><h3> Description </h3> <div>Delete an Item from SharePoint List <br/> <br/><b>DELETE: /datasets('{dataset}')/tables('{table}')/items('{id}') </b> </div>


| Name| Type|Required|In|Default Value|Description|
| ---|---|---|---|---|---|
|dataSet|string|true|path| |SharePoint Site URL. The URL should be encoded (twice).|
|table|string|true|path| |SharePoint List name from which the item has to be deleted|
|id|string|true|path| |ID of Item to be fetched|
<br/><div> <b> <h3> Response </h3> </b> </div>

|Name|Description|
|---|---|
|200|OK|
|default|Operation Failed.|
<br/><h3> Description </h3> <div>Get SharePoint List metadata <br/> <br/><b>GET: /$metadata.json/datasets/{dataSet}/tables/{table} </b> </div>


| Name| Type|Required|In|Default Value|Description|
| ---|---|---|---|---|---|
|dataSet|string|true|path| |SharePoint Site URL. The URL should be encoded (twice).|
|table|string|true|path| |SharePoint List name|
<br/><div> <b> <h3> Response </h3> </b> </div>

|Name|Description|
|---|---|
|200|OK|
|default|Operation Failed.|
<br/><h3> Description </h3> <div>Trigger for new items in a SharePoint List <br/> <br/><b>GET: /api/datasets/{dataSet}/Tables/{table}/OnNewItems </b> </div>


| Name| Type|Required|In|Default Value|Description|
| ---|---|---|---|---|---|
|dataSet|string|true|path| |SharePoint Site URL. The URL should be encoded (twice).|
|table|string|true|path| |SharePoint List name|
<br/><div> <b> <h3> Response </h3> </b> </div>

|Name|Description|
|---|---|
|200|OK|
|default|Operation Failed.|
<br/>
##Objects: 
<div> <b>TableMetadata</b>:undefined</div><div> Required properties for TableMetadata: </div><div> None of the properties are required. </div><div> All properties: </div>

| Name | Type | Description |
|---|---|---|
|Name|string||
|DisplayName|string||
|Permission|string||
|Schema|undefined||

<br/><div> <b>Object</b>:undefined</div><div> Required properties for Object: </div><div> None of the properties are required. </div><div> All properties: </div>

| Name | Type | Description |
|---|---|---|

<br/><div> <b>Table</b>:undefined</div><div> Required properties for Table: </div><div> None of the properties are required. </div><div> All properties: </div>

| Name | Type | Description |
|---|---|---|
|Name|string||
|DisplayName|string||

<br/><div> <b>Item</b>:undefined</div><div> Required properties for Item: </div><div> None of the properties are required. </div><div> All properties: </div>

| Name | Type | Description |
|---|---|---|
|ItemInternalId|string||
|DynamicProperties|object||

<br/>