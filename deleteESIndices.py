import elasticsearch
import curator
#import sys
import argparse

def main():


    parser = argparse.ArgumentParser(description='Utility script for deleting indices from elastic search clusters')
    parser.add_argument("clusterUrl", help="Provide the elasticsearch url with credentials if necessary e.g. http://<user>:<pass>@clusterurl<:port>")
    parser.add_argument("prefix", help="Provide the index prefix you are cleaning up e.g. .marvel-es-1-")
    parser.add_argument('-f', '--dateFormat', help='Enter the date format on your index', default="%Y.%m.%d")
    parser.add_argument('-d', '--daysToKeep', help="Enter the number of days you want to keep (default 90)", type=int, default=90)
    args = parser.parse_args()

    try:
        client = elasticsearch.Elasticsearch([args.clusterUrl])
        ilo = curator.IndexList(client)
        ilo.filter_by_regex(kind='prefix', value=args.prefix)
        ilo.filter_by_age(source='name', direction='older', timestring=args.dateFormat, unit='days', unit_count=args.daysToKeep)
        delete_indices = curator.DeleteIndices(ilo)
        delete_indices.do_action()
        print "Successfullly deleted indices"
    except curator.NoIndices:
        print "Nothing found meeting the criteria to delete, check your prefix name and that there are items to delete"

if __name__ == "__main__":
    #for debug purposes simulate args
    #sys.argv = ['deleteMarvelIndices.py', 'url', 'marvel-es-1-', '-d', '5']
    #sys.argv = ['-h']
    main()