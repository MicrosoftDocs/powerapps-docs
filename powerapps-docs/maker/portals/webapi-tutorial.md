---
title: Tutorial on how to use the portal Web API
description: This page walks you through example steps for performing read, write, update, and delete portal Web API requests.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/31/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: ndoelman
contributors:
  - neerajnandwana-msft
  - tapanm-msft
  - nickdoelman
---

# Tutorial: Use portal Web API

In this example, you will use the contact table with columns *firstname*, *lastname*, *fullname*, *emailaddress1*, and *telephone1*.

**NOTE:** You can change the column names, or use a different table, while following the steps in this example.

### Step 1 - Create site settings

Before you can use the portals Web API, you have to enable the required site settings with the Portal Management app. The site settings depend on the table that you want to use when interacting with the Web API.

1. Go to [Power Apps](https://make.powerapps.com/).

1. On the left pane, select **Apps**.

1. Select the **Portal Management** app.

    :::image type="content" source="media/read-operations/portal-management-app.png" alt-text="Launch Portal Management app." border="false":::

1. In the **Portal Management** app on the left pane, select **Site Settings**.

    :::image type="content" source="media/read-operations/site-settings.png" alt-text="Open site settings in Portal Management app." border="false":::

1. Select **New**.

1. In the **Name** box, enter **WebAPI/enableReadOperationPreview**.

1. In the **Website** list, select your website record.

1. In the **Value** box, enter **true**.

    :::image type="content" source="media/read-operations/enable-read.png" alt-text="Enable WebAPI read operation site setting. " border="true":::

1. Select **New**.

1. In the **Name** box, enter **Webapi/contact/enabled**.

1. In the **Website** list, select your website record.

1. In the **Value** box, enter **true**.

    :::image type="content" source="media/read-operations/enable-contact.png" alt-text="Enable contact table for WebAPI site setting. " border="false":::

1. Select **Save & Close**.

1. Select **New**.

1. In the **Name** box, enter **Webapi/contact/fields**.

1. In the **Website** list, select your website record.

1. In the **Value** box, enter  
 **firstname,lastname,fullname,emailaddress1,telephone1**

    :::image type="content" source="media/read-operations/contact-fields.png" alt-text="Enable Web API contact table fields site setting. " border="false":::

1. Select **Save & Close**.

1. Select **New**.

1. In the **Name** box, enter **Webapi/error/innererror**.

    :::image type="content" source="media/read-operations/inner-error.png" alt-text="Enable Web API inner error site setting. " border="false":::

1. In the **Website** list, select your website record.

1. In the **Value** box, enter **true**.

1. Select **Save & Close**.

1. Verify the site settings for **Web API**.

### Step 2 - Configure permissions

You'll have to configure permissions so that users are able to use the Web API feature. In this example, you'll enable the Contact table for table permissions, create a web role for using the Web API, add the table permissions for the Contact table to this web role, and then add the web role to users to allow them to use the Web API.

1. In the **Portal Management** app on the left pane, select **Table Permissions**.

1. Select **New**.

1. In the **Name** box, enter **Contact Table Permission**.

1. In the **Table Name** list, select **Contact (contact)**.

1. In the **Website** list, select your website record.

1. In the **Access Type** list, select **Global**.

1. Select **Read**, **Write**, **Create**, and **Delete** privileges.

1. Select **Save & Close**.

:::image type="content" source="media/read-operations/table-permissions.png" alt-text="Contact table permissions." border="false":::

1. On the left pane, select **Web Roles** .

1. Select **New**.

1. In the **Name** box, enter **Web API User**.

1. In the **Website** list, select your website record.

1. For **Authenticated Users Role**, select **Yes**.

    :::image type="content" source="media/read-operations/wepAPIuser-webrole.png" alt-text="Add Web API User web role." border="false":::

1. Select **Save**.

1. Select **Related** &gt; **Table Permissions**.

    :::image type="content" source="media/read-operations/related-table-permissions.png" alt-text="Add related table permissions to web role." border="true":::

1. Select **Add Existing Table Permission**.

1. Select **Contact Table Permission**, created earlier.

    :::image type="content" source="media/read-operations/select-table-permission.png" alt-text="Select contact table permission." border="false":::

1. Select **Add**.

1. Select **Save & Close**.

    :::image type="content" source="media/read-operations/table-permissions-view.png" alt-text="Table permissions view." border="false":::

1. On the left pane, select **Contacts**.

1. Select a contact that you want to use in this example for the Web API.

> [!NOTE]
> This contact is the user account used in this example for testing the Web API. Be sure to select the correct contact in your portal.

1. Select **Related** &gt; **Web Roles**.

    :::image type="content" source="media/read-operations/related-webroles.png" alt-text="Selecting related web roles." border="false":::

1. Select **Add Existing Web Role**.

1. Select the **Web API User** role, created earlier.

1. Select **Add**.

    :::image type="content" source="media/read-operations/webrole-view.png" alt-text="Web role associated view. " border="false":::

1. Select **Save & Close**.

### Step 3 - Create a webpage

Now that you've enabled the Web API and configured user permissions, create a webpage with sample code to view, edit, create, and delete records.

1. In the **Portal Management** app on the left pane, select **Web Pages**.

1. Select **New**.

1. In the **Name** box, enter **webapi**.

1. In the **Website** list, select your website record.

1. For **Parent Page**, select **Home**.

1. For **Partial URL**, enter **webapi**.

1. For **Page Template**, select **Home**.

1. For **Publishing State**, select **Published**.

1. Select **Save**.

    :::image type="content" source="media/web-api/webpage.png" alt-text="Web page." border="false":::

1. Select **Related** > **Web Pages**.

    :::image type="content" source="media/web-api/webpages-related.png" alt-text="Related Web Pages" border="false":::

1. From **Web Page Associated View**, select **webapi**.

    :::image type="content" source="media/web-api/webpage-associated-view.png" alt-text="Web Page Associated View." border="false":::

1. Scroll down to the **Content** section, and then go to **Copy (HTML)** (HTML designer).

    :::image type="content" source="media/web-api/copy-content.png" alt-text="Copy HTML content" border="false":::

1. Select the **HTML** tab.

    :::image type="content" source="media/web-api/select-html-tab.png" alt-text="Select the HTML tab" border="false":::

1. Copy the following sample code snippet and paste it in the HTML designer.

    ```html
        <!-- Sample code for Web API demonstration -->
    <style>
        #processingMsg {
            width: 150px;
            text-align: center;
            padding: 6px 10px;
            z-index: 9999;
            top: 0;
            left: 40%;
            position: fixed;
            -webkit-border-radius: 0 0 2px 2px;
            border-radius: 0 0 2px 2px;
            -webkit-box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            display: none;
        }
    
        table td[data-attribute] .glyphicon-pencil {
            margin-left: 5px;
            opacity: 0;
        }
    
        table td[data-attribute]:hover .glyphicon-pencil {
            opacity: 0.7;
        }
    </style>
    
    <script>
      $(function() {
        //Web API ajax wrapper
        (function(webapi, $) {
          function safeAjax(ajaxOptions) {
            var deferredAjax = $.Deferred();
            shell.getTokenDeferred().done(function(token) {
              // Add headers for ajax
              if (!ajaxOptions.headers) {
                $.extend(ajaxOptions, {
                  headers: {
                    "__RequestVerificationToken": token
                  }
                });
              } else {
                ajaxOptions.headers["__RequestVerificationToken"] = token;
              }
              $.ajax(ajaxOptions)
                .done(function(data, textStatus, jqXHR) {
                  validateLoginSession(data, textStatus, jqXHR, deferredAjax.resolve);
                }).fail(deferredAjax.reject); //ajax
            }).fail(function() {
              deferredAjax.rejectWith(this, arguments); // On token failure pass the token ajax and args
            });
            return deferredAjax.promise();
          }
          webapi.safeAjax = safeAjax;
        })(window.webapi = window.webapi || {}, jQuery)
        // Notification component
        var notificationMsg = (function() {
          var $processingMsgEl = $('#processingMsg'),
            _msg = 'Processing...',
            _stack = 0,
            _endTimeout;
          return {
            show: function(msg) {
              $processingMsgEl.text(msg || _msg);
              if (_stack === 0) {
                clearTimeout(_endTimeout);
                $processingMsgEl.show();
              }
              _stack++;
            },
            hide: function() {
              _stack--;
              if (_stack <= 0) {
                _stack = 0;
                clearTimeout(_endTimeout);
                _endTimeout = setTimeout(function() {
                  $processingMsgEl.hide();
                }, 500);
              }
            }
          }
        })();
        // Inline editable table component
        var webAPIExampleTable = (function() {
          var trTpl = '<% _.forEach(data, function(data){ %>' +
            '<tr data-id="<%=data.id%>" data-name="<%=data.fullname%>">' +
            '<% _.forEach(columns, function(col){ %>' +
            '<td data-attribute="<%=col.name%>" data-label="<%=col.label%>" data-value="<%=data[col.name]%>">' +
            '<%-data[col.name]%><i class="glyphicon glyphicon-pencil"></i>' +
            '</td>' +
            '<% }) %>' +
            '<td>' +
            '<button class="btn btn-default delete" type="submit"><i class="glyphicon glyphicon-trash" aria-hidden="true"></i></button>' +
            '</td>' +
            '</tr>' +
            '<% }) %>';
          var tableTpl = '<table class="table table-hover">' +
            '<thead>' +
            '<tr>' +
            '<% _.forEach(columns, function(col){ %>' +
            '<th><%=col.label%></th>' +
            '<% }) %>' +
            '<th>' +
            '<button class="btn btn-default add" type="submit">' +
            '<i class="glyphicon glyphicon-plus" aria-hidden="true"></i> Add Sample Record' +
            '</button>' +
            '</th>' +
            '</tr>' +
            '</thead>' +
            '<tbody>' + trTpl + '</tbody>' +
            '</table>';
          function getDataObject(rowEl) {
            var $rowEl = $(rowEl),
              attrObj = {
                id: $rowEl.attr('data-id'),
                name: $rowEl.attr('data-name')
              };
            $rowEl.find('td').each(function(i, el) {
              var $el = $(el),
                key = $el.attr('data-attribute');
              if (key) {
                attrObj[key] = $el.attr('data-value');
              }
            })
            return attrObj;
          }
          function bindRowEvents(tr, config) {
            var $row = $(tr),
              $deleteButton = $row.find('button.delete'),
              dataObj = getDataObject($row);
            $.each(config.columns, function(i, col) {
              var $el = $row.find('td[data-attribute="' + col.name + '"]');
              $el.on('click', $.proxy(col.handler, $el, col, dataObj));
            });
            //User can delete record using this button
            $deleteButton.on('click', $.proxy(config.deleteHandler, $row, dataObj));
          }
          function bindTableEvents($table, config) {
            $table.find('tbody tr').each(function(i, tr) {
              bindRowEvents(tr, config);
            });
            $table.find('thead button.add').on('click', $.proxy(config.addHandler, $table));
          }
          return function(config) {
            var me = this,
              columns = config.columns,
              addHandler = config.addHandler,
              deleteHandler = config.deleteHandler,
              $table;
            me.render = function(el) {
              $table = $(el).html(_.template(tableTpl)({
                columns: columns,
                data: me.data
              })).find('table');
              bindTableEvents($table, {
                columns: columns,
                addHandler: addHandler,
                deleteHandler: deleteHandler
              });
            }
            me.addRecord = function(record) {
              $table.find('tbody tr:first').before(_.template(trTpl)({
                columns: columns,
                data: [record]
              }));
              bindRowEvents($table.find('tbody tr:first'), config);
            }
            me.updateRecord = function(attributeName, newValue, record) {
              $table.find('tr[data-id="' + record.id + '"] td[data-attribute="' + attributeName + '"]').text(newValue);
            }
            me.removeRecord = function(record) {
              $table.find('tr[data-id="' + record.id + '"]').fadeTo("slow", 0.7, function() {
                $(this).remove();
              });
            }
          };
        })();
        //Applicaton ajax wrapper 
        function appAjax(processingMsg, ajaxOptions) {
          notificationMsg.show(processingMsg);
          return webapi.safeAjax(ajaxOptions)
            .fail(function(response) {
              if (response.responseJSON) {
                alert("Error: " + response.responseJSON.error.message)
              } else {
                alert("Error: Web API is not available... ")
              }
            }).always(notificationMsg.hide);
        }
        function loadRecords() {
          return appAjax('Loading...', {
            type: "GET",
            url: "/_api/contacts?$select=fullname,firstname,lastname,emailaddress1,telephone1",
            contentType: "application/json"
          });
        }
        function addSampleRecord() {
          //Sample data to create a record - change as appropriate
          var recordObj = {
            firstname: "Willie",
            lastname: "Huff" + _.random(100, 999),
            emailaddress1: "Willie.Huff@contoso.com",
            telephone1: "555-123-4567"
          };
          appAjax('Adding...', {
            type: "POST",
            url: "/_api/contacts",
            contentType: "application/json",
            data: JSON.stringify(recordObj),
            success: function(res, status, xhr) {
              recordObj.id = xhr.getResponseHeader("entityid");
              recordObj.fullname = recordObj.firstname + " " + recordObj.lastname;
              table.addRecord(recordObj);
            }
          });
          return false;
        }
        function deleteRecord(recordObj) {
          var response = confirm("Are you sure, you want to delete \"" + recordObj.name + "\" ?");
          if (response == true) {
            appAjax('Deleting...', {
              type: "DELETE",
              url: "/_api/contacts(" + recordObj.id + ")",
              contentType: "application/json",
              success: function(res) {
                table.removeRecord(recordObj);
              }
            });
          }
          return false;
        }
        function updateRecordAttribute(col, recordObj) {
          var attributeName = col.name,
            value = recordObj[attributeName],
            newValue = prompt("Please enter \"" + col.label + "\"", value);
          if (newValue != null && newValue !== value) {
            appAjax('Updating...', {
              type: "PUT",
              url: "/_api/contacts(" + recordObj.id + ")/" + attributeName,
              contentType: "application/json",
              data: JSON.stringify({
                "value": newValue
              }),
              success: function(res) {
                table.updateRecord(attributeName, newValue, recordObj);
              }
            });
          }
          return false;
        }
        var table = new webAPIExampleTable({
          columns: [{
            name: 'firstname',
            label: 'First Name',
            handler: updateRecordAttribute
          }, {
            name: 'lastname',
            label: 'Last Name',
            handler: updateRecordAttribute
          }, {
            name: 'emailaddress1',
            label: 'Email',
            handler: updateRecordAttribute
          }, {
            name: 'telephone1',
            label: 'Telephone',
            handler: updateRecordAttribute
          }],
          data: [],
          addHandler: addSampleRecord,
          deleteHandler: deleteRecord
        });
        loadRecords().done(function(data) {
          debugger;
          table.data = _.map(data.value, function(record){
            record.id = record.contactid;
            return record;
          });
          table.render($('#dataTable'));
        });
      });
    </script>
    <div id="processingMsg" class="alert alert-warning" role="alert"></div>
    <div id="dataTable"></div>
    ```

    :::image type="content" source="media/web-api/paste-code.png" alt-text="Paste code." border="false":::

1. Select **Save & Close**.

### Step 4 - Clear the portals cache

You've created a **webapi** sample page to test the Web API functionality. Before you get started, ensure that the Power Apps portals cache has been cleared so that the changes from the Portal Management app are reflected on your portal.

**IMPORTANT:** Clearing the portal server-side cache causes temporary performance degradation of the portal while data gets reloaded from Microsoft Dataverse.

**To clear the cache:**

1. Sign in to your portal as a member of the Administrators web role.

1. Change the URL by appending **/\_services/about** at the end. For example, if the portal URL is [https://contoso.powerappsportals.com](https://contoso.powerappsportals.com/), change it to <https://contoso.powerappsportals.com/_services/about>.

    :::image type="content" source="media/read-operations/clear-cache.png" alt-text="Clear the cache." border="false":::

**NOTE:** You must be a member of the **Administrators** web role to clear the cache. If you see a blank screen, check the web role assignments.

1. Select **Clear cache**.

More information: [Clear the server-side cache for a portal](admin/clear-server-side-cache.md)

### Step 5 - Use the Web API to read, view, edit, create, and delete

The sample webpage with the URL **webapi** created earlier in this example is now ready for testing.

To test the Web API functionality:

1. Sign in to your portal with the user account that has been assigned the **Web API User** role you created earlier.

1. Go to the **webapi** webpage created earlier. For example, *https://contoso.powerappsportals.com/webapi*. The WebAPI will retrieve records from Micrsoft Dataverse.

    :::image type="content" source="media/web-api/sample-page.png" alt-text="Sample webapi webpage." border="false":::

1. Select **Add Sample Record** to add the sample record from the script.

1. Select a field. In this example, we've selected **Email** to change the email address of a contact.

    :::image type="content" source="media/web-api/edit-record.png" alt-text="Edit email" border="false":::

1. Select :::image type="content" source="media/web-api/delete.png" alt-text="Delete button" border="false"::: to delete a record.

Now that you've created a webpage with a sample in this example to read, edit, create and delete records, you can customize the forms and layout.

## Next step

[Compose HTTP requests and handle errors](web-api-http-requests-handle-errors.md)

### See also

[Web API overview](web-api-overview.md)</br>
[Portals write, update and delete operations using the Web API](write-update-delete-operations.md)</br>
[Portals read operations using the Web API](read-operations.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
