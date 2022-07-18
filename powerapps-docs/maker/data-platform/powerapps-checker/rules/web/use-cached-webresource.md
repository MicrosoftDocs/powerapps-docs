# `use-cached-webresource`

Don't use a relative or absolute URL that retrieves a web resource from the server rather than from the cache. Web resource URLs should always be relative to ensure caching support. Additionally, don't include '/WebResources/' within the URL path as it will refer to the caller's default organization.
