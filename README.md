# ElasticSearchCuratorScripts
Scripts to maintain elastic search cluster.

## Prerequisites
* For these scripts to work you must have Python 2.7 or later installed
* Additionally you need to have pip installed (comes with python 2.7.9 or later)
* You need to install the curator python modul `pip install elasticsearch-curator` [Other install options](https://www.elastic.co/guide/en/elasticsearch/client/curator/4.0/installation.html)

## Additional Documentation
These script is nother more than a convenient wrapper around Curator. For doing real things you can visit their documentation for more ideas or anything else you may want to do.

[Curator documentation](http://curator.readthedocs.io/en/4.0/)

## Usage

```
usage: deleteESIndices.py [-h] [-f DATEFORMAT] [-d DAYSTOKEEP]
                          clusterUrl prefix

Utility script for deleting indices from elastic search clusters

positional arguments:
  clusterUrl            Provide the elasticsearch url with credentials if
                        necessary e.g. http://<user>:<pass>@clusterurl<:port>
  prefix                Provide the index prefix you are cleaning up e.g.
                        .marvel-es-1-

optional arguments:
  -h, --help            show this help message and exit
  -f DATEFORMAT, --dateFormat DATEFORMAT
                        Enter the date format on your index
  -d DAYSTOKEEP, --daysToKeep DAYSTOKEEP
                        Enter the number of days you want to keep (default 90)
```



